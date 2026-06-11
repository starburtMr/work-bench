# PROJECT_STRUCTURE.md

## 1. 总原则

1. 尊重框架官方目录约定。
2. 页面文件只做组合，不堆复杂业务逻辑。
3. 业务按模块隔离，跨模块复用必须上提到 `components` 或 `shared`。
4. API、类型、样式、测试不得散落在无关目录。
5. 后续 AI 新增文件必须遵守本文件。

## 2. 推荐通用结构

```text
src/
  app/                    # 应用入口、Provider、全局初始化、路由挂载
  pages/                  # 路由页面；Next/Nuxt/Astro 等按框架目录调整
  modules/                # 业务模块，按领域隔离
    auth/
      pages/
      components/
      api.ts
      types.ts
      hooks.ts
      constants.ts
      __tests__/
  components/             # 跨模块复用组件
    ui/                   # shadcn/headless/薄封装 UI 底座
    layout/               # AppShell、Sidebar、TopNav
    feedback/             # Loading、Empty、Error、Confirm
    data/                 # DataTable、FilterBar、StatusBadge
    business/             # 可跨模块业务组件
  api/                    # 全局请求层、错误结构、Mock、OpenAPI client
    client.ts
    errors.ts
    types.ts
    mock.ts
  styles/                 # 全局样式、tokens、主题映射
    tokens.css
    theme.css
    globals.css
  hooks/ 或 composables/   # 跨模块通用逻辑
  utils/                  # 无 UI 纯函数
  i18n/                   # 多语言文案
  types/                  # 全局类型
  tests/                  # E2E 或跨模块测试
```

## 3. React + Vite SPA

```text
src/
  main.tsx
  app/
    App.tsx
    providers.tsx
    router.tsx
  pages/
    HomePage.tsx
    NotFoundPage.tsx
  modules/
    auth/
    users/
    settings/
  components/
  api/
  styles/
  hooks/
  utils/
  types/
```

## 4. Next.js App Router

```text
src/
  app/
    layout.tsx
    page.tsx
    globals.css
    (auth)/
      login/
        page.tsx
    (dashboard)/
      dashboard/
        page.tsx
        loading.tsx
        error.tsx
    not-found.tsx
  modules/
    auth/
    dashboard/
    users/
  components/
    ui/
    layout/
    feedback/
  lib/
    api/
    utils.ts
  styles/
    tokens.css
    theme.css
  types/
```

规则：`app` 主要负责路由、布局和特殊文件；复杂业务逻辑放 `modules` / `lib` / `components`。

## 5. Vue + Vite SPA

```text
src/
  main.ts
  app/
    App.vue
    providers.ts
  router/
    index.ts
  views/
    HomeView.vue
    NotFoundView.vue
  modules/
    auth/
      views/
      components/
      api.ts
      types.ts
      composables.ts
  components/
  api/
  styles/
  composables/
  utils/
  types/
```

## 6. Nuxt

```text
app/
  pages/
  components/
  composables/
  layouts/
  middleware/
  plugins/
  utils/
shared/
  types/
  utils/
server/
  api/
content/
nuxt.config.ts
```

## 7. Astro 内容型项目

```text
src/
  pages/
  layouts/
  components/
  content/
  styles/
  utils/
public/
```

## 8. Taro / 小程序多端

```text
src/
  app.config.ts
  app.ts
  pages/
  modules/
    auth/
    profile/
    orders/
  components/
    common/
    feedback/
  services/
    apiClient.ts
  styles/
    tokens.scss
    mixins.scss
  utils/
  types/
```

## 9. uni-app

```text
src/
  pages.json
  manifest.json
  App.vue
  main.ts
  pages/
  modules/
  components/
  services/
  styles/
  utils/
  types/
```

## 10. 禁止目录行为

- 禁止 `components` 里混入页面。
- 禁止 `pages` 里直接写 API 请求和复杂计算。
- 禁止多个模块互相引用私有组件。
- 禁止样式文件散落到无法追踪的位置。
- 禁止新增 `common2`、`components-new`、`utils-old` 这类临时目录。
