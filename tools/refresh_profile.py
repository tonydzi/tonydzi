#!/usr/bin/env python3
"""Refresh the public profile's evidence block and complete repository catalog.

Inputs: public GitHub REST/GraphQL responses via the authenticated ``gh`` CLI:
own repositories, and every merged and open upstream PR (paginated, counted in full).
Outputs: README's PROFILE-ACTIVITY block, docs/REPOSITORIES.md, and
docs/profile-snapshot.json. Everything outside that README block is preserved.
The profile repository's own push timestamp is excluded to prevent a refresh loop.
Caller: the existing weekly editorial routine, or a human running this module.
Rail: 0 LLM, Python 3.9+ standard library and the existing GitHub CLI login.
Break/fix: API/count/marker errors preserve existing artifacts; check the public
source and marker pair, then rerun. No commits, pushes, or scheduling happen here.
Usage counter: one JSON result on stdout for the caller's run ledger.
Provenance: authored with Codex; machine attribution belongs in the git commit.
"""

import argparse
from datetime import datetime, timezone
import html
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


OWNER = "tonydzi"
START = "<!-- PROFILE-ACTIVITY:START -->"
END = "<!-- PROFILE-ACTIVITY:END -->"
SELF_PUSH_NOTE = "self timestamp excluded to avoid refresh loop"
NAME = re.compile(r"[A-Za-z0-9_.-]+\Z")
SEARCH = "is:pr is:public author:tonydzi is:%s -user:tonydzi sort:updated-desc"
QUERY = """query ProfileRefresh($q: String!, $after: String) {
  search(query: $q, type: ISSUE, first: 100, after: $after) {
    issueCount
    pageInfo { hasNextPage endCursor }
    nodes {
      __typename
      ... on PullRequest {
        title url state mergedAt createdAt author { login }
        repository { nameWithOwner isPrivate owner { login } }
      }
    }
  }
}"""
# Not counted as upstream engineering: the operator's own lab organization and curated
# link lists (awesome-*, *registry*), whose merges are listings rather than code review.
OWN_ORGS = {"tonydzi", "palo-alto-ai-research-lab"}
CURATED = re.compile(r"awesome|registry", re.I)
# Owners whose identity GitHub itself proves; lower rank is listed first.
VENDORS = {"microsoft": 1, "google": 2, "google-gemini": 2, "chromedevtools": 2, "googleapis": 2,
           "anthropics": 3, "openai": 3, "nvidia": 4, "meta-llama": 4, "facebookresearch": 4,
           "aws": 4, "awslabs": 4, "huggingface": 5, "bytedance": 5, "qwenlm": 5,
           "ukgovernmentbeis": 5}
LEDGER = "https://tonydzi.github.io/contributions/"
SHOW_MERGED, SHOW_OPEN = 12, 6


class SourceError(ValueError):
    """A source or output contract could not be verified."""


