# Deployment

## Local Run

```bash
docker compose up -d
pnpm dev
```

## Production Build

```bash
pnpm build
pnpm start:prod
```

## Local Dist Run

```bash
pnpm start:local
```

## Environment Files

- `.env.development` for local watch mode examples
- `.env.production` for production runtime examples
- `.env.sample` as the template for new environments

## Before Release

- run `pnpm typecheck`
- run `pnpm lint`
- run `pnpm build`
- confirm `/docs` is generated correctly
- confirm the required plugins are enabled
- confirm auth, queues, and admin surfaces are protected
- replace all dummy secrets and provider credentials
