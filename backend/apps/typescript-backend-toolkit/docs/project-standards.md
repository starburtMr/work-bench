# Project Standards

## Core Rules

- Use TypeScript everywhere.
- Use Zod for validation and typed schemas.
- Use MagicRouter for HTTP routes.
- Keep controllers thin.
- Keep services framework-agnostic.
- Keep database and external clients in `lib`.
- Keep shared code in `common`, `config`, `middlewares`, or `utils`.

## Naming

- Use `camelCase` for variables and functions.
- Use `PascalCase` for classes and types.
- Use clear feature names for modules and plugins.
- Keep file names focused and descriptive.

## Validation And Responses

- Put request and response schemas in `*.schema.ts`.
- Export response schemas from schema files rather than inlining them in routers.
- Use the typed response helpers from the MagicRouter layer.
- Use `validator.isMongoId()` for MongoDB IDs instead of regex.

## Environment

- Use `src/config/env.ts` for all environment access.
- Do not read `process.env` directly in application code.
- Keep `.env.development`, `.env.production`, and `.env.sample` aligned as examples.
- Replace dummy secrets, database names, admin credentials, and public origins after copying the skeleton into a real project.

## Common Mistakes To Avoid

- using plain Express route handlers instead of MagicRouter
- placing business logic in controllers
- creating modules by hand instead of using `pnpm tbk generate:module`
- forgetting to register a router in `src/routes/routes.ts`
- using `req.file` or `req.files` for Formidable uploads
