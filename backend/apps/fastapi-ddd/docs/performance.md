# Performance

This template is designed to stay lightweight while still being practical for real services.

## Good Defaults

- use async database access where possible
- keep routers thin so requests do not do extra work
- let use cases and repositories own the heavy lifting
- prefer clear query boundaries over repeated round trips
- use `orjson` where the stack already supports fast JSON output

## Things To Watch

- avoid putting business logic in middleware
- avoid unnecessary DB work in request handlers
- keep response shapes focused on what the client needs
- do not add abstractions that do not buy anything yet

## Practical Rule

- optimize only after the current flow is clear and measurable
