# STACK_DECISION_MATRIX.md

## 1. 场景到技术组合

| 场景 | 默认推荐 | 备选 | 关键理由 | 风险 |
|---|---|---|---|---|
| B 端后台 | React + Vite + Ant Design | Vue + Element Plus / Naive UI | 表格/表单/弹窗成熟 | 风格容易重，需要 Token 控制 |
| SaaS / AI 工具 | Next.js + shadcn/ui + Tailwind | React + Vite + MUI/AntD | 兼顾产品、营销、工作台 | shadcn 需要维护本地组件代码 |
| 内容站 / 官网 | Astro | Next.js / Nuxt | 内容路由和静态性能好 | 动态应用能力需额外设计 |
| Vue 团队后台 | Vue + Vite + Element Plus | Nuxt + Element Plus | 学习成本低，组件生态成熟 | 大型项目需模块边界 |
| 企业大型规范 | Angular | React/Next | CLI/workspace/企业治理强 | 上手成本较高 |
| 移动 H5 | Vue/React + Vant/Nut UI | uni-app/Taro H5 | 移动组件适配好 | PC 复用弱 |
| 小程序 | Taro / uni-app / 原生 |  | 先看团队 React/Vue 和平台数量 | 不要套 Web 组件库 |
| APP | Expo + React Native | Flutter/原生 | React 团队快速移动端 | 不能照搬 Web DOM |
| 多端 | uni-app / Taro | Expo + Web 单独 | 一套代码多端 | 平台差异必须预留 |
| 硬件 GUI / 车机 | 定制技术栈 + 设计 Token + 大屏交互规则 | WebView/Qt/原生 | 受设备输入和分辨率约束 | 不要套普通网页审美 |

## 2. 组件库选择

| 组件库 | 适合 | 不适合 | 注意事项 |
|---|---|---|---|
| Ant Design | React 中后台、数据密集 | 高度个性化 C 端 | 用主题系统统一 |
| Element Plus | Vue 3 中后台 | React 项目 | 与 Vue 生态配合 |
| Naive UI | Vue 3，主题可定制 | 需要固定企业规范的团队需评估 | 主题能力强但需规范 |
| MUI | React，Material 或自定义系统 | 国内后台默认审美可能需调 | 主题体系强 |
| shadcn/ui | SaaS、AI 产品、可控设计系统 | 想即装即用不维护组件源码 | 它不是传统组件库 |
| Radix UI / Headless UI | 自建设计系统、可访问基础组件 | 不想写样式 | 需要设计 Token 和样式工程 |
| Vant / Nut UI | 移动 H5、小程序移动场景 | PC 后台 | 注意平台适配 |

## 3. 状态管理选择

| 问题 | 推荐 | 不推荐 |
|---|---|---|
| 远程列表/详情/缓存/刷新 | TanStack Query / 框架数据能力 | 全部塞进 Redux/Pinia |
| 主题/侧栏/用户偏好 | Zustand/Pinia/Context | API hooks |
| 大型复杂业务事件 | Redux Toolkit / Pinia | 零散 useState |
| 表单 | 组件库 Form / React Hook Form / Vue Form 方案 | 全局 store |
| 分页/筛选 | URL query + Query key | 只放内存导致刷新丢失 |
