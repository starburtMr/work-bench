# Project Structure

Most of the code lives under `app/`. When this skeleton is copied into a real project, this layout becomes the target project's backend root.

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
- `app/modules/example` demonstrates the full DDD path.
- `app/modules/blank` is the clean copy point for new modules.
- `app/modules/health` provides the smallest runtime check.

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
- Add tests with the module they prove; do not leave new behavior covered only by docs.

## Docs

- `docs/` contains short references for the architecture and working rules.
- `docs/logging_rule.png` is a visual reference for request logging flow.
