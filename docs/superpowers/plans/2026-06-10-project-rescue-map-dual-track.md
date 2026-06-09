# Project Rescue Map Dual-Track Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a five-area management summary to `project-rescue-map` while preserving the existing 00-10 execution workflow.

**Architecture:** Keep 00-10 as the detailed repair layer and add a five-area management layer for report readability. The skill instructions define the dual-track model, templates expose it in generated reports, and docs explain that this is an overlay rather than a migration.

**Tech Stack:** Markdown-based Codex skills, skill metadata JSON/YAML, existing `skill-creator` validator, Git diff checks.

---

## File Structure

- Modify `.codex/skills/project-rescue-map/SKILL.md`: add the dual-track model, five-area mapping, report ordering, and aggregation rules.
- Modify `.codex/skills/project-rescue-map/templates/03_project_rescue_report.md`: add a five-area management summary before the 00-10 stage matrix.
- Modify `.codex/skills/project-rescue-map/templates/02_stage_gap_matrix.md`: add management-area fields and mapping guidance without removing the 00-10 rows.
- Modify `.codex/skills/project-rescue-map/templates/06_risk_register.md`: add a management-area column so risks can roll up into the five-area summary.
- Modify `.codex/skills/project-rescue-map/references/scoring-model.md`: document conservative aggregation from detailed stages to five-area status.
- Modify `README.md`: explain work-bench as a skill/skeleton library with dual-track workflow vocabulary.
- Create or modify `WORKFLOW.md`: document 00-10 execution layer plus five-area management layer.

Do not rename, delete, or migrate existing 00-10 skill directories. Do not change frontend/backend skeleton implementation files.

---

### Task 1: Add Dual-Track Model To The Skill

**Files:**
- Modify: `.codex/skills/project-rescue-map/SKILL.md`

- [ ] **Step 1: Locate the workflow-position and stage-matrix sections**

Run:

```bash
rg -n "在完整 work-bench 工作流中的位置|对照基线|阶段缺口矩阵|补救路线" .codex/skills/project-rescue-map/SKILL.md
```

Expected: output includes the section around the current 00-10 workflow position and the 01-10 stage matrix.

- [ ] **Step 2: Add a dual-track explanation after the workflow-position section**

Insert this text after the current "在完整 work-bench 工作流中的位置" section and before "何时启用":

```markdown
## 1.x 双轨视图：管理层与执行层

本 skill 使用双轨视图输出诊断：

- **管理层五大类**：帮助用户先看懂项目主要乱在哪些大块，适合摘要、排序和决策。
- **执行层 00-10**：保留现有 work-bench 精细阶段，负责指向真正要调用的补救 skill。

五大类不是新的 skill 名称，也不替代 00-10。任何补救动作最终都必须落回现有执行层 skill。

| 管理大类 | 映射执行阶段 | 诊断目的 |
|---|---|---|
| 范围 | `01-idea-check` | 产品目标、V1 边界、用户路径、验收标准是否清楚 |
| 架构 | `02-tool-pick`、`03-data-map`、`04-talk-link` | 技术栈、数据模型、API 契约和集成边界是否一致 |
| 骨架 | `05-skeleton-check`、`06-web-frame`、`07-server-frame` | 前后端骨架、目录责任、运行基线是否可靠 |
| 交付 | `08-work-plan`、`09-doc-rules` | 垂直切片、README、AGENTS、docs index、CI 是否支撑继续开发 |
| 验收 | `10-final-check` | 测试、构建、发布、回滚、安全和证据包是否足够 |
```

- [ ] **Step 3: Update the report-output instructions**

Find the output/report section and ensure it says the main report order is:

```markdown
主报告必须按以下顺序组织：

1. 项目阶段与止血门结论。
2. 五大类管理摘要。
3. 01-10 执行阶段缺口矩阵。
4. 风险登记与适用性。
5. 补救路线图。
6. 证据账本与命令记录。
```

- [ ] **Step 4: Add conservative aggregation rules**

Add this rule block near the stage status or scoring section:

