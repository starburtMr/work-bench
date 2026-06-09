# Workflow Project Root and Skeleton Requirements

## 1. Purpose

This document defines how the full `build-map` workflow should use the work-bench repository, target project roots, generated documents, and frontend/backend skeletons.

The goal is to prevent confusion between:

- the work-bench repository, which stores skills and reusable skeleton candidates;
- the target project root, which receives project-specific docs, frontend code, backend code, plans, rules, and verification evidence.

## 2. Terms

| Term | Meaning |
|---|---|
| `work-bench` | `/home/xiaoyaozu/AI/projects/work-bench`; the skill and skeleton library repository. |
| target project root | The real project directory selected by the user. In examples and skill text, use `<project-root>`. |
| frontend skeleton library | `work-bench/frontend/apps/*`. |
| backend skeleton library | `work-bench/backend/apps/*`. |
| frontend delivery target | Default: `<project-root>/frontend`, unless the user explicitly asks for another path. |
| backend delivery target | Default: `<project-root>/backend`, unless the user explicitly asks for another path. |

Do not use single-letter placeholders in skill instructions or workflow docs. Use `target project root`, `real project root`, `<project-root>`, `frontend delivery target`, and `backend delivery target`.

## 3. Repository Responsibilities

### 3.1 work-bench

`work-bench` is only responsible for:

- storing workflow skills under `.codex/skills/*`;
- storing frontend skeleton candidates under `frontend/apps/*`;
- storing backend skeleton candidates under `backend/apps/*`;
- maintaining skeleton index files:
  - `frontend/README.md`
  - `backend/README.md`

`work-bench` is not the default output location for project-specific docs, code, plans, or final verification reports.

### 3.2 target project root

The target project root is responsible for project-specific output:

```text
<project-root>/
  docs/
  frontend/
  backend/
  README.md
  AGENTS.md
```

Default delivery paths:

- frontend: `<project-root>/frontend`
- backend: `<project-root>/backend`
- workflow docs: `<project-root>/docs/...`

If the user explicitly requests different paths, record those paths in the project docs and use them consistently for the rest of the workflow.

The target project root should not receive an `apps` directory by default. The `apps` directories belong to the work-bench skeleton libraries only.

## 4. Workflow Requirements

### 4.1 idea-check

`idea-check` must identify the target project root before any project-specific files are written.

Rules:

- If the target project root is unknown, ask the user for it.
- If the target project root does not exist, ask for confirmation before creating it.
- If the user only wants analysis and no file writes, the workflow may proceed with an explicitly marked path assumption.
- Before writing, copying, or generating files, the target project root must be confirmed.
- If only frontend or only backend is in scope, only record and create the relevant delivery target.

Outputs go under:

- `<project-root>/docs/product/*`

Required path output:

- `<project-root>/docs/product/bootstrap-targets.md`

That document must record:

- target project root;
- frontend delivery target, if frontend is in scope;
- backend delivery target, if backend is in scope;
- any user-specified non-default paths.

### 4.2 tool-pick

`tool-pick` uses the product documents from the target project root and writes architecture decisions to:

- `<project-root>/docs/architecture/*`

It must not write project-specific technology decisions into `work-bench`.

### 4.3 data-map

`data-map` uses product and technology decisions from the target project root and writes database design output to:

- `<project-root>/docs/database/*`

### 4.4 talk-link

`talk-link` uses product, technology, and database documents from the target project root and writes API contract output to:

- `<project-root>/docs/api/*`

### 4.5 skeleton-check

`skeleton-check` bridges the work-bench skeleton libraries and the target project root.

Before scanning candidate directories, it must read:

- `work-bench/frontend/README.md`
- `work-bench/backend/README.md`

Those README files are skeleton indexes only. They must describe available candidates in the work-bench library and must not contain target-project-root delivery rules.

Then `skeleton-check` scans:

- `work-bench/frontend/apps/*`
- `work-bench/backend/apps/*`

For each side in scope, it produces either:

- `reuse`: select an existing skeleton candidate and copy it to the delivery target;
- `create`: create a new reusable skeleton candidate in the work-bench skeleton library, update the relevant skeleton index README, then copy it to the delivery target.

Default copy destinations:

- selected frontend skeleton -> `<project-root>/frontend`
- selected backend skeleton -> `<project-root>/backend`

Unless the user explicitly requests otherwise, do not copy into:

- `<project-root>/frontend/apps`
- `<project-root>/backend/apps`

Outputs go under:

- `<project-root>/docs/skeleton/*`

