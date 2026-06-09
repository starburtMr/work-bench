# Security and Supply Chain Rescue Playbook

## 触发信号

- repo 中疑似包含密钥。
- lockfile 冲突或依赖来源不明。
- CI 权限过大或不跑安全/质量命令。
- 生产配置、测试配置、本地配置混在一起。
- 权限/敏感数据/日志有高危缺口。

## 止血顺序

1. 冻结普通开发和发布。
2. 确认是否有真实密钥进入 git 历史；如有，建议轮换密钥，不只删除文件。
3. 确认是否有真实数据可能被诊断命令修改。
4. 记录安全证据，不直接打印敏感值。
5. 把问题分流到 `tool-pick`、`data-map`、`talk-link`、`server-frame`、`doc-rules`、`final-check`。

## 检查维度

| 维度 | 证据 | 风险 | 建议 |
|---|---|---|---|
| Secrets |  |  |  |
| Env config |  |  |  |
| Dependencies |  |  |  |
| Lockfile |  |  |  |
| CI permissions |  |  |  |
| Build provenance |  |  |  |
| AuthN/AuthZ |  |  |  |
| Sensitive data |  |  |  |
| Logging |  |  |  |

## 完成门槛

- 高危 secrets 处理路径明确。
- 生产数据保护边界明确。
- 依赖和构建来源可追溯。
- 安全缺口不再被普通功能开发掩盖。
