# Frontend Skeleton Index

This directory is the frontend skeleton library for work-bench. It records reusable candidates under `apps/*` so `skeleton-check` can compare them before choosing `reuse` or `create`.

This file is only an index for skeleton candidates. It does not define target project paths or delivery targets.

## Candidates

| Candidate | Stack | Best for | Poor fit for | Local guidance | Verification entry points |
| --- | --- | --- | --- | --- | --- |
| [apps/react-spa-toolkit](./apps/react-spa-toolkit) | React 18, Vite, React Router, TanStack Query, Zustand, React Hook Form, MSW, Vitest, Playwright, Storybook | Authenticated product SPAs, dashboards, internal tools, and API-backed prototypes that do not need server rendering | Projects requiring Next.js SSR, App Router, Pages Router compatibility, or server components | [README](./apps/react-spa-toolkit/README.md), [AGENTS](./apps/react-spa-toolkit/AGENTS.md), [docs](./apps/react-spa-toolkit/docs) | `yarn lint`, `yarn check-types`, `yarn test`, `yarn build`, `yarn test-e2e` |
| [apps/nextjs-app-router-toolkit](./apps/nextjs-app-router-toolkit) | Next.js App Router, React, TypeScript, TanStack Query, Vitest, Playwright, Storybook | Modern Next.js apps needing App Router layouts, nested routes, SSR-ready routing, server components, and API-backed product flows | Legacy Pages Router maintenance or pure SPA-only prototypes | [README](./apps/nextjs-app-router-toolkit/README.md), [AGENTS](./apps/nextjs-app-router-toolkit/AGENTS.md), [docs](./apps/nextjs-app-router-toolkit/docs) | `yarn lint`, `yarn check-types`, `yarn test`, `yarn build`, `yarn test-e2e` |
| [apps/nextjs-pages-router-toolkit](./apps/nextjs-pages-router-toolkit) | Next.js Pages Router, React, TypeScript, TanStack Query, Vitest, Playwright, Storybook | Maintaining or bootstrapping traditional Next.js Pages Router projects with SSR entry points and `src/pages` compatibility | New App Router-first projects or SPA-only prototypes | [README](./apps/nextjs-pages-router-toolkit/README.md), [AGENTS](./apps/nextjs-pages-router-toolkit/AGENTS.md), [docs](./apps/nextjs-pages-router-toolkit/docs) | `yarn lint`, `yarn check-types`, `yarn test`, `yarn build`, `yarn test-e2e` |
| [apps/e2e-smoke-20260611170745](./apps/e2e-smoke-20260611170745) | React, TypeScript | 需要 React、TypeScript 可复用工程基线的前端项目 | 技术栈或交付形态与 e2e-smoke-20260611170745 不匹配的项目 | [README](./apps/e2e-smoke-20260611170745/README.md), [AGENTS](./apps/e2e-smoke-20260611170745/AGENTS.md), [docs](./apps/e2e-smoke-20260611170745/docs) | - |

## Shared Reference Docs

These shared docs describe common frontend expectations across the examples:

- [docs/application-overview.md](./docs/application-overview.md)
- [docs/project-structure.md](./docs/project-structure.md)
- [docs/project-standards.md](./docs/project-standards.md)
- [docs/api-layer.md](./docs/api-layer.md)
- [docs/state-management.md](./docs/state-management.md)
- [docs/testing.md](./docs/testing.md)
- [docs/components-and-styling.md](./docs/components-and-styling.md)
- [docs/performance.md](./docs/performance.md)
- [docs/error-handling.md](./docs/error-handling.md)
- [docs/security.md](./docs/security.md)

## How skeleton-check Should Use This Index

1. Read this index before scanning `apps/*`.
2. Use the candidate table to shortlist likely matches.
3. Read each shortlisted candidate's local README, AGENTS.md, docs, and package scripts.
4. Decide `reuse` when an existing candidate matches the requested stack and product shape.
5. Decide `create` when no candidate fits; add the new candidate under `apps/*` and update this index in the same change.

## Adding a Candidate

When adding a frontend skeleton candidate:

- Place it under `apps/<candidate-name>`.
- Include a local `README.md`.
- Include local `AGENTS.md` when the skeleton has stack-specific agent rules.
- Include `docs/` when the skeleton has reusable architecture, testing, deployment, or style guidance.
- Add a row to the Candidates table with stack, best-fit, poor-fit, guidance links, and verification entry points.
