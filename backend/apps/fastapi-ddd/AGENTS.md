# AGENTS.md

## Project Overview

This app is the `fastapi-ddd` backend skeleton for work-bench projects.
It uses FastAPI, SQLAlchemy, Alembic, Pydantic Settings, Loguru, JWT cookies, Docker Compose, and `uv`.

When selected by `skeleton-check`, copy this directory's contents into the real project's `<project-root>/backend` directory. The target project should not receive the work-bench `backend/apps` wrapper unless the user explicitly requests that layout.

The code is split into:

- `app/core` for shared configuration and infrastructure wiring
- `app/modules/<module>` for feature modules
- `migrations` for Alembic revisions
- `scripts` for helper utilities
- `test` for pytest suites

Current modules include:

- `authentication`
- `health`
- `user`
- `shared`
- `example`
- `blank`

## Local Docs

Read the app-local docs first when you need guidance:

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

## Setup and Commands

```bash
cd backend/apps/fastapi-ddd
cp .env.example .env
uv sync
uv run -- python -m fastapi app.app:app --reload
uv run --with pytest -- pytest -q
uv run -- ruff check .
uv run -- ruff format --check .
alembic revision --autogenerate -m "description"
alembic upgrade head
make start
make start-silent
make dependencies-up
make dependencies-down
```

## Structure

- `app/app.py` assembles the FastAPI app, middleware, exception handlers, and routers.
- `app/core` holds database, logging, security, settings, middleware, resources, migrations helpers, and key management.
- `app/modules/<module>` follows `domain`, `application`, `infrastructure`, and `presentation`.
- `app/modules/example` is the complete DDD reference module.
- `app/modules/blank` is the clean copy point for new modules.
- `app/modules/health` is the minimal runtime verification module.
- `docs` holds short reference docs.
- `test` mirrors the application structure with pytest coverage.
- `migrations` holds Alembic revisions.
- `scripts` holds utility scripts.

## Working Rules

- Keep business rules in `domain`.
- Keep orchestration in `application`.
- Keep persistence and external adapters in `infrastructure`.
- Keep routers, schemas, dependencies, and docs helpers in `presentation`.
- Prefer direct imports and avoid cross-module coupling unless the code is shared.
- Use type hints, small functions, and docstrings for public APIs.
- Use `ruff` for style checks and `pytest` for behavior checks.
- Use `alembic` for schema changes instead of editing migration history manually.
- Keep `.env.example` parseable; do not leave required integers, lists, or URLs empty.
- Do not hardcode real credentials, signing keys, encryption keys, or production secrets.
- Update local docs when changing commands, module responsibilities, public routes, environment variables, or Docker behavior.

## Verification

- Use unit tests for domain and use case logic.
- Use integration tests for repositories, routes, and database wiring.
- Use Docker or the Makefile targets when you need the full local stack.
- Check the generated OpenAPI docs after router changes.
