# AI_TASK_HEADER.md

每次让 AI 修改本项目时，把以下内容贴在任务开头：

```md
你正在修改一个已有前端项目。必须遵守：

1. 先阅读 `docs/FRONTEND_BLUEPRINT.md`、`docs/AI_GUARDRAILS.md`、`docs/PROJECT_STRUCTURE.md`、`docs/COMPONENT_GOVERNANCE.md`、`docs/API_CONTRACTS.md`。
2. 不得擅自更换框架、组件库、路由、状态管理、样式方案。
3. 不得新建与规范冲突的目录。
4. 相似 UI 出现 2 次及以上，必须抽象为复用组件。
5. 所有颜色、字号、间距、圆角、阴影必须来自 Token。
6. API 请求必须走统一 API Client 或 hooks，不得散落在页面组件中。
7. 先输出影响范围和文件清单，再给代码。
```
