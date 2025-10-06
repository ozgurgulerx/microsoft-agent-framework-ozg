# Bicep Deployment Notes

These templates intentionally focus on infrastructure building blocks for long-running Agent Framework services:

- Azure Container Apps or AKS for workflow hosting
- Azure OpenAI deployments (optional)
- Azure Monitor / Application Insights with OTEL exporters

Provide parameter files per environment and link them into your CI/CD pipeline once ready. Templates are not included yet to keep the repo provider-neutral; scaffold them here when your project is ready.
