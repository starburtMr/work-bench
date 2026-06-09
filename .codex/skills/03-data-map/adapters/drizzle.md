# Drizzle ORM 适配器

## 1. 适用场景

用户使用 TypeScript，并希望通过 Drizzle schema 和 Drizzle Kit 管理 SQL migration。

## 2. 官方工作流内化原则

- Drizzle Kit 可基于 Drizzle schema 生成 SQL migration 文件。
- `drizzle-kit generate` 生成 migration。
- `drizzle-kit migrate` 应用已经生成的 migration。
- `drizzle-kit pull` 可从已有数据库 introspect 生成 schema。
- `drizzle-kit push` 会直接把 schema diff 应用到数据库，适合原型或明确低风险场景，不应作为默认生产流程。

## 3. 输出要求

必须输出：

- `src/db/schema.ts`。
- `drizzle.config.ts`。
- 生成的 SQL migration 说明。
- `drizzle-kit generate` / `migrate` 命令。
- 生产不要默认 `push`。

## 4. 字段规范

- PostgreSQL：`bigserial` 或 identity，Drizzle 中按方言定义。
- 时间：`timestamp('created_at', { withTimezone: true }).defaultNow().notNull()`。
- 金额：`bigint('amount_cents', { mode: 'number' | 'bigint' })`，大额建议 `bigint` 模式；或 `numeric`。
- 状态：`varchar` + 应用层类型，或 pgEnum。
- 软删除：`deleted_at` nullable。
- 索引：使用 `index` / `uniqueIndex`。

## 5. 示例

```ts
export const orders = pgTable('orders', {
  id: bigserial('id', { mode: 'bigint' }).primaryKey(),
  userId: bigint('user_id', { mode: 'bigint' }).notNull().references(() => users.id, { onDelete: 'restrict' }),
  orderNo: varchar('order_no', { length: 64 }).notNull().unique(),
  status: varchar('status', { length: 32 }).notNull().default('pending'),
  totalAmountCents: bigint('total_amount_cents', { mode: 'bigint' }).notNull(),
  currency: char('currency', { length: 3 }).notNull().default('CNY'),
  paidAt: timestamp('paid_at', { withTimezone: true }),
  createdAt: timestamp('created_at', { withTimezone: true }).notNull().defaultNow(),
  updatedAt: timestamp('updated_at', { withTimezone: true }).notNull().defaultNow(),
  deletedAt: timestamp('deleted_at', { withTimezone: true }),
}, (table) => ({
  userCreatedIdx: index('orders_user_created_at_idx').on(table.userId, table.createdAt),
  statusCreatedIdx: index('orders_status_created_at_idx').on(table.status, table.createdAt),
}));
```

## 6. 生产注意事项

- 首选 `generate` + 审查 SQL + `migrate`。
- `push` 不生成传统 migration 历史，不适合作为默认生产发布方式。
- 生成 migration 后检查重命名是否被误判为 drop + add。
