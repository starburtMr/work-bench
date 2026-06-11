# Architecture

## Request Flow

`HTTP request -> MagicRouter -> middleware -> controller -> service -> model or adapter -> response`

## Layers

- `src/routes` wires HTTP entry points
- `src/modules` owns business features
- `src/plugins` adds platform capabilities
- `src/lib` contains infrastructure clients
- `src/app` boots the server and registers plugins
- `src/config` validates environment values

## Module Pattern

Modules keep their own DTOs, schemas, services, controllers, models, and routers together.
That keeps the business logic easy to find and easy to scaffold.

## Plugin System

Plugins are registered during app startup.
They are used for platform concerns that should not live inside a feature module.

Common built-in plugins include:

- logger
- basic parser
- observability
- security
- cache
- magic
- lifecycle
- auth
- admin
- realtime
- bullboard

## Key Idea

Keep domain logic in modules, keep reusable platform code in plugins and libs, and keep HTTP wiring thin.
