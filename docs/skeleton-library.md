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
