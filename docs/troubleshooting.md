# Troubleshooting

- Notebook fails on import: ensure you ran `pip install nbformat nbconvert`.
- `_runs/` folder missing: rerun the setup cell; it creates lab-specific directories.
- Mermaid diagrams not rendering locally: open the `.mmd` files in VS Code or let CI export PNGs.
- Switching to live mode: confirm environment variables are set and restart the kernel.
