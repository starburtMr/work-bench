# Next.js Pages Router Toolkit

Reusable Next.js Pages Router skeleton for authenticated, API-backed product frontends. It is a work-bench frontend candidate, not a finished product.

## Best Fit

Use this skeleton when the target project needs:

- traditional Next.js Pages Router compatibility under `src/pages`;
- `getServerSideProps` entry points for route-level SSR data;
- authenticated app routes plus public and auth flows;
- TanStack Query API flows with a preconfigured API client;
- React Hook Form and Zod form patterns;
- feature-owned modules under `src/features`;
- MSW-backed local API mocks;
- Vitest, Testing Library, Playwright, Storybook, and Plop component generation.

Use another skeleton when the project needs App Router route groups, server components, or a pure client-side SPA.

## Included Example Domain

The demo domain is a team collaboration product:

- users register, log in, and edit profiles;
- users create or join teams;
- teams contain discussions and comments;
- roles include `ADMIN` and `USER`.

Treat this domain as a replaceable reference flow. It exists to show Pages Router entries, SSR data hooks, auth, server-state, forms, feature boundaries, mocks, tests, and e2e coverage in a realistic shape.

## Stack

- Next.js 14 Pages Router, React 18, and TypeScript
- Tailwind CSS, Radix UI, and Lucide icons
- TanStack Query
- Zustand for lightweight shared state
- React Hook Form and Zod
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

The mock server reads `NEXT_PUBLIC_*` values through `src/config/env.ts`.

## Commands

```bash
yarn dev              # start Next.js in development mode
yarn run-mock-server  # start the local mock API server
yarn lint             # run Next.js ESLint checks
yarn check-types      # run TypeScript checks
yarn test             # run Vitest
yarn build            # build the production Next.js app
yarn start            # start the production Next.js server
yarn test-e2e         # start mock API and run Playwright
yarn storybook        # start Storybook
yarn build-storybook  # build Storybook
yarn generate         # run Plop generators
```

## Structure

```text
src/
  pages/        Pages Router entries, SSR hooks, and route exports
  app/          providers, layouts, and page implementation modules
  components/   shared UI, layouts, errors, and SEO helpers
  config/       env and path constants
  features/     domain-owned auth, teams, discussions, comments, and users code
  hooks/        shared hooks
  lib/          API client, auth helpers, authorization, and query setup
  testing/      test utilities, router mocks, and MSW mocks
  types/        shared TypeScript types
  utils/        shared utilities
```

Keep `src/pages` thin. Put route implementations and layout composition in `src/app`, business behavior inside `src/features`, and reusable UI or adapters in shared folders.

## Reuse Boundary

When `skeleton-check` selects this candidate for a real project, copy the contents of this directory into the target frontend delivery directory, normally `<project-root>/frontend`. Do not copy the surrounding work-bench path or preserve an `apps/` wrapper in the real project unless the user asked for that layout.

After copying, update:

- `package.json` name and metadata;
- `.env` values such as `NEXT_PUBLIC_API_URL`, `NEXT_PUBLIC_URL`, and mock settings;
- public icons and app branding;
- landing page copy and external links;
- route names and paths in `src/config/paths.ts`;
- page entries and SSR hooks under `src/pages`;
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

Remove generated directories such as `node_modules`, `.next`, `coverage`, `playwright-report`, `test-results`, `storybook-static`, `.env`, `e2e/.auth`, and `mocked-db.json` before committing skeleton changes.

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
