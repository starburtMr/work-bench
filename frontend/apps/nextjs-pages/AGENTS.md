# AGENTS.md

## Project Overview

This app is the Next.js Pages Router implementation of Bulletproof React.
It uses Next.js 14, React 18, TypeScript, TanStack Query, react-query-auth, Zustand, React Hook Form, MSW, Storybook, Playwright, and next-router-mock.

Routing lives in `src/pages`.
The `src/app` folder is the application composition layer for providers, layouts, and feature composition.
Keep `src/pages` thin and let it expose page entry points and `getServerSideProps` when needed.

## Local Docs

Read the app-local docs first when you need guidance:

- `docs/application-overview.md`
- `docs/project-structure.md`
- `docs/project-standards.md`
- `docs/api-layer.md`
- `docs/state-management.md`
- `docs/testing.md`
- `docs/components-and-styling.md`
- `docs/performance.md`
- `docs/error-handling.md`
- `docs/security.md`

## Setup and Commands

```bash
cd apps/nextjs-pages
cp .env.example .env
yarn install
yarn run-mock-server
yarn dev
yarn test
yarn test-e2e
yarn lint
yarn check-types
yarn build
yarn start
yarn storybook
yarn build-storybook
```

## Structure

- `src/pages` is the actual Next.js routing layer.
- `src/app` composes providers, layouts, and page implementations under `src/app/pages`.
- `src/features` contains feature-owned code.
- `src/components` contains shared UI.
- `src/lib` contains configured clients, auth helpers, and query helpers.
- `src/testing` contains MSW setup, router mocks, and test utilities.
- `src/config`, `src/hooks`, `src/types`, and `src/utils` contain shared support code.

Keep the route layer thin and compose real behavior in `src/app` and `src/features`.

## Working Rules

- Use TypeScript strictly and keep imports direct.
- Prefer shared -> features -> app flow.
- Do not import one feature from another.
- Keep page modules focused on routing and SSR entry points.
- Use `next-router-mock` for route tests where router behavior matters.
- Use React Query for server state, local state first for UI state, and React Hook Form + Zod for forms.
- Use `yarn generate` when a scaffolded component or feature template is the fastest path.

## Verification

- Use Vitest and Testing Library for unit and integration tests.
- Use Playwright for e2e flows and start the mock server first.
- Validate `getServerSideProps`, page exports, and route behavior when touching `src/pages`.
- Keep page-level tests close to the code they exercise.
