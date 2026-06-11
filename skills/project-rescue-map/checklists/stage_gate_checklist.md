# Work-bench Stage Gate Checklist

## 01 idea-check

- [ ] V1 目标清楚。
- [ ] Must/Should/Could/Won't 边界清楚。
- [ ] 核心用户路径闭环。
- [ ] 核心业务对象清楚。
- [ ] 验收标准可检查。
- [ ] 代码没有明显偏离 V1。

## 02 tool-pick

- [ ] 技术栈决策存在。
- [ ] 依赖规则存在。
- [ ] 包管理器唯一。
- [ ] 禁用技术/重评条件清楚。
- [ ] 实际依赖与决策一致。

## 03 data-map

- [ ] 业务对象目录存在。
- [ ] 关系矩阵/ERD 存在。
- [ ] schema/model 与文档一致。
- [ ] migration 计划存在。
- [ ] 敏感字段、审计、生命周期清楚。
- [ ] 回滚/前滚策略存在。

## 04 talk-link

- [ ] API 契约真源存在。
- [ ] 请求/响应/错误码定义清楚。
- [ ] 鉴权、权限、分页、过滤、幂等清楚。
- [ ] 前端 API client 与后端 route 一致。
- [ ] mock/contract test 策略存在。

## 05 skeleton-check

- [ ] 前后端 delivery target 明确。
- [ ] 复用/创建决策有记录。
- [ ] 骨架来源和限制清楚。

## 06 web-frame

- [ ] 前端目录职责清楚。
- [ ] 路由和页面清单清楚。
- [ ] 组件和 design token 规则存在。
- [ ] API client 集中。
- [ ] 前端质量命令存在。

## 07 server-frame

- [ ] 后端入口和配置清楚。
- [ ] 错误、日志、requestId 清楚。
- [ ] 鉴权/权限/输入校验基线存在。
- [ ] 健康检查存在。
- [ ] 数据访问层边界清楚。

## 08 work-plan

- [ ] V1 垂直切片存在。
- [ ] 每个切片有 DoD。
- [ ] 任务边界可 PR 化。
- [ ] 变更控制存在。

## 09 doc-rules

- [ ] README 与真实命令一致。
- [ ] docs index 完整。
- [ ] AGENTS.md 约束真实可执行。
- [ ] CI 跑真实命令。

## 10 final-check

- [ ] 范围验收。
- [ ] 架构一致性验收。
- [ ] 数据/API/前端/后端验收。
- [ ] 测试和安全证据。
- [ ] 发布/回滚计划。
- [ ] 风险豁免清楚。
