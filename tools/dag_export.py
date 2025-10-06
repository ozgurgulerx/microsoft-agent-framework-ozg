"""Helpers for exporting lightweight workflow visualisations."""
    from __future__ import annotations

    from pathlib import Path
    from typing import Literal

    DEFAULT_VIZ_DIR = Path('_runs/_viz')


    def export_graph(name: str, content: str, fmt: Literal['mermaid', 'dot'] = 'mermaid', run_dir: Path | None = None, create_png_placeholder: bool = False) -> Path:
        """Persist graph markup for CI to render."""

        out_dir = run_dir or DEFAULT_VIZ_DIR
        out_dir.mkdir(parents=True, exist_ok=True)
        ext = '.mmd' if fmt == 'mermaid' else '.dot'
        target = out_dir / f"{name}{ext}"
        target.write_text(content.strip() + '
', encoding='utf-8')

        if create_png_placeholder:
            placeholder = out_dir / f"{name}.png.todo"
            placeholder.write_text('render in CI', encoding='utf-8')

        return target
