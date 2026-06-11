# Backend Skeleton Index

This directory is the backend skeleton library for work-bench. It records reusable candidates under `apps/*` so `skeleton-check` can compare them before choosing `reuse` or `create`.

This file is only an index for skeleton candidates. It does not define target project paths or delivery targets.

## Candidates

| Candidate | Stack | Best for | Poor fit for | Local guidance | Verification entry points |
| --- | --- | --- | --- | --- | --- |
| [apps/fastapi-ddd](./apps/fastapi-ddd) | Python, FastAPI, SQLAlchemy/Alembic, Clean Architecture, DDD, Docker Compose, `uv` | Python APIs needing layered architecture, explicit migrations, modular domains, and strong separation of concerns | Node/TypeScript teams, MongoDB-first projects, queue-heavy plugin systems | [README](./apps/fastapi-ddd/README.md), [AGENTS](./apps/fastapi-ddd/AGENTS.md), [docs](./apps/fastapi-ddd/docs) | `make start`, `make dependencies-up`, `uv sync`, `ruff`, `pytest` |
| [apps/typescript-backend-toolkit](./apps/typescript-backend-toolkit) | Node.js, TypeScript, Express, MongoDB/Mongoose, Redis/BullMQ, OpenAPI, plugin system, pnpm | TypeScript APIs needing queues, cache, admin/plugin surfaces, OpenAPI generation, and extensible backend modules | Python-first teams, relational database-first DDD projects, minimal script-like APIs | [README](./apps/typescript-backend-toolkit/README.md), [AGENTS](./apps/typescript-backend-toolkit/AGENTS.md), [docs](./apps/typescript-backend-toolkit/docs) | `pnpm lint`, `pnpm typecheck`, `pnpm build`, `pnpm start:dev` |

## How skeleton-check Should Use This Index

1. Read this index before scanning `apps/*`.
2. Use the candidate table to shortlist likely matches.
3. Read each shortlisted candidate's local README, AGENTS.md, docs, manifests, and runtime scripts.
4. Decide `reuse` when an existing candidate matches the requested stack and product shape.
5. Decide `create` when no candidate fits; add the new candidate under `apps/*` and update this index in the same change.

## Adding a Candidate

When adding a backend skeleton candidate:

- Place it under `apps/<candidate-name>`.
- Include a local `README.md`.
- Include local `AGENTS.md` when the skeleton has stack-specific agent rules.
- Include `docs/` when the skeleton has reusable architecture, testing, deployment, API, or security guidance.
- Add a row to the Candidates table with stack, best-fit, poor-fit, guidance links, and verification entry points.
