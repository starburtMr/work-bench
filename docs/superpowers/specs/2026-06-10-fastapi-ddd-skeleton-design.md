# FastAPI DDD Backend Skeleton Design

## Goal

Optimize the work-bench Python backend skeleton and rename it from `python-app` to `fastapi-ddd`.

The skeleton lives in the work-bench skeleton library at:

`backend/apps/fastapi-ddd`

When selected by the workflow, it is copied into a real project at:

`<project-root>/backend`

The target project must not receive an extra `apps` directory unless the user explicitly asks for a different layout.

## Selected Skills

Use these skills during implementation:

- `skeleton-check`: verify skeleton-library naming, README index coverage, copy boundaries, and target delivery rules.
- `server-frame`: improve the FastAPI backend skeleton, including app assembly, configuration, routing, health checks, errors, logging, database wiring, and tests.
- `doc-rules`: keep README, AGENTS, and local docs aligned with the actual skeleton behavior.
- `final-check`: verify the finished skeleton is copyable, runnable, testable, and documented.

## Skeleton Positioning

`fastapi-ddd` is the standard Python backend skeleton for FastAPI projects that use DDD and Clean Architecture.

It should support three usage modes:

- Quick start: a copied project can install dependencies, start the API, run lint, and run tests.
- Quick development: `blank` shows the minimum structure for a new business module.
- Quick understanding: `example` shows a complete module path from router to use case, domain, repository, schemas, and tests.

The skeleton is not a real business project. It should avoid project-specific concepts, external service assumptions, and domain-specific workflow choices.

## Architecture Design

Keep the existing high-level layout:

- `app/app.py`: FastAPI application assembly, middleware, exception handlers, routers, and OpenAPI metadata.
- `app/core`: shared configuration, database, logging, security, middleware, resource lifecycle, migrations, and key helpers.
- `app/modules/<module>`: feature modules split into `domain`, `application`, `infrastructure`, and `presentation`.
- `migrations`: Alembic migration setup and sample revisions.
- `scripts`: small utility scripts for secrets, keys, and structure inspection.
- `test`: pytest suites mirroring application structure.
- `docs`: concise local reference docs.

Module intent:

- `health`: minimal runtime and readiness verification.
- `blank`: clean module template for new business modules.
- `example`: complete DDD demonstration module.
- `authentication` and `user`: generic auth/user skeleton pieces, kept only where they remain maintainable and documented.
- `shared`: cross-module primitives only.

## Implementation Scope

Rename and metadata:

- Rename `backend/apps/python-app` to `backend/apps/fastapi-ddd`.
- Update project metadata, README, AGENTS, Docker/compose names, and docs that still refer to the old skeleton name.
- Update `backend/README.md` so the skeleton index lists `fastapi-ddd` instead of recommending `python-app`.

Backend skeleton quality:

- Review `app/app.py` for clear router registration, OpenAPI metadata, middleware order, and production docs behavior.
- Make `health` the smallest reliable runtime check.
- Keep `blank` minimal and copy-friendly.
- Make `example` the primary DDD teaching module.
- Add useful starter tests so the skeleton is not only a directory layout.

Documentation:

- Update `README.md` with skeleton purpose, quick start, verification commands, and replacement points after copying.
- Update `AGENTS.md` with agent-facing rules for layering, testing, migrations, and safe edits.
- Update `docs/` so each document explains how to develop from this skeleton, not just what files exist.
- Keep docs concise and avoid duplicating large blocks.

## Verification Design

Run the smallest meaningful checks first, then broaden:

- `uv sync` or an equivalent dependency sanity check if the environment supports it.
- `uv run -- ruff check .`
- `uv run -- ruff format --check .`
- `uv run --with pytest -- pytest -q`
- Import the FastAPI app to confirm application assembly works.
- Check `backend/README.md` still indexes all backend skeleton candidates.
- Check no target-project copy rule tells agents to copy `backend/apps` into a real project by default.

If the local environment cannot run dependency or test commands, record the exact skipped command and reason.

## Non-Goals

- Do not build a real product feature.
- Do not add project-specific business domains.
- Do not introduce new production dependencies unless existing tools cannot cover the skeleton need.
- Do not change frontend skeletons.
- Do not rewrite unrelated workflow skills except where the skeleton index or copy rule directly requires it.

## Acceptance Criteria

- The skeleton directory is named `backend/apps/fastapi-ddd`.
- The old `python-app` name is removed from recommendation paths, except in migration notes if needed.
- `backend/README.md` describes `fastapi-ddd` as the FastAPI DDD backend skeleton.
- The skeleton README and AGENTS files explain how to start, verify, extend, and safely copy the skeleton.
- `blank` remains a minimal module template.
- `example` provides a complete DDD reference flow.
- Basic tests exist and pass, or any environment blocker is documented with the exact command that could not run.
- Final verification uses `skeleton-check`, `server-frame`, `doc-rules`, and `final-check` responsibilities as the review lens.
