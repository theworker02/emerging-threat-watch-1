#!/usr/bin/env python3
"""Build LE-oriented CTI-Evidence-Repository from published-indicators (no invented IOCs)."""
from __future__ import annotations

import csv
import hashlib
import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "reports" / "law-enforcement" / "CTI-Evidence-Repository"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
CREATED = NOW

FAMILIES = [
    ("Rapuncel", "rapuncel", "Windows info stealer / GitHub-SEO distribution"),
    ("Settra", "settra", "Enterprise ransomware + operator intrusion"),
    ("RatHat", "rathat", "Android Accessibility / Wireless ADB RAT"),
    ("NodeRabbit", "noderabbit", "Cross-platform Node.js developer-targeted RAT"),
    ("PollCat", "pollcat", "Obfuscated JavaScript RAT (Mirage Kitten co-disclosure)"),
    ("SynkLoader", "synkloader", "Teams phishing modular loader"),
    ("Showboat", "showboat", "Linux modular post-exploitation / telecom targeting"),
]

IOC_HEADERS = [
    "indicator_type",
    "value",
    "first_seen_utc",
    "last_seen_utc",
    "confidence",
    "provenance",
    "evidence_id",
    "notes",
]


def stix_id(kind: str) -> str:
    return f"{kind}--{uuid.uuid4()}"


def load_indicators(slug: str) -> list[dict]:
    p = ROOT / "investigations" / slug / "evidence" / "published-indicators.csv"
    if not p.exists():
        return []
    with p.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def classify(ind_type: str) -> str | None:
    t = (ind_type or "").lower()
    if t in ("ipv4", "ip", "ipv6"):
        return "ips"
    if t in ("domain", "hostname", "url", "uri_path"):
        return "domains"
    if t in ("sha256", "md5", "sha1", "hash"):
        return "hashes"
    return None


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=IOC_HEADERS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in IOC_HEADERS})


def build_stix(family: str, slug: str, rows: list[dict]) -> dict:
    bundle_id = stix_id("bundle")
    objects = []
    identity = {
        "type": "identity",
        "spec_version": "2.1",
        "id": stix_id("identity"),
        "created": CREATED,
        "modified": CREATED,
        "name": "Emerging Threat Watch",
        "identity_class": "organization",
        "description": "Defensive threat-intelligence research package (not a formal LE agency).",
    }
    objects.append(identity)
    malware = {
        "type": "malware",
        "spec_version": "2.1",
        "id": stix_id("malware"),
        "created": CREATED,
        "modified": CREATED,
        "name": family,
        "is_family": True,
        "malware_types": ["unknown"],
        "description": f"ETW case {slug}. See family SUMMARY.md. Case-isolated; no cross-family attribution without evidence.",
    }
    objects.append(malware)

    for row in rows:
        value = (row.get("indicator") or "").strip()
        if not value:
            continue
        itype = (row.get("type") or "").lower()
        conf = (row.get("confidence") or "Moderate").capitalize()
        prov = row.get("provenance") or "PRIMARY-SOURCE"
        eid = row.get("evidence_id") or ""
        pattern = None
        ind_types = []
        if itype in ("sha256",):
            pattern = f"[file:hashes.'SHA-256' = '{value.lower()}']"
            ind_types = ["file"]
        elif itype in ("md5",):
            pattern = f"[file:hashes.MD5 = '{value.lower()}']"
            ind_types = ["file"]
        elif itype in ("ipv4", "ip"):
            pattern = f"[ipv4-addr:value = '{value}']"
            ind_types = ["ipv4-addr"]
        elif itype == "domain":
            pattern = f"[domain-name:value = '{value}']"
            ind_types = ["domain-name"]
        elif itype == "url":
            pattern = f"[url:value = '{value}']"
            ind_types = ["url"]
        else:
            # skip behavioral/path artifacts in STIX pattern for validity
            continue
        ind = {
            "type": "indicator",
            "spec_version": "2.1",
            "id": stix_id("indicator"),
            "created": CREATED,
            "modified": CREATED,
            "name": f"{family} {itype} {value[:48]}",
            "description": f"evidence_id={eid}; provenance={prov}; confidence={conf}. NOT author attribution.",
            "indicator_types": ["malicious-activity"],
            "pattern": pattern,
            "pattern_type": "stix",
            "valid_from": CREATED,
            "confidence": {"High": 85, "Moderate": 60, "Low": 30}.get(conf, 50),
        }
        objects.append(ind)
        objects.append(
            {
                "type": "relationship",
                "spec_version": "2.1",
                "id": stix_id("relationship"),
                "created": CREATED,
                "modified": CREATED,
                "relationship_type": "indicates",
                "source_ref": ind["id"],
                "target_ref": malware["id"],
            }
        )

    return {
        "type": "bundle",
        "id": bundle_id,
        "objects": objects,
    }


