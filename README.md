# Agent Framework Quests

Agent Framework Quests is a Jupyter-first curriculum for the Microsoft Agent Framework. It complements the official samples by leaning into story-driven labs, fixtures, and auto-grading so teams can experiment completely offline before connecting to production services.

The learning path runs in four acts: **Prologue**, **Basics Gauntlet**, **Quests**, and **Boss Fights**. Each notebook uses deterministic fixtures plus a `USE_REAL_CLIENT` toggle so learners can flip between mock mode and live endpoints at their own pace.

Offline mode relies on the datasets under `_fixtures/` and writes artifacts to `_runs/<lab>/...` for grading and dashboards. Switch `USE_REAL_CLIENT=True` once credentials are ready and the same notebooks will point at real Agent Framework clients.

![Basics Gauntlet Cleared](https://img.shields.io/badge/Basics%20Gauntlet-Cleared-3b82f6)
![MCP Explorer](https://img.shields.io/badge/MCP-Explorer-22c55e)
![Workflow Wizard](https://img.shields.io/badge/Workflow-Wizard-f97316)

* Docs live under [`docs/`](docs/index.md)
* Course assets live under [`course/`](course/)
