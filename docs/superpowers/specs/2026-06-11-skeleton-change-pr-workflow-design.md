# Skeleton Change PR Workflow Design

## Summary

Add a workflow for turning any reusable skeleton library change into a GitHub pull request. The workflow covers adding, updating, documenting, removing, and renaming frontend or backend skeletons. It does not push directly into the plugin installation branch. Instead, every automated skeleton change targets a dedicated `skeleton-inbox` branch so changes can be reviewed before they are merged into the plugin release branch.

## Goals

- Let the user or an agent promote complete skeleton changes from the user-global skeleton library into the `work-bench` repository.
- Support all skeleton change types, not only new skeletons.
- Generate a Chinese description for each skeleton change and include it in the PR.
- Keep the plugin installation branch stable while still making skeleton contributions easy to upload.
- Prevent secrets, generated artifacts, and incomplete skeletons from being committed automatically.
- Use deterministic script behavior for file, git, and GitHub actions so Codex can call the workflow reliably.

## Non-Goals

- Do not automatically merge `skeleton-inbox` into `codex/initialize-workbench`.
- Do not modify plugin cache directories directly.
- Do not require a web UI or dashboard.
- Do not make pull requests to upstream repositories where the current user lacks GitHub permissions.
- Do not replace the existing user-global skeleton registration flow.

## Existing Context

`work-bench` already has two skeleton sources:

- User-global skeletons under `<codex-home>/work-bench/frontend/apps` and `<codex-home>/work-bench/backend/apps`.
- Plugin-builtin skeletons under `frontend/apps` and `backend/apps` in this repository.

The existing `scripts/work_bench_skeletons.py` can list, copy, and register skeletons. Registration stores reusable skeletons in the user-global library. The new workflow adds the reverse path: turning user-global or explicitly provided skeleton changes into reviewed repository PRs.

## Branch Model

The workflow uses three branch roles:

```text
codex/initialize-workbench
  Plugin installation and release branch. Keep stable.

skeleton-inbox
  Dedicated base branch for all automated skeleton change PRs.

skeleton/<change-type>-<kind>-<name>
  Per-change contribution branch created by the workflow.
```

Example contribution branches:

```text
skeleton/add-frontend-react-admin-dashboard
skeleton/update-backend-typescript-backend-toolkit
skeleton/remove-frontend-old-spa
skeleton/rename-frontend-old-name-to-new-name
skeleton/docs-frontend-react-spa-toolkit
```

All automatically created PRs use:

```text
base: skeleton-inbox
head: skeleton/<change-type>-<kind>-<name>
```

If `skeleton-inbox` does not exist, the workflow creates it from the configured install ref. If the install ref cannot be resolved, it falls back to the remote default branch, then to `main`.

## Repository Workspace

The workflow must not edit the installed plugin cache. It maintains a dedicated clone at:

```text
<codex-home>/work-bench/repo
```

`<codex-home>` resolves to `CODEX_HOME` when set, otherwise `~/.codex`.

The clone is used only for repository contribution work:

1. Clone `starburtMr/work-bench` if the repo directory does not exist.
2. Fetch remote refs if it already exists.
3. Ensure `skeleton-inbox` exists locally and remotely.
4. Create or reset a contribution branch from `skeleton-inbox`.
5. Apply the requested skeleton change.
6. Commit, push, and create a PR.

The workflow must refuse to continue if the contribution workspace has unrelated uncommitted changes.

## Command Design

Add a new subcommand to `scripts/work_bench_skeletons.py`:

```bash
python3 scripts/work_bench_skeletons.py change-pr
```

Required arguments:

- `--type`: one of `add`, `update`, `docs`, `remove`, `rename`.
- `--kind`: one of `frontend`, `backend`.
- `--name`: existing or new skeleton name, depending on change type.

Conditional arguments:

- `--source`: required for `add`, `update`, `docs`, and `rename`.
- `--new-name`: required for `rename`.

Optional arguments:

- `--repo`: override upstream repository, default `starburtMr/work-bench`.
- `--install-ref`: override install ref, default `codex/initialize-workbench`.
- `--inbox-branch`: override inbox branch, default `skeleton-inbox`.
- `--repo-dir`: override local contribution clone directory, default `<codex-home>/work-bench/repo`.
- `--dry-run`: run validation and show planned git/PR actions without changing files.
- `--json`: emit machine-readable result.

Example commands:

```bash
python3 scripts/work_bench_skeletons.py change-pr \
  --type add \
  --kind frontend \
  --name react-admin-dashboard \
  --source ~/.codex/work-bench/frontend/apps/react-admin-dashboard
```

```bash
python3 scripts/work_bench_skeletons.py change-pr \
  --type update \
  --kind backend \
  --name typescript-backend-toolkit \
  --source ~/.codex/work-bench/backend/apps/typescript-backend-toolkit
```

```bash
python3 scripts/work_bench_skeletons.py change-pr \
  --type remove \
  --kind frontend \
  --name old-react-template
```

```bash
python3 scripts/work_bench_skeletons.py change-pr \
  --type rename \
  --kind frontend \
  --name old-name \
  --new-name new-name \
  --source ~/.codex/work-bench/frontend/apps/new-name
```

## Change Application Rules

For `add`:

- The target path must not already exist in `frontend/apps` or `backend/apps`.
- Copy the source directory into the matching built-in skeleton directory.
- Add or update the matching root index row.

For `update`:

- The target skeleton must already exist.
- Replace the built-in skeleton directory with the source directory.
- Preserve repository-level files outside that skeleton unless explicitly changed by index generation.
- Update the matching root index row.

For `docs`:

