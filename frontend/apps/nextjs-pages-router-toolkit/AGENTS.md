# AGENTS.md

## Project Overview

This app is the Next.js Pages Router Toolkit frontend skeleton.
It is a reusable Pages Router candidate built with Next.js 14, React 18, TypeScript, TanStack Query, Zustand, React Hook Form, MSW, Storybook, Playwright, and `next-router-mock`.

The demo domain is a replaceable team collaboration product:

- users create or join teams
- teams contain discussions and comments
- roles are ADMIN and USER

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
cd apps/nextjs-pages-router-toolkit
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

- `src/pages` is the actual Next.js Pages Router layer.
- `src/pages/**` should stay thin and expose route entries, redirects, or SSR hooks.
- `src/app` composes providers, layouts, and page implementations.
- `src/features` contains feature-owned code.
- `src/components` contains shared UI.
- `src/lib` contains configured clients, auth helpers, authorization helpers, and query helpers.
- `src/testing` contains MSW setup, router mocks, and test utilities.
- `src/config`, `src/hooks`, `src/types`, and `src/utils` contain shared support code.

Keep the route layer thin and compose real behavior from `src/app`, `src/features`, and shared modules.

## Working Rules

- Use TypeScript strictly and keep imports direct.
- Prefer shared -> features -> app -> pages flow.
- Do not import one feature from another.
- Keep page modules focused on routing and SSR entry points.
- Use `getServerSideProps` only for route-level data and redirects.
- Pass request cookies into server-side API helpers when SSR needs authenticated data.
- Use `next-router-mock` for route tests where router behavior matters.
- Use TanStack Query for server state, local state first for UI state, and React Hook Form + Zod for forms.
- Use `yarn generate` when a scaffolded component or feature template is the fastest path.

## Verification

- Use Vitest and Testing Library for unit and integration tests.
- Use Playwright for e2e flows and start the mock server first.
- Validate `getServerSideProps`, page exports, and route behavior when touching `src/pages`.
- Keep page-level tests close to the code they exercise.
- Before committing skeleton work, remove generated directories such as `node_modules`, `.next`, `coverage`, `playwright-report`, `test-results`, `storybook-static`, `.env`, `e2e/.auth`, and `mocked-db.json`.
