# 示例：已有项目规范化 / 防止后续 Vibe Coding 写乱

## 用户输入

我已经有一个 React 项目，页面越来越乱，按钮样式不统一，接口都写在页面里，AI 每次改都会新增组件。帮我整理规范，不要大重构。

## Skill 应答方向

### 1. 先要求用户提供

```md
请粘贴：
1. package.json
2. tree -L 3 的目录结构
3. 2-3 个典型页面文件
4. 当前使用的组件库和样式方式
5. 是否允许新增 docs、src/styles、src/lib/request.ts、src/components/feedback
```

### 2. 诊断输出

| 风险 | 级别 | 说明 | 建议 |
|---|---|---|---|
| 样式硬编码 | 高 | 多页面重复写颜色/圆角 | 建 tokens.css，逐步迁移 |
| API 散落 | 高 | 页面内直接 axios | 建 request client 和 api 层 |
| 组件重复 | 中 | 多个 Button/Modal 变体 | 先统一 feedback 和 business components |
| AI 护栏缺失 | 高 | 后续修改无约束 | 先加 AI_GUARDRAILS.md |

### 3. 低风险迁移计划

1. 不改业务逻辑，先新增 docs 规范。
2. 新增 `src/styles/tokens.css`，只替换主色/背景/文本色。
3. 新增 `src/lib/request.ts`，新接口先走统一层，旧接口逐步迁移。
4. 新增 `LoadingState`、`EmptyState`、`ErrorState`，替换高频重复状态 UI。
5. 新增 AI 任务模板，禁止后续直接复制组件。

### 4. 后续 AI 任务模板

```md
任务类型：refactor
目标：仅迁移订单列表页 API 请求到 src/features/orders/api，不改变页面视觉和路由。
必须遵守：docs/AI_GUARDRAILS.md、docs/API_CONTRACTS.md。
允许修改：src/features/orders、src/lib/request.ts、docs/API_CONTRACTS.md。
禁止修改：全局主题、路由、其他模块页面。
验收：订单列表功能不变；无页面内 axios/fetch；错误状态保持可见。
```

