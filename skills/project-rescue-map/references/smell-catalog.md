# Project Rescue Smell Catalog

| 异味 | 可能根因 | 需要收集证据 | 风险 | 推荐回到 skill |
|---|---|---|---|---|
| 页面很多但主流程不闭环 | V1 scope 缺失、范围膨胀 | 路由、页面、PRD、用户路径 | 方向错误 | idea-check |
| README 命令跑不起来 | 文档漂移、脚本改名 | README、package scripts、Makefile、CI | 新人无法接手 | doc-rules |
| 有 API 文档但前端仍写死 mock | 契约不可用或后端缺失 | OpenAPI、API client、后端 route、mock | 前后端脱节 | talk-link |
| schema 改了但没有 migration | 原型思维进入共享环境 | schema、migrations、DB docs | 数据损坏 | data-map |
| package-lock 和 pnpm-lock 同时活跃 | 包管理器混用 | lockfiles、README、CI | 构建不可复现 | tool-pick |
| 每个组件里都 fetch | 缺前端 API 边界 | pages/components/hooks | 错误处理混乱 | web-frame |
| 后端 route 直接写 SQL 和业务 | 缺 server frame | routes/controllers/services/repos | 难测试难维护 | server-frame |
| CI 只 echo success | 门禁作假 | workflow、scripts | 假通过 | doc-rules / final-check |
| `.env` 进入 git | secret 管理缺失 | git/files/env docs | 安全事故 | server-frame / final-check |
| 管理接口只靠前端隐藏按钮 | 权限模型缺失 | frontend guards、backend middleware | 权限绕过 | talk-link / server-frame |
| 任务列表全是大块功能 | 缺垂直切片和 DoD | roadmap、issues、PRs | 交付失控 | work-plan |
| AI 反复重写同一模块 | 缺规则和真源 | git diff、docs、AGENTS | 技术债膨胀 | doc-rules / web-frame / server-frame |
| 没有回滚但要上线 | 发布门禁缺失 | deploy docs、CI/CD、release notes | 发布事故 | final-check |
| mock 字段多于数据库/API | 展示先行未回填设计 | mock、schema、OpenAPI、API client | 数据/API 错配 | data-map / talk-link |
| 多套样式系统并存 | 未冻结组件库和 token | CSS、theme、component lib | UI 维护成本高 | web-frame |
| 日志输出完整请求体 | 安全和隐私缺口 | logger、middleware、error handler | 数据泄露 | server-frame / final-check |
