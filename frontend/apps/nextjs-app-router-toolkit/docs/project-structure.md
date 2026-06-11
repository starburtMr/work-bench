# Project Structure

Most code lives in `src`.

```text
src/
  app/          Next.js App Router layouts, pages, route groups, and providers
  components/   shared UI, layout, error, and primitive components
  config/       environment parsing and route path constants
  features/     feature-owned auth, teams, discussions, comments, and users code
  hooks/        shared React hooks
  lib/          preconfigured clients, auth helpers, and query utilities
  testing/      MSW handlers, data generators, and test utilities
  types/        shared TypeScript types
  utils/        shared utility functions
```

## App Layer

`src/app` follows Next.js App Router conventions:

```text
src/app/
  layout.tsx
  page.tsx
  provider.tsx
  not-found.tsx
  auth/
  app/
  public/
```

Use server components by default. Add `use client` only when a component needs state, effects, browser APIs, event handlers, or client-only libraries.

Keep route files thin. Pages and layouts should compose feature modules and shared components rather than owning business logic.

## Feature Layer

A feature can use this shape:

```text
src/features/example-feature/
  api/
  components/
  hooks/
  stores/
  types/
  utils/
```

Only create folders that the feature needs. Keep feature-specific code inside the feature and shared UI or utilities outside it.

## Import Direction

Prefer one-way dependencies:

```text
shared -> features -> app
```

Shared code can be imported by features and app routes. Features can import shared code. The app layer composes features. Avoid importing one feature from another; compose them at the route or page level instead.

## Direct Imports

Prefer direct imports over broad barrel files when direct imports make ownership clearer. Barrel files are acceptable for small, stable public surfaces, but they should not hide cross-feature dependencies or make server/client boundaries harder to see.
