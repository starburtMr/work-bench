---
title: "docs: Add Context7-first rules to skeleton skills"
type: "docs"
date: "2026-06-11"
origin: "docs/superpowers/specs/2026-06-11-context7-skill-doc-rules-design.md"
---

# docs: Add Context7-first rules to skeleton skills

## Summary

Add a Context7-first official documentation rule to the frontend and backend skeleton skills. The change keeps Context7 as the preferred lookup path, preserves official-source fallbacks, and makes documentation evidence part of skeleton deliverables.

---

## Problem Frame

`06-web-frame` and `07-server-frame` already prefer mature frameworks and official capabilities, but only the backend skill currently has an explicit official-reference section. Neither skill clearly tells agents to use Context7 before relying on current framework, CLI, configuration, or skeleton conventions.

The approved design requires a practical rule: use Context7 first, fall back to official or primary sources when Context7 is unavailable or incomplete, and record the evidence when it affects architecture or commands.

---

## Requirements

- R1. `06-web-frame` defines Context7 as the preferred first lookup path for version-sensitive frontend framework, CLI, routing, styling, component-library, API, mock, and quality-tool decisions.
- R2. `07-server-frame` strengthens its existing official-documentation section with Context7-first lookup, official-source fallback, and evidence-recording rules.
- R3. Both skills allow documented fallback when Context7 is unavailable, quota-limited, missing a library, or insufficient for the question.
- R4. Both skills prohibit sending secrets, private connection strings, internal URLs, or credential-bearing config into documentation lookup queries.
- R5. Both skills tell agents where to record documentation evidence in their downstream deliverables.
- R6. The implementation only edits the two skill files and does not change skeleton code, templates, dependencies, global instructions, or reference matrices.

---

## Key Technical Decisions

- **Context7-first, not Context7-only:** The approved policy avoids blocking skeleton work on tool outages while still preventing memory-based framework claims.
- **Patch skill rules near existing decision points:** The frontend rule belongs after mature-solution guidance; the backend rule belongs inside the existing official-documentation section to avoid two competing policies.
- **Evidence belongs in generated deliverables:** The skill text should name the frontend and backend documents that must carry documentation evidence, so the rule survives beyond chat history.
- **No reference-matrix rewrite:** Existing matrices remain useful background. This change adds an execution protocol rather than updating every framework row.

---

## Scope Boundaries

### In Scope

- Add concise Context7-first rule text to `.codex/skills/06-web-frame/SKILL.md`.
- Strengthen `.codex/skills/07-server-frame/SKILL.md` without changing its current official-reference matrix structure.
- Add verification language that makes fallback reasons and evidence locations clear.

### Deferred to Follow-Up Work

- Updating templates under `.codex/skills/06-web-frame/templates/` or `.codex/skills/07-server-frame/templates/`.
- Adding a shared helper skill for documentation lookup across all project skills.
- Installing or configuring Context7 MCP servers.

### Out of Scope

- Changing frontend or backend skeleton application code.
- Changing package versions, CLIs, dependencies, or generated project files.
- Editing global `AGENTS.md` or user-level Codex rules.

---

## Implementation Units

### U1. Add frontend Context7-first rule

- **Goal:** Make `06-web-frame` require Context7-first official documentation checks before frontend skeleton decisions that depend on current framework or tool behavior.
- **Requirements:** R1, R3, R4, R5, R6.
- **Dependencies:** None.
- **Files:** `.codex/skills/06-web-frame/SKILL.md`.
- **Approach:** Add a new subsection after `#### 3.2 成熟方案优先`. The subsection should state the Context7 lookup flow, fallback chain, secret-safety rule, and evidence locations for frontend deliverables.
- **Patterns to follow:** Existing numbered section style under `### 3. 最高优先级原则`; approved design in `docs/superpowers/specs/2026-06-11-context7-skill-doc-rules-design.md`.
- **Test scenarios:** Test expectation: none -- this is a documentation-rule change with no executable behavior.
- **Verification:** The frontend skill contains a clear Context7-first rule, includes fallback behavior, and names frontend deliverables for evidence recording.

### U2. Strengthen backend official-documentation rule

- **Goal:** Make `07-server-frame` apply Context7-first lookup inside its existing official-documentation policy.
- **Requirements:** R2, R3, R4, R5, R6.
- **Dependencies:** None.
- **Files:** `.codex/skills/07-server-frame/SKILL.md`.
- **Approach:** Update `### 3. 官方资料驱动的工程原则` without duplicating it elsewhere. Keep the official-reference matrix intact, then add Context7 lookup, fallback, safety, and evidence-recording requirements around the existing final sentence.
- **Patterns to follow:** Existing backend section language that emphasizes official docs, framework-native capabilities, and evidence-based acceptance.
- **Test scenarios:** Test expectation: none -- this is a documentation-rule change with no executable behavior.
- **Verification:** The backend skill references Context7 as preferred lookup, still supports official fallback, and names backend deliverables for evidence recording.

### U3. Verify scope and consistency

- **Goal:** Confirm the final diff is narrow and the two skills express the same policy without contradicting existing rules.
- **Requirements:** R3, R4, R5, R6.
- **Dependencies:** U1, U2.
- **Files:** `.codex/skills/06-web-frame/SKILL.md`, `.codex/skills/07-server-frame/SKILL.md`.
- **Approach:** Review the diff for unintended files, duplicate rules, contradictory wording, absolute-path leakage in user-facing rule text, and accidental changes to skeleton templates or package files.
- **Patterns to follow:** The approved verification plan in `docs/superpowers/specs/2026-06-11-context7-skill-doc-rules-design.md`.
- **Test scenarios:** Test expectation: none -- verification is diff and text review for documentation-only changes.
- **Verification:** The final diff only includes the two skill files, both mention Context7-first behavior, both allow documented fallback, and neither includes secrets or implementation changes.

---

## Risks & Dependencies

- **Rule drift risk:** If frontend and backend wording diverges, future agents may apply different fallback behavior. Keep the shared policy language consistent while allowing framework-specific examples.
- **Overly rigid wording risk:** If the text says Context7 is mandatory in all cases, skeleton work may block on quota or network failures. The implementation must say preferred first lookup with documented fallback.
- **Template gap:** Existing deliverable templates may not have a dedicated evidence section. This plan intentionally leaves template changes deferred; implementers should phrase the rule so evidence can land in existing ADR, blueprint, runbook, quality, and acceptance sections.

---

## Documentation / Operational Notes

The implementation should preserve the Chinese style of both skill files. The Context7 command examples may remain in English-style CLI syntax, but surrounding instructions should match the existing Chinese documentation.

---

## Sources & Research

- `docs/superpowers/specs/2026-06-11-context7-skill-doc-rules-design.md` is the approved design source.
- `.codex/skills/06-web-frame/SKILL.md` currently has mature-solution guidance but no Context7 rule.
- `.codex/skills/07-server-frame/SKILL.md` currently has an official-documentation section and should be strengthened in place.
- Context7 CLI docs confirm the lookup flow: resolve a library ID first, then query documentation with `ctx7 docs <library-id> <question>`.
