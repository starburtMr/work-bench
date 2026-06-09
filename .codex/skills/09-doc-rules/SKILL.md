---
name: doc-rules
description: "Synchronize README, docs indexes, AGENTS.md, agent rules, and CI with the real stack and source-of-truth docs. Use after skeleton or architecture changes, or when repo docs drift."
---

# 仓库文档与 Agent 协作规范同步 Skill


## 1. 在完整开发工作流中的位置

- 阶段编号：`09`
- 阶段名称：仓库文档 / AGENTS.md / CI 规则固化
- 总控入口：[`build-map`](../00-build-map/SKILL.md)
- 本阶段目标：把前面阶段的产品、技术、数据库、API、前后端骨架规则同步到仓库文档、AGENTS.md 和 CI 工作流中。

## 2. 何时启用

- 新增或更新前端/后端骨架后，需要补 README、docs、AGENTS.md 或 CI。
- 完成产品/技术/数据库/API/骨架阶段后，需要把规则固化到仓库。
- 已有仓库文档与实际项目不一致，需要同步。

## 3. 上游输入契约

本 skill 不应孤立执行。除非用户明确要求单独使用，否则应优先读取或生成以下输入：

- 所有阶段真源文档。
- 仓库现有 README、docs、AGENTS.md、package.json、pyproject.toml、Makefile、CI 配置、部署配置。
- 前端/后端实际命令和测试工具。

## 4. 下游输出契约

本 skill 必须把结果沉淀成可被后续 skill 直接消费的交付物：

- `README.md`：项目入口说明与文档索引。
- `docs/README.md` 或 `docs/index.md`：文档导航。
- `AGENTS.md`：Agent 工作规则、目录地图、命令、禁止事项、验收方法。
- `.github/workflows/*`：与真实栈匹配的 CI 工作流。
- `docs/agent-rules/*`：可选的前端、后端、数据库、API 分域规则。
- `docs/skeleton/*`：骨架候选选择和 delivery target 记录。

## 5. 与其他 skill 的引用关系

### 5.1 上游 skill

- [`idea-check`](../01-idea-check/SKILL.md)
- [`tool-pick`](../02-tool-pick/SKILL.md)
- [`data-map`](../03-data-map/SKILL.md)
- [`talk-link`](../04-talk-link/SKILL.md)
- [`skeleton-check`](../05-skeleton-check/SKILL.md)
- [`web-frame`](../06-web-frame/SKILL.md)
- [`server-frame`](../07-server-frame/SKILL.md)
- [`work-plan`](../08-work-plan/SKILL.md)

### 5.2 下游 skill

- [`final-check`](../10-final-check/SKILL.md)

### 5.3 交接载荷

交给下游时，至少携带以下信息：

- 文档索引、AGENTS.md、CI 工作流。
- 每个真源文档的链接和负责阶段。
- 当前可运行命令、测试命令、构建命令和部署注意事项。
- 仍需补齐的文档缺口。

## 6. 本阶段不可违反的硬规则

1. 必须以真实仓库命令和配置为准，不得复制不存在的命令。
2. 不得保留旧项目、旧技术栈、旧路径、旧包管理器引用。
3. AGENTS.md 必须引用当前项目真源文档，而不是泛泛而谈。
4. CI 必须与实际语言、框架、测试工具和数据库依赖匹配。
5. 文档要短、可扫读、可导航，不能生成没人维护的长篇废话。

## 7. 阶段完成门禁

- [ ] README 能从零引导新人理解项目、安装、运行、测试和找到文档。
- [ ] AGENTS.md 明确 Agent 可做/不可做、变更控制、命令和验收证据。
- [ ] 所有文档链接存在且路径正确。
- [ ] CI workflow 的每一步命令在项目中能找到来源。
- [ ] 不存在跨项目引用、过期栈名、虚假命令或 stale 文档。

## 8. 工作模式补充

本 skill 是工程规则落盘器，不是重新做架构设计。若发现文档与真源冲突，返回对应上游 skill 修正真源，而不是在 README 中自行发明规则。

## 9. 推荐落盘位置

- 阶段真源文档：`docs/`
- 阶段决策记录：`docs/decisions/`
- 阶段检查清单：`docs/checklists/`
- 面向 Agent 的长期约束：`AGENTS.md` 或 `docs/agent-rules/`

## 10. 继承自原 skill 的详细规则库

> 以下内容来自原始 skill，已作为新版 skill 的细节规则保留。若出现旧 skill 名称、旧版本号或旧目录名，以新版 front matter 的 `name` 与本文件第 1-7 节为准。

## Sync Skeleton Docs

### Overview

Use this skill when a new frontend or backend skeleton has been placed in the workspace and needs its local docs, agent instructions, and GitHub Actions workflows completed from nearby example projects.

### Workflow

1. Identify whether the target skeleton is `frontend` or `backend`.
2. Read the target app's manifest and runtime clues first. Use the actual package manager, framework, test runner, and deployment files as the source of truth.
3. Read sibling example projects with the same stack and mirror their doc layout, not their wording.
4. Fill `docs/` with a short index plus concise topic pages that match the current stack only.
5. Fill `AGENTS.md` with the project overview, docs map, setup commands, structure, working rules, and verification notes.
6. Add or update `.github/workflows/*` so CI matches the real stack: install, lint, typecheck, tests, build, and optional e2e or database checks when they exist.
7. Update any repo-level index page if the workspace uses one for front-end or back-end navigation.
8. Remove cross-project references, stale stack names, and commands that do not exist in the current skeleton.

### What To Keep In Sync

- Frontend skeletons usually need:
  - a docs index
  - app overview, structure, standards, API layer, testing, security, error handling, performance, deployment, and any frontend-specific pages such as styling or state management
  - CI for install, build, lint, typecheck, tests, and Playwright or browser checks if present
- Backend Python skeletons usually need:
  - a docs index
  - app overview, structure, standards, API layer, testing, security, error handling, performance, deployment, and additional resources
  - CI for `uv sync`, `ruff`, `pytest`, and a lightweight syntax or import check when useful
- Backend TypeScript skeletons usually need:
  - a docs index
  - app overview, structure, standards, commands, architecture, routing, security, testing, deployment, and additional resources
  - CI for install, lint, typecheck, tests, build, and e2e or docs-generation steps when the repo supports them

### Quality Bar

- Keep every page short and easy to scan.
- Prefer the same file names and order used by sibling skeletons.
- Use commands that already exist in `package.json`, `pyproject.toml`, `Makefile`, `README.md`, or the repo's existing docs.
- Verify the result by checking that every linked file exists and every workflow step is runnable in the target project.

### Reference

- See [adaptation-checklist.md](references/adaptation-checklist.md) for stack-specific doc and CI patterns.
