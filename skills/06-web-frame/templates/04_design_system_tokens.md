# DESIGN_TOKENS.md

## 1. 原则

- Token 是样式系统的唯一源头。
- 页面和组件优先使用语义 Token，不直接写颜色、字号、间距、圆角、阴影。
- Token 文件中允许出现实际值；业务页面中不允许随手硬编码。
- 主题、暗色模式、多语言长度变化、响应式必须预留。

## 2. Token 分层

| 层级 | 命名 | 用途 |
|---|---|---|
| Base | `--blue-600`, `--gray-100`, `--space-4` | 原始设计值 |
| Semantic | `--color-primary`, `--color-bg-page`, `--color-text-muted` | 面向业务语义 |
| Component | `--button-primary-bg`, `--card-radius`, `--table-row-hover-bg` | 组件级控制 |

## 3. CSS Variables 示例

```css
:root {
  /* Base colors */
  --blue-600: #1677ff;
  --green-600: #16a34a;
  --amber-500: #f59e0b;
  --red-600: #dc2626;
  --gray-50: #f9fafb;
  --gray-100: #f3f4f6;
  --gray-200: #e5e7eb;
  --gray-500: #6b7280;
  --gray-900: #111827;

  /* Semantic colors */
  --color-primary: var(--blue-600);
  --color-success: var(--green-600);
  --color-warning: var(--amber-500);
  --color-danger: var(--red-600);
  --color-bg-page: var(--gray-50);
  --color-bg-card: #ffffff;
  --color-text-primary: var(--gray-900);
  --color-text-secondary: var(--gray-500);
  --color-border: var(--gray-200);

  /* Typography */
  --font-family-base: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --font-size-xs: 12px;
  --font-size-sm: 14px;
  --font-size-md: 16px;
  --font-size-lg: 20px;
  --font-size-xl: 24px;
  --line-height-base: 1.5;

  /* Spacing */
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-3: 12px;
  --spacing-4: 16px;
  --spacing-6: 24px;
  --spacing-8: 32px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;

  /* Shadow */
  --shadow-card: 0 4px 16px rgba(15, 23, 42, 0.08);
  --shadow-modal: 0 16px 48px rgba(15, 23, 42, 0.18);

  /* Breakpoints */
  --breakpoint-mobile: 480px;
  --breakpoint-tablet: 768px;
  --breakpoint-desktop: 1024px;
  --breakpoint-wide: 1440px;

  /* Z-index */
  --z-header: 100;
  --z-dropdown: 1000;
  --z-modal: 2000;
  --z-toast: 3000;

  /* Motion */
  --duration-fast: 120ms;
  --duration-normal: 200ms;
  --duration-slow: 320ms;
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);
}

[data-theme="dark"] {
  --color-bg-page: #0f172a;
  --color-bg-card: #111827;
  --color-text-primary: #f9fafb;
  --color-text-secondary: #cbd5e1;
  --color-border: #334155;
}
```

## 4. Tailwind v4 `@theme` 示例

```css
@import "tailwindcss";

@theme {
  --color-primary: #1677ff;
  --color-bg-page: #f9fafb;
  --color-text-primary: #111827;
  --spacing-1: 4px;
  --spacing-2: 8px;
  --spacing-4: 16px;
  --radius-md: 8px;
  --shadow-card: 0 4px 16px rgba(15, 23, 42, 0.08);
  --breakpoint-xs: 480px;
}
```

规则：

- 需要生成 Tailwind 工具类的 Token 放进 `@theme`。
- 仅运行时使用、不需要工具类的变量可放 `:root`。
- 禁止业务页面大量使用任意值类绕过 Token。

## 5. 组件库主题映射表

| Token | Ant Design / MUI / Element / Naive 等映射 | 备注 |
|---|---|---|
| `--color-primary` | 组件库 primary color | 品牌主色 |
| `--radius-md` | borderRadius | 全局圆角 |
| `--font-family-base` | fontFamily | 全局字体 |
| `--color-bg-page` | layout/page background | 页面背景 |
| `--color-border` | border color | 分割线/边框 |

## 6. 硬编码例外

允许硬编码的地方：

- Token 定义文件。
- 第三方组件库主题配置文件。
- 明确标注 TODO 的临时 Spike。

禁止硬编码的地方：

- 页面组件。
- 模块业务组件。
- 重复出现的局部样式。
