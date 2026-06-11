---
name: server-frame
description: "Build, audit, repair, and validate a backend skeleton with route rules, errors, logging, config, data access, and security baselines. Use when starting or hardening a backend base."
---

# 后端工程骨架与架构验收 Skill


## 1. 在完整开发工作流中的位置

- 阶段编号：`07`
- 阶段名称：后端骨架 / 业务裁判层基线冻结
- 总控入口：[`build-map`](../00-build-map/SKILL.md)
- 本阶段目标：建立可启动、可验证、可持续迭代的后端最小工程基线，防止后续业务实现绕过权限、错误、日志、配置和数据访问规则。

## 2. 何时启用

- 需要从 0 到 1 搭建后端骨架。
- 已有后端项目被 AI 写乱，需要审计、修复和架构收敛。
- 已经通过 `skeleton-check` 选定了后端候选骨架或 create 路径。
- 需要验收后端是否能长期维护，而不只是“接口能跑”。

## 3. 上游输入契约

本 skill 不应孤立执行。除非用户明确要求单独使用，否则应优先读取或生成以下输入：

- `<project-root>/docs/product/v1-mvp-scope.md` 与权限/异常边界。
- `<project-root>/docs/architecture/tech-stack-decision.md`。
- `<project-root>/docs/database/database-design.md` 与迁移计划。
- `<project-root>/docs/api/api-contract-source-of-truth.md`、错误码、认证策略和接口返回规范。
- `<project-root>/docs/product/bootstrap-targets.md` 与 `<project-root>/docs/skeleton/backend-selection.md`。
- 模式 B 审计已有后端时，优先生成或读取 [`reverse-dfd-analysis`](../reverse-dfd-analysis/SKILL.md) 产物：
  - `<project-root>/docs/backend/dfd/顶层图.md`
  - `<project-root>/docs/backend/dfd/0层图.md`
  - `<project-root>/docs/backend/dfd/证据表.md`

## 4. 下游输出契约

本 skill 必须把结果沉淀成可被后续 skill 直接消费的交付物：

- `<project-root>/docs/backend/backend-architecture-source-of-truth.md`：后端架构真源文档。
- `<project-root>/docs/backend/api-contract.md`：后端 API 约束与实现边界。
- `<project-root>/docs/backend/error-codes.md`：业务错误码与错误返回规范。
- `<project-root>/docs/backend/file-responsibility-map.md`：目录/文件责任表。
- `<project-root>/docs/backend/runbook.md`：启动、配置、数据库连接、日志、排障。
- `<project-root>/docs/backend/security-baseline.md`：认证、权限、输入校验、密钥与日志安全。
- `<project-root>/docs/backend/acceptance-report.md`：运行证据与验收报告。
- 模式 B 条件输出 `<project-root>/docs/backend/dfd/`：现有后端逻辑数据流图和证据表。

## 5. 与其他 skill 的引用关系

### 5.1 上游 skill

- [`idea-check`](../01-idea-check/SKILL.md)
- [`tool-pick`](../02-tool-pick/SKILL.md)
- [`data-map`](../03-data-map/SKILL.md)
- [`talk-link`](../04-talk-link/SKILL.md)
- [`skeleton-check`](../05-skeleton-check/SKILL.md)
- 条件上游：[`reverse-dfd-analysis`](../reverse-dfd-analysis/SKILL.md)，仅用于模式 B 的现有后端代码审计、修复和架构收敛。

### 5.2 下游 skill

- [`work-plan`](../08-work-plan/SKILL.md)
- [`doc-rules`](../09-doc-rules/SKILL.md)
- [`final-check`](../10-final-check/SKILL.md)

### 5.3 交接载荷

交给下游时，至少携带以下信息：

- 后端架构真源文档。
- API 实现边界、错误码、日志/追踪规则。
- 数据库连接和数据访问边界。
- 目录/文件责任表和框架复用清单。
- 模式 B 的 DFD 证据引用：系统边界、主要加工、数据存储、敏感数据流和代码证据索引。
- 运行证据、已知风险、待修复项。

## 6. 本阶段不可违反的硬规则

1. 骨架未验收前不得实现登录、支付、订单、文件上传等高风险业务。
2. 不能相信“已搞定”，只相信可复查的运行证据。
3. 不得伪造运行结果、命令输出、接口响应或测试结果。
4. 不得让 AI 自由发挥技术栈、目录、错误结构或权限边界。
5. 密钥不得硬编码；配置与密钥必须隔离。
6. 每个目录和关键文件必须有责任登记。
7. 框架原生能力优先，禁止为了炫技重复造框架。
8. 模式 B 审计已有后端时，不得跳过 DFD 证据门；模式 A 0→1 骨架搭建不强制生成 DFD。
9. DFD 是静态逻辑数据流证据，不替代启动、健康检查、接口响应、测试结果或运行证据包。

## 7. 阶段完成门禁

- [ ] 项目能按真实命令启动。
- [ ] 健康检查、配置加载、数据库连接验证、日志/requestId 或 traceId 可验证。
- [ ] API 成功/失败响应结构和错误码稳定。
- [ ] 目录和文件责任表完整。
- [ ] 安全基线覆盖认证、权限、输入校验、错误与日志安全。
- [ ] 运行证据包和后端真源文档已生成。

## 8. 工作模式补充

本 skill 在 backend delivery target 中工作，默认是 `<project-root>/backend`。它可以与前端骨架并行，但二者必须共同引用 `talk-link` 的接口真源。若后端发现数据模型不支持接口，应回到数据库 skill 修订。

## 9. 推荐落盘位置

- 阶段真源文档：`<project-root>/docs/`
- 阶段决策记录：`<project-root>/docs/decisions/`
- 阶段检查清单：`<project-root>/docs/checklists/`
- 面向 Agent 的长期约束：`<project-root>/AGENTS.md` 或 `<project-root>/docs/agent-rules/`

## 10. 继承自原 skill 的详细规则库

> 以下内容来自原始 skill，已作为新版 skill 的细节规则保留。若出现旧 skill 名称、旧版本号或旧目录名，以新版 front matter 的 `name` 与本文件第 1-7 节为准。

## 后端架构骨架搭建、审计、修复与验收 Skill

### 0. Skill 的定位

本 Skill 用于 Vibe Coding 场景下的后端工程控制。它不把后端当成“写几个接口”，而是把后端视为产品背后的**业务裁判层**：后端负责判断用户是谁、能不能做、该怎么做、数据如何变化、失败如何返回、日志如何追踪、密钥如何隔离、权限谁说了算。

如果 `skeleton-check` 选择 `create`，先把新候选骨架放进 `backend/apps` 并更新 `backend/README.md` 索引，再把它复制/落地到 backend delivery target。

本 Skill 有两个工作模式：

1. **模式 A：0→1 后端可运行骨架搭建**  
   从零建立一个可启动、可验证、可持续迭代的后端最小工程基线。该模式不直接开发登录、支付、订单等业务功能。

2. **模式 B：现有后端代码梳理、审计、修复**  
   对已有后端代码进行现状盘点、架构审计、目录责任重建、工程基线补齐、接口规范收敛、安全检查、运行验收和文档固化。

本 Skill 的核心产出不是“看起来能跑的代码”，而是：

