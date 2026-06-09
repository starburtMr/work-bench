---
name: build-map
description: "Orchestrate the full development workflow from idea to release. Use when you need to sequence discovery, stack choice, data design, API contracts, skeleton candidate selection, frontend, backend, planning, docs, and release gates."
---

# 全栈开发工作流总控 Skill


## 1. 总工作流顺序

| 阶段 | Skill | 目标 | 主要产出 | 通过后进入 |
|---|---|---|---|---|
| 01 | [`idea-check`](../01-idea-check/SKILL.md) | 产品立项与 V1 边界 | project brief、MVP scope、用户路径、核心对象、风险计划、bootstrap targets | 02 |
| 02 | [`tool-pick`](../02-tool-pick/SKILL.md) | 技术栈唯一决策 | 技术选型报告、依赖规则、禁用清单、重评条件 | 03 |
| 03 | [`data-map`](../03-data-map/SKILL.md) | 数据模型与迁移策略 | 数据库设计、ERD、表规格、迁移计划 | 04 |
| 04 | [`talk-link`](../04-talk-link/SKILL.md) | API 契约与联调边界 | API 真源、OpenAPI、错误码、Mock/契约测试 | 05 |
| 05 | [`skeleton-check`](../05-skeleton-check/SKILL.md) | 骨架候选检查与复用判定 | 前后端候选报告、复用/新建结论、delivery target 映射 | 06/07 |
| 06 | [`web-frame`](../06-web-frame/SKILL.md) | 前端骨架与组件治理 | 前端蓝图、目录、Token、组件、API Client、质量门禁 | 08 |
| 07 | [`server-frame`](../07-server-frame/SKILL.md) | 后端骨架与业务裁判层 | 后端真源、目录责任、错误码、日志、配置、安全、运行证据 | 08 |
| 08 | [`work-plan`](../08-work-plan/SKILL.md) | MVP 垂直切片和 PR 计划 | 切片计划、任务池、PR 计划、DoD、变更控制 | 09 |
| 09 | [`doc-rules`](../09-doc-rules/SKILL.md) | 文档、AGENTS.md、CI 固化 | README、docs index、AGENTS.md、CI workflow | 10 |
| 10 | [`final-check`](../10-final-check/SKILL.md) | 全链路验收与发布准备 | 验收报告、证据包、回归计划、发布/回滚清单 | 继续开发 / 发布 |

## 2. 什么时候启用本 workflow

当用户提出以下需求时，优先启用本 workflow，而不是单独调用某一个 skill：

- “帮我从想法到开发流程梳理一遍。”
- “我有一组前端、后端、数据库、技术选型、产品、文档 skill，想串成完整流程。”
- “我要开始一个项目，希望 AI 不要写乱。”
- “帮我搭完整开发规范、项目文档、Agent 规则和验收流程。”
- “已有项目被 AI 写乱了，想从产品、技术、数据、接口、前后端、文档、质量重新收口。”

## 3. 总控硬规则

1. **不得跳过产品边界。** 除非用户已经提供高质量 PRD，否则先运行 `idea-check`。
2. **不得先写代码再补规则。** 技术、数据库、API、前后端骨架至少要有真源文档初版。
3. **不得让各 skill 各说各话。** 每个阶段必须读取上游产出，并把下游需要的字段写清楚。
4. **不得伪造证据。** 命令、测试、接口响应、截图、日志都必须真实可复查；无法执行就说明原因。
5. **不得无门禁进入下一阶段。** 每个阶段必须有“通过 / 条件通过 / 不通过”结论。
6. **不得偷偷扩大 V1。** 所有新增需求进入停车场或变更控制，不直接塞进当前实现。
7. **不得让 AGENTS.md 与真源文档冲突。** 若冲突，以阶段真源为准并同步修正文档。
8. **不得把 workflow 当瀑布。** 允许小步返工，但返工必须记录原因、影响和更新文档。

## 4. 状态板

总控过程必须维护状态板，可落盘为 `docs/workflow/development-workflow-stateboard.md`。

```md
# 开发工作流状态板

## 1. 当前阶段

- 当前阶段：
- 当前结论：未开始 / 进行中 / 条件通过 / 通过 / 不通过
- 最近更新时间：

## 2. 阶段状态

| 阶段 | Skill | 状态 | 真源文档 | 阻塞项 | 下一步 |
|---|---|---|---|---|---|
| 01 | idea-check |  |  |  |  |
| 02 | tool-pick |  |  |  |  |
| 03 | data-map |  |  |  |  |
| 04 | talk-link |  |  |  |  |
| 05 | skeleton-check |  |  |  |  |
| 06 | web-frame |  |  |  |  |
| 07 | server-frame |  |  |  |  |
| 08 | work-plan |  |  |  |  |
| 09 | doc-rules |  |  |  |  |
| 10 | final-check |  |  |  |  |

## 3. 跨阶段决策记录

| 日期 | 决策 | 影响阶段 | 理由 | 是否需要返工 |
|---|---|---|---|---|

## 4. 假设与待确认

| ID | 内容 | 影响 | 所属阶段 | 处理方式 |
|---|---|---|---|---|

## 5. 返工记录

| 日期 | 从阶段 | 回到阶段 | 原因 | 更新文档 |
|---|---|---|---|---|
```

## 5. 阶段门禁

### G1：产品门禁

进入技术选型前必须满足：

- [ ] 一句话产品定义清楚。
- [ ] V1 Must / Won't 明确。
- [ ] 至少一条核心用户路径闭环。
- [ ] 核心业务对象、角色、权限和异常场景有初稿。
- [ ] 验收标准可检查。

