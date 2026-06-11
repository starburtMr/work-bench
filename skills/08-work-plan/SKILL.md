---
name: work-plan
description: "Split a V1 MVP into vertical slices, tickets, PR boundaries, dependencies, DoD, and change-control rules. Use after product, stack, data, API, frontend, and backend baselines are ready."
---

# MVP 功能切片与交付计划 Skill


## 1. 在完整开发工作流中的位置

- 阶段编号：`08`
- 阶段名称：MVP 功能切片 / 交付计划冻结
- 总控入口：[`build-map`](../00-build-map/SKILL.md)
- 本阶段目标：把 V1 MVP 拆成可执行、可验收、可回滚的垂直切片任务和 PR 边界。

## 2. 何时启用

当前端骨架、后端骨架、数据库设计和 API 契约已经通过阶段验收后，且 `skeleton-check` 已经给出前后端候选判定时，启用本 skill。它不替代编码，而是防止开发顺序混乱、AI 一次性改太多文件、PR 无法审查。

## 3. 上游输入契约

本 skill 不应孤立执行。除非用户明确要求单独使用，否则应优先读取或生成以下输入：

- `<project-root>/docs/product/v1-mvp-scope.md`
- `<project-root>/docs/product/user-journey-and-data-flow.md`
- `<project-root>/docs/architecture/tech-stack-decision.md`
- `<project-root>/docs/database/database-design.md`
- `<project-root>/docs/api/api-contract-source-of-truth.md`
- `<project-root>/docs/skeleton/skeleton-selection-report.md`
- `<project-root>/docs/skeleton/delivery-targets.md`
- `<project-root>/docs/frontend/frontend-blueprint.md`
- `<project-root>/docs/backend/backend-architecture-source-of-truth.md`

## 4. 下游输出契约

- `<project-root>/docs/delivery/mvp-feature-slice-plan.md`：V1 垂直切片计划。
- `<project-root>/docs/delivery/implementation-backlog.md`：按依赖排序的任务池。
- `<project-root>/docs/delivery/pr-plan.md`：PR 粒度、改动范围、验收命令。
- `<project-root>/docs/delivery/feature-dependency-map.md`：前端、后端、数据库、API、第三方依赖关系。
- `<project-root>/docs/delivery/definition-of-done.md`：每类任务的完成定义。
- `<project-root>/docs/delivery/change-control.md`：需求变更、接口变更、依赖变更处理规则。

## 5. 与其他 skill 的引用关系

### 上游 skill

- [`idea-check`](../01-idea-check/SKILL.md)
- [`tool-pick`](../02-tool-pick/SKILL.md)
- [`data-map`](../03-data-map/SKILL.md)
- [`talk-link`](../04-talk-link/SKILL.md)
- [`skeleton-check`](../05-skeleton-check/SKILL.md)
- [`web-frame`](../06-web-frame/SKILL.md)
- [`server-frame`](../07-server-frame/SKILL.md)

### 下游 skill

- [`doc-rules`](../09-doc-rules/SKILL.md)
- [`final-check`](../10-final-check/SKILL.md)

### 5.3 交接载荷

交给下游时，至少携带以下信息：

- V1 垂直切片计划、任务池和 PR 计划。
- 每个切片的用户价值、改动范围、禁止范围、验收命令和回滚方式。
- 功能依赖图、DoD 和变更控制规则。

## 6. 切片原则

1. 优先按用户价值闭环切片，而不是按技术层切片。
2. 每个切片必须有可观察结果，例如“用户能创建项目并在列表看到”。
3. 每个切片必须包含必要的前端、后端、数据库、API、测试和文档更新范围。
4. 不允许一个 PR 同时改多个无关业务域。
5. 不允许为了“顺手”添加 V1 范围外功能。
6. 不允许绕过已冻结的技术栈、API 契约、目录责任和安全规则。
7. 每个任务必须写清楚：输入文档、允许改动文件、禁止改动文件、验收命令、回滚方式。
8. 对高风险任务必须先做 spike 或验证任务，再进入正式实现。

## 7. 标准工作流

### Step 1：从 V1 Must-have 提取用户闭环

把 Must-have 转成闭环，例如：

- 访客注册/登录。
- 创建核心业务对象。
- 查看列表与详情。
- 修改状态。
- 完成支付/提交/审批等关键动作。

### Step 2：为每个闭环建立垂直切片

每个切片必须包含：

- 用户故事；
- 关联页面；
- 关联 API；
- 关联表和字段；
- 后端服务/权限/校验；
- 前端状态和错误处理；
- 测试策略；
- 文档更新；
- 验收证据。

### Step 3：按依赖排序

排序规则：

1. 工程基线验证。
2. 认证/权限基础。
3. 核心对象 CRUD 的最小闭环。
4. 状态流转或关键业务动作。
5. 通知、统计、导出、优化等非核心能力。
6. V1.1 体验修补。

### Step 4：定义 PR 粒度

每个 PR 应尽量只服务一个切片或一个基础设施目标。PR 计划必须写明：

- 目标；
- 改动范围；
- 不改什么；
- 测试/构建命令；
- 手工验收路径；
- 截图、日志、接口响应等证据。

### Step 5：建立变更控制

需求、接口、数据库、技术依赖任一变化，都必须记录：

- 变更原因；
- 影响范围；
- 是否需要回到上游 skill；
- 是否影响 V1 边界；
- 是否需要更新 AGENTS.md 或 CI。

## 8. 输出模板

```md
# V1 MVP 垂直切片计划

## 1. 输入文档

| 文档 | 状态 | 链接 |
|---|---|---|

## 2. V1 闭环列表

| 编号 | 用户闭环 | 用户价值 | 阶段 |
|---|---|---|---|

## 3. 切片详情

### Slice-01：<名称>

- 用户故事：
- 价值闭环：
- 关联页面：
- 关联 API：
- 关联数据库对象：
- 后端改动范围：
- 前端改动范围：
- 测试：
- 文档更新：
- 不做范围：
- 验收标准：
- 回滚方式：

## 4. PR 计划

| PR | 目标 | 允许改动 | 禁止改动 | 验收命令 |
|---|---|---|---|---|

## 5. 风险与前置验证

## 6. 变更控制
```

## 9. 阶段完成门禁

- [ ] 所有 V1 Must-have 都映射到垂直切片或明确被延后。
- [ ] 每个切片能追溯到产品、API、数据库、前端和后端真源文档。
- [ ] 每个 PR 粒度可审查、可测试、可回滚。
- [ ] 已明确禁止范围，防止 AI 扩写到 V2/V3。
- [ ] 每个切片都有验收命令和手工验收路径。

## 10. 推荐落盘位置

- 阶段真源文档：`<project-root>/docs/`
- 阶段决策记录：`<project-root>/docs/decisions/`
- 阶段检查清单：`<project-root>/docs/checklists/`
- 面向 Agent 的长期约束：`<project-root>/AGENTS.md` 或 `<project-root>/docs/agent-rules/`
