"""Reference redaction middleware used throughout the notebooks."""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable, Mapping

EMAIL_RE = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.IGNORECASE)


@dataclass
class RedactionResult:
    original: str
    redacted: str
    replacements: int


def redact_emails(text: str) -> RedactionResult:
    """Replace email addresses with a ``[REDACTED]`` token."""
    redacted, count = EMAIL_RE.subn('[REDACTED]', text)
    return RedactionResult(original=text, redacted=redacted, replacements=count)


def apply_redaction(messages: Iterable[Mapping[str, str]]) -> list[Mapping[str, str]]:
    """Return a list of messages with email addresses masked out."""
    cleaned = []
    for message in messages:
        content = message.get('content', '')
        result = redact_emails(content)
        cleaned.append({**message, 'content': result.redacted, 'redactions': result.replacements})
    return cleaned