- 明确的语言与框架选择；
- 不可随意更改的项目架构设计文档；
- 最小可运行后端骨架；
- 每个目录和每个关键文件的责任说明；
- 统一 API 契约；
- 统一错误处理与业务错误码；
- 配置与密钥隔离；
- 日志、requestId / traceId、错误兜底；
- 数据库连接验证；
- 权限校验占位；
- 框架原生能力复用清单；
- 可复查的运行证据包；
- 《后端架构实施真源文档》；
- Git 稳定基线建议。

一句话原则：

> 文档先行，框架约束，最小闭环，文件责任清晰，证据验收，业务后置。

---

### 1. 适用场景

当用户提出以下需求时，启用本 Skill：

- “帮我搭一个后端骨架”；
- “从 0 到 1 搭后端”；
- “先别写业务，帮我把后端架构定好”；
- “帮我整理 AI 写乱的后端”；
- “帮我审计现有后端代码”；
- “登录/支付/订单之前，先搭稳定后端”；
- “帮我写后端架构设计文档”；
- “帮我验收 AI 搭的后端骨架”；
- “帮我制定 API 规范、目录规范、错误处理、日志、权限规则”；
- “帮我检查后端是不是能长期维护”。

不适用场景：

- 只需要写一个一次性脚本，且不需要长期维护、权限、API、部署；
- 用户明确要求只解释概念，不需要生成工程规则或审计；
- 用户明确要求只做前端页面，不涉及后端。

---

### 2. 最高优先级硬规则

#### 2.1 骨架未验收前，不得直接写高风险业务

在后端骨架通过验收前，不得直接实现真实业务模块，包括但不限于：

- 登录注册；
- 支付；
- 退款；
- 订单；
- 管理后台；
- 文件上传；
- 第三方密钥调用；
- 用户数据导出；
- 权限复杂的业务审核流程。

骨架阶段只允许实现工程基础能力：

- 应用启动入口；
- 配置读取；
- `.env.example`；
- 路由分组；
- `/health` 健康检查；
- 数据库连接配置与验证；
- 统一响应结构；
- 全局错误处理；
- 统一日志入口；
- 请求日志；
- 错误日志；
- requestId / traceId；
- 参数校验机制示例；
- 权限校验占位；
- API 文档入口或 OpenAPI 约定；
- README / Runbook 启动说明；
- 架构真源文档；
- 骨架验收报告。

#### 2.2 不能相信“已搞定”，只相信证据

AI 不得只输出：

- “已完成”；
- “符合最佳实践”；
- “可以开发业务”；
- “理论上可运行”；
- “应该没问题”；
- “后面再测试”。

必须给出：

- 规则来源；
- 文件路径；
- 目录/文件职责；
- 验证命令；
- 实际返回；
- 日志示例；
- 执行结果；
- `通过 / 失败 / 未验证` 状态。

没有证据，就必须标记为：**未验收**。

#### 2.3 不得伪造运行结果

如果当前环境不能安装依赖、不能启动项目、不能访问数据库、不能执行 curl、不能运行测试，必须明确标记为：

```text
未验证：当前环境无法执行该命令。
```

不得把“理论可行”写成“通过”。

#### 2.4 不得让 AI 自由发挥技术栈

语言与框架必须先确认，并写入真源文档。选型必须说明：

- 为什么选这个语言；
- 为什么选这个框架；
- 为什么不选其他主流方案；
- 当前项目是否真的需要该复杂度；
- 是否符合团队/部署/维护条件；
- 框架官方能力能帮我们约束什么；
- 对 AI 生成稳定代码有什么帮助。

一旦选定，不得在后续无理由切换技术栈。

#### 2.5 密钥不得硬编码

以下内容不得写进源码，不得写进前端，不得提交到 Git：

- API Key；
- 数据库连接串；
- Token Secret；
- JWT Secret；
- OAuth Client Secret；
- 支付密钥；
- 对象存储密钥；
- 邮件服务密钥；
- 第三方服务密钥；
- 管理员初始密码。

必须使用环境变量、受控配置系统或部署平台的 secrets 管理能力。必须提供 `.env.example`，真实 `.env` 必须进入 `.gitignore`。

#### 2.6 每个目录和关键文件必须登记责任

后端骨架不是只输出树形目录。必须记录：

- 每个目录的职责；
- 每个目录应放什么；
- 每个目录禁止放什么；
- 每个目录是框架自带还是项目自定义；
- 新增模块时如何使用；
- 每个关键文件为什么存在；
- 每个关键文件允许依赖什么；
- 每个关键文件禁止依赖什么；
- 该文件如何验证。

如果不能解释“这个文件为什么存在”，就不要创建这个文件。

#### 2.7 框架能力优先复用，不为炫技封装

能用框架原生能力的地方，不要手写二次封装。

优先复用：

- 路由分组；
- 参数校验；
- 中间件 / Guards / Filters / Pipes / Interceptors；
- 依赖注入；
- ORM / migrations；
- HTTP 状态码机制；
- 全局异常处理；
- 配置管理；
- 日志设施；
- 健康检查；
- OpenAPI / Swagger 支持；
- 测试工具。

任何自定义封装都必须回答：

1. 解决什么具体问题？
2. 为什么框架原生能力不够？
3. 当前代码是否实际调用？
4. 去掉它会怎样？
5. 是否写入真源文档？

说不清的封装必须删除或暂缓。

---

### 3. 官方资料驱动的工程原则

使用本 Skill 时，应优先参考所选框架和标准的官方文档。不要凭“听说某框架更专业/更安全”做选型。以下资料用于指导 Skill 的内置规则：

涉及框架、库、CLI、版本行为、配置、路由、参数校验、错误处理、日志、健康检查、API 文档、测试或部署入口时，不得凭记忆写规则、命令或配置。应优先使用 Context7 查询当前官方文档，再创建、审计、修复或验收后端骨架。

标准流程：

```bash
npx ctx7@latest library <官方库名> "<当前后端骨架问题>"
npx ctx7@latest docs <library-id> "<当前后端骨架问题>"
```

适用对象包括但不限于 FastAPI、Django、Django REST Framework、NestJS、Express、Spring Boot、Laravel、Gin、Pydantic、OpenAPI 工具、配置/日志库和测试框架。框架原生能力仍然优先，但当能力、命令或配置随版本变化时，必须用当前官方资料支撑结论。

如果 Context7 不可用、限额不足、查不到对应库或结果不足以支撑决策，可以降级到以下官方或一手来源，并记录降级原因：

1. 官方文档站，包括 `/llms.txt` 或 `/llms-full.txt`。
2. 官方 GitHub 仓库的 README、docs、examples、release notes。
3. 厂商官方 MCP 文档源。
4. Firecrawl / WebSearch 等抓取或搜索工具，但只采用官方或一手来源。

查询时不得包含 API Key、Token、数据库连接串、私有内网地址、客户数据或任何带凭证的配置。当文档依据影响架构、命令、配置、安全基线或验收结论时，必须把依据摘要写入后端交付物，例如：

- `docs/backend/backend-architecture-source-of-truth.md`
- `docs/backend/runbook.md`
- `docs/backend/security-baseline.md`
- `docs/backend/acceptance-report.md`

