# Repository Scan Checklist

## 1. 指令与入口

- [ ] 最近的 `AGENTS.md` / `AGENTS.override.md` / `Claude.md`。
- [ ] `.codex/config.toml` 或其他 agent 配置。
- [ ] `README.md`。
- [ ] `docs/README.md` / `docs/index.md`。
- [ ] 项目状态文件：`PROJECT_STATE`、`TASK_LOG`、`PLANS.md`、ADR。

## 2. 产品与计划

- [ ] PRD / V1 scope。
- [ ] 用户路径 / user journey。
- [ ] 验收标准 / demo script。
- [ ] 任务切片 / roadmap / DoD。
- [ ] 变更记录 / 决策记录。

## 3. 技术栈与依赖

- [ ] `package.json` / `pnpm-lock.yaml` / `yarn.lock` / `package-lock.json`。
- [ ] `pyproject.toml` / `requirements.txt` / `poetry.lock`。
- [ ] `go.mod` / `Cargo.toml` / `pom.xml` / `build.gradle`。
- [ ] `Makefile` / `Taskfile` / npm scripts。
- [ ] 框架配置：Next/Vite/Nuxt/Django/FastAPI/Rails/Laravel/Spring 等。

## 4. 数据

- [ ] schema / models / entities。
- [ ] migrations。
- [ ] seed / fixtures。
- [ ] DB config / env usage。
- [ ] 数据访问层 / repository / ORM client。
- [ ] 备份、回滚、迁移计划文档。

## 5. API

- [ ] OpenAPI / GraphQL schema / RPC proto。
- [ ] 后端 route/controller/handler。
- [ ] DTO / validation schema。
- [ ] 前端 API client。
- [ ] mock / MSW / fixture。
- [ ] 错误码、鉴权、分页、排序、过滤、幂等。

## 6. 前端

- [ ] 路由和页面。
- [ ] layout / component / module 结构。
- [ ] design tokens / theme。
- [ ] 状态管理。
- [ ] 表单校验。
- [ ] API client 使用是否集中。
- [ ] 构建、lint、typecheck、测试脚本。

## 7. 后端

- [ ] 入口和启动。
- [ ] 配置加载和 env 文档。
- [ ] 日志、requestId、错误处理中间件。
- [ ] 鉴权、权限、输入校验。
- [ ] 健康检查。
- [ ] 任务队列、缓存、文件存储、外部服务。

## 8. 质量与交付

- [ ] 单元测试、集成测试、契约测试、E2E。
- [ ] CI workflow。
- [ ] Dockerfile / compose / deployment config。
- [ ] release notes / rollback plan。
- [ ] monitoring / logs / incident postmortem。

## 9. 安全与供应链

- [ ] secrets 是否进入仓库。
- [ ] `.env.example` 与实际 env usage 是否一致。
- [ ] lockfile 是否唯一且更新。
- [ ] 依赖高危或过期迹象。
- [ ] CI 权限和 token 权限。
- [ ] 构建产物来源和可追溯性。
