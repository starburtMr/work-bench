import json
import tempfile
import unittest
from pathlib import Path

from scripts.work_bench_skeletons import (
    copy_skeleton,
    list_skeletons,
    register_skeleton,
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


if __name__ == "__main__":
    unittest.main()
