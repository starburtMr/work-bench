# 示例：从 0 到 1 搭 Next.js SaaS / AI 工具骨架

## 用户输入

我要做一个 AI 写作工具，有官网、登录、工作台、文档列表、编辑器页、设置页。希望风格像现代 SaaS，浅色为主，后续可能要 SEO 和多语言。

## Skill 应答方向

### 1. 模式判断

新项目从 0 到 1，目标端为响应式 Web，产品类型为 SaaS / AI 工具。

### 2. 推荐技术栈

- 框架：Next.js + TypeScript + App Router
- UI：Tailwind + shadcn/ui
- 样式：CSS Variables + Tailwind theme variables
- API：统一 `src/lib/request.ts`，若无后端则 MSW
- 状态：URL 状态 + 本地状态；服务端状态按需使用 TanStack Query
- 测试：Playwright 核心流程，组件测试按需

### 3. 页面地图

| 页面 | 路由 | 目标 |
|---|---|---|
| 官网首页 | `/` | 产品介绍、CTA、SEO |
| 登录 | `/login` | 登录/注册入口 |
| 工作台 | `/app` | 最近文档、快捷入口 |
| 文档列表 | `/app/docs` | 搜索、筛选、分页 |
| 编辑器 | `/app/docs/[id]` | 内容编辑、保存状态 |
| 设置 | `/app/settings` | 用户偏好、主题、多语言 |

### 4. 目录策略

```text
src/app/
  layout.tsx
  page.tsx
  login/page.tsx
  app/layout.tsx
  app/page.tsx
  app/docs/page.tsx
  app/docs/[id]/page.tsx
  app/settings/page.tsx
src/components/ui/
src/components/layout/
src/features/docs/
src/features/auth/
src/lib/
src/styles/
```

### 5. AI 编码提示词

```md
任务类型：scaffold
目标：搭建 Next.js SaaS 骨架，不开发完整 AI 编辑功能。
必须遵守：先建立 docs 规范、Token、目录、AppShell、基础路由。
允许：创建基础页面占位、shadcn/ui 基础组件、Tailwind tokens。
禁止：复制参考产品设计；硬编码颜色；在页面里写死接口；实现真实 AI 调用。
验收：首页、登录、工作台可访问；主题变量生效；App Router 结构清晰；docs 规范完整。
```
