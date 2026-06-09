# work-bench Workflow

## 双轨模型

```text
旁路入口：
  project-rescue-map
    -> 先用管理层五大类快速摘要问题和优先级
    -> 再输出 01-10 诊断矩阵
    -> 最后回到对应执行层 skill 补救

管理层五大类：
  范围 -> 01-idea-check
  架构 -> 02-tool-pick, 03-data-map, 04-talk-link
  骨架 -> 05-skeleton-check, 06-web-frame, 07-server-frame
  交付 -> 08-work-plan, 09-doc-rules
  验收 -> 10-final-check

执行层 00-10：
  00-build-map 编排新项目完整流程
  01-idea-check 明确产品范围
  02-tool-pick 选择技术栈
  03-data-map 设计数据模型
  04-talk-link 定义前后端契约
  05-skeleton-check 选择或创建骨架
  06-web-frame 落地前端骨架
  07-server-frame 落地后端骨架
  08-work-plan 拆分交付计划
  09-doc-rules 同步文档和规则
  10-final-check 做发布前验收
```

## 使用原则

- 新项目默认从 `00-build-map` 进入。
- 已开工但状态混乱的项目先走 `project-rescue-map`。
- `project-rescue-map` 先给五大类摘要，再给 `01-10` 矩阵。
- 五大类用于理解和排序，`00-10` 用于实际补救。
- 不因五大类而重命名、删除、迁移现有 skill。

## 目标路径规则

- 开始写入前先确认 `project-root`。
- work-bench 不存放默认项目产物。
- 前端默认写入目标项目的 `frontend/`。
- 后端默认写入目标项目的 `backend/`。
- 复制骨架时只把候选骨架内容复制到目标目录，禁止形成 `frontend/apps/<candidate>` 或 `backend/apps/<candidate>` 这类嵌套产物路径。