| 方向 | 官方/权威资料 | 本 Skill 采用的规则 |
|---|---|---|
| HTTP 状态码 | RFC 9110 HTTP Semantics | HTTP 状态码表达请求结果语义，业务错误码不得替代 HTTP 状态码 |
| API 错误结构 | RFC 9457 Problem Details for HTTP APIs | 错误响应应机器可读、结构统一；RFC 9457 已取代 RFC 7807 |
| API 契约 | OpenAPI Specification | API 需要可被人和机器理解的 paths、operations、schemas、responses |
| 配置管理 | Twelve-Factor App Config | 配置与代码分离，环境差异通过环境变量或受控配置注入 |
| API 安全 | OWASP API Security Top 10 2023 | 后端必须防对象级越权、字段级越权、认证缺陷、安全配置错误、资源滥用 |
| FastAPI | FastAPI 官方文档 | 使用 APIRouter、Dependencies、Pydantic response_model、Settings、exception handlers |
| Django / DRF | Django 与 Django REST Framework 官方文档 | 使用项目/app结构、settings、models、migrations、serializers、viewsets、permissions、middleware |
| NestJS | NestJS 官方文档 | 使用 modules、controllers、providers/services、pipes、guards、filters、ConfigModule、Terminus health checks |
| Express | Express 官方文档 | 使用 Router、中间件、错误处理中间件，避免路由里堆业务 |
| Spring Boot | Spring Boot / Spring Framework 官方文档 | 使用 controller/service/repository、externalized configuration、Actuator health、ControllerAdvice、ExceptionHandler |
| Laravel | Laravel 官方文档 | 使用 routes、controllers、Form Request validation、middleware、resources、errors、env/config |
| Go Gin | Gin 官方文档与 Go 官方文档 | 使用 route groups、middleware、binding/validation、recovery、Go modules、cmd/internal 分层约束 |

执行中如果需要查最新版本、命令、框架行为，必须优先使用 Context7 查官方文档；若降级到其他官方或一手来源，必须说明原因和依据。

---

### 4. 技术选型协议

#### 4.1 先判断项目类型

必须先判断项目属于哪一类：

| 项目类型 | 后端复杂度 | 推荐倾向 |
|---|---:|---|
| 一次性脚本 / 文件处理 / 报表生成 | 低 | Python 脚本或轻量 CLI，通常不需要完整后端骨架 |
| 小型 API / AI 工具 / 数据服务 | 低-中 | FastAPI、Express/Fastify、Gin |
| SaaS / 后台管理 / CRUD 密集 | 中 | Django/DRF、Laravel、NestJS、Spring Boot |
| 权限复杂 / 多角色 / 审核流 | 中-高 | Django/DRF、NestJS、Spring Boot、Laravel |
| 企业系统 / 复杂事务 / 强一致性 | 高 | Spring Boot、NestJS、Django/DRF，视团队能力定 |
| 高性能单服务 / 云原生小服务 | 中-高 | Go + Gin/Echo/Fiber，需更强文档约束 |

#### 4.2 主流框架选择建议

##### Python + FastAPI

适合：

- API 服务；
- AI 工具；
- 数据处理接口；
- 中小型后端；
- 需要自动 OpenAPI 的项目。

必须补齐：

- 目录规范；
- 统一响应；
- 全局错误处理；
- 权限占位；
- 日志规范；
- 数据库迁移；
- 配置校验。

框架能力优先使用：

- `APIRouter` 做路由分组；
- `Depends` / `Security` 做依赖注入、认证占位；
- Pydantic models 做请求/响应校验；
- `response_model` 控制输出字段；
- `@app.exception_handler` 处理错误；
- Settings / environment variables 管理配置。

##### Python + Django / Django REST Framework

适合：

- 后台管理；
- CRUD 密集；
- 多角色权限；
- 用户系统；
- 内容/订单/运营平台；
- 非技术用户希望用成熟框架约束 AI。

框架能力优先使用：

- Django project / app 结构；
- settings；
- models；
- migrations；
- admin；
- middleware；
- DRF serializers；
- DRF views/viewsets/routers；
- authentication / permission classes。

注意：

- 不要在 view 里堆复杂业务；
- 不要绕过 serializer 做参数校验；
- 不要把配置硬编码进 settings；
- 生产环境必须处理 DEBUG、ALLOWED_HOSTS、SECRET_KEY 等安全配置。

##### Node.js + NestJS

适合：

- 中大型 API；
- 模块化后端；
- 团队协作；
- 需要强结构约束的 Vibe Coding 项目。

框架能力优先使用：

- module / controller / provider(service)；
- pipes 做参数校验；
- guards 做认证与权限；
- exception filters 做错误处理；
- interceptors 做响应/日志横切；
- ConfigModule 管理配置；
- Terminus 做 health check；
- Swagger module 做 API 文档。

注意：

- 不要把数据库操作写进 controller；
- 不要在 service 中直接拼 HTTP 响应；
- 不要绕开 DI 乱实例化依赖；
- 目录应按 module 边界组织。

##### Node.js + Express / Fastify

适合：

- 轻量 API；
- 小工具；
- 低复杂度服务。

必须补齐：

- 路由分层；
- validation 中间件；
- error-handling middleware；
- requestId；
- logger；
- config loader；
- auth placeholder；
- API 文档。

注意：

- Express 灵活但约束少，必须靠真源文档限制 AI；
- 错误处理中间件必须集中，不能每个路由自由返回。

##### Java + Spring Boot

适合：

- 企业系统；
- 复杂事务；
- 强类型后端；
- 权限、审计、流程较复杂的系统。

框架能力优先使用：

- `@RestController`；
- service 层；
- repository 层；
- externalized configuration；
- profiles；
- validation annotations；
- `@ControllerAdvice` / `@ExceptionHandler`；
- Actuator health endpoints；
- Spring Security 占位或基础配置。

注意：

- 对非技术用户复杂度较高；
- 代码生成必须严格按包结构和层级规则执行。

##### PHP + Laravel

适合：

- 后台系统；
- 传统 Web + API；
- CRUD；
- 快速产品验证；
- 中小团队。

框架能力优先使用：

- `routes/api.php`；
- controllers；
- middleware；
- Form Request validation；
- resources；
- migrations；
- policies/gates；
- exception handling；
- `.env` / config。

注意：

- 不要在 controller 里堆所有业务；
- 不要绕过 request validation；
- 不要直接暴露异常堆栈。

##### Go + Gin / Echo / Fiber

适合：

- 高性能 API；
- 部署简单的服务；
- 云原生单服务；
- 团队具备 Go 维护能力。

必须补齐：

- `cmd/` 启动入口；
- `internal/` 业务代码；
- router groups；
- middleware；
- binding/validation；
- config/env；
- recovery；
- logger；
- repository/service 分层；
- OpenAPI 生成策略。

注意：

- Go 项目结构容易变成“个人习惯”，必须明确目录责任；
- 不要为了 Clean Architecture 过度抽象。

#### 4.3 技术选型输出模板

```markdown
# 语言与框架选型说明

## 选择结果
- 语言：
- 框架：
- 数据库：
- ORM / 数据访问方案：
- API 文档方案：
- 部署方式：

## 项目需求匹配
- 项目类型：
- 用户角色：
- 核心业务对象：
- 复杂度等级：低/中/高

## 为什么选择该技术栈
- ...

## 为什么不选择其他方案
- FastAPI：适合/不适合，因为 ...
- Django/DRF：适合/不适合，因为 ...
- NestJS：适合/不适合，因为 ...
- Spring Boot：适合/不适合，因为 ...
- Laravel：适合/不适合，因为 ...
- Go Gin：适合/不适合，因为 ...

## 当前项目是否真的需要该复杂度
- ...

## 对 AI 协作的约束收益
- 目录约束：
- 参数校验：
- 权限占位：
- 错误处理：
- API 文档：
- 部署验证：
```

