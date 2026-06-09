# Project Structure

Most of the code lives under `app/`.

```text
app/
  app.py
  core/
  modules/
docs/
migrations/
scripts/
test/
```

## Root Files

- `pyproject.toml` - project metadata and dependency definitions
- `uv.lock` - locked dependency versions
- `.env.example` - sample environment variables
- `Dockerfile` and `docker-compose.yaml` - containerized local and production runs
- `Makefile` - shortcuts for common Docker commands
- `alembic.ini` and `migrations/` - database migration setup

## App Layer

- `app/app.py` is the FastAPI entry point.
- `app/core` contains database, logging, security, middleware, settings, resources, and key management.
- `app/modules/<module>` contains feature code.

Each module follows the same structure:

```text
app/modules/<module>/
  domain/
  application/
  infrastructure/
  presentation/
```

## Tests

- `test/` mirrors the application modules.
- `test/core` covers shared backend behavior.
- `test/modules/<module>` holds module-specific tests.

## Docs

- `docs/` contains short references for the architecture and working rules.
- `docs/logging_rule.png` is a visual reference for request logging flow.
