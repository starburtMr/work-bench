# Security

## Main Topics

- JWT auth
- HttpOnly cookies
- password hashing with Argon2
- key management
- request validation
- CORS and middleware configuration

## Where It Lives

- `app/core/security.py`
- `app/core/key_management.py`
- `app/core/middleware.py`
- `app/core/settings.py`
- module-level presentation exceptions and dependencies

## Rules

- Keep secrets in `.env`, not in code.
- Never commit real credentials.
- Validate data at the API boundary.
- Keep auth and cookie handling centralized.
- Use shared security helpers instead of ad hoc logic in routers.

## Practical Notes

- The template is designed to keep access tokens out of JavaScript when possible.
- The auth flow should remain consistent across modules and tests.
