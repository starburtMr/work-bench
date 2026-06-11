# work-bench

work-bench 是给 Codex 这类编程助手使用的全局插件、Skill 和骨架库。仓库根目录包含 `.codex-plugin/plugin.json`，可以作为插件源码根安装或分发。

它包含：

- `.codex/skills/`：从想法、选型、数据、接口、骨架、前后端落地、文档到验收的工作流 skill。
- `skills/`：插件导出的 skill 目录，内容与 `.codex/skills/` 同步，用于满足 Codex plugin manifest 规范。
- `frontend/apps/*`：可复用前端骨架候选。
- `backend/apps/*`：可复用后端骨架候选。
- `scripts/work_bench_skeletons.py`：合并用户全局骨架库和插件内置骨架库的辅助脚本。

## 插件使用

### 通过 Codex CLI 安装

当前公开仓库地址是：

```text
https://github.com/starburtMr/work-bench
```

先把这个仓库作为 Codex 插件 marketplace 加入本机：

```bash
codex plugin marketplace add starburtMr/work-bench --ref codex/initialize-workbench
```

然后从该 marketplace 安装插件：

```bash
codex plugin add work-bench@work-bench
```

安装后开启一个新的 Codex 会话，让插件里的 skills 重新加载。可用下面命令确认插件已安装：

```bash
codex plugin list
```

说明：当前 Codex CLI 的安装子命令是 `codex plugin add`。如果你使用的 Codex 版本把同等能力命名为 `codex plugin install`，则使用 `codex plugin install work-bench@work-bench`。

- 插件说明：[docs/plugin-usage.md](docs/plugin-usage.md)
- 骨架库规则：[docs/skeleton-library.md](docs/skeleton-library.md)
- 新骨架沉淀规范：[docs/skeleton-contribution.md](docs/skeleton-contribution.md)

用户新增或定制的可复用骨架默认放到 `<codex-home>/work-bench/`，其中 `<codex-home>` 是 `CODEX_HOME` 或 `~/.codex`。插件内置骨架仍随仓库的 `frontend/apps` 和 `backend/apps` 分发。

### 提交内置骨架变更

个人项目里沉淀的新骨架先注册到用户全局骨架库；当这个骨架已经完整、希望合入 work-bench 仓库供别人使用时，使用 `change-pr` 创建 PR，不直接改插件缓存或推发布分支。

```bash
python3 scripts/work_bench_skeletons.py change-pr \
  --type add \
  --kind frontend \
  --name react-dashboard \
  --source ~/.codex/work-bench/frontend/apps/react-dashboard
```

`change-pr` 支持 `add`、`update`、`docs`、`remove`、`rename`，默认把 PR 发到 `skeleton-inbox` 分支。该命令会使用 `<codex-home>/work-bench/repo` 作为贡献 clone，检查敏感内容和构建产物，生成中文 PR 标题/说明，并更新 `frontend/README.md` 或 `backend/README.md` 的内置骨架索引。机器调用可加 `--json`，本地演练可加 `--dry-run`。

## 推荐入口

| 场景 | 入口 | 用途 |
| --- | --- | --- |
| 新项目从零启动 | `.codex/skills/00-build-map/` | 串联 01-10，按完整落地流程推进。 |
| 已开工但范围、架构、骨架或交付混乱 | `.codex/skills/project-rescue-map/` | 先快速诊断问题、排序优先级，再回到对应细分 skill 修复。 |
| 前端骨架索引 | `frontend/README.md` | 复制前先比较用户全局和插件内置的前端候选。 |
| 后端骨架索引 | `backend/README.md` | 复制前先比较用户全局和插件内置的后端候选。 |

## 双轨工作流

执行层是 `00-10`：`00-build-map` 负责编排，`01-10` 负责真正落地，覆盖范围澄清、技术选型、数据模型、前后端契约、骨架选择、前端、后端、交付计划、文档规则和最终验收。

管理层是五大类：范围、架构、骨架、交付、验收。它用于 `project-rescue-map` 快速说明项目问题和优先级，方便先看清哪里最乱、哪里最该补。

五大类只是摘要视图，不替代 `00-10` skill。实际修复仍回到对应细分 skill 执行，例如范围问题回到 `01-idea-check`，骨架问题回到 `05-skeleton-check`，验收问题回到 `10-final-check`。

## 核心原则

- work-bench 是 Skill 和骨架库，不是项目默认输出目录。
- 项目文档和代码默认写入已确认的 `project-root`。
- 前端默认目标路径是目标项目内的 `frontend/`，后端默认目标路径是目标项目内的 `backend/`。
- 复制骨架前必须先读用户全局骨架库和插件内置骨架库，再读候选骨架自己的 `README.md`、`AGENTS.md` 和 `docs/`。
- 同名骨架优先使用用户全局版本，并在报告中标注 `source` 和 `path`。
