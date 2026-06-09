# 框架差异速记

## 一句话原则

- Prisma：`schema.prisma` 是模型入口，migration SQL 必须提交；生产用 `migrate deploy`。
- Django：Model 变更通过 `makemigrations` 打包成 migration，`migrate` 应用。
- Laravel：Migration + Schema facade 管理表结构。
- Rails：Migration 是 schema 时间线上的版本。
- TypeORM：生产禁用 `synchronize: true`，使用 migration。
- Drizzle：推荐 `generate` + SQL 审查 + `migrate`；`push` 只做原型/低风险。
- SQLAlchemy/Alembic：`autogenerate` 只是候选，必须人工审查。
- EF Core：Model/DbContext 生成 migration，生产前可生成 SQL 脚本审查。

## 字段命名差异

| 层 | 推荐 |
|---|---|
| 数据库 | snake_case：`created_at`, `password_hash` |
| JS/TS ORM | camelCase + 映射：`createdAt @map("created_at")` |
| Python/Django | snake_case，与数据库一致或通过 db_column |
| Rails | snake_case |
| C#/EF Core | PascalCase 属性 + Fluent API 映射到 snake_case |

## Migration 风险分级

| 变更 | 风险 | 建议 |
|---|---|---|
| 新增 nullable 字段 | 低 | 可直接迁移 |
| 新增非空字段无默认值 | 高 | 先 nullable，回填，再 not null |
| 删除字段 | 高/阻塞 | 先应用停止读取，再删除 |
| 修改字段类型 | 高 | 新字段 + 回填 + 切换 |
| 新增唯一约束 | 中/高 | 先查重清洗 |
| 新增外键 | 中/高 | 先清理孤儿数据 |
| 大表新增索引 | 中/高 | 评估在线索引/锁表 |
| 重命名字段 | 中/高 | 确认工具是否误判为 drop + add |
