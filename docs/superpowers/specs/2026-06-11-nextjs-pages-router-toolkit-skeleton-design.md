# Next.js Pages Router Toolkit Skeleton Design

Date: 2026-06-11

## Goal

Refactor `frontend/apps/nextjs-pages` into a reusable work-bench frontend skeleton named `nextjs-pages-router-toolkit`.

The skeleton should clearly represent a traditional Next.js Pages Router project template for React applications that need file-based Pages Router compatibility, SSR entry points through `getServerSideProps`, authenticated product flows, API integration, mock data, tests, Storybook, and deployment-ready checks.

## Context

`frontend/apps/nextjs-pages` is already structured around Next.js Pages Router conventions and includes:

- Next.js, React, TypeScript, Tailwind CSS, TanStack Query, Zustand, React Hook Form, Zod, MSW, Vitest, Playwright, Storybook, and `next-router-mock`.
- Thin route files under `src/pages`.
- Application composition under `src/app`.
- Feature modules under `src/features`.
- Local docs under `docs/`.
- A local `AGENTS.md`.
- A skeleton-local CI workflow under `.github/workflows/`.

The current skeleton still contains upstream template identity and naming drift:

- The package name is `bulletproof-react-nextjs-pages`.
- README setup instructions point at the upstream Bulletproof React repository.
- Some docs still describe the generic upstream project rather than work-bench skeleton usage.
- The directory name `nextjs-pages` is understandable but less consistent with the newer toolkit naming used by the other skeletons.
- CI, docs, and visible identity should align with the final skeleton name.

## Selected Skills

This design uses four workflow perspectives:

- `skeleton-check`: keep the frontend skeleton index accurate and make this candidate easy to choose or reject.
- `web-frame`: preserve and clarify the Pages Router frontend structure, routing boundaries, test surfaces, and UI conventions.
- `doc-rules`: synchronize README, AGENTS, docs, package naming, and CI with the actual skeleton.
- `final-check`: verify the renamed skeleton with install, lint, typecheck, test, build, and e2e evidence, then remove generated artifacts.

## Recommended Approach

Use a standard skeletonization pass rather than a light rename or a deep product redesign.

The skeleton should be renamed to:

```text
frontend/apps/nextjs-pages-router-toolkit
```

The npm package should be renamed to:

```text
nextjs-pages-router-toolkit
```

This keeps the name parallel with `nextjs-app-router-toolkit` while making the Pages Router distinction explicit. It also fits the frontend skeleton index, where `skeleton-check` needs to distinguish App Router, Pages Router, and SPA candidates quickly.

## In Scope

- Rename the skeleton directory from `nextjs-pages` to `nextjs-pages-router-toolkit`.
- Update `frontend/README.md` so the candidate table points to the new path and describes the candidate accurately.
- Update package metadata and user-facing app identity to `Next.js Pages Router Toolkit`.
- Remove outdated upstream setup instructions and replace them with local skeleton usage instructions.
- Update local `AGENTS.md` to describe Pages Router rules, route composition, SSR entry points, scripts, and verification.
- Update local docs so they describe this skeleton rather than Bulletproof React.
- Rename the skeleton-local CI workflow to match the candidate name.
- Rename mock auth cookie values and related tests/docs to skeleton-owned names when they still carry old identity.
- Preserve the existing sample features, Pages Router files, test structure, Storybook setup, and mock API behavior unless a change is needed for the rename.
- Run relevant verification from the renamed skeleton directory.
- Clean generated files such as `node_modules`, `.next`, `coverage`, Playwright reports, Storybook output, local `.env`, and mock databases after verification.

## Out of Scope

- Upgrading Next.js, React, Storybook, Playwright, or other production dependencies.
- Rewriting the sample product domain.
- Adding new production dependencies.
- Converting this Pages Router skeleton into an App Router or SPA skeleton.
- Changing unrelated frontend candidates such as `nextjs-app-router-toolkit` or `react-spa-toolkit`.
- Committing unrelated existing work from other skeleton refactors.

## Architecture

The skeleton remains a Next.js Pages Router application.

Primary layers:

- `src/pages`: the actual Next.js routing layer. Files here should stay thin and should export route entries or SSR hooks.
- `src/app`: application composition, providers, layouts, and page implementation modules that keep route files small.
- `src/features`: feature-owned API calls, components, and domain UI.
- `src/components`: shared layout, SEO, form, dialog, table, notification, and primitive UI components.
- `src/lib`: API client, auth helpers, query utilities, authorization helpers, and cross-cutting client setup.
- `src/testing`: MSW handlers, router mocks, data generators, test utilities, and test setup.
- `docs`: local reusable guidance for API, state, testing, styling, performance, security, deployment, and structure.

The key architectural rule is that `src/pages` owns routing compatibility, not business logic. Reusable behavior should live in `src/app`, `src/features`, and shared modules so a copied project can evolve without turning page files into large mixed-responsibility modules.

## Data Flow

The skeleton keeps its existing frontend data flow:

1. Environment values are read through `src/config/env.ts`.
2. API calls go through the configured API client.
3. Server state is managed with TanStack Query.
4. UI state remains local first, with Zustand only for shared UI/application state.
5. Auth samples use the mock API and cookie-based token flow to model how a real API could issue secure cookies.
6. Tests use MSW, `next-router-mock`, and deterministic data generators to avoid relying on external services.
7. Pages Router SSR entry points should pass only route-level data and compose real UI from app or feature modules.

## Error Handling

The design preserves the current error-handling pattern:

- API errors are handled through shared API utilities and surfaced through UI states or notifications.
- Route-level 404 behavior remains in `src/pages/404.tsx`.
- Auth failures should produce deterministic mocked responses for tests.
- SSR hooks should return explicit redirects, props, or not-found behavior instead of swallowing errors.
- Documentation should describe expected real-project hardening without claiming the mock server provides production security.

## Testing And Verification

Verification should be run from:

```bash
cd frontend/apps/nextjs-pages-router-toolkit
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

- `frontend/apps/nextjs-pages` no longer exists, and `frontend/apps/nextjs-pages-router-toolkit` contains the renamed skeleton.
- `frontend/README.md` lists `apps/nextjs-pages-router-toolkit` as the Pages Router candidate.
- The skeleton no longer presents itself as Bulletproof React.
- The skeleton-local CI workflow points to `apps/nextjs-pages-router-toolkit`.
- Local docs and AGENTS guidance match the actual Pages Router skeleton.
- The app identity, package name, cookie names, and mock/test helpers use skeleton-owned names.
- Relevant verification commands pass or any environment-specific blocker is recorded with exact commands and output context.
- No generated artifacts or local environment files remain in the final worktree.

## Risks

- Existing uncommitted work for other skeletons may make `git status` noisy. The implementation must stage and report only intentional files.
- Because this skeleton intentionally uses Pages Router, broad text replacement from other Next.js skeletons could accidentally introduce App Router wording. Documentation and route references need a focused review.
- `next lint` behavior depends on the installed Next.js version and project config. Verification must use the package scripts rather than invented commands.
- Playwright and mock server processes can remain running after e2e. Cleanup must verify no related process remains.
