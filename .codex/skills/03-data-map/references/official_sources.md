# 官方资料来源与内化原则

> 访问日期：2026-06-09。以下资料用于 v3 版本的工程规则提炼。使用 Skill 时，如用户指定某个框架版本，应优先查看对应版本官方文档。

## 数据库官方资料

### PostgreSQL

- Constraints: https://www.postgresql.org/docs/current/ddl-constraints.html
- CREATE INDEX: https://www.postgresql.org/docs/current/sql-createindex.html
- Numeric Types: https://www.postgresql.org/docs/current/datatype-numeric.html
- Identity Columns: https://www.postgresql.org/docs/current/ddl-identity-columns.html

内化原则：

- 约束用于让数据库拒绝违反规则的数据，不只依赖应用层校验。
- 索引用于提升查询性能，但不合适的索引会拖慢写入或整体性能。
- 金额应使用整数最小单位或精确数值类型，不使用浮点数。
- 自动生成主键可使用 identity column，但唯一性仍由 PRIMARY KEY / UNIQUE 约束保障。

### MySQL

- Foreign Key Constraints: https://dev.mysql.com/doc/refman/8.4/en/create-table-foreign-keys.html
- CREATE TABLE: https://dev.mysql.com/doc/en/create-table.html
- ALTER TABLE: https://dev.mysql.com/doc/en/alter-table.html

内化原则：

- 外键关系由子表字段引用父表字段，帮助保持相关数据一致。
- 必须明确 `ON DELETE` / `ON UPDATE` 行为。
- 大表 ALTER 和外键变更要评估锁与执行风险。

### SQLite

- Appropriate Uses For SQLite: https://sqlite.org/whentouse.html
- SQLite Documentation: https://sqlite.org/docs.html

内化原则：

- SQLite 非常适合本地、嵌入式、轻量应用。
- 当数据和应用跨网络分离，或存在高写并发要求时，通常应考虑 client/server 数据库。

### Redis

- Redis Docs: https://redis.io/docs/latest/

内化原则：

- Redis 可作为 cache、primary、vector 或 custom database，但常规业务系统不要默认把 Redis 当关系型主库替代品。
- 首版只有在明确缓存、验证码、登录态、限流、队列、热点数据、实时流等需求时引入 Redis。

## ORM / Migration 官方资料

### Prisma

- Prisma Migrate Overview: https://www.prisma.io/docs/orm/prisma-migrate
- Deploying database changes with Prisma Migrate: https://www.prisma.io/docs/orm/prisma-client/deployment/deploy-database-changes-with-prisma-migrate
- Prototyping your schema: https://www.prisma.io/docs/orm/prisma-migrate/workflows/prototyping-your-schema
- Prisma Migrate CLI: https://www.prisma.io/docs/cli/migrate

内化原则：

- Prisma Migrate 会生成 SQL migration 历史。
- 开发与生产流程分开：本地生成 migration，生产/CI 使用 `migrate deploy`。
- `db push` 适合原型，不是默认生产流程。

### Django

- Migrations: https://docs.djangoproject.com/en/6.0/topics/migrations/
- Migration Operations: https://docs.djangoproject.com/en/6.0/ref/migration-operations/

内化原则：

- Django Migration 把 Model 变更传播到数据库 schema。
- `makemigrations` 生成 migration，`migrate` 应用 migration，`sqlmigrate` 可审查 SQL。
- Migration 可理解为数据库 schema 的版本控制系统。

### Laravel

- Database Migrations: https://laravel.com/docs/13.x/migrations

内化原则：

- Laravel Schema facade 提供跨数据库的表和字段创建/修改能力。
- Migration 文件是团队协作的数据库结构版本文件，应提交 Git。

### Rails

- Active Record Migrations: https://guides.rubyonrails.org/active_record_migrations.html
- Rails API ActiveRecord::Migration: https://api.rubyonrails.org/classes/ActiveRecord/Migration.html

内化原则：

- Rails Migration 以可复现方式演进 schema。
- 每个 migration 是数据库 schema 时间线上的一个版本。

### TypeORM

- How migrations work: https://typeorm.io/docs/migrations/why/
- FAQ synchronize: https://typeorm.io/docs/help/faq/

内化原则：

- 生产环境已有数据后，`synchronize: true` 通常不安全。
- 应使用 migration 同步模型变化。

### Drizzle

- Drizzle Kit Overview: https://orm.drizzle.team/docs/kit-overview
- Drizzle Migrations: https://orm.drizzle.team/docs/migrations
- drizzle-kit generate: https://orm.drizzle.team/docs/drizzle-kit-generate
- drizzle-kit migrate: https://orm.drizzle.team/docs/drizzle-kit-migrate
- drizzle-kit push: https://orm.drizzle.team/docs/drizzle-kit-push
- drizzle-kit pull: https://orm.drizzle.team/docs/drizzle-kit-pull

内化原则：

- `generate` 生成 SQL migration 文件。
- `migrate` 应用 migration。
- `pull` 从已有数据库 introspect。
- `push` 直接应用 schema diff，适合原型/低风险，不作为默认生产流程。

### SQLAlchemy / Alembic

- Alembic Tutorial: https://alembic.sqlalchemy.org/en/latest/tutorial.html
- Alembic Autogenerate: https://alembic.sqlalchemy.org/en/latest/autogenerate.html

内化原则：

- Alembic migration environment 应随应用源码维护。
- autogenerate 生成候选 migration 后必须人工审查。

### EF Core

- EF Core Migrations Overview: https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/
- EF Core tools reference: https://learn.microsoft.com/en-us/ef/core/cli/dotnet

内化原则：

- EF Core Migration 用于随着模型演进管理数据库 schema。
- CLI 工具可创建、应用 migration，也可用于生成/审查脚本。

## 前端框架官方资料

### Next.js

- App Router docs: https://nextjs.org/docs/app
- Layouts and Pages: https://nextjs.org/docs/app/getting-started/layouts-and-pages
- File conventions: https://nextjs.org/docs/app/api-reference/file-conventions

内化原则：

- 文件系统路由可作为页面和用户流程入口证据。
- `page`、`layout`、动态段、`route` 文件能提示页面、资源和 API 操作。

### React Router

- Route Object: https://reactrouter.com/start/data/route-object
- Framework Routing: https://reactrouter.com/start/framework/routing
- Data Loading: https://reactrouter.com/start/framework/data-loading

内化原则：

- route object / route module 暴露 data loading、actions、revalidation 等信息。
- loader 是读取线索，action 是写入线索。

### SvelteKit

- Routing: https://svelte.dev/docs/kit/routing

内化原则：

- 文件系统路由、`+page`、`+page.server`、`+server` 是页面和接口证据。

## 安全官方资料

### OWASP

- Password Storage Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- Cryptographic Storage Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html
- Logging Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html

内化原则：

- 密码不能明文存储，应使用现代慢哈希。
- 敏感数据能不存就不存，需要存时根据威胁模型选择加密层级。
- 日志不要直接记录密码、访问令牌、密钥、数据库连接串、银行卡等敏感数据。
