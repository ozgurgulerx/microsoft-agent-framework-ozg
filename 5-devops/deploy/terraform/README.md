# Terraform Deployment Notes

Use this folder to capture Terraform modules for multi-cloud rollouts. Suggested structure:

- `modules/` for reusable primitives (queues, storage, observability)
- `envs/<environment>` for environment-specific stacks

Each module should expose outputs that the notebooks or Foundry configuration can ingest, such as endpoint URLs or OTEL exporters.
