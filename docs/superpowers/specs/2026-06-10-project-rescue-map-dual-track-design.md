# Project Rescue Map Dual-Track Optimization Design

## Goal

Optimize `project-rescue-map` by adding a five-area management view on top of the existing 00-10 execution workflow.

The change should make rescue reports easier to understand without replacing the current detailed skills. The five-area view is for quick diagnosis and prioritization; the 00-10 workflow remains the execution layer for actual repair work.

## Context

The inspected `work-bench-optimized.zip` compresses the full workflow into five stages:

- scope
- architecture
- skeletons
- delivery
- verification

That compression is useful as a management view, but its simplified `project-rescue-map` is weaker than the current local version. The current local skill already has stronger rescue behavior, including evidence grading, stage-aware safety gates, risk applicability, run-based output paths, and richer templates.

Therefore, this design keeps the existing 00-10 skills and adds a five-area summary layer instead of replacing the workflow.

## Non-Goals

- Do not rename existing skills.
- Do not delete or migrate the 00-10 skill directories.
- Do not adopt the zip's `define-scope`, `design-architecture`, `prepare-skeletons`, `plan-delivery`, or `verify-release` skill names as real directories.
- Do not overwrite the current enhanced `project-rescue-map`.
- Do not modify frontend or backend skeleton code.

## Dual-Track Model

### Management View

The management view groups the 00-10 workflow into five areas:

| Management area | Mapped execution stages | Purpose |
|---|---|---|
| Scope | `01-idea-check` | Product goal, V1 boundary, user journey, acceptance clarity |
| Architecture | `02-tool-pick`, `03-data-map`, `04-talk-link` | Stack, data model, API contract, dependency and integration consistency |
| Skeleton | `05-skeleton-check`, `06-web-frame`, `07-server-frame` | Frontend/backend skeleton choice, directory responsibility, runnable baseline |
| Delivery | `08-work-plan`, `09-doc-rules` | Vertical slices, README, AGENTS, docs index, CI and collaboration rules |
| Verification | `10-final-check` | Tests, build, release readiness, rollback, safety and evidence pack |

### Execution View

The 00-10 workflow remains the detailed repair map:

1. `idea-check`
2. `tool-pick`
3. `data-map`
4. `talk-link`
5. `skeleton-check`
6. `web-frame`
7. `server-frame`
8. `work-plan`
9. `doc-rules`
10. `final-check`

`project-rescue-map` should use the management view to explain where the project is unhealthy, then use the execution view to point to the exact skill or sequence needed for repair.

## Report Behavior

When invoked as:

```bash
project-rescue-map <project-root>
```

the skill should continue writing to:

```text
<project-root>/docs/rescue/runs/<run-id>/
<project-root>/docs/rescue/index.md
```

The main rescue report should present results in this order:

1. Project stage and safety decision.
2. Five-area management summary.
3. 00-10 execution-stage gap matrix.
4. Risk register and applicability.
5. Recommended rescue route.
6. Evidence ledger and command log.

The management summary should include:

| Field | Meaning |
|---|---|
| `management_area` | One of Scope, Architecture, Skeleton, Delivery, Verification |
| `mapped_stages` | The 00-10 stages represented by the area |
| `area_status` | Aggregated state for that area |
| `key_findings` | Short evidence-backed diagnosis |
| `first_repair_action` | First concrete repair step and target skill |
| `risk_level` | Highest relevant risk level in the area |
| `confidence` | Evidence confidence for the area conclusion |

## Status Aggregation

Area status should be derived conservatively from mapped execution stages:

- `STOP` if any applicable mapped stage contains a stop-level safety issue.
- `冲突` if mapped stages contradict each other in docs, code, config, schema, API, or commands.
- `缺失` if the area has no usable source of truth.
- `部分具备` if some evidence exists but important gates are incomplete or unverified.
- `通过` only when mapped stages have enough evidence and no material conflict.
- `不可验证` when permissions, environment, or missing evidence prevent judgment.
- `不适用` only when the project shape clearly does not need that area, with reason.

For prototype or early MVP projects, missing future-only capabilities such as payment, production privacy controls, or mature release operations should be marked as `未来门禁` or `暂不适用`, not automatically as `STOP`.

## Files To Update During Implementation

Expected implementation files:

- `.codex/skills/project-rescue-map/SKILL.md`
- `.codex/skills/project-rescue-map/templates/02_stage_gap_matrix.md`
- `.codex/skills/project-rescue-map/templates/03_project_rescue_report.md`
- `.codex/skills/project-rescue-map/templates/06_risk_register.md` if risk mapping needs a management-area column
- `.codex/skills/project-rescue-map/references/scoring-model.md` if aggregation rules belong there
- `README.md` for the repository-level dual-track explanation
- `WORKFLOW.md` if present or intentionally created as a workflow overview

Implementation should preserve existing run output rules and all stage-aware safety behavior already added to `project-rescue-map`.

## Testing And Verification

After implementation:

1. Run the skill validator:

   ```bash
   python3 /home/xiaoyaozu/.codex/skills/.system/skill-creator/scripts/quick_validate.py /home/xiaoyaozu/AI/projects/work-bench/.codex/skills/project-rescue-map
   ```

2. Run whitespace diff validation:

   ```bash
   git -C /home/xiaoyaozu/AI/projects/work-bench diff --check -- .codex/skills/project-rescue-map README.md WORKFLOW.md
   ```

3. Inspect the final diff to confirm:

   - no existing 00-10 skill was renamed or deleted
   - `project-rescue-map` still writes to `docs/rescue/runs/<run-id>/`
   - the report contains both five-area summary and 00-10 detailed matrix
   - prototype-stage safety noise remains controlled

## Acceptance Criteria

- A reader can understand project health from the five-area summary before reading the detailed 00-10 matrix.
- Every five-area conclusion maps back to concrete 00-10 stages and target skills.
- Existing `project-rescue-map` safety, evidence, run-id, and output-path rules remain intact.
- Repository docs explain the dual-track model without implying that the 00-10 workflow has been replaced.
- No business code or skeleton implementation files are changed.