def gh_json(*arguments):
    """Invoke gh without a shell; never echo auth-bearing process output."""
    try:
        result = subprocess.run(
            ["gh", "api", *arguments], capture_output=True, text=True,
            encoding="utf-8", timeout=120, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise SourceError("GitHub CLI unavailable or timed out; existing files preserved") from exc
    if result.returncode:
        raise SourceError("GitHub API call failed (exit %d); existing files preserved" % result.returncode)
    try:
        return json.loads(result.stdout)
    except (ValueError, TypeError) as exc:
        raise SourceError("GitHub returned malformed JSON; existing files preserved") from exc


def markdown(value):
    """Treat remote titles/descriptions as text, including HTML and table syntax."""
    text = html.escape(" ".join(str(value or "").split()), quote=False)
    return re.sub(r"([\\`*_[\]{}()#!|])", r"\\\1", text)


def timestamp(value, field, nullable=False):
    if nullable and value is None:
        return None
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", value):
        raise SourceError("Missing or invalid public timestamp: " + field)
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise SourceError("Invalid calendar timestamp: " + field) from exc
    return value


def markers(text):
    if text.count(START) != 1 or text.count(END) != 1:
        raise SourceError("README must contain exactly one PROFILE-ACTIVITY marker pair")
    begin, finish = text.index(START) + len(START), text.index(END)
    if begin > finish:
        raise SourceError("README PROFILE-ACTIVITY markers are reversed")
    return begin, finish


def repositories(profile, pages):
    if not isinstance(profile, dict) or str(profile.get("login", "")).casefold() != OWNER:
        raise SourceError("Public profile identity does not match " + OWNER)
    expected = profile.get("public_repos")
    if type(expected) is not int or expected < 0:
        raise SourceError("Public repository count is missing")
    if not isinstance(pages, list) or not pages or any(not isinstance(page, list) for page in pages):
        raise SourceError("Repository pagination must be a nonempty array of pages")
    if any(len(page) != 100 for page in pages[:-1]) or len(pages[-1]) > 100:
        raise SourceError("Repository pagination has an incomplete intermediate page")
    public = []
    seen = set()
    for item in [item for page in pages for item in page]:
        if not isinstance(item, dict) or type(item.get("private")) is not bool:
            raise SourceError("Repository visibility is unverified")
        if item["private"]:
            continue  # Do not copy, log, or serialize any private repository field.
        owner = item.get("owner")
        if not isinstance(owner, dict) or str(owner.get("login", "")).casefold() != OWNER:
            raise SourceError("Repository response contains a different owner")
        name = item.get("name")
        if not isinstance(name, str) or not NAME.fullmatch(name) or name.casefold() in seen:
            raise SourceError("Invalid or duplicate public repository name")
        seen.add(name.casefold())
        if item.get("html_url") != "https://github.com/%s/%s" % (OWNER, name):
            raise SourceError("Public repository URL does not match its identity")
        if type(item.get("fork")) is not bool or type(item.get("archived")) is not bool:
            raise SourceError("Public repository kind is unverified")
        description = item.get("description")
        if description is not None and not isinstance(description, str):
            raise SourceError("Public repository description has an unexpected shape")
        record = {
            "name": name, "url": item["html_url"], "description": description or "",
            "fork": item["fork"], "archived": item["archived"],
            "pushed_at": timestamp(item.get("pushed_at"), "pushed_at", nullable=True),
        }
        if name.casefold() == OWNER:
            record.update(pushed_at=None, pushed_at_note=SELF_PUSH_NOTE)
        public.append(record)
    if len(public) != expected:
        raise SourceError("Public repository count changed or pagination is partial (%d/%d)" % (len(public), expected))
    own = sorted((r for r in public if not r["fork"]), key=lambda r: r["name"].casefold())
    return own, {"public_repositories": expected, "public_forks_excluded": sum(r["fork"] for r in public)}


def contributions(pages, state="MERGED"):
    """Validate every page of one search; return all public upstream PRs in that state."""
    if not isinstance(pages, list) or not pages:
        raise SourceError("GraphQL contribution search returned no pages")
    nodes, total = [], None
    for response in pages:
        if not isinstance(response, dict) or response.get("errors"):
            raise SourceError("GraphQL contribution search returned errors")
        try:
            search = response["data"]["search"]
            count, page = search["issueCount"], search["nodes"]
        except (KeyError, TypeError) as exc:
            raise SourceError("GraphQL contribution search is incomplete") from exc
        if type(count) is not int or count < 0 or not isinstance(page, list) or (total is not None and count != total):
            raise SourceError("GraphQL contribution search changed while paginating")
        total = count
        nodes.extend(page)
    if len(nodes) != total:
        raise SourceError("GraphQL contribution search returned a partial sample (%d/%d)" % (len(nodes), total))
    result, seen = [], set()
    for item in nodes:
        if not isinstance(item, dict):
            raise SourceError("GraphQL contribution search contains an invalid node")
        repository, author = item.get("repository"), item.get("author")
        if item.get("__typename") != "PullRequest" or item.get("state") != state:
            raise SourceError("Contribution is not a verified %s pull request" % state.lower())
        if not isinstance(author, dict) or str(author.get("login", "")).casefold() != OWNER:
            raise SourceError("Contribution author is unverified")
        if not isinstance(repository, dict) or repository.get("isPrivate") is not False:
            raise SourceError("Contribution repository is not verified public")
        identity = repository.get("nameWithOwner", "")
        parts = identity.split("/") if isinstance(identity, str) else []
        if len(parts) != 2 or any(not NAME.fullmatch(p) for p in parts) or parts[0].casefold() == OWNER:
            raise SourceError("Contribution is not an upstream public repository")
        if not isinstance(repository.get("owner"), dict) or str(repository["owner"].get("login", "")).casefold() != parts[0].casefold():
            raise SourceError("Contribution repository ownership disagrees")
        url = item.get("url", "")
        if not isinstance(url, str) or not re.fullmatch(re.escape("https://github.com/" + identity + "/pull/") + r"[1-9]\d*", url) or url in seen:
            raise SourceError("Contribution URL is invalid or duplicated")
        title = item.get("title")
        if not isinstance(title, str) or not title.strip():
            raise SourceError("Contribution title is missing")
        seen.add(url)
        if parts[0].casefold() in OWN_ORGS or CURATED.search(identity):
            continue
        record = {"repository": identity, "title": title, "url": url,
                  "created_at": timestamp(item.get("createdAt"), "createdAt")}
        if state == "MERGED":
            record["merged_at"] = timestamp(item.get("mergedAt"), "mergedAt")
        result.append(record)
    return result


def rank(identity):
    return VENDORS.get(identity.split("/")[0].casefold(), 99)


def summary(merged, opened):
    """Counts plus the short lists the README shows: large vendors first, then recency."""
    by_repo = {}
    for pr in merged:
        entry = by_repo.setdefault(pr["repository"], {"repository": pr["repository"], "merged": 0, "last": ""})
        entry["merged"] += 1
        entry["last"] = max(entry["last"], pr["merged_at"][:10])
    projects = sorted(by_repo.values(), key=lambda e: (e["last"], e["repository"].casefold()), reverse=True)
    projects.sort(key=lambda e: rank(e["repository"]))
    pending = sorted(opened, key=lambda p: (p["created_at"], p["url"]), reverse=True)
    pending.sort(key=lambda p: rank(p["repository"]))
    return {"merged": len(merged), "merged_projects": len(by_repo),
            "large_vendor_projects": sum(rank(r) < 99 for r in by_repo),
            "open": len(opened), "open_projects": len({p["repository"] for p in opened}),
            "projects": projects[:SHOW_MERGED], "in_review": pending[:SHOW_OPEN]}


def snapshot_from_sources(profile, pages, merged, opened, as_of):
    own, counts = repositories(profile, pages)
    return {
        "schema": "public-profile-snapshot/v1", "owner": OWNER, "as_of_utc": as_of,
        "source": "GitHub public REST repositories and GraphQL merged/open PR search",
        "scope": {**counts, "own_public_non_fork": len(own),
                  "own_archived": sum(r["archived"] for r in own)},
        "repositories": own,
        "upstream_pull_requests": summary(contributions(merged, "MERGED"), contributions(opened, "OPEN")),
    }


def outputs(readme, snapshot):
    begin, finish = markers(readme)
    date = snapshot["as_of_utc"]
    up = snapshot["upstream_pull_requests"]
    activity = ["Live from the GitHub API, verified %s UTC. Own repositories and awesome-/registry-list entries are not counted." % date, "",
                "**%d pull requests merged into %d upstream projects** (%d of them at large tech companies and labs) \u00b7 **%d more open in review** across %d projects \u00b7 [full list with live status](%s)" % (
                    up["merged"], up["merged_projects"], up["large_vendor_projects"], up["open"], up["open_projects"], LEDGER),
                "", "Merged, large vendors first:", ""]
    for e in up["projects"]:
        activity.append("- **%s**: [%d merged](https://github.com/%s/pulls?q=is%%3Apr+is%%3Amerged+author%%3A%s), last %s." % (
            markdown(e["repository"]), e["merged"], e["repository"], OWNER, e["last"]))
    if not up["projects"]:
        activity.append("No matching public merged contributions were returned by GitHub.")
    activity += ["", "In review now:", ""]
    for pr in up["in_review"]:
        activity.append("- **%s**: [%s](%s), opened %s." % (
            markdown(pr["repository"]), markdown(pr["title"]), pr["url"], pr["created_at"][:10]))
    if not up["in_review"]:
        activity.append("No open upstream pull requests right now.")
    newline = "\r\n" if "\r\n" in readme else "\n"
    refreshed = readme[:begin] + newline + newline.join(activity) + newline + readme[finish:]
    scope = snapshot["scope"]
    catalog = ["# Public repository catalog", "",
               "Generated by `tools/refresh_profile.py` from the GitHub API on **%s UTC**." % date, "",
               "%d own public repositories, including %d archived. %d public forks are excluded; private repositories are never published here." % (
                   scope["own_public_non_fork"], scope["own_archived"], scope["public_forks_excluded"]),
               "", "Repository dates are GitHub `pushed_at`, not proof of a release, meaningful work, deployment, or production health.", "",
               "| Repository | Purpose from its public description | State | Last push (UTC) |",
               "|---|---|---|---|"]
    for repo in snapshot["repositories"]:
        push_display = repo.get("pushed_at_note") or (repo["pushed_at"] or "Unknown")[:10]
        catalog.append("| [%s](%s) | %s | %s | %s |" % (
            markdown(repo["name"]), repo["url"], markdown(repo["description"]) or "No public description",
            "Archived" if repo["archived"] else "Not archived", push_display))
    catalog.extend(["", "Sources: [public repository API](https://api.github.com/users/tonydzi/repos?per_page=100&type=owner) and [profile](https://github.com/tonydzi).",
                    "The companion `profile-snapshot.json` contains only selected public fields.", ""])
    return {"README.md": refreshed, "docs/REPOSITORIES.md": "\n".join(catalog),
            "docs/profile-snapshot.json": json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n"}


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="wb", dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(text.encode("utf-8"))
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def search_pages(fetch, state, limit=10):
    """Follow GraphQL cursors; GitHub search caps at 1000 results (10 pages)."""
    pages, after = [], None
    for _ in range(limit):
        args = ["graphql", "-f", "query=" + QUERY, "-f", "q=" + SEARCH % state]
        if after:
            args += ["-f", "after=" + after]
        page = fetch(*args)
        pages.append(page)
        try:
            info = page["data"]["search"]["pageInfo"]
        except (KeyError, TypeError):
            return pages  # contributions() reports the malformed page
        if not isinstance(info, dict) or not info.get("hasNextPage"):
            return pages
        after = info.get("endCursor")
        if not isinstance(after, str) or not after:
            raise SourceError("GraphQL pagination cursor is missing")
    raise SourceError("More than %d pages of %s pull requests" % (limit, state))


def run(root, write=False, fetch=gh_json, as_of=None):
    root = Path(root).resolve()
    readme = (root / "README.md").read_bytes().decode("utf-8")
    markers(readme)  # Refuse invalid output contracts before spending API requests.
    as_of = as_of or datetime.now(timezone.utc).date().isoformat()
    profile = fetch("users/" + OWNER)
    pages = fetch("users/%s/repos?per_page=100&type=owner&sort=full_name" % OWNER, "--paginate", "--slurp")
    merged, opened = search_pages(fetch, "merged"), search_pages(fetch, "open")
    snapshot = snapshot_from_sources(profile, pages, merged, opened, as_of)
    planned = outputs(readme, snapshot)  # All sources validated before any write.
    changed = []
    for name, content in planned.items():
        path = root / name
        if not path.parent.resolve().is_relative_to(root) or path.is_symlink():
            raise SourceError("Output path escapes the checkout or is a symbolic link")
        if not path.exists() or path.read_bytes() != content.encode("utf-8"):
            changed.append(name)
    if write:
        for name in changed:
            atomic_write(root / name, planned[name])
    return {"event": "profile.refresh", "outcome": "written" if write and changed else "drift" if changed else "current",
            "as_of_utc": as_of, "own_public_non_fork": snapshot["scope"]["own_public_non_fork"],
            "changed": changed, "write": write}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="report drift without writes (default)")
    mode.add_argument("--write", action="store_true", help="write only the three documented outputs")
    args = parser.parse_args(argv)
    try:
        result = run(args.root, write=args.write)
    except (SourceError, OSError, UnicodeError) as exc:
        print(json.dumps({"event": "profile.refresh", "outcome": "error", "error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 1 if result["changed"] and not args.write else 0


if __name__ == "__main__":
    sys.exit(main())
