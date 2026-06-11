# Command Evidence Log

> 没有执行的命令不能写成已通过。任何会改变环境的命令都必须先获得用户授权。

| ID | 时间 | 工作目录 | 命令 | 授权类型 | 预期目的 | 结果 | 退出码 | 关键输出摘要 | 是否改变文件 | 证据位置 | 备注 |
|---|---|---|---|---|---|---|---:|---|---|---|---|
| CMD-001 |  |  | `git status --short` | Read-only | 检查未提交变更 |  |  |  | No |  |  |
| CMD-002 |  |  | `npm test` | Local verification | 验证测试 | 未执行 |  |  | Unknown |  | 未授权 / 环境缺失 |

## 命令分类

| 分类 | 示例 | 默认策略 |
|---|---|---|
| 只读文件扫描 | `find`, `ls`, `rg`, `cat`, `sed` | 允许 |
| Git 只读 | `git status`, `git log --oneline` | 允许 |
| 本地验证 | `npm test`, `pnpm build`, `pytest` | 需要注意缓存/产物，按用户授权 |
| 数据库读 | schema inspect / dry-run | 需要授权 |
| 可变命令 | install, migrate, format write, deploy, seed, reset | 默认禁止 |
| 生产/第三方调用 | payment, sms, email, prod API | 默认禁止 |
