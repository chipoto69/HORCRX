#!/usr/bin/env python3
# H4 redaction validator — specs/vessel-format/traces-format.md §Redaction-validator contract

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = REPO / "validation/fixtures/traces/redaction-input.ndjson"
DEFAULT_EXPECTED = REPO / "validation/fixtures/traces/redaction-expected.ndjson"
MAX_LINE_BYTES = 64 * 1024

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE_RE = re.compile(r"(?:\+\d{1,3}[-\s]?)?(?:\(?\d{3}\)?[-\s]?)\d{3}[-\s]\d{4}")
SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
BEARER_RE = re.compile(r"(?i)\bBearer\s+[A-Za-z0-9._\-]{8,}")
ASSIGNMENT_RE = re.compile(r"(?i)\b(api[_-]?key|token|secret)\b\s*[:=]\s*[A-Za-z0-9._\-]{8,}")


def fail(message: str) -> None:
    print(f"REDACTION VALIDATOR FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def redact_text(text: str) -> str:
    text = EMAIL_RE.sub("[REDACTED_EMAIL]", text)
    text = PHONE_RE.sub("[REDACTED_PHONE]", text)
    text = SSN_RE.sub("[REDACTED_SSN]", text)
    text = BEARER_RE.sub("Bearer [REDACTED_TOKEN]", text)

    def replace_assignment(match: re.Match[str]) -> str:
        label = match.group(1)
        separator = "=" if "=" in match.group(0) else ": "
        return f"{label}{separator}[REDACTED_SECRET]"

    text = ASSIGNMENT_RE.sub(replace_assignment, text)
    return text


def redact_value(value: Any) -> Any:
    if isinstance(value, str):
        return redact_text(value)
    if isinstance(value, list):
        return [redact_value(item) for item in value]
    if isinstance(value, dict):
        return {key: redact_value(item) for key, item in value.items()}
    return value


def detect_leak(rendered: str) -> str | None:
    for name, pattern in (
        ("email", EMAIL_RE),
        ("phone", PHONE_RE),
        ("ssn", SSN_RE),
        ("bearer token", BEARER_RE),
        ("secret assignment", ASSIGNMENT_RE),
    ):
        match = pattern.search(rendered)
        if match:
            return f"{name}: {match.group(0)}"
    return None


def load_lines(path: Path) -> list[str]:
    return [line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT
    expected_path = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_EXPECTED

    rendered_lines: list[str] = []
    for raw_line in load_lines(input_path):
        obj = json.loads(raw_line)
        redacted = redact_value(obj)
        rendered = json.dumps(redacted, ensure_ascii=False, sort_keys=True)
        if len(rendered.encode("utf-8")) > MAX_LINE_BYTES:
            fail(f"redacted line exceeds 64 KiB limit: {redacted.get('event_id', 'unknown-event')}")
        leak = detect_leak(rendered)
        if leak:
            fail(f"redacted line still leaks {leak}")
        rendered_lines.append(rendered)

    expected_lines = load_lines(expected_path)
    if rendered_lines != expected_lines:
        fail(
            "redacted output did not match golden fixture\n"
            f"EXPECTED: {expected_lines}\n"
            f"RENDERED: {rendered_lines}"
        )

    print(
        "REDACTION VALIDATOR PASS: fixture traces were deterministically redacted "
        "and no secret or PII pattern remained in the serialized output."
    )


if __name__ == "__main__":
    main()
