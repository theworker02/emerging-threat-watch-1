#!/usr/bin/env python3
"""Rebuild STIX bundles using official stix2 library for validator compatibility."""
from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

from stix2 import Bundle, Identity, Indicator, Malware, Relationship

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "law-enforcement" / "CTI-Evidence-Repository" / "families"
NOW = datetime.now(timezone.utc)

FAMILIES = [
    "Rapuncel",
    "Settra",
    "RatHat",
    "NodeRabbit",
    "PollCat",
    "SynkLoader",
    "Showboat",
]

SLUG = {
    "Rapuncel": "rapuncel",
    "Settra": "settra",
    "RatHat": "rathat",
    "NodeRabbit": "noderabbit",
    "PollCat": "pollcat",
    "SynkLoader": "synkloader",
    "Showboat": "showboat",
}


def load_rows(slug: str) -> list[dict]:
    p = ROOT / "investigations" / slug / "evidence" / "published-indicators.csv"
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pattern_for(itype: str, value: str) -> str | None:
    t = (itype or "").lower()
    if t == "sha256":
        return f"[file:hashes.'SHA-256' = '{value.lower()}']"
    if t == "md5":
        return f"[file:hashes.MD5 = '{value.lower()}']"
    if t in ("ipv4", "ip"):
        return f"[ipv4-addr:value = '{value}']"
    if t == "domain":
        return f"[domain-name:value = '{value}']"
    if t == "url":
        return f"[url:value = '{value}']"
    return None


def build(family: str) -> None:
    rows = load_rows(SLUG[family])
    identity = Identity(
        name="Emerging Threat Watch",
        identity_class="organization",
        description="Defensive threat-intelligence research package.",
    )
    malware = Malware(
        name=family,
        is_family=True,
        malware_types=["unknown"],
        description=f"ETW family {family}. Author attribution NOT_ESTABLISHED. Case-isolated.",
    )
    objs: list = [identity, malware]
    for row in rows:
        value = (row.get("indicator") or "").strip()
        pat = pattern_for(row.get("type") or "", value)
        if not pat:
            continue
        conf = {"High": 85, "Moderate": 60, "Low": 30}.get(
            (row.get("confidence") or "Moderate"), 50
        )
        ind = Indicator(
            name=f"{family} {(row.get('type') or '')} {value[:64]}",
            description=(
                f"evidence_id={row.get('evidence_id')}; "
                f"provenance={row.get('provenance')}; "
                f"confidence={row.get('confidence')}. NOT author attribution."
            ),
            pattern=pat,
            pattern_type="stix",
            valid_from=NOW,
            indicator_types=["malicious-activity"],
            confidence=conf,
        )
        rel = Relationship(
            relationship_type="indicates",
            source_ref=ind.id,
            target_ref=malware.id,
        )
        objs.extend([ind, rel])

    bundle = Bundle(*objs, allow_custom=True)
    out = OUT / family / "stix_bundle.json"
    out.write_text(bundle.serialize(pretty=True) + "\n", encoding="utf-8")
    print(family, "objects", len(objs), "->", out)


def main() -> None:
    for fam in FAMILIES:
        build(fam)


if __name__ == "__main__":
    main()
