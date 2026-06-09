# MIGRATION_PLAN.md

## 1. 迁移原则

- 不做一次性大重构。
- 每次只改一个模块或一种基础能力。
- 先补文档与 Guardrails，再动代码。
- 先收敛 API 与 Token，再抽组件，再整理模块。
- 每阶段必须可启动、可回滚、可验收。

## 2. 阶段计划

### 阶段 0：规范落盘

- 生成 FRONTEND_BLUEPRINT.md
- 生成 AI_GUARDRAILS.md
- 生成 PROJECT_STRUCTURE.md
- 生成 DESIGN_TOKENS.md
- 生成 QUALITY_GATES.md

验收：后续 AI 任务可以引用这些文件。

### 阶段 1：低风险基础收敛

- 建立统一 API client。
- 建立错误结构。
- 建立基础 Token。
- 建立 EmptyState、ErrorState、LoadingState、ConfirmDialog。

验收：不改变业务路由和页面功能。

### 阶段 2：最高频页面组件抽象

- 抽象列表页 DataTable。
- 抽象筛选栏 SearchFilterBar。
- 抽象页面头 PageHeader。
- 抽象状态标签 StatusBadge。

验收：至少 2 个页面复用同一套组件。

### 阶段 3：模块边界整理

- auth/users/orders/content/settings 按模块迁移。
- 模块内 api/types/components 归位。
- 通用组件只保留跨模块能力。

验收：改动模块不影响无关模块。

### 阶段 4：质量加固

- 补 type-check/lint/build。
- 补关键组件测试。
- 补关键流程 E2E。
- 组件进入 Storybook 或组件说明文档。

验收：质量命令可运行，新增代码不突破 Guardrails。

## 3. 回滚策略

- 每阶段单独提交。
- 不同模块拆分提交。
- 不同时改技术栈和业务逻辑。
- 保留旧组件一段时间，通过适配层迁移。
