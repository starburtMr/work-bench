---
name: talk-link
description: "Define the API contract and frontend-backend integration rules between schema design and implementation. Use when endpoints, DTOs, errors, auth, pagination, or mock strategy need to be set."
---

# API 契约与前后端联调设计 Skill


## 1. 在完整开发工作流中的位置

- 阶段编号：`04`
- 阶段名称：API 契约 / 前后端联调边界冻结
- 总控入口：[`build-map`](../00-build-map/SKILL.md)
- 本阶段目标：在前端、后端和数据库之间建立统一接口真源，冻结 V1 接口、DTO、错误、权限、分页、Mock 和契约测试规则。

## 2. 何时启用

当产品边界、技术栈和首版数据模型已经有初稿，需要在前端、后端和数据库之间建立统一接口真源时启用。典型场景包括：

- 前端准备搭骨架，但接口返回结构、错误结构、分页、鉴权、Mock 还没统一。
- 后端准备搭骨架，但 API 边界、资源命名、错误码、状态码、OpenAPI 策略还没冻结。
- 数据库已经设计了表，但不知道哪些对象通过接口暴露，哪些只属于内部实现。
- 已有项目接口散落、前后端字段对不上、错误处理不统一，需要收敛。

## 3. 上游输入契约

本 skill 不应孤立执行。除非用户明确要求单独使用，否则应优先读取或生成以下输入：

- `<project-root>/docs/product/v1-mvp-scope.md`
- `<project-root>/docs/product/user-journey-and-data-flow.md`
- `<project-root>/docs/architecture/tech-stack-decision.md`
- `<project-root>/docs/database/database-design.md`
- 若已有前后端代码：路由、API client、controller/service、OpenAPI、Postman collection、mock 文件、类型定义。

信息不足时，不要直接生成一套“看起来完整”的 API。必须标注：已确认、合理推导、待确认。

## 4. 下游输出契约

必须输出可落盘的接口真源：

- `<project-root>/docs/api/api-contract-source-of-truth.md`：接口契约真源。
- `<project-root>/docs/api/resource-model.md`：资源、领域对象、DTO、数据库对象的映射关系。
- `<project-root>/docs/api/openapi.yaml` 或 `<project-root>/docs/api/openapi.md`：OpenAPI 草案。
- `<project-root>/docs/api/error-response-and-codes.md`：HTTP 状态码、业务错误码、错误响应结构。
- `<project-root>/docs/api/auth-and-permission-contract.md`：认证、授权、角色与权限检查点。
- `<project-root>/docs/api/pagination-filtering-sorting.md`：分页、过滤、排序、搜索约定。
- `<project-root>/docs/api/mock-and-contract-testing-plan.md`：Mock、契约测试和前后端联调计划。
- `<project-root>/docs/api/integration-risk-list.md`：跨端字段、时区、金额、幂等、并发、第三方依赖风险。

## 5. 与其他 skill 的引用关系

### 上游 skill

- [`idea-check`](../01-idea-check/SKILL.md)
- [`tool-pick`](../02-tool-pick/SKILL.md)
- [`data-map`](../03-data-map/SKILL.md)

### 下游 skill

- [`web-frame`](../06-web-frame/SKILL.md)
- [`server-frame`](../07-server-frame/SKILL.md)
- [`work-plan`](../08-work-plan/SKILL.md)

### 5.3 交接载荷

交给下游时，至少携带以下信息：

- 接口契约真源、资源模型和 OpenAPI 草案。
- 统一响应、错误结构、认证、权限和分页规则。
- Mock、契约测试和联调顺序。
- 跨端字段、时区、金额、幂等、并发等风险项。

## 6. 核心原则

