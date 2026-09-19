#!/usr/bin/env python3
"""Validate required IOC fields for a case combined.csv."""
from __future__ import annotations
import argparse
import csv
import sys
from pathlib import Path

REQUIRED = ["value", "type", "source", "confidence", "status", "case_id"]
STATUSES = {
    "HIGH CONFIDENCE MALICIOUS",
    "CAMPAIGN ASSOCIATED",
    "SUSPICIOUS",
    "HISTORICAL",
    "UNVERIFIED",
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path", type=Path)
    args = ap.parse_args()
    errors = 0
    with args.csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for i, row in enumerate(reader, start=2):
            for field in REQUIRED:
                if not (row.get(field) or "").strip():
                    print(f"L{i}: missing {field}")
                    errors += 1
            status = (row.get("status") or "").strip()
            if status and status not in STATUSES:
                print(f"L{i}: invalid status {status!r}")
                errors += 1
    if errors:
        print(f"{errors} validation error(s)")
        return 1
    print("IOC validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())