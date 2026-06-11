# Data and API Consistency Checklist

## 1. 数据对象到 API

- [ ] V1 用户路径能映射到业务对象。
- [ ] 每个核心 API 都能追溯到业务对象和表/model。
- [ ] API response 字段不是随意拼接，字段来源明确。
- [ ] 前端展示字段与真实数据字段区分清楚。
- [ ] 枚举、状态机、生命周期在 DB/API/前端一致。

## 2. API 契约到前后端

- [ ] OpenAPI/契约文档存在且被引用为真源。
- [ ] 后端路由方法、路径、参数与契约一致。
- [ ] DTO/validation schema 与契约一致。
- [ ] 前端 API client 只通过统一入口调用。
- [ ] 错误结构、错误码、权限错误、校验错误一致。
- [ ] 分页、排序、过滤字段一致。

## 3. Migration 与运行安全

- [ ] schema/model 与 migrations 一致。
- [ ] migration 有顺序和命名规则。
- [ ] 破坏性变更有回滚/前滚计划。
- [ ] 共享/生产环境已执行状态清楚。
- [ ] seed 不会覆盖真实数据。

## 4. 常见红旗

- [ ] 前端 mock 字段多于后端 response。
- [ ] 后端返回 `any` / 未校验对象。
- [ ] 多个 API client 并存。
- [ ] 同一状态在前端、后端、数据库用不同字符串。
- [ ] migration 目录缺失但 schema 已变。
- [ ] 文档写 REST，代码实际 GraphQL/RPC，或反之。
