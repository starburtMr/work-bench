#!/usr/bin/env python3
"""Manage work-bench frontend/backend skeleton libraries."""

from __future__ import annotations

import argparse
import json
import os
import shutil
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

KINDS = ("frontend", "backend")
SOURCE_USER = "user-global"
SOURCE_BUILTIN = "plugin-builtin"


@dataclass(frozen=True)
class SkeletonCandidate:
    name: str
    kind: str
    source: str
    path: str
    stack: list[str]
    description: str


def plugin_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()


def default_user_root() -> Path:
    return codex_home() / "work-bench"


def apps_dir(root: Path, kind: str, source: str) -> Path:
    if kind not in KINDS:
        raise ValueError(f"Unsupported skeleton kind: {kind}")
    if source == SOURCE_USER:
        return root / kind / "apps"
    if source == SOURCE_BUILTIN:
        return root / kind / "apps"
    raise ValueError(f"Unsupported skeleton source: {source}")


def registry_path(user_root: Path, kind: str) -> Path:
    if kind not in KINDS:
        raise ValueError(f"Unsupported skeleton kind: {kind}")
    return user_root / "registry" / f"{kind}-skeletons.json"


def load_registry(user_root: Path, kind: str) -> dict[str, dict]:
    path = registry_path(user_root, kind)
    if not path.exists():
        return {}

    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        entries = data
    elif isinstance(data, dict):
        entries = data.get("skeletons", [])
    else:
        raise ValueError(f"Registry must be a list or object: {path}")

    registry: dict[str, dict] = {}
    for entry in entries:
        if isinstance(entry, dict) and entry.get("name"):
            registry[str(entry["name"])] = entry
    return registry


def save_registry(user_root: Path, kind: str, entries: Iterable[dict]) -> None:
    path = registry_path(user_root, kind)
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(entries, key=lambda item: item["name"])
    path.write_text(json.dumps({"skeletons": ordered}, indent=2) + "\n", encoding="utf-8")


def read_description(skeleton_dir: Path) -> str:
    readme = skeleton_dir / "README.md"
    if not readme.exists():
        return ""
    for raw_line in readme.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw_line.strip()
        if line and not line.startswith("#"):
            return line
    return ""


