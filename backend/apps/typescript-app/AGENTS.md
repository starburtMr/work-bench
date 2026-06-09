# AGENTS.md

## Project Overview

`typescript-app` is a reusable backend runtime built on Express + MongoDB/Mongoose + Redis/BullMQ + a plugin system.
It also includes MagicRouter, Zod validation, OpenAPI generation, JWT auth, queues, admin tooling, realtime support, and email templates.

The runtime code lives in `src/`.
The CLI scaffolder lives in `packages/create-tbk-app/` and should be used when generating new modules or plugins.

## Local Docs

Read the local docs first when you need guidance:

- `docs/README.md`
- `docs/application-overview.md`
- `docs/project-structure.md`
- `docs/project-standards.md`
- `docs/commands.md`
- `docs/architecture.md`
- `docs/magic-router.md`
- `docs/security.md`
- `docs/testing.md`
- `docs/deployment.md`
- `docs/additional-resources.md`

## Setup and Commands

```bash
docker compose up -d
pnpm dev
pnpm start:dev
pnpm build
pnpm start:prod
pnpm start:local
pnpm typecheck
pnpm lint
pnpm lint:fix
pnpm email:dev
pnpm tbk generate:module <name>
pnpm tbk generate:plugin <name>
pnpm tbk generate:middleware <name>
pnpm tbk generate:factory <name>
pnpm tbk seed
pnpm tbk docs:openapi
pnpm tbk docs:sdk
```

## Structure

- `src/app` bootstraps the server and registers plugins.
- `src/routes` wires HTTP entry points.
- `src/modules` holds business modules.
- `src/plugins` holds extensible platform features.
- `src/lib` holds infrastructure clients such as database, cache, queue, storage, and email.
- `src/config` holds validated environment configuration.
- `src/middlewares` holds shared middleware.
- `src/common` holds shared schemas and helpers.
- `src/utils` holds pure utility functions.
- `src/email` holds email templates and services.
- `src/queues` holds queue definitions.
- `src/seeders` holds seed logic.
- `src/extras` holds supporting utilities.

Each module should keep its own DTO, schema, service, controller, model, and router files together.

## Working Rules

- Use MagicRouter for all routes. Do not add plain Express route handlers.
- Put request and response schemas in `*.schema.ts` files.
- Keep controllers thin and push business logic into services.
- Keep services framework-agnostic.
- Use Zod for validation and `validator.isMongoId()` for MongoDB IDs.
- Use `req.body` for Formidable uploads, not `req.file` or `req.files`.
- Use `config/env.ts` instead of reading `process.env` directly.
- Keep module scaffolding aligned with `packages/create-tbk-app/templates`.
- Use `pnpm` for package commands.

## Verification

- Use `pnpm typecheck` and `pnpm lint` for local checks.
- Use `pnpm dev` for runtime verification and `http://localhost:3000/docs` for the generated API docs.
- Update the CLI templates when a module or plugin shape changes.
- Keep operational surfaces such as admin, queue, and realtime tooling protected in production.
