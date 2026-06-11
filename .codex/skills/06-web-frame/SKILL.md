---
name: web-frame
description: "Create or normalize a maintainable frontend skeleton with routing, design tokens, component rules, API client boundaries, and quality gates. Use when starting or repairing a frontend base."
---

# 前端工程骨架与组件治理 Skill


## 1. 在完整开发工作流中的位置

- 阶段编号：`06`
- 阶段名称：前端骨架 / 页面与组件规则冻结
- 总控入口：[`build-map`](../00-build-map/SKILL.md)
- 本阶段目标：建立可持续迭代的前端工程结构，让后续 AI 写页面时受目录、组件、样式、接口和质量规则约束。

## 2. 何时启用

- 需要从 0 到 1 搭建前端骨架。
- 已有前端项目被 AI 写乱，需要统一目录、组件、样式、接口规则。
- 已经通过 `skeleton-check` 选定了前端候选骨架或 create 路径。
- 需要为后续页面开发先建立可维护的前端工程基线。

## 3. 上游输入契约

本 skill 不应孤立执行。除非用户明确要求单独使用，否则应优先读取或生成以下输入：

- `<project-root>/docs/product/v1-mvp-scope.md` 与用户路径。
- `<project-root>/docs/architecture/tech-stack-decision.md`。
- `<project-root>/docs/api/api-contract-source-of-truth.md` 或 OpenAPI / 接口草案。
- `<project-root>/docs/product/bootstrap-targets.md` 与 `<project-root>/docs/skeleton/frontend-selection.md`。
- 设计风格、页面清单、组件库约束、已有项目目录和 package 信息。

## 4. 下游输出契约

本 skill 必须把结果沉淀成可被后续 skill 直接消费的交付物：

- `<project-root>/docs/frontend/frontend-blueprint.md`：前端蓝图。
- `<project-root>/docs/frontend/architecture-decision-record.md`：前端 ADR。
- `<project-root>/docs/frontend/project-structure.md`：目录责任与模块边界。
- `<project-root>/docs/frontend/design-system-tokens.md`：Token、主题、样式约束。
- `<project-root>/docs/frontend/component-governance.md`：组件分层、复用和抽象规则。
- `<project-root>/docs/frontend/page-specs.md`：V1 页面规格。
- `<project-root>/docs/frontend/api-client-contract.md`：API Client、Mock、错误处理、类型生成规则。
- `<project-root>/docs/frontend/ai-guardrails.md` 与 `<project-root>/docs/frontend/quality-gates.md`。

## 5. 与其他 skill 的引用关系

### 5.1 上游 skill

- [`idea-check`](../01-idea-check/SKILL.md)
- [`tool-pick`](../02-tool-pick/SKILL.md)
- [`talk-link`](../04-talk-link/SKILL.md)
- [`skeleton-check`](../05-skeleton-check/SKILL.md)

### 5.2 下游 skill

- [`work-plan`](../08-work-plan/SKILL.md)
- [`doc-rules`](../09-doc-rules/SKILL.md)
- [`final-check`](../10-final-check/SKILL.md)

### 5.3 交接载荷

交给下游时，至少携带以下信息：

- 前端蓝图、目录结构、页面规格。
- 设计 Token、组件治理和样式规则。
- API Client 契约、Mock 策略、错误处理约定。
- 前端质量命令、构建/测试/类型检查要求。
- 后续 Agent 不得违反的前端 guardrails。

## 6. 本阶段不可违反的硬规则

1. 先骨架、后页面；不得把本 skill 用成一次性 UI 生成器。
2. 不得擅自换技术栈、组件库、包管理器或路由方案。
3. 接口调用必须走统一 API Client，不得散落 fetch/axios。
4. 样式必须受 Token 和组件库主题约束，不得随意硬编码。
5. 重复 UI 达到抽象条件时必须进入组件治理。
6. 已有项目只能增量治理，不能无计划大重构。

## 7. 阶段完成门禁

