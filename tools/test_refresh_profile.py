"""Offline behavioral tests; no live checkout, API, auth, or user data writes."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock


spec = importlib.util.spec_from_file_location("refresh_profile", Path(__file__).with_name("refresh_profile.py"))
refresh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(refresh)


def repo(name="example", **changes):
    value = {"name": name, "owner": {"login": "tonydzi"}, "private": False,
             "fork": False, "archived": False, "html_url": "https://github.com/tonydzi/" + name,
             "description": "Public tool", "pushed_at": "2026-11-03T08:00:00Z"}
    value.update(changes)
    return value


def pull(**changes):
    value = {"__typename": "PullRequest", "title": "Fix a real failure", "state": "MERGED",
             "mergedAt": "2026-11-02T08:00:00Z", "url": "https://github.com/upstream/tool/pull/42",
             "author": {"login": "tonydzi"}, "repository": {
                 "nameWithOwner": "upstream/tool", "isPrivate": False, "owner": {"login": "upstream"}}}
    value.update(changes)
    return value


def search(items=None):
    items = [pull()] if items is None else items
    return {"data": {"search": {"issueCount": len(items), "nodes": items}}}


class RefreshTests(unittest.TestCase):
    def test_filters_private_and_forks_without_serializing_private_fields(self):
        own, counts = refresh.repositories({"login": "tonydzi", "public_repos": 2}, [[
            repo(), repo("fork", fork=True), {"private": True, "name": "PRIVATE-MARKER"}]])
        self.assertEqual([r["name"] for r in own], ["example"])
        self.assertEqual(counts["public_forks_excluded"], 1)
        self.assertNotIn("PRIVATE-MARKER", json.dumps((own, counts)))

    def test_owner_mismatch_refuses(self):
        with self.assertRaises(refresh.SourceError):
            refresh.repositories({"login": "tonydzi", "public_repos": 1}, [[repo(owner={"login": "someone"})]])

    def test_count_mismatch_refuses_partial_pagination(self):
        with self.assertRaises(refresh.SourceError):
            refresh.repositories({"login": "tonydzi", "public_repos": 2}, [[repo()]])

    def test_short_intermediate_page_refuses(self):
        with self.assertRaises(refresh.SourceError):
            refresh.repositories({"login": "tonydzi", "public_repos": 2}, [[repo()], [repo("second")]])

    def test_duplicate_repositories_refuse(self):
        with self.assertRaises(refresh.SourceError):
            refresh.repositories({"login": "tonydzi", "public_repos": 2}, [[repo(), repo()]])

    def test_100_item_page_and_last_page_are_complete(self):
        items = [repo("repo-%03d" % n) for n in range(101)]
        own, _ = refresh.repositories({"login": "tonydzi", "public_repos": 101}, [items[:100], items[100:]])
        self.assertEqual(len(own), 101)

    def test_unverified_visibility_refuses(self):
        with self.assertRaises(refresh.SourceError):
            refresh.repositories({"login": "tonydzi", "public_repos": 1}, [[repo(private="false")]])

    def test_malicious_markdown_is_text(self):
        text = refresh.markdown("a | [click](https://evil) <script>\n# title `code`")
        self.assertNotIn("<script>", text)
        self.assertNotIn("[click]", text)
        self.assertIn(r"\|", text)
        self.assertNotIn("\n", text)

    def test_bad_markers_fail(self):
        for text in ["missing", refresh.END + refresh.START, refresh.START * 2 + refresh.END]:
            with self.subTest(text=text), self.assertRaises(refresh.SourceError):
                refresh.markers(text)

    def test_graphql_errors_and_incomplete_sample_refuse(self):
        invalid = search()
        invalid["data"]["search"]["issueCount"] = 10
        for response in [{"errors": [{"message": "partial"}]}, invalid, {"data": None}]:
            with self.subTest(response=response), self.assertRaises(refresh.SourceError):
                refresh.contributions(response)

    def test_unmerged_private_self_or_wrong_author_refuses(self):
        for changes in [{"state": "OPEN"}, {"mergedAt": None}, {"author": {"login": "other"}},
                        {"repository": {"isPrivate": True}},
                        {"repository": {"isPrivate": False, "nameWithOwner": "tonydzi/tool"}}]:
            with self.subTest(changes=changes), self.assertRaises(refresh.SourceError):
                refresh.contributions(search([pull(**changes)]))

    def test_output_preserves_everything_outside_crlf_marker_block(self):
        before, after = "# Original\r\n", "\r\nHuman text\r\n"
        readme = before + refresh.START + "\r\nold\r\n" + refresh.END + after
        snap = refresh.snapshot_from_sources({"login": "tonydzi", "public_repos": 1}, [[repo()]], search(), "2026-11-03")
        rendered = refresh.outputs(readme, snap)["README.md"]
        self.assertTrue(rendered.startswith(before + refresh.START))
        self.assertTrue(rendered.endswith(refresh.END + after))
        self.assertIn("Merged status verified 2026-11-03 UTC", rendered)
        self.assertNotIn("**Recently updated merged contributions**", rendered)
        self.assertNotIn("lifetime total**", rendered)

    def test_profile_push_timestamp_cannot_create_a_refresh_loop(self):
        profile = {"login": "tonydzi", "public_repos": 2}
        before = [[repo("tonydzi", pushed_at="2026-11-03T08:00:00Z"), repo("another-tool")]]
        after = copy.deepcopy(before)
        after[0][0]["pushed_at"] = "2026-11-03T09:00:00Z"
        readme = refresh.START + "\nold\n" + refresh.END
        old = refresh.snapshot_from_sources(profile, before, search(), "2026-11-03")
        new = refresh.snapshot_from_sources(profile, after, search(), "2026-11-03")
        self.assertEqual(refresh.outputs(readme, old), refresh.outputs(readme, new))
        own_profile = next(r for r in new["repositories"] if r["name"] == "tonydzi")
        self.assertIsNone(own_profile["pushed_at"])
        self.assertEqual(own_profile["pushed_at_note"], "self timestamp excluded to avoid refresh loop")
        self.assertIn("self timestamp excluded to avoid refresh loop", refresh.outputs(readme, new)["docs/REPOSITORIES.md"])
        changed_other = copy.deepcopy(after)
        changed_other[0][1]["pushed_at"] = "2026-11-03T10:00:00Z"
        other_snapshot = refresh.snapshot_from_sources(profile, changed_other, search(), "2026-11-03")
        self.assertNotEqual(refresh.outputs(readme, new), refresh.outputs(readme, other_snapshot))

    def test_no_source_or_contract_error_writes_anything(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = refresh.START + "\nold\n" + refresh.END
            (root / "README.md").write_text(original, encoding="utf-8")
            fetch = mock.Mock(side_effect=refresh.SourceError("offline"))
            with self.assertRaises(refresh.SourceError):
                refresh.run(root, write=True, fetch=fetch)
            self.assertEqual((root / "README.md").read_text(), original)
            self.assertFalse((root / "docs").exists())
            (root / "README.md").write_text("no markers", encoding="utf-8")
            fetch.reset_mock()
            with self.assertRaises(refresh.SourceError):
                refresh.run(root, write=True, fetch=fetch)
            fetch.assert_not_called()

    def test_check_is_read_only_and_write_is_idempotent(self):
        responses = [{"login": "tonydzi", "public_repos": 1}, [[repo()]], search()]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(refresh.START + "\nold\n" + refresh.END, encoding="utf-8")
            result = refresh.run(root, fetch=mock.Mock(side_effect=copy.deepcopy(responses)), as_of="2026-11-03")
            self.assertEqual(result["outcome"], "drift")
            self.assertFalse((root / "docs").exists())
            result = refresh.run(root, write=True, fetch=mock.Mock(side_effect=copy.deepcopy(responses)), as_of="2026-11-03")
            self.assertEqual(result["outcome"], "written")
            self.assertEqual(set(result["changed"]), {"README.md", "docs/REPOSITORIES.md", "docs/profile-snapshot.json"})
            before = {p: p.stat().st_mtime_ns for p in root.rglob("*") if p.is_file()}
            result = refresh.run(root, write=True, fetch=mock.Mock(side_effect=copy.deepcopy(responses)), as_of="2026-11-03")
            self.assertEqual(result["outcome"], "current")
            self.assertEqual(result["changed"], [])
            self.assertEqual(before, {p: p.stat().st_mtime_ns for p in root.rglob("*") if p.is_file()})

    def test_source_failure_after_two_successful_calls_still_writes_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            original = refresh.START + "\nold\n" + refresh.END
            (root / "README.md").write_text(original, encoding="utf-8")
            fetch = mock.Mock(side_effect=[{"login": "tonydzi", "public_repos": 1}, [[repo()]], refresh.SourceError("search failed")])
            with self.assertRaises(refresh.SourceError):
                refresh.run(root, write=True, fetch=fetch)
            self.assertEqual((root / "README.md").read_text(), original)
            self.assertEqual(list(root.iterdir()), [root / "README.md"])


if __name__ == "__main__":
    unittest.main()
