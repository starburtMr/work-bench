# OFFICIAL_REFERENCE_MATRIX.md

本文件整理了创建本 Skill v2 时参考的官方资料方向。实际项目中应优先查对应官网最新文档。

## 1. 框架与目录

| 技术 | 官方要点 | 对 Skill 的影响 |
|---|---|---|
| React | 新 React 应用推荐从框架开始；从零搭建需要自己选择路由、数据获取等方案 | React SPA 默认必须明确路由、数据、状态，不让 AI 随机选 |
| Vite | 官方脚手架支持 React/Vue/Svelte/Solid 等模板，并提示 Node 版本要求 | React/Vue 轻量 SPA 默认可用 Vite，但要记录 Node/包管理器 |
| Next.js App Router | `app` 目录嵌套文件夹定义路由；`layout`、`loading`、`error`、`not-found`、`page` 有特殊层级 | Next 项目不得随意组织 `app`；业务代码可放 `modules/lib/components` |
| Vue | `create-vue` 官方脚手架会提示 TypeScript、Router、Pinia、Vitest、E2E、ESLint、Prettier 等选项 | Vue 新项目应显式选择这些工程选项 |
| Angular | Angular CLI `ng new` 创建 workspace；workspace 可包含一个或多个 project | Angular 项目要尊重 workspace 和 CLI 配置，不照搬 React/Vue 目录 |
| Nuxt | Nuxt 4 目录结构含 `app/pages`、`components`、`composables`、`layouts`、`middleware`、`plugins`、`utils` | Nuxt 项目以官方目录为第一约束 |
| Astro | `src/pages` 创建路由，`src/components` 放可复用组件，`src/layouts` 放共享 UI 结构 | 内容型网站不要用后台式目录硬套 |
| Expo / React Native | React Native 新项目官方推荐 Expo 作为生产级框架，支持 Android、iOS、TV、Web | APP 项目不能套 Web DOM 逻辑，需用 Expo/Native 组件思维 |
| Taro | 跨端跨框架方案，支持 React/Vue 开发多类小程序、H5、RN | 小程序/跨端要先确认平台能力和组件限制 |
| uni-app | Vue 语法开发多端，可发布到 iOS、Android、Web、各种小程序等平台 | Vue 团队多端项目可选 uni-app，但需处理平台差异 |

## 2. UI 组件库与样式

| 技术 | 官方要点 | 对 Skill 的影响 |
|---|---|---|
| Ant Design | 提供丰富组件和设计规范生态，适合快速构建网站应用 | B 端后台默认推荐之一 |
| Element Plus | Vue 3 UI 框架，提供设计指南、组件和资源 | Vue 后台默认推荐之一 |
| MUI | React UI 工具套件，支持 Material Design 或自定义设计系统，重视可访问性 | React 产品可选，适合需要 Material 或自定义主题 |
| shadcn/ui | 不是传统组件库，而是开放代码的组件分发和构建设计系统方式 | 使用时必须维护本地 `components/ui` 和主题，不当作 npm 组件库 |
| Tailwind CSS | `@theme` 主题变量影响工具类生成，适合把设计 Token 变成 utility API | Tailwind 项目必须用 Token 管理，禁止任意值泛滥 |
| Radix UI | 开源组件库，强调快速开发、维护和可访问性 | 适合需要 headless/accessible primitives 的设计系统 |
| Style Dictionary | 可把 Design Tokens 导出到 iOS、Android、CSS、JS 等平台 | 多端或设计系统项目可用 tokens.json + 转换流程 |

## 3. API、状态、测试、体验

| 技术 / 标准 | 官方要点 | 对 Skill 的影响 |
|---|---|---|
| OpenAPI | 标准化描述 HTTP API，可帮助理解 API、生成代码、测试和应用设计标准 | API_CONTRACTS 可升级为 openapi.yaml |
| TanStack Query | 管理服务端状态：缓存、生命周期、刷新、mutation、跨框架适配 | 不要把服务端状态塞进全局 store |
| Vitest | Vite 原生测试运行器，能复用 Vite 配置 | Vite 项目优先考虑 Vitest |
| Playwright | 现代 Web E2E 测试，支持 Chromium/WebKit/Firefox、移动模拟 | 核心流程应考虑 E2E 验收 |
| WCAG | Web 内容可访问性建议，覆盖多类残障和设备场景 | 页面规格要包含 label、焦点、键盘、错误提示等 |
| MDN RWD | 响应式设计是让页面在不同屏幕和分辨率下保持可用 | Token 和页面规格必须包含断点和响应式规则 |
