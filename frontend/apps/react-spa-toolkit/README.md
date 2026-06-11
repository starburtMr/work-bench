# React SPA Toolkit

Reusable React + Vite skeleton for authenticated, API-backed single-page applications. It is a work-bench frontend candidate, not a finished product.

## Best Fit

Use this skeleton when the target project needs:

- client-side React routing without Next.js server rendering;
- authenticated app routes plus public landing and auth pages;
- TanStack Query API flows with a preconfigured API client;
- React Hook Form and Zod form patterns;
- feature-owned modules under `src/features`;
- MSW-backed local API mocks;
- Vitest, Testing Library, Playwright, Storybook, and Plop component generation.

Use another skeleton when the project needs Next.js App Router, Pages Router, SSR, server components, or framework-level API routes.

## Included Example Domain

The demo domain is a team collaboration product:

- users register, log in, and edit profiles;
- users create or join teams;
- teams contain discussions and comments;
- roles include `ADMIN` and `USER`.

Treat this domain as a replaceable reference flow. It exists to show routing, auth, server-state, forms, feature boundaries, mocks, tests, and e2e coverage in a realistic shape.

## Stack

- React 18 and TypeScript
- Vite
- React Router
- TanStack Query
- Zustand for lightweight local state
- React Hook Form and Zod
- Tailwind CSS, Radix UI, Lucide icons
- Axios API client
- MSW mock API
- Vitest, Testing Library, Playwright
- Storybook
- Plop component generator

## Setup

From this skeleton directory:

```bash
cp .env.example .env
yarn install
yarn dev
```

The dev server runs on `http://localhost:3000`.

For API-backed local flows, run the mock API server in a second terminal:

```bash
yarn run-mock-server
```

The app reads `VITE_APP_*` values and strips the prefix in `src/config/env.ts`.

## Commands

```bash
yarn dev              # start Vite
yarn run-mock-server  # start the local mock API server
yarn lint             # run ESLint
yarn check-types      # run TypeScript checks
yarn test             # run Vitest
yarn build            # type-check and build static assets
yarn preview          # preview the production build
yarn test-e2e         # start mock API and run Playwright
yarn storybook        # start Storybook
yarn build-storybook  # build Storybook
yarn generate         # run Plop generators
```

## Structure

```text
src/
  app/          route composition and providers
  components/   shared UI, layouts, errors, and SEO helpers
  config/       env and path constants
  features/     domain-owned auth, teams, discussions, comments, and users code
  hooks/        shared hooks
  lib/          API client, auth helpers, and query setup
  testing/      test utilities and MSW mocks
  types/        shared TypeScript types
  utils/        shared utilities
```

Keep route composition in `src/app`. Keep business behavior inside `src/features`. Shared UI, adapters, hooks, and utilities should not import app or feature modules.

## Reuse Boundary

When `skeleton-check` selects this candidate for a real project, copy the contents of this directory into the target frontend delivery directory, normally `<project-root>/frontend`. Do not copy the surrounding work-bench path or preserve an `apps/` wrapper in the real project unless the user asked for that layout.

After copying, update:

- `package.json` name and metadata;
- `.env` values such as `VITE_APP_API_URL`, `VITE_APP_APP_URL`, and mock settings;
- public icons and app branding;
- landing page copy and external links;
- route names and paths in `src/config/paths.ts`;
- demo feature modules under `src/features`;
- MSW handlers and data generators under `src/testing`;
- Playwright flows under `e2e`.

## Verification

Run the standard checks before offering this skeleton as ready:

```bash
yarn lint
yarn check-types
yarn test
yarn build
```

Run e2e when Playwright browsers and local ports are available:

```bash
yarn test-e2e
```

Remove generated directories such as `node_modules`, `dist`, `coverage`, `playwright-report`, and `storybook-static` before committing skeleton changes.

## Local Docs

- [Application overview](./docs/application-overview.md)
- [Project structure](./docs/project-structure.md)
- [Project standards](./docs/project-standards.md)
- [API layer](./docs/api-layer.md)
- [State management](./docs/state-management.md)
- [Testing](./docs/testing.md)
- [Components and styling](./docs/components-and-styling.md)
- [Performance](./docs/performance.md)
- [Error handling](./docs/error-handling.md)
- [Security](./docs/security.md)
- [Deployment](./docs/deployment.md)
- [Additional resources](./docs/additional-resources.md)
