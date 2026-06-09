# Django 适配器

## 1. 适用场景

用户使用 Django ORM，希望通过 Model 和 Migration 管理数据库结构。

## 2. 官方工作流内化原则

- Django Migration 用于把 Model 变更传播到数据库 schema。
- `makemigrations` 负责基于 Model 变更创建 migration 文件。
- `migrate` 负责应用或撤销 migration。
- `sqlmigrate` 可展示 migration 对应 SQL，适合审查关键变更。
- migration 可视为数据库 schema 的版本控制系统。

## 3. 输出要求

必须输出：

- `models.py` 设计。
- migration 文件草案或生成说明。
- `python manage.py makemigrations` / `migrate` / `sqlmigrate` 命令。
- admin / serializer 不属于数据库主设计，但可作为补充。

## 4. 字段规范

- 主键：默认 `BigAutoField` 或项目统一 UUID。
- 时间：`auto_now_add=True`、`auto_now=True`，但要说明由应用维护。
- 软删除：`deleted_at = models.DateTimeField(null=True, blank=True)`。
- 金额：`IntegerField` 存最小单位，或 `DecimalField(max_digits=12, decimal_places=2)`。
- 状态：`TextChoices`。
- 外键：`ForeignKey(..., on_delete=...)` 必须明确。
- 多对多：无业务属性可用 `ManyToManyField`；有业务属性必须显式 through model。

## 5. 删除策略映射

- `PROTECT`：保护核心历史数据。
- `CASCADE`：父对象删除时从对象无独立意义。
- `SET_NULL`：保留历史但允许主对象删除。
- `RESTRICT`：阻止有依赖时删除。

## 6. 示例

```python
class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PAID = "paid", "Paid"
        CANCELLED = "cancelled", "Cancelled"

    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT, related_name="orders")
    order_no = models.CharField(max_length=64, unique=True)
    status = models.CharField(max_length=32, choices=Status.choices, default=Status.PENDING)
    total_amount_cents = models.BigIntegerField()
    currency = models.CharField(max_length=3, default="CNY")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "orders"
        indexes = [
            models.Index(fields=["user", "-created_at"]),
            models.Index(fields=["status", "-created_at"]),
        ]
```

## 7. 生产注意事项

- 对大表新增非空字段：先 nullable，加数据回填，再改 not null。
- 对大表新增唯一约束：先清洗重复数据。
- 使用 `sqlmigrate` 审查复杂 migration。
- 数据迁移使用 `RunPython`，必须可重复或说明幂等策略。
