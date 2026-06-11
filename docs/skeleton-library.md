# Skeleton Library

`work-bench` has two skeleton sources:

- User-global skeletons: `<codex-home>/work-bench/frontend/apps` and `<codex-home>/work-bench/backend/apps`
- Plugin-builtin skeletons: `frontend/apps` and `backend/apps`

`<codex-home>` resolves to `CODEX_HOME` when set, otherwise `~/.codex`.

## Precedence

Skeleton discovery checks user-global skeletons first, then plugin-builtin skeletons.

If both sources contain the same skeleton name and kind, the user-global skeleton wins. Reports should still show both the selected `source` and the selected `path` so the user can see whether the choice came from their own library or from the plugin bundle.

## Candidate Metadata

Each discovered skeleton should expose:

- `name`
- `kind`: `frontend` or `backend`
- `source`: `user-global` or `plugin-builtin`
- `path`
- `stack`, when it can be inferred
- `description`, when it can be inferred

The built-in index files remain:

- `frontend/README.md`
- `backend/README.md`

These indexes describe bundled candidates. User-global candidates can also be registered in:

- `<codex-home>/work-bench/registry/frontend-skeletons.json`
- `<codex-home>/work-bench/registry/backend-skeletons.json`

## Copying Skeletons

Copy skeleton contents into the target project delivery path, not into a nested `apps/<candidate>` directory.

Default delivery paths remain:

- Frontend: `<project-root>/frontend`
- Backend: `<project-root>/backend`

Copy operations must refuse to overwrite a non-empty target unless overwrite behavior is explicitly requested.

## Promoting User-Global Skeletons

When a user-global skeleton becomes useful enough to ship with the plugin, promote it through a reviewed PR rather than editing plugin cache files. The promotion path is:

1. Finish the skeleton in `<codex-home>/work-bench/frontend/apps/<name>` or `<codex-home>/work-bench/backend/apps/<name>`.
2. Ensure it has a `README.md`; add `AGENTS.md` and `docs/` when the skeleton needs reusable agent or architecture rules.
3. Run `scripts/work_bench_skeletons.py change-pr` with the matching `--type`, `--kind`, `--name`, and `--source`.
4. Review the generated PR against `skeleton-inbox`.

The `change-pr` command updates the plugin-builtin app directory and `frontend/README.md` or `backend/README.md` index inside a dedicated contribution clone at `<codex-home>/work-bench/repo`. It blocks likely secrets, generated artifacts, dirty contribution workspaces, empty diffs, and invalid add/update/docs/remove/rename states before creating the PR.
