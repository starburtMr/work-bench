---
name: project-rescue-map
description: "Diagnose an already-started project that did not go through the work-bench 00-10 workflow. Use when an existing repo is messy, missing product boundaries, data design, API contracts, frontend/backend baselines, docs, or quality gates, and the user needs a stage-level rescue roadmap before any repair work."
---

# 已开工项目补救诊断 Skill

## 1. 定位

本 skill 是 work-bench 00-10 工作流的补救入口，用于接手已经开始开发、但没有按工作流初始化的项目。

目标不是修代码，而是先判断项目缺了哪些阶段真源、哪些规则互相冲突、哪些风险会阻塞后续开发，并输出阶段级补救路线图。

## 2. 工作边界

默认只做诊断和路线图，不做修复动作：

- 不改业务代码。
- 不创建或修改数据库迁移。
- 不安装、升级或删除依赖。
- 不重构目录。
- 不生成 PR 计划。
- 不伪造不存在的文档、命令、接口、测试或运行证据。
- 只有用户明确要求落盘时，才写入 `docs/rescue/`。

## 3. 上游输入

优先读取目标项目中的真实证据，而不是根据目录名猜测：

- `README.md`、`AGENTS.md`、`Claude.md`、`.codex/config.toml`。
- `docs/`、`PROJECT_STATE`、`TASK_LOG`、`PLANS.md` 或类似项目文档。
- 前端、后端、数据库、API、脚本、测试、CI、部署配置。
- `package.json`、`pyproject.toml`、`Cargo.toml`、`go.mod`、`Makefile`、`.github/workflows/*` 等工具文件。
- 已有路由、controller、API client、schema、migration、mock、类型定义和测试。

如果目标项目有更近的 `AGENTS.md` 或项目规则，先遵守目标项目规则，再执行本诊断。

## 4. 对照基线

按 work-bench 的 00-10 阶段做阶段级诊断：

| 阶段 | Skill | 诊断重点 |
|---|---|---|
| 01 | [`idea-check`](../01-idea-check/SKILL.md) | 产品定义、V1 边界、用户路径、核心对象、验收标准是否清晰 |
| 02 | [`tool-pick`](../02-tool-pick/SKILL.md) | 技术栈、依赖规则、禁用技术、重评条件是否唯一且真实 |
| 03 | [`data-map`](../03-data-map/SKILL.md) | 业务对象、关系、表设计、迁移计划、安全字段是否有真源 |
| 04 | [`talk-link`](../04-talk-link/SKILL.md) | API 契约、DTO、错误码、鉴权、分页、Mock、契约测试是否统一 |
| 05 | [`skeleton-check`](../05-skeleton-check/SKILL.md) | 前后端骨架来源、delivery target、reuse/create 决策是否清楚 |
| 06 | [`web-frame`](../06-web-frame/SKILL.md) | 前端目录、路由、组件、Token、API Client、质量门禁是否收敛 |
| 07 | [`server-frame`](../07-server-frame/SKILL.md) | 后端路由、错误、日志、配置、数据访问、安全基线是否可验收 |
| 08 | [`work-plan`](../08-work-plan/SKILL.md) | V1 是否被拆成垂直切片、任务边界、DoD、变更控制是否存在 |
| 09 | [`doc-rules`](../09-doc-rules/SKILL.md) | README、docs index、AGENTS.md、CI 是否和真实项目一致 |
| 10 | [`final-check`](../10-final-check/SKILL.md) | 范围、架构、测试、安全、回滚、证据包是否达到继续开发门槛 |

## 5. 诊断流程

### Step 1：确认目标项目根目录

明确本次诊断的 `<project-root>`。如果用户给了路径，以该路径为准；如果没有给路径，使用当前工作目录并在报告中标注该假设。

### Step 2：读取项目入口和规则

读取目标项目最近的协作规则和入口文档：

- 先找 `AGENTS.md`、`AGENTS.override.md`、`Claude.md`。
- 再读 `README.md`、`docs/README.md` 或 `docs/index.md`。
- 再看工具配置和脚本，确认真实技术栈与可运行命令。

不要因为文件名存在就判定阶段通过，必须检查内容是否足够下游使用。

### Step 3：扫描工程证据

按项目实际结构扫描：

