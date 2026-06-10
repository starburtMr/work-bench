# React SPA Toolkit Skeleton Design

## Goal

Rename and sharpen the frontend skeleton currently at `frontend/apps/react-vite` so it reflects its real role as a reusable, product-ready React SPA toolkit rather than a generic Vite starter.

The target skeleton name is `react-spa-toolkit`.

## Current Context

The existing skeleton already includes more than a minimal React/Vite setup:

- React 18, TypeScript, Vite, React Router, TanStack Query, Zustand, React Hook Form, Zod, Tailwind, Radix UI, and Lucide.
- Feature-first source structure under `src/features`.
- App-level route composition under `src/app`.
- API client, auth helpers, query client setup, env/path config, shared UI, layouts, and SEO helpers.
- MSW-backed local mocks, Vitest, Testing Library, Playwright e2e tests, Storybook stories, and Plop component generation.
- A demo team collaboration domain with auth, teams, discussions, comments, users, and profile flows.

The main mismatch is presentation: the directory name, package name, README, and several docs still describe it like a plain `react-vite` or upstream Bulletproof React example. That makes the skeleton harder for `skeleton-check` to select correctly.

## Recommended Skills To Apply Later

Use these skills during implementation and validation:

- `skeleton-check`: confirm the renamed skeleton is indexed correctly and still fits the frontend skeleton library rules.
- `web-frame`: review the SPA structure, routing, providers, shared UI, state, and API layer for reusable frontend skeleton quality.
- `doc-rules`: align README, AGENTS, and docs with the renamed skeleton and actual commands.
- `final-check`: verify the skeleton is reusable, documented, and passes the relevant checks before handoff.

## Naming Decision

Rename:

```text
frontend/apps/react-vite
```

to:

```text
frontend/apps/react-spa-toolkit
```

Rationale:

- `react-spa-toolkit` describes capability, not only build tooling.
- It remains broad enough for dashboards, internal tools, SaaS frontends, and authenticated business SPAs.
- It avoids over-narrow names such as `react-dashboard-spa`, because the current skeleton includes landing, auth, discussions, users, and profile flows.
- It makes `frontend/README.md` and `skeleton-check` selection clearer.

## Scope

Implementation should:

- Rename the skeleton directory to `frontend/apps/react-spa-toolkit`.
- Update `frontend/README.md` candidate links, stack description, best-fit guidance, and verification commands.
- Update the skeleton root `package.json` name to match the new skeleton.
- Rewrite the skeleton root `README.md` so it explains:
  - what the skeleton is for;
  - when to reuse it;
  - when not to reuse it;
  - setup commands;
  - verification commands;
  - mock server and e2e flow;
  - how to adapt the demo domain after copying into a real project.
- Update `AGENTS.md` to use the new path and accurate setup commands.
- Update local docs under `docs/` where they still have stale upstream wording, stale path references, or incorrect config filenames.
- Remove or reword Bulletproof React branding where it makes this work-bench skeleton look like an upstream clone rather than a curated reusable candidate.
- Keep the existing demo team collaboration domain as a reference business flow.
- Keep the current app architecture and dependency set unless a small fix is required for verification.

## Non-Goals

Do not:

- Replace the demo business domain with a new product.
- Redesign the UI.
- Upgrade React, Vite, Storybook, Playwright, or other dependencies as part of this rename.
- Convert the app to Next.js or another router/runtime.
- Add new runtime features.
- Commit generated output such as `node_modules`, `dist`, coverage reports, or Storybook build artifacts.

## Expected Structure

After implementation, the frontend skeleton library should include:

```text
frontend/
  README.md
  apps/
    react-spa-toolkit/
      README.md
      AGENTS.md
      package.json
      docs/
      src/
      e2e/
      public/
      generators/
```

The real project copy behavior remains unchanged: `skeleton-check` may copy this skeleton into a target project's `frontend/` directory unless the user requested another target path.

## Documentation Rules

Docs should use work-bench language:

- Say "skeleton", "candidate", and "reuse" where appropriate.
- Avoid instructing users to clone the upstream repository.
- Prefer local relative links over external links when explaining this skeleton.
- Keep external references only as optional learning resources.
- Ensure config filenames match the repo, such as `eslint.config.mjs` and `.prettierrc`.
- Ensure setup examples use the renamed directory.

## Verification

Run verification from `frontend/apps/react-spa-toolkit`:

```bash
yarn install --frozen-lockfile
yarn lint
yarn check-types
yarn test
yarn build
```

Run `yarn test-e2e` if the mock server and browser dependencies are available in the environment. If not, document the blocker and leave the exact command for follow-up.

Also run static checks from the repo root:

```bash
rg -n "apps/react-vite|bulletproof-react|React Vite Application|\\.env\\.example|\\.eslintrc\\.cjs" frontend
find frontend/apps/react-spa-toolkit -maxdepth 3 -type d \( -name node_modules -o -name dist -o -name coverage -o -name storybook-static \)
```

The first command may still find intentional package names or optional learning resources only if they are explicitly explained. The second command should return no generated directories before finishing.

## Acceptance Criteria

- `frontend/apps/react-vite` no longer exists.
- `frontend/apps/react-spa-toolkit` exists and contains the previous skeleton content.
- `frontend/README.md` lists `apps/react-spa-toolkit` as the React SPA candidate.
- The skeleton README and AGENTS file describe the actual skeleton and commands.
- Local docs no longer mislead readers with upstream clone instructions or stale config references.
- Existing demo flows are preserved.
- Relevant checks pass or any environmental blocker is reported precisely.
