# FastAPI DDD Backend

`fastapi-ddd` is the reusable Python backend skeleton for work-bench projects that need FastAPI, SQLAlchemy/Alembic, DDD, Clean Architecture, Docker Compose, and `uv`.

When this skeleton is selected, copy the contents of this directory into the real project's `<project-root>/backend` directory. Do not copy the surrounding `backend/apps` library path into the target project unless the user explicitly asks for that layout.

## What It Contains

- `app/app.py` assembles FastAPI, middleware, exception handlers, routers, and OpenAPI metadata.
- `app/core/` contains shared configuration, database, logging, security, middleware, lifecycle, migrations, and key helpers.
- `app/modules/example/` is the complete DDD reference module.
- `app/modules/blank/` is the clean module template for new business modules.
- `app/modules/health/` is the minimal runtime verification module.
- `migrations/` contains Alembic setup and starter revisions.
- `test/` mirrors the application structure with starter pytest coverage.
- `docs/` contains short reference notes for people and agents.

## Quick Start

```bash
cp .env.example .env
uv sync
uv run -- python -m fastapi app.app:app --reload
```

The API starts from `app.app:app`. OpenAPI docs are available at `/docs` outside production mode.

## Verification

```bash
uv run --with pytest -- pytest -q
uv run -- ruff check .
uv run -- ruff format --check .
uv run -- python -m compileall app
```

Use Docker when you need the local PostgreSQL and pgAdmin stack:

```bash
make dependencies-up
make start
make dependencies-down
```

## Adapting After Copy

- Replace `APPLICATION_*`, `POSTGRESQL_*`, `SECURITY_*`, cookie, and JWT values in `.env`.
- Generate real signing and encryption keys with the scripts in `scripts/`.
- Rename the project in `pyproject.toml`, Docker Compose names, and docs if the target project needs a product-specific package name.
- Keep `example` as a reference or remove it after the first real module is implemented.
- Copy `blank` when creating a new module, then rename the files, router docs, schemas, exceptions, and tests together.

## Docs

- `AGENTS.md` - agent rules and command shortcuts
- `docs/README.md` - docs index
- `docs/project-structure.md` - layout and module responsibilities
- `docs/api-layer.md` - router, use case, mapper, and schema flow
- `docs/testing.md` - starter testing strategy
- `docs/deployment.md` - local, Docker, and release notes
