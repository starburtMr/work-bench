# COMPONENT_GOVERNANCE.md

## 1. 组件治理目标

减少重复 UI，统一交互和反馈，让后续 AI 写页面时只做组合，不重新发明按钮、弹窗、表格、空状态、筛选栏。

## 2. 组件分层

| 层级 | 说明 | 示例 | 存放位置 |
|---|---|---|---|
| UI 底座 | 组件库或 headless primitives | Button, Input, Modal | `components/ui` 或直接引用组件库 |
| Layout | 全局布局 | AppShell, Sidebar, TopNav, PageLayout | `components/layout` |
| Feedback | 状态反馈 | LoadingState, EmptyState, ErrorState, ConfirmDialog | `components/feedback` |
| Data | 数据展示 | DataTable, SearchFilterBar, StatusBadge, Pagination | `components/data` |
| Business | 跨模块业务组件 | MoneyText, UserAvatar, OrderStatus | `components/business` |
| Module Private | 模块私有组件 | UserForm, OrderTimeline | `modules/<module>/components` |

## 3. 抽象规则

以下任一条件满足，必须抽象组件：

- 同类 UI 出现 2 次及以上。
- 同类表格结构出现 2 次及以上。
- 同类筛选栏出现 2 次及以上。
- 同类弹窗确认出现 2 次及以上。
- 同类状态标签出现 2 次及以上。
- 同类空、错、加载、成功反馈出现 2 次及以上。

## 4. 组件登记表

| 组件 | 层级 | 来源 | 用途 | Props 约束 | 使用位置 | Owner |
|---|---|---|---|---|---|---|
| AppShell | Layout | 自建 | 全局页面壳 | nav, user, children | 全站 |  |
| PageHeader | Layout/Common | 自建 | 页面标题和操作区 | title, description, actions | 页面 |  |
| DataTable | Data | 组件库封装 | 表格/分页/状态 | columns, data, loading, empty | 列表页 |  |
| ConfirmDialog | Feedback | 组件库封装 | 危险操作确认 | open, title, onConfirm | 删除/停用 |  |

## 5. 禁止行为

- 禁止复制粘贴同类组件。
- 禁止通用组件依赖具体业务路由。
- 禁止组件内部调用无关模块 API。
- 禁止绕过 Token 写死颜色和间距。
- 禁止混用多个完整 UI 组件库。
- 禁止通用组件写死中英文文案；文案应从调用方或 i18n 传入。

## 6. 新增组件前检查

新增组件前，AI 必须回答：

1. 是否已有组件库组件可用？
2. 是否已有项目组件可复用？
3. 新组件属于哪一层？
4. 是否跨模块复用？
5. 是否需要新增 Token？
6. 是否需要登记到组件表？
