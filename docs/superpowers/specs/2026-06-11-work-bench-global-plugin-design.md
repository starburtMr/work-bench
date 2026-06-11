# work-bench 全局插件设计

## 目标

把当前 `work-bench` 项目做成一个可分发、可全局安装的 Codex 插件，让其他用户安装后能直接使用完整工作流 skill 和前后端骨架库。

插件第一版采用单插件大包：`work-bench`。它同时包含项目级 skills、前端骨架库、后端骨架库、说明文档和少量维护脚本。用户后续新建或沉淀的骨架也应进入全局骨架库，而不是散落在业务项目里。

## 背景

当前项目已经具备插件化基础：

- `.codex/skills/` 中有从想法、选型、数据、接口、骨架、前后端落地、文档到验收的 workflow skills。
- `frontend/apps/*` 是可复用前端骨架候选。
- `backend/apps/*` 是可复用后端骨架候选。
- `README.md` 已把项目定位为给 Codex 使用的 Skill 和骨架库。

要提供给别人下载使用时，只复制项目级 `.codex/skills` 不够。用户需要安装一次后，全局可用这些 skills，也能在全局位置访问、复用、扩展前后端骨架库。

## 方案选择

采用方案：**单插件大包**。

插件名：`work-bench`

包含内容：

- `.codex-plugin/plugin.json`：插件 manifest。
- `skills/`：由当前 `.codex/skills/*` 迁入或复制而来。
- `frontend/apps/`：内置前端骨架库。
- `backend/apps/`：内置后端骨架库。
- `docs/`：插件使用说明、骨架贡献规范、版本说明。
- `scripts/`：用于列出、复制、注册骨架的辅助脚本。

不采用拆分插件套件。拆成 `work-bench-skills`、`work-bench-frontend`、`work-bench-backend` 会增加安装和版本匹配成本，也会让 skill 引用骨架路径更复杂。

不采用“插件只带下载器”。下载器依赖网络和远程仓库状态，不符合“安装后前后端骨架库也在全局”的目标。

## 插件目录

建议插件源码目录使用：

```text
~/plugins/work-bench/
  .codex-plugin/
    plugin.json
  skills/
    00-build-map/
    01-idea-check/
    ...
    reverse-dfd-analysis/
  frontend/
    README.md
    apps/
      <builtin-frontend-skeleton>/
  backend/
    README.md
    apps/
      <builtin-backend-skeleton>/
  docs/
    plugin-usage.md
    skeleton-library.md
    skeleton-contribution.md
    changelog.md
  scripts/
    list_skeletons.py
    copy_skeleton.py
    register_skeleton.py
```

`skills/` 内的 `SKILL.md` 需要能引用插件内置的 `frontend/`、`backend/`、`docs/`。引用方式应避免写死当前项目路径 `/home/xiaoyaozu/AI/projects/work-bench`，改成相对当前 skill 或插件根目录的路径说明。

## 全局用户骨架库

插件本体是可更新资产，用户新增骨架是用户资产。两者必须分开。

用户新增骨架默认写入：

```text
~/.codex/work-bench/
  frontend/
    apps/
      <user-frontend-skeleton>/
  backend/
    apps/
      <user-backend-skeleton>/
  registry/
    frontend-skeletons.json
    backend-skeletons.json
```

读取顺序：

1. 用户全局骨架库：`~/.codex/work-bench/frontend/apps`、`~/.codex/work-bench/backend/apps`
2. 插件内置骨架库：`<plugin-root>/frontend/apps`、`<plugin-root>/backend/apps`

同名策略：

- 用户全局骨架优先。
- 插件内置骨架保持只读语义。
- 如果用户想定制内置骨架，应复制到 `~/.codex/work-bench/...` 后再改。
- skill 在报告中应说明实际选用的是“用户全局骨架”还是“插件内置骨架”。

这样插件升级时不会覆盖用户新增或定制骨架。

## Skill 行为调整

### skeleton-check

`skeleton-check` 负责比较候选骨架。插件化后它应同时扫描用户全局骨架库和插件内置骨架库，并在候选清单里标注来源。

输出候选时建议增加字段：

