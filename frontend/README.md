# Frontend Index

这个目录下放的是 3 个前端示例和一组共享说明文档。
这份文件只做索引，方便快速定位每个项目的作用。

## 示例项目

| 目录 | 作用 | 适合场景 |
| --- | --- | --- |
| [apps/react-vite](./apps/react-vite) | React + Vite + React Router 示例 | 快速做页面、做纯前端 SPA 原型、看最轻量的实现 |
| [apps/nextjs-app](./apps/nextjs-app) | Next.js App Router 示例 | 需要现代 Next.js 写法、布局嵌套、SSR 和 Server Components |
| [apps/nextjs-pages](./apps/nextjs-pages) | Next.js Pages Router 示例 | 维护旧 Next.js 项目、理解传统 Pages Router、做迁移参考 |

## 共享文档

- [docs/application-overview.md](./docs/application-overview.md) - 整个 demo 的业务概览
- [docs/project-structure.md](./docs/project-structure.md) - 通用目录结构和分层思路
- [docs/project-standards.md](./docs/project-standards.md) - 代码和协作规范
- [docs/api-layer.md](./docs/api-layer.md) - API 层约定
- [docs/state-management.md](./docs/state-management.md) - 状态管理约定
- [docs/testing.md](./docs/testing.md) - 测试策略
- [docs/components-and-styling.md](./docs/components-and-styling.md) - 组件和样式约定
- [docs/performance.md](./docs/performance.md) - 性能建议
- [docs/error-handling.md](./docs/error-handling.md) - 错误处理建议
- [docs/security.md](./docs/security.md) - 安全建议

## 每个示例自己的说明

每个示例目录下还有自己的 `AGENTS.md` 和 `docs/`：

- `apps/react-vite`
- `apps/nextjs-app`
- `apps/nextjs-pages`

它们只对各自示例生效，用来写更具体的技术栈和开发约束。
