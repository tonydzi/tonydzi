# Maintaining this profile

The profile has an editorial introduction, selected work and research links, plus three mechanically maintained surfaces: `PROFILE-ACTIVITY` in the README, `docs/REPOSITORIES.md`, and `docs/profile-snapshot.json`.

The existing writing workflow owns `BLOG-POST-LIST`; the metrics workflow owns `metrics.svg`. Keep those owners separate. Generic repository footers and full connector-kit catalogs should not be appended to a personal profile.

## Refresh

Requirements: Python 3.9+ and an authenticated GitHub CLI (`gh`). Authentication stays in the local GitHub CLI or environment; credentials are never written to the snapshot.

```sh
python3 tools/refresh_profile.py --check
python3 tools/refresh_profile.py --write
python3 -m unittest discover -s tools -p 'test_refresh_profile.py' -v
```

Check is the default and changes no files. Exit 0 means current, 1 means generated content differs, and 2 means the source or document contract could not be verified. Write mode updates only the named generated outputs. A source failure must leave the previous profile intact.

The repository catalog includes all own public source repositories and labels archived entries. It excludes forks and private repositories. The activity block counts **every** merged and open public pull request into other owners' repositories (all search pages, refused when the page total disagrees), excluding the operator's own organizations and awesome-/registry-list entries. It shows the totals, up to 12 merged projects (large vendors first) and up to 6 open pull requests, and links the full ledger. `.github/workflows/profile-refresh.yml` runs `--write` daily and commits only the three generated outputs.

The verification date advances when the public data is checked on a new day. A date-only diff is an evidence refresh, not new engineering work. Report those separately in the weekly receipt.

Output files are replaced atomically one at a time, not as a filesystem transaction. An I/O failure can leave a partial local refresh. Do not commit or publish after exit 2: inspect the error, recover the three outputs in a clean clone and rerun. API and marker errors are detected before any output write.

## Weekly acceptance

The operator's existing weekly routine calls this tool, reviews the editorial sections, checks the portfolio and continues the source-to-repository publication work. This tool does not copy private sources, create releases, commit, push or schedule itself.

Work from a clean clone, fetch the default branch first, inspect the exact diff, run tests and the publication privacy checks, and obtain independent review before pushing. Stage only named outputs. On concurrent remote changes, fetch and rebuild; never force-push.

After publication, read the default-branch SHA and public README back from GitHub. Record updated, current, blocked and unknown separately. Local generation and a successful scheduled invocation are not evidence that the public profile changed.

Provenance is recorded in Git commit trailers. This public runbook contains no machine names, credential paths or private source inventory.
