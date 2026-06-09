# API 契约文档

## 1. API 全局规则

- Base URL：`/api/v1`
- 认证方式：未定/Session/JWT/OAuth2/API Key/其他
- 成功响应格式：统一 envelope / 其他
- 错误响应格式：统一 envelope + Problem Details 字段 / strict application/problem+json / 其他
- requestId / traceId：必须包含
- 删除成功策略：204 No Content / 200 JSON，二选一
- 参数错误策略：400 / 422，二选一并全项目统一

## 2. 接口清单

| 方法 | 路径 | 业务目的 | 认证 | 角色权限 | 请求参数 | 成功响应 | 失败响应 | 读写数据 | 日志 | 幂等/安全 |
|---|---|---|---|---|---|---|---|---|---|---|
| GET | /health | 健康检查 | 否 | 无 | 无 | 200 | 500 | health only | 请求日志 | 不暴露敏感信息 |

## 3. 单接口模板

### [METHOD] /api/v1/example

#### 业务目的

#### 调用角色

#### 认证要求

#### 请求参数

| 位置 | 字段 | 类型 | 必填 | 校验规则 | 示例 |
|---|---|---|---|---|---|
| query/body/path/header |  |  | 是/否 |  |  |

#### 成功响应

```json
{
  "success": true,
  "data": {},
  "meta": {
    "requestId": "req_xxx",
    "timestamp": "2026-06-09T12:00:00Z"
  }
}
```

#### 失败响应

| 场景 | HTTP 状态码 | 业务错误码 | message | 处理位置 |
|---|---:|---|---|---|
| 参数错误 | 400/422 | VALIDATION_ERROR | 请求参数错误 |  |

#### 数据读写

- 读取：
- 写入：
- 事务：

#### 日志要求

#### 幂等与安全要求
