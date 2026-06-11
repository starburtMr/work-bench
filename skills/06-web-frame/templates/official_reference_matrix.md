# 官方资料参考矩阵（2026-06-09 调研）

> 本文件用于提醒 Skill 使用者：选择框架、组件库、样式系统和质量工具时，应优先参考官方文档，而不是让 AI 凭空发明规则。具体版本和 CLI 命令在执行时应再次查看对应官网。

## 1. 框架 / 元框架

| 技术 | 官方资料 | Skill 中的用法 |
|---|---|---|
| React | https://react.dev/ | React 是 UI 组件库，不自带完整路由和数据方案；搭完整应用时需配合框架/路由/数据层 |
| Vite | https://vite.dev/guide/ | React/Vue SPA 骨架的优先构建工具之一 |
| Next.js | https://nextjs.org/docs/app | 需要 App Router、文件路由、布局、SSR/SEO 时使用 |
| Vue | https://vuejs.org/guide/quick-start | Vue 3 + Vite + SFC 项目骨架 |
| Nuxt | https://nuxt.com/ | Vue 全栈/SSR/文件路由场景 |
| Angular | https://angular.dev/ | 大型企业级 Web 应用可选，使用官方 Router/CLI/结构 |
| SvelteKit | https://svelte.dev/docs/kit/routing | Svelte 全栈文件路由场景 |
| Astro | https://astro.build/ | 内容驱动网站、官网、博客、文档 |
| React Native | https://reactnative.dev/ | 原生 iOS/Android App |
| Expo | https://docs.expo.dev/ | React Native 应用快速骨架和跨平台工具链 |
| Taro | https://docs.taro.zone/en/docs/ | React/Vue 多端、小程序、H5、RN 场景 |
| uni-app | https://uniapp.dcloud.net.cn/ | Vue 多端、小程序、App、H5 场景 |

## 2. UI 组件库

| 技术 | 官方资料 | Skill 中的用法 |
|---|---|---|
| Ant Design | https://ant.design/docs/react/introduce/ | React 企业级后台、表格表单密集场景 |
| MUI | https://mui.com/material-ui/ | React + Material Design 或可定制主题场景 |
| Element Plus | https://element-plus.org/ | Vue 3 后台与业务系统 |
| Naive UI | https://www.naiveui.com/ | Vue 3、TypeScript、主题可定制场景 |
| shadcn/ui | https://ui.shadcn.com/ | Tailwind + 本地可控 UI 源码，适合 SaaS/AI 工具 |
| Tailwind CSS | https://tailwindcss.com/ | Utility-first 样式系统，需结合 Token 约束 |
| Vant | https://youzan.github.io/vant/ | Vue 移动 H5 |
| NutUI | https://nutui.jd.com/ | 移动端 / 小程序组件库，适合 Taro 生态 |
| Nuxt UI | https://ui.nuxt.com/ | Nuxt/Vue + Tailwind 组件库 |

## 3. 状态、API、测试、质量

| 技术 | 官方资料 | Skill 中的用法 |
|---|---|---|
| TypeScript | https://www.typescriptlang.org/ | 默认强制，建立类型边界 |
| TanStack Query | https://tanstack.com/query/latest | 服务端状态、请求缓存、刷新 |
| Pinia | https://pinia.vuejs.org/ | Vue 全局客户端状态 |
| Zustand | https://zustand.docs.pmnd.rs/ | React 轻量客户端状态 |
| Redux Toolkit | https://redux-toolkit.js.org/ | 大型复杂全局状态 |
| OpenAPI | https://swagger.io/specification/ | REST API 契约标准 |
| MSW | https://mswjs.io/docs/ | API Mock，前后端并行开发 |
| Vitest | https://vitest.dev/ | Vite 项目测试 |
| Testing Library | https://testing-library.com/ | 以用户行为为中心的组件测试 |
| Playwright | https://playwright.dev/ | 端到端测试和冒烟验收 |
| ESLint | https://eslint.org/ | Lint 问题发现 |
| Prettier | https://prettier.io/ | 代码格式统一 |
| WCAG/WAI | https://www.w3.org/WAI/standards-guidelines/wcag/ | 无障碍基线 |
| MDN Responsive Design | https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design | 响应式与媒体查询基线 |
| DTCG Design Tokens | https://www.designtokens.org/ | Token 跨工具/跨平台概念 |
| Apple HIG | https://developer.apple.com/design/human-interface-guidelines | Apple 平台设计参考 |
| Material Design 3 | https://m3.material.io/ | Material 风格与组件/颜色/排版参考 |
