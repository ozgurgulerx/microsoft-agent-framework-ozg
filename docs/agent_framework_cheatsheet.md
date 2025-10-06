# Agent Framework Cheatsheet

## Core Concepts
- **Agents**: encapsulate goals, tools, and memory policies.
- **Workflows**: orchestrate multi-step behaviors with sequential, concurrent, or conditional edges.
- **Edges**: routing logic between workflow nodes (draft, fact-check, polish, etc.).
- **Tools**: call external services via structured input/output contracts.
- **Approvals / HITL**: pause execution and resume once a decision arrives.
- **Checkpoints**: persist state for restarts and long-running processes.

## Patterns
- Use middleware (`tools/redact_middleware.py`) to scrub content before logging.
- Stream tokens with `tools/tee_stream.py` to capture both UX and audit trails.
- Export workflow diagrams with `tools/dag_export.py` to `_runs/_viz/`.
- Wrap flaky operations with `tools/backoff.py.retry` for deterministic retries.