- [ ] 前端技术栈与技术选型文档一致。
- [ ] 目录结构、路由、状态、接口、样式、组件边界清晰。
- [ ] 至少覆盖 V1 核心页面规格和数据需求。
- [ ] API Client、Mock、错误处理和类型策略明确。
- [ ] 设计 Token 和组件治理规则可落盘执行。
- [ ] 质量命令、检查清单和 AI guardrails 已生成。

## 8. 工作模式补充

本 skill 在 frontend delivery target 中工作，默认是 `<project-root>/frontend`。它不直接绕过 API 契约写死数据结构。若接口或页面数据不清，回到 `talk-link` 或 `idea-check`。

如果本次复用骨架，必须使用 `skeleton-check` 输出的候选 `source` 和 `path`。候选来源可以是用户全局骨架库 `<codex-home>/work-bench/frontend/apps`，也可以是插件内置骨架库 `frontend/apps`；同名候选以 `user-global` 为准。

如果本次创建可复用前端骨架，必须注册到 `<codex-home>/work-bench/frontend/apps/<skeleton-name>/` 并更新用户 registry。不要把新骨架写入插件安装缓存目录；只有维护插件内置资产时才修改 `frontend/apps`。

如果这个新增、更新、文档调整、删除或重命名后的前端骨架已经完整，并且要合入 work-bench 仓库作为插件内置骨架，必须运行 `scripts/work_bench_skeletons.py change-pr --kind frontend ...` 创建到 `skeleton-inbox` 的 PR。`change-pr` 会在贡献 clone 中更新 `frontend/apps` 与 `frontend/README.md`，生成中文 PR 说明并执行安全检查；不要直接推插件发布分支。

## 9. 推荐落盘位置

- 阶段真源文档：`<project-root>/docs/`
- 阶段决策记录：`<project-root>/docs/decisions/`
- 阶段检查清单：`<project-root>/docs/checklists/`
- 面向 Agent 的长期约束：`<project-root>/AGENTS.md` 或 `<project-root>/docs/agent-rules/`

## 10. 继承自原 skill 的详细规则库

> 以下内容来自原始 skill，已作为新版 skill 的细节规则保留。若出现旧 skill 名称、旧版本号或旧目录名，以新版 front matter 的 `name` 与本文件第 1-7 节为准。

## Frontend Skeleton Architect Vibe Coding Skill v2

### 0. Skill 使命

本 Skill 的目标不是“帮用户一次性生成很多页面”，而是先建立一套可长期约束 AI 的前端骨架：

- 明确项目场景：Web、APP、小程序、跨端、桌面端、硬件 GUI、车机、工业屏。
- 明确设计语言：视觉调性、信息密度、颜色、字体、间距、圆角、阴影、动效、响应式。
- 明确技术路径：框架、构建工具、路由、状态、接口、测试、部署、包管理器。
- 明确组件治理：成熟组件库优先，重复 UI 必须抽象，组件边界清晰。
- 明确目录边界：页面、模块、组件、接口、样式、工具、类型、测试各归其位。
- 明确接口契约：统一 API Client、统一错误结构、Mock 策略、OpenAPI 草案。
- 如果 `skeleton-check` 选择 `create`，先把新候选骨架注册进 `<codex-home>/work-bench/frontend/apps` 并更新用户 registry，再把它复制/落地到 frontend delivery target。只有维护插件内置资产时才修改 `frontend/apps` 和 `frontend/README.md`。
- 如果要把该前端骨架作为插件内置资产发布，使用 `scripts/work_bench_skeletons.py change-pr` 向 `skeleton-inbox` 发起 PR，覆盖 add/update/docs/remove/rename，不直接修改插件缓存或发布分支。
- 明确 AI 约束：后续 Vibe Coding 不能擅自换栈、乱建目录、绕过 Token、复制组件、散落接口。

一句话：**先定规则，再让 AI 进场；把 AI 从“自由艺术家”变成“守规工程师”。**

---

### 1. 何时启用本 Skill

当用户提出以下任一需求时启用：

- “帮我从 0 到 1 搭一个前端骨架 / 项目架构 / 页面规范”。
- “我想让后续 Vibe Coding 不要写乱”。
- “帮我确定前端框架、组件库、目录结构、样式系统、API 规范”。
- “帮我把已有项目整理规范，防止后面 AI 改乱”。
- “帮我设计页面规范、接口规范、组件规范、样式 Token”。
- “做 Web / APP / 小程序 / 跨端 / 硬件 GUI 的前端方案”。

