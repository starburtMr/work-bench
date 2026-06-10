---
name: skeleton-check
description: "Inspect existing frontend/apps and backend/apps skeleton candidates, decide reuse vs create, and output the chosen candidate path plus the delivery target mapping. Use after API contract design and before frontend/backend skeleton implementation."
---

# 骨架候选检查 Skill

## 1. 在完整开发工作流中的位置

- 阶段编号：`05`
- 阶段名称：骨架候选检查 / 复用或新建判定
- 总控入口：[`build-map`](../00-build-map/SKILL.md)
- 本阶段目标：先检查 `frontend/apps` 和 `backend/apps` 里的候选骨架，再决定复用现有模板，还是先新建一个候选骨架补充库。

## 2. 何时启用

- `talk-link` 已经产出接口契约，现在要决定前端或后端骨架怎么落地。
- 需要先读取 `frontend/README.md` / `backend/README.md` 候选骨架索引，再判断现有 `frontend/apps` / `backend/apps` 里是否已经有可复用的骨架。
- 需要明确本次项目的 delivery target 和候选库边界。

## 3. 上游输入契约

本 skill 不应孤立执行。除非用户明确要求单独使用，否则应优先读取或生成以下输入：

- `<project-root>/docs/product/v1-mvp-scope.md` 与用户路径。
- `<project-root>/docs/architecture/tech-stack-decision.md`。
- `<project-root>/docs/api/api-contract-source-of-truth.md` 或接口草案。
- `<project-root>/docs/product/bootstrap-targets.md` 记录的 frontend/backend delivery target。
- `frontend/README.md` 和 `backend/README.md` 候选骨架索引。
- `frontend/apps/*` 和 `backend/apps/*` 当前已有的候选骨架。

## 4. 下游输出契约

本 skill 必须把结果沉淀成可被后续 skill 直接消费的交付物：

- `<project-root>/docs/skeleton/skeleton-selection-report.md`：前端/后端候选选择报告。
- `<project-root>/docs/skeleton/frontend-selection.md`：前端 reuse/create 判定。
- `<project-root>/docs/skeleton/backend-selection.md`：后端 reuse/create 判定。
- `<project-root>/docs/skeleton/delivery-targets.md`：本次项目的 frontend/backend 落地路径。

## 5. 与其他 skill 的引用关系

### 5.1 上游 skill

- [`idea-check`](../01-idea-check/SKILL.md)
- [`tool-pick`](../02-tool-pick/SKILL.md)
- [`data-map`](../03-data-map/SKILL.md)
- [`talk-link`](../04-talk-link/SKILL.md)

### 5.2 下游 skill

- [`web-frame`](../06-web-frame/SKILL.md)
- [`server-frame`](../07-server-frame/SKILL.md)
- [`work-plan`](../08-work-plan/SKILL.md)

### 5.3 交接载荷

交给下游时，至少携带以下信息：

- frontend / backend 各自的 delivery target。
- 每侧的 `reuse` 或 `create` 决策。
- 选中的候选骨架路径，或建议新建的候选骨架路径。
- 候选库缺口、风险和下一步动作。

## 6. 本阶段不可违反的硬规则

1. 只做候选检查和判定，不直接实现业务功能。
2. 查询候选前必须先读 `frontend/README.md` 和 `backend/README.md`，再扫描 `frontend/apps/*` 与 `backend/apps/*`。
3. 不得把 `frontend/apps` 和 `backend/apps` 外的项目目录当成候选库。
4. 如果没有合适候选，必须明确输出 `create`，并把新骨架放回 `frontend/apps` 或 `backend/apps`，同时更新对应 README 索引。
5. 复用候选时，从 work-bench 候选库复制到记录的 delivery target；默认 frontend 为 `<project-root>/frontend`，backend 为 `<project-root>/backend`。
6. 不能把 delivery target 和 candidate library 混在一起；默认不得把 `apps` 目录复制进目标项目。
7. 不得伪造“已有可复用骨架”的结论。

## 7. 阶段完成门禁

- [ ] `frontend/README.md` / `backend/README.md` 候选索引已读取。
- [ ] 前端候选扫描完成。
- [ ] 后端候选扫描完成。
- [ ] 每侧都给出 `reuse` 或 `create` 结论。
- [ ] delivery target 已和 `<project-root>/docs/product/bootstrap-targets.md` 对齐。
- [ ] 若选择 `create`，对应 README 索引已纳入更新范围。
- [ ] 选择报告可被 `web-frame` / `server-frame` 直接消费。
