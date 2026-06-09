# EF Core 适配器

## 1. 适用场景

用户使用 .NET / C# / Entity Framework Core 管理数据库 schema。

## 2. 官方工作流内化原则

- EF Core Migrations 用于随着应用模型变化管理数据库 schema。
- CLI 工具可以创建 migration、应用 migration、生成代码等。
- 多 DbContext 或共享模型时，要明确哪些实体参与 migration，避免冲突。

## 3. 输出要求

必须输出：

- Entity class。
- DbContext Fluent API 配置。
- Migration 命令。
- 生产 SQL 脚本生成建议。

## 4. 字段规范

- 主键：`long Id` 或 `Guid Id`。
- 时间：`DateTimeOffset CreatedAt`。
- 金额：`long AmountCents` 或 `decimal Amount` 并配置 precision。
- 状态：string enum 或枚举转换；注意数据库可读性。
- 软删除：`DeletedAt` + query filter。
- 外键：显式 FK 属性 + navigation。
- 索引：`HasIndex`。

## 5. 示例

```csharp
public class Order
{
    public long Id { get; set; }
    public long UserId { get; set; }
    public User User { get; set; } = null!;
    public string OrderNo { get; set; } = null!;
    public string Status { get; set; } = "pending";
    public long TotalAmountCents { get; set; }
    public string Currency { get; set; } = "CNY";
    public DateTimeOffset? PaidAt { get; set; }
    public DateTimeOffset CreatedAt { get; set; }
    public DateTimeOffset UpdatedAt { get; set; }
    public DateTimeOffset? DeletedAt { get; set; }
}

protected override void OnModelCreating(ModelBuilder modelBuilder)
{
    modelBuilder.Entity<Order>(entity =>
    {
        entity.ToTable("orders");
        entity.HasKey(e => e.Id);
        entity.HasIndex(e => e.OrderNo).IsUnique();
        entity.HasIndex(e => new { e.UserId, e.CreatedAt });
        entity.HasIndex(e => new { e.Status, e.CreatedAt });
        entity.Property(e => e.OrderNo).HasColumnName("order_no").HasMaxLength(64).IsRequired();
        entity.Property(e => e.TotalAmountCents).HasColumnName("total_amount_cents").IsRequired();
        entity.HasOne(e => e.User).WithMany(u => u.Orders).HasForeignKey(e => e.UserId).OnDelete(DeleteBehavior.Restrict);
        entity.HasQueryFilter(e => e.DeletedAt == null);
    });
}
```

## 6. 生产注意事项

- 生成 migration 后审查 C# 和 SQL。
- 生产发布前可生成 SQL script 给 DBA 或 CI 审查。
- 破坏性变更要拆分。
