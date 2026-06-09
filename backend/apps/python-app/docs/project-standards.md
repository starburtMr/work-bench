# Project Standards

## Layering

- Keep domain rules in `domain`.
- Keep orchestration and use cases in `application`.
- Keep database and external integrations in `infrastructure`.
- Keep HTTP concerns in `presentation`.
- Keep shared runtime code in `core`.

## Naming

- Use `snake_case` for Python files, functions, and variables.
- Use `PascalCase` for classes and Pydantic models.
- Keep module names short and descriptive.
- Keep feature folders self-contained.

## Code Style

- Use type hints on public functions and methods.
- Keep functions small and focused.
- Use docstrings for public classes and complex helpers.
- Prefer direct imports over deep re-export chains.
- Do not move code across layers unless there is a clear reason.

## Architecture Rules

- Inner layers must not depend on outer layers.
- Routers should call use cases, not database code directly.
- Repositories should hide ORM details from the application layer.
- Shared helpers belong in `shared` or `core`, not in feature folders.
- `blank` is a scaffold module, not a production feature.

## Tooling

- Use `ruff` for linting and formatting checks.
- Use `uv` to manage dependencies and run commands.
- Use Alembic for schema changes.

## Logging

- The request logging path is shown in `docs/logging_rule.png`.
- Keep logs useful and short.
- Let middleware and shared logging code handle common logging behavior.
