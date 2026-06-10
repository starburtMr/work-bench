# Testing

## Test Layout

- `test/core` for shared backend behavior
- `test/modules/<module>` for module-level tests

## What To Test

- domain entities and domain services
- use cases and application orchestration
- repositories and database wiring
- router behavior and request/response contracts

## Tools

- `pytest`
- fixtures
- integration tests where the database or HTTP layer matters

## Commands

```bash
uv run --with pytest -- pytest -q
uv run -- ruff check .
uv run -- ruff format --check .
```

## Testing Rules

- Keep tests deterministic.
- Prefer behavior checks over implementation details.
- Mirror the app structure when adding new tests.
- Add integration coverage when a change touches the database, router, or middleware path.
- Keep a fast app import or route registration test so skeleton drift is caught early.
