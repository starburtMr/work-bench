# Repo Scan Prompt

```text
使用 project-rescue-map 的 Standard Rescue Audit 模式扫描当前 repo。

要求：
- 先读取最近的 AGENTS/Claude/README/docs index。
- 建立 evidence ledger，给每个判断标 E0-E5。
- 先判断项目阶段和风险适用性，再跑 STOP/CONTAIN/CONTINUE 止血门。
- 按 01-10 work-bench 阶段输出缺口矩阵。
- 额外输出横向健康扫描：产品、技术、架构、数据、API、前端、后端、质量、安全、交付、文档。
- 找出 README/scripts、docs/code、API/front/backend、schema/migration、CI/local 命令之间的冲突。
- 只给阶段级补救路线图，不修改代码。
- 未运行的命令必须写明未运行，不能伪造结果。
```
