# 前端框架证据提取适配器

数据库设计必须优先从用户流程和页面证据中推导。当前端项目可用时，按框架识别入口。

## 1. Next.js App Router

检查：

- `app/**/page.tsx` / `page.jsx`：页面入口。
- `app/**/layout.tsx`：共享布局，常暗示模块边界。
- `app/**/route.ts`：API route / 资源操作。
- 动态段 `[id]`、`[slug]`：实体详情或资源标识。
- route groups `(group)`：业务区域或权限区域。
- server actions / form actions：写入动作。

数据库线索：页面展示字段、动态路由参数、表单、筛选、排序、API route。

## 2. React Router

检查：

- `app/routes.ts` 或 route config。
- Route Object。
- loader：读取需求。
- action：写入/变更需求。
- dynamic params：实体标识。
- middleware/guard：权限与审计线索。

## 3. Vue / Nuxt

检查：

- Vue Router routes 配置。
- Nuxt `pages/` 文件路由。
- `server/api`、`server/routes`。
- 表单组件、Pinia/store、API client。

## 4. Angular

检查：

- `Routes` 数组。
- route guard。
- resolver。
- reactive form。
- service 层 HTTP 调用。

## 5. SvelteKit

检查：

- `src/routes/**/+page.svelte`：页面。
- `+page.server.ts`：服务端数据读取/表单动作。
- `+server.ts`：API endpoint。
- `[id]` / `[slug]`：动态实体。

## 6. Remix

检查：

- routes。
- loader：读取需求。
- action：写入需求。
- resource routes。
- Form 提交。

## 7. 字段还原规则

前端字段分为：

- 数据库原子字段：如 `email`, `phone`, `title`。
- 组合展示字段：如 `displayName`, `contactInfo`。
- 聚合字段：如 `orderCount`, `commentCount`。
- 计算字段：如 `remainingTime`, `displayStatus`。
- 权限派生字段：如 `canEdit`, `canDelete`。
- UI 临时字段：如 `isOpen`, `selected`, `expanded`。

只有数据库原子字段和确认为需要持久化的业务字段才进入表设计。
