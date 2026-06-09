# Rails Active Record 适配器

## 1. 适用场景

用户使用 Ruby on Rails，希望通过 Active Record Migration 管理数据库结构。

## 2. 官方工作流内化原则

- Rails Migration 是可复现地演进数据库 schema 的方式。
- 每个 migration 是数据库时间线上的一个版本。
- Migration 文件应提交 Git。

## 3. 输出要求

必须输出：

- `db/migrate/<timestamp>_create_xxx.rb`。
- Model association 说明。
- `bin/rails db:migrate`。
- rollback 或前滚策略。

## 4. 字段规范

- 主键：Rails 默认 `id`。
- 外键：`t.references :user, null: false, foreign_key: true`。
- 金额：`bigint :amount_cents` 或 `decimal :amount, precision: 12, scale: 2`。
- 时间：Rails 默认 `t.timestamps`。
- 软删除：`t.datetime :deleted_at`。
- 状态：string/integer + model enum；注意可读性和迁移稳定性。

## 5. 示例

```ruby
class CreateOrders < ActiveRecord::Migration[8.0]
  def change
    create_table :orders do |t|
      t.references :user, null: false, foreign_key: { on_delete: :restrict }
      t.string :order_no, null: false
      t.string :status, null: false, default: "pending"
      t.bigint :total_amount_cents, null: false
      t.string :currency, null: false, default: "CNY", limit: 3
      t.datetime :paid_at
      t.datetime :deleted_at
      t.timestamps
    end

    add_index :orders, :order_no, unique: true
    add_index :orders, [:user_id, :created_at]
    add_index :orders, [:status, :created_at]
  end
end
```

## 6. 生产注意事项

- 大表新增字段、索引、约束要考虑在线迁移策略。
- 删除字段前先让应用停止读取该字段。
- 不可逆 migration 使用 `up` / `down` 明确写出，或说明 irreversible。
