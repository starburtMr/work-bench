# Rescue Handoff Prompt

```text
基于 project-rescue-map 的输出，为下一个 work-bench skill 生成 handoff packet。

字段：
- 推荐调用 skill。
- 调用原因。
- 输入证据列表。
- 必须解决的问题。
- 不得越界事项。
- 通过门槛。
- 待确认问题。
- 风险豁免。

只传递与下一个 skill 相关的信息，不要把整个诊断报告复制过去。
```