```markdown
### 五大类状态聚合规则

- 任一映射阶段存在适用的 `STOP` 风险时，该管理大类不得标为 `通过`。
- 映射阶段之间存在文档、代码、配置、schema、API 或命令冲突时，优先标为 `冲突`。
- 没有可用真源时标为 `缺失`。
- 有部分证据但缺关键门禁或运行验证时标为 `部分具备`。
- 权限、环境或证据不足导致不能判断时标为 `不可验证`。
- 只有映射阶段证据充分且无关键冲突时，才可标为 `通过`。
- 原型期或 MVP 早期尚未开发到的能力继续使用 `暂不适用` 或 `未来门禁`，不得仅因未实现支付、权限、隐私或生产发布能力判为 `STOP`。
```

- [ ] **Step 5: Verify the skill text still references existing 00-10 skills**

Run:

```bash
rg -n "define-scope|design-architecture|prepare-skeletons|plan-delivery|verify-release" .codex/skills/project-rescue-map/SKILL.md
```

Expected: no output unless the terms are explicitly described as zip-only names not adopted by this repository.

---

### Task 2: Add Five-Area Summary To The Report Template

**Files:**
- Modify: `.codex/skills/project-rescue-map/templates/03_project_rescue_report.md`

- [ ] **Step 1: Insert the management summary before the existing stage matrix**

Place this section between "总体结论" and the current "阶段缺口矩阵":

```markdown
## 4. 五大类管理摘要

| 管理大类 | 映射阶段 | 大类状态 | 适用性 | 证据等级 | 置信度 | 关键发现 | 最高风险 | 第一补救动作 |
|---|---|---|---|---|---|---|---|---|
| 范围 | 01 idea-check |  |  |  |  |  |  |  |
| 架构 | 02 tool-pick / 03 data-map / 04 talk-link |  |  |  |  |  |  |  |
| 骨架 | 05 skeleton-check / 06 web-frame / 07 server-frame |  |  |  |  |  |  |  |
| 交付 | 08 work-plan / 09 doc-rules |  |  |  |  |  |  |  |
| 验收 | 10 final-check |  |  |  |  |  |  |  |
```

- [ ] **Step 2: Renumber the following sections**

Update the following headings so ordering remains readable:

```markdown
## 5. 阶段缺口矩阵
## 6. 横向健康扫描
## 7. 冲突与漂移
## 8. 风险分级
## 9. 补救路线图
## 10. 风险豁免
## 11. 本轮禁止事项
## 12. 下一步
```

- [ ] **Step 3: Add management area to the rescue roadmap table**

Change the rescue roadmap header from:

```markdown
| 顺序 | 回到阶段 | 调用 skill | 目标产出 | 通过门槛 | 依赖/前置 |
|---|---|---|---|---|---|
```

to:

```markdown
| 顺序 | 管理大类 | 回到阶段 | 调用 skill | 目标产出 | 通过门槛 | 依赖/前置 |
|---|---|---|---|---|---|---|
```

Update the sample rows to include `范围`、`架构`、`交付`、`验收` as appropriate.

- [ ] **Step 4: Check the report template headings**

Run:

```bash
rg -n "^## " .codex/skills/project-rescue-map/templates/03_project_rescue_report.md
```

Expected: headings run from 1 through 12 and include "五大类管理摘要" before "阶段缺口矩阵".

---

### Task 3: Extend The Stage Gap Matrix Template

**Files:**
- Modify: `.codex/skills/project-rescue-map/templates/02_stage_gap_matrix.md`

- [ ] **Step 1: Add a management-area rollup table above the 00-10 matrix**

Insert this section after the title:

```markdown
## 五大类管理摘要

| 管理大类 | 映射阶段 | 大类状态 | 适用性 | 证据等级 | 置信度 | 关键证据 | 关键缺口 | 最高风险 | 第一补救动作 |
|---|---|---|---|---|---|---|---|---|---|
| 范围 | 01 |  |  |  |  |  |  |  |  |
| 架构 | 02 / 03 / 04 |  |  |  |  |  |  |  |  |
| 骨架 | 05 / 06 / 07 |  |  |  |  |  |  |  |  |
| 交付 | 08 / 09 |  |  |  |  |  |  |  |  |
| 验收 | 10 |  |  |  |  |  |  |  |  |

## 01-10 执行阶段矩阵
```

