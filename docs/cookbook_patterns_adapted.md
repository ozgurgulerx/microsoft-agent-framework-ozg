# Cookbook Patterns Adapted for Agent Framework

| Pattern | Adaptation |
| --- | --- |
| Streaming responses | `01_streaming_basics.ipynb` uses `tee_stream.py` to capture streams. |
| Function calling | `02_tools_fncalling.ipynb` simulates tool IO based on fixtures. |
| Structured output | `03_structured_output.ipynb` enforces JSON schema-like structures. |
| Retriable middleware | `05_middleware_redaction_retry.ipynb` shows redaction plus backoff. |
| Checkpoint resume | `10_checkpoint_resume.ipynb` persists state and reloads it. |
| Nested workflows | `11_workflow_nesting.ipynb` shows parent/child orchestration. |
| Request/response HITL | `12_workflow_request_response.ipynb` demonstrates explicit pauses. |
