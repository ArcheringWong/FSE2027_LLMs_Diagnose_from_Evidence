#!/usr/bin/env python3
"""Verify the anonymous review package against SHA256SUMS."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    ledger = ROOT / "SHA256SUMS"
    failures: list[str] = []
    checked = 0
    for line_number, line in enumerate(ledger.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        expected, relative = line.split("  ", 1)
        target = ROOT / relative
        checked += 1
        if not target.is_file():
            failures.append(f"missing:{relative}")
        elif sha256(target) != expected:
            failures.append(f"mismatch:{relative}")
    if failures:
        raise SystemExit("INTEGRITY_CHECK_FAILED\n" + "\n".join(failures))
    print(f"INTEGRITY_CHECK_PASSED files={checked}")


if __name__ == "__main__":
    main()

