# Adaptation Checklist

Use this checklist when a new skeleton is added to the workspace and needs local docs, `AGENTS.md`, and `.github/workflows`.

## Common

- Read the target app's manifest files first.
- Use sibling example projects in the same repo as the reference source.
- Mirror structure and command shape, not wording.
- Remove any cross-project references.
- Keep docs concise and project-specific.
- Only add CI jobs for commands the skeleton actually supports.

## Frontend Skeletons

Typical docs set:

- `docs/README.md`
- `docs/application-overview.md`
- `docs/project-structure.md`
- `docs/project-standards.md`
- `docs/api-layer.md`
- `docs/testing.md`
- `docs/security.md`
- `docs/error-handling.md`
- `docs/performance.md`
- `docs/deployment.md`
- optional stack-specific pages such as `components-and-styling.md` or `state-management.md`

Typical `AGENTS.md` content:

- project overview
- docs list
- setup and commands
- folder structure
- working rules
- verification notes

Typical workflow checks:

- install dependencies
- build
- lint
- typecheck
- tests
- Playwright or browser tests when present
- artifact upload for test reports when useful

## Backend Python Skeletons

Typical docs set:

- `docs/README.md`
- `docs/application-overview.md`
- `docs/project-structure.md`
- `docs/project-standards.md`
- `docs/api-layer.md`
- `docs/testing.md`
- `docs/security.md`
- `docs/error-handling.md`
- `docs/performance.md`
- `docs/deployment.md`
- `docs/additional-resources.md`

Typical `AGENTS.md` content:

- FastAPI or equivalent backend overview
- `uv`, `ruff`, `pytest`, and Alembic commands when present
- app structure and layering rules
- verification notes for tests, linting, and local startup

Typical workflow checks:

- `uv sync`
- `ruff check`
- `ruff format --check`
- `pytest`
- `python -m compileall`
- Alembic or migration smoke checks if the project provides them

## Backend TypeScript Skeletons

Typical docs set:

- `docs/README.md`
- `docs/application-overview.md`
- `docs/project-structure.md`
- `docs/project-standards.md`
- `docs/commands.md`
- `docs/architecture.md`
- `docs/magic-router.md`
- `docs/security.md`
- `docs/testing.md`
- `docs/deployment.md`
- `docs/additional-resources.md`

Typical `AGENTS.md` content:

- runtime stack summary
- module and plugin structure
- setup and commands
- working rules for routing, schemas, validation, and environment config
- verification notes for typecheck, lint, tests, build, and docs

Typical workflow checks:

- install dependencies
- lint
- typecheck
- tests
- build
- e2e or docs-generation jobs when the repo includes them

## Validation

- Check that every workflow command exists in the target skeleton.
- Check that `AGENTS.md` only mentions files that exist in that skeleton.
- Check that docs links do not point at other skeletons unless they are intentionally shared references.
