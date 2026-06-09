---
name: project-rescue-map
description: "Evidence-driven rescue diagnosis for already-started projects that skipped the work-bench 00-10 workflow. Use when a repo is messy, product scope is unclear, data/API/frontend/backend/docs/tests/security are inconsistent, or the user needs a risk-ranked rescue roadmap before repair work."
---

# 已开工项目补救诊断 Skill v2

## 0. 一句话

本 skill 把“已经写乱、没有按 00-10 工作流初始化的项目”从**凭感觉修**改成**证据驱动救援**：先稳住风险，再找真源缺口，再决定回到哪些 work-bench 阶段补救，最后输出可交接、可验收、可追踪的补救路线图。

它不是修代码 skill，而是一个 **项目救援地图 / Project Rescue Map**：回答“现在还能不能继续？先补哪几个阶段？哪些东西会炸？哪些证据证明它能继续？”

---

## 1. 在完整 work-bench 工作流中的位置

- 阶段编号：`rescue`
- 阶段名称：已开工项目补救诊断 / Project Rescue Mapping
- 总控入口：[`build-map`](../00-build-map/SKILL.md)
- 适用对象：已经存在代码、文档、配置或半成品交付物，但没有按 [`01-idea-check`](../01-idea-check/SKILL.md) 到 [`10-final-check`](../10-final-check/SKILL.md) 完成阶段真源的项目。
- 核心目标：识别产品、技术、数据、API、前端、后端、计划、文档、质量、安全、交付之间的缺口和冲突，输出**阶段级补救路线图**。

---

## 1.1 双轨视图：管理层与执行层

本 skill 使用双轨视图输出诊断：

- **管理层五大类**：帮助用户先看懂项目主要乱在哪些大块，适合摘要、排序和决策。
- **执行层 00-10**：保留现有 work-bench 精细阶段，负责指向真正要调用的补救 skill。

五大类不是新的 skill 名称，也不替代 00-10。任何补救动作最终都必须落回现有执行层 skill。

| 管理大类 | 映射执行阶段 | 诊断目的 |
|---|---|---|
| 范围 | `01-idea-check` | 产品目标、V1 边界、用户路径、验收标准是否清楚 |
| 架构 | `02-tool-pick`、`03-data-map`、`04-talk-link` | 技术栈、数据模型、API 契约和集成边界是否一致 |
| 骨架 | `05-skeleton-check`、`06-web-frame`、`07-server-frame` | 前后端骨架、目录责任、运行基线是否可靠 |
| 交付 | `08-work-plan`、`09-doc-rules` | 垂直切片、README、AGENTS、docs index、CI 是否支撑继续开发 |
| 验收 | `10-final-check` | 测试、构建、发布、回滚、安全和证据包是否足够 |

---

## 2. 何时启用

当用户表达以下任一意图时，启用本 skill：

- “`project-rescue-map <项目地址>`”。
- “这个项目已经写了一半，但感觉很乱，帮我诊断。”
- “接手一个老项目 / AI 写乱的项目 / 外包交付物，先看看还能不能继续。”
- “前端、后端、数据库、接口文档对不上。”
- “没有 PRD、没有数据库设计、没有 API 契约，但已经有代码了。”
- “想补齐 work-bench 流程，但项目不是从 0 开始。”
- “先给补救路线，不要马上改代码。”
- “判断项目是继续、冻结、重做一部分，还是建议停止投入。”

不要用本 skill 处理以下请求：

- 用户明确要求直接实现功能、修 bug、重构目录、创建 migration、安装依赖、上线发布。
- 项目尚未开工且没有代码，此时应回到 [`idea-check`](../01-idea-check/SKILL.md)。
- 已经完成 01-09，只是需要发布前验收，此时应调用 [`final-check`](../10-final-check/SKILL.md)。

---

## 3. 诊断深度模式

根据输入和项目风险选择模式。用户没有指定时，默认使用 `Standard Rescue Audit`。

| 模式 | 适用场景 | 输出深度 | 是否运行命令 |
|---|---|---|---|
| `Fast Triage` | 用户只想先知道项目是否危险、能不能继续 | 关键证据、红旗、最短补救链路 | 默认只做只读文件扫描 |
| `Standard Rescue Audit` | 常规已开工项目补救 | 完整阶段矩阵、风险登记、冲突漂移、补救路线图 | 默认只读扫描；可记录无法运行项 |
| `Deep Rescue Map` | 大型项目、多个子系统、生产风险、交付压力高 | 子系统拆分、风险评分、证据账本、救援状态板、handoff packet | 只有明确授权才运行非只读命令 |
| `Release Continuation Decision` | 判断是否继续开发、冻结、返工或终止投入 | 继续/条件继续/冻结/终止候选结论 | 需要更高证据标准 |