def family_summary(family: str, slug: str, category: str, rows: list[dict]) -> str:
    ips = [r for r in rows if (r.get("type") or "").lower() in ("ipv4", "ip")]
    doms = [r for r in rows if (r.get("type") or "").lower() == "domain"]
    hashes = [r for r in rows if (r.get("type") or "").lower() in ("sha256", "md5")]
    return f"""# {family} — Family Summary

**Case ID slug:** `{slug}`  
**Category:** {category}  
**TLP:** TLP:AMBER+STRICT (see repository `TLP-LICENSE.md`)  
**Generated:** {NOW}  
**Source:** Emerging Threat Watch published-indicators (no invented IOCs)

## Executive overview

Defensive threat-intelligence package for **{family}**. Indicators below are transcribed from vendor PRIMARY-SOURCE reporting and/or ETW OBSERVED_PASSIVE collection. **Author personal identity / home IP is NOT ESTABLISHED.**

## Indicator counts (this build)

| Class | Count |
|-------|------:|
| Domains / URLs / URI paths (domain-class export) | {len(doms)} |
| IPs | {len(ips)} |
| Hashes (SHA-256/MD5) | {len(hashes)} |
| Total published-indicator rows | {len(rows)} |

## Machine-readable

- STIX 2.1: `stix_bundle.json`
- IOCs: `iocs/ips.csv`, `iocs/domains.csv`, `iocs/hashes.csv`

## Evidence folders (placeholders until lab fills)

| Folder | Status |
|--------|--------|
| `network_captures/` | Empty — requires human/licensed sandbox PCAP (see ENFORCEMENT_READINESS) |
| `memory_dumps/` | Empty — no ETW decrypted stubs in-repo |
| `rules/` | Stub YARA/Sigma placeholders — expand when signatures are validated |
| `actors_and_finance/` | No crypto wallets established for this family in ETW corpus |

## Case isolation

Do not merge with other ETW families without linkage evidence. PollCat ↔ NodeRabbit: COMMON TECHNIQUE / Moderate delivery overlap only — **not** shared authorship.

## Cross-references (full research corpus)

- Investigation: `investigations/{slug}/`
- LE narrative package: `reports/law-enforcement/packages/`
- Enforcement readiness: `docs/ENFORCEMENT_READINESS.md`
""".replace("{slug}", slug)


PLACEHOLDER_RULES_YARA = """rule ETW_PLACEHOLDER_DoNotDeploy
{
    meta:
        description = "Placeholder — replace with validated family signatures before operational use"
        author = "Emerging Threat Watch"
        tlp = "AMBER"
        reference = "investigations/"
    condition:
        false
}
"""

PLACEHOLDER_SIGMA = """title: ETW Placeholder — Do Not Deploy
id: 00000000-0000-0000-0000-000000000000
status: experimental
description: Placeholder Sigma rule. Replace with validated detections before SIEM use.
logsource:
    product: windows
detection:
    selection:
        EventID: 0
    condition: selection
falsepositives:
    - Placeholder never matches
level: informational
"""


