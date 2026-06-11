# Project Structure

Most code lives in `src`.

```text
src/
  pages/        Next.js Pages Router entries, SSR hooks, and route exports
  app/          providers, layouts, and page implementation modules
  components/   shared UI, layout, error, SEO, and primitive components
  config/       environment parsing and route path constants
  features/     feature-owned auth, teams, discussions, comments, and users code
  hooks/        shared React hooks
  lib/          preconfigured clients, auth helpers, authorization, and query utilities
  testing/      MSW handlers, router mocks, data generators, and test utilities
  types/        shared TypeScript types
  utils/        shared utility functions
```

## Pages Layer

`src/pages` is the real Next.js routing surface:

```text
src/pages/
  _app.tsx
  404.tsx
  index.tsx
  auth/
  app/
  public/
```

Keep page files thin. They should export route components, redirects, and SSR hooks, then compose real behavior from `src/app`, `src/features`, and shared modules.

Use `getServerSideProps` for route-level data loading and redirects. When SSR needs authenticated data, pass request cookies into the API helpers that already accept a cookie argument.

## App Composition Layer

`src/app` is not the Next.js App Router. In this skeleton it is the application composition layer:

```text
src/app/
  provider.tsx
  pages/
```

Use this layer for page implementations, providers, layouts, and cross-feature composition that would make `src/pages` too large.

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
shared -> features -> app -> pages
```

Shared code can be imported by features, app composition modules, and pages. Features can import shared code. The app layer composes features. Pages expose the Next.js route contract. Avoid importing one feature from another; compose them at the app or page level instead.

## Direct Imports

Prefer direct imports over broad barrel files when direct imports make ownership clearer. Barrel files are acceptable for small, stable public surfaces, but they should not hide cross-feature dependencies or make route boundaries harder to see.
