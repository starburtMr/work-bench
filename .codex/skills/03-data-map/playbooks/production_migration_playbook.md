# 生产数据库迁移执行手册

## 1. 原则

生产数据库迁移不是“执行一下命令”。任何变更都要经历：设计、审查、备份、staging 验证、生产执行、监控、验收。

## 2. 低风险变更

通常包括：

- 新增表。
- 新增 nullable 字段。
- 新增不影响旧逻辑的索引。

处理：

1. 生成 migration。
2. 审查 SQL。
3. staging 执行。
4. 生产执行。
5. 验收。

## 3. 高风险变更

包括：

- 删除字段/表。
- 修改字段类型。
- nullable 改 not null。
- 新增唯一约束。
- 大表新增索引。
- 新增外键。

处理：

使用 expand-contract：

1. 新增兼容字段或新表。
2. 应用开始双写。
3. 回填历史数据。
4. 校验一致性。
5. 切换读取来源。
6. 观察稳定。
7. 删除旧字段/旧表。

## 4. 回填脚本要求

- 幂等。
- 可断点续跑。
- 分批处理。
- 有进度日志。
- 有失败重试。
- 有校验 SQL。

## 5. 验收 SQL 示例

```sql
-- 检查空值
SELECT COUNT(*) FROM target_table WHERE new_column IS NULL;

-- 检查重复
SELECT business_key, COUNT(*)
FROM target_table
GROUP BY business_key
HAVING COUNT(*) > 1;

-- 检查孤儿外键
SELECT child.*
FROM child
LEFT JOIN parent ON child.parent_id = parent.id
WHERE parent.id IS NULL;
```
