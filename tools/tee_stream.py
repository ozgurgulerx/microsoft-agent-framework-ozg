"""Utility helpers for streaming notebook demos."""
    from __future__ import annotations

    import sys
    from pathlib import Path
    from typing import Iterable, Union


    def tee_stream(chunks: Iterable[str], run_dir: Union[str, Path], filename: str = "stream.txt", end: str = "
") -> Path:
        """Write streamed chunks to stdout *and* persist them under ``run_dir``."""

        run_path = Path(run_dir)
        run_path.mkdir(parents=True, exist_ok=True)
        target = run_path / filename

        with target.open('w', encoding='utf-8') as handle:
            for part in chunks:
                sys.stdout.write(part)
                sys.stdout.flush()
                handle.write(part)
            if end:
                sys.stdout.write(end)
                sys.stdout.flush()
                handle.write(end)
        return target