- The target skeleton must already exist.
- Sync documentation-oriented files from the source, such as `README.md`, `AGENTS.md`, and `docs/`.
- Update the matching root index row.
- Do not replace runtime code unless the source docs command explicitly includes it in a future extension.

For `remove`:

- The target skeleton must already exist.
- Delete the built-in skeleton directory.
- Remove the matching root index row.

For `rename`:

- The old target skeleton must exist.
- The new target skeleton name must not exist.
- Delete or move the old built-in skeleton path.
- Copy the source directory into the new built-in skeleton path.
- Update the matching root index row from old name to new name.

## Index And Chinese Description

The workflow updates either:

- `frontend/README.md`
- `backend/README.md`

The generated index row should include:

- Skeleton path.
- Stack inferred from metadata and dependency files.
- Chinese fit description.
- Chinese poor-fit description when it can be inferred.
- Guidance links to `README.md`, `AGENTS.md`, and `docs/` when those paths exist.
- Verification commands inferred from `package.json` scripts or existing README content.

Chinese description generation order:

1. Use an explicit `--description` argument if a future version adds it.
2. Use the first meaningful paragraph from the skeleton `README.md`.
3. Infer stack and purpose from `package.json`, directory names, and existing docs.
4. Fall back to a conservative sentence based on `kind`, `name`, and `type`.

Example:

```text
React 管理后台骨架，适合需要认证、表格、表单、权限控制和 API 数据流的中后台前端项目。
```

## Validation

Hard failures block commit, push, and PR creation:

- Skeleton name is not lower-case hyphen-case.
- `kind` is not `frontend` or `backend`.
- `type` is not supported.
- Required `--source` or `--new-name` is missing.
- Source path does not exist or is not a directory.
- Source contains generated dependency or build output directories:
  - `node_modules`
  - `dist`
  - `build`
  - `.next`
  - `coverage`
  - `playwright-report`
  - `storybook-static`
- Source contains obvious secrets or local credentials:
  - `.env` files that are not documented examples.
  - Private keys.
  - GitHub tokens.
  - AWS access keys.
  - API key, password, token, or secret values that do not look like placeholders.
- `add` targets an existing skeleton.
- `update`, `docs`, `remove`, or `rename` targets a missing skeleton.
- `rename` target name already exists.
- Contribution workspace has unrelated uncommitted changes.
- `gh` is not installed, not logged in, or cannot create PRs for the repo.
- Final repository diff is empty.

Soft warnings are included in the PR body but do not block:

- Missing `README.md`.
- Missing `AGENTS.md`.
- Missing `docs/`.
- `package.json` has no scripts.
- README does not mention start commands.
- README does not mention test or verification commands.
- Description quality is inferred instead of explicit.

## Commit And PR Output

Commit subjects should use conventional commit style:

```text
feat(skeleton): add frontend react-admin-dashboard skeleton
refactor(skeleton): update backend typescript-backend-toolkit skeleton
docs(skeleton): update frontend react-spa-toolkit skeleton docs
chore(skeleton): remove frontend old-react-template skeleton
refactor(skeleton): rename frontend old-name skeleton
```

PR title should be Chinese and concise:

```text
新增前端骨架：react-admin-dashboard
更新后端骨架：typescript-backend-toolkit
删除前端骨架：old-react-template
重命名前端骨架：old-name -> new-name
```

PR body template:

```markdown
## 变更类型
新增 / 修改 / 删除 / 重命名 / 文档更新

## 骨架
- 类型：frontend
- 名称：react-admin-dashboard
- 路径：frontend/apps/react-admin-dashboard

## 中文说明
- 用途：提供 React 管理后台骨架。
- 适用场景：需要认证、表格、表单、权限控制和 API 数据流的中后台前端项目。
- 技术栈：React、TypeScript、Vite、TanStack Query。
- 主要变更：新增 `frontend/apps/react-admin-dashboard` 并更新前端骨架索引。

## 自动检查
- 通过：敏感内容检查
- 通过：构建产物检查
- 提示：缺少 docs/

## 后续合并建议
该 PR 先合并到 `skeleton-inbox`；确认稳定后，再统一合并到插件发布分支。
```

The JSON result should include:

- `repo_dir`
- `branch`
- `base`
- `commit`
- `pr_url`
- `warnings`

## Configuration

Default configuration:

```json
{
  "upstream": {
    "repo": "starburtMr/work-bench",
    "install_ref": "codex/initialize-workbench",
    "inbox_branch": "skeleton-inbox",
    "repo_dir": "~/.codex/work-bench/repo"
  }
}
```

User override path:

```text
<codex-home>/work-bench/config.json
```

Fork users can override:

```json
{
  "upstream": {
    "repo": "someone/work-bench",
    "install_ref": "main",
    "inbox_branch": "skeleton-inbox"
  }
}
```

The script should prefer explicit CLI flags, then config file values, then defaults.

## Documentation Updates

Implementation should update:

- `README.md`: mention the skeleton change PR workflow.
- `docs/skeleton-contribution.md`: explain that built-in skeleton changes use `change-pr`.
- `docs/skeleton-library.md`: distinguish user-global registration from built-in skeleton PR contribution.
- `05-skeleton-check`, `06-web-frame`, `07-server-frame`, and `09-doc-rules`: mention that mature skeleton changes should be submitted through the PR workflow.

## Success Criteria

- A user can add, update, document, remove, or rename a skeleton and create a PR to `skeleton-inbox` with one command.
- The workflow never commits secrets or generated build/dependency artifacts.
- PRs contain Chinese descriptions and check summaries.
- Plugin installation branch remains untouched by automated skeleton PRs.
- The workflow can be run from an installed plugin without editing plugin cache directories.