不要把本 Skill 用成单页 UI 生成器。它的第一职责是**架构定规矩**。

---

### 2. 两种工作模式

#### 模式 A：从 0 到 1 新项目骨架

适用于尚未开始或刚开始的项目。目标是：

1. 明确需求边界。
2. 选择成熟技术组合。
3. 输出前端蓝图。
4. 生成可落地的目录、Token、组件、API 和 AI 约束文档。
5. 再进入代码骨架或页面原型。

#### 模式 B：已有项目规范化 / 优化 / 防失控

适用于已经有代码或页面的项目。目标是：

1. 诊断已有技术栈、目录、依赖、组件、样式、接口、路由、状态、测试。
2. 找出风格割裂、组件重复、硬编码、接口散落、模块混杂等问题。
3. 输出目标规范和迁移计划。
4. 把规范落盘为文档和检查清单。
5. 后续按模块小步改造，不做无计划大重构。

---

### 3. 最高优先级原则

#### 3.1 不清楚关键方向时必须问

遇到以下缺失信息，不要直接生成完整项目：

- 不知道是新项目还是已有项目。
- 不知道目标平台：Web、APP、小程序、跨端、硬件 GUI。
- 不知道项目类型：后台、SaaS、内容、电商、AI 工具、官网、数据看板等。
- 不知道第一阶段页面和核心流程。
- 不知道设计风格或参考对象。
- 不知道是否有指定技术栈 / 组件库 / 团队约束。
- 不知道后端接口是否存在、REST/GraphQL/RPC/Mock。
- 已有项目没有目录结构、`package.json` 或代码片段。

允许用户说“你帮我默认选”。如果用户授权默认选择，可以继续，但必须写明：**默认假设、选择理由、后续可替换点、潜在风险**。

#### 3.2 成熟方案优先

不要让 AI 发明框架、组件库、目录结构或样式系统。优先使用官方推荐脚手架、成熟框架、成熟组件库和常见工程实践。

必须分清：

- **框架 / 元框架**：React、Vue、Next.js、Nuxt、Angular、Astro、SvelteKit、Expo、Taro、uni-app。
- **构建工具**：Vite、框架内置构建、Angular CLI、Expo CLI 等。
- **UI 组件库**：Ant Design、Element Plus、Naive UI、MUI、Vant、Nut UI、Radix UI、Headless UI、shadcn/ui。
- **样式系统**：CSS Variables、Tailwind `@theme`、CSS Modules、Sass、组件库主题系统。
- **路由**：Next App Router、React Router、Vue Router、Nuxt pages、Angular Router、Taro/uni-app 页面配置。
- **状态**：服务端状态、客户端状态、表单状态、URL 状态必须分开判断。
- **接口契约**：OpenAPI / 手写 API_CONTRACTS / Mock。

#### 3.2.1 Context7 优先的官方文档依据规则

涉及框架、组件库、CLI、版本行为、路由约定、样式系统、API Client、Mock、测试或质量工具时，不得凭记忆写规则、命令或配置。应优先使用 Context7 查询当前官方文档，再创建或优化前端骨架。

标准流程：

```bash
npx ctx7@latest library <官方库名> "<当前前端骨架问题>"
npx ctx7@latest docs <library-id> "<当前前端骨架问题>"
```

适用对象包括但不限于 React、Vite、Next.js、Vue、Nuxt、Angular、SvelteKit、Astro、Expo、Taro、uni-app、Tailwind CSS、shadcn/ui、Ant Design、MUI、Element Plus、Naive UI、TanStack Query、MSW、Vitest、Testing Library、Playwright、ESLint、Prettier。

如果 Context7 不可用、限额不足、查不到对应库或结果不足以支撑决策，可以降级到以下官方或一手来源，并记录降级原因：

1. 官方文档站，包括 `/llms.txt` 或 `/llms-full.txt`。
2. 官方 GitHub 仓库的 README、docs、examples、release notes。
3. 厂商官方 MCP 文档源。
4. Firecrawl / WebSearch 等抓取或搜索工具，但只采用官方或一手来源。