- [ ] **Step 2: Add `管理大类` to the existing detailed matrix**

Change the detailed matrix header from:

```markdown
| 阶段 | Skill | 状态 | 适用性 | 证据等级 | 置信度 | 关键证据 | 缺口 | 风险等级 | 推荐下一步 | 通过门槛 |
```

to:

```markdown
| 管理大类 | 阶段 | Skill | 状态 | 适用性 | 证据等级 | 置信度 | 关键证据 | 缺口 | 风险等级 | 推荐下一步 | 通过门槛 |
```

Prefix each row with the matching management area:

```markdown
| 范围 | 01 | idea-check |  |  |  |  |  |  |  |  | V1 scope、用户路径、验收标准一致 |
| 架构 | 02 | tool-pick |  |  |  |  |  |  |  |  | 技术决策与实际依赖一致 |
| 架构 | 03 | data-map |  |  |  |  |  |  |  |  | schema/model/migration 与数据设计真源一致 |
| 架构 | 04 | talk-link |  |  |  |  |  |  |  |  | API 契约、DTO、前端 client、后端路由一致 |
| 骨架 | 05 | skeleton-check |  |  |  |  |  |  |  |  | 前后端骨架来源和 delivery target 明确 |
| 骨架 | 06 | web-frame |  |  |  |  |  |  |  |  | 前端目录、路由、组件、API client、质量门禁收敛 |
| 骨架 | 07 | server-frame |  |  |  |  |  |  |  |  | 后端入口、配置、错误、日志、鉴权、安全基线可验收 |
| 交付 | 08 | work-plan |  |  |  |  |  |  |  |  | V1 垂直切片、DoD、任务边界和变更控制存在 |
| 交付 | 09 | doc-rules |  |  |  |  |  |  |  |  | README、docs index、AGENTS、CI 与真实项目一致 |
| 验收 | 10 | final-check |  |  |  |  |  |  |  |  | 全链路证据包、回归、发布/回滚计划存在 |
```

- [ ] **Step 3: Add area status enum note**

Below "状态枚举", add:

```markdown
同一管理大类内的执行阶段状态必须保守聚合；存在冲突或适用的 STOP 风险时，大类不得标为 `通过`。
```

- [ ] **Step 4: Check table pipe consistency**

Run:

```bash
awk '/^\\|/ { print NR ":" gsub(/\\|/,"&") ":" $0 }' .codex/skills/project-rescue-map/templates/02_stage_gap_matrix.md
```

Expected: management summary rows have the same pipe count as their header; detailed matrix rows have the same pipe count as their header.

---

### Task 4: Add Management Area To Risk And Scoring

**Files:**
- Modify: `.codex/skills/project-rescue-map/templates/06_risk_register.md`
- Modify: `.codex/skills/project-rescue-map/references/scoring-model.md`

- [ ] **Step 1: Inspect the risk register template**

Run:

```bash
sed -n '1,220p' .codex/skills/project-rescue-map/templates/06_risk_register.md
```

Expected: risk tables exist for risk levels or risk entries.

- [ ] **Step 2: Add management-area fields to risk tables**

For each risk entry table, ensure the header contains:

```markdown
| ID | 管理大类 | 关联阶段 | 风险 | 适用性 | 证据 | 影响 | 建议 | 负责人 | 截止/触发条件 |
|---|---|---|---|---|---|---|---|---|---|
```

For observation-only tables, use:

```markdown
| ID | 管理大类 | 关联阶段 | 风险 | 适用性 | 证据 | 影响 | 复查信号 |
|---|---|---|---|---|---|---|---|
```

- [ ] **Step 3: Add scoring aggregation rules**

Append this section to `.codex/skills/project-rescue-map/references/scoring-model.md`:

