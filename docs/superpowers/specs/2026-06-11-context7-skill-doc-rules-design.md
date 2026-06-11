# Context7 Skill Documentation Rules Design

## Goal

Update the project-level `06-web-frame` and `07-server-frame` skills so frontend and backend skeleton creation or optimization is grounded in current official documentation.

The rule should make Context7 the preferred documentation lookup path while keeping a practical fallback chain for outages, limits, missing libraries, or incomplete Context7 results.

## Scope

This design covers only skill documentation changes under:

- `.codex/skills/06-web-frame/SKILL.md`
- `.codex/skills/07-server-frame/SKILL.md`

It does not change frontend or backend skeleton code, templates, package versions, or generated project files.

## Recommended Approach

Use a Context7-first official documentation rule.

When either skill needs to choose, create, normalize, or validate framework-specific behavior, the agent should first query Context7:

```bash
npx ctx7@latest library <official-library-name> "<current skeleton question>"
npx ctx7@latest docs <library-id> "<current skeleton question>"
```

This applies to framework behavior, CLI commands, project structure, routing, configuration, package setup, test setup, styling systems, API conventions, and version-sensitive implementation details.

If Context7 is unavailable or insufficient, the agent may fall back to official sources in this order:

1. Official documentation website, including `/llms.txt` or `/llms-full.txt` when available.
2. Official GitHub repository docs, README, examples, or release notes.
3. Official vendor MCP documentation sources when relevant.
4. Trusted extraction/search tools such as Firecrawl or web search, limited to official or primary sources.

The agent must record the fallback reason when it does not use Context7.

## Frontend Skill Design

Add a new rule section after `06-web-frame`'s mature-solution guidance.

The section should state:

- Do not rely on memory for current framework, CLI, routing, styling, component-library, or test-tool behavior.
- Use Context7 before deciding or implementing rules for tools such as React, Vite, Next.js, Vue, Nuxt, Angular, SvelteKit, Astro, Expo, Tailwind CSS, shadcn/ui, TanStack Query, MSW, Vitest, Playwright, ESLint, and Prettier.
- If the project already has fixed technology choices, Context7 should be used to verify the chosen stack's current official setup and skeleton conventions, not to reopen unrelated stack decisions.
- Record documentation evidence in frontend deliverables when the evidence affects architecture or commands.

Expected evidence locations:

- `docs/frontend/frontend-blueprint.md`
- `docs/frontend/architecture-decision-record.md`
- `docs/frontend/quality-gates.md`
- `docs/frontend/ai-guardrails.md`

## Backend Skill Design

Strengthen `07-server-frame`'s existing official-documentation section instead of adding a separate competing policy.

The section should state:

- Context7 is the preferred first lookup path for current framework, CLI, configuration, routing, validation, error handling, logging, health check, API docs, and testing behavior.
- Framework-native capabilities remain preferred, but the claim must be grounded in current official docs when the behavior is version-sensitive.
- Use Context7 for frameworks and libraries such as FastAPI, Django, Django REST Framework, NestJS, Express, Spring Boot, Laravel, Gin, Pydantic, OpenAPI tooling, logging/config libraries, and test runners when they shape the skeleton.
- Do not query Context7 with secrets, private connection strings, internal URLs, or credential-bearing config.
- Record fallback reasons when Context7 cannot provide usable documentation.

Expected evidence locations:

- `docs/backend/backend-architecture-source-of-truth.md`
- `docs/backend/runbook.md`
- `docs/backend/security-baseline.md`
- `docs/backend/acceptance-report.md`

## Execution Rules

The implementation should add concise, reusable language to both skills:

- Context7 is preferred, not an absolute blocker.
- Official and primary sources are required for fallback.
- Version-sensitive claims need evidence.
- Evidence should be summarized, not copied at length.
- Do not exceed necessary documentation queries.
- If Context7 fails because of quota or login requirements, report the limitation and continue with official fallback sources.

## Non-Goals

- Installing or configuring new MCP servers.
- Replacing Context7 with another service.
- Changing global `AGENTS.md` rules.
- Adding package dependencies to skeleton projects.
- Rewriting the existing official reference matrices.

## Verification Plan

After implementation:

1. Inspect the diff for only the two intended skill files.
2. Confirm `06-web-frame` contains an explicit Context7-first rule and evidence requirements.
3. Confirm `07-server-frame` strengthens the existing official-documentation section without contradiction.
4. Confirm the wording allows documented fallback when Context7 is unavailable.
5. Confirm no secrets, package changes, or unrelated files are touched.

## Open Decisions

None. The selected policy is Context7-first with official fallback and evidence recording.
