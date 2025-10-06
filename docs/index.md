# Welcome to Agent Framework Quests

## Visual Curriculum Map

- **Prologue** – setup, mock mode, and hello world agent
- **Basics Gauntlet** – twelve labs covering streaming, tools, workflows, approvals, and checkpointing
- **Open Standards** – MCP, agent-to-agent, and OpenAPI adapters
- **Foundry Integration** – persistent agents with Azure AI Foundry
- **Quests** – scenario-based challenges with fixtures and grading
- **Boss Fights** – capstone labs that combine everything

## Quickstart

1. Create a virtual environment and install `nbformat nbconvert nbval` (or reuse the provided container).
2. Launch JupyterLab and open `Launcher.ipynb`.
3. Work through notebooks in order; each writes progress into `_runs/`.
4. Use `4-evals/Grader.ipynb` to review completion stats.

## Offline First

All notebooks default to `USE_REAL_CLIENT=False` and use `_fixtures/` to simulate responses. Run notebooks end-to-end without network access, then switch to live providers when ready.
