# 框架输出契约

## 1. 技术栈

- 主库：PostgreSQL / MySQL / SQLite / 其他
- 框架：Prisma / Django / Laravel / Rails / TypeORM / Drizzle / SQLAlchemy-Alembic / EF Core / 原生 SQL
- 迁移目录：
- 环境：development / staging / production

## 2. 必须交付的文件

| 框架 | 文件 | 是否必须 | 说明 |
|---|---|---|---|
| SQL | `schema.sql` / `migrations/*.sql` | 是 | 可审查、可提交 Git |
| Prisma | `schema.prisma` + `prisma/migrations/*/migration.sql` | 是 | 不只给 `db push` |
| Django | `models.py` + `migrations/*.py` | 是 | migration 需可执行 |
| Laravel | `database/migrations/*.php` | 是 | 使用 Schema facade |
| Rails | `db/migrate/*.rb` | 是 | 版本化 schema 时间线 |
| TypeORM | Entity + Migration | 是 | 生产禁用 synchronize |
| Drizzle | `schema.ts` + `drizzle/*.sql` | 是 | 推荐 generate + migrate |
| SQLAlchemy/Alembic | Model + revision file | 是 | autogenerate 后人工审查 |
| EF Core | Entity + DbContext + Migration | 是 | 必要时生成 SQL 脚本审查 |

## 3. 输出必须包含

- 表名与字段名。
- 类型映射。
- 主键、外键、唯一约束、非空、默认值。
- 关系定义。
- 索引定义。
- 软删除字段。
- 金额字段精度。
- 状态枚举。
- 数据迁移/回填逻辑。
- 执行命令。
- 回滚或前滚策略。

## 4. 禁止输出

- 只给 ORM Model，不给 Migration。
- 只给 SQL，不解释业务关系。
- 生产建议使用自动同步。
- 未说明风险就删除字段或改类型。
- 未说明数据回填就把 nullable 改 not null。