1. API 是前后端协作边界，不是某一端的临时实现细节。
2. 接口字段必须来自产品流程、页面数据需求和数据库模型，不能凭空造字段。
3. API DTO 不等于数据库表；可以聚合、裁剪、脱敏、计算，但必须说明来源。
4. 错误结构必须统一，不能每个接口自由发挥。
5. 金额、时间、枚举、状态机、权限和幂等规则必须显式定义。
6. 前端 Mock 必须服从接口契约，不得自己发明返回结构。
7. 后端实现必须服从接口契约；若实现发现契约不合理，必须回到本 skill 修订契约，而不是私自改接口。
8. 对外 API 一旦进入 V1 开发，破坏性变更必须有版本、迁移或兼容策略。

## 7. 标准工作流

### Step 1：列出 V1 用户路径中的接口事件

从用户路径中提取事件，例如：注册、登录、创建项目、提交订单、上传文件、查看列表、更新状态、导出数据。

### Step 2：识别资源与边界

把事件归到资源：`users`、`projects`、`orders`、`files`、`memberships` 等。每个资源必须说明：

- 业务职责；
- 谁可以访问；
- 是否对外暴露；
- 是否需要审计；
- 是否有状态流转；
- 与数据库对象的关系。

### Step 3：定义接口清单

每个接口至少定义：

- 方法与路径；
- 认证要求；
- 请求参数、请求体、文件上传规则；
- 成功响应；
- 失败响应；
- 幂等与并发规则；
- 权限检查点；
- 关联数据库对象；
- 前端页面/组件使用方；
- 测试样例。

### Step 4：统一响应与错误模型

必须给出统一结构，例如：

```json
{
  "data": {},
  "requestId": "req_xxx"
}
```

失败响应必须包含稳定的机器可读错误码、用户可读提示、requestId，以及可选字段级错误。

### Step 5：定义 Mock 与契约测试

明确：

- 前端何时使用 Mock；
- Mock 数据放在哪里；
- Mock 与 OpenAPI / 类型定义如何同步；
- 哪些接口需要契约测试；
- 前后端联调前必须满足哪些条件。

### Step 6：形成联调计划

按垂直切片列出联调顺序：先健康检查和认证，再核心闭环，再异常场景，再边界和权限。

## 8. 输出模板

```md
# API 契约真源文档

## 1. 契约版本

- 版本：v1
- 状态：draft / reviewed / frozen / changed
- 最近变更：

## 2. 全局约定

- Base URL：
- 认证方式：
- requestId / traceId：
- 时间格式：
- 金额格式：
- 枚举命名：
- 分页：
- 错误结构：

## 3. 资源模型

| 资源 | 业务职责 | 数据来源 | 对外暴露 | 权限 | 状态 |
|---|---|---|---|---|---|

## 4. 接口清单

| 方法 | 路径 | 页面/调用方 | 权限 | 数据对象 | 状态 |
|---|---|---|---|---|---|

## 5. 详细接口

### <METHOD> <PATH>

- 业务目的：
- 调用方：
- 认证：
- 权限：
- 请求参数：
- 请求体：
- 成功响应：
- 失败响应：
- 幂等/并发：
- 数据库读写：
- 审计日志：
- 测试样例：

## 6. Mock 与契约测试

## 7. 联调顺序

## 8. 风险与待确认
```

## 9. 阶段完成门禁

- [ ] V1 核心用户路径涉及的接口事件已列出。
- [ ] 每个接口都能追溯到产品场景、页面需求和数据模型。
- [ ] 成功响应、失败响应、状态码、业务错误码统一。
- [ ] 认证、权限、敏感字段、审计和幂等规则明确。
- [ ] OpenAPI / 接口文档 / Mock 策略可供前后端共同使用。
- [ ] 前后端对契约状态达成一致：draft、reviewed、frozen 或 changed。

## 10. 推荐落盘位置

- 阶段真源文档：`<project-root>/docs/`
- 阶段决策记录：`<project-root>/docs/decisions/`
- 阶段检查清单：`<project-root>/docs/checklists/`
- 面向 Agent 的长期约束：`<project-root>/AGENTS.md` 或 `<project-root>/docs/agent-rules/`
