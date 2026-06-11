# Security

## Environment And Secrets

- keep secrets in `.env.*` files
- use `src/config/env.ts` for validated settings
- do not access `process.env` directly in app code
- treat checked-in env files as examples and replace dummy values in real projects

## Auth

- JWT auth is handled through the auth middleware and helpers
- protected requests can read the user from `req.user`
- session management is separate from JWT token handling

## Uploads

- use Formidable-backed multipart handling
- read uploaded files from `req.body`
- do not use `req.file` or `req.files`

## Operational Surfaces

- protect admin surfaces in production
- protect queue dashboards in production
- protect realtime tools in production
- rotate JWT, session, admin, and provider secrets when copying the skeleton

## Useful Files

- `src/middlewares/can-access.ts`
- `src/middlewares/extract-jwt.ts`
- `src/middlewares/error-handler.ts`
- `src/config/env.ts`
- `src/utils/jwt.utils.ts`
- `src/lib/storage.ts`
