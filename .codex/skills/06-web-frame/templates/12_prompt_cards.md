# Prompt Cards：可直接复用的话术

## 1. 新项目从 0 到 1

```md
请启用 frontend-skeleton-vibe-coding Skill。
我的目标是从 0 到 1 搭一个前端骨架，不要直接横推页面。
请先判断目标端、项目类型、设计风格、技术栈、组件库、目录结构、样式 Token、API 契约和 AI Guardrails。
不清楚的关键问题必须先问我。
```

## 2. 用户没技术偏好时

```md
我没有技术偏好。请根据我的项目类型给出 2-3 套成熟方案，并推荐一套默认方案。
要求说明：适用场景、优点、风险、后续可替换点。
确认后再生成前端骨架蓝图。
```

## 3. 已有项目加固

```md
请启用 frontend-skeleton-vibe-coding Skill 的模式 B。
我有一个已有项目，需要规范化和防止后续 Vibe Coding 写乱。
请先根据目录结构和 package.json 做诊断，不要直接大改。
输出：现状诊断、风险分级、目标蓝图、迁移计划、AI_GUARDRAILS.md。
```

## 4. 新增页面但不能破坏规范

```md
请先读取 FRONTEND_BLUEPRINT.md、COMPONENT_RULES.md、DESIGN_TOKENS.md、API_CONTRACTS.md、AI_GUARDRAILS.md。
然后为【页面名称】新增页面规格，再按既有目录和组件规范实现。
不得新增未经确认的依赖，不得散落 API 请求，不得硬编码样式。
输出前请说明影响文件和验收方式。
```