### G2：技术门禁

进入数据库设计前必须满足：

- [ ] 唯一主线技术栈已确定。
- [ ] 不选方案和禁用技术清单已记录。
- [ ] 数据库、ORM/Migration、API 风格、测试、部署约束明确。
- [ ] 新增依赖申请和重评触发条件明确。

### G3：数据库门禁

进入 API 契约前必须满足：

- [ ] 核心对象、关系、ERD 和表设计覆盖 V1 路径。
- [ ] 字段、约束、索引、生命周期、安全规则明确。
- [ ] Migration 和回滚/前滚策略明确。
- [ ] 假设与待确认项已标注。

### G4：API 门禁

进入骨架候选检查前必须满足：

- [ ] 核心接口、请求、响应、错误结构、分页、认证、权限明确。
- [ ] API DTO、数据库对象、前端页面的数据来源能互相追溯。
- [ ] Mock 和契约测试策略明确。
- [ ] 破坏性变更处理规则明确。

### G5：骨架候选门禁

进入前端或后端骨架实施前必须满足：

- [ ] frontend/backend 的 delivery target 已在 `idea-check` 中确认。
- [ ] `frontend/apps` 和 `backend/apps` 的候选骨架已扫描。
- [ ] 每侧都给出 `reuse` 或 `create` 结论。
- [ ] 候选库路径和 delivery target 路径已区分清楚。

### G6：前端骨架门禁

进入功能切片前，前端侧必须满足：

- [ ] 前端蓝图、目录、页面规格、Token、组件治理完成。
- [ ] API Client、Mock、错误处理和类型策略明确。
- [ ] 构建/测试/类型检查/lint 命令明确。
- [ ] AI guardrails 已落盘。

### G7：后端骨架门禁

进入功能切片前，后端侧必须满足：

- [ ] 后端能启动并有运行证据。
- [ ] 健康检查、配置、数据库连接、日志/requestId 可验证。
- [ ] API 响应、错误码、权限占位、安全基线明确。
- [ ] 目录/文件责任表和运行手册已生成。

### G8：交付计划门禁

进入仓库文档固化前必须满足：

- [ ] V1 Must-have 已映射到垂直切片。
- [ ] 每个切片有用户价值、改动范围、禁止范围、测试和验收路径。
- [ ] PR 粒度可审查、可回滚。
- [ ] 变更控制规则明确。

### G9：文档与 Agent 门禁

进入全链路验收前必须满足：

- [ ] README、docs index、AGENTS.md 与真实项目一致。
- [ ] CI workflow 使用真实命令。
- [ ] 所有文档链接有效。
- [ ] 没有过期技术栈、旧项目、虚假命令引用。

### G10：质量门禁

进入发布或持续业务开发前必须满足：

- [ ] 全链路验收报告完成。
- [ ] 阻塞项为 0。
- [ ] 高风险项已修复或明确风险豁免。
- [ ] 测试、构建、接口、运行、文档证据可复查。
- [ ] 发布/回滚/恢复计划明确。

## 6. 返工规则

发现问题时按影响范围回退：

| 发现问题 | 回退到 |
|---|---|
| V1 范围不清、用户路径变化、角色变化 | `idea-check` |
| 技术栈不适合、依赖冲突、部署不可行 | `tool-pick` |
| 数据对象缺失、关系错误、字段/索引不支持查询 | `data-map` |
| 前后端字段不一致、错误结构混乱、权限接口不清 | `talk-link` |
| 前端或后端候选骨架不匹配、delivery target 未确认 | `skeleton-check` |
| 前端目录、组件、样式、API Client 失控 | `web-frame` |
| 后端启动、配置、错误、日志、权限、安全基线缺失 | `server-frame` |
| PR 太大、任务切片混乱、范围膨胀 | `work-plan` |
| README、AGENTS.md、CI 与真实项目不一致 | `doc-rules` |
| 证据不足、测试失败、安全风险未处理 | `final-check` |

返工后必须更新：状态板、相关真源文档、AGENTS.md 或 CI（如受影响）。

## 7. 推荐启动语

```text
请启用 build-map，按完整开发工作流推进这个项目。
当前我的项目想法是：<描述>。
请先做 V0 产品边界和 MVP 范围，不要直接写代码。
每个阶段都要输出阶段真源文档、门禁结论、下游交接信息和待确认项。
```

已有项目治理启动语：

```text
请启用 build-map，对这个已有项目做全链路治理。
先盘点产品边界、技术栈、数据库、API、前端、后端、文档和质量门禁。
不要直接大重构，先给我现状报告、风险分级、返工顺序和阶段门禁。
```

## 8. 最终交付物清单

完整流程结束后，仓库中至少应有：

- `docs/product/*`
- `docs/architecture/*`
- `docs/database/*`
- `docs/api/*`
- `docs/frontend/*`
- `docs/backend/*`
- `docs/skeleton/*`
- `docs/delivery/*`
- `docs/workflow/development-workflow-stateboard.md`
- `docs/quality/*`
- `README.md`
- `AGENTS.md`
- `.github/workflows/*`

## 9. 完成标准

这个 workflow 成功的标志不是“生成了很多文件”，而是：

- 每个阶段都有清晰职责和真源文档；
- 每个下游结论都能追溯到上游证据；
- 前端、后端、数据库、API 不再各说各话；
- Agent 后续开发有明确边界；
- 测试、构建、运行、文档和发布风险都有证据；
- V1 可被小步实现、审查、验收和迭代。
