# Frontend / Backend Boundary Rescue Playbook

## 触发信号

- 前端页面已写很多，但后端没有对应接口。
- 后端接口存在，但前端 mock 字段不一致。
- API client 分散在组件、页面、hook 中。
- 错误处理、loading、权限判断每处写法不同。
- 后端 route/controller/service/data access 混在一起。

## 诊断步骤

1. 列出 V1 页面和用户动作。
2. 找每个页面的数据来源和调用路径。
3. 找前端 API client 是否集中。
4. 找后端 route/controller/service/repository 边界。
5. 对照 API 契约或生成缺口清单。
6. 区分“契约问题”与“骨架治理问题”。

## 分流规则

| 问题 | 回到 skill |
|---|---|
| API 路径/DTO/错误/权限不一致 | `talk-link` |
| 前端目录、组件、样式、client 分散 | `web-frame` |
| 后端入口、错误、日志、配置、数据访问边界混乱 | `server-frame` |
| 产品页面不该存在或缺核心路径 | `idea-check` |
| 文档和 CI 与真实命令不一致 | `doc-rules` |

## 输出

| 页面/接口 | 前端位置 | 后端位置 | 契约位置 | 状态 | 主要冲突 | 建议 skill |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