关键信息不足时，最多先问 **1 个会改变诊断路径的关键问题**。如果不能问或用户要求直接处理，则明确假设并继续。

---

## 4. 最高优先级原则

1. **先判断阶段和适用性，再止血、诊断、补救。** 如果发现真实数据损坏、安全泄露、生产不可恢复、密钥暴露、付费/权限错误等高危证据，先标记 `STOP / CONTAIN`。如果项目尚未进入相关能力阶段，把风险标为 `未来门禁` 或 `暂不适用`，不要误报为生产事故。
2. **只相信证据，不相信感觉。** 文件存在不等于阶段通过；README 写了不等于代码实现；测试脚本存在不等于测试通过。
3. **文档与代码冲突时，以可验证事实为准。** 同时记录“应回到哪个 skill 修正文档或代码真源”。
4. **不把诊断变成修复。** 默认不改业务代码、不写 migration、不安装/升级/删除依赖、不重构目录、不生成 PR 任务池。
5. **不伪造运行结果。** 没有执行的命令必须标注“未执行”；执行失败必须记录失败；截图、日志、接口响应、测试结果不得脑补。
6. **先缩小爆炸半径。** 对大型项目先按子系统、用户路径、部署单元、数据域或团队边界拆分，再逐个诊断。
7. **补救路线必须回到已有 work-bench skill。** 本 skill 只负责地图；后续修复必须交给 `idea-check`、`data-map`、`talk-link` 等对应阶段。
8. **风险豁免必须显式化。** 任何“先带着风险继续”的建议都必须写清影响、期限、负责人、复查条件和触发回滚/冻结的条件。

---

## 5. 工作边界

### 5.1 默认允许

- 读取项目文档、配置、代码、测试、CI、脚本和目录结构。
- 做静态证据扫描、阶段矩阵、风险评分、冲突分析。
- 在聊天中输出摘要报告。
- 默认把完整诊断文档写入目标项目的 `docs/rescue/runs/<run-id>/`。
- 更新目标项目的 `docs/rescue/index.md`，追加本次诊断索引。

### 5.2 默认禁止

- 修改业务代码、移动目录、创建/修改 migration、删除文件。
- 安装、升级、删除依赖。
- 执行会改变环境、数据库、远端服务、生产数据或 git 状态的命令。
- 为了“验证”而调用真实支付、短信、邮件、生产第三方接口。
- 自动修复安全问题但不说明影响。
- 把“缺证据”包装成“通过”。

### 5.3 命令授权与记录

只读扫描命令默认允许，但必须写入 `command-evidence-log`：

- `git status --short`
- `find` / `tree` / `ls`
- `cat` / `sed` / `grep` / `rg`
- 本地只读数据库 schema 检查

用户明确授权后，才可以运行可能生成产物、启动服务、改变缓存或触达外部依赖的验证命令：

- `npm run lint`、`npm test`、`pnpm build` 等可能生成缓存或构建产物的命令
- 本地容器启动、健康检查、mock 接口调用

任何命令都要记录：命令、工作目录、是否授权、结果、证据位置、是否改变文件、无法执行原因。

---

## 6. 证据协议：Evidence First

### 6.1 证据等级

报告中的每个关键判断都要标记证据等级：

| 等级 | 名称 | 含义 | 可用于通过阶段吗 |
|---|---|---|---|
| `E0` | 无证据 | 没有文件、代码、命令或用户确认 | 不可 |
| `E1` | 口头/聊天证据 | 用户描述或团队说法，但未落盘 | 只能作为假设 |
| `E2` | 文档证据 | README、PRD、ADR、接口文档、设计文档 | 需要和代码一致 |
| `E3` | 静态代码证据 | 路由、schema、DTO、配置、测试文件、CI 文件 | 可支持“部分具备” |
| `E4` | 可执行证据 | 测试、构建、类型检查、迁移 dry-run、contract test 实际结果 | 可支持“通过” |
| `E5` | 运行/生产证据 | 真实环境日志、监控、发布记录、事故复盘、用户验收 | 可支持高置信通过 |

