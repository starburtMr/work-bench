# Prisma 适配器

## 1. 适用场景

用户使用 Node.js / TypeScript，并希望以 `schema.prisma` 作为数据模型入口。

## 2. 官方工作流内化原则

- `schema.prisma` 描述数据模型。
- Prisma Migrate 会生成 `.sql` migration 历史。
- 开发环境通常使用 `prisma migrate dev` 创建并应用 migration。
- 生产 / staging 应使用 `prisma migrate deploy` 应用已经提交的 pending migrations。
- `prisma db push` 适合快速原型，不生成 migration 历史；不要作为生产流程。

## 3. 输出要求

必须输出：

- `prisma/schema.prisma`。
- `prisma/migrations/<timestamp_name>/migration.sql` 的核心 SQL 设计或说明。
- migration 执行命令。
- seed / 验收数据。
- 生产部署提醒。

## 4. Prisma 字段规范

- 主键：`id BigInt @id @default(autoincrement())` 或 `String @id @default(uuid())`。
- 时间：`createdAt DateTime @default(now())`，`updatedAt DateTime @updatedAt`。
- 软删除：`deletedAt DateTime?`。
- 金额：`amountCents BigInt` 或 `Decimal @db.Decimal(12, 2)`。
- 状态：`enum` 或 `String` + 应用层枚举。状态变化频繁时谨慎使用数据库 enum。
- 外键：显式 `@relation(fields: [userId], references: [id])`。
- 多对多：有业务属性时必须显式中间 model；不要依赖隐式多对多。

## 5. 命名转换

数据库字段建议小写下划线；Prisma Model 可用 camelCase，并通过 `@map` / `@@map` 映射。

```prisma
model User {
  id           BigInt    @id @default(autoincrement())
  email        String    @unique
  passwordHash String    @map("password_hash")
  createdAt    DateTime  @default(now()) @map("created_at")
  updatedAt    DateTime  @updatedAt @map("updated_at")
  deletedAt    DateTime? @map("deleted_at")

  orders       Order[]

  @@map("users")
}
```

## 6. 生产注意事项

禁止建议：

- 在生产使用 `prisma migrate dev`。
- 在生产使用 `prisma db push` 推结构。
- 删除字段前不做备份和兼容发布。
- 用 `migrate reset` 处理生产问题。

推荐流程：

1. 本地修改 `schema.prisma`。
2. 运行 `prisma migrate dev --name <change>`。
3. 审查生成的 SQL。
4. 提交 `schema.prisma` 和 `prisma/migrations`。
5. staging 执行 `prisma migrate deploy`。
6. 验收。
7. 生产 CI 执行 `prisma migrate deploy`。
