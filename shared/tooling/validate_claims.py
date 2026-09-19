#!/usr/bin/env python3
"""Validate claims-ledger CSV rows against claim.schema.json rules (local only)."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

CLAIM_ID_RE = re.compile(r"^(RAP|SET|RAT|NRB)-CLAIM-[0-9]{4}$")
STATUSES = {
    "PRIMARY_SOURCE",
    "SECONDARY",
    "CORROBORATED",
    "UNVERIFIED",
    "CONTRADICTED",
    "INFERRED",
}
SOURCE_TYPES = {"PRIMARY", "INDEPENDENT_CORROBORATION", "SECONDARY", "UNVERIFIED"}
CONF = {"High", "Moderate", "Low"}
FAMILIES = {"Rapuncel": "RAP", "Settra": "SET", "RatHat": "RAT", "NodeRabbit": "NRB"}


def validate_row(row: dict, line_no: int) -> list[str]:
    errs: list[str] = []
    cid = row.get("claim_id", "")
    if not CLAIM_ID_RE.match(cid):
        errs.append(f"L{line_no}: bad claim_id {cid!r}")
    family = row.get("family", "")
    case_id = row.get("case_id", "")
    if family not in FAMILIES:
        errs.append(f"L{line_no}: bad family {family!r}")
    elif FAMILIES[family] != case_id:
        errs.append(f"L{line_no}: family/case_id mismatch {family}/{case_id}")
    if not (row.get("claim") or "").strip():
        errs.append(f"L{line_no}: empty claim")
    if row.get("status") not in STATUSES:
        errs.append(f"L{line_no}: bad status {row.get('status')!r}")
    if row.get("source_type") not in SOURCE_TYPES:
        errs.append(f"L{line_no}: bad source_type {row.get('source_type')!r}")
    if row.get("confidence") not in CONF:
        errs.append(f"L{line_no}: bad confidence {row.get('confidence')!r}")
    iv = (row.get("independently_verified") or "").strip().lower()
    if iv not in {"true", "false"}:
        errs.append(f"L{line_no}: independently_verified must be true/false")
    if (row.get("cutoff_applies") or "").strip().lower() != "true":
        errs.append(f"L{line_no}: cutoff_applies must be true")
    if not (row.get("retrieval_date_utc") or "").strip():
        errs.append(f"L{line_no}: missing retrieval_date_utc")
    if not (row.get("source_url") or "").strip():
        errs.append(f"L{line_no}: missing source_url")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_paths", nargs="+", type=Path)
    ap.add_argument(
        "--schema",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "schemas" / "claim.schema.json",
    )
    args = ap.parse_args()
    if args.schema.exists():
        json.loads(args.schema.read_text(encoding="utf-8"))

    all_errs: list[str] = []
    total = 0
    for path in args.csv_paths:
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader, start=2):
                total += 1
                all_errs.extend(validate_row(row, i))
        print(f"{path}: checked")
    if all_errs:
        print(f"FAIL ({len(all_errs)} issues / {total} claims)", file=sys.stderr)
        for e in all_errs[:50]:
            print(e, file=sys.stderr)
        if len(all_errs) > 50:
            print(f"... +{len(all_errs) - 50} more", file=sys.stderr)
        return 1
    print(f"OK: {total} claims valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
