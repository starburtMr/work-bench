---
name: final-check
description: "Verify fullstack release readiness with evidence across scope, stack, schema, API, frontend, backend, docs, tests, security, and rollback plans. Use before merge, release, demo, or handoff."
---

# 全链路质量门禁与发布准备 Skill


## 1. 在完整开发工作流中的位置

- 阶段编号：`10`
- 阶段名称：全链路质量门禁 / 发布准备
- 总控入口：[`build-map`](../00-build-map/SKILL.md)
- 本阶段目标：用真实证据验证产品、技术栈、数据库、API、前端、后端、文档、测试、安全和回滚计划是否达到发布或继续开发标准。

## 2. 何时启用

当产品、技术、数据库、API、前端、后端、交付计划和仓库文档都已经完成一轮后，启用本 skill 做全链路质量门禁。它用于判断项目是否真的可以进入业务开发、合并、演示、部署或发布。

## 3. 上游输入契约

本 skill 不应孤立执行。除非用户明确要求单独使用，否则应优先读取或生成以下输入：

- `<project-root>/docs/product/*`
- `<project-root>/docs/skeleton/*`
- `<project-root>/docs/architecture/*`
- `<project-root>/docs/database/*`
- `<project-root>/docs/api/*`
- `<project-root>/docs/frontend/*`
- `<project-root>/docs/backend/*`
- `<project-root>/docs/delivery/*`
- `<project-root>/README.md`
- `<project-root>/AGENTS.md`
- `<project-root>/.github/workflows/*`
- 实际代码、配置、测试、构建脚本和运行证据。

## 4. 下游输出契约

- `<project-root>/docs/quality/fullstack-acceptance-report.md`：全链路验收报告。
- `<project-root>/docs/quality/evidence-pack.md`：命令、截图、接口响应、日志、测试结果证据清单。
- `<project-root>/docs/quality/regression-test-plan.md`：回归测试计划。
- `<project-root>/docs/quality/security-and-data-check.md`：安全与数据检查。
- `<project-root>/docs/quality/release-readiness-checklist.md`：发布准备清单。
- `<project-root>/docs/quality/rollback-and-recovery-plan.md`：回滚/恢复计划。
- `<project-root>/docs/quality/open-issues-and-waivers.md`：遗留问题、风险豁免和负责人。

## 5. 与其他 skill 的引用关系

### 上游 skill

- [`idea-check`](../01-idea-check/SKILL.md)
- [`tool-pick`](../02-tool-pick/SKILL.md)
- [`data-map`](../03-data-map/SKILL.md)
- [`talk-link`](../04-talk-link/SKILL.md)
- [`skeleton-check`](../05-skeleton-check/SKILL.md)
- [`web-frame`](../06-web-frame/SKILL.md)
- [`server-frame`](../07-server-frame/SKILL.md)
- [`work-plan`](../08-work-plan/SKILL.md)
- [`doc-rules`](../09-doc-rules/SKILL.md)

### 下游 skill

- 无。

### 5.3 交接载荷

- 无。该阶段输出最终验收结论、证据包、风险豁免、发布/回滚建议和后续修复顺序。

## 6. 核心原则

1. 不相信“应该可以”，只相信证据。
2. 不允许伪造命令结果、测试结果、接口响应、构建结果或截图。
3. 验收不是只看功能，也要看产品边界、架构一致性、数据安全、文档准确性和可维护性。
4. 任何失败必须分类为：阻塞、发布前必须修复、可带风险上线、后续优化。
5. 对阻塞项不得给出“通过”。
6. 文档与实际代码冲突时，以实际证据为准，并要求更新真源文档。
7. 涉及支付、权限、隐私、敏感数据、删除、导出、第三方密钥的功能必须提高门禁等级。

## 7. 标准验收维度

### 7.1 产品边界一致性

- V1 Must-have 是否全部覆盖。
- Won't-have 是否没有偷偷实现。
- 验收标准是否可检查。
- 用户路径是否闭环。

### 7.2 技术栈一致性

- 实际依赖是否符合技术栈决策。
- 是否新增未审批依赖。
- 是否出现互斥技术或重复框架。
- 包管理器、构建、测试、部署命令是否一致。

### 7.3 数据库与数据安全

- 表、字段、索引、约束是否符合数据库设计。
- Migration 是否可版本化、可审查、可回滚/前滚。
- 敏感数据是否脱敏、加密、哈希或不存。
- 软删除、审计、生命周期是否落地。

### 7.4 API 契约

- 接口路径、方法、请求、响应、错误码是否符合契约。
- 认证、权限、分页、排序、过滤、幂等是否一致。
- Mock、前端类型、后端 DTO 是否同步。

### 7.5 前端

- 页面、组件、样式、Token、状态、API Client 是否符合前端骨架规则。
- 是否有硬编码、重复组件、散落请求、绕过错误处理。
- 构建、类型检查、lint、测试是否通过。

### 7.6 后端

- 启动、配置、数据库连接、健康检查、日志/requestId 是否可验证。
- 错误处理、权限占位、输入校验、安全基线是否存在。
- 目录/文件责任是否清晰。

### 7.7 文档与 Agent 规则

- README、docs index、AGENTS.md 是否与真实项目一致。
- CI workflow 是否执行真实命令。
- 文档链接是否有效。

## 8. 输出模板

```md
# 全链路验收报告

## 1. 验收结论

- 结论：通过 / 条件通过 / 不通过
- 阻塞项数量：
- 高风险项数量：
- 可接受遗留项：

## 2. 验收范围

| 范围 | 文档 | 代码/证据 | 状态 |
|---|---|---|---|

## 3. 命令证据

| 命令 | 结果 | 证据 | 备注 |
|---|---|---|---|

## 4. 功能与用户路径验收

## 5. 技术栈一致性验收

## 6. 数据库与安全验收

## 7. API 契约验收

## 8. 前端验收

## 9. 后端验收

## 10. 文档与 Agent 验收

## 11. 问题清单

| ID | 等级 | 问题 | 影响 | 处理建议 | 负责人 |
|---|---|---|---|---|---|

## 12. 发布/继续开发建议

## 13. 风险豁免
```

## 9. 阶段完成门禁

- [ ] 所有关键命令都有真实执行证据或明确说明无法执行的原因。
- [ ] 阻塞项为 0，或明确判定“不通过”。
- [ ] 文档、代码、CI 和 AGENTS.md 不存在明显冲突。
- [ ] 数据、安全、权限、错误处理和密钥管理没有高危缺口。
- [ ] 发布/继续开发建议明确，并列出下一步修复顺序。

## 10. 推荐落盘位置

- 阶段真源文档：`<project-root>/docs/`
- 阶段决策记录：`<project-root>/docs/decisions/`
- 阶段检查清单：`<project-root>/docs/checklists/`
- 面向 Agent 的长期约束：`<project-root>/AGENTS.md` 或 `<project-root>/docs/agent-rules/`
