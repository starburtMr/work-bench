# Error Handling

## Goal

Keep errors predictable, structured, and easy to debug.

## Main Pieces

- `app/core/exception_handler.py` for centralized exception handling
- `app/core/middleware.py` for request and response middleware
- module-level `presentation/exceptions.py` files for feature-specific errors

## Rules

- Catch expected domain and application errors close to the presentation layer.
- Return consistent HTTP errors instead of leaking raw exceptions.
- Keep internal stack traces in logs, not in the public response.
- Use middleware for cross-cutting behavior such as request logging and response shaping.

## Logging Flow

- The visual flow is shown in `docs/logging_rule.png`.
- Use it as a quick reference for how request logging should move through the stack.
