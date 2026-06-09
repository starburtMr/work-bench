# Python App

This is the Python backend template for FastAPI, Clean Architecture, and DDD.

## What It Contains

- `app/` for application code
- `docs/` for short reference notes
- `migrations/` for Alembic revisions
- `scripts/` for helper utilities
- `test/` for pytest coverage

## Common Commands

```bash
cp .env.example .env
uv sync
uv run -- python -m fastapi app.app:app --reload
uv run --with pytest -- pytest -q
uv run -- ruff check .
uv run -- ruff format --check .
```

## Docs

- `docs/README.md` - docs index
- `AGENTS.md` - project instructions and command shortcuts
