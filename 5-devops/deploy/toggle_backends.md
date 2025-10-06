# Toggling Backend Providers

The notebooks default to fixture-backed mock mode. To enable live traffic:

1. Copy `.env.example` to `.env` and set `USE_REAL_CLIENT=true`.
2. Provide credentials for the providers you wish to test (Azure OpenAI, OpenAI, or GitHub Models).
3. Restart your notebook kernel so environment variables are refreshed.

When the mock fixtures should be reused for regression testing, flip the flag back to `false`. The helper utilities always respect the toggle at runtime, so no code changes are required.
