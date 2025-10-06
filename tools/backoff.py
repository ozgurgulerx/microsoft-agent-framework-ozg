"""Simple deterministic backoff helper with jitter."""
from __future__ import annotations

import random
import time
from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class Attempt:
    index: int
    delay: float
    success: bool
    error: Optional[str] = None


def compute_delay(attempt: int, base: float, factor: float, jitter: float) -> float:
    deterministic = base * (factor ** (attempt - 1))
    return deterministic + random.uniform(0, jitter)


def retry(operation: Callable[[], object], attempts: int = 3, base: float = 0.5, factor: float = 2.0, jitter: float = 0.05, sleeper: Callable[[float], None] = time.sleep) -> tuple[object | None, list[Attempt]]:
    """Retry ``operation`` with exponential backoff."""
    history: list[Attempt] = []
    for idx in range(1, attempts + 1):
        try:
            result = operation()
            history.append(Attempt(index=idx, delay=0.0, success=True))
            return result, history
        except Exception as exc:  # pragma: no cover - illustrative
            delay = compute_delay(idx, base, factor, jitter)
            history.append(Attempt(index=idx, delay=delay, success=False, error=str(exc)))
            if idx == attempts:
                return None, history
            sleeper(delay)
    return None, history
