# Commands

## Development

```bash
pnpm dev
pnpm start:dev
pnpm build
pnpm start:prod
pnpm start:local
pnpm typecheck
pnpm lint
pnpm lint:fix
pnpm email:dev
```

## Docker

```bash
docker compose up -d
docker compose down
```

## CLI

```bash
pnpm tbk generate:module <name>
pnpm tbk generate:plugin <name>
pnpm tbk generate:middleware <name>
pnpm tbk make:seeder <module>/<name>
pnpm tbk make:factory <module>/<name>
pnpm tbk seed
pnpm tbk docs:openapi
pnpm tbk docs:sdk
```

## Notes

- `pnpm dev` runs the server and email preview together.
- `pnpm start:dev` runs only the backend server in watch mode.
- `pnpm start:prod` runs the compiled app with the production env file.
- `pnpm start:local` runs the compiled app with the local env file.
- `pnpm tbk` is the main scaffolding and maintenance entry point.
- `pnpm tbk` runs the local CLI source through `tsx`; published packages still build their own `dist/` output.
