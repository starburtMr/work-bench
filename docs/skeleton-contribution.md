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
