# Project Structure

Most runtime code lives in `src/`.

```text
src/
  app/
  common/
  config/
  email/
  extras/
  lib/
  middlewares/
  modules/
  plugins/
  queues/
  routes/
  seeders/
  utils/
```

## Root Files

- `package.json` - runtime scripts and CLI entry points
- `pnpm-workspace.yaml` - workspace definition
- `build.ts` - build configuration
- `docker-compose.yml` - local dependency stack
- `.env.development`, `.env.production`, `.env.sample` - example environment values
- `packages/tbk/` - local toolkit CLI source
- `packages/create-tbk-app/` - CLI scaffolder source

## Runtime Layout

- `src/app` bootstraps the server and plugin registration
- `src/routes` aggregates route modules
- `src/modules/<module>` contains feature code
- `src/plugins/<plugin>` contains cross-cutting platform features
- `src/lib` contains database, cache, queue, storage, and email clients
- `src/middlewares` contains shared middleware
- `src/common` contains shared schemas and helpers
- `src/email` contains templates and email services
- `src/queues` contains queue definitions
- `src/seeders` contains seed logic
- `src/utils` contains pure helper functions

## Module Shape

Modules are typically organized as:

```text
src/modules/<name>/
  <name>.dto.ts
  <name>.model.ts
  <name>.schema.ts
  <name>.services.ts
  <name>.controller.ts
  <name>.router.ts
```

## CLI Source

- `packages/tbk/` holds the generator used by `pnpm tbk`
- `packages/create-tbk-app/` holds the standalone project scaffolder
- templates live under `packages/create-tbk-app/templates/`
