# AGENTS.md

## Project Overview

This app is the Next.js App Router Toolkit frontend skeleton.
It is a reusable App Router candidate built with Next.js 14, React 18, TypeScript, TanStack Query, Zustand, React Hook Form, MSW, Storybook, and Playwright.

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
cd apps/nextjs-app-router-toolkit
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

- `src/app` is the Next.js App Router layer.
- `src/app/auth`, `src/app/app`, and `src/app/public` hold route groups and layout composition.
- `src/features` contains feature-owned code.
- `src/components` contains shared UI.
- `src/lib` contains configured clients, auth helpers, and query helpers.
- `src/testing` contains MSW setup and test utilities.
- `src/config`, `src/hooks`, `src/types`, and `src/utils` contain shared support code.

Keep route files thin and compose behavior from features and shared components.

## Working Rules

- Use TypeScript strictly and keep imports direct.
- Prefer shared -> features -> app flow.
- Do not import one feature from another.
- Respect the App Router server/client boundary: server components by default, client components only when interaction or browser APIs require them.
- Keep `layout.tsx`, `page.tsx`, `not-found.tsx`, and metadata files focused on route-level composition.
- Use TanStack Query for server state, local state first for UI state, and React Hook Form + Zod for forms.
- Use `yarn generate` when a scaffolded component or feature template is the fastest path.

## Verification

- Use Vitest and Testing Library for unit and integration tests.
- Use Playwright for e2e flows and start the mock server first.
- Keep route-level tests close to the code they exercise.
- Re-check server component and client component boundaries when changing `src/app`.
- Before committing skeleton work, remove generated directories such as `node_modules`, `.next`, `coverage`, `playwright-report`, `test-results`, `storybook-static`, `.env`, and `mocked-db.json`.
