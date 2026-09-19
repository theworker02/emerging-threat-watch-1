#!/usr/bin/env python3
"""Fetch primary research pages into evidence/primary-sources/ with SHA-256 manifests.

Does NOT create OBSERVED infrastructure rows. Passive retrieval ≠ independent infra observation.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EV = ROOT / "evidence"
PRIMARY = EV / "primary-sources"
PASSIVE = EV / "passive-observations"
MANIFESTS = EV / "manifests"
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 EmergingThreatWatch/1.0"
)
RETRIEVED = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

SOURCES = [
    {
        "evidence_id": "PS-RAP-001",
        "source_id": "SOURCE-RAP-001",
        "family": "rapuncel",
        "original_url": "https://blog.lastpass.com/posts/lastpass-delphos-report-rapuncel-infostealer",
        "publication_date": "2026-09-17",
        "publisher": "LastPass TIME + Delphos",
        "filename": "lastpass-delphos-rapuncel-2026-09-17.html",
        "notes": "Investigation state-as-of 2026-09-10 per article. Target: CONTENT-VERIFIED; FROZEN only after immutable archive retained.",
        "verify_strings": [
            "ea8c31a86fa785ab514022c278a2f6e571c86aac9283745a96605c44d88382d6",
            "albinofennel",
            "edgarcostartqd",
        ],
    },
    {
        "evidence_id": "PS-SET-001",
        "source_id": "SOURCE-SET-CYNET-SUMMARY",
        "family": "settra",
        "original_url": "https://www.cynet.com/blog/inside-cynets-settra-ransomware-investigation/",
        "publication_date": "2026-09-17",
        "publisher": "Cynet CyOps",
        "filename": "cynet-settra-summary-2026-09-17.html",
        "notes": "Summary companion; prefer long-form RE for technical depth.",
        "verify_strings": ["Settra", "exfiltrat"],
    },
    {
        "evidence_id": "PS-SET-002",
        "source_id": "SOURCE-SET-CYNET-LONG",
        "family": "settra",
        "original_url": "https://www.cynet.com/settra-ransomware-inside-a-new-enterprise-grade-extortion-threat/",
        "publication_date": "2026-09-17",
        "publisher": "Cynet Research Labs",
        "filename": "cynet-settra-longform-2026-09-17.html",
        "notes": "Primary RE: --pass, ~200k SHA-256, AES-256-CTR, LP77, offline encryptor, no exfil stack.",
        "verify_strings": ["Settra", "AES", "pass"],
    },
    {
        "evidence_id": "PS-SET-003",
        "source_id": "SOURCE-SET-HUNTRESS",
        "family": "settra",
        "original_url": "https://www.huntress.com/blog/new-settra-ransomware-variant",
        "publication_date": "2026-09",
        "publisher": "Huntress",
        "filename": "huntress-settra-2026-09.html",
        "notes": "Primary for MeshAgent IPs, WIN-LIVFRVQFMKO history, RaaS-negative statement.",
        "verify_strings": ["WIN-LIVFRVQFMKO", "45.13.122", "MeshAgent"],
    },
    {
        "evidence_id": "PS-RAT-001",
        "source_id": "SOURCE-RAT-ZIMP",
        "family": "rathat",
        "original_url": "https://zimperium.com/blog/rathat-ai-powered-mobile-threat-is-here-for-your-credentials-bank-accounts",
        "publication_date": "2026-09-16",
        "publisher": "Zimperium zLabs",
        "filename": "zimperium-rathat-2026-09-16.html",
        "notes": "Primary architecture + API surface + getevent/locateValues.json PIN reconstruction.",
        "verify_strings": ["liblocal-service", "getevent", "7910"],
    },
    {
        "evidence_id": "PS-NRB-001",
        "source_id": "SOURCE-NRB-SECURELIST",
        "family": "noderabbit",
        "original_url": "https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/",
        "publication_date": "2026-09-01",
        "publisher": "Kaspersky GReAT / Securelist",
        "filename": "securelist-noderabbit-2026-09-01.html",
        "notes": "NodeRabbit primary. May need alternate retrieval if distinctive strings absent.",
        "verify_strings": ["NodeRabbit", "Front-Technical-Challenge", "Copilot"],
    },
    {
        "evidence_id": "PS-NRB-002",
        "source_id": "SOURCE-NRB-MK-JULY",
        "family": "noderabbit",
        "original_url": "https://securelist.com/mirage-kitten-new-tools/120811/",
        "publication_date": "2026-07-28",
        "publisher": "Kaspersky GReAT / Securelist",
        "filename": "securelist-mirage-kitten-nightledger-2026-07-28.html",
        "notes": "Attribution/context only (NightLedger/ArcBridge/BridgeHead). NOT a substitute for NodeRabbit primary.",
        "verify_strings": ["NightLedger", "BridgeHead", "Mirage Kitten"],
    },
    {
        "evidence_id": "PS-SET-004",
        "source_id": "SOURCE-SET-MOXFIVE",
        "family": "settra",
        "original_url": "https://www.moxfive.com/blog/settra-ransomware-ttps-victims-and-defense-guide",
        "publication_date": "2026-07-22",
        "publisher": "MOXFIVE",
        "filename": "moxfive-settra-2026-07.html",
        "notes": "Operator TTPs primary IR.",
        "verify_strings": ["Settra", "MeshAgent"],
    },
]

PASSIVE_DIRS = [
    "certificate-transparency",
    "rdap",
    "dns",
    "urlscan",
    "github",
    "archives",
    "sample-metadata",
]

MANIFEST_FIELDS = [
    "evidence_id",
    "source_id",
    "original_url",
    "retrieved_utc",
    "content_type",
    "filename",
    "sha256",
    "collection_method",
    "publication_date",
    "publisher",
    "family",
    "provenance",
    "retrieval_status",
    "content_verified",
    "frozen",
    "bytes",
    "http_status",
    "verify_hits",
    "notes",
]


def ensure_tree() -> None:
    for fam in ["rapuncel", "settra", "rathat", "noderabbit"]:
        (PRIMARY / fam).mkdir(parents=True, exist_ok=True)
        keep = PRIMARY / fam / ".gitkeep"
        if not keep.exists():
            keep.write_text("", encoding="utf-8")
    for d in PASSIVE_DIRS:
        p = PASSIVE / d
        p.mkdir(parents=True, exist_ok=True)
        keep = p / ".gitkeep"
        if not keep.exists():
            keep.write_text("", encoding="utf-8")
    MANIFESTS.mkdir(parents=True, exist_ok=True)
    # README enforcing distinction
    (EV / "README.md").write_text(
        """# Evidence Tree — Emerging Threat Watch

