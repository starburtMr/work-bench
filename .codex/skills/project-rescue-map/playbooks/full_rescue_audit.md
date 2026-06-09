# Full Rescue Audit Playbook

## 目标

给已开工项目生成完整 `Project Rescue Report`、`Evidence Ledger`、`Risk Register`、`Conflict and Drift Log`、`Rescue Stateboard`。

## 阶段

### 1. Intake

- 明确项目根目录。
- 明确是否有生产数据和高风险业务。
- 明确是否允许落盘和运行命令。

### 2. Instruction Scan

- 读取 agent 规则。
- 读取 README 和 docs index。
- 记录项目自定义禁令。

### 3. Evidence Ledger

按维度收集证据：产品、技术、数据、API、前端、后端、计划、文档、质量、安全、交付。

### 4. Emergency Gate

先判断 `STOP / CONTAIN / CONTINUE`。

### 5. Stage Matrix

按 work-bench 01-10 逐阶段诊断。每个阶段必须有：状态、证据等级、缺口、风险、推荐下一步。

### 6. Cross-cutting Analysis

输出横向健康扫描：范围、架构、数据/API、质量、安全、交付、文档。

### 7. Conflict and Drift

找出所有“同一问题多套真源”的地方，标注应回到哪个 skill 修正。

### 8. Rescue Roadmap

按影响下游程度和风险不可逆性排序。只做阶段级，不做具体代码任务池。

### 9. Handoff

为下一步 skill 输出 `handoff-packet`。

## 完成门槛

- 阶段矩阵完整。
- 阻塞项和必须补项清楚。
- 路线图不越权修复。
- 没有伪造命令或证据。
