import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.work_bench_skeletons import (
    ChangeRequest,
    UpstreamConfig,
    apply_change,
    branch_name,
    copy_skeleton,
    execute_change_pr,
    load_upstream_config,
    list_skeletons,
    register_skeleton,
    validate_change_request,
)


class WorkBenchSkeletonTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.plugin_root = self.root / "plugin"
        self.user_root = self.root / "user"

    def tearDown(self):
        self.tmp.cleanup()

    def make_skeleton(self, root, kind, name, description="Reusable skeleton"):
        path = root / kind / "apps" / name
        path.mkdir(parents=True)
        (path / "README.md").write_text(f"# {name}\n\n{description}\n", encoding="utf-8")
        return path

    def make_index(self, root, kind):
        path = root / kind / "README.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "\n".join(
                [
                    f"# {kind.title()} Skeleton Index",
                    "",
                    "## Candidates",
                    "",
                    "| Candidate | Stack | Best for | Poor fit for | Local guidance | Verification entry points |",
                    "| --- | --- | --- | --- | --- | --- |",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        return path

    def test_lists_user_and_builtin_skeletons(self):
        self.make_skeleton(self.plugin_root, "frontend", "react-spa")
        self.make_skeleton(self.user_root, "frontend", "custom-spa")

        candidates = list_skeletons(
            kind="frontend",
            plugin_root=self.plugin_root,
            user_root=self.user_root,
        )

        names = {(item.name, item.source) for item in candidates}
        self.assertEqual(
            names,
            {
                ("custom-spa", "user-global"),
                ("react-spa", "plugin-builtin"),
            },
        )

    def test_user_skeleton_wins_name_collision(self):
        self.make_skeleton(self.plugin_root, "backend", "api-kit", "builtin")
        self.make_skeleton(self.user_root, "backend", "api-kit", "user")

        candidates = list_skeletons(
            kind="backend",
            plugin_root=self.plugin_root,
            user_root=self.user_root,
        )

        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0].name, "api-kit")
        self.assertEqual(candidates[0].source, "user-global")
        self.assertIn("user", candidates[0].description)

    def test_missing_user_directories_are_empty(self):
        self.make_skeleton(self.plugin_root, "frontend", "react-spa")

        candidates = list_skeletons(
            kind="frontend",
            plugin_root=self.plugin_root,
            user_root=self.user_root,
        )

        self.assertEqual([item.name for item in candidates], ["react-spa"])

    def test_register_copies_to_user_library_and_updates_registry(self):
        source = self.root / "source"
        source.mkdir()
        (source / "README.md").write_text("# candidate\n\nRegistered skeleton\n", encoding="utf-8")

        candidate = register_skeleton(
            kind="frontend",
            name="registered-spa",
            source_dir=source,
            user_root=self.user_root,
            stack=["React"],
        )

        self.assertEqual(candidate.source, "user-global")
        self.assertTrue((self.user_root / "frontend" / "apps" / "registered-spa" / "README.md").exists())

        registry_path = self.user_root / "registry" / "frontend-skeletons.json"
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        self.assertEqual(registry["skeletons"][0]["name"], "registered-spa")
        self.assertEqual(registry["skeletons"][0]["stack"], ["React"])

    def test_copy_refuses_non_empty_target_without_overwrite(self):
        self.make_skeleton(self.plugin_root, "backend", "api-kit")
        target = self.root / "target"
        target.mkdir()
        (target / "keep.txt").write_text("do not replace", encoding="utf-8")

        with self.assertRaises(FileExistsError):
            copy_skeleton(
                kind="backend",
                name="api-kit",
                target=target,
                plugin_root=self.plugin_root,
                user_root=self.user_root,
            )

    def test_copy_allows_empty_existing_target(self):
        self.make_skeleton(self.plugin_root, "frontend", "react-spa")
        target = self.root / "target"
        target.mkdir()

        candidate = copy_skeleton(
            kind="frontend",
            name="react-spa",
            target=target,
            plugin_root=self.plugin_root,
            user_root=self.user_root,
        )

        self.assertEqual(candidate.source, "plugin-builtin")
        self.assertTrue((target / "README.md").exists())

    def test_copy_uses_user_global_when_names_collide(self):
        self.make_skeleton(self.plugin_root, "backend", "api-kit", "builtin")
        self.make_skeleton(self.user_root, "backend", "api-kit", "user")
        target = self.root / "target"

        candidate = copy_skeleton(
            kind="backend",
            name="api-kit",
            target=target,
            plugin_root=self.plugin_root,
            user_root=self.user_root,
        )

        self.assertEqual(candidate.source, "user-global")
        self.assertIn("user", (target / "README.md").read_text(encoding="utf-8"))

    def test_upstream_config_precedence(self):
        config_dir = self.root / "config"
        config_dir.mkdir()
        config = config_dir / "config.json"
        config.write_text(
            json.dumps(
                {
                    "upstream": {
                        "repo": "from/config",
                        "install_ref": "develop",
                        "inbox_branch": "inbox",
                        "repo_dir": str(self.root / "repo-from-config"),
                    }
                }
            ),
            encoding="utf-8",
        )

        resolved = load_upstream_config(path=config)
        self.assertEqual(resolved.repo, "from/config")
        self.assertEqual(resolved.install_ref, "develop")
        self.assertEqual(resolved.inbox_branch, "inbox")

        overridden = load_upstream_config(repo="from/flag", inbox_branch="flag-inbox", path=config)
        self.assertEqual(overridden.repo, "from/flag")
        self.assertEqual(overridden.install_ref, "develop")
        self.assertEqual(overridden.inbox_branch, "flag-inbox")

    def test_branch_name_includes_change_type_kind_and_name(self):
        self.assertEqual(
            branch_name(ChangeRequest(change_type="add", kind="frontend", name="react-admin")),
            "skeleton/add-frontend-react-admin",
        )
        self.assertEqual(
            branch_name(
                ChangeRequest(
                    change_type="rename",
                    kind="backend",
                    name="old-api",
                    new_name="new-api",
                )
            ),
            "skeleton/rename-backend-old-api-to-new-api",
        )

    def test_validate_rejects_invalid_names_and_generated_dirs(self):
        source = self.make_skeleton(self.root, "frontend", "source")
        (source / "node_modules").mkdir()

        result = validate_change_request(
            ChangeRequest(
                change_type="add",
                kind="frontend",
                name="React_Admin",
                source=source,
            ),
            self.plugin_root,
        )

        self.assertFalse(result.ok)
        self.assertTrue(any("Invalid skeleton name" in error for error in result.errors))
        self.assertTrue(any("generated directories" in error for error in result.errors))

    def test_validate_rejects_secret_like_source(self):
        source = self.make_skeleton(self.root, "backend", "source")
        (source / ".env").write_text("API_KEY=sk_live_1234567890abcdef\n", encoding="utf-8")

        result = validate_change_request(
            ChangeRequest(
                change_type="add",
                kind="backend",
                name="api-kit",
                source=source,
            ),
            self.plugin_root,
        )

        self.assertFalse(result.ok)
        self.assertTrue(any("secret-like" in error for error in result.errors))

    def test_validate_rejects_secret_like_content_outside_env_files(self):
        source = self.make_skeleton(self.root, "backend", "source")
        (source / "config.txt").write_text("API_KEY=sk_live_1234567890abcdef\n", encoding="utf-8")

        result = validate_change_request(
            ChangeRequest(
                change_type="add",
                kind="backend",
                name="api-kit",
                source=source,
            ),
            self.plugin_root,
        )

        self.assertFalse(result.ok)
        self.assertTrue(any("config.txt" in error for error in result.errors))

    def test_validate_warns_for_missing_optional_docs(self):
        source = self.root / "plain-source"
        source.mkdir()
        (source / "README.md").write_text("# plain\n\nPlain skeleton\n", encoding="utf-8")

        result = validate_change_request(
            ChangeRequest(
                change_type="add",
                kind="frontend",
                name="plain-source",
                source=source,
            ),
            self.plugin_root,
        )

        self.assertTrue(result.ok)
        self.assertIn("缺少 AGENTS.md", result.warnings)
        self.assertIn("缺少 docs/", result.warnings)

    def test_apply_add_update_remove_and_rename_changes_indexes(self):
        self.make_index(self.plugin_root, "frontend")
        source = self.make_skeleton(self.root, "frontend", "source", "React 管理后台骨架")
        (source / "package.json").write_text(
            json.dumps({"dependencies": {"react": "1", "typescript": "1"}, "scripts": {"test": "vitest"}}),
            encoding="utf-8",
        )

        apply_change(
            ChangeRequest(change_type="add", kind="frontend", name="react-admin", source=source),
            self.plugin_root,
        )
        index_text = (self.plugin_root / "frontend" / "README.md").read_text(encoding="utf-8")
        self.assertIn("apps/react-admin", index_text)
        self.assertTrue((self.plugin_root / "frontend" / "apps" / "react-admin" / "README.md").exists())

        updated = self.make_skeleton(self.root, "frontend", "updated", "更新后的中文说明")
        (updated / "extra.txt").write_text("updated", encoding="utf-8")
        apply_change(
            ChangeRequest(change_type="update", kind="frontend", name="react-admin", source=updated),
            self.plugin_root,
        )
        self.assertTrue((self.plugin_root / "frontend" / "apps" / "react-admin" / "extra.txt").exists())

        renamed = self.make_skeleton(self.root, "frontend", "renamed", "重命名后的骨架")
        apply_change(
            ChangeRequest(
                change_type="rename",
                kind="frontend",
                name="react-admin",
                source=renamed,
                new_name="react-admin-new",
            ),
            self.plugin_root,
        )
        index_text = (self.plugin_root / "frontend" / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("apps/react-admin)", index_text)
        self.assertIn("apps/react-admin-new", index_text)

        apply_change(
            ChangeRequest(change_type="remove", kind="frontend", name="react-admin-new"),
            self.plugin_root,
        )
        index_text = (self.plugin_root / "frontend" / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("apps/react-admin-new", index_text)

    def test_apply_docs_only_does_not_replace_runtime_files(self):
        self.make_index(self.plugin_root, "backend")
        target = self.make_skeleton(self.plugin_root, "backend", "api-kit", "Old docs")
        (target / "src").mkdir()
        (target / "src" / "main.ts").write_text("runtime", encoding="utf-8")
        source = self.make_skeleton(self.root, "backend", "api-docs", "New docs")
        (source / "docs").mkdir()
        (source / "docs" / "testing.md").write_text("# Testing\n", encoding="utf-8")

        apply_change(
            ChangeRequest(change_type="docs", kind="backend", name="api-kit", source=source),
            self.plugin_root,
        )

        self.assertEqual((target / "src" / "main.ts").read_text(encoding="utf-8"), "runtime")
        self.assertIn("New docs", (target / "README.md").read_text(encoding="utf-8"))
        self.assertTrue((target / "docs" / "testing.md").exists())

    def test_change_pr_dry_run_does_not_push_or_create_pr(self):
        repo = self.root / "repo"
        repo.mkdir()
        self.make_index(repo, "frontend")
        source = self.make_skeleton(self.root, "frontend", "dry-source", "Dry run skeleton")
        calls = []

        def fake_runner(command, cwd=None):
            calls.append(command)
            if command[:3] == ["git", "status", "--porcelain"]:
                produced = repo / "frontend" / "apps" / "dry-source"
                stdout = " M frontend/README.md\n" if produced.exists() else ""
                return subprocess.CompletedProcess(command, 0, stdout=stdout, stderr="")
            if command[:3] == ["git", "ls-remote", "--heads"]:
                return subprocess.CompletedProcess(command, 0, stdout="", stderr="")
            return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

        result = execute_change_pr(
            change=ChangeRequest(
                change_type="add",
                kind="frontend",
                name="dry-source",
                source=source,
            ),
            config=UpstreamConfig(
                repo="owner/repo",
                install_ref="main",
                inbox_branch="skeleton-inbox",
                repo_dir=repo,
            ),
            dry_run=True,
            runner=fake_runner,
        )

        flat_calls = [" ".join(command) for command in calls]
        self.assertEqual(result.branch, "skeleton/add-frontend-dry-source")
        self.assertFalse(any("push" in call for call in flat_calls))
        self.assertFalse(any("pr create" in call for call in flat_calls))

    def test_change_pr_checks_auth_and_uses_non_force_push(self):
        repo = self.root / "repo"
        repo.mkdir()
        self.make_index(repo, "frontend")
        source = self.make_skeleton(self.root, "frontend", "live-source", "Live run skeleton")
        calls = []

        def fake_runner(command, cwd=None):
            calls.append(command)
            if command[:3] == ["git", "status", "--porcelain"]:
                produced = repo / "frontend" / "apps" / "live-source"
                stdout = " M frontend/README.md\n?? frontend/apps/live-source/\n" if produced.exists() else ""
                return subprocess.CompletedProcess(command, 0, stdout=stdout, stderr="")
            if command[:3] == ["git", "ls-remote", "--heads"]:
                return subprocess.CompletedProcess(command, 0, stdout="abc\trefs/heads/skeleton-inbox\n", stderr="")
            if command[:3] == ["git", "rev-parse", "--short"]:
                return subprocess.CompletedProcess(command, 0, stdout="abc123\n", stderr="")
            if command[:3] == ["gh", "pr", "create"]:
                return subprocess.CompletedProcess(command, 0, stdout="https://github.com/owner/repo/pull/1\n", stderr="")
            return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

        result = execute_change_pr(
            change=ChangeRequest(
                change_type="add",
                kind="frontend",
                name="live-source",
                source=source,
            ),
            config=UpstreamConfig(
                repo="owner/repo",
                install_ref="main",
                inbox_branch="skeleton-inbox",
                repo_dir=repo,
            ),
            runner=fake_runner,
        )

        flat_calls = [" ".join(command) for command in calls]
        self.assertEqual(result.commit, "abc123")
        self.assertIn("gh auth status --hostname github.com", flat_calls)
        push_calls = [command for command in calls if command[:2] == ["git", "push"]]
        self.assertEqual(push_calls, [["git", "push", "-u", "origin", "skeleton/add-frontend-live-source"]])


if __name__ == "__main__":
    unittest.main()