---

### 5. 通用后端骨架标准

无论选用哪个框架，后端骨架必须具备以下能力。

#### 5.1 启动线

必须有：

- 固定启动命令；
- 依赖安装命令；
- 监听端口说明；
- `.env.example`；
- 配置读取与必填项校验；
- `/health` 健康检查；
- README 或 Runbook。

验收证据必须包含：

- 安装命令输出；
- 启动命令输出；
- 监听端口日志；
- `curl /health` 返回。

#### 5.2 接口线

必须有：

- 路由分组；
- 版本前缀建议，如 `/api/v1`；
- 统一成功响应；
- 统一错误响应；
- requestId / traceId；
- HTTP 状态码规则；
- 业务错误码规则；
- 12 类响应样例；
- API 契约文档或 OpenAPI 入口。

#### 5.3 业务线

必须有清晰调用链：

```text
HTTP 请求
→ 路由 / Controller / Handler
→ 参数校验
→ 认证与权限占位
→ Service / Use Case / Business Logic
→ Repository / Model / Data Access
→ 统一响应
→ 日志与错误处理
```

禁止：

- 在路由里写复杂业务规则；
- 在 controller/handler 里直接写 SQL 或复杂 ORM 查询；
- 在 repository/model 里处理 HTTP 响应；
- 在 service 里读取零散环境变量；
- 把所有东西放进 `utils`；
- 每个接口自己定义一套错误返回。

#### 5.4 运维线

必须有：

- 请求日志；
- 错误日志；
- 全局错误兜底；
- 数据库连接验证；
- 健康检查；
- 配置加载失败时快速失败；
- 敏感信息脱敏；
- 启动说明；
- 最小验收命令。

---

### 6. API 规范

#### 6.1 API 契约必须先于业务实现

每个 API 在实现前必须定义：

| 字段 | 说明 |
|---|---|
| 业务目的 | 这个接口解决什么业务问题 |
| 方法与路径 | 如 `GET /api/v1/orders` |
| 调用角色 | 游客/普通用户/管理员等 |
| 认证要求 | 无需登录/需要登录/需要特定角色 |
| 请求参数 | path/query/body/header |
| 字段校验 | 必填、类型、范围、格式、长度 |
| 读取数据 | 读哪些表/模型/外部服务 |
| 修改数据 | 写哪些表/模型/外部服务 |
| 成功响应 | 对象/列表/空响应 |
| 失败响应 | 400/401/403/404/409/429/500 等 |
| 日志要求 | 是否记录操作人、对象、结果 |
| 幂等要求 | 支付/回调/删除/导出等高危操作必须说明 |
| 安全注意 | 是否涉及越权、敏感字段、频率限制 |

#### 6.2 成功响应：对象

```json
{
  "success": true,
  "data": {
    "id": "123",
    "name": "example"
  },
  "meta": {
    "requestId": "req_abc123",
    "timestamp": "2026-06-09T12:00:00Z"
  }
}
```

#### 6.3 成功响应：列表

```json
{
  "success": true,
  "data": {
    "items": [],
    "pagination": {
      "page": 1,
      "pageSize": 20,
      "total": 0,
      "totalPages": 0
    }
  },
  "meta": {
    "requestId": "req_abc123",
    "timestamp": "2026-06-09T12:00:00Z"
  }
}
```

#### 6.4 成功响应：删除或无内容

优先使用：

- `204 No Content`：无响应体；
- 或项目统一要求 `200`：返回统一 JSON。

二者只能选一种并写入真源文档，不得混用。

#### 6.5 失败响应

默认使用统一 envelope，并兼容 Problem Details 思路：

```json
{
  "success": false,
  "error": {
    "type": "https://example.com/problems/auth/unauthorized",
    "code": "AUTH_UNAUTHORIZED",
    "title": "Unauthorized",
    "status": 401,
    "message": "未登录或登录已过期",
    "details": null
  },
  "meta": {
    "requestId": "req_abc123",
    "timestamp": "2026-06-09T12:00:00Z"
  }
}
```

如果项目选择严格 `application/problem+json`，必须写入真源文档，并保持全项目一致。

#### 6.6 HTTP 状态码规则

| 场景 | 推荐 HTTP 状态码 | 说明 |
|---|---:|---|
| 获取成功 | 200 | GET 成功 |
| 创建成功 | 201 | POST 创建资源成功 |
| 更新成功 | 200 | PUT/PATCH 成功并返回对象 |
| 删除成功无返回 | 204 | DELETE 成功且无响应体 |
| 参数错误 | 400 或 422 | 默认 400；若框架默认 422，需统一记录，不得混用 |
| 未登录/Token 无效 | 401 | 身份认证失败 |
| 无权限 | 403 | 已认证但无权操作 |
| 资源不存在 | 404 | 资源不存在或对当前用户不可见 |
| 资源冲突 | 409 | 状态冲突、重复提交、幂等冲突 |
| 请求过于频繁 | 429 | 频率限制 |
| 系统异常 | 500 | 未预期服务端错误 |
| 上游服务异常 | 502/503/504 | 第三方服务、网关、超时等 |

#### 6.7 业务错误码规则

业务错误码格式：

```text
领域_错误原因
```

示例：

- `AUTH_UNAUTHORIZED`
- `AUTH_FORBIDDEN`
- `USER_NOT_FOUND`
- `USER_PHONE_INVALID`
- `ORDER_STATUS_INVALID`
- `ORDER_NOT_OWNER`
- `PAYMENT_DUPLICATED`
- `PAYMENT_CALLBACK_INVALID`
- `VALIDATION_ERROR`
- `RATE_LIMITED`
- `INTERNAL_ERROR`

要求：

- 错误码必须集中维护；
- 新增错误码必须登记在 `<project-root>/docs/backend/error-codes.md` 或等价真源文档；
- 不得在业务文件里随手新增魔法字符串；
- 错误 message 可面向用户，code 必须稳定面向程序。

---

### 7. 目录责任表与文件责任表

#### 7.1 目录责任表模板

```markdown
# 目录责任表

| 路径 | 主要职责 | 应放内容 | 禁止内容 | 来源 | 新增模块规则 |
|---|---|---|---|---|---|
| src/routes 或等价目录 | HTTP 路由入口 | 路由声明、URL 分组、调用 controller/handler | 禁止复杂业务、禁止直接 SQL、禁止读取密钥 | 框架习惯/项目约定 | 新增模块只登记路由，不写业务 |
| src/controllers 或等价目录 | 请求入口控制 | 解析请求、调用 service、返回统一响应 | 禁止数据库 CRUD、禁止堆业务规则 | 框架习惯/项目约定 | 每个模块一个 controller |
| src/services 或等价目录 | 业务规则执行 | 业务判断、流程编排、事务边界 | 禁止拼 HTTP 响应、禁止直接读 .env | 项目约定 | 复杂业务必须放这里 |
| src/repositories 或等价目录 | 数据访问 | ORM 查询、CRUD、数据持久化 | 禁止处理 HTTP、禁止判断用户角色 | 项目约定 | 每个聚合/模型一个 repository |
| src/models 或 src/entities | 数据模型 | ORM 实体、数据库模型定义 | 禁止业务流程、禁止 HTTP 响应 | 框架/ORM 约定 | 修改字段需同步迁移 |
| src/schemas 或 dto | 请求/响应结构 | DTO、Pydantic schema、serializer、validation schema | 禁止业务执行、禁止数据库查询 | 框架习惯 | 所有 API 入参出参先定义 schema |
| src/middlewares / guards | 横切逻辑 | 认证、权限、日志、requestId、rate limit | 禁止具体业务流程 | 框架能力 | 只放跨模块通用逻辑 |
| src/errors | 错误体系 | 错误类、错误码映射、异常转换 | 禁止业务流程 | 项目约定 | 新错误码先登记文档 |
| src/config | 配置读取 | env 解析、配置校验、默认值 | 禁止真实密钥、禁止业务逻辑 | 项目约定 | 新增 env 必须更新 .env.example |
| src/db | 数据库基础设施 | 连接、迁移入口、seed、health check | 禁止 HTTP 和业务流程 | 项目约定 | 新增数据源先记录 |
| src/logger | 日志基础设施 | logger 初始化、格式、脱敏 | 禁止业务判断 | 项目约定 | 业务只调用，不自建 logger |
| docs | 真源文档 | 架构、API、错误码、运行、验收 | 禁止过期规则 | 项目约定 | 规则变化必须同步更新 |
| tests | 测试与验证 | 单元/集成/契约测试 | 禁止生产代码 | 框架习惯 | 新模块需补最小测试 |
```