```markdown
## 5. 五大类聚合规则

五大类摘要从 01-10 执行阶段和风险登记中聚合，不单独发明证据。

| 管理大类 | 阶段来源 | 聚合重点 |
|---|---|---|
| 范围 | 01 | 产品边界、V1、用户路径、验收标准 |
| 架构 | 02 / 03 / 04 | 技术栈、数据模型、API 契约一致性 |
| 骨架 | 05 / 06 / 07 | 骨架来源、前端基线、后端基线 |
| 交付 | 08 / 09 | 切片计划、文档、AGENTS、CI |
| 验收 | 10 | 测试、构建、发布、回滚、证据包 |

聚合时按最保守状态展示：`STOP`/阻塞优先，其次 `冲突`、`缺失`、`不可验证`、`部分具备`、`通过`。`暂不适用` 和 `未来门禁` 不得升级为当前阻塞，除非项目阶段已经进入对应能力范围。
```

- [ ] **Step 4: Confirm scoring model still keeps prototype noise control**

Run:

```bash
rg -n "原型期|未来门禁|暂不适用|五大类聚合" .codex/skills/project-rescue-map/references/scoring-model.md
```

Expected: output includes the existing prototype rule and the new five-area aggregation section.

---

### Task 5: Document The Dual-Track Workflow At Repository Level

**Files:**
- Modify: `README.md`
- Create or modify: `WORKFLOW.md`

- [ ] **Step 1: Update README without claiming 00-10 was replaced**

Replace the current short README body with:

