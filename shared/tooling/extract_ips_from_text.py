#!/usr/bin/env python3
"""Extract public IPv4 addresses from sandbox/memory/text exports into ETW ips.csv schema.

Does NOT execute malware, contact C2, or invent indicators.
Private/loopback/link-local/CGNAT bogons are filtered out.
"""
from __future__ import annotations

import argparse
import csv
import ipaddress
import re
from datetime import datetime, timezone
from pathlib import Path

IP_REGEX = re.compile(
    r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b"
)

HEADERS = [
    "indicator_type",
    "value",
    "first_seen_utc",
    "last_seen_utc",
    "confidence",
    "provenance",
    "evidence_id",
    "notes",
]


def is_public_ip(ip: str) -> bool:
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError:
        return False
    if addr.version != 4:
        return False
    return not (
        addr.is_private
        or addr.is_loopback
        or addr.is_link_local
        or addr.is_multicast
        or addr.is_reserved
        or addr.is_unspecified
    )


def extract_ips(text: str) -> list[str]:
    found = sorted({m.group(0) for m in IP_REGEX.finditer(text)})
    return [ip for ip in found if is_public_ip(ip)]


def load_existing(path: Path) -> set[str]:
    if not path.exists():
        return set()
    values: set[str] = set()
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            v = (row.get("value") or "").strip()
            if v:
                values.add(v)
    return values


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--input", "-i", required=True, help="Text/strings/sandbox export file")
    ap.add_argument("--family", "-f", required=True, help="Malware family name (metadata only)")
    ap.add_argument("--output", "-o", required=True, help="Destination ips.csv path")
    ap.add_argument("--append", action="store_true", help="Append unique IPs to existing CSV")
    ap.add_argument(
        "--provenance",
        default="LAB_SANDBOX",
        help="Provenance label (default LAB_SANDBOX)",
    )
    ap.add_argument("--confidence", default="High", choices=["High", "Moderate", "Low"])
    ap.add_argument("--source-ref", default="", help="Lab run ID / sandbox URL / dump path")
    ap.add_argument(
        "--evidence-id-prefix",
        default="",
        help="Optional prefix e.g. POL-LAB- for generated evidence_id",
    )
    args = ap.parse_args()

    inp = Path(args.input)
    out = Path(args.output)
    text = inp.read_text(encoding="utf-8", errors="ignore")
    ips = extract_ips(text)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    existing = load_existing(out) if args.append else set()
    new_ips = [ip for ip in ips if ip not in existing]

    rows: list[dict] = []
    if args.append and out.exists():
        with out.open(newline="", encoding="utf-8") as f:
            rows.extend(list(csv.DictReader(f)))

    for i, ip in enumerate(new_ips, start=1):
        eid = ""
        if args.evidence_id_prefix:
            eid = f"{args.evidence_id_prefix}{i:04d}"
        note = (
            f"Extracted from {inp.name} for family={args.family}. "
            f"Filter=public-IPv4-only. {args.source_ref}".strip()
        )
        rows.append(
            {
                "indicator_type": "ipv4",
                "value": ip,
                "first_seen_utc": ts,
                "last_seen_utc": ts,
                "confidence": args.confidence,
                "provenance": args.provenance,
                "evidence_id": eid,
                "notes": note,
            }
        )

    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADERS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in HEADERS})

    print(
        f"Wrote {out}: {len(new_ips)} new public IPv4 "
        f"(seen_in_input={len(ips)}, skipped_existing={len(ips) - len(new_ips)})"
    )


if __name__ == "__main__":
    main()
