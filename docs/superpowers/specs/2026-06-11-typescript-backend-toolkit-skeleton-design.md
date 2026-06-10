# TypeScript Backend Toolkit Skeleton Design

## Goal

Optimize the work-bench TypeScript backend skeleton and rename it from `typescript-app` to `typescript-backend-toolkit`.

The skeleton lives in the work-bench backend skeleton library at:

`backend/apps/typescript-backend-toolkit`

When selected by the workflow, it is copied into a real project at:

`<project-root>/backend`

The target project must not receive the surrounding `backend/apps` library path unless the user explicitly asks for that layout.

## Selected Skills

Use these skills during implementation:

- `skeleton-check`: verify backend skeleton-library naming, README index coverage, copy boundaries, and target delivery rules.
- `server-frame`: improve the Express backend skeleton, including runtime startup, configuration, routing, plugins, queues, cache, database, errors, observability, and verification.
- `doc-rules`: keep README, AGENTS, local docs, package metadata, and command references aligned with the actual skeleton behavior.
- `final-check`: verify the finished skeleton is copyable, runnable, documented, and free of cache artifacts.

## Skeleton Positioning

`typescript-backend-toolkit` is the standard TypeScript backend toolkit skeleton for work-bench projects that need a plugin-oriented Node.js backend.

It should support these usage modes:

- Quick start: a copied project can install dependencies, start the API, build, typecheck, and lint.
- Quick development: `packages/tbk` and `packages/create-tbk-app` provide scaffolding entry points for modules, plugins, middleware, factories, seeds, and generated docs.
- Platform extension: `src/plugins` demonstrates reusable platform concerns such as MagicRouter, auth, admin, realtime, observability, cache, lifecycle, security, and queue dashboards.
- Runtime reference: `src/modules` shows generic auth, user, upload, and healthcheck modules that a real project can adapt or replace.

The skeleton is not a real business product. It should avoid product-specific domains, hidden production credentials, and docs that imply the skeleton is a finished application.

## Architecture Design

Keep the existing high-level layout:

- `src/main.ts`: runtime bootstrap, database connection, API route mounting, error handling, and server listen.
- `src/app`: Express application creation and plugin registration.
- `src/routes`: MagicRouter-based HTTP entry points.
- `src/modules`: generic feature modules such as auth, user, upload, and healthcheck.
- `src/plugins`: reusable platform plugins and plugin registry surfaces.
- `src/lib`: infrastructure clients for database, cache, queue, storage, email, and errors.
- `src/config`: validated environment configuration.
- `src/middlewares`: shared Express middleware.
- `src/common`: shared schemas and helpers.
- `src/email`: email templates and services.
- `src/queues`: BullMQ queue definitions.
- `packages/tbk`: CLI actions for module, plugin, middleware, factory, seed, OpenAPI, and SDK generation.
- `packages/create-tbk-app`: project scaffolder package and templates.
- `docs`: concise local reference docs.

## Implementation Scope

Rename and metadata:

- Rename `backend/apps/typescript-app` to `backend/apps/typescript-backend-toolkit`.
- Keep the package name `typescript-backend-toolkit` unless implementation discovers a strong reason to change it.
- Update `backend/README.md` so the candidate table lists `typescript-backend-toolkit`.
- Update local path references in AGENTS, docs, package metadata, scripts, and generated docs where they still point to `typescript-app`.

Documentation:

- Add or repair the root `README.md`; the current backend index points to it, but it is missing.
- Update `AGENTS.md` with skeleton copy rules, command references, module/plugin boundaries, and verification expectations.
- Update `docs/README.md` to remove stale `CLAUDE.md` references unless that file exists.
- Keep docs based on the real structure; do not invent `example` or `blank` modules if the skeleton does not contain them.
- Document post-copy replacement points: package metadata, environment values, database name, JWT secret, admin account, Mailgun dummy values, allowed origins, and plugin exposure.

Backend skeleton quality:

- Review startup and app assembly around `src/main.ts`, `src/app/createApp.ts`, and `src/app/app.ts`.
- Review MagicRouter and plugin entry docs so route, schema, response, and OpenAPI conventions are easy to follow.
- Keep auth, user, upload, and healthcheck as generic starter modules.
- Keep plugins as platform capabilities, not business features.
- Add focused starter verification only where the skeleton is currently missing basic confidence.

Environment examples:

- Keep `.env.development` and `.env.production` as example files because the user confirmed they are examples.
- Ensure their values are visibly local or dummy values.
- Avoid adding real credentials or machine-specific secrets.

## Verification Design

Run the smallest meaningful checks first, then broaden:

- `pnpm typecheck`
- `pnpm lint`
- `pnpm build`
- `pnpm tbk --help` or an equivalent CLI availability check if the package scripts support it.
- Check that `backend/README.md` indexes all backend skeleton candidates exactly once.
- Check no changed docs recommend the old `typescript-app` path.
- Check no target-project copy rule tells agents to copy `backend/apps` into a real project by default.
- Check cache and install artifacts are not staged.

If the local environment cannot run a command because dependencies, Docker, Redis, MongoDB, or network access are unavailable, record the exact skipped command and reason.

## Non-Goals

- Do not build a real product feature.
- Do not add a new database or backend framework.
- Do not rewrite the plugin system.
- Do not turn this skeleton into a DDD skeleton; `fastapi-ddd` already covers that lane.
- Do not modify `backend/apps/fastapi-ddd`.
- Do not create frontend changes.

## Acceptance Criteria

- The skeleton directory is named `backend/apps/typescript-backend-toolkit`.
- `backend/README.md` points to `apps/typescript-backend-toolkit` and no longer recommends `apps/typescript-app`.
- A root README exists for the skeleton and explains purpose, stack, commands, copy rules, and adaptation points.
- AGENTS and local docs match the real Express, MongoDB, Redis/BullMQ, MagicRouter, plugin, OpenAPI, and CLI structure.
- Stale references to missing docs such as `CLAUDE.md` are removed or corrected.
- `.env.development` and `.env.production` remain example files with dummy/local values.
- Verification commands pass, or blockers are documented with exact command output.
- No cache, virtual environment, install, or build output is included in the final staged changes.