### 6.2 证据引用格式

所有重要判断都要带路径或证据标识：

- `path/to/file:line`：静态文件证据。
- `command:<cmd>`：命令证据。
- `doc:<title>#section`：文档证据。
- `user-confirmed:<date>`：用户明确确认。
- `not-found:<scan-scope>`：扫描范围内未发现。

### 6.3 判断置信度

每个阶段建议标注 `confidence`：

- `High`：有 E4/E5，且文档与代码一致。
- `Medium`：有 E2/E3，缺运行验证或关键细节。
- `Low`：主要来自 E1 或合理推导。
- `Unknown`：证据不足，不能判断。

### 6.4 反脑补规则

- 不能因为项目叫 `backend` 就假定有 API 契约。
- 不能因为有 `schema.prisma` 就假定有迁移计划。
- 不能因为有 `openapi.yaml` 就假定前后端一致。
- 不能因为有 `.github/workflows` 就假定 CI 有效。
- 不能因为测试目录存在就写“测试通过”。
- 不能因为 `README` 有运行命令就假定命令可运行。

---

## 7. 安全止血门：STOP / CONTAIN / CONTINUE

在普通阶段诊断前，先做项目阶段识别和风险适用性判定，再检查是否触发止血门。

### 7.1 项目阶段

先判断项目当前最接近哪个阶段：

| 阶段 | 定义 | 安全门强度 |
|---|---|---|
| `prototype` | 本地原型、demo、还没有真实用户/共享数据 | 只阻止真实密钥、误连生产、破坏性命令 |
| `mvp-dev` | MVP 开发中，开始形成数据/API/权限边界 | 检查未来门禁和关键真源，不因尚未实现的能力误报 STOP |
| `staging` | 准备演示、内测、交付验收或共享环境联调 | 提高数据、权限、回滚、测试和第三方服务门槛 |
| `production` | 已有真实用户、真实数据、真实支付/消息/第三方调用 | 启用完整 STOP / CONTAIN 门禁 |
| `handoff` | 外包交付、团队接手或准备移交 | 按 `staging` 以上标准检查文档、证据、风险豁免 |
| `unknown` | 证据不足，无法判断阶段 | 不直接假定生产，但必须标注不可验证并提出首要确认问题 |

### 7.2 风险适用性

每个高危项必须先标注适用性：

| 适用性 | 含义 | 处理 |
|---|---|---|
| `适用` | 当前项目已有对应能力、数据、环境或代码证据 | 可参与 STOP / CONTAIN 判断 |
| `暂不适用` | 当前阶段还没有该能力，也没有真实环境证据 | 不升级为阻塞 |
| `未来门禁` | 当前不适用，但进入 staging/production 或实现该 V1 能力前必须补齐 | 记录为观察项或可后补 |
| `不可验证` | 无法判断是否适用，例如生产数据/第三方环境不清楚 | 记录缺证原因，必要时作为 CONTAIN |

### 7.3 止血决策

| 决策 | 触发条件 | 处理方式 |
|---|---|---|
| `STOP` | 有证据表明适用风险已触达真实数据、真实密钥、生产环境、真实资金/权限/隐私、不可逆共享 migration | 暂停普通开发，输出阻塞风险和隔离建议 |
| `CONTAIN` | 风险适用性不可验证，或存在共享环境/内测/交付风险但尚可隔离 | 允许有限诊断，禁止扩大变更 |
| `CONTINUE` | 没有发现高危止血信号 | 进入完整阶段诊断 |

止血门不是最终结论，只决定诊断是否需要先加安全护栏。

### 7.4 原型期降噪规则

- 项目没有真实用户、真实数据、真实密钥、真实第三方服务或共享数据库证据时，不得因为“缺少支付/权限/隐私设计”直接判 `STOP`。
- V1 scope 未包含支付、权限、隐私、生产部署时，相关缺口标为 `未来门禁`，并写清进入该能力前必须回到的 skill。
- 发现 `.env` 文件、支付字段、admin 路由、migration、生产 URL、真实第三方 SDK 配置时，必须重新评估适用性，不能继续按原型期降噪处理。
- `unknown` 不等于安全。若是否有生产数据/真实密钥无法判断，标为 `不可验证`，通常给 `CONTAIN` 而不是 `STOP`。

---

## 8. 诊断维度

