# Example: Messy SaaS Project Rescue Report

> 这是示例，不代表真实项目。用于展示报告粒度和表达方式。

## 1. 诊断范围

- 项目根目录：`/repo/acme-saas`
- 诊断模式：Standard Rescue Audit
- 已读取证据：`README.md`、`package.json`、`apps/web/*`、`apps/api/*`、`prisma/schema.prisma`、`.github/workflows/ci.yml`
- 未读取证据：生产日志、真实数据库、外部支付后台
- 已执行命令：未执行；本轮只做静态扫描
- 当前假设：该项目为 Next.js + API service + PostgreSQL SaaS MVP

## 2. 止血门结论

- 决策：CONTAIN
- 触发信号：`prisma/schema.prisma` 存在账单字段，但未发现 migration 计划；前端 billing 页面调用 mock；API 未发现对应权限检查。
- 立即禁止事项：不要继续开发 billing/payment 相关功能，不要执行 migration。
- 允许继续的诊断范围：产品 scope、数据设计、API 契约、后端权限基线。

## 3. 总体结论

- 当前状态：条件可继续
- 主要阻塞：数据模型和 API 契约缺真源；billing 范围疑似超出 V1；CI 未跑测试。
- 推荐补救主线：`01 -> 03 -> 04 -> 07 -> 09 -> 10`
- 最高优先级下一步：调用 `idea-check` 冻结 V1 scope，确认 billing 是否属于 V1。

## 4. 阶段缺口矩阵

| 阶段 | Skill | 状态 | 证据等级 | 置信度 | 证据 | 缺口 | 风险等级 | 建议下一步 |
|---|---|---|---|---|---|---|---|---|
| 01 | idea-check | 冲突 | E2/E3 | Medium | README 称 V1 只做 team tasks；web 有 billing route | billing 是否属于 V1 不清 | 阻塞 | 回到 idea-check |
| 02 | tool-pick | 部分具备 | E3 | Medium | package.json + pnpm-lock | 缺技术决策文档 | 可后补 | 回到 tool-pick 简补 |
| 03 | data-map | 部分具备 | E3 | Medium | prisma/schema.prisma | 缺 ERD、migration plan、敏感字段策略 | 阻塞 | 回到 data-map |
| 04 | talk-link | 缺失 | E0/E3 | Low | route 存在但无 OpenAPI | 前后端 DTO/mock 不一致 | 阻塞 | 回到 talk-link |
| 05 | skeleton-check | 不可验证 | E3 | Low | apps/web/apps/api | 未发现骨架选择记录 | 可后补 | 结合 06/07 补 |
| 06 | web-frame | 部分具备 | E3 | Medium | apps/web/routes | API client 分散 | 必须补 | 回到 web-frame |
| 07 | server-frame | 部分具备 | E3 | Medium | apps/api/routes | 权限和错误结构不统一 | 必须补 | 回到 server-frame |
| 08 | work-plan | 缺失 | E0 | Low | 未发现任务切片 | 无 DoD | 必须补 | 回到 work-plan |
| 09 | doc-rules | 冲突 | E2/E3 | Medium | README vs scripts | README 命令过时 | 必须补 | 回到 doc-rules |
| 10 | final-check | 缺失 | E0 | Low | 未发现验收报告 | 无证据包/回滚 | 必须补 | 最后回到 final-check |

## 5. 补救路线图

| 顺序 | 回到阶段 | 调用 skill | 目标产出 | 通过门槛 | 依赖/前置 |
|---|---|---|---|---|---|
| 1 | 01 | idea-check | V1 scope，确认 billing 是否进入 V1 | Must/Won't 明确 | 产品 owner 确认 |
| 2 | 03 | data-map | 业务对象、ERD、migration plan | schema 与 V1 一致 | V1 scope |
| 3 | 04 | talk-link | API 契约、DTO、错误码、权限 | 前后端 client/route 一致 | 数据模型 |
| 4 | 07 | server-frame | 后端错误、权限、配置基线 | authz 不只靠前端 | API 契约 |
| 5 | 09 | doc-rules | README/docs/AGENTS/CI 同步 | 新人按 README 可启动 | 真实脚本 |
| 6 | 10 | final-check | 继续开发证据包 | 无阻塞项 | 1-5 完成 |
