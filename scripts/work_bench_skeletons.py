#!/usr/bin/env python3
"""Manage work-bench frontend/backend skeleton libraries."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Iterable

KINDS = ("frontend", "backend")
SOURCE_USER = "user-global"
SOURCE_BUILTIN = "plugin-builtin"
CHANGE_TYPES = ("add", "update", "docs", "remove", "rename")
DEFAULT_REPO = "starburtMr/work-bench"
DEFAULT_INSTALL_REF = "codex/initialize-workbench"
DEFAULT_INBOX_BRANCH = "skeleton-inbox"
GENERATED_DIRS = {
    "node_modules",
    "dist",
    "build",
    ".next",
    "coverage",
    "playwright-report",
    "storybook-static",
}
SECRET_FILE_NAMES = {
    ".env",
    ".env.local",
    ".env.development.local",
    ".env.production.local",
    ".env.test.local",
}
PLACEHOLDER_MARKERS = (
    "example",
    "dummy",
    "placeholder",
    "change-me",
    "changeme",
    "your-",
    "replace-me",
    "some-secret",
    "password",
    "secret",
    "test",
    "dev",
)


@dataclass(frozen=True)
class SkeletonCandidate:
    name: str
    kind: str
    source: str
    path: str
    stack: list[str]
    description: str


@dataclass(frozen=True)
class UpstreamConfig:
    repo: str
    install_ref: str
    inbox_branch: str
    repo_dir: Path


@dataclass(frozen=True)
class ChangeRequest:
    change_type: str
    kind: str
    name: str
    source: Path | None = None
    new_name: str | None = None


@dataclass
class ValidationResult:
    errors: list[str]
    warnings: list[str]

    @property
    def ok(self) -> bool:
        return not self.errors


@dataclass(frozen=True)
class ChangeMetadata:
    path: str
    stack: list[str]
    description: str
    best_for: str
    poor_fit_for: str
    guidance: str
    verification: str


@dataclass(frozen=True)
class ChangeResult:
    repo_dir: str
    branch: str
    base: str
    commit: str | None
    pr_url: str | None
    warnings: list[str]


CommandRunner = Callable[[list[str], Path | None], subprocess.CompletedProcess[str]]


def plugin_root_from_script() -> Path:
    return Path(__file__).resolve().parents[1]


def codex_home() -> Path:
    return Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")).expanduser()


def default_user_root() -> Path:
    return codex_home() / "work-bench"


def default_repo_dir() -> Path:
    return default_user_root() / "repo"


def config_path() -> Path:
    return default_user_root() / "config.json"


def run_command(command: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def load_upstream_config(
    *,
    repo: str | None = None,
    install_ref: str | None = None,
    inbox_branch: str | None = None,
    repo_dir: Path | None = None,
    path: Path | None = None,
) -> UpstreamConfig:
    payload = {}
    cfg_path = path or config_path()
    if cfg_path.exists():
        data = json.loads(cfg_path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            upstream = data.get("upstream", {})
            if isinstance(upstream, dict):
                payload = upstream

    resolved_repo = repo or str(payload.get("repo") or DEFAULT_REPO)
    resolved_install_ref = install_ref or str(payload.get("install_ref") or DEFAULT_INSTALL_REF)
    resolved_inbox_branch = inbox_branch or str(payload.get("inbox_branch") or DEFAULT_INBOX_BRANCH)
    raw_repo_dir = repo_dir or payload.get("repo_dir") or default_repo_dir()
    resolved_repo_dir = Path(raw_repo_dir).expanduser()

    return UpstreamConfig(
        repo=resolved_repo,
        install_ref=resolved_install_ref,
        inbox_branch=resolved_inbox_branch,
        repo_dir=resolved_repo_dir,
    )


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


def validate_skeleton_name(name: str) -> bool:
    return re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is not None


def branch_name(change: ChangeRequest) -> str:
    suffix = change.name
    if change.change_type == "rename" and change.new_name:
        suffix = f"{change.name}-to-{change.new_name}"
    return f"skeleton/{change.change_type}-{change.kind}-{suffix}"


def builtin_target(plugin_root: Path, kind: str, name: str) -> Path:
    return apps_dir(plugin_root, kind, SOURCE_BUILTIN) / name


def is_example_env(path: Path) -> bool:
    name = path.name.lower()
    return name.endswith(".example") or name.endswith(".sample") or name in {
        ".env.example",
        ".env.sample",
    }


def looks_like_placeholder(value: str) -> bool:
    normalized = value.strip().strip('"').strip("'").lower()
    return any(marker in normalized for marker in PLACEHOLDER_MARKERS)


def find_generated_dirs(source_dir: Path) -> list[str]:
    matches = []
    for child in source_dir.rglob("*"):
        if child.is_dir() and child.name in GENERATED_DIRS:
            matches.append(str(child.relative_to(source_dir)))
    return sorted(matches)


def find_secret_like_content(source_dir: Path) -> list[str]:
    findings = []
    private_key_pattern = re.compile(r"BEGIN .*PRIVATE KEY")
    github_token_pattern = re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}")
    aws_key_pattern = re.compile(r"AKIA[0-9A-Z]{16}")
    assignment_pattern = re.compile(
        r"(?i)\b(api[_-]?key|token|password|secret|access[_-]?key)\b\s*[:=]\s*['\"]?([^'\"\s#]{8,})"
    )

    for path in source_dir.rglob("*"):
        if not path.is_file():
            continue
        rel = str(path.relative_to(source_dir))
        if path.name in SECRET_FILE_NAMES or (path.name.startswith(".env") and not is_example_env(path)):
            findings.append(rel)
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if private_key_pattern.search(text) or github_token_pattern.search(text) or aws_key_pattern.search(text):
            findings.append(rel)
            continue
        for match in assignment_pattern.finditer(text):
            if not looks_like_placeholder(match.group(2)):
                findings.append(rel)
                break
    return sorted(set(findings))


def collect_quality_warnings(source_dir: Path | None) -> list[str]:
    if source_dir is None:
        return []
    warnings = []
    if not (source_dir / "README.md").exists():
        warnings.append("缺少 README.md")
    if not (source_dir / "AGENTS.md").exists():
        warnings.append("缺少 AGENTS.md")
    if not (source_dir / "docs").exists():
        warnings.append("缺少 docs/")
    package_json = source_dir / "package.json"
    if package_json.exists():
        try:
            data = json.loads(package_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            warnings.append("package.json 不是有效 JSON")
        else:
            if not isinstance(data.get("scripts"), dict) or not data["scripts"]:
                warnings.append("package.json 没有 scripts")
    return warnings


def validate_change_request(change: ChangeRequest, plugin_root: Path) -> ValidationResult:
    errors = []
    warnings = []

    if change.change_type not in CHANGE_TYPES:
        errors.append(f"Unsupported change type: {change.change_type}")
    if change.kind not in KINDS:
        errors.append(f"Unsupported skeleton kind: {change.kind}")
    if not validate_skeleton_name(change.name):
        errors.append(f"Invalid skeleton name: {change.name}")
    if change.new_name and not validate_skeleton_name(change.new_name):
        errors.append(f"Invalid new skeleton name: {change.new_name}")

    needs_source = change.change_type in {"add", "update", "docs", "rename"}
    if needs_source and change.source is None:
        errors.append(f"--source is required for {change.change_type}")
    if change.change_type == "rename" and not change.new_name:
        errors.append("--new-name is required for rename")
    if change.source is not None:
        if not change.source.exists() or not change.source.is_dir():
            errors.append(f"Source must be an existing directory: {change.source}")
        else:
            generated = find_generated_dirs(change.source)
            if generated:
                errors.append(f"Source contains generated directories: {', '.join(generated)}")
            secrets = find_secret_like_content(change.source)
            if secrets:
                errors.append(f"Source contains secret-like files or values: {', '.join(secrets)}")
            warnings.extend(collect_quality_warnings(change.source))

    if change.kind in KINDS:
        target = builtin_target(plugin_root, change.kind, change.name)
        target_exists = target.exists()
        if change.change_type == "add" and target_exists:
            errors.append(f"Target skeleton already exists: {target}")
        if change.change_type in {"update", "docs", "remove", "rename"} and not target_exists:
            errors.append(f"Target skeleton does not exist: {target}")
        if change.change_type == "rename" and change.new_name:
            new_target = builtin_target(plugin_root, change.kind, change.new_name)
            if new_target.exists():
                errors.append(f"Rename target already exists: {new_target}")

    return ValidationResult(errors=errors, warnings=warnings)


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


def read_package_scripts(skeleton_dir: Path) -> list[str]:
    package_json = skeleton_dir / "package.json"
    if not package_json.exists():
        return []
    try:
        data = json.loads(package_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    scripts = data.get("scripts", {})
    if not isinstance(scripts, dict):
        return []
    preferred = [
        "lint",
        "typecheck",
        "check-types",
        "test",
        "build",
        "test-e2e",
        "start:dev",
        "dev",
    ]
    return [name for name in preferred if name in scripts]


def guidance_links(kind: str, name: str, skeleton_dir: Path) -> str:
    base = f"./apps/{name}"
    links = []
    if (skeleton_dir / "README.md").exists():
        links.append(f"[README]({base}/README.md)")
    if (skeleton_dir / "AGENTS.md").exists():
        links.append(f"[AGENTS]({base}/AGENTS.md)")
    if (skeleton_dir / "docs").exists():
        links.append(f"[docs]({base}/docs)")
    return ", ".join(links) if links else "-"


def command_prefix(skeleton_dir: Path) -> str:
    if (skeleton_dir / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (skeleton_dir / "yarn.lock").exists():
        return "yarn"
    if (skeleton_dir / "package-lock.json").exists():
        return "npm run"
    if (skeleton_dir / "pyproject.toml").exists():
        return "uv run"
    if (skeleton_dir / "Makefile").exists():
        return "make"
    return ""


def verification_commands(skeleton_dir: Path) -> str:
    scripts = read_package_scripts(skeleton_dir)
    prefix = command_prefix(skeleton_dir)
    if scripts and prefix:
        if prefix == "npm run":
            return ", ".join(f"`npm run {script}`" for script in scripts)
        return ", ".join(f"`{prefix} {script}`" for script in scripts)
    if (skeleton_dir / "Makefile").exists():
        return "`make test`, `make start`"
    return "-"


def chinese_description(kind: str, name: str, skeleton_dir: Path | None) -> str:
    if skeleton_dir is not None:
        description = read_description(skeleton_dir)
        if description:
            return description
        stack = infer_stack(skeleton_dir, kind)
    else:
        stack = []
    stack_text = "、".join(stack) if stack else ("前端" if kind == "frontend" else "后端")
    kind_text = "前端" if kind == "frontend" else "后端"
    return f"{stack_text} {kind_text}骨架，适合需要可复用工程基线的项目。"


def build_metadata(kind: str, name: str, skeleton_dir: Path | None) -> ChangeMetadata:
    stack = infer_stack(skeleton_dir, kind) if skeleton_dir is not None and skeleton_dir.exists() else []
    description = chinese_description(kind, name, skeleton_dir)
    kind_text = "前端" if kind == "frontend" else "后端"
    stack_text = "、".join(stack) if stack else kind_text
    return ChangeMetadata(
        path=f"apps/{name}",
        stack=stack,
        description=description,
        best_for=f"需要 {stack_text} 可复用工程基线的{kind_text}项目",
        poor_fit_for=f"技术栈或交付形态与 {name} 不匹配的项目",
        guidance=guidance_links(kind, name, skeleton_dir) if skeleton_dir else "-",
        verification=verification_commands(skeleton_dir) if skeleton_dir else "-",
    )


def index_path(plugin_root: Path, kind: str) -> Path:
    return plugin_root / kind / "README.md"


def index_row(name: str, metadata: ChangeMetadata) -> str:
    stack = ", ".join(metadata.stack) if metadata.stack else "-"
    return (
        f"| [apps/{name}](./apps/{name}) | {stack} | {metadata.best_for} | "
        f"{metadata.poor_fit_for} | {metadata.guidance} | {metadata.verification} |"
    )


def update_index(plugin_root: Path, kind: str, name: str, metadata: ChangeMetadata | None, remove: bool = False) -> None:
    path = index_path(plugin_root, kind)
    if not path.exists():
        return
    lines = path.read_text(encoding="utf-8").splitlines()
    prefix = f"| [apps/{name}]"
    new_lines = [line for line in lines if not line.startswith(prefix)]
    if not remove and metadata is not None:
        row = index_row(name, metadata)
        insert_at = None
        for index, line in enumerate(new_lines):
            if line.startswith("| [apps/"):
                insert_at = index + 1
        if insert_at is None:
            new_lines.append(row)
        else:
            new_lines.insert(insert_at, row)
    path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def copytree_replace(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    ignore = shutil.ignore_patterns(*GENERATED_DIRS)
    shutil.copytree(source, target, ignore=ignore, symlinks=True)


def sync_docs_only(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for name in ("README.md", "AGENTS.md", "docs"):
        source_path = source / name
        target_path = target / name
        if not source_path.exists():
            continue
        if target_path.exists():
            if target_path.is_dir():
                shutil.rmtree(target_path)
            else:
                target_path.unlink()
        if source_path.is_dir():
            shutil.copytree(source_path, target_path, symlinks=True)
        else:
            shutil.copy2(source_path, target_path)


def apply_change(change: ChangeRequest, plugin_root: Path) -> ChangeMetadata | None:
    target_name = change.new_name if change.change_type == "rename" and change.new_name else change.name
    target = builtin_target(plugin_root, change.kind, target_name)
    old_target = builtin_target(plugin_root, change.kind, change.name)

    if change.change_type == "remove":
        shutil.rmtree(old_target)
        update_index(plugin_root, change.kind, change.name, None, remove=True)
        return None

    if change.source is None:
        raise ValueError(f"Source is required for {change.change_type}")

    if change.change_type == "docs":
        sync_docs_only(change.source, old_target)
        metadata = build_metadata(change.kind, change.name, old_target)
        update_index(plugin_root, change.kind, change.name, metadata)
        return metadata

    if change.change_type == "rename":
        shutil.rmtree(old_target)
        update_index(plugin_root, change.kind, change.name, None, remove=True)
        copytree_replace(change.source, target)
        metadata = build_metadata(change.kind, target_name, target)
        update_index(plugin_root, change.kind, target_name, metadata)
        return metadata

    copytree_replace(change.source, target)
    metadata = build_metadata(change.kind, target_name, target)
    update_index(plugin_root, change.kind, target_name, metadata)
    return metadata


def change_type_label(change_type: str) -> str:
    return {
        "add": "新增",
        "update": "更新",
        "docs": "文档更新",
        "remove": "删除",
        "rename": "重命名",
    }[change_type]


def kind_label(kind: str) -> str:
    return "前端" if kind == "frontend" else "后端"


def commit_subject(change: ChangeRequest) -> str:
    target = change.new_name if change.change_type == "rename" and change.new_name else change.name
    prefix = {
        "add": "feat",
        "update": "refactor",
        "docs": "docs",
        "remove": "chore",
        "rename": "refactor",
    }[change.change_type]
    action = {
        "add": "add",
        "update": "update",
        "docs": "update",
        "remove": "remove",
        "rename": "rename",
    }[change.change_type]
    suffix = " skeleton docs" if change.change_type == "docs" else " skeleton"
    return f"{prefix}(skeleton): {action} {change.kind} {target}{suffix}"


def pr_title(change: ChangeRequest) -> str:
    if change.change_type == "rename" and change.new_name:
        return f"重命名{kind_label(change.kind)}骨架：{change.name} -> {change.new_name}"
    return f"{change_type_label(change.change_type)}{kind_label(change.kind)}骨架：{change.name}"


def pr_body(change: ChangeRequest, metadata: ChangeMetadata | None, warnings: list[str]) -> str:
    target_name = change.new_name if change.change_type == "rename" and change.new_name else change.name
    target_path = f"{change.kind}/apps/{target_name}"
    description = metadata.description if metadata else f"{kind_label(change.kind)}骨架 `{target_name}` 已从内置骨架库移除。"
    stack = "、".join(metadata.stack) if metadata and metadata.stack else "未推断"
    warning_lines = "\n".join(f"- 提示：{warning}" for warning in warnings) if warnings else "- 通过：无软提示"
    return f"""## 变更类型
{change_type_label(change.change_type)}

