# API Layer

The backend is organized as a set of layers that work from the outside in.

## Typical Flow

`HTTP request -> router -> dependency -> use case -> repository or service -> response`

## Presentation

- routers
- request and response schemas
- dependencies
- endpoint docs helpers
- presentation-level exceptions

## Application

- use cases
- interfaces or ports
- orchestration logic
- feature-level rules that do not belong in HTTP or database code

## Domain

- entities
- value objects
- domain services
- mapping helpers

## Infrastructure

- SQLAlchemy models
- repositories
- database access
- external services and adapters

## Rules to Keep

- Routers should stay thin.
- Do not let HTTP handlers talk to the database directly.
- Do not leak ORM models into the application layer.
- Keep shared behavior in reusable helpers instead of repeating it across modules.
