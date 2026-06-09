# Intake Prompt

Use this prompt when the user asks for project rescue diagnosis but gives limited context.

```text
我要使用 project-rescue-map 对这个已开工项目做补救诊断。默认不改代码、不装依赖、不运行会改变环境的命令。

请先确认或假设：
1. 项目根目录。
2. 当前项目阶段：prototype / mvp-dev / staging / production / handoff / unknown。
3. 是否有生产/真实数据。
4. 是否已经实现或计划在 V1 实现支付、权限、隐私或敏感数据能力。
5. 本轮是否要求只聊天不落盘；默认把报告落盘到 docs/rescue/runs/<run-id>/。

如果只能问一个问题，优先问：项目根目录在哪里？如果根目录已知，优先问：当前是否已有真实用户/真实数据/真实密钥或共享环境？
然后读取 README、AGENTS、docs、配置和关键代码，输出 Project Rescue Report。
```