- 产品证据：PRD、范围文档、用户流程、验收标准。
- 技术证据：依赖、框架、包管理器、部署目标、测试工具。
- 数据证据：schema、migration、ORM model、种子数据、数据访问层。
- API 证据：路由、OpenAPI、controller、DTO、API client、mock、错误结构。
- 前端证据：路由、页面、组件、样式、状态、接口调用。
- 后端证据：入口、配置、日志、错误、鉴权、权限、健康检查。
- 交付证据：任务计划、PR 边界、CI、测试、发布和回滚材料。

### Step 4：生成阶段矩阵

每个阶段给一个状态：

- `通过`：有真实证据，内容能直接支撑下游工作。
- `部分具备`：有一些材料，但缺关键字段、门禁或一致性。
- `缺失`：没有可用真源。
- `冲突`：文档、代码、配置或运行命令互相矛盾。
- `不适用`：当前项目形态确实不需要该阶段内容。

### Step 5：分级风险

把发现的问题归入四类：

- `阻塞`：不补会导致后续开发方向错误、数据损坏、安全事故或无法验收。
- `必须补`：短期可以继续观察，但进入主要开发前必须补齐。
- `可后补`：不影响当前补救顺序，但需要记录。
- `观察项`：证据不足或影响较小，后续复查。

### Step 6：输出补救顺序

给出阶段级路线图，不展开完整任务池：

- 先列最小必要返工链路，例如 `01 -> 03 -> 04 -> 07 -> 09 -> 10`。
- 每个阶段只写 1-3 条下一步产出提示。
- 明确下一步应调用哪个已有 skill。
- 如果发现项目过大，先建议按子系统拆分，再分别运行本 skill。

## 6. 标准输出格式

在聊天中输出以下报告。只有用户明确要求落盘时，写入 `docs/rescue/project-rescue-report.md` 和 `docs/rescue/rescue-stateboard.md`。

```md
# Project Rescue Report

## 1. 诊断范围

- 项目根目录：
- 诊断时间：
- 已读取证据：
- 未读取/不可读取证据：
- 当前假设：

## 2. 总体结论

- 当前状态：可继续 / 条件可继续 / 不建议继续开发
- 主要阻塞：
- 推荐补救主线：

## 3. 阶段缺口矩阵

| 阶段 | Skill | 状态 | 证据 | 缺口 | 风险等级 | 建议下一步 |
|---|---|---|---|---|---|---|

## 4. 冲突与漂移

| 类型 | 位置 | 冲突内容 | 影响 | 建议回到的 skill |
|---|---|---|---|---|

## 5. 风险分级

### 阻塞

### 必须补

### 可后补

### 观察项

## 6. 补救路线图

| 顺序 | 回到阶段 | 调用 skill | 目标产出 | 通过门槛 |
|---|---|---|---|---|

## 7. 禁止事项

- 本轮不改业务代码。
- 本轮不创建迁移。
- 本轮不安装或升级依赖。
- 本轮不重构目录。

## 8. 下一步

- 推荐立即调用：
- 调用前必须准备：
```

## 7. 完成门禁

- [ ] 目标项目根目录已明确。
- [ ] 项目入口文档和最近协作规则已读取。
- [ ] 技术栈、数据、API、前端、后端、文档和质量证据已扫描。
- [ ] 01-10 阶段矩阵已完成。
- [ ] 每个 `缺失`、`部分具备`、`冲突` 阶段都有风险等级。
- [ ] 补救顺序只指向已有 skill，不自行执行修复。
- [ ] 报告明确列出未验证项和原因。

## 8. 与其他 skill 的关系

本 skill 只负责补救诊断。后续执行必须回到对应阶段 skill：

- 产品边界不清：调用 `idea-check`。
- 技术栈混乱：调用 `tool-pick`。
- 数据模型缺失或危险：调用 `data-map`。
- 前后端接口不一致：调用 `talk-link`。
- 骨架来源和落地路径不清：调用 `skeleton-check`。
- 前端结构混乱：调用 `web-frame`。
- 后端基线缺失：调用 `server-frame`。
- 开发顺序混乱：调用 `work-plan`。
- 文档和规则漂移：调用 `doc-rules`。
- 需要发布或交付门禁：调用 `final-check`。
