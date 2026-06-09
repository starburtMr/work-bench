# FRAMEWORK_DIRECTORY_BLUEPRINTS.md

## React + Vite + Ant Design

```text
src/
  main.tsx
  app/
    App.tsx
    providers.tsx
    router.tsx
  pages/
    DashboardPage.tsx
    NotFoundPage.tsx
  modules/
    auth/
      pages/LoginPage.tsx
      components/LoginForm.tsx
      api.ts
      types.ts
    users/
      pages/UserListPage.tsx
      components/UserForm.tsx
      api.ts
      types.ts
  components/
    layout/AppShell.tsx
    common/PageHeader.tsx
    feedback/EmptyState.tsx
    feedback/ErrorState.tsx
    feedback/ConfirmDialog.tsx
    data/DataTable.tsx
    data/SearchFilterBar.tsx
  api/client.ts
  api/errors.ts
  styles/tokens.css
  styles/theme.css
  styles/globals.css
  hooks/
  utils/
  types/
```

## Next.js App Router + shadcn/ui

```text
src/
  app/
    layout.tsx
    page.tsx
    globals.css
    (auth)/login/page.tsx
    (dashboard)/dashboard/page.tsx
    (dashboard)/dashboard/loading.tsx
    (dashboard)/dashboard/error.tsx
    not-found.tsx
  components/
    ui/                  # shadcn components
    layout/
    feedback/
    data/
  modules/
    auth/
    dashboard/
    billing/
  lib/
    api/
    utils.ts
  styles/
    tokens.css
    theme.css
```

## Vue + Vite + Element Plus

```text
src/
  main.ts
  app/App.vue
  router/index.ts
  views/
  modules/
    auth/
      views/LoginView.vue
      components/LoginForm.vue
      api.ts
      types.ts
    users/
  components/
    layout/
    feedback/
    data/
  api/
  styles/
  composables/
  utils/
  types/
```

## Nuxt

```text
app/
  app.vue
  pages/
  layouts/
  components/
  composables/
  middleware/
  plugins/
  utils/
shared/
  types/
  utils/
server/
  api/
nuxt.config.ts
```

## Astro

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

## Taro

```text
src/
  app.config.ts
  app.ts
  pages/
  modules/
  components/
  services/apiClient.ts
  styles/tokens.scss
  utils/
  types/
```

## uni-app

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
```