具体路径必须服从所选框架官方习惯。如果框架没有对应概念，必须说明替代机制。

#### 7.2 文件责任表模板

每个骨架创建或改动的关键文件都必须登记：

```markdown
# 文件责任表

| 文件路径 | 文件职责 | 为什么需要它 | 允许依赖 | 禁止依赖 | 验证方式 | 状态 |
|---|---|---|---|---|---|---|
| src/main.* | 应用启动入口 | 初始化应用、注册路由/中间件/错误处理 | config、logger、router | 具体业务 service、数据库查询细节 | 启动命令成功 | 通过/失败/未验证 |
| src/config/* | 配置加载与校验 | 防止硬编码和缺失配置 | env loader、schema validator | controller、service 业务 | 缺失必填 env 时快速失败 | 通过/失败/未验证 |
| src/health/* | 健康检查 | 验证服务和基础依赖是否可用 | db health、logger | 业务模块 | curl /health | 通过/失败/未验证 |
```

文件责任原则：

- 一个文件只承担一个主要职责；
- 文件命名必须体现职责；
- 不允许出现“万能文件”“大杂烩 utils”；
- 如果一个文件超过合理范围，应考虑拆分；
- 移动文件必须更新 import 并运行验证；
- 删除文件必须说明没有被引用。

---

### 8. 模式 A：0→1 后端可运行骨架搭建

#### A1. 项目边界确认

先输出：

```markdown
# 项目边界确认

## 已知信息
- ...

## 合理假设
- ...

## 待确认事项
- ...

## 本阶段明确不做
- 真实登录
- 真实支付
- 真实订单
- 真实退款
- 真实文件上传
- 真实第三方密钥调用
```

如果用户没有回答，不得停滞，应做保守假设，并把风险写清楚。

#### A2. 技术选型复核

使用第 4 节模板输出《语言与框架选型说明》。如果用户已经指定框架，则默认尊重用户选择，但仍需复核复杂度和风险。

#### A3. 生成《项目架构设计文档》

写代码前必须先生成文档。文档至少包含：

1. 项目目标与业务边界；
2. 语言、框架、版本、数据库、部署方式；
3. 技术选型理由；
4. 官方框架能力复用清单；
5. 目录结构草案；
6. 目录责任表；
7. 文件责任登记规则；
8. 请求处理链路；
9. API 响应规范；
10. HTTP 状态码规范；
11. 业务错误码规范；
12. 参数校验规范；
13. 认证与权限占位规范；
14. 数据库访问规范；
15. 事务与幂等占位规范；
16. 日志规范；
17. 配置与密钥管理规范；
18. API 文档 / OpenAPI 规范；
19. 新增业务模块规则；
20. 禁止事项；
21. 骨架验收标准。

必须包含声明：

```markdown
后续所有后端开发必须以本文档为唯一权威源。任何目录调整、规则修改、框架更换、关键依赖新增、接口响应格式调整，都必须先说明原因，并同步更新本文档。
```

#### A4. 搭建最小骨架

骨架必须只包含基础工程能力：

- 应用启动入口；
- 配置管理；
- `.env.example`；
- `.gitignore` 敏感文件排除；
- 路由注册；
- `/health`；
- 数据库连接配置；
- 数据库连接验证；
- 统一响应 helper / interceptor / serializer；
- 全局错误处理；
- 错误码集中定义；
- 日志入口；
- 请求日志；
- 错误日志；
- requestId / traceId；
- 参数校验机制示例；
- 权限校验占位；
- API 文档入口或 OpenAPI 说明；
- README / Runbook；
- `<project-root>/docs/backend/backend-architecture-source-of-truth.md`；
- `<project-root>/docs/backend/file-responsibility-map.md`；
- `<project-root>/docs/backend/api-contract.md`；
- `<project-root>/docs/backend/error-codes.md`；
- `<project-root>/docs/backend/acceptance-report.md`。

禁止骨架阶段实现真实业务逻辑。

#### A5. 生成目录树与责任登记

输出：

```markdown
# 实际目录树

```text
...
```

# 目录责任表
...

# 文件责任表
...
```

注意：目录树必须和真实文件一致，不得画一个不存在的目录结构。

#### A6. 定义 API 契约与 OpenAPI 策略

必须输出：

- API 基础路径，如 `/api/v1`；
- `/health` 契约；
- 示例接口契约，用于验证统一响应，不代表真实业务；
- OpenAPI 生成或维护方式；
- 成功/失败响应结构；
- 12 类响应样例。

#### A7. 最小端到端演练

不写真实业务，只做一个非业务演练模块，例如：

- `GET /health`；
- `GET /api/v1/_example/ping`；
- `POST /api/v1/_example/validate`，用于触发参数校验；
- `GET /api/v1/_example/error`，用于触发错误处理。

该演练必须证明链路可用：

```text
HTTP 请求
→ 路由
→ 参数校验
→ 权限占位
→ service 或等价层
→ repository 或 mock data access 占位
→ 统一响应
→ 错误处理
→ 日志
```

如果没有数据库，也必须明确：

```text
数据库连接未启用：当前项目边界暂不需要数据库，已保留连接配置位置和验证规则。
```

#### A8. 运行证据包

必须实际执行并记录：

```markdown
# 运行证据包

| 验收项 | 命令/路径 | 实际结果 | 状态 |
|---|---|---|---|
| 依赖安装 | ... | ... | 通过/失败/未验证 |
| 项目启动 | ... | ... | 通过/失败/未验证 |
| 健康检查 | curl .../health | ... | 通过/失败/未验证 |
| 配置读取 | ... | ... | 通过/失败/未验证 |
| 数据库连接 | ... | ... | 通过/失败/未验证 |
| 成功请求 | curl ... | ... | 通过/失败/未验证 |
| 参数错误 | curl ... | ... | 通过/失败/未验证 |
| 未登录/无权限占位 | curl ... | ... | 通过/失败/未验证 |
| 系统异常 | curl ... | ... | 通过/失败/未验证 |
| 请求日志 | ... | ... | 通过/失败/未验证 |
| 错误日志 | ... | ... | 通过/失败/未验证 |
```

