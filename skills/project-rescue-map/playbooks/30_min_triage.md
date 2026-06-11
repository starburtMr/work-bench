# Fast Triage Playbook

> 适合用户只想先知道“能不能继续、有没有大雷、第一步补什么”。名称表示轻量分诊模式，不承诺实际耗时。

## 目标

输出最小但可信的结论：`STOP / CONTAIN / CONTINUE`、前三个阻塞、最短补救链路。

## 输入

- 项目根目录。
- README / AGENTS / docs index。
- package/config/CI 文件。
- 关键前后端/data/API 入口。

## 步骤

1. 确认根目录和诊断范围。
2. 读取规则：`AGENTS.md`、`README.md`、`docs/index`。
3. 建立最小证据账本：产品、技术、数据、API、质量、安全。
4. 跑 `Emergency Safety Gate`。
5. 填 01-10 简版矩阵，只标 `通过/部分具备/缺失/冲突/不可验证`。
6. 输出前三个阻塞和最短补救链路。

## 输出

```md
# Fast Project Rescue Triage

- 止血门：STOP / CONTAIN / CONTINUE
- 总体结论：
- 前 3 个阻塞：
- 最短补救链路：
- 本轮未验证：
- 下一步调用 skill：
```

## 不做

- 不展开完整任务池。
- 不修代码。
- 不运行可变命令。
- 不给发布通过结论。