def infer_stack(skeleton_dir: Path, kind: str) -> list[str]:
    package_json = skeleton_dir / "package.json"
    if not package_json.exists():
        return []
    try:
        data = json.loads(package_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    names = set()
    for group in ("dependencies", "devDependencies"):
        deps = data.get(group, {})
        if isinstance(deps, dict):
            names.update(deps)

    stack = []
    checks = {
        "frontend": [
            ("next", "Next.js"),
            ("react", "React"),
            ("vite", "Vite"),
            ("vue", "Vue"),
            ("svelte", "Svelte"),
            ("typescript", "TypeScript"),
        ],
        "backend": [
            ("@nestjs/core", "NestJS"),
            ("express", "Express"),
            ("fastify", "Fastify"),
            ("hono", "Hono"),
            ("typescript", "TypeScript"),
        ],
    }[kind]
    for package_name, label in checks:
        if package_name in names:
            stack.append(label)
    return stack


def scan_source(
    *,
    kind: str,
    source: str,
    root: Path,
    user_root: Path,
) -> list[SkeletonCandidate]:
    base = apps_dir(root, kind, source)
    if not base.exists():
        return []

    registry = load_registry(user_root, kind) if source == SOURCE_USER else {}
    candidates = []
    for child in sorted(base.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        metadata = registry.get(child.name, {})
        candidates.append(
            SkeletonCandidate(
                name=child.name,
                kind=kind,
                source=source,
                path=str(child),
                stack=list(metadata.get("stack") or infer_stack(child, kind)),
                description=str(metadata.get("description") or read_description(child)),
            )
        )
    return candidates


def list_skeletons(
    *,
    kind: str | None = None,
    plugin_root: Path | None = None,
    user_root: Path | None = None,
) -> list[SkeletonCandidate]:
    plugin_root = plugin_root or plugin_root_from_script()
    user_root = user_root or default_user_root()
    kinds = KINDS if kind in (None, "all") else (kind,)

    merged: dict[tuple[str, str], SkeletonCandidate] = {}
    for item_kind in kinds:
        for candidate in scan_source(
            kind=item_kind,
            source=SOURCE_USER,
            root=user_root,
            user_root=user_root,
        ):
            merged[(candidate.kind, candidate.name)] = candidate
        for candidate in scan_source(
            kind=item_kind,
            source=SOURCE_BUILTIN,
            root=plugin_root,
            user_root=user_root,
        ):
            merged.setdefault((candidate.kind, candidate.name), candidate)

    return sorted(merged.values(), key=lambda item: (item.kind, item.name))


def ensure_safe_target(target: Path, overwrite: bool) -> None:
    if not target.exists():
        return
    if not target.is_dir():
        raise FileExistsError(f"Target exists and is not a directory: {target}")
    if any(target.iterdir()) and not overwrite:
        raise FileExistsError(f"Target is non-empty; pass --overwrite to replace: {target}")


def copy_skeleton(
    *,
    kind: str,
    name: str,
    target: Path,
    plugin_root: Path | None = None,
    user_root: Path | None = None,
    overwrite: bool = False,
) -> SkeletonCandidate:
    matches = [
        candidate
        for candidate in list_skeletons(kind=kind, plugin_root=plugin_root, user_root=user_root)
        if candidate.name == name
    ]
    if not matches:
        raise ValueError(f"No {kind} skeleton named {name}")

    candidate = matches[0]
    ensure_safe_target(target, overwrite)
    if target.exists() and overwrite:
        shutil.rmtree(target)
    shutil.copytree(candidate.path, target, dirs_exist_ok=True)
    return candidate


def register_skeleton(
    *,
    kind: str,
    name: str,
    source_dir: Path,
    user_root: Path | None = None,
    overwrite: bool = False,
    stack: list[str] | None = None,
    description: str | None = None,
) -> SkeletonCandidate:
    user_root = user_root or default_user_root()
    target = apps_dir(user_root, kind, SOURCE_USER) / name
    ensure_safe_target(target, overwrite)
    if target.exists() and overwrite:
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_dir, target, dirs_exist_ok=True)

    registry = load_registry(user_root, kind)
    registry[name] = {
        "name": name,
        "kind": kind,
        "source": SOURCE_USER,
        "path": str(target),
        "stack": stack or infer_stack(target, kind),
        "description": description if description is not None else read_description(target),
    }
    save_registry(user_root, kind, registry.values())

    return SkeletonCandidate(**registry[name])


def print_candidates(candidates: list[SkeletonCandidate], as_json: bool) -> None:
    if as_json:
        print(json.dumps([asdict(item) for item in candidates], indent=2))
        return

    for item in candidates:
        stack = f" [{', '.join(item.stack)}]" if item.stack else ""
        print(f"{item.kind}\t{item.name}\t{item.source}\t{item.path}{stack}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin-root", type=Path, default=plugin_root_from_script())
    parser.add_argument("--user-root", type=Path, default=default_user_root())
    subcommands = parser.add_subparsers(dest="command", required=True)

    list_parser = subcommands.add_parser("list")
    list_parser.add_argument("--kind", choices=("all", *KINDS), default="all")
    list_parser.add_argument("--json", action="store_true")

    copy_parser = subcommands.add_parser("copy")
    copy_parser.add_argument("--kind", choices=KINDS, required=True)
    copy_parser.add_argument("--name", required=True)
    copy_parser.add_argument("--target", type=Path, required=True)
    copy_parser.add_argument("--overwrite", action="store_true")
    copy_parser.add_argument("--json", action="store_true")

    register_parser = subcommands.add_parser("register")
    register_parser.add_argument("--kind", choices=KINDS, required=True)
    register_parser.add_argument("--name", required=True)
    register_parser.add_argument("--source", type=Path, required=True)
    register_parser.add_argument("--overwrite", action="store_true")
    register_parser.add_argument("--stack", action="append", default=[])
    register_parser.add_argument("--description", default=None)
    register_parser.add_argument("--json", action="store_true")

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.command == "list":
        print_candidates(
            list_skeletons(kind=args.kind, plugin_root=args.plugin_root, user_root=args.user_root),
            args.json,
        )
    elif args.command == "copy":
        print_candidates(
            [
                copy_skeleton(
                    kind=args.kind,
                    name=args.name,
                    target=args.target,
                    plugin_root=args.plugin_root,
                    user_root=args.user_root,
                    overwrite=args.overwrite,
                )
            ],
            args.json,
        )
    elif args.command == "register":
        print_candidates(
            [
                register_skeleton(
                    kind=args.kind,
                    name=args.name,
                    source_dir=args.source,
                    user_root=args.user_root,
                    overwrite=args.overwrite,
                    stack=args.stack,
                    description=args.description,
                )
            ],
            args.json,
        )


if __name__ == "__main__":
    main()
