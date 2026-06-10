# Application Overview

This backend is a FastAPI template built around Clean Architecture and DDD ideas.
It is meant to be a reusable starting point for modular API services.

## Main Modules

- `authentication` - login, token, and session related flows
- `health` - health and readiness endpoints
- `user` - user management features
- `shared` - shared enums, helpers, and cross-cutting application code
- `example` - a reference module that shows the intended structure
- `blank` - a scaffold module for new feature creation

## What It Is Good For

- showing a layered FastAPI backend layout
- keeping domain logic separated from web and database details
- giving a repeatable module structure for new features
- providing a practical base for API-first backend work

## Main Layers

- `presentation` - routers, schemas, request dependencies, and docs helpers
- `application` - use cases and ports
- `domain` - entities, value objects, services, and rules
- `infrastructure` - repositories, ORM models, and external adapters
- `core` - settings, database, security, logging, middleware, and shared runtime wiring
