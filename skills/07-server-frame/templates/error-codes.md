# 业务错误码登记表

错误码格式：`领域_错误原因`。错误码必须稳定，message 可以调整，code 不得随意改名。

| 错误码 | HTTP 状态码 | 用户提示 | 触发场景 | 处理位置 | 维护人/模块 |
|---|---:|---|---|---|---|
| VALIDATION_ERROR | 400/422 | 请求参数错误 | 参数校验失败 | 全局校验/错误处理 | common |
| AUTH_UNAUTHORIZED | 401 | 未登录或登录已过期 | 缺少或无效认证信息 | auth middleware/guard | auth |
| AUTH_FORBIDDEN | 403 | 无权限操作 | 角色/对象权限不足 | auth middleware/guard | auth |
| RESOURCE_NOT_FOUND | 404 | 资源不存在 | 查询资源为空或不可见 | service/error handler | common |
| RESOURCE_CONFLICT | 409 | 资源状态冲突 | 重复提交/状态不允许 | service/error handler | common |
| RATE_LIMITED | 429 | 请求过于频繁 | 命中限流 | middleware | common |
| INTERNAL_ERROR | 500 | 系统异常 | 未预期服务端错误 | global error handler | common |