如果项目已经固定技术栈，Context7 用于验证当前官方脚手架、目录、配置和骨架约定，不得借机重开无关选型。查询时不得包含 API Key、Token、数据库连接串、私有内网地址、客户数据或任何带凭证的配置。

当文档依据影响架构、命令、配置或质量门禁时，必须把依据摘要写入前端交付物，例如：

- `docs/frontend/frontend-blueprint.md`
- `docs/frontend/architecture-decision-record.md`
- `docs/frontend/quality-gates.md`
- `docs/frontend/ai-guardrails.md`

#### 3.3 先骨架，后页面

禁止一上来横推一堆页面。标准顺序是：

1. 模式判断。
2. 需求澄清。
3. 技术选型。
4. 设计风格与 Token。
5. 页面地图与路由。
6. 目录结构与模块边界。
7. 组件治理。
8. API 契约与 Mock。
9. 质量门禁。
10. 骨架实施计划。
11. 验收通过后再生成页面。

#### 3.4 规则必须落盘

所有关键规则必须写成项目文件，而不是只停留在聊天记录里。至少生成：

```text
docs/
  FRONTEND_BLUEPRINT.md
  AI_GUARDRAILS.md
  PROJECT_STRUCTURE.md
  COMPONENT_GOVERNANCE.md
  API_CONTRACTS.md
  QUALITY_GATES.md
src/
  styles/tokens.css 或 tokens.ts
```

若使用 Tailwind，必须说明 Token 如何进入 `@theme`。若使用组件库主题系统，必须说明 Token 与组件库主题变量如何映射。

---

### 4. 第一轮交互协议

#### 4.1 先判断模式

如果用户没说明模式，先问：

```md
我先判断这个需求需要进入前端骨架模式。请确认：

1. 这是【新项目从 0 到 1】还是【已有项目规范化优化】？
2. 目标平台是 Web、APP、小程序、跨端，还是硬件 GUI？
3. 项目类型是什么：管理后台、SaaS、内容社区、电商、AI 工具、官网、数据看板，还是其他？
```

#### 4.2 新项目最小澄清问题

如果用户要快速开始，最多先问 8 个关键问题：

```md
为了避免后续 AI 写乱，我需要先确认 8 个关键点：

1. 目标平台：Web / APP / 小程序 / 跨端 / 硬件 GUI？
2. 项目类型：后台 / SaaS / 内容 / 电商 / AI 工具 / 官网 / 数据看板？
3. 第一阶段必须有哪些页面？
4. 用户角色有哪些？不同角色权限是否不同？
5. 设计风格：企业后台、SaaS 极简、科技感、内容型、年轻化、商务，还是有参考产品？
6. 是否指定框架或组件库？没有的话是否允许我推荐默认组合？
7. 后端接口状态：已有接口 / 正在开发 / 暂无接口先 Mock？
8. 是否需要响应式、多语言、暗色模式、主题换肤、权限控制、埋点、无障碍？
```

#### 4.3 已有项目最小澄清问题

```md
为了做规范化优化，请先提供：

1. 项目目录结构，至少到 `src` 下 2–3 层。
2. `package.json` 依赖和 scripts。
3. 当前最大痛点：风格乱、组件重复、目录混乱、样式硬编码、接口散落、性能、测试缺失，还是其他？
4. 是否允许调整目录结构、抽象公共组件、引入或替换组件库？
5. 是否必须保持现有路由、页面路径和业务功能不变？
```

---

### 5. 默认技术组合推荐

当用户没有技术偏好且授权默认选择时，优先给 2–3 套方案，并推荐一套。

#### 5.1 B 端管理后台 / 数据看板

默认推荐：

```text
React + TypeScript + Vite + React Router + Ant Design + TanStack Query + CSS Variables Tokens + Vitest + Playwright
```

适用：后台、CRM、ERP、运营系统、订单管理、数据密集型表格。
理由：组件覆盖完整，表单、表格、弹窗、菜单成熟，适合高信息密度后台。

