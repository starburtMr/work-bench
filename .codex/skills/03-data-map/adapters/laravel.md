# Laravel 适配器

## 1. 适用场景

用户使用 Laravel，希望通过 Migration 和 Eloquent Model 管理数据库。

## 2. 官方工作流内化原则

- Laravel Migration 使用 Schema facade 创建和修改表。
- Migration 是团队协作中的数据库结构版本文件，应提交 Git。
- 迁移文件应该包含 `up()` 和 `down()` 或明确不可逆原因。

## 3. 输出要求

必须输出：

- `database/migrations/<timestamp>_create_xxx_table.php`。
- Eloquent Model 字段/关系说明。
- `php artisan migrate` 命令。
- `php artisan migrate:rollback` 或前滚策略。

## 4. 字段规范

- 主键：`$table->id()`。
- UUID：`$table->uuid('id')->primary()`。
- 时间：`$table->timestamps()`。
- 软删除：`$table->softDeletes()`。
- 金额：`$table->unsignedBigInteger('amount_cents')` 或 `$table->decimal('amount', 12, 2)`。
- 状态：`$table->string('status', 32)->default('pending')`，可加 check 视数据库支持。
- 外键：`foreignId()->constrained()->restrictOnDelete()` 等。
- 唯一：`$table->unique([...])`。

## 5. 示例

```php
Schema::create('orders', function (Blueprint $table) {
    $table->id();
    $table->foreignId('user_id')->constrained('users')->restrictOnDelete();
    $table->string('order_no', 64)->unique();
    $table->string('status', 32)->default('pending');
    $table->unsignedBigInteger('total_amount_cents');
    $table->char('currency', 3)->default('CNY');
    $table->timestamp('paid_at')->nullable();
    $table->timestamps();
    $table->softDeletes();

    $table->index(['user_id', 'created_at']);
    $table->index(['status', 'created_at']);
});
```

## 6. 生产注意事项

- 不要直接在生产手改表结构后忘记 Migration。
- 破坏性变更要拆分多次发布。
- `down()` 中删除表/字段可能导致数据丢失，必须提示风险。
- 大表索引、字段类型变更要评估锁和执行时间。
