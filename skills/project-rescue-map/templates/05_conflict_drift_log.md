# Conflict and Drift Log

> 冲突是当前证据互相矛盾；漂移是真源曾经正确但已被代码或决策改变。

| ID | 类型 | 范围 | 证据 A | 证据 B | 冲突/漂移描述 | 影响 | 风险等级 | 回到 skill | 处理建议 | 状态 |
|---|---|---|---|---|---|---|---|---|---|---|
| DRIFT-001 | README vs scripts | 运行命令 | `README.md` | `package.json` |  |  |  | doc-rules |  | Open |
| DRIFT-002 | API doc vs backend | API | `docs/api/*` | `backend/routes/*` |  |  |  | talk-link |  | Open |
| DRIFT-003 | schema vs migration | 数据 | `schema/*` | `migrations/*` |  |  |  | data-map |  | Open |
| DRIFT-004 | AGENTS vs actual structure | Agent 规则 | `AGENTS.md` | repo tree |  |  |  | doc-rules |  | Open |

## 常见类型

- README vs scripts
- docs vs code
- API doc vs backend route
- API doc vs frontend client
- schema vs migration
- frontend route vs product scope
- CI vs package scripts
- env docs vs code env usage
- AGENTS rules vs actual directories
- dependency decision vs lockfile
- deployment docs vs actual workflow
