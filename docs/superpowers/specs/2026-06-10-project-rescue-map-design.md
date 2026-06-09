# Project Rescue Map Design

## Goal

Create a `project-rescue-map` skill for projects that have already started but did not go through the work-bench 00-10 workflow. The skill diagnoses workflow gaps and produces a stage-level rescue roadmap before any repair work.

## Scope

The skill only diagnoses and plans. It does not modify business code, create migrations, install dependencies, restructure directories, or generate PR plans.

## Recommended Shape

Use one skill, not two. `project-rescue-map` acts as a triage and routing entrypoint. Execution stays with the existing stage skills: `idea-check`, `data-map`, `talk-link`, `web-frame`, `server-frame`, `doc-rules`, and the rest of the 00-10 chain.

## Workflow

1. Confirm the target project root.
2. Read the nearest project rules and entry docs.
3. Scan product, stack, data, API, frontend, backend, delivery, docs, CI, and quality evidence.
4. Compare the project against the 01-10 workflow stages.
5. Mark each stage as `通过`, `部分具备`, `缺失`, `冲突`, or `不适用`.
6. Classify risks as `阻塞`, `必须补`, `可后补`, or `观察项`.
7. Output a rescue roadmap that points to existing stage skills.

## Output

The default output is a chat report. If the user explicitly asks to persist it, write:

- `docs/rescue/project-rescue-report.md`
- `docs/rescue/rescue-stateboard.md`

## Guardrails

- Do not repair during diagnosis.
- Do not invent missing docs, commands, APIs, schemas, tests, or run evidence.
- Do not treat file existence as stage completion.
- Do not expand into task-level or PR-level planning unless a later skill is invoked.
- If the project is too large, recommend decomposing by subsystem and run the diagnosis per subsystem.

## Acceptance

- The skill has clear trigger metadata.
- The body gives a deterministic diagnostic workflow.
- The output format is reusable.
- The skill routes repair work back to existing work-bench skills.
- Validation passes with the skill validation script.
