# TypeScript Backend Toolkit Skeleton

This is the reusable TypeScript backend toolkit skeleton for work-bench projects that need an Express API with MongoDB/Mongoose, Redis/BullMQ, MagicRouter, OpenAPI generation, JWT/session auth, admin tooling, realtime support, observability, cache, lifecycle, security, and CLI scaffolding.

It is a skeleton, not a finished business product. Keep the starter `auth`, `user`, `upload`, and `healthcheck` modules generic, then adapt or replace them after copying the skeleton into a real project.

## When To Choose It

- The backend should be TypeScript-first and Express-based.
- The project needs MongoDB/Mongoose rather than a relational DDD stack.
- The team wants reusable platform plugins for auth, queues, admin, realtime, observability, cache, security, and OpenAPI.
- The project benefits from `tbk` generators for modules, plugins, middleware, factories, seeders, OpenAPI, and SDK output.

## Copy Boundary

This candidate lives in the work-bench skeleton library at `backend/apps/typescript-backend-toolkit`.

When selected for a real project, copy this candidate's contents into the recorded backend delivery directory, normally `<project-root>/backend`. Do not copy the surrounding `backend/apps` library path into the target project unless the user explicitly asks for that layout.

## Stack And Layout

- `src/main.ts` connects the database, initializes the app, mounts `/api`, installs error handling, and starts the server.
- `src/app/app.ts` registers built-in plugins.
- `src/app/createApp.ts` creates the Express app, HTTP server, plugin context, and priority-ordered plugin registration.
- `src/routes` wires MagicRouter-based HTTP entry points.
- `src/modules` contains generic starter modules.
- `src/plugins` contains reusable platform plugins.
- `src/lib` contains infrastructure clients for database, cache, queues, storage, email, and errors.
- `packages/tbk` contains the local toolkit CLI.
- `packages/create-tbk-app` contains the project scaffolder and templates.
- `docs` contains concise local references for architecture, commands, routing, security, testing, and deployment.

## Local Commands

```bash
docker compose up -d
pnpm install
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
pnpm tbk make:seeder <module>/<name>
pnpm tbk make:factory <module>/<name>
pnpm tbk seed
pnpm tbk docs:openapi
pnpm tbk docs:sdk
```

`pnpm tbk` runs the local CLI source through `tsx`, so it is available in a fresh checkout after dependencies are installed.

## Post-Copy Adaptation Points

After copying the skeleton into a real project, update:

- `package.json` name, description, author, license, and published package metadata.
- `.env.development`, `.env.production`, and `.env.sample` values.
- MongoDB database name and connection URL.
- JWT and session secrets.
- Admin email, username, password, and session secret.
- Email provider values such as Mailgun, Resend, or SMTP.
- `CLIENT_SIDE_URL`, CORS origins, and trusted proxy settings.
- Enabled plugins in `src/app/app.ts`, especially admin, queue dashboard, realtime, metrics, cache, storage, and email.
- Starter modules under `src/modules` that should become project-specific domains.

## Verification

Run the smallest checks first:

```bash
pnpm typecheck
pnpm lint
pnpm build
pnpm tbk --help
```

Runtime verification may also need MongoDB and Redis:

```bash
docker compose up -d
pnpm start:dev
```

## Environment Examples

The checked-in `.env.development` and `.env.production` files are examples with local or dummy values. Replace all secrets, database names, admin credentials, email provider settings, and public origins before using a copied project outside local development.
