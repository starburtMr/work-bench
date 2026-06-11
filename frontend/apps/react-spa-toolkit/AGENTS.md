# AGENTS.md

## Project Overview

This app is the React SPA Toolkit frontend skeleton.
It is a reusable client-side SPA candidate built with React 18, TypeScript, Vite, React Router, TanStack Query, Zustand, React Hook Form, MSW, Storybook, and Playwright.

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
cd apps/react-spa-toolkit
cp .env.example .env
yarn install
yarn run-mock-server
yarn dev
yarn test
yarn lint
yarn build
yarn preview
```

## Structure

- `src/main.tsx` is the entry point.
- `src/app` owns the router, provider, and route composition.
- `src/app/routes` holds route modules and page-level composition.
- `src/features` contains feature-owned code.
- `src/components` contains shared UI.
- `src/lib` contains preconfigured clients and adapters.
- `src/testing` contains test utilities and MSW mocks.
- `src/config`, `src/hooks`, `src/types`, and `src/utils` contain shared support code.

Keep route composition in the app layer and business logic inside features.

## Working Rules

- Use TypeScript strictly and keep imports direct.
- Prefer shared -> features -> app flow.
- Do not import one feature from another.
- Avoid barrel files if they make Vite tree-shaking worse.
- Use React Query for server state, local state first for UI state, and React Hook Form + Zod for forms.
- Put route-level changes in `src/app/routes` and reusable UI in shared folders or feature folders.
- Use `yarn generate` when a scaffolded component or feature template is the fastest path.

## Verification

- Use Vitest and Testing Library for unit and integration tests.
- Use Playwright for e2e flows.
- Keep storybook stories and tests aligned when changing reusable UI.
- Start the mock server when you need local API-backed flows or e2e coverage.
- Before committing skeleton work, remove generated directories such as `node_modules`, `dist`, `coverage`, `playwright-report`, and `storybook-static`.
