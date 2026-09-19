#!/usr/bin/env python3
"""Fail if the same IOC value appears in multiple cases without a Supported cross-case relationship."""
from __future__ import annotations
import argparse
import csv
import sys
from collections import defaultdict
from pathlib import Path

CASES = ("rapuncel", "settra", "rathat", "noderabbit")


def load_iocs(root: Path) -> dict[str, set[str]]:
    by_value: dict[str, set[str]] = defaultdict(set)
    for case in CASES:
        path = root / "investigations" / case / "iocs" / "combined.csv"
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                value = (row.get("value") or "").strip().lower()
                if value:
                    by_value[value].add(case)
    return by_value


def supported_links(root: Path) -> set[frozenset[str]]:
    path = root / "intelligence" / "campaign-relationships.csv"
    links: set[frozenset[str]] = set()
    if not path.exists():
        return links
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if (row.get("status") or "").upper() != "SUPPORTED":
                continue
            links.add(frozenset({row["case_a"], row["case_b"]}))
    return links


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = ap.parse_args()
    by_value = load_iocs(args.root)
    links = supported_links(args.root)
    violations = []
    for value, cases in sorted(by_value.items()):
        if len(cases) < 2:
            continue
        # every pair among cases must be Supported
        case_list = sorted(cases)
        ok = True
        for i in range(len(case_list)):
            for j in range(i + 1, len(case_list)):
                if frozenset({case_list[i], case_list[j]}) not in links:
                    ok = False
        if not ok:
            violations.append((value, case_list))
    if violations:
        print("CASE ISOLATION VIOLATIONS:")
        for value, cases in violations:
            print(f"  {value} -> {', '.join(cases)}")
        return 1
    print("Case isolation check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())