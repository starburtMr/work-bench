# PROMPT_TEMPLATES.md

## 1. 新项目启动 Skill

```md
请启用 Frontend Skeleton Architect Vibe Coding Skill。

模式：新项目从 0 到 1。
目标：先搭前端骨架，不要直接横推页面。

请先问我必要问题；如果信息足够，请输出：
- ADR
- FRONTEND_BLUEPRINT.md
- PROJECT_STRUCTURE.md
- DESIGN_TOKENS.md
- COMPONENT_GOVERNANCE.md
- API_CONTRACTS.md
- AI_GUARDRAILS.md
- QUALITY_GATES.md
- 第一阶段实施计划和验收清单
```

## 2. 快速默认方案

```md
请启用 Frontend Skeleton Architect Vibe Coding Skill。

我授权你先采用默认成熟方案，但必须写明默认假设、选择理由、后续可替换点和风险。

项目大概是：<项目描述>
第一阶段页面：<页面列表>
设计风格：<关键词或参考>
后端状态：<已有接口/Mock>
```

## 3. 已有项目优化

```md
请启用 Frontend Skeleton Architect Vibe Coding Skill。

模式：已有项目规范化 / 优化。
目标：不要直接大重构，先诊断再输出迁移计划。

我会提供：
- 目录结构
- package.json
- 当前痛点
- 是否允许调整目录和组件

请输出：
- EXISTING_PROJECT_AUDIT.md
- 目标目录结构
- Token 迁移表
- API 收敛方案
- 组件抽象清单
- AI_GUARDRAILS.md
- MIGRATION_PLAN.md
```

## 4. 骨架完成后的页面开发请求

```md
请遵守项目中的 AI_GUARDRAILS.md、FRONTEND_BLUEPRINT.md、COMPONENT_GOVERNANCE.md 和 DESIGN_TOKENS.md。

任务：新增/修改 <页面名>。

在写代码前，请先输出页面规格：
- 路由
- 访问角色
- 页面目标
- 数据字段
- 交互流程
- 页面状态
- 响应式规则
- 可复用组件

然后再给出代码变更，并说明验证方式。
```
