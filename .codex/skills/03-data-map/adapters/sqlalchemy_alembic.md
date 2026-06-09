# SQLAlchemy + Alembic 适配器

## 1. 适用场景

用户使用 Python、SQLAlchemy ORM，并用 Alembic 管理数据库迁移。

## 2. 官方工作流内化原则

- Alembic 用于创建、管理和调用关系型数据库 change management scripts。
- Alembic migration environment 是项目的一部分，应随源码维护。
- `--autogenerate` 会比较数据库当前 schema 与应用 metadata，生成候选 migration；生成后必须人工审查和修改。

## 3. 输出要求

必须输出：

- SQLAlchemy model。
- Alembic revision 草案。
- `alembic revision --autogenerate -m ...`。
- `alembic upgrade head`。
- 数据迁移和回滚策略。

## 4. 字段规范

- 主键：`BigInteger` + identity/sequence，或 UUID。
- 时间：`DateTime(timezone=True)`。
- 金额：`BigInteger` 存最小单位，或 `Numeric(12, 2)`。
- 状态：`String(32)` + check constraint，或 Enum。
- 外键：`ForeignKey(..., ondelete='RESTRICT')`。
- 索引：`Index(...)`。
- 软删除：`deleted_at`。

## 5. 示例

```python
class Order(Base):
    __tablename__ = "orders"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)
    order_no = Column(String(64), nullable=False, unique=True)
    status = Column(String(32), nullable=False, server_default="pending")
    total_amount_cents = Column(BigInteger, nullable=False)
    currency = Column(String(3), nullable=False, server_default="CNY")
    paid_at = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    __table_args__ = (
        Index("orders_user_created_at_idx", "user_id", "created_at"),
        Index("orders_status_created_at_idx", "status", "created_at"),
        CheckConstraint("status in ('pending','paid','cancelled','refunded')", name="orders_status_check"),
    )
```

## 6. 生产注意事项

- autogenerate 不是免审查工具。
- 复杂迁移手写 `upgrade()` / `downgrade()`。
- 数据回填要分批、幂等、可重跑。
- SQLite 迁移可能需要 batch 模式。
