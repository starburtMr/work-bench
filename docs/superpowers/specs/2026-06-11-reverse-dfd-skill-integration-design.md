# reverse-dfd-analysis 条件接入设计

## 目标

把 `reverse-dfd-analysis` 接入 `project-rescue-map`、`data-map`、`server-frame`，作为已有代码场景下的数据流证据前置能力。

本设计采用“条件强制”策略：当目标项目已经有代码、旧项目需要救援、AI 写乱、文档与代码不一致，或需要从代码反推真实数据流时，相关 skill 必须先调用或引用 `reverse-dfd-analysis` 的产物。新项目从 0 到 1 初始化时不强制生成 DFD。

## 背景

`reverse-dfd-analysis` 能从路由、控制器、服务、实体、Repository、SQL、事件处理和页面组件中抽象出 DFD 的外部实体、加工、数据存储和数据流，并同步输出代码证据索引。

它适合补足三个现有阶段的共同缺口：

- `project-rescue-map` 需要在混乱项目中建立跨产品、数据、API、后端的证据地图。
- `data-map` 需要从真实业务流程和读写证据中反推业务对象、关系、生命周期和查询路径。
- `server-frame` 在审计已有后端时，需要判断路由、服务、数据访问、安全边界是否与真实数据流一致。

## 设计选择

采用方案：**条件强制，作为证据前置**。

触发条件：

- 项目已有可读代码，且用户要求诊断、救援、审计、修复、整理或反推设计。
- 代码、文档、数据库设计、API 契约、前后端实现之间存在不一致。
- 用户明确提到旧项目、AI 写乱、外包交付、接手项目、没有真源文档。
- `data-map` 或 `server-frame` 需要从已有代码而不是 PRD/新需求中推导对象、读写路径或边界。

不触发条件：

- 新项目 0 到 1，从 PRD、用户旅程、技术选型开始设计。
- 用户只要求解释概念，不要求分析代码或产出项目文档。
- 用户明确要求只做某个独立实现，且不涉及数据流、数据库、后端边界或救援诊断。

## project-rescue-map 接入

`project-rescue-map` 把 DFD 作为旧项目救援的横向证据层，而不是替代阶段矩阵。

接入规则：

- 在 `Standard Rescue Audit` 或 `Deep Rescue Map` 中，如果发现路由、控制器、服务、Repository、SQL、事件处理或页面组件，必须调用或引用 `reverse-dfd-analysis`。
- 最小产物是 `顶层图.md` 和 `证据表.md`。
- 当诊断需要判断数据/API/后端冲突时，补充 `0层图.md`。
- 如果缺少目标层级的前置图，必须遵守 `reverse-dfd-analysis` 的层级门禁，不得跳层补画。

推荐落盘：

- `<project-root>/docs/rescue/runs/<run-id>/dfd/顶层图.md`
- `<project-root>/docs/rescue/runs/<run-id>/dfd/0层图.md`
- `<project-root>/docs/rescue/runs/<run-id>/dfd/证据表.md`

报告引用：

- `project-rescue-report.md` 引用 DFD 结论。
- `evidence-ledger.md` 收录 DFD 证据表摘要。
- `conflict-drift-log.md` 记录 DFD 暴露出的文档/代码/接口/数据库漂移。
- `risk-register.md` 记录由数据流暴露出的安全、隐私、权限、迁移或数据一致性风险。

## data-map 接入

`data-map` 把 DFD 作为数据库设计输入证据，不替代 ERD、表设计或迁移计划。

接入规则：

- 当数据库设计来自已有代码、已有前端页面、已有 API 或旧项目反推时，必须读取或生成 DFD 证据。
- `业务流程证据表` 应引用 DFD 中的加工和数据流。
- `核心业务对象清单` 应引用 DFD 中的数据存储、数据流和证据表。
- `关系矩阵` 和 `table-specs.md` 应能追溯到 DFD 证据或标注合理推导/待确认。
- 索引和查询计划不能只来自表字段猜测，必须结合 DFD 中的读数据流、写数据流和页面/API 入口。

推荐落盘：

- `<project-root>/docs/database/dfd/顶层图.md`
- `<project-root>/docs/database/dfd/0层图.md`
- `<project-root>/docs/database/dfd/证据表.md`

输出引用：

- `database-design.md` 增加“DFD 输入证据”小节。
- `business-object-catalog.md` 增加“来源 DFD 元素/证据”列。
- `relationship-matrix.md` 标注关系来自直接证据、合理推导或待确认。
- `table-specs.md` 标注每张表的来源数据流、读写加工和证据文件。

## server-frame 接入

`server-frame` 只在模式 B “现有后端代码梳理、审计、修复”中强制接入 DFD。模式 A “0→1 后端可运行骨架搭建”不强制接入。

接入规则：

- 在审计已有后端时，先用 DFD 建立路由、Controller/Handler、Service、Repository/Data Access、数据存储和外部实体之间的逻辑数据流。
- 用 DFD 检查路由是否承载复杂业务、Service 是否绕过权限、Repository 是否处理 HTTP 或角色判断、Controller 是否直接 SQL。
- 用 DFD 检查敏感数据是否经过输入校验、认证/授权、日志脱敏和错误处理边界。
- 用 DFD 证据辅助生成目录/文件责任表，但不能用 DFD 代替运行证据。

推荐落盘：

- `<project-root>/docs/backend/dfd/顶层图.md`
- `<project-root>/docs/backend/dfd/0层图.md`
- `<project-root>/docs/backend/dfd/证据表.md`

输出引用：

- `backend-architecture-source-of-truth.md` 引用系统边界、主要加工和数据流。
- `file-responsibility-map.md` 引用 DFD 证据说明每层职责。
- `security-baseline.md` 引用敏感数据流和外部实体交互。
- `acceptance-report.md` 说明 DFD 是静态证据，不替代启动、健康检查、API 响应或测试结果。

## 硬边界

- 不为新项目 0→1 强制生成 DFD。
- 不跳过 `reverse-dfd-analysis` 的目标层级门禁。
- DFD 是逻辑数据流证据，不替代数据库 ERD、API 契约、后端运行证据或最终验收。
- 证据不足时必须标注缺口，不能脑补数据流。
- 引用 DFD 时必须保留代码证据索引，不只引用图。
- 三个接入 skill 不应复制 DFD 绘图规则；只引用 `reverse-dfd-analysis`，避免规则分叉。

## 验收标准

- `project-rescue-map` 明确在旧项目诊断中何时必须调用 `reverse-dfd-analysis`。
- `data-map` 明确在已有代码反推数据库时如何消费 DFD 证据。
- `server-frame` 明确在模式 B 后端审计中如何消费 DFD 证据。
- 三个 skill 都保留自己的职责边界，不把 DFD 当作唯一真源。
- 输出路径和引用位置清楚，后续 agent 可以按文档落盘和交接。

## 暂不纳入

- 不把 DFD 接入 `build-map` 总控入口。
- 不要求 `talk-link`、`final-check` 或 `work-plan` 直接引用 DFD。
- 不实现自动生成 Mermaid 的脚本。
- 不新增跨 skill 的共享模板系统。
