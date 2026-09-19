#!/usr/bin/env python3
"""Emit a simple markdown table from a CSV (for report assembly)."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path", type=Path)
    ap.add_argument("--limit", type=int, default=50)
    args = ap.parse_args()
    with args.csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fields = reader.fieldnames or []
        rows = []
        for i, row in enumerate(reader):
            if i >= args.limit:
                break
            rows.append(row)
    print("| " + " | ".join(fields) + " |")
    print("| " + " | ".join(["---"] * len(fields)) + " |")
    for row in rows:
        print("| " + " | ".join((row.get(f) or "").replace("|", "\\|") for f in fields) + " |")


if __name__ == "__main__":
    main()