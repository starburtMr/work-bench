# Testing

## Current Approach

This repository does not ship with a dedicated test runner in the root scripts.
Use the existing checks and add tests alongside the code when you introduce them.

## What To Verify

- module services and controllers
- schema validation
- MagicRouter route wiring
- plugin registration
- auth and session behavior
- queue and email integrations

## Useful Checks

```bash
pnpm typecheck
pnpm lint
pnpm build
pnpm tbk --help
pnpm dev
pnpm tbk docs:openapi
pnpm email:dev
```

## If You Add Tests

- keep them close to the code they cover
- prefer deterministic behavior
- mock external services at the boundary
- cover the business logic first
