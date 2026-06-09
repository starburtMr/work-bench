# AGENTS.md

## Project Overview

This app is the Next.js App Router implementation of Bulletproof React.
It uses Next.js 14, React 18, TypeScript, TanStack Query, Zustand, React Hook Form, MSW, Storybook, and Playwright.

The route groups in `src/app` are:

- `auth`
- `app`
- `public`

Use App Router conventions throughout: `layout.tsx`, `page.tsx`, `not-found.tsx`, server components by default, and client components only when interaction requires them.

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
cd apps/nextjs-app
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
- Respect the server/client boundary in App Router files.
- Keep page and layout files focused on composition, navigation, and route-level concerns.
- Use React Query for server state, local state first for UI state, and React Hook Form + Zod for forms.
- Use `yarn generate` when a scaffolded component or feature template is the fastest path.

## Verification

- Use Vitest and Testing Library for unit and integration tests.
- Use Playwright for e2e flows and start the mock server first.
- Keep route-level tests close to the code they exercise.
- Re-check server component and client component boundaries when changing `src/app`.
