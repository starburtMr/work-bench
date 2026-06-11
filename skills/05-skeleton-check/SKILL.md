---
name: skeleton-check
description: "Inspect existing frontend/apps and backend/apps skeleton candidates, decide reuse vs create, and output the chosen candidate path plus the delivery target mapping. Use after API contract design and before frontend/backend skeleton implementation."
---

# 骨架候选检查 Skill

## 1. 在完整开发工作流中的位置

- 阶段编号：`05`
- 阶段名称：骨架候选检查 / 复用或新建判定
- 总控入口：[`build-map`](../00-build-map/SKILL.md)
- 本阶段目标：先检查用户全局骨架库和插件内置骨架库里的候选骨架，再决定复用现有模板，还是先新建一个候选骨架补充库。

## 2. 何时启用

- `talk-link` 已经产出接口契约，现在要决定前端或后端骨架怎么落地。
- 需要先读取 `frontend/README.md` / `backend/README.md` 候选骨架索引，再判断用户全局库与插件内置库里是否已经有可复用的骨架。
- 需要明确本次项目的 delivery target 和候选库边界。

## 3. 上游输入契约

本 skill 不应孤立执行。除非用户明确要求单独使用，否则应优先读取或生成以下输入：

- `<project-root>/docs/product/v1-mvp-scope.md` 与用户路径。
- `<project-root>/docs/architecture/tech-stack-decision.md`。
- `<project-root>/docs/api/api-contract-source-of-truth.md` 或接口草案。
- `<project-root>/docs/product/bootstrap-targets.md` 记录的 frontend/backend delivery target。
- `frontend/README.md` 和 `backend/README.md` 插件内置候选骨架索引。
- 用户全局骨架库：`<codex-home>/work-bench/frontend/apps/*` 与 `<codex-home>/work-bench/backend/apps/*`。
- 插件内置骨架库：`frontend/apps/*` 与 `backend/apps/*`。

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
- 选中候选的来源：`user-global` 或 `plugin-builtin`。
- 候选库缺口、风险和下一步动作。

## 6. 本阶段不可违反的硬规则

1. 只做候选检查和判定，不直接实现业务功能。
2. 查询候选前必须先读 `frontend/README.md` 和 `backend/README.md`，再扫描用户全局骨架库与插件内置骨架库。
3. 不得把 delivery target 或业务项目目录当成候选库。
4. 用户全局骨架库优先于插件内置骨架库；同名同类型候选冲突时选 `user-global`，并在报告中标注被覆盖的 `plugin-builtin` 候选。
5. 如果没有合适候选，必须明确输出 `create`，并把新骨架注册到 `<codex-home>/work-bench/frontend/apps` 或 `<codex-home>/work-bench/backend/apps`，同时更新用户 registry；不要写入插件安装缓存目录。
6. 复用候选时，从选中的 work-bench 候选库复制到记录的 delivery target；默认 frontend 为 `<project-root>/frontend`，backend 为 `<project-root>/backend`。
7. 不能把 delivery target 和 candidate library 混在一起；默认不得把 `apps` 目录复制进目标项目。
8. 每个候选必须输出 `source` 和 `path`。
9. 不得伪造“已有可复用骨架”的结论。
10. 当完整的用户全局骨架需要沉淀为插件内置骨架时，必须使用 `scripts/work_bench_skeletons.py change-pr` 创建到 `skeleton-inbox` 的 PR；不得直接修改插件缓存目录或推送发布分支。

## 7. 阶段完成门禁

- [ ] `frontend/README.md` / `backend/README.md` 插件内置候选索引已读取。
- [ ] 用户全局骨架库已扫描；不存在时按空库处理。
- [ ] 前端候选扫描完成。
- [ ] 后端候选扫描完成。
- [ ] 每侧都给出 `reuse` 或 `create` 结论。
- [ ] 选择报告包含候选 `source` 和 `path`。
- [ ] delivery target 已和 `<project-root>/docs/product/bootstrap-targets.md` 对齐。
- [ ] 若选择 `create`，用户 registry 已纳入更新范围；只有维护插件内置资产时才更新 `frontend/README.md` 或 `backend/README.md`。
- [ ] 若本次要把新增/修改/删除/重命名的骨架提交回 work-bench 仓库，已改用 `change-pr` 生成到 `skeleton-inbox` 的 PR。
- [ ] 选择报告可被 `web-frame` / `server-frame` 直接消费。
