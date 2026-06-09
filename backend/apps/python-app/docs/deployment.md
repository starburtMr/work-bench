# Deployment

## Local Development

```bash
uv sync
uv run -- python -m fastapi app.app:app --reload
```

## Docker

- `make start` runs the full stack with Docker Compose
- `make start-silent` runs the same stack in the background
- `make dependencies-up` starts only the database services
- `make dependencies-down` stops the database services

## Database Changes

```bash
alembic revision --autogenerate -m "description"
alembic upgrade head
```

## Release Notes

- keep `.env` values aligned with the target environment
- run tests before packaging or deploying
- check migrations before promoting a change
- confirm the app boots cleanly with the selected startup method
