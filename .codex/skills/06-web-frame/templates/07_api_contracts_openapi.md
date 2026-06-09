# API_CONTRACTS.md

## 1. 原则

- 前端骨架阶段先定义契约，不替后端实现业务规则。
- 所有请求经过统一 API Client。
- 接口类型集中管理，不散落在页面中。
- 每个接口都要有加载、空、错、权限不足、提交中等页面状态处理。
- 中大型项目建议维护 `openapi.yaml`，用于生成类型、Mock、文档和测试。

## 2. 通用响应结构

```ts
export type ApiResponse<T> = {
  data: T;
  message?: string;
  requestId?: string;
};

export type ApiError = {
  code: string;
  message: string;
  details?: unknown;
  requestId?: string;
};
```

## 3. 统一请求层文件

```text
src/api/
  client.ts       # baseURL、headers、auth、拦截器、错误转换
  errors.ts       # ApiError、错误码映射
  types.ts        # 通用响应类型
  mock.ts         # Mock 策略入口
src/modules/<module>/api.ts
```

## 4. 接口清单

| 能力 | 方法 | 路径 | Auth | 请求 | 响应 | 页面状态 |
|---|---|---|---|---|---|---|
| 登录 | POST | `/api/auth/login` | 否 | username/password | token/user | 提交中/成功/失败 |
| 当前用户 | GET | `/api/auth/me` | 是 | - | user | 加载/未登录/错误 |

## 5. 接口详情模板

## 接口：<接口名>

- Method：
- Path：
- Auth：none / optional / required
- Owner：

### Query / Params / Body

| 字段 | 类型 | 必填 | 说明 | 示例 |
|---|---|---|---|---|
|  |  |  |  |  |

### Response

```ts
type Response = {};
```

### Error

| code | message | 前端处理 |
|---|---|---|
| AUTH_REQUIRED | 请先登录 | 跳转登录 |
| FORBIDDEN | 无权限 | 显示权限不足 |
| VALIDATION_ERROR | 参数错误 | 表单字段错误 |
| INTERNAL_ERROR | 服务异常 | ErrorState + 重试 |

### Mock 数据

```json
{}
```

### 页面状态映射

- loading：
- empty：
- success：
- error：
- unauthorized：
- forbidden：

## 6. OpenAPI 草案骨架

```yaml
openapi: 3.1.0
info:
  title: Project API
  version: 0.1.0
servers:
  - url: /api
paths:
  /auth/login:
    post:
      summary: Login
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [username, password]
              properties:
                username:
                  type: string
                password:
                  type: string
      responses:
        '200':
          description: Login success
        '400':
          description: Validation error
components:
  schemas:
    ApiError:
      type: object
      required: [code, message]
      properties:
        code:
          type: string
        message:
          type: string
        details: {}
```