备选：

```text
Vue + TypeScript + create-vue/Vite + Vue Router + Pinia + Element Plus / Naive UI + CSS Variables Tokens
```

适用：团队熟悉 Vue 或国内中后台生态。

#### 5.2 SaaS / AI 工具 / 创业产品

推荐：

```text
Next.js App Router + TypeScript + shadcn/ui + Tailwind @theme + TanStack Query 或框架数据能力 + Playwright
```

适用：登录、工作台、设置、订阅、营销页、SEO、需要服务端渲染或全栈能力的产品。

备选：

```text
React + Vite + MUI / Ant Design + CSS Variables Tokens
```

适用：纯前端 SPA，后端独立，想快速稳定上线。

#### 5.3 内容型网站 / 官网 / 文档站

推荐：

```text
Astro + TypeScript + Markdown/MDX + CSS Variables/Tailwind + 轻量交互组件
```

适用：内容展示、博客、官网、文档、营销页，强调性能与内容结构。

备选：Next.js / Nuxt，适合需要更强动态能力、会员、服务端逻辑或内容后台。

#### 5.4 移动 H5 / 小程序 / 多端

小程序优先判断平台：

- 只做微信小程序且需要最大平台贴合：微信原生或 Taro。
- React/Vue 团队想复用前端习惯：Taro。
- Vue 团队需要 H5、App、多小程序多端发布：uni-app。
- 移动 H5 UI：Vant / Nut UI。

#### 5.5 原生 APP / React 技术栈

推荐：

```text
Expo + React Native + TypeScript + Expo Router + NativeWind 或组件库 + 统一 Token
```

适用：iOS/Android/部分 Web，共享 React 心智，需要快速启动移动端应用。

---

### 6. 技术选型判断矩阵

每次选择技术栈时，必须回答以下表格：

| 维度 | 必须判断的问题 | 输出要求 |
|---|---|---|
| 目标端 | Web / H5 / 小程序 / APP / 多端 / 硬件 GUI | 不同目标端不能混用代码假设 |
| 渲染需求 | SPA / SSR / SSG / 混合渲染 | 决定 Vite、Next、Nuxt、Astro 等 |
| SEO | 是否需要搜索引擎收录 | 官网/内容更偏 Next/Nuxt/Astro |
| 信息密度 | 表格后台还是内容阅读 | 决定 AntD/Element/MUI/shadcn/Vant |
| 团队熟悉度 | React、Vue、Angular、移动端经验 | 优先团队能维护的栈 |
| 组件需求 | 表格/表单/图表/弹窗/日期/上传 | 决定组件库是否成熟 |
| 跨端能力 | 是否要一套代码多端 | 决定 Taro/uni-app/Expo |
| 主题设计 | 是否需要暗色/换肤/品牌白标 | 决定 Token 与主题架构 |
| 接口状态 | 已有接口 / 需要 Mock / 需要 OpenAPI | 决定 API 层与 Mock 策略 |
| 质量要求 | 类型、测试、Lint、E2E、CI | 决定质量门禁 |

---

### 7. 模式 A 标准工作流：新项目 0 到 1

#### A1. 需求澄清

先收集：平台、类型、角色、页面、流程、风格、技术偏好、接口状态、扩展要求。

#### A2. 输出前端决策记录 ADR

必须说明：

- 为什么选这个框架。
- 为什么选这个组件库。
- 为什么选这个样式系统。
- 为什么这样组织目录。
- 哪些点以后可替换。
- 哪些点一旦开始就不建议随便改。

#### A3. 输出前端蓝图

包含：

1. 项目基本信息。
2. 技术栈表。
3. 设计风格说明。
4. 页面地图。
5. 用户角色与权限矩阵。
6. 路由表。
7. 模块划分。
8. 目录结构。
9. 组件分层与首批组件。
10. Design Token 表。
11. API 契约与 Mock 策略。
12. 状态管理策略。
13. 响应式、多语言、主题、无障碍预留。
14. 质量门禁。
15. 阶段计划。
16. 骨架验收标准。

#### A4. 骨架阶段只做“结构正确”

第一阶段不要追求功能完整，只要做到：

