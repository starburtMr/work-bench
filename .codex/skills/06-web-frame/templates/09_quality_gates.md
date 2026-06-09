# QUALITY_GATES.md

## 1. 命令清单

| 命令 | 目的 | 必须通过阶段 |
|---|---|---|
| install | 安装依赖 | 每次环境初始化 |
| dev | 本地启动 | 骨架阶段 |
| type-check | 类型检查 | 每次提交前 |
| lint | 代码规范 | 每次提交前 |
| format | 格式化 | 每次提交前 |
| test | 单元测试 | 组件/工具函数变更后 |
| test:e2e | 端到端测试 | 核心流程变更后 |
| build | 生产构建 | 每次阶段验收 |
| storybook | 组件隔离验证 | 组件库/基础组件变更后 |

## 2. 推荐 package scripts 模板

> 具体命令按项目技术栈调整。

```json
{
  "scripts": {
    "dev": "vite --host 0.0.0.0",
    "build": "tsc -b && vite build",
    "type-check": "tsc --noEmit",
    "lint": "eslint .",
    "format": "prettier . --write",
    "format:check": "prettier . --check",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:e2e": "playwright test",
    "storybook": "storybook dev -p 6006"
  }
}
```

## 3. 骨架验收

- [ ] dev 可启动。
- [ ] build 成功。
- [ ] type-check 无错误。
- [ ] lint 无错误或已有明确 TODO。
- [ ] Token 生效。
- [ ] 组件库主题生效。
- [ ] API Client 可调用 Mock。
- [ ] 首页、登录页、404 可访问。
- [ ] 页面状态完整。

## 4. AI 生成代码验收

- [ ] 未新增未经确认的依赖。
- [ ] 未改动无关模块。
- [ ] 未绕开目录规范。
- [ ] 未绕开组件复用规则。
- [ ] 未散落硬编码样式。
- [ ] 未散落 API 请求。
- [ ] 有启动与验证说明。