除了 01-10 阶段矩阵，还要做横向维度检查，避免只看文档清单。

| 维度 | 关键问题 |
|---|---|
| 产品与范围 | V1 是什么？用户路径是否闭环？Won't-have 是否被偷偷实现？验收标准是否可检查？ |
| 利益相关方与决策 | 谁能拍板？哪些决策未记录？是否存在多套互相冲突的目标？ |
| 技术栈与依赖 | 实际栈是否唯一？包管理器是否混用？新增依赖是否有理由？禁用技术是否被引入？ |
| 架构与边界 | 模块责任是否清楚？有没有跨层调用、循环依赖、重复框架、架构漂移？ |
| 数据与迁移 | 业务对象、关系、生命周期、敏感字段、migration、回滚/前滚是否有真源？ |
| API 与契约 | 请求/响应/错误码/鉴权/分页/DTO/mock/API client 是否一致？ |
| 前端 | 路由、页面、组件、样式 token、状态、API client、错误处理是否收敛？ |
| 后端 | 配置、日志、错误处理、鉴权、权限、健康检查、数据访问是否可验收？ |
| 测试与质量 | lint/typecheck/test/build/contract/e2e 是否存在、真实、可运行？ |
| 安全与供应链 | secrets、依赖、锁文件、权限、输入校验、审计、CI 权限、构建来源是否可控？ |
| 交付与运维 | 启动、部署、回滚、备份、监控、事故复盘、发布记录是否存在？ |
| 文档与 Agent 规则 | README、docs index、AGENTS、CI、实际代码是否一致？ |

---

## 9. 对照基线：work-bench 01-10 阶段矩阵

| 阶段 | Skill | 诊断重点 | 最低可接受证据 |
|---|---|---|---|
| 01 | [`idea-check`](../01-idea-check/SKILL.md) | 产品定义、V1 边界、用户路径、核心对象、验收标准 | V1 scope、用户路径、验收标准，且代码没有明显跑偏 |
| 02 | [`tool-pick`](../02-tool-pick/SKILL.md) | 技术栈、依赖规则、禁用技术、重评条件 | 技术决策文档 + 实际依赖/脚本一致 |
| 03 | [`data-map`](../03-data-map/SKILL.md) | 业务对象、关系、表设计、迁移计划、敏感字段 | schema/model/migration + 数据设计真源 |
| 04 | [`talk-link`](../04-talk-link/SKILL.md) | API 契约、DTO、错误码、鉴权、分页、Mock、契约测试 | OpenAPI/契约文档 + 前后端调用一致证据 |
| 05 | [`skeleton-check`](../05-skeleton-check/SKILL.md) | 前后端骨架来源、delivery target、reuse/create 决策 | 骨架选择记录 + 真实目录/入口一致 |
| 06 | [`web-frame`](../06-web-frame/SKILL.md) | 前端目录、路由、组件、Token、API Client、质量门禁 | 前端蓝图 + 代码结构/API client/质量脚本一致 |
| 07 | [`server-frame`](../07-server-frame/SKILL.md) | 后端路由、错误、日志、配置、数据访问、安全基线 | 后端蓝图 + 启动/健康/错误/配置证据 |
| 08 | [`work-plan`](../08-work-plan/SKILL.md) | 垂直切片、任务边界、DoD、变更控制 | MVP slice plan + DoD + 当前任务状态 |
| 09 | [`doc-rules`](../09-doc-rules/SKILL.md) | README、docs index、AGENTS、CI 与真实项目一致 | 文档索引 + 规则 + CI 命令与代码一致 |
| 10 | [`final-check`](../10-final-check/SKILL.md) | 范围、架构、测试、安全、回滚、证据包 | 验收报告、证据包、回归/回滚计划 |

---

## 10. 阶段状态定义

每个阶段必须给一个状态：

| 状态 | 定义 | 典型后果 |
|---|---|---|
| `通过` | 有真实证据，内容足够支撑下游，文档与代码一致 | 可继续依赖该阶段 |
| `部分具备` | 有一些材料，但缺关键字段、门禁、命令或一致性 | 进入补救链路 |
| `缺失` | 没有可用真源或只有空壳 | 必须回到对应 skill |
| `冲突` | 文档、代码、配置、运行命令互相矛盾 | 优先解决冲突，再继续开发 |
| `过时` | 曾经存在真源，但已被代码或决策漂移超过 | 需要刷新文档和规则 |
| `不可验证` | 当前权限/环境/证据不足，不能判定 | 记录缺证原因和复查条件 |
| `不适用` | 当前项目形态确实不需要该阶段内容 | 说明原因，不能滥用 |