#### A9. 生成后端架构实施真源文档

验收通过后，生成或更新：

```text
<project-root>/docs/backend/backend-architecture-source-of-truth.md
```

该文档是后续业务开发唯一权威源。

#### A10. Git 固化基线

验收通过后建议执行：

```bash
git add .
git commit -m "chore: backend architecture v1.0 — first stable baseline"
git tag backend-architecture-v1.0
```

如果存在未验证项，只能提交为：

```bash
git commit -m "chore: backend architecture baseline — verification pending"
```

并在文档中列出未验证项。

---

### 9. 模式 B：现有后端代码梳理、审计、修复

#### B0. DFD 证据门

模式 B 面对已有后端代码，必须先调用或引用 [`reverse-dfd-analysis`](../reverse-dfd-analysis/SKILL.md)，建立路由、Controller/Handler、Service、Repository/Data Access、数据存储和外部实体之间的逻辑数据流。

推荐输出：

- `<project-root>/docs/backend/dfd/顶层图.md`
- `<project-root>/docs/backend/dfd/0层图.md`
- `<project-root>/docs/backend/dfd/证据表.md`

执行约束：

- 不得跳过 `reverse-dfd-analysis` 的目标层级门禁；缺少顶层图或父加工时，必须先补前置 DFD 或标注证据缺口。
- 使用 DFD 检查路由是否承载复杂业务、Service 是否绕过权限、Repository 是否处理 HTTP 或角色判断、Controller 是否直接 SQL。
- 使用 DFD 检查敏感数据流是否经过输入校验、认证/授权、错误处理和日志脱敏边界。
- DFD 可辅助生成目录/文件责任表和安全基线，但不能替代运行证据、健康检查、API 响应或测试结果。
- 模式 A “0→1 后端可运行骨架搭建”不强制生成 DFD；只有用户明确要求或已有代码需要反推时才使用。

#### B1. 现状盘点

先读取或检查项目文件，输出《现有后端现状报告》。必须包含：

- 语言；
- 框架；
- 依赖文件；
- 启动命令；
- 监听端口；
- 目录结构；
- 路由位置；
- 业务逻辑位置；
- 数据库访问位置；
- 配置文件位置；
- 是否存在 `.env.example`；
- 是否可能提交真实 `.env`；
- 是否有统一响应；
- 是否有全局错误处理；
- 是否有日志；
- 是否有 requestId；
- 是否有数据库连接验证；
- 是否有权限校验；
- 是否有 README / Runbook；
- 是否有 API 文档；
- 是否有测试；
- Git 当前状态。
- DFD 证据路径或未生成原因。

模板：

```markdown
# 现有后端现状报告

| 项目 | 当前发现 | 文件/证据 | 风险 |
|---|---|---|---|
| 语言 | ... | ... | 低/中/高 |
| 框架 | ... | ... | 低/中/高 |
| 启动命令 | ... | ... | 低/中/高 |
| 目录结构 | ... | ... | 低/中/高 |
| 配置管理 | ... | ... | 低/中/高 |
| 统一响应 | ... | ... | 低/中/高 |
| 错误处理 | ... | ... | 低/中/高 |
| 日志 | ... | ... | 低/中/高 |
| 数据库连接 | ... | ... | 低/中/高 |
| 权限校验 | ... | ... | 低/中/高 |
| DFD 证据 | ... | ... | 低/中/高 |
```

#### B2. 架构问题审计

每个问题必须有证据。

```markdown
# 后端架构审计报告

| 等级 | 问题 | 证据路径 | 具体表现 | 影响范围 | 修复建议 | 是否阻塞业务 |
|---|---|---|---|---|---|---|
| Blocker | ... | ... | ... | ... | ... | 是/否 |
```

等级定义：

| 等级 | 含义 | 示例 |
|---|---|---|
| Blocker | 阻塞继续写业务 | 无法启动、无配置隔离、密钥硬编码、无路由入口、无法连接 DB |
| High | 高风险，需优先修 | 无鉴权、接口越权风险、无统一错误处理、数据库访问散落 |
| Medium | 中风险，应近期修 | 目录边界不清、日志不完整、响应格式不统一 |
| Low | 可排期优化 | README 不完整、命名不统一、少量未用封装 |

架构问题审计应引用 DFD 证据来说明跨层调用、数据访问越界、敏感数据流绕过校验、错误处理或日志脱敏缺口。没有 DFD 支撑的推断必须标为未验证。

#### B3. 目录责任重建

必须输出：

```markdown
# 目录责任重建表

| 当前路径 | 当前用途 | 问题 | 处理方式 | 调整后职责 | 是否移动文件 | 验证方式 |
|---|---|---|---|---|---|---|
| ... | ... | ... | 保留/调整/合并/拆分/删除 | ... | 是/否 | ... |
```

修复原则：

- 优先遵守当前框架官方结构；
- 不为了“看起来专业”而新增多余目录；
- 不一口气重写全部业务；
- 移动文件必须更新 import；
- 移动后必须启动验证；
- 保留兼容策略，避免突然破坏前端。

#### B4. 安全基线检查

必须检查：

- 硬编码密钥；
- `.env` 是否被提交；
- `.gitignore` 是否排除敏感文件；
- 生产配置是否泄露 DEBUG / stack trace；
- 管理接口是否有后端鉴权；
- 用户是否可能访问他人数据；
- 字段级权限是否缺失；
- 输入是否只在前端校验；
- 高危操作是否有日志；
- 删除/支付/回调是否有幂等或二次确认；
- 错误响应是否泄露数据库、路径、堆栈、密钥；
- CORS、rate limit、upload size、body size 是否有合理限制。

模板：

```markdown
# 安全基线检查

| 检查项 | 当前状态 | 证据路径 | 风险 | 修复建议 |
|---|---|---|---|---|
| 密钥硬编码 | 是/否/未发现 | ... | 高 | ... |
| .env 提交 | 是/否/未发现 | ... | 高 | ... |
| 管理接口鉴权 | 有/无/不完整 | ... | 高 | ... |
| 对象级越权 | 有风险/未发现/未验证 | ... | 高 | ... |
| 字段级越权 | 有风险/未发现/未验证 | ... | 高 | ... |
```

#### B5. 渐进修复计划

不得盲目大改。必须按阶段修复：

```markdown
# 渐进修复计划

## Phase 1：阻塞项修复
- ...

## Phase 2：启动、配置、健康检查、日志基线
- ...

## Phase 3：统一响应、错误处理、错误码
- ...

## Phase 4：目录责任重建与文件移动
- ...

## Phase 5：权限占位、安全基线、数据库连接验证
- ...

## Phase 6：真源文档与验收固化
- ...
```

每个修复项必须包含：

- 修改文件；
- 修改原因；
- 风险；
- 验证命令；
- 预期结果；
- 回滚方式。

#### B6. 执行修复

修复时应优先补齐工程基线，而不是先改业务语义：

- `.env.example`；
- 配置读取与校验；
- `/health`；
- 统一响应；
- 全局错误处理；
- 日志入口；
- 请求日志；
- 错误日志；
- 数据库连接验证；
- 权限校验占位；
- 参数校验机制；
- README / Runbook；
- API 样例；
- 真源文档。

如果必须修改业务行为，必须单独标注并说明影响。

#### B7. 兼容策略

如果现有前端已经依赖旧 API 格式，不得直接破坏。

必须选择一种：

