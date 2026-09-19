#!/usr/bin/env python3
"""Sort a case master-timeline.csv by UTC timestamp."""
from __future__ import annotations
import argparse
import csv
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path", type=Path)
    ap.add_argument("--inplace", action="store_true")
    args = ap.parse_args()
    with args.csv_path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        fieldnames = reader.fieldnames or []
        rows = list(reader)
    rows.sort(key=lambda r: (r.get("timestamp_utc") or "", r.get("event_id") or ""))
    out = args.csv_path if args.inplace else args.csv_path.with_suffix(".sorted.csv")
    with out.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()