def ensure_placeholders(fam_dir: Path, family: str) -> None:
    (fam_dir / "network_captures").mkdir(parents=True, exist_ok=True)
    (fam_dir / "memory_dumps").mkdir(parents=True, exist_ok=True)
    (fam_dir / "network_captures" / "README.md").write_text(
        f"# Network captures — {family}\n\n"
        "Place timed `.pcap` / `.pcapng` files here from **human isolated lab** or licensed "
        "sandbox (ANY.RUN / Triage / Hybrid Analysis). Autonomous ETW collectors do not execute malware.\n\n"
        "Required for hosting-provider takedown packages (see `TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`).\n",
        encoding="utf-8",
    )
    (fam_dir / "memory_dumps" / "README.md").write_text(
        f"# Memory dumps / configs — {family}\n\n"
        "Place decrypted stubs, extracted C2 configs, and dump artifacts here. "
        "Hash every file and update repository CHECKSUMS.\n",
        encoding="utf-8",
    )
    rules = fam_dir / "rules"
    rules.mkdir(parents=True, exist_ok=True)
    (rules / "yara.yar").write_text(PLACEHOLDER_RULES_YARA, encoding="utf-8")
    (rules / "sigma.yml").write_text(PLACEHOLDER_SIGMA, encoding="utf-8")
    (rules / "README.md").write_text(
        "Placeholder rules (`condition: false` / never-match). Replace before operational use. Lint via CI.\n",
        encoding="utf-8",
    )
    af = fam_dir / "actors_and_finance"
    af.mkdir(parents=True, exist_ok=True)
    (af / "wallets.txt").write_text(
        "# No cryptocurrency wallet addresses established in ETW corpus for this family.\n"
        "# Add BTC/XMR/USDT/ETH addresses only with PRIMARY-SOURCE or OBSERVED_PASSIVE provenance.\n",
        encoding="utf-8",
    )
    (af / "handle_correlations.json").write_text(
        json.dumps(
            {
                "family": family,
                "forum_handles": [],
                "telegram_ids": [],
                "discord_ids": [],
                "notes": "Empty by design until evidenced. Do not invent handles.",
                "author_attribution": "NOT_ESTABLISHED",
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (af / "ssl_jarm_pdb.md").write_text(
        f"# SSL / JARM / PDB — {family}\n\n"
        "| Asset | Value | Provenance |\n|-------|-------|------------|\n"
        "| TLS cert fingerprint | _pending bounded Censys/Shodan on ledger IPs_ | — |\n"
        "| JARM | _pending_ | — |\n"
        "| PDB paths | _pending sample RE_ | — |\n\n"
        "Fill only from OBSERVED_PASSIVE or PRIMARY sample analysis. Never fabricate.\n",
        encoding="utf-8",
    )


def sha256_file(path: Path) -> str:
    """SHA-256 of file bytes with CRLF normalized to LF.

    Working trees on Windows often checkout text as CRLF while git stores LF.
    CI (Linux) and the committed CHECKSUMS.sha256 must agree on LF bytes.
    """
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    schemas = OUT / "schemas"
    schemas.mkdir(exist_ok=True)
    # Minimal note pointing to STIX — full OASIS schema is huge; CI uses stix2-validator
    (schemas / "README.md").write_text(
        "STIX 2.1 validation uses the `stix2-validator` package in CI "
        "(official OASIS schemas). Family `stix_bundle.json` files are generated by "
        "`shared/tooling/build_cti_evidence_repository.py`.\n",
        encoding="utf-8",
    )

    matrix_rows = []
    all_hash_targets: list[Path] = []

    for family, slug, category in FAMILIES:
        rows = load_indicators(slug)
        fam_dir = OUT / "families" / family
        fam_dir.mkdir(parents=True, exist_ok=True)
        (fam_dir / "SUMMARY.md").write_text(
            family_summary(family, slug, category, rows), encoding="utf-8"
        )

        by = {"ips": [], "domains": [], "hashes": []}
        for r in rows:
            bucket = classify(r.get("type") or "")
            if not bucket:
                # still put uri_path etc. into domains as "other" typed
                t = (r.get("type") or "").lower()
                if t in ("uri_path", "url", "path", "filename", "filename_pattern", "local_service"):
                    bucket = "domains"
                elif t in ("extension", "service", "device", "behavioral", "command", "manifest_chunk", "port", "artifact"):
                    continue
                else:
                    continue
            by[bucket].append(
                {
                    "indicator_type": r.get("type") or "",
                    "value": r.get("indicator") or "",
                    "first_seen_utc": r.get("first_seen") or r.get("retrieval_date_utc") or "",
                    "last_seen_utc": r.get("retrieval_date_utc") or "",
                    "confidence": r.get("confidence") or "",
                    "provenance": r.get("provenance") or "",
                    "evidence_id": r.get("evidence_id") or "",
                    "notes": (r.get("notes") or "")[:500],
                }
            )

        iocs = fam_dir / "iocs"
        write_csv(iocs / "ips.csv", by["ips"])
        write_csv(iocs / "domains.csv", by["domains"])
        write_csv(iocs / "hashes.csv", by["hashes"])

        stix = build_stix(family, slug, rows)
        stix_path = fam_dir / "stix_bundle.json"
        stix_path.write_text(json.dumps(stix, indent=2) + "\n", encoding="utf-8")

        ensure_placeholders(fam_dir, family)

        # primary C2 summary for matrix
        non_cdn_ips = [
            r["value"]
            for r in by["ips"]
            if "cloudflare" not in (r.get("notes") or "").lower()
            and "cdn" not in (r.get("notes") or "").lower()
        ][:3]
        c2_cell = ", ".join(non_cdn_ips) if non_cdn_ips else (by["domains"][0]["value"] if by["domains"] else "See iocs/")
        matrix_rows.append(
            {
                "family": family,
                "category": category,
                "c2": c2_cell,
                "crypto": "N/A (none established)",
                "stix": f"./families/{family}/stix_bundle.json",
                "ips": len(by["ips"]),
                "domains": len(by["domains"]),
                "hashes": len(by["hashes"]),
            }
        )
        all_hash_targets.extend(
            [
                fam_dir / "SUMMARY.md",
                stix_path,
                iocs / "ips.csv",
                iocs / "domains.csv",
                iocs / "hashes.csv",
            ]
        )

    # TLP
    (OUT / "TLP-LICENSE.md").write_text(
        """# Traffic Light Protocol

**Classification:** TLP:AMBER+STRICT

## Meaning

Recipients may share **only** with their organization and with clients or customers who need to know to protect themselves or prevent further harm. **Do not** publish publicly (social media, blogs, public GitHub mirrors of unredacted packages) without explicit authorization from the package maintainer.

## Rationale

This package aggregates campaign infrastructure indicators and research derived from vendor publications and passive collection. Misuse could tip operators or harm investigations.

## Clearance for LE / CISA / HSI / FBI

Sharing with federal cyber investigators and designated ISACs under TLP:AMBER+STRICT is intended. Contact the Point of Contact in `README.md` for unredacted PCAPs (when available) or GPG-encrypted channels.

## Not TLP:CLEAR

Public research summaries may exist elsewhere in the Emerging Threat Watch main repository under more open terms; **this** `CTI-Evidence-Repository` tree is the LE handoff surface and remains AMBER+STRICT.
""",
        encoding="utf-8",
    )

    # Root README
    matrix_md = "\n".join(
        f"| **{r['family']}** | {r['category']} | `{r['c2']}` | {r['crypto']} | `{r['stix']}` |"
        for r in matrix_rows
    )
    counts_md = "\n".join(
        f"| {r['family']} | {r['ips']} | {r['domains']} | {r['hashes']} |" for r in matrix_rows
    )
    (OUT / "README.md").write_text(
        f"""# Evidentiary Threat Intelligence Package

## Executive Summary

This repository folder contains **actionable technical telemetry** structured for automated ingestion and federal analyst review (FBI / HSI / CISA and partners). It covers Emerging Threat Watch **active cases**:

**Rapuncel, Settra, RatHat, NodeRabbit, PollCat, SynkLoader, Showboat.**

Commodity/MaaS families such as AsyncRAT, Remcos, Lumma Stealer, and Matanbuchus are tracked as **candidates / technique comparators** in the parent repo (`docs/CANDIDATE_FAMILIES.md`) and are **not** full evidence trees here until promoted.

## Chain of Custody & Integrity

- **Collection / research cutoff (v1):** 2026-09-19 (ongoing passive enrichment may append newer `retrieved_utc` stamps)
- **Integrity verification:** SHA-256 of package text/CSV/STIX artifacts listed in `CHECKSUMS.sha256`. When GPG-signed, also see `CHECKSUMS.asc` (gitignored if present).
- **Classification / TLP:** **TLP:AMBER+STRICT** — see `TLP-LICENSE.md`
- **Provenance:** Indicators carry PRIMARY-SOURCE / OBSERVED_PASSIVE labels. Retrieving vendor articles ≠ independent infra observation. **Author attribution = NOT ESTABLISHED** unless a public LE/court source says otherwise.
- **No malware binaries** are stored in this package (see parent `.gitignore`). PCAPs/memory dumps are placeholders until human-lab fills them.

## Key Threat Summary Matrix

| Threat Family | Category | Primary C2 / Infra leads | Crypto / Financial Identifiers | STIX 2.1 File |
| :--- | :--- | :--- | :--- | :--- |
{matrix_md}

### Indicator inventory (this build)

| Family | IPs | Domains/URLs | Hashes |
|--------|----:|-------------:|-------:|
{counts_md}

## Directory map

```
CTI-Evidence-Repository/
├── README.md                 ← this cover sheet
├── TLP-LICENSE.md
├── CHECKSUMS.sha256
├── schemas/
└── families/<Family>/
    ├── SUMMARY.md
    ├── stix_bundle.json
    ├── iocs/{{ips,domains,hashes}}.csv
    ├── network_captures/     ← lab PCAPs (placeholder)
    ├── memory_dumps/         ← configs/dumps (placeholder)
    ├── rules/{{yara.yar,sigma.yml}}
    └── actors_and_finance/
```

## Point of Contact

For law enforcement inquiries, raw unredacted `.pcap` files (when available), or encrypted GPG communication:

| Field | Value |
|-------|-------|
| Project | Emerging Threat Watch |
| GitHub tips | See parent `docs/SUBMIT_INTEL.md` |
| Contact name | _[TO BE FILLED]_ |
| Email / Signal | _[TO BE FILLED]_ |
| PGP fingerprint | _[TO BE FILLED]_ |
| Related IC3 / FBI tip numbers | See `../MASTER_INDEX.csv` |

## Related parent-repo paths

- Narrative IC3/FBI packages: `../packages/`
- Comprehensive private dossier: `../SUBMISSION_REPORT.md` (gitignored)
- Takedown template: `../TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`
- Methodology: `../../../shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`
- Enforcement readiness: `../../../docs/ENFORCEMENT_READINESS.md`

## Rebuild

```bash
python shared/tooling/build_cti_evidence_repository.py
```

Generated: {NOW}
""",
        encoding="utf-8",
    )

    # CHECKSUMS.sha256
    lines = []
    for p in sorted(all_hash_targets):
        if p.exists() and p.is_file():
            rel = p.relative_to(OUT).as_posix()
            lines.append(f"{sha256_file(p)}  {rel}")
    # also hash README and TLP
    for name in ("README.md", "TLP-LICENSE.md"):
        p = OUT / name
        lines.insert(0, f"{sha256_file(p)}  {name}")
    (OUT / "CHECKSUMS.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Prefer official stix2 library bundles when available
    try:
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "rebuild_stix_bundles",
            Path(__file__).resolve().parent / "rebuild_stix_bundles.py",
        )
        mod = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(mod)
        mod.main()
        lines2 = []
        for line in (OUT / "CHECKSUMS.sha256").read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            digest, path = line.split(None, 1)
            p = OUT / path
            if p.exists():
                lines2.append(f"{sha256_file(p)}  {path}")
            else:
                lines2.append(line)
        (OUT / "CHECKSUMS.sha256").write_text("\n".join(lines2) + "\n", encoding="utf-8")
    except Exception as e:
        print("NOTE: stix2 rebuild skipped:", e)

    # CHAIN_OF_CUSTODY note
    (OUT / "CHAIN_OF_CUSTODY.md").write_text(
        f"""# Chain of Custody Notes

**Package root:** `reports/law-enforcement/CTI-Evidence-Repository/`  
**Built:** {NOW}  
**Builder:** `shared/tooling/build_cti_evidence_repository.py`

## What is attested

1. CSV/STIX/SUMMARY text artifacts listed in `CHECKSUMS.sha256` (SHA-256 of file bytes at build time).
2. Provenance columns on IOC CSVs (PRIMARY-SOURCE / OBSERVED_PASSIVE).
3. Empty `network_captures/` and `memory_dumps/` — **no** binary evidence claimed until files are added and checksums regenerated.

## What is not attested

- Live malware execution by ETW autonomous collectors
- Authentication to attacker C2 panels
- Cryptocurrency wallet ownership
- Personal author/home IP attribution

## Adding lab evidence

1. Drop `.pcapng` / dumps into the family folders.
2. Re-run `build_cti_evidence_repository.py` **or** append hashes manually to `CHECKSUMS.sha256`.
3. Optionally GPG-sign: `gpg --clearsign CHECKSUMS.sha256` → `CHECKSUMS.asc` (keep private/gitignored if desired).
""",
        encoding="utf-8",
    )

    print(f"Built {OUT}")
    for r in matrix_rows:
        print(f"  {r['family']}: ips={r['ips']} domains={r['domains']} hashes={r['hashes']}")


if __name__ == "__main__":
    main()
