# 示例：骨架后让 AI 新增页面

```md
请严格遵守项目中的：
- docs/FRONTEND_BLUEPRINT.md
- docs/PROJECT_STRUCTURE.md
- docs/DESIGN_TOKENS.md
- docs/COMPONENT_GOVERNANCE.md
- docs/API_CONTRACTS.md
- docs/AI_GUARDRAILS.md

任务：新增订单列表页面。

要求：
1. 先输出 PAGE_SPEC。
2. 复用 AppShell、PageHeader、SearchFilterBar、DataTable、EmptyState、ErrorState、ConfirmDialog。
3. API 请求走 modules/orders/api.ts 和统一 api client。
4. 样式只能使用 Token 或组件库主题。
5. 必须处理 loading、empty、error、forbidden。
6. 输出修改文件列表和验证命令。
```
