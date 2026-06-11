# 示例：从 0 到 1 搭 React B 端管理后台骨架

## 用户输入

我想做一个订单管理后台，第一阶段有登录、首页、订单列表、订单详情、用户管理。没有后端，先用 Mock。风格要企业级、简洁、高信息密度。我不会选技术栈，你来定。

## Skill 应答方向

### 1. 模式判断

新项目从 0 到 1，目标端为 PC Web 管理后台。

### 2. 默认技术决策

- 框架：React + TypeScript + Vite
- UI 组件库：Ant Design
- 路由：React Router
- 服务端状态：TanStack Query
- Mock：MSW
- 测试：Vitest + Testing Library + Playwright
- 样式系统：AntD Theme Token + CSS Variables

### 3. 第一阶段页面地图

| 页面 | 路由 | 组件 | 状态 |
|---|---|---|---|
| 登录 | `/login` | LoginForm | loading/error |
| 首页 | `/` | StatCards、RecentOrders | loading/empty/error |
| 订单列表 | `/orders` | FilterBar、OrderTable | loading/empty/error |
| 订单详情 | `/orders/:id` | OrderSummary、OrderTimeline | loading/error/notFound |
| 用户管理 | `/users` | UserTable、UserStatusTag | loading/empty/error |

### 4. 首批骨架交付

```text
docs/
  FRONTEND_BLUEPRINT.md
  AI_GUARDRAILS.md
  PROJECT_STRUCTURE.md
  DESIGN_TOKENS.md
  COMPONENT_RULES.md
  API_CONTRACTS.md
src/
  app/
  router/
  components/ui/
  components/layout/
  components/feedback/
  features/auth/
  features/orders/
  features/users/
  lib/request.ts
  lib/queryClient.ts
  mocks/handlers.ts
  styles/tokens.css
```

### 5. AI 编码提示词

```md
任务类型：scaffold
目标：基于 React + TypeScript + Vite + Ant Design 搭建订单管理后台前端骨架。
必须遵守：docs/FRONTEND_BLUEPRINT.md、docs/AI_GUARDRAILS.md、docs/PROJECT_STRUCTURE.md。
允许创建：src/app、src/router、src/components、src/features、src/lib、src/mocks、src/styles、docs。
禁止：实现真实后端业务；页面直接 fetch；硬编码主色/圆角/阴影；绕过 AntD 重写 Button/Table/Form。
验收：pnpm dev 可启动；登录页和首页可访问；AntD ConfigProvider 生效；MSW handlers 存在；LoadingState/EmptyState/ErrorState 存在。
```