- 项目可安装、可启动、可构建。
- 核心路由可访问。
- 组件库接入成功。
- Token 生效。
- AppShell、PageHeader、EmptyState、ConfirmDialog、Loading、ErrorState 可用。
- API Client、错误结构、Mock 策略可用。
- 规范文档落盘。
- 后续新增页面必须引用页面规格和 AI Guardrails。

---

### 8. 模式 B 标准工作流：已有项目规范化

#### B1. 先诊断，不直接重构

必须先看：

- `package.json`：框架、组件库、样式、状态、测试、构建脚本。
- 目录结构：页面、组件、API、样式是否混放。
- 页面截图或页面文件：风格是否一致。
- 样式：是否散落颜色、px、阴影、圆角。
- 组件：是否复制表格、弹窗、按钮组、筛选栏、状态标签。
- 接口：是否页面内直接 fetch/axios，是否错误处理分散。
- 路由：是否无权限边界，路由和页面职责混乱。
- 状态：是否把服务端状态塞进全局 store。
- 质量：是否缺少 typecheck、lint、format、unit/e2e。

#### B2. 按风险分级

| 风险级别 | 典型问题 | 处理策略 |
|---|---|---|
| P0 | 项目无法启动、构建失败、路由破坏 | 先恢复可运行 |
| P1 | 接口散落、样式硬编码严重、组件重复严重 | 建统一 API 层、Token、组件治理 |
| P2 | 目录边界弱、模块混杂、命名不统一 | 分模块迁移 |
| P3 | 测试不足、文档缺失、主题/多语言未预留 | 补门禁和文档 |

#### B3. 只做增量迁移

禁止无计划一次性大重构。标准迁移顺序：

1. 新建规范文档，不改业务。
2. 建立 Token 与主题入口。
3. 建立 API Client，不立即改所有接口。
4. 抽象最高频组件。
5. 每次迁移一个模块或一个页面族。
6. 每次改造后跑启动、构建、类型、Lint、关键页面验收。

---

### 9. 样式系统规则

#### 9.1 Token 分层

必须区分三层 Token：

| 层级 | 作用 | 示例 |
|---|---|---|
| Base Tokens | 原始设计值 | `--blue-600`, `--gray-100`, `--space-4` |
| Semantic Tokens | 语义用途 | `--color-primary`, `--color-bg-page`, `--color-text-muted` |
| Component Tokens | 组件局部语义 | `--button-primary-bg`, `--card-radius`, `--table-row-hover-bg` |

页面和组件优先使用 Semantic / Component Token，不直接使用 Base Token。

#### 9.2 Token 覆盖范围

至少包含：

- 颜色：主色、文本、背景、边框、成功、警告、危险、信息。
- 字体：字体族、字号、字重、行高、字距。
- 间距：页面、模块、组件、表单、表格、卡片。
- 圆角：按钮、输入框、卡片、弹窗、标签。
- 阴影：卡片、弹窗、浮层。
- 断点：mobile、tablet、desktop、wide。
- 层级：header、dropdown、popover、modal、toast。
- 动效：duration、easing。

#### 9.3 Tailwind 项目规则

若使用 Tailwind，必须：

- 用 `@theme` 定义能生成工具类的 Token。
- 对不需要工具类的运行时变量，可用 `:root`。
- 禁止页面随手堆任意值类，例如大量 `mt-[17px]`、`text-[#123456]`。
- shadcn/ui 项目必须维护 `components.json`、`lib/utils`、`components/ui`、主题变量和组件注册规则。

#### 9.4 组件库主题映射

如果使用 Ant Design、MUI、Element Plus、Naive UI 等组件库，必须定义：

- 品牌主色如何映射到组件库主题。
- 圆角、字体、边框、阴影如何统一。
- 是否允许覆盖组件库样式；若允许，只能在集中主题文件或组件包装层覆盖。
- 禁止在业务页面里散落 `.ant-btn`、`.el-button` 等深度覆盖。

---

### 10. 组件治理规则

#### 10.1 组件分层

