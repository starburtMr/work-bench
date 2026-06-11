# MagicRouter

MagicRouter is the routing layer used by this runtime.
It replaces plain Express route definitions and keeps routes, validation, and responses typed.

## Rules

- always create routes with MagicRouter
- always pass a config object as the second argument
- always export `router.getRouter()`
- keep response schemas in `*.schema.ts`
- keep the controller as the last handler

## Response Builders

Use the builders from `src/plugins/magic/response.builders.ts`:

- `R.success(schema)`
- `R.paginated(schema)`
- `R.noContent()`
- `R.error()`
- `R.raw(schema)`

## Typical Pattern

```ts
const router = new MagicRouter('/api/users');

router.post(
  '/create',
  {
    requestType: { body: createUserSchema },
    responses: { 201: createUserResponseSchema },
  },
  canAccess(),
  handleCreate,
);

export default router.getRouter();
```

## Why It Matters

- routes stay consistent
- OpenAPI is generated from schemas
- request and response types stay in sync
- middleware and controller responsibilities stay clear
