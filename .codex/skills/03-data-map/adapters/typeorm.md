# TypeORM 适配器

## 1. 适用场景

用户使用 Node.js / TypeScript / NestJS，并通过 TypeORM Entity 和 Migration 管理数据库。

## 2. 官方工作流内化原则

- `synchronize: true` 在已有生产数据后通常不安全。
- 生产环境应使用 migration 同步 schema 变更。
- Migration 是包含更新数据库 schema SQL 的单文件。

## 3. 输出要求

必须输出：

- Entity 文件。
- Migration 文件。
- DataSource 配置注意事项。
- 运行命令，例如 `typeorm migration:generate` / `migration:run`。
- 生产环境 `synchronize: false`。

## 4. Entity 设计规范

- 使用 `@PrimaryGeneratedColumn('increment')` 或 UUID。
- 时间字段：`@CreateDateColumn`、`@UpdateDateColumn`。
- 软删除：`@DeleteDateColumn`。
- 金额：`bigint` 存最小单位；若用 decimal，注意 JS 读取精度，建议使用 string/Decimal 库处理。
- 状态：enum 或 varchar；数据库 enum 迁移要谨慎。
- 外键：显式 relation + join column。
- 多对多有业务属性时，不用 `@ManyToMany` 隐式表，建立显式中间 Entity。

## 5. 示例

```ts
@Entity('orders')
@Index(['userId', 'createdAt'])
@Index(['status', 'createdAt'])
export class Order {
  @PrimaryGeneratedColumn('increment', { type: 'bigint' })
  id!: string;

  @Column({ name: 'user_id', type: 'bigint' })
  userId!: string;

  @ManyToOne(() => User, user => user.orders, { onDelete: 'RESTRICT' })
  @JoinColumn({ name: 'user_id' })
  user!: User;

  @Column({ name: 'order_no', type: 'varchar', length: 64, unique: true })
  orderNo!: string;

  @Column({ type: 'varchar', length: 32, default: 'pending' })
  status!: 'pending' | 'paid' | 'cancelled';

  @Column({ name: 'total_amount_cents', type: 'bigint' })
  totalAmountCents!: string;

  @CreateDateColumn({ name: 'created_at' })
  createdAt!: Date;

  @UpdateDateColumn({ name: 'updated_at' })
  updatedAt!: Date;

  @DeleteDateColumn({ name: 'deleted_at', nullable: true })
  deletedAt?: Date;
}
```

## 6. 生产注意事项

- `synchronize` 必须关闭。
- 自动生成 migration 后必须审查 SQL。
- 不要让应用启动时自动执行高风险 migration，除非团队明确采用该流程并有锁/幂等/失败处理。
- 删除字段、修改字段类型需要 expand-contract。
