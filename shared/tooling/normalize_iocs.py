#!/usr/bin/env python3
"""Normalize IOC CSV rows (passive, local-only). No network calls."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

DEFANG_RE = re.compile(r"\[\.\]|\\\.")
WS_RE = re.compile(r"\s+")


def normalize_value(value: str, ioc_type: str) -> str:
    v = WS_RE.sub("", value.strip())
    v = DEFANG_RE.sub(".", v)
    if ioc_type in {"sha256", "sha1", "md5"}:
        return v.lower()
    if ioc_type in {"domain", "url"}:
        return v.lower().rstrip("/")
    if ioc_type in {"ipv4", "ipv6"}:
        return v
    return value.strip()


def main() -> int:
    p = argparse.ArgumentParser(description="Normalize IOC CSV values locally")
    p.add_argument("csv_path", type=Path)
    p.add_argument("--value-col", default="value")
    p.add_argument("--type-col", default="type")
    p.add_argument("--inplace", action="store_true")
    args = p.parse_args()

    with args.csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            print("empty CSV", file=sys.stderr)
            return 1
        rows = list(reader)
        fields = list(reader.fieldnames)

    for row in rows:
        t = row.get(args.type_col, "")
        if args.value_col in row and row[args.value_col]:
            row[args.value_col] = normalize_value(row[args.value_col], t)

    out = args.csv_path if args.inplace else args.csv_path.with_suffix(".normalized.csv")
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {out} ({len(rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