| 层级 | 说明 | 存放位置 | 规则 |
|---|---|---|---|
| UI 底座 | 组件库或 headless primitives | `components/ui` 或直接 import | 不重复造轮子 |
| Layout 组件 | AppShell、Sidebar、TopNav、PageLayout | `components/layout` | 全局统一 |
| Feedback 组件 | Loading、EmptyState、ErrorState、ConfirmDialog、Toast | `components/feedback` | 全站统一反馈 |
| Data 组件 | DataTable、SearchFilterBar、Pagination、StatusBadge | `components/data` | 列表页统一 |
| Business 组件 | UserCard、OrderStatus、MoneyText | `components/business` 或模块内 | 复用时抽上来 |
| Module 私有组件 | 只属于一个模块 | `modules/<module>/components` | 禁止跨模块偷用 |

#### 10.2 抽象触发条件

以下任一成立，必须抽象：

- 同类 UI 出现 2 次及以上。
- 同类表格列、筛选栏、分页、状态标签出现 2 次及以上。
- 同类弹窗确认、提交反馈、错误提示出现 2 次及以上。
- 同类详情页区块、描述列表、卡片组出现 2 次及以上。
- 同类接口状态处理反复出现。

#### 10.3 禁止事项

- 禁止复制粘贴整段组件逻辑。
- 禁止组件内部跨模块调用 API。
- 禁止通用组件依赖具体路由。
- 禁止通用组件写死业务文案。
- 禁止绕过 Token 写样式。
- 禁止混用多个完整 UI 组件库，除非有清晰边界和理由。

---

### 11. API 与状态管理规则

#### 11.1 API 契约优先

骨架阶段至少要有 `API_CONTRACTS.md`。中大型项目应考虑 `openapi.yaml` 草案。

每个接口必须说明：

- Method、Path、Auth。
- Query / Params / Body。
- Response。
- Error code。
- 页面加载、空、错误、权限不足、提交中状态。
- Mock 数据示例。

#### 11.2 统一请求层

所有请求必须经过统一请求层，例如：

```text
src/api/client.ts
src/api/errors.ts
src/api/types.ts
src/modules/<module>/api.ts
```

禁止在页面组件里直接散落 `fetch`、`axios` 或平台请求 API。

#### 11.3 状态分类

| 状态类型 | 推荐位置 | 说明 |
|---|---|---|
| 服务端状态 | TanStack Query / 框架数据能力 / API hooks | 列表、详情、远程数据、缓存、刷新 |
| 客户端全局状态 | Zustand / Redux Toolkit / Pinia / Context | 主题、侧栏、用户偏好、跨页面临时状态 |
| 表单状态 | 表单库或组件局部 | 不要塞全局 store |
| URL 状态 | Query string / route params | 筛选、分页、tab、详情 id |
| 权限状态 | Auth module + route guard | 不要写散在按钮里 |

服务端状态和客户端状态不要混为一谈。

---

### 12. 目录结构规则

目录结构必须尊重框架官方约定，再叠加业务模块边界。不要为了统一而破坏框架约定。

#### 12.1 通用 SPA 结构

```text
src/
  main.tsx/main.ts
  app/
    App.tsx/App.vue
    providers.tsx
    router.tsx
  pages/ 或 views/
  modules/
    auth/
      pages/
      components/
      api.ts
      types.ts
      hooks.ts/composables.ts
    users/
  components/
    ui/
    layout/
    feedback/
    data/
    business/
  api/
    client.ts
    errors.ts
    types.ts
    mock.ts
  styles/
    globals.css
    tokens.css
    theme.css
  hooks/ 或 composables/
  utils/
  i18n/
  types/
  tests/
```

#### 12.2 框架目录优先级

- Next.js App Router：`app` 是路由系统；`layout/loading/error/not-found/page/route` 有特殊含义。共享业务代码可放 `src/modules`、`src/components`、`src/lib`，不要把所有业务都塞进 route 文件。
- Nuxt：尊重 `app/pages`、`components`、`composables`、`layouts`、`middleware`、`plugins`、`utils` 等目录。
- Astro：`src/pages` 必须承载路由，`src/components` 放可复用组件，`src/layouts` 放共享页面壳。
- Angular：尊重 Angular workspace、CLI、`src/app` 和项目配置文件；按 feature 或 domain 组织。
- Taro/uni-app：页面配置、平台差异、条件编译和跨端组件限制必须提前写明。
- Expo：按 Expo Router / app 目录或项目模板约定组织，不照搬 Web DOM 假设。