```markdown
# work-bench

work-bench 是给 Codex / AI 编程助手使用的项目交付工作台，包含：

- `.codex/skills/`：项目初始化、补救诊断、交付验收相关 Skill。
- `frontend/apps/*`：可复用前端骨架候选。
- `backend/apps/*`：可复用后端骨架候选。

## 推荐入口

| 场景 | 入口 |
|---|---|
| 新项目从想法到可开发骨架 | `.codex/skills/00-build-map/SKILL.md` |
| 已开工项目混乱，需要先诊断 | `.codex/skills/project-rescue-map/SKILL.md` |
| 只需要前端骨架候选 | `frontend/README.md` |
| 只需要后端骨架候选 | `backend/README.md` |

## 双轨工作流

- **执行层 00-10**：保留现有细分 skill，用于真正落地产品范围、技术选型、数据设计、API 契约、前后端骨架、交付计划、文档规则和发布验收。
- **管理层五大类**：范围、架构、骨架、交付、验收，用于 `project-rescue-map` 快速说明项目主要问题和补救优先级。

五大类只是摘要视图，不替代 00-10 skill。实际修复仍回到对应细分 skill。

## 核心原则

- work-bench 是 Skill 和骨架库，不是项目默认输出目录。
- 项目文档和代码默认写入用户确认的 `<project-root>`。
- 前端默认交付到 `<project-root>/frontend`，后端默认交付到 `<project-root>/backend`，除非用户明确指定其他 delivery target。
- 复制骨架前先读 `frontend/README.md` 和 `backend/README.md` 的候选索引。
```

- [ ] **Step 2: Create or update WORKFLOW.md**

If `WORKFLOW.md` does not exist, create it with the following content:

````markdown
# work-bench Workflow

## 双轨模型

work-bench 使用双轨模型：

```text
管理层五大类
  范围      -> 01 idea-check
  架构      -> 02 tool-pick + 03 data-map + 04 talk-link
  骨架      -> 05 skeleton-check + 06 web-frame + 07 server-frame
  交付      -> 08 work-plan + 09 doc-rules
  验收      -> 10 final-check

执行层 00-10
  00 build-map
  01 idea-check
  02 tool-pick
  03 data-map
  04 talk-link
  05 skeleton-check
  06 web-frame
  07 server-frame
  08 work-plan
  09 doc-rules
  10 final-check

旁路入口
  project-rescue-map
```

## 使用原则

- 新项目默认从 `00-build-map` 开始。
- 已经开工且真源混乱的项目，先用 `project-rescue-map`。
- `project-rescue-map` 先输出五大类摘要，再输出 01-10 精细补救矩阵。
- 五大类用于理解和排序，00-10 用于实际补救。
- 不因为引入五大类视图而重命名、删除或迁移现有 skill。

## 目标路径规则

- `<project-root>` 必须由用户确认。
- work-bench 只存放 Skill 和骨架候选，不存放默认项目产物。
- frontend 默认交付到 `<project-root>/frontend`。
- backend 默认交付到 `<project-root>/backend`。
- 默认禁止把 `frontend/apps/*` 或 `backend/apps/*` 原样嵌套复制为 `<project-root>/frontend/apps` 或 `<project-root>/backend/apps`。
````

- [ ] **Step 3: Validate docs references**

Run:

```bash
rg -n "define-scope|design-architecture|prepare-skeletons|plan-delivery|verify-release|不再使用 00-10|替代 00-10" README.md WORKFLOW.md
```

Expected: no output.

---

### Task 6: Validate Skill And Diff

**Files:**
- Verify only.

- [ ] **Step 1: Run skill validation**

Run:

```bash
python3 /home/xiaoyaozu/.codex/skills/.system/skill-creator/scripts/quick_validate.py /home/xiaoyaozu/AI/projects/work-bench/.codex/skills/project-rescue-map
```

Expected:

```text
Skill is valid!
```

- [ ] **Step 2: Run diff whitespace check**

Run:

```bash
git -C /home/xiaoyaozu/AI/projects/work-bench diff --check -- .codex/skills/project-rescue-map README.md WORKFLOW.md
```

Expected: no output.

- [ ] **Step 3: Inspect scoped status**

Run:

```bash
git status --short -- .codex/skills/project-rescue-map README.md WORKFLOW.md docs/superpowers/plans/2026-06-10-project-rescue-map-dual-track.md
```

Expected: only planned files are modified or untracked. Existing unrelated worktree changes may exist outside this scoped command and must not be staged.

- [ ] **Step 4: Inspect final scoped diff**

Run:

```bash
git diff -- .codex/skills/project-rescue-map README.md WORKFLOW.md docs/superpowers/plans/2026-06-10-project-rescue-map-dual-track.md | sed -n '1,260p'
```

Expected: diff shows dual-track wording, five-area templates, scoring aggregation, README/WORKFLOW docs, and this plan.

---

### Task 7: Commit The Implementation

**Files:**
- Stage only planned files.

- [ ] **Step 1: Stage scoped files**

Run:

```bash
git add .codex/skills/project-rescue-map README.md WORKFLOW.md docs/superpowers/plans/2026-06-10-project-rescue-map-dual-track.md
```

- [ ] **Step 2: Confirm staged scope**

Run:

```bash
git diff --cached --name-only
```

Expected: staged paths are limited to:

```text
.codex/skills/project-rescue-map/SKILL.md
.codex/skills/project-rescue-map/agents/openai.yaml
.codex/skills/project-rescue-map/checklists/...
.codex/skills/project-rescue-map/examples/...
.codex/skills/project-rescue-map/playbooks/...
.codex/skills/project-rescue-map/prompts/...
.codex/skills/project-rescue-map/references/...
.codex/skills/project-rescue-map/skill.json
.codex/skills/project-rescue-map/templates/...
README.md
WORKFLOW.md
docs/superpowers/plans/2026-06-10-project-rescue-map-dual-track.md
```

If unrelated files are staged, unstage them with:

```bash
git restore --staged <path>
```

- [ ] **Step 3: Commit**

Run:

```bash
git commit -m "feat: add project rescue dual-track view"
```

Expected: commit succeeds without staging unrelated repository changes.

---

## Self-Review Notes

- Spec coverage: Tasks 1-5 cover skill instructions, report template, gap matrix, risk/scoring, and repository docs. Task 6 covers validation. Task 7 covers commit hygiene.
- Completion scan: This plan contains no unresolved markers or unspecified implementation steps.
- Scope check: The plan is focused on `project-rescue-map` and repository workflow docs; it does not migrate the whole work-bench workflow.
