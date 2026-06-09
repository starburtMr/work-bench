# Minimal Usage Example

## 用户请求

```text
project-rescue-map /path/to/existing-project
```

## 推荐响应流程

1. 使用 `project-rescue-map`。
2. 明确项目根目录；如果没有给，使用当前目录并标注假设。
3. 读取 `AGENTS.md`、`README.md`、`docs/`、配置、关键代码。
4. 生成 `STOP / CONTAIN / CONTINUE`。
5. 生成 `run-id`。
6. 写入 `docs/rescue/runs/<run-id>/` 并更新 `docs/rescue/index.md`。
7. 输出 01-10 阶段缺口矩阵。
8. 给出阶段级补救路线图。

## 最小输出

```md
# Project Rescue Report

- 止血门：CONTAIN
- 总体结论：条件可继续
- Run ID：20260610-143012-standard
- 报告目录：docs/rescue/runs/20260610-143012-standard/
- 主要阻塞：数据/API 缺真源；README 与脚本冲突
- 推荐补救主线：03 -> 04 -> 09 -> 10
- 下一步调用：data-map
```
