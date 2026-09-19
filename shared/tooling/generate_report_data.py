#!/usr/bin/env python3
"""Assemble lightweight JSON summary stats for a case (passive)."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path


def count_csv(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(newline="", encoding="utf-8") as fh:
        return max(sum(1 for _ in csv.DictReader(fh)), 0)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("case_id", choices=["rapuncel", "settra", "rathat", "noderabbit"])
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = ap.parse_args()
    base = args.root / "investigations" / args.case_id
    data = {
        "case_id": args.case_id,
        "evidence_rows": count_csv(base / "evidence" / "evidence-ledger.csv"),
        "source_rows": count_csv(base / "evidence" / "source-index.csv"),
        "ioc_rows": count_csv(base / "iocs" / "combined.csv"),
        "timeline_rows": count_csv(base / "timelines" / "master-timeline.csv"),
    }
    out = base / "analysis" / "report-data.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()