1. 保留旧接口，新增 `/api/v2`；
2. 增加适配层，内部统一、外部兼容；
3. 分阶段迁移，列出旧格式下线时间；
4. 经用户确认后统一破坏性迁移。

未经说明不得直接改掉响应格式。

#### B8. 修复执行记录

每完成一组修复，输出：

```markdown
# 修复执行记录

| 修复项 | 修改文件 | 验证命令 | 实际结果 | 状态 |
|---|---|---|---|---|
| ... | ... | ... | ... | 通过/失败/未验证 |
```

#### B9. 更新真源文档

修复完成后，必须把真实现状写入：

- 当前语言和框架；
- 当前启动方式；
- 当前目录职责；
- 当前文件责任表；
- 当前 API 规范；
- 当前错误处理；
- 当前日志方式；
- 当前配置方式；
- 当前数据库连接方式；
- 当前权限校验策略；
- 后续新增模块规则；
- 禁止 AI 绕过文档自由发挥。

#### B10. Git 固化修复基线

修复和验收通过后建议：

```bash
git add .
git commit -m "chore: backend architecture audit and repair baseline"
git tag backend-architecture-repaired-v1.0
```

存在未验证项时，只能提交为：

```bash
git commit -m "chore: backend architecture partial repair — verification pending"
```

---

### 10. 八步架构验收规则

无论模式 A 还是模式 B，最终都必须执行八步验收。

#### 第一步：验收规则，而不是验收功能

输出：

```markdown
# 规则验收报告

| 规则 | 来源 | 文件路径 | 验证命令/日志 | 实际结果 | 状态 |
|---|---|---|---|---|---|
| 统一响应格式 | <project-root>/docs/backend/api-contract.md | src/common/response.* | curl ... | 返回符合规范 | 通过 |
```

不合格情况：

- 无证据；
- 无文件路径；
- 无命令或日志；
- 只有“最佳实践”；
- 解释晦涩；
- 规则写在聊天里但没落到文档。

#### 第二步：验收目录与文件责任

必须输出：

- 目录责任表；
- 文件责任表；
- 新增模块放置规则；
- 禁止依赖规则。

必须解释：

1. 为什么接口入口不能堆业务判断；
2. 为什么数据库访问不能散落在 Controller/路由里；
3. 为什么配置不能硬编码；
4. 为什么错误码不能到处自由新增；
5. 为什么真实业务必须等骨架验收后再写。

#### 第三步：用最小模块演练规则落地性

演练链路：

```text
HTTP 请求
→ 路由/Controller/Handler
→ 参数校验
→ 权限占位
→ Service / Use Case
→ Repository / Data Access 占位
→ 统一成功响应
→ 统一错误处理
→ 请求日志/错误日志
```

必须输出：

- 新增/修改哪些文件；
- 各放哪个目录；
- 每个文件职责；
- 完整调用路径图；
- 实际请求命令；
- 实际返回。

一票否决：

- 每次推演文件位置不一致；
- “全在一个接口里搞定”；
- 业务逻辑、数据库访问、响应拼装混在一个文件；
- 错误处理散落在每个接口。

#### 第四步：接口返回必须见真例

必须输出 12 类真实 HTTP 场景响应：

1. 列表成功；
2. 空列表；
3. 详情成功；
4. 创建成功；
5. 更新成功；
6. 删除成功；
7. 参数错误；
8. 未登录；
9. 无权限；
10. 资源不存在；
11. 业务规则失败；
12. 系统异常。

每个样例必须包含：

- 请求方法；
- 请求路径；
- HTTP 状态码；
- JSON 结构；
- 处理文件或中间件；
- 是否已实际请求验证。

#### 第五步：验收框架能力最大化复用

输出：

```markdown
# 框架能力复用清单

| 能力 | 使用方式 | 框架原生/项目自定义 | 文件路径 | 为什么需要自定义 | 是否实际调用 |
|---|---|---|---|---|---|
| 路由分组 | ... | 框架原生 | ... | 不适用 | 是 |
| 参数校验 | ... | 框架原生 | ... | 不适用 | 是 |
| 错误处理 | ... | 项目自定义 | ... | 统一错误响应结构 | 是 |
```

红灯信号：

- 为显得专业而提前封装；
- 未被实际调用；
- 说不清解决什么问题；
- 框架已有能力却重复造轮子；
- 未写入真源文档。

#### 第六步：验收启动、配置、数据库、日志四大运行基线

必须交付运行证据包：

1. 依赖安装命令及输出；
2. 启动命令及监听端口；
3. 健康检查 URL 及返回；
4. 配置文件路径和 `.env.example`；
5. 数据库连接验证命令和结果；
6. 请求日志示例；
7. 错误日志示例；
8. 至少一个成功请求；
9. 至少一个错误请求；
10. 如果有测试，测试命令和结果。

只说“理论可行”不通过。

#### 第七步：收口成《后端架构实施真源文档》

该文档不是问答汇总，而是可执行规则手册。必须包含：

- 语言/框架/版本；
- 启动命令；
- 环境变量说明；
- 目录责任地图；
- 文件责任地图；
- 请求处理链路；
- API 响应规范；
- HTTP 状态码规范；
- 业务错误码规范；
- 参数校验规则；
- 认证与权限占位；
- 数据库连接规则；
- 日志规则；
- 框架能力复用清单；
- 新增模块规则；
- 禁止事项；
- 验收证据包；
- 未验证项；
- 后续变更规则。

Agent 宪法只引用该文档，不把所有技术细节塞进去：

```markdown
后端开发必须遵守《后端架构实施真源文档》。任何偏离必须先说明原因，并同步更新该文档。
```

#### 第八步：Git 提交稳定基线

验收通过后：

```bash
git add .
git commit -m "chore: backend architecture v1.0 — first stable baseline"
git tag backend-architecture-v1.0
```

未验证项不得标记“基本完成”。

---

### 11. 安全基线要求

#### 11.1 认证与权限

骨架阶段不实现真实登录，但必须预留统一入口：

- auth middleware / guard / dependency / permission class；
- 当前用户上下文；
- 角色检查占位；
- 对象级权限检查占位；
- 字段级权限检查占位；
- 管理接口保护占位。

后续真实业务必须遵守：

- 前端隐藏按钮不是权限；
- 后端必须校验每个敏感操作；
- 用户访问对象 ID 时必须做对象级授权；
- 返回对象字段时必须做字段级过滤；
- 管理接口必须后端鉴权；
- 导出、删除、支付、回调必须记录日志。

#### 11.2 输入校验

所有外部输入必须在后端校验：

- path params；
- query params；
- body；
- headers；
- file metadata；
- webhook payload。

校验必须覆盖：

- 必填；
- 类型；
- 长度；
- 格式；
- 枚举；
- 数值范围；
- 金额正数；
- 分页上限；
- 文件大小与类型；
- 字段白名单，防止 mass assignment。

#### 11.3 错误与日志安全

错误响应不得暴露：

- stack trace；
- 数据库连接串；
- SQL；
- 服务器绝对路径；
- 密钥；
- 第三方 token；
- 内部服务地址；
- 用户敏感信息。

日志必须：

- 带 requestId / traceId；
- 记录时间、方法、路径、状态码、耗时；
- 高危操作记录操作者、对象、结果；
- 对敏感字段脱敏；
- 错误日志记录异常类型和可排查信息；
- 不把密码、token、密钥写入日志。

#### 11.4 高危操作占位

