# Application Overview

`typescript-backend-toolkit` is a reusable backend toolkit skeleton, not a single business app.
It is built on Express + MongoDB/Mongoose + Redis/BullMQ + a plugin system, and is designed to help teams bootstrap a production-ready API with a predictable structure.

## What It Includes

- Express server setup
- MagicRouter-based HTTP wiring
- OpenAPI docs at `/docs`
- Zod validation and typed responses
- JWT auth and session support
- file uploads
- queues and background jobs
- email templates and preview
- admin and realtime plugins
- a CLI for generating modules and plugins
- a project scaffolder package with reusable templates

## Main Runtime Areas

- `src/app` boots the server and registers plugins
- `src/modules` holds business modules
- `src/plugins` adds platform capabilities without touching core code
- `src/lib` connects to infrastructure
- `src/routes` wires HTTP entry points
- `src/config` validates environment variables

## When To Use It

- when you want a consistent backend architecture
- when you want code generation for modules and plugins
- when you want typed routes, schemas, and OpenAPI output
- when you want a backend that already includes common platform concerns
