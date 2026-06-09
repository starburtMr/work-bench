# IMPLEMENTATION_PLAN.md

## 1. 阶段总览

| 阶段 | 目标 | 交付物 | 验收 |
|---|---|---|---|
| P0 决策 | 明确模式、平台、技术栈、风格 | 决策表、默认假设 | 用户确认或默认假设写明 |
| P1 骨架 | 项目能启动且结构正确 | 脚手架、目录、docs、Token、组件库 | dev/build/typecheck/lint 通过 |
| P2 基础页面 | 建最小页面地图 | 登录、首页、列表示例、状态页 | 路由可访问，状态完整 |
| P3 API/Mock | 前端无后端也能跑 | request client、DTO、MSW | Mock 可切换，错误态可测 |
| P4 业务模块 | 按模块增量开发 | feature modules | 不破坏已有骨架 |
| P5 加固 | 测试、无障碍、性能、主题 | 测试、checklist、优化 | 质量门禁通过 |

## 2. P1 骨架文件清单

```text
docs/
  FRONTEND_BLUEPRINT.md
  AI_GUARDRAILS.md
  PROJECT_STRUCTURE.md
  DESIGN_TOKENS.md
  COMPONENT_RULES.md
  API_CONTRACTS.md
  TESTING_STRATEGY.md
  ACCEPTANCE_CHECKLIST.md
src/
  styles/
    tokens.css
    theme.css
    globals.css
  lib/
    request.ts
  api/
  components/
    ui/
    layout/
    feedback/
    business/
  features/
  mocks/
```

## 3. 开发顺序

1. 创建官方脚手架。
2. 接入 TypeScript、ESLint、Prettier。
3. 接入组件库和全局主题。
4. 创建 Token 文件。
5. 创建目录结构。
6. 创建 AppShell / PageContainer / LoadingState / EmptyState / ErrorState。
7. 创建 request client 和 API 契约。
8. 创建 Mock 层。
9. 创建登录 / 首页 / 列表示例路由。
10. 创建测试和质量脚本。
11. 更新 docs。
12. 验收并提交 Git。

## 4. 每阶段结束必须输出

```md
## 本阶段交付
- ...

## 修改文件
- ...

## 验收命令
- ...

## 已知假设
- ...

## 下一阶段建议
- ...
```