骨架阶段必须在文档中声明：

- 支付回调必须幂等；
- 删除必须确认权限和日志；
- 导出必须限制权限和记录审计；
- 文件上传必须限制大小、类型、存储路径；
- 第三方 API 调用密钥只能在后端；
- 用户数据读取必须避免越权。

---

### 12. 数据库与数据访问规则

#### 12.1 数据库连接

如果项目需要数据库，骨架必须具备：

- 连接配置；
- 连接池或 ORM 初始化；
- 迁移方案；
- health check 中的连接验证或单独验证命令；
- `.env.example` 中的数据库变量；
- 本地开发数据库说明。

如果暂不需要数据库，必须明确标记：

```text
当前骨架未启用数据库。已保留数据库接入规则，后续接入前必须更新真源文档并补齐连接验证。
```

#### 12.2 数据访问边界

禁止：

- controller/route 直接写 SQL；
- controller/route 直接拼复杂 ORM 查询；
- service 随意跨多个 repository 操作且无事务说明；
- repository 判断 HTTP 状态码；
- repository 判断用户角色；
- 把数据库字段直接原样暴露给 API。

必须：

- 数据访问集中在 repository/model/data-access 层；
- DTO/schema/serializer 控制 API 输出字段；
- 敏感字段默认不返回；
- 写操作说明事务边界；
- 高危写操作说明幂等策略。

---

### 13. 输出状态词规范

只能使用以下状态词：

| 状态 | 含义 |
|---|---|
| 通过 | 已实际执行并有证据 |
| 失败 | 已执行但结果不符合预期 |
| 未验证 | 当前环境或信息不足，未能执行验证 |
| 不适用 | 当前项目边界明确不需要该项 |
| 待确认 | 需要用户或项目上下文确认 |

禁止使用：

- 基本完成；
- 应该可以；
- 差不多；
- 理论上没问题；
- 后续再测；
- 最佳实践所以没问题。

---

### 14. 最终交付物清单

#### 模式 A：0→1 骨架搭建

至少交付：

- 《项目边界确认》；
- 《语言与框架选型说明》；
- 《项目架构设计文档》；
- 最小可运行后端骨架；
- `.env.example`；
- `.gitignore`；
- `/health`；
- 统一响应与错误处理；
- 错误码集中定义；
- 日志入口；
- requestId / traceId；
- 数据库连接验证或明确不适用；
- 权限校验占位；
- API 文档入口或 OpenAPI 策略；
- 目录责任表；
- 文件责任表；
- 12 类 HTTP 响应样例；
- 运行证据包；
- 《后端架构实施真源文档》；
- Git 稳定基线建议。

#### 模式 B：现有代码梳理修复

至少交付：

- 《现有后端现状报告》；
- 《后端架构审计报告》；
- 《目录责任重建表》；
- 《文件责任重建表》；
- 《安全基线检查》；
- 《渐进修复计划》；
- 修复后的工程基线；
- 修复执行记录；
- 接口规范统一结果；
- 运行证据包；
- 更新后的《后端架构实施真源文档》；
- Git 修复基线建议。

---

### 15. 推荐用户启动语

#### 15.1 从 0→1 搭建

```text
请启用 backend-architecture-builder-auditor Skill，使用模式 A：0→1 后端可运行骨架搭建。
我的项目是：[项目说明]。
请先输出项目边界、技术选型说明和项目架构设计文档，不要直接写登录、支付、订单等业务功能。
```

#### 15.2 审计和修复现有代码

```text
请启用 backend-architecture-builder-auditor Skill，使用模式 B：现有后端代码梳理、审计、修复。
请先审计当前后端代码，输出现状报告、架构问题清单、目录/文件责任重建表、安全基线检查和渐进修复计划。
不要直接大规模重写，先给证据和修复顺序。
```

#### 15.3 验收 AI 已搭建的后端

```text
请启用 backend-architecture-builder-auditor Skill，对当前后端骨架做完整八步验收。
不要只听“已完成”，必须输出规则来源、文件路径、验证命令、实际返回、日志示例和通过/失败/未验证状态。
```

---

### 16. 最终判断标准

后端骨架只有同时满足以下条件，才能标记为“通过”：

- 语言和框架已确认，并写明理由；
- 架构文档已生成；
- 目录责任边界清晰；
- 文件责任表完整；
- 项目能启动；
- `/health` 能返回；
- 配置不硬编码；
- `.env.example` 存在；
- `.gitignore` 排除真实 `.env`；
- 数据库连接已验证，或明确标记不适用/未验证；
- 统一响应格式存在且有真实样例；
- 全局错误处理存在且有真实样例；
- HTTP 状态码规则已写入文档；
- 业务错误码规则已写入文档；
- 请求日志和错误日志有样例；
- requestId / traceId 存在；
- 权限校验有统一占位；
- 参数校验机制存在；
- 框架原生能力已最大化复用；
- 自定义封装有明确理由且实际调用；
- 12 类 HTTP 响应样例完整；
- 运行证据包完整；
- 真源文档已收口；
- Git 基线提交建议已给出。

若任一关键项缺失，必须标记为“失败”或“未验证”，不得说“基本完成”。

---

### 17. 参考资料链接

执行本 Skill 时优先使用官方资料。以下链接用于后续查证和更新：

- FastAPI Bigger Applications: https://fastapi.tiangolo.com/tutorial/bigger-applications/
- FastAPI Settings and Environment Variables: https://fastapi.tiangolo.com/advanced/settings/
- FastAPI Handling Errors: https://fastapi.tiangolo.com/tutorial/handling-errors/
- FastAPI Response Model: https://fastapi.tiangolo.com/tutorial/response-model/
- Django Documentation: https://docs.djangoproject.com/
- Django Deployment Checklist: https://docs.djangoproject.com/en/stable/howto/deployment/checklist/
- Django REST Framework ViewSets: https://www.django-rest-framework.org/api-guide/viewsets/
- NestJS Documentation: https://docs.nestjs.com/
- NestJS Guards: https://docs.nestjs.com/guards
- NestJS Pipes: https://docs.nestjs.com/pipes
- NestJS Exception Filters: https://docs.nestjs.com/exception-filters
- NestJS Configuration: https://docs.nestjs.com/techniques/configuration
- NestJS Health Checks / Terminus: https://docs.nestjs.com/recipes/terminus
- Express Error Handling: https://expressjs.com/en/guide/error-handling/
- Spring Boot Actuator Endpoints: https://docs.spring.io/spring-boot/reference/actuator/endpoints.html
- Spring Framework Exception Handling: https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-exceptionhandler.html
- Laravel Middleware: https://laravel.com/docs/middleware
- Laravel Validation: https://laravel.com/docs/validation
- Laravel Error Handling: https://laravel.com/docs/errors
- Gin Documentation: https://gin-gonic.com/en/docs/
- Gin Grouping Routes: https://gin-gonic.com/en/docs/routing/grouping-routes/
- Go Modules / How to Write Go Code: https://go.dev/doc/code
- OpenAPI Specification: https://swagger.io/specification/
- RFC 9110 HTTP Semantics: https://www.rfc-editor.org/info/rfc9110
- RFC 9457 Problem Details for HTTP APIs: https://www.rfc-editor.org/info/rfc9457
- OWASP API Security Top 10 2023: https://owasp.org/API-Security/editions/2023/en/0x11-t10/
- Twelve-Factor App Config: https://12factor.net/config
