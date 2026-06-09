# Scope Boundary Rescue Playbook

## 触发信号

- 代码里出现大量未在 V1 说明的功能。
- 用户路径不闭环，但页面很多。
- 前端 mock 和后端能力严重不匹配。
- 团队对“先做什么”没有共识。
- 验收标准无法判断通过/失败。

## 诊断步骤

1. 找 V1 scope、PRD、roadmap、任务计划。
2. 从前端路由和页面反推实际 scope。
3. 从后端 API 和数据库反推实际业务对象。
4. 标出 `Must / Should / Could / Won't / Accidentally Built`。
5. 找出下游最大风险：数据、API、页面、权限、交付。
6. 建议回到 `idea-check` 输出冻结版 V1。

## 输出

| 项 | 内容 |
|---|---|
| 当前真实 scope |  |
| 文档声明 scope |  |
| 代码实际 scope |  |
| 偷偷膨胀范围 |  |
| 缺失闭环路径 |  |
| 必须砍掉/冻结 |  |
| 回到 skill | `idea-check` |

## 通过门槛

- V1 有唯一真源。
- Won't-have 明确。
- 代码继续开发只围绕 Must-have。
- 下游 data/API/frontend/backend 都能引用 V1 scope。