- `source`: `user-global` 或 `plugin-builtin`
- `path`: 实际骨架路径
- `kind`: `frontend` 或 `backend`
- `stack`: 从骨架 README、AGENTS 或 manifest 中提取

### web-frame

`web-frame` 在创建或规范化前端骨架时，应优先考虑用户全局前端骨架，再考虑插件内置前端骨架。

当用户要求“把这个新前端骨架保存为可复用骨架”时，应保存到：

```text
~/.codex/work-bench/frontend/apps/<skeleton-name>/
```

### server-frame

`server-frame` 在创建或规范化后端骨架时，应优先考虑用户全局后端骨架，再考虑插件内置后端骨架。

当用户要求“把这个新后端骨架保存为可复用骨架”时，应保存到：

```text
~/.codex/work-bench/backend/apps/<skeleton-name>/
```

### build-map

`build-map` 作为总控入口，不直接复制骨架。它只需要知道骨架来源已经扩展为“用户全局 + 插件内置”，实际选择仍交给 `skeleton-check`、`web-frame`、`server-frame`。

### doc-rules

`doc-rules` 应覆盖插件文档约定：

- 插件 README 说明安装和全局使用方式。
- `docs/skeleton-contribution.md` 说明如何把新骨架沉淀到 `~/.codex/work-bench`。
- 骨架自身 README 说明适用场景、技术栈、复制方式和验证命令。

## 骨架注册

第一版可以不强制每个骨架都有 manifest，但需要为后续自动化预留注册机制。

推荐脚本职责：

- `list_skeletons.py`：合并列出用户全局骨架和插件内置骨架。
- `copy_skeleton.py`：把选定骨架复制到目标项目的 `frontend/` 或 `backend/`。
- `register_skeleton.py`：把当前项目中的新骨架复制到用户全局骨架库，并更新 registry。

registry 第一版可以只记录最小元数据：

```json
{
  "name": "react-spa-toolkit",
  "kind": "frontend",
  "source": "user-global",
  "path": "~/.codex/work-bench/frontend/apps/react-spa-toolkit",
  "stack": ["React", "Vite"],
  "description": "React SPA skeleton with routing, tests, and app structure."
}
```

内置骨架可以通过目录扫描获得，不需要写入用户 registry。用户 registry 只记录用户新增或覆盖的骨架。

## 分发与安装

使用 `plugin-creator` 的标准结构创建插件：

- 使用 `.codex-plugin/plugin.json` 作为 manifest。
- 生成个人 marketplace 条目用于本机开发和预览。
- 对外分发时，插件源码应能作为一个完整目录或仓库被安装。

本设计不规定最终发布渠道。第一版只要求本地插件结构有效，并能通过 plugin validator。

## 迁移步骤

实施时按低风险顺序迁移：

1. 用 `plugin-creator` scaffold `work-bench` 插件。
2. 复制当前 `.codex/skills/*` 到插件 `skills/`。
3. 复制当前 `frontend/`、`backend/`、`README.md` 和必要 docs 到插件。
4. 调整 skill 中的路径说明，移除项目绝对路径假设。
5. 增加全局用户骨架库读取规则。
6. 增加或预留 `scripts/`。
7. 运行 plugin validator。
8. 检查 diff，只提交插件化相关文件。

## 验收标准

- `work-bench` 插件目录包含合法 `.codex-plugin/plugin.json`。
- 插件通过 `plugin-creator/scripts/validate_plugin.py` 校验。
- 安装后能看到并使用核心 skills：`build-map`、`skeleton-check`、`web-frame`、`server-frame`、`project-rescue-map`、`reverse-dfd-analysis`。
- 插件内置前端和后端骨架库随插件可用。
- 用户新增骨架保存到 `~/.codex/work-bench`，不会写入插件安装缓存目录。
- 同名骨架时用户全局版本优先，并在输出中标注来源。
- 文档说明插件安装、骨架选择、骨架复制、用户新增骨架沉淀方式。

## 暂不纳入

- 不在第一版实现远程骨架下载器。
- 不把插件拆成多个独立插件。
- 不要求所有骨架立即补齐 manifest。
- 不自动迁移用户本地已有项目中的骨架。
- 不修改当前前后端骨架的业务代码，除非为插件路径引用所必需。
