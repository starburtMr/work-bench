# Skeleton Contribution

Reusable skeletons created during project work belong in the user-global work-bench library by default, not inside plugin cache directories.

## User-Global Paths

`<codex-home>` resolves to `CODEX_HOME` when set, otherwise `~/.codex`.

```text
<codex-home>/work-bench/
  frontend/
    apps/
      <skeleton-name>/
  backend/
    apps/
      <skeleton-name>/
  registry/
    frontend-skeletons.json
    backend-skeletons.json
```

## Registering a Skeleton

Use `scripts/work_bench_skeletons.py register` to copy a candidate skeleton into the user-global library and update the matching registry.

Registration should record at least:

- `name`
- `kind`
- `source`
- `path`
- `stack`
- `description`

## Contribution Rules

- Use lower-case hyphen-case skeleton names.
- Include a `README.md` that states purpose, stack, start commands, test commands, and known constraints.
- Include `AGENTS.md` when the skeleton has stack-specific agent rules.
- Include `docs/` when the skeleton has reusable architecture, testing, deployment, API, or style guidance.
- Do not store secrets, local `.env` files, generated dependency directories, build output, or project-specific customer data.
- If a user-global skeleton intentionally customizes a plugin-builtin skeleton with the same name, document that override in its README.

## Updating Built-In Skeletons

Plugin-builtin skeletons live in `frontend/apps` and `backend/apps`. Treat them as plugin source assets. Updating them is a plugin change and should be reviewed separately from registering a personal user-global skeleton.

Built-in skeleton changes must go through a PR to `skeleton-inbox`. Do not edit plugin cache directories, and do not push skeleton changes directly to the plugin install branch.

Use `change-pr` after a skeleton add/update/docs/remove/rename is complete:

```bash
python3 scripts/work_bench_skeletons.py change-pr \
  --type add \
  --kind frontend \
  --name react-dashboard \
  --source ~/.codex/work-bench/frontend/apps/react-dashboard
```

Supported change types:

- `add`: copy a new frontend/backend skeleton into `frontend/apps` or `backend/apps`.
- `update`: replace an existing built-in skeleton from a reviewed source directory.
- `docs`: sync only `README.md`, `AGENTS.md`, and `docs/` for an existing built-in skeleton.
- `remove`: delete an existing built-in skeleton and remove its index row.
- `rename`: replace an existing built-in skeleton under `--new-name` and update the index.

The command uses `<codex-home>/work-bench/repo` as the contribution clone by default, ensures `skeleton-inbox` exists, creates a `skeleton/<type>-<kind>-<name>` branch, updates the matching built-in index, checks for generated output and likely secrets, and creates a GitHub PR with a Chinese title/body. Add `--dry-run` for local validation without push/PR creation, and `--json` for agent-readable output.

Example rename:

```bash
python3 scripts/work_bench_skeletons.py change-pr \
  --type rename \
  --kind backend \
  --name express-api \
  --new-name express-service \
  --source ~/.codex/work-bench/backend/apps/express-service
```