### 10.1 五大类状态聚合规则

- 任一映射阶段存在适用的 `STOP` 风险时，该管理大类不得标为 `通过`。
- 映射阶段之间存在文档、代码、配置、schema、API 或命令冲突时，优先标为 `冲突`。
- 没有可用真源时标为 `缺失`。
- 有部分证据但缺关键门禁或运行验证时标为 `部分具备`。
- 权限、环境或证据不足导致不能判断时标为 `不可验证`。
- 只有映射阶段证据充分且无关键冲突时，才可标为 `通过`。
- 原型期或 MVP 早期尚未开发到的能力，在适用性字段继续使用 `暂不适用` 或 `未来门禁`；阶段状态仍使用 `不适用`，不得仅因未实现支付、权限、隐私或生产发布能力判为 `STOP`。

---

## 11. 风险分级与决策

### 11.1 风险等级

| 等级 | 名称 | 判断标准 |
|---|---|---|
| `阻塞` | Blocker | 不补会导致方向错误、数据损坏、安全事故、无法验收、无法继续协作 |
| `必须补` | Must Fix | 短期可继续观察，但进入主要开发/发布前必须补齐 |
| `可后补` | Later | 不影响当前补救顺序，但会增加维护成本 |
| `观察项` | Watch | 证据不足或影响较小，需要复查 |

### 11.2 风险评分

如需更细分，用 1-5 分记录以下字段：

- `Impact`：影响范围。
- `Likelihood`：发生概率。
- `Reversibility`：是否可逆，越不可逆分越高。
- `Evidence Gap`：缺证程度。
- `Blast Radius`：影响模块/用户/数据范围。

建议公式：

`Risk Score = Impact + Likelihood + Reversibility + Evidence Gap + Blast Radius`

推荐映射：

- `21-25`：阻塞，建议 `STOP` 或先隔离。
- `16-20`：必须补，进入补救主线。
- `10-15`：可后补，但必须登记。
- `<10`：观察项。

### 11.3 总体结论

报告必须给出一个总体结论：

- `可继续`：没有阻塞项，关键阶段有足够证据。
- `条件可继续`：有必须补项，但有安全边界和补救顺序。
- `冻结普通开发`：存在阻塞项，应先止血/补真源。
- `建议重开关键阶段`：某些阶段缺口太大，局部重做更经济。
- `终止/暂停投入候选`：目标、技术、数据、安全或交付证据显示继续投入风险过高；需要业务负责人决策。

---

## 12. 标准诊断流程

### Step 0：确认目标项目根目录

明确 `<project-root>`。标准调用形式是：

```text
project-rescue-map <项目地址>
```

用户给路径则以路径为准；没有给路径则使用当前工作目录，并在报告中标注该假设。路径必须解析为目标项目根目录，不要把 work-bench 的 skill 目录当成被诊断项目。

### Step 0.5：创建本轮诊断编号和输出目录

每次诊断都必须生成唯一 `run-id`，避免同一个项目多次诊断互相覆盖。

推荐格式：

```text
YYYYMMDD-HHMMSS-<mode-or-short-label>
```

示例：

```text
20260610-143012-standard
20260610-151855-fast-triage
20260610-163400-release-decision
```

默认输出目录：

```text
<project-root>/docs/rescue/runs/<run-id>/
```

同时维护索引文件：

```text
<project-root>/docs/rescue/index.md
```

索引只追加本轮摘要和链接，不覆盖历史 run。若用户明确要求只聊天不落盘，仍要在聊天报告中标注“未落盘：用户要求只输出聊天报告”。

### Step 1：读取指令层级与项目入口

按优先级读取：

1. 最近的 `AGENTS.md`、`AGENTS.override.md`、`Claude.md`、`.codex/config.toml`。
2. `README.md`、`docs/README.md`、`docs/index.md`。
3. `docs/`、`PROJECT_STATE`、`TASK_LOG`、`PLANS.md`、ADR、PRD、设计文档。
4. `package.json`、`pyproject.toml`、`Cargo.toml`、`go.mod`、`Makefile`、CI workflow。