Required outputs include:

- `<project-root>/docs/skeleton/skeleton-selection-report.md`
- `<project-root>/docs/skeleton/frontend-selection.md`, if frontend is in scope
- `<project-root>/docs/skeleton/backend-selection.md`, if backend is in scope
- `<project-root>/docs/skeleton/delivery-targets.md`

### 4.6 web-frame

`web-frame` runs after a frontend skeleton exists at the frontend delivery target.

It customizes the copied skeleton for the current project using:

- product docs;
- architecture decisions;
- API contract;
- skeleton selection report;
- user requirements.

It works in the frontend delivery target, defaulting to:

- `<project-root>/frontend`

Outputs go under:

- `<project-root>/docs/frontend/*`

### 4.7 server-frame

`server-frame` runs after a backend skeleton exists at the backend delivery target.

It customizes the copied skeleton for the current project using:

- product docs;
- architecture decisions;
- database design;
- API contract;
- skeleton selection report;
- user requirements.

It works in the backend delivery target, defaulting to:

- `<project-root>/backend`

Outputs go under:

- `<project-root>/docs/backend/*`

### 4.8 work-plan

`work-plan` runs after the target project root has:

- project docs;
- selected/copied frontend skeleton, if frontend is in scope;
- selected/copied backend skeleton, if backend is in scope;
- frontend/backend project-specific baseline docs.

Outputs go under:

- `<project-root>/docs/delivery/*`

### 4.9 doc-rules

`doc-rules` synchronizes the target project root, not the work-bench repository.

It updates, creates, or verifies:

- `<project-root>/README.md`
- `<project-root>/AGENTS.md`
- `<project-root>/docs/README.md` or `<project-root>/docs/index.md`
- `<project-root>/.github/workflows/*`, if CI is in scope

### 4.10 final-check

`final-check` verifies the target project root using real evidence.

It checks:

- target project docs;
- frontend/backend code under their delivery targets;
- README and AGENTS.md;
- CI configuration;
- real commands, tests, builds, runtime checks, logs, API responses, or explicit unverified reasons.

Outputs go under:

- `<project-root>/docs/quality/*`

It must not mark unexecuted commands as passing.

## 5. Skeleton Index README Requirements

The following files are skeleton library indexes:

- `work-bench/frontend/README.md`
- `work-bench/backend/README.md`

They must answer:

- What skeleton candidates exist?
- What technology stack does each candidate use?
- What project type is each candidate best for?
- What project type is each candidate not suitable for?
- Where is the candidate directory?
- Where are its local README, AGENTS.md, docs, and verification commands?

They must not describe:

- a specific target project root;
- `<project-root>/frontend`;
- `<project-root>/backend`;
- user-specific delivery paths.

When a new skeleton candidate is added to `frontend/apps/*` or `backend/apps/*`, the corresponding README index must be updated in the same change.

## 6. Default Structure and Overrides

Default target project structure:

```text
<project-root>/
  docs/
  frontend/
  backend/
  README.md
  AGENTS.md
```

Override rule:

- If the user explicitly asks for another frontend or backend path, use the user's path.
- Record the override in:
  - `<project-root>/docs/product/bootstrap-targets.md`
  - `<project-root>/docs/skeleton/delivery-targets.md`
- Every downstream skill must use the recorded delivery target instead of recomputing or assuming paths.

## 7. Non-Goals

This workflow must not:

- treat `work-bench` as the target project root by default;
- write target-project-specific docs into `work-bench`;
- copy `frontend/apps` or `backend/apps` as nested `apps` directories into the target project root;
- store target-project-root rules inside `frontend/README.md` or `backend/README.md`;
- create both frontend and backend directories when the user only requests one side;
- silently create a missing target project root without confirmation.

## 8. Acceptance Criteria

- Skills use `<project-root>` or equivalent wording instead of a single-letter placeholder.
- `idea-check` confirms the target project root before file writes.
- `tool-pick`, `data-map`, `talk-link`, `work-plan`, `doc-rules`, and `final-check` write project-specific outputs under `<project-root>/docs/...`.
- `skeleton-check` reads the frontend/backend README indexes before scanning skeleton candidates.
- Reused skeletons are copied from the work-bench skeleton libraries to the recorded delivery targets.
- Newly created skeleton candidates are added to the work-bench skeleton library and indexed in the relevant README before being copied to the target project.
- The target project root does not receive an `apps` directory unless the user explicitly requests it.
- Final verification uses real target project evidence and records unverified checks honestly.
