# COMPONENT_LIBRARY_MATRIX.md

## 1. 基本原则

1. 框架不是组件库；组件库不是框架。
2. 每个项目通常只选一个主组件体系。
3. Headless / shadcn / Radix 这类方案需要更强设计 Token 和组件治理能力。
4. 组件库主题配置必须集中管理。
5. 不要在业务页面中深度覆盖第三方组件样式。

## 2. 选择矩阵

| 组件方案 | 类型 | 适合 | 风险 | Skill 约束 |
|---|---|---|---|---|
| Ant Design | React 完整组件库 | 后台、表格、表单、运营系统 | 默认风格强 | 通过 ConfigProvider / token 统一主题 |
| Element Plus | Vue 3 完整组件库 | Vue 后台 | 风格固定 | 主题和变量集中配置 |
| Naive UI | Vue 3 组件库 | Vue + 主题定制 | 需要统一规范 | 主题 overrides 集中 |
| MUI | React 组件库 | Material、自定义主题、复杂组件 | 国内后台可能需调风格 | 通过 ThemeProvider 管控 |
| shadcn/ui | 代码分发 + 组件构建方式 | SaaS、AI 产品、设计系统 | 需要维护源码 | `components/ui` 必须纳入治理 |
| Radix UI | 可访问 primitives / themes | 自定义设计系统 | 需要自己做样式 | 配合 Token 和样式层 |
| Headless UI | 无样式可访问组件 | Tailwind 自定义 UI | 需要设计能力 | 禁止无规范自由写样式 |
| Vant | 移动 H5 | 移动端表单、列表 | 不适合 PC 后台 | 仅移动场景 |
| Nut UI | 移动端 / 小程序 | 京东生态、小程序/H5 | 平台差异 | 明确目标端 |

## 3. 组件库接入验收

- [ ] 组件库安装并可渲染基础 Button/Input/Modal。
- [ ] 主题主色与 Token 映射。
- [ ] 字体、圆角、边框、阴影策略明确。
- [ ] 暗色模式/主题扩展策略明确。
- [ ] 组件库样式覆盖入口集中。
- [ ] 不混用多个完整组件库。
