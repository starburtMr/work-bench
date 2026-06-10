# Blank Module

This module is the clean copy point for new business modules.

When creating a real module:

1. Copy `blank` to `app/modules/<new-module>`.
2. Rename classes, routers, schemas, docs, exceptions, and tests together.
3. Put domain rules in `domain`.
4. Put orchestration in `application`.
5. Put persistence and external adapters in `infrastructure`.
6. Put HTTP schemas, routes, dependencies, and docs in `presentation`.

Do not add product behavior to `blank`; keep it minimal so it remains reusable.
