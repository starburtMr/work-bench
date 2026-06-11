# 查询与索引设计手册

## 1. 从页面到查询

每个索引必须能对应到一个页面或接口查询。

| 页面/API | WHERE | ORDER BY | LIMIT | 推荐索引 |
|---|---|---|---|---|
| 用户订单列表 | user_id, deleted_at | created_at desc | 20 | (user_id, created_at) 或 partial index |
| 后台订单筛选 | status, created_at range | created_at desc | 50 | (status, created_at) |
| 登录 | email | 无 | 1 | unique(email) |

## 2. 组合索引原则

- 等值过滤字段优先。
- 范围字段通常放在等值字段后。
- 排序字段要结合查询条件设计。
- 不同数据库优化器不同，最终要用执行计划验证。

## 3. 不该加索引的情况

- 数据量极小。
- 字段选择性很低且查询不频繁。
- 高频写入但几乎不按该字段查询。
- 只是“以后可能查”。

## 4. 必须唯一的业务键

- 用户邮箱/手机号：视业务要求唯一。
- 订单号：唯一。
- 支付平台流水号：平台内唯一。
- 租户 slug：唯一。
- 多租户内资源 slug：`(tenant_id, slug)` 唯一。
