# Governance & Safety

- **Redaction**: Apply `tools/redact_middleware.py` before logging transcripts.
- **Tool allowlists**: Define explicit tool registries per workflow; default to deny.
- **PII handling**: Keep sensitive data in short-lived fixtures; never commit production secrets.
- **Rate limits**: The backoff utility demonstrates how to handle throttling gracefully.
- **Observability**: Ship traces and metrics through OTEL exporters for auditability.