---

### 13. 页面规格规则

每个页面在写代码前必须有页面规格：

```md
# 页面规格：<页面名>

- 路由：
- 访问角色：
- 页面目标：
- 用户从哪里来：
- 用户完成什么动作后离开：
- 所属模块：
- 是否需要登录：

## 页面区域
1. 顶部：标题、说明、主操作。
2. 主体：列表 / 表单 / 卡片 / 图表 / 内容。
3. 反馈：加载、空状态、错误、权限不足、成功提示。

## 组件组成
- Layout：
- 通用组件：
- 业务组件：
- 组件库组件：

## 数据需求
| 字段 | 来源接口 | 展示位置 | 是否后端计算 | 备注 |
|---|---|---|---|---|

## 交互
| 用户动作 | 前端反馈 | 调用接口 | 成功 | 失败 |
|---|---|---|---|---|

## 响应式
- Mobile：
- Tablet：
- Desktop：

## 可访问性
- 表单 label：
- 键盘操作：
- 焦点状态：
- 错误提示是否可读：
```

---

### 14. 质量门禁

骨架阶段至少定义以下命令或替代方案：

```json
{
  "scripts": {
    "dev": "...",
    "build": "...",
    "typecheck": "...",
    "lint": "...",
    "format": "...",
    "test": "...",
    "test:e2e": "..."
  }
}
```

每次 AI 修改代码后，必须说明：

- 修改了哪些文件。
- 影响哪些模块。
- 是否新增依赖。
- 是否新增组件。
- 是否新增 Token。
- 如何启动验证。
- 如何检查页面状态、响应式和组件复用。

---

### 15. 标准输出格式

#### 15.1 当信息不足时

```md
我先判断：这是【模式 A / 模式 B】。

现在有几个关键点会影响前端骨架，不能直接横推页面：
1. ...
2. ...

如果你想快速开始，我可以按以下默认方案继续：
- 技术栈：...
- 组件库：...
- 样式：...
- 接口：...

请确认是否采用默认方案，或补充上述信息。
```

#### 15.2 当信息足够时

```md
我会按【模式 A / 模式 B】输出前端骨架方案。

本次交付包括：
1. 前端决策记录 ADR
2. FRONTEND_BLUEPRINT.md
3. PROJECT_STRUCTURE.md
4. DESIGN_TOKENS.md / tokens.css
5. COMPONENT_GOVERNANCE.md
6. API_CONTRACTS.md
7. AI_GUARDRAILS.md
8. QUALITY_GATES.md
9. 第一阶段骨架实施计划
10. 骨架验收清单
```

---

### 16. 禁止行为

- 禁止没有目标端就生成完整项目。
- 禁止没有设计风格就生成多个页面。
- 禁止没有技术栈就输出可运行代码。
- 禁止让 AI 随机选择组件库。
- 禁止把框架、组件库、样式系统混为一谈。
- 禁止同类 UI 复制粘贴。
- 禁止组件库已有基础组件重复手写。
- 禁止页面内直接请求接口。
- 禁止样式硬编码满天飞。
- 禁止为了一个页面破坏全局规则。
- 禁止把后端业务规则写死在前端页面。
- 禁止已有项目无诊断就大重构。
- 禁止新增依赖不说明理由。
- 禁止后续 Vibe Coding 不引用 `AI_GUARDRAILS.md`。

---

### 17. 合格骨架最终标准

一个合格的前端骨架，必须满足：

- 技术栈明确。
- 目标端明确。
- 设计风格明确。
- 组件库明确。
- 目录边界明确。
- 模块职责明确。
- Token 明确。
- 页面状态明确。
- API 契约明确。
- 路由和权限策略明确。
- 状态管理边界明确。
- 测试和质量门禁明确。
- AI 后续编码约束明确。
- 项目能启动，后续页面能长在同一套规则上。