如果目标项目规则与本 skill 冲突，优先遵守目标项目规则，但不能违反本 skill 的安全边界和反伪造规则。

### Step 2：建立证据账本

为每条关键证据记录：路径、类型、阶段、结论、证据等级、置信度、备注。

优先读取目标项目中的真实证据，而不是按目录名猜测：

- 产品证据：PRD、范围文档、用户流程、验收标准。
- 技术证据：依赖、框架、包管理器、部署目标、测试工具。
- 数据证据：schema、migration、ORM model、seed、数据访问层。
- API 证据：OpenAPI、路由、controller、DTO、API client、mock、错误结构。
- 前端证据：路由、页面、组件、样式、状态、接口调用。
- 后端证据：入口、配置、日志、错误、鉴权、权限、健康检查。
- 交付证据：任务计划、PR 边界、CI、测试、发布、回滚、监控、事故。

### Step 3：跑阶段感知安全止血门

先判断项目阶段，再判断每个高危项的适用性，最后给出 `STOP` / `CONTAIN` / `CONTINUE`。若有 `STOP` 或 `CONTAIN`，报告必须把止血动作排在普通补救路线前。若风险属于 `未来门禁`，写入风险登记和补救路线，但不得伪装成当前阻塞。

### Step 4：生成阶段缺口矩阵

按 01-10 输出阶段状态、证据、缺口、风险等级、建议回到哪个 skill。

### Step 5：做冲突与漂移分析

至少检查以下冲突：

- README 运行命令 vs package/Makefile/CI。
- 技术选型文档 vs 实际依赖。
- 数据设计文档 vs schema/migration/model。
- API 文档 vs 后端路由 vs 前端 API client。
- 页面/用户路径 vs V1 范围。
- AGENTS/规则 vs 实际目录和脚本。
- CI 命令 vs 本地真实命令。
- 环境变量文档 vs 代码读取的 env。

### Step 6：识别补救主线

只给阶段级路线图，不展开完整任务池。路线图应满足：

- 先补会影响大量下游的真源，如 `01 -> 03 -> 04`。
- 先处理不可逆风险，如 migration、安全、权限、支付、删除、密钥。
- 先固定接口和数据，再让前后端继续写。
- 文档漂移严重时，把 `09-doc-rules` 放到补救链路中。
- 发布或交付前必须回到 `10-final-check`。

### Step 7：落盘完整报告并输出聊天摘要

默认写入本轮 run 目录：

- `project-rescue-report.md`
- `rescue-stateboard.md`
- `evidence-ledger.md`
- `risk-register.md`
- `conflict-drift-log.md`
- `command-evidence-log.md`
- `handoff-packet.md`

可选写入：

- `rescue-intake.md`
- `stage-gap-matrix.md`
- `subsystem-split-map.md`

然后在聊天中输出摘要，必须包含：

- 本轮 `run-id`。
- 完整报告目录。
- 总体结论。
- 止血门结论。
- 前 3 个最高风险。
- 推荐补救主线。
- 下一步应该调用的 skill。

每次运行都必须更新 `docs/rescue/index.md`，追加：

- run-id。
- 时间。
- 诊断模式。
- 项目阶段。
- 总体结论。
- 止血门结论。
- 报告目录链接。
- 下一步 skill。

---

## 13. 标准输出格式

聊天报告使用摘要结构。文件版完整报告使用 `templates/03_project_rescue_report.md`，写入本轮 run 目录。

### 13.1 聊天摘要格式

```md
# Project Rescue Summary

- 项目根目录：
- Run ID：
- 报告目录：
- 诊断模式：
- 项目阶段：prototype / mvp-dev / staging / production / handoff / unknown
- 止血门：STOP / CONTAIN / CONTINUE
- 总体结论：
- 推荐补救主线：
- 下一步 skill：

## 最高风险

1.
2.
3.

## 已落盘文件

- `docs/rescue/runs/<run-id>/project-rescue-report.md`
- `docs/rescue/runs/<run-id>/rescue-stateboard.md`
- `docs/rescue/runs/<run-id>/evidence-ledger.md`
- `docs/rescue/runs/<run-id>/risk-register.md`
- `docs/rescue/runs/<run-id>/conflict-drift-log.md`
- `docs/rescue/runs/<run-id>/command-evidence-log.md`
- `docs/rescue/runs/<run-id>/handoff-packet.md`
- `docs/rescue/index.md`
```