Two tracks. Do not conflate them.

## `primary-sources/`
Immutable (or pending-freeze) copies of vendor/research publications.
Provenance: **PRIMARY-SOURCE**. Retrieval does **not** make campaign infrastructure `OBSERVED`.

## `passive-observations/`
Independent passive collection (CT, RDAP, DNS, urlscan, GitHub metadata, archives, sample metadata).
Only these results may be labeled **OBSERVED** — and only after method + timestamp are recorded.

## `manifests/`
- `primary-source-manifest.csv` — every primary fetch attempt
- `passive-observation-manifest.csv` — stays empty until passive collection runs

Status vocabulary for primary rows:
| Status | Meaning |
|--------|---------|
| UNRETRIEVED | Not obtained |
| RETRIEVED | Bytes saved locally |
| CONTENT-VERIFIED | Distinctive primary strings present in saved bytes |
| FROZEN | CONTENT-VERIFIED + intentional immutable retention (hash locked in ledger) |
""",
        encoding="utf-8",
    )
    # empty passive manifest if missing
    pman = MANIFESTS / "passive-observation-manifest.csv"
    if not pman.exists():
        with pman.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(
                f,
                fieldnames=[
                    "evidence_id",
                    "family",
                    "query",
                    "observation_type",
                    "value",
                    "first_seen",
                    "last_seen",
                    "asn",
                    "source",
                    "retrieved_utc",
                    "sha256_of_raw",
                    "filename",
                    "provenance",
                    "confidence",
                    "notes",
                ],
            )
            w.writeheader()
            # deliberately zero data rows — OBSERVED count remains 0


def fetch(url: str) -> tuple[int | None, bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml"})
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = resp.read()
            ctype = resp.headers.get("Content-Type", "application/octet-stream")
            return resp.status, data, ctype
    except urllib.error.HTTPError as e:
        body = e.read() if e.fp else b""
        return e.code, body, e.headers.get("Content-Type", "") if e.headers else ""
    except Exception as e:
        return None, str(e).encode("utf-8", errors="replace"), "error"


def main() -> None:
    ensure_tree()
    rows = []
    for src in SOURCES:
        fam_dir = PRIMARY / src["family"]
        out = fam_dir / src["filename"]
        status_code, data, ctype = fetch(src["original_url"])
        sha = hashlib.sha256(data).hexdigest() if data else ""
        text = ""
        try:
            text = data.decode("utf-8", errors="replace")
        except Exception:
            text = ""
        hits = [s for s in src["verify_strings"] if s.lower() in text.lower()]
        content_verified = len(hits) >= max(1, len(src["verify_strings"]) // 2) and status_code == 200
        retrieved = status_code == 200 and len(data) > 500
        if retrieved:
            out.write_bytes(data)
            # sidecar metadata
            meta = {
                "evidence_id": src["evidence_id"],
                "source_id": src["source_id"],
                "original_url": src["original_url"],
                "retrieved_utc": RETRIEVED,
                "sha256": sha,
                "http_status": status_code,
                "bytes": len(data),
                "content_verified": content_verified,
                "frozen": False,
                "verify_hits": hits,
            }
            (fam_dir / (src["filename"] + ".meta.json")).write_text(
                json.dumps(meta, indent=2), encoding="utf-8"
            )
            retrieval_status = "CONTENT-VERIFIED" if content_verified else "RETRIEVED"
        else:
            # save error stub for audit trail
            stub = fam_dir / (src["filename"] + ".FETCH_FAILED.txt")
            stub.write_text(
                f"url={src['original_url']}\nhttp_status={status_code}\nbytes={len(data)}\n"
                f"sha256={sha}\nretrieved_utc={RETRIEVED}\npreview={text[:500]!r}\n",
                encoding="utf-8",
            )
            retrieval_status = "UNRETRIEVED"
            content_verified = False

        row = {
            "evidence_id": src["evidence_id"],
            "source_id": src["source_id"],
            "original_url": src["original_url"],
            "retrieved_utc": RETRIEVED,
            "content_type": ctype,
            "filename": src["filename"] if retrieved else (src["filename"] + ".FETCH_FAILED.txt"),
            "sha256": sha,
            "collection_method": "HTTP GET (urllib) with browser UA; passive document retrieval only",
            "publication_date": src["publication_date"],
            "publisher": src["publisher"],
            "family": src["family"],
            "provenance": "PRIMARY-SOURCE",
            "retrieval_status": retrieval_status,
            "content_verified": str(content_verified).lower(),
            "frozen": "false",
            "bytes": str(len(data)),
            "http_status": str(status_code),
            "verify_hits": ";".join(hits),
            "notes": src["notes"],
        }
        rows.append(row)
        print(
            f"{src['evidence_id']}: http={status_code} status={retrieval_status} "
            f"verified={content_verified} hits={hits} bytes={len(data)}"
        )

    man = MANIFESTS / "primary-source-manifest.csv"
    with man.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=MANIFEST_FIELDS)
        w.writeheader()
        w.writerows(rows)
    print("manifest ->", man)


if __name__ == "__main__":
    main()
