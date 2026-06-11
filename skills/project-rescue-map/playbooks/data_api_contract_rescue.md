# Data and API Contract Rescue Playbook

## 触发信号

- 前端字段、API 文档、后端 DTO、数据库字段不一致。
- 有 schema 但没有 migration 计划。
- 有 API route 但没有统一错误结构。
- 前端直接散落 fetch/axios。
- mock 与真实 API 不一致。

## 诊断顺序

1. 从 V1 用户路径列出核心动作。
2. 为每个动作定位业务对象和数据生命周期。
3. 对照 schema/model/migration，标出缺表、错关系、危险字段。
4. 对照 API 契约、后端 route、前端 client，标出路径、DTO、错误、权限冲突。
5. 把问题分成：先回 `data-map`，再回 `talk-link`。
6. 禁止直接让前端或后端继续按当前混乱接口写新功能。

## 输出矩阵

| 用户动作 | 业务对象 | 数据证据 | API 证据 | 前端证据 | 冲突 | 回到 skill |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  | data-map / talk-link |

## 推荐路线

1. `data-map`：冻结业务对象、关系、表设计、migration 计划。
2. `talk-link`：冻结 API 契约、DTO、错误码、鉴权、mock/contract test。
3. `web-frame` / `server-frame`：按契约更新前后端边界。
4. `final-check`：验证契约一致性。