### 13.2 完整报告格式

主报告必须按以下顺序组织：

1. 项目阶段与止血门结论。
2. 五大类管理摘要。
3. 01-10 执行阶段缺口矩阵。
4. 风险登记与适用性。
5. 补救路线图。
6. 证据账本与命令记录。

```md
# Project Rescue Report

## 1. 项目阶段与止血门结论

- 项目根目录：
- Run ID：
- 报告目录：
- 诊断模式：Fast Triage / Standard Rescue Audit / Deep Rescue Map / Release Continuation Decision
- 项目阶段：prototype / mvp-dev / staging / production / handoff / unknown
- 诊断时间：
- 已读取证据：
- 未读取/不可读取证据：
- 已执行命令：
- 未执行命令与原因：
- 当前假设：
- 决策：STOP / CONTAIN / CONTINUE
- 阶段判定：
- 触发信号：
- 不适用/未来门禁：
- 立即禁止事项：
- 允许继续的诊断范围：

## 2. 五大类管理摘要

| 管理大类 | 映射阶段 | 大类状态 | 适用性 | 证据等级 | 置信度 | 关键发现 | 最高风险 | 第一补救动作 |
|---|---|---|---|---|---|---|---|---|
| 范围 | 01 idea-check |  |  |  |  |  |  |  |
| 架构 | 02 tool-pick / 03 data-map / 04 talk-link |  |  |  |  |  |  |  |
| 骨架 | 05 skeleton-check / 06 web-frame / 07 server-frame |  |  |  |  |  |  |  |
| 交付 | 08 work-plan / 09 doc-rules |  |  |  |  |  |  |  |
| 验收 | 10 final-check |  |  |  |  |  |  |  |

## 3. 01-10 执行阶段缺口矩阵

| 阶段 | Skill | 状态 | 适用性 | 证据等级 | 置信度 | 证据 | 缺口 | 风险等级 | 建议下一步 |
|---|---|---|---|---|---|---|---|---|---|

## 4. 风险登记与适用性

### 总体结论

- 当前状态：可继续 / 条件可继续 / 冻结普通开发 / 建议重开关键阶段 / 终止或暂停投入候选
- 主要阻塞：
- 推荐补救主线：
- 最高优先级下一步：

### 横向健康扫描

| 维度 | 状态 | 关键证据 | 主要问题 | 风险 | 建议 |
|---|---|---|---|---|---|

### 冲突与漂移

| 类型 | 位置 | 冲突内容 | 影响 | 建议回到的 skill |
|---|---|---|---|---|

### 风险分级

#### 阻塞

#### 必须补

#### 可后补

#### 观察项

### 风险豁免

| 豁免项 | 理由 | 到期条件 | 负责人 | 复查信号 |
|---|---|---|---|---|

## 5. 补救路线图

| 顺序 | 管理大类 | 回到阶段 | 调用 skill | 目标产出 | 通过门槛 | 依赖/前置 |
|---|---|---|---|---|---|---|

## 6. 证据账本与命令记录

### 证据账本

| 证据 | 类型 | 阶段 | 结论 | 证据等级 | 置信度 | 备注 |
|---|---|---|---|---|---|---|

### 命令记录

| 命令 | 工作目录 | 是否授权 | 结果 | 证据位置 | 是否改变文件 | 无法执行原因 |
|---|---|---|---|---|---|---|

## 7. 禁止事项

- 本轮不改业务代码。
- 本轮不创建 migration。
- 本轮不安装或升级依赖。
- 本轮不重构目录。

## 8. 下一步

- 推荐立即调用：
- 调用前必须准备：
- 需要用户/团队确认的 1 个关键问题：
```

---

## 14. 输出质量门禁

完成本 skill 前，必须满足：