## 骨架
- 类型：{change.kind}
- 名称：{target_name}
- 路径：{target_path}

## 中文说明
- 用途：{description}
- 适用场景：{metadata.best_for if metadata else '不再推荐使用该骨架'}
- 技术栈：{stack}
- 主要变更：{change_type_label(change.change_type)} `{target_path}` 并更新骨架索引。

## 自动检查
- 通过：敏感内容检查
- 通过：构建产物检查
{warning_lines}

## 后续合并建议
该 PR 先合并到 `skeleton-inbox`；确认稳定后，再统一合并到插件发布分支。
"""


def print_change_result(result: ChangeResult, as_json: bool) -> None:
    if as_json:
        print(json.dumps(asdict(result), indent=2, ensure_ascii=False))
        return
    print(f"branch\t{result.branch}")
    print(f"base\t{result.base}")
    if result.commit:
        print(f"commit\t{result.commit}")
    if result.pr_url:
        print(f"pr\t{result.pr_url}")
    for warning in result.warnings:
        print(f"warning\t{warning}")


def remote_url(repo: str) -> str:
    if repo.startswith("http://") or repo.startswith("https://") or repo.startswith("git@"):
        return repo
    return f"https://github.com/{repo}.git"


def repo_is_dirty(repo_dir: Path, runner: CommandRunner = run_command) -> bool:
    result = runner(["git", "status", "--porcelain"], repo_dir)
    return bool(result.stdout.strip())


def prepare_repo(config: UpstreamConfig, runner: CommandRunner = run_command) -> None:
    if not config.repo_dir.exists():
        config.repo_dir.parent.mkdir(parents=True, exist_ok=True)
        runner(["git", "clone", remote_url(config.repo), str(config.repo_dir)], None)
    runner(["git", "fetch", "origin", "--prune"], config.repo_dir)
    if repo_is_dirty(config.repo_dir, runner):
        raise RuntimeError(f"Contribution repo is dirty: {config.repo_dir}")


def remote_branch_exists(repo_dir: Path, branch: str, runner: CommandRunner = run_command) -> bool:
    result = runner(["git", "ls-remote", "--heads", "origin", branch], repo_dir)
    return bool(result.stdout.strip())


def ensure_inbox_branch(config: UpstreamConfig, runner: CommandRunner = run_command) -> None:
    if remote_branch_exists(config.repo_dir, config.inbox_branch, runner):
        runner(["git", "checkout", config.inbox_branch], config.repo_dir)
        runner(["git", "pull", "--ff-only", "origin", config.inbox_branch], config.repo_dir)
        return
    base_ref = f"origin/{config.install_ref}"
    try:
        runner(["git", "rev-parse", "--verify", base_ref], config.repo_dir)
    except subprocess.CalledProcessError:
        try:
            default_branch = runner(
                ["git", "symbolic-ref", "refs/remotes/origin/HEAD", "--short"],
                config.repo_dir,
            ).stdout.strip().removeprefix("origin/")
        except subprocess.CalledProcessError:
            default_branch = "main"
        base_ref = f"origin/{default_branch}"
    runner(["git", "checkout", "-B", config.inbox_branch, base_ref], config.repo_dir)
    runner(["git", "push", "-u", "origin", config.inbox_branch], config.repo_dir)


def checkout_inbox_base(config: UpstreamConfig, dry_run: bool, runner: CommandRunner = run_command) -> None:
    if not dry_run:
        ensure_inbox_branch(config, runner)
        return

    if remote_branch_exists(config.repo_dir, config.inbox_branch, runner):
        runner(["git", "checkout", "-B", config.inbox_branch, f"origin/{config.inbox_branch}"], config.repo_dir)
        return

    base_ref = f"origin/{config.install_ref}"
    try:
        runner(["git", "rev-parse", "--verify", base_ref], config.repo_dir)
    except subprocess.CalledProcessError:
        base_ref = "origin/HEAD"
    runner(["git", "checkout", "-B", config.inbox_branch, base_ref], config.repo_dir)


def create_contribution_branch(
    config: UpstreamConfig,
    branch: str,
    runner: CommandRunner = run_command,
) -> None:
    runner(["git", "checkout", "-B", branch, config.inbox_branch], config.repo_dir)


def final_diff_empty(repo_dir: Path, runner: CommandRunner = run_command) -> bool:
    result = runner(["git", "status", "--porcelain"], repo_dir)
    return not result.stdout.strip()


def ensure_github_auth(repo_dir: Path, runner: CommandRunner = run_command) -> None:
    runner(["gh", "auth", "status", "--hostname", "github.com"], repo_dir)


def commit_push_pr(
    *,
    config: UpstreamConfig,
    change: ChangeRequest,
    metadata: ChangeMetadata | None,
    warnings: list[str],
    branch: str,
    runner: CommandRunner = run_command,
) -> tuple[str, str]:
    runner(["git", "add", change.kind, f"{change.kind}/README.md"], config.repo_dir)
    body = pr_body(change, metadata, warnings)
    runner(["git", "commit", "-m", commit_subject(change), "-m", body], config.repo_dir)
    commit = runner(["git", "rev-parse", "--short", "HEAD"], config.repo_dir).stdout.strip()
    runner(["git", "push", "-u", "origin", branch], config.repo_dir)
    pr_url = runner(
        [
            "gh",
            "pr",
            "create",
            "--repo",
            config.repo,
            "--base",
            config.inbox_branch,
            "--head",
            branch,
            "--title",
            pr_title(change),
            "--body",
            body,
        ],
        config.repo_dir,
    ).stdout.strip()
    return commit, pr_url


def execute_change_pr(
    *,
    change: ChangeRequest,
    config: UpstreamConfig,
    dry_run: bool = False,
    runner: CommandRunner = run_command,
) -> ChangeResult:
    prepare_repo(config, runner)
    checkout_inbox_base(config, dry_run, runner)
    validation = validate_change_request(change, config.repo_dir)
    if not validation.ok:
        raise ValueError("; ".join(validation.errors))

    branch = branch_name(change)
    create_contribution_branch(config, branch, runner)
    if not dry_run:
        ensure_github_auth(config.repo_dir, runner)
    metadata = apply_change(change, config.repo_dir)
    if final_diff_empty(config.repo_dir, runner):
        raise RuntimeError("No repository changes were produced")

    if dry_run:
        runner(["git", "reset", "--hard"], config.repo_dir)
        runner(["git", "checkout", config.inbox_branch], config.repo_dir)
        return ChangeResult(
            repo_dir=str(config.repo_dir),
            branch=branch,
            base=config.inbox_branch,
            commit=None,
            pr_url=None,
            warnings=validation.warnings,
        )

    commit, pr_url = commit_push_pr(
        config=config,
        change=change,
        metadata=metadata,
        warnings=validation.warnings,
        branch=branch,
        runner=runner,
    )
    return ChangeResult(
        repo_dir=str(config.repo_dir),
        branch=branch,
        base=config.inbox_branch,
        commit=commit,
        pr_url=pr_url,
        warnings=validation.warnings,
    )


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

    change_parser = subcommands.add_parser("change-pr")
    change_parser.add_argument("--type", choices=CHANGE_TYPES, required=True, dest="change_type")
    change_parser.add_argument("--kind", choices=KINDS, required=True)
    change_parser.add_argument("--name", required=True)
    change_parser.add_argument("--source", type=Path, default=None)
    change_parser.add_argument("--new-name", default=None)
    change_parser.add_argument("--repo", default=None)
    change_parser.add_argument("--install-ref", default=None)
    change_parser.add_argument("--inbox-branch", default=None)
    change_parser.add_argument("--repo-dir", type=Path, default=None)
    change_parser.add_argument("--dry-run", action="store_true")
    change_parser.add_argument("--json", action="store_true")

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
    elif args.command == "change-pr":
        result = execute_change_pr(
            change=ChangeRequest(
                change_type=args.change_type,
                kind=args.kind,
                name=args.name,
                source=args.source.expanduser() if args.source is not None else None,
                new_name=args.new_name,
            ),
            config=load_upstream_config(
                repo=args.repo,
                install_ref=args.install_ref,
                inbox_branch=args.inbox_branch,
                repo_dir=args.repo_dir,
            ),
            dry_run=args.dry_run,
        )
        print_change_result(result, args.json)


if __name__ == "__main__":
    main()
