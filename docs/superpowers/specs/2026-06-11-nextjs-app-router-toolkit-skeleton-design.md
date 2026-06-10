# Next.js App Router Toolkit Skeleton Design

Date: 2026-06-11

## Goal

Refactor `frontend/apps/nextjs-app` into a reusable work-bench frontend skeleton named `nextjs-app-router-toolkit`.

The skeleton should clearly represent a Next.js App Router project template for modern React applications that need route groups, layouts, server-capable routing, client interactivity, API integration, mock data, tests, Storybook, and deployment-ready checks.

## Context

`frontend/apps/nextjs-app` is already structured around Next.js App Router conventions and includes:

- Next.js, React, TypeScript, Tailwind CSS, TanStack Query, Zustand, React Hook Form, Zod, MSW, Vitest, Playwright, and Storybook.
- `src/app` route groups for authenticated, auth, and public flows.
- Local docs under `docs/`.
- A local `AGENTS.md`.
- CI workflow files under `.github/workflows/`.

The current skeleton still contains upstream template identity and naming drift:

- The package name is `bulletproof-react-nextjs-pages`, which conflicts with its App Router implementation.
- README setup instructions point at the upstream Bulletproof React repository.
- App metadata, visible copy, docs, cookie names, and mock helpers still reference Bulletproof React.
- The skeleton-local workflow directory includes workflows for other frontend candidates.

## Selected Skills

This design uses four workflow perspectives:

- `skeleton-check`: keep the skeleton library index accurate and make the candidate easy to choose or reject.
- `web-frame`: preserve and clarify the App Router frontend structure, routing boundaries, test surfaces, and UI conventions.
- `doc-rules`: synchronize README, AGENTS, docs, package naming, and CI with the actual skeleton.
- `final-check`: verify the renamed skeleton with install, lint, typecheck, test, build, and e2e evidence, then remove generated artifacts.

## Recommended Approach

Use a standard skeletonization pass rather than a light rename or deep product redesign.

The skeleton should be renamed to:

```text
frontend/apps/nextjs-app-router-toolkit
```

The npm package should be renamed to:

```text
nextjs-app-router-toolkit
```

This matches the naming style already used by `react-spa-toolkit` and `typescript-backend-toolkit`, while making the App Router distinction explicit.

## In Scope

- Rename the skeleton directory from `nextjs-app` to `nextjs-app-router-toolkit`.
- Update `frontend/README.md` so the candidate table points to the new path and describes the candidate accurately.
- Update package metadata and user-facing app identity to `Next.js App Router Toolkit`.
- Remove outdated upstream setup instructions and replace them with local skeleton usage instructions.
- Update local `AGENTS.md` to describe App Router rules, route composition, server/client boundaries, scripts, and verification.
- Update local docs so they describe this skeleton rather than Bulletproof React.
- Rename and trim CI workflow files so the skeleton-local workflows only apply to this candidate.
- Rename mock auth cookie values and related tests/docs to skeleton-owned names.
- Preserve the existing sample features, route groups, test structure, Storybook setup, and mock API behavior unless a change is needed for the rename.
- Run relevant verification from the renamed skeleton directory.
- Clean generated files such as `node_modules`, `.next`, `coverage`, Playwright reports, Storybook output, local `.env`, and mock databases after verification.

## Out of Scope

- Upgrading Next.js, React, Storybook, Playwright, or other production dependencies.
- Rewriting the sample product domain.
- Adding new production dependencies.
- Converting this App Router skeleton into a Pages Router or SPA skeleton.
- Changing unrelated frontend candidates such as `nextjs-pages` or `react-spa-toolkit`.
- Committing unrelated existing work from other skeleton refactors.

## Architecture

The skeleton remains a Next.js App Router application.

Primary layers:

- `src/app`: route groups, layouts, pages, metadata, provider wiring, and route-level composition.
- `src/features`: feature-owned API calls, components, and domain UI.
- `src/components`: shared layout, form, dialog, table, notification, and primitive UI components.
- `src/lib`: API client, auth helpers, query utilities, and cross-cutting client setup.
- `src/testing`: MSW handlers, data generators, test utilities, and test setup.
- `docs`: local reusable guidance for API, state, testing, styling, performance, security, deployment, and structure.

Route files should stay thin. They should compose feature modules and shared components instead of owning business logic.

## Data Flow

The skeleton keeps its existing frontend data flow:

1. Environment values are read through `src/config/env.ts`.
2. API calls go through the configured API client.
3. Server state is managed with TanStack Query.
4. UI state remains local first, with Zustand only for shared UI/application state.
5. Auth samples use the mock API and cookie-based token flow to model how a real API could issue secure cookies.
6. Tests use MSW and deterministic data generators to avoid relying on external services.

## Error Handling

The design preserves the current error-handling pattern:

- API errors are handled through shared API utilities and surfaced through UI states or notifications.
- Route-level failures should be handled by App Router boundaries when applicable.
- Auth failures should produce deterministic mocked responses for tests.
- Documentation should describe expected real-project hardening without claiming the mock server provides production security.

## Testing And Verification

Verification should be run from:

```bash
cd frontend/apps/nextjs-app-router-toolkit
```

Expected checks:

```bash
yarn install --frozen-lockfile
yarn lint
yarn check-types
yarn test --run
yarn build
yarn test-e2e
```

If e2e requires environment values, copy the existing example file to `.env` for local verification and remove it afterward.

Generated artifacts must be removed after verification so the skeleton remains clean.

## Success Criteria

- `frontend/apps/nextjs-app` no longer exists, and `frontend/apps/nextjs-app-router-toolkit` contains the renamed skeleton.
- `frontend/README.md` lists `apps/nextjs-app-router-toolkit` as the App Router candidate.
- The skeleton no longer presents itself as Bulletproof React or as a Pages Router package.
- The skeleton-local CI workflow points to `apps/nextjs-app-router-toolkit`.
- Local docs and AGENTS guidance match the actual skeleton.
- Relevant verification commands pass or any environment-specific blocker is recorded with exact commands and output context.
- No generated artifacts or local environment files remain in the final worktree.

## Risks

- Existing uncommitted work for other skeletons may make `git status` noisy. The implementation must stage and report only intentional files.
- Workflow files live inside the skeleton directory. Renaming them must not accidentally preserve references to old candidates.
- Next.js App Router server/client boundaries can break subtly during text renames. Typecheck and build are required.
- Playwright and mock server processes can remain running after e2e. Cleanup must verify no related process remains.

