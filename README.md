# work-bench

work-bench 是给 Codex 这类编程助手使用的 Skill 和骨架库，包含：

- `.codex/skills/`：从想法、选型、数据、接口、骨架、前后端落地、文档到验收的工作流 skill。
- `frontend/apps/*`：可复用前端骨架候选。
- `backend/apps/*`：可复用后端骨架候选。

## 推荐入口

| 场景 | 入口 | 用途 |
| --- | --- | --- |
| 新项目从零启动 | `.codex/skills/00-build-map/` | 串联 01-10，按完整落地流程推进。 |
| 已开工但范围、架构、骨架或交付混乱 | `.codex/skills/project-rescue-map/` | 先快速诊断问题、排序优先级，再回到对应细分 skill 修复。 |
| 前端骨架索引 | `frontend/README.md` | 复制前先比较 `frontend/apps/*` 候选。 |
| 后端骨架索引 | `backend/README.md` | 复制前先比较 `backend/apps/*` 候选。 |

## 双轨工作流

执行层是 `00-10`：`00-build-map` 负责编排，`01-10` 负责真正落地，覆盖范围澄清、技术选型、数据模型、前后端契约、骨架选择、前端、后端、交付计划、文档规则和最终验收。

管理层是五大类：范围、架构、骨架、交付、验收。它用于 `project-rescue-map` 快速说明项目问题和优先级，方便先看清哪里最乱、哪里最该补。

五大类只是摘要视图，不替代 `00-10` skill。实际修复仍回到对应细分 skill 执行，例如范围问题回到 `01-idea-check`，骨架问题回到 `05-skeleton-check`，验收问题回到 `10-final-check`。

## 核心原则

- work-bench 是 Skill 和骨架库，不是项目默认输出目录。
- 项目文档和代码默认写入已确认的 `project-root`。
- 前端默认目标路径是目标项目内的 `frontend/`，后端默认目标路径是目标项目内的 `backend/`。
- 复制骨架前必须先读 `frontend/README.md` 或 `backend/README.md`，再读候选骨架自己的 `README.md`、`AGENTS.md` 和 `docs/`。
