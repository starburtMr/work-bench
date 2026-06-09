# Evidence Model

## 1. 证据等级

| 等级 | 名称 | 例子 | 限制 |
|---|---|---|---|
| E0 | 无证据 | 未找到 API 文档 | 只能判断缺失或不可验证 |
| E1 | 用户口头/聊天 | 用户说“后端能跑” | 只能作为假设 |
| E2 | 文档 | README、PRD、ADR、OpenAPI | 可能过时，需要代码验证 |
| E3 | 静态代码/配置 | route、schema、DTO、CI 文件 | 不代表运行成功 |
| E4 | 可执行结果 | test/build/typecheck/contract test 输出 | 需要记录命令和环境 |
| E5 | 运行/生产/验收 | 监控、日志、发布记录、用户验收 | 注意权限和隐私 |

## 2. 证据到结论的最低标准

| 结论 | 最低证据 |
|---|---|
| 阶段通过 | E4/E5；或 E2/E3 强一致且明确未到发布门禁 |
| 部分具备 | E2 或 E3，但缺关键字段、命令或一致性 |
| 缺失 | E0，且扫描范围已写清楚 |
| 冲突 | 至少两条证据互相矛盾 |
| 过时 | 曾经的真源与当前代码/配置/命令不一致 |
| 不可验证 | 权限、环境、时间、依赖不足导致无法判断 |

## 3. 证据条目格式

```md
- Claim: API 契约与后端路由不一致
- Evidence: `docs/api/openapi.yaml`, `backend/src/routes/users.ts`
- Evidence level: E3
- Observation: OpenAPI 中 `POST /users`，后端实际为 `POST /api/users`
- Impact: 前端 client 生成/调用可能失败
- Confidence: Medium
- Next skill: talk-link
```

## 4. 常见证据陷阱

- 复制旧项目 README 后没有更新命令。
- CI workflow 只跑 echo 或过时脚本。
- OpenAPI 文件来自早期设计，后端已漂移。
- schema 由 ORM 自动同步，migration 缺失。
- mock 数据变成事实来源。
- 用户口头确认与仓库证据相反。
