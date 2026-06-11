# work-bench Plugin Usage

`work-bench` is a Codex plugin that packages workflow skills and reusable frontend/backend skeletons. The repository root is the plugin source root because it contains `.codex-plugin/plugin.json`.

## What the Plugin Includes

- `skills/`: plugin-exported workflow skills from idea, stack choice, data design, API contracts, skeleton selection, frontend, backend, docs, and final checks.
- `.codex/skills/`: project-local copy of the same workflow skills for work-bench development.
- `frontend/apps/`: plugin-builtin frontend skeletons.
- `backend/apps/`: plugin-builtin backend skeletons.
- `scripts/work_bench_skeletons.py`: helper for listing, copying, and registering skeletons.

## Local Preview

For local development, use the default personal marketplace at:

```text
~/.agents/plugins/marketplace.json
```

The personal marketplace entry should point to `./plugins/work-bench` relative to the marketplace root and include `policy.installation`, `policy.authentication`, and `category`.

Do not use `codex plugin marketplace add` for the default personal marketplace path. Codex discovers that file automatically.

When updating an already installed local plugin, use the plugin-creator cachebuster flow instead of hand-editing marketplace files:

```text
python3 scripts/update_plugin_cachebuster.py <plugin-path>
python3 scripts/read_marketplace_name.py
codex plugin add work-bench@<marketplace-name>
```

After reinstalling, start a new Codex thread so updated skills are loaded.

## Distribution

For sharing with others, distribute this repository or a packaged copy of it. The downloaded `work-bench/` directory is the plugin source root.

The marketplace file is not the distribution format. It is only a local preview/install index for a given machine.

## Plugin Validation

Before sharing or reinstalling, validate the plugin source root:

```text
python3 /path/to/plugin-creator/scripts/validate_plugin.py <work-bench-plugin-root>
```

The manifest must not contain placeholder values, unsupported fields, or references to missing optional assets. The manifest `skills` field must resolve to `skills`, so keep the top-level `skills/` export in sync with `.codex/skills/` when editing skill behavior.