- [ ] 目标项目根目录已明确，或已标注默认假设。
- [ ] 本轮 `run-id` 已生成，且输出目录为 `docs/rescue/runs/<run-id>/`。
- [ ] 项目入口文档和最近协作规则已读取或记录未找到。
- [ ] 已建立证据账本，关键判断都有证据等级。
- [ ] 已判断项目阶段和高危项适用性。
- [ ] 已检查阶段感知 `STOP / CONTAIN / CONTINUE` 止血门。
- [ ] 技术栈、数据、API、前端、后端、文档、质量、安全、交付证据已扫描。
- [ ] 01-10 阶段矩阵已完成。
- [ ] 每个 `缺失`、`部分具备`、`冲突`、`过时`、`不可验证` 阶段都有风险等级。
- [ ] 补救顺序只指向已有 skill，不自行执行修复。
- [ ] 报告明确列出未验证项和原因。
- [ ] 尚未开发到的能力已标为 `暂不适用` 或 `未来门禁`，没有误报为当前阻塞。
- [ ] 完整报告已落盘，或已记录用户要求只输出聊天报告。
- [ ] `docs/rescue/index.md` 已追加本轮诊断记录，或已记录无法写入原因。
- [ ] 不存在伪造命令结果、伪造测试通过、伪造接口响应。
- [ ] 如果建议继续开发，已写清继续的边界、前置补救和复查条件。

---

## 15. 推荐资料与模板

本 skill 附带可落盘模板、检查表、playbook、prompt 和参考映射：

- `templates/00_rescue_intake.md`：诊断输入表。
- `templates/01_evidence_ledger.md`：证据账本。
- `templates/02_stage_gap_matrix.md`：阶段缺口矩阵。
- `templates/03_project_rescue_report.md`：完整报告模板。
- `templates/04_rescue_stateboard.md`：救援状态板。
- `templates/05_conflict_drift_log.md`：冲突与漂移日志。
- `templates/06_risk_register.md`：风险登记表。
- `templates/07_command_evidence_log.md`：命令证据日志。
- `templates/08_stakeholder_interview_pack.md`：关键问题包。
- `templates/09_subsystem_split_map.md`：子系统拆分图。
- `templates/10_handoff_packet.md`：交接包。
- `templates/11_rescue_index.md`：多轮诊断索引。
- `checklists/`：反脑补、安全止血、仓库扫描、阶段门禁、安全供应链、数据/API 一致性、交付健康。
- `playbooks/`：快速分诊、完整审计、范围救援、数据/API 救援、前后端救援、安全供应链救援、继续/冻结决策。
- `references/`：证据模型、评分模型、异味目录、外部方法来源映射。
- `examples/`：示例报告和使用方式。

---

## 16. 与其他 skill 的关系

本 skill 只负责补救诊断。后续执行必须回到对应阶段 skill：

- 产品边界不清：调用 [`idea-check`](../01-idea-check/SKILL.md)。
- 技术栈混乱：调用 [`tool-pick`](../02-tool-pick/SKILL.md)。
- 数据模型缺失或危险：调用 [`data-map`](../03-data-map/SKILL.md)。
- 前后端接口不一致：调用 [`talk-link`](../04-talk-link/SKILL.md)。
- 骨架来源和落地路径不清：调用 [`skeleton-check`](../05-skeleton-check/SKILL.md)。
- 前端结构混乱：调用 [`web-frame`](../06-web-frame/SKILL.md)。
- 后端基线缺失：调用 [`server-frame`](../07-server-frame/SKILL.md)。
- 开发顺序混乱：调用 [`work-plan`](../08-work-plan/SKILL.md)。
- 文档和规则漂移：调用 [`doc-rules`](../09-doc-rules/SKILL.md)。
- 需要发布或交付门禁：调用 [`final-check`](../10-final-check/SKILL.md)。

---

## 17. 版本说明

v2.1 相比 v2 的主要增强：

- 新增项目阶段：`prototype`、`mvp-dev`、`staging`、`production`、`handoff`、`unknown`。
- 新增风险适用性：`适用`、`暂不适用`、`未来门禁`、`不可验证`。
- 安全止血门改为阶段感知，避免原型项目因尚未实现支付/权限/隐私能力而被误判为 `STOP`。
- 只有真实数据、真实密钥、生产环境、不可逆共享 migration、真实资金/权限/隐私证据才触发当前 `STOP`。

v2 相比 v1 的主要增强：

- 从“阶段清单”升级为“证据驱动救援系统”。
- 新增 `STOP / CONTAIN / CONTINUE` 止血门。
- 新增 E0-E5 证据等级和置信度规则。
- 新增横向健康维度、风险评分、冲突漂移、风险豁免。
- 新增 10 个模板、7 个检查表、7 个 playbook、4 个 prompt、4 个参考文件和示例报告。
- 明确与 DORA、NIST SSDF、OWASP SAMM、OpenAPI、C4、Twelve-Factor、OpenSSF Scorecard、SLSA、EBM、事故复盘等外部方法的映射。
