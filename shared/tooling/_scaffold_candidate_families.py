#!/usr/bin/env python3
"""One-shot scaffolder: candidate/comparator family stubs (~15 total case folders).

Does not invent PRIMARY IOCs. Safe to re-run (overwrites stub text files).
"""
from __future__ import annotations

import json
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NOW = "2026-09-19T20:30:00Z"
NS = uuid.UUID("6ba7b810-9dad-11d1-80b4-00c04fd430c8")

FAMILIES = [
    dict(
        slug="abyssos",
        display="Abyssos",
        code="ABY",
        pkg="08-abyssos",
        pkg_id="ETW-ABY-IC3",
        status="CANDIDATE",
        kind="candidate",
        category="Modular RAT",
        platform="Windows (vendor-reported)",
        disclosure="Zscaler Aug 2026",
        why="Modular RAT; young corpus; high autonomous-collection value",
        primary_org="Zscaler",
        primary_url="UNVERIFIED — freeze primary URL before IOC ingest",
        comparator_note="Standalone candidate. Do not merge with active ETW families.",
        tip="Young modular RAT corpus — prioritize primary URL freeze + sparse CT/pDNS collection.",
    ),
    dict(
        slug="sharkloader",
        display="SharkLoader",
        code="SHK",
        pkg="09-sharkloader",
        pkg_id="ETW-SHK-IC3",
        status="CANDIDATE",
        kind="candidate",
        category="Custom loader → Cobalt Strike",
        platform="Windows",
        disclosure="Kaspersky June 2026",
        why="Custom loader leading to Cobalt Strike",
        primary_org="Kaspersky",
        primary_url="UNVERIFIED — freeze primary URL before IOC ingest",
        comparator_note="Standalone candidate. Loader→CS is COMMON TECHNIQUE class only vs other loaders.",
        tip="Loader→Cobalt Strike delivery chain; no CS beacon hashes invented here.",
    ),
    dict(
        slug="tencshell",
        display="TencShell",
        code="TEN",
        pkg="10-tencshell",
        pkg_id="ETW-TEN-IC3",
        status="CANDIDATE",
        kind="candidate",
        category="Go implant (Rshell OSS lineage problem)",
        platform="Cross-platform (vendor-reported)",
        disclosure="Cato CTRL 2026",
        why="Go implant; Rshell OSS lineage problem",
        primary_org="Cato CTRL",
        primary_url="UNVERIFIED — freeze primary URL before IOC ingest",
        comparator_note="OSS lineage similarity ≠ shared operators. Authorship NOT_ESTABLISHED.",
        tip="Track OSS Rshell overlap carefully; do not treat public Rshell as TencShell IOCs.",
    ),
    dict(
        slug="minifast",
        display="MiniFast",
        code="MNF",
        pkg="11-minifast",
        pkg_id="ETW-MNF-IC3",
        status="CANDIDATE",
        kind="candidate",
        category="Loader / Zoom installer trust abuse (Nimbus Manticore context)",
        platform="Windows",
        disclosure="Check Point May 2026",
        why="Nimbus Manticore; Zoom installer trust abuse; PollCat C2 structural overlap noted in candidate notes",
        primary_org="Check Point",
        primary_url="UNVERIFIED — freeze primary URL before IOC ingest",
        comparator_note=(
            "Context for PollCat lineage assessment only — do NOT auto-merge into POL case. "
            "authorship_link=NOT_ESTABLISHED."
        ),
        tip="Zoom trust-abuse delivery; structural C2 notes vs PollCat are ASSOCIATION_ONLY until primary freeze.",
    ),
    dict(
        slug="argamal",
        display="Argamal",
        code="ARG",
        pkg="12-argamal",
        pkg_id="ETW-ARG-IC3",
        status="CANDIDATE",
        kind="candidate",
        category="RAT (trojanized adult games)",
        platform="Windows (vendor-reported)",
        disclosure="Kaspersky June 2026",
        why="Trojanized adult games RAT",
        primary_org="Kaspersky",
        primary_url="UNVERIFIED — freeze primary URL before IOC ingest",
        comparator_note="Standalone candidate. Case-isolated from all active families.",
        tip="Trojanized game distribution surface; no lure URLs invented.",
    ),
    dict(
        slug="okobot",
        display="Okobot",
        code="OKO",
        pkg="13-okobot",
        pkg_id="ETW-OKO-IC3",
        status="CANDIDATE",
        kind="candidate",
        category="Multi-payload spyware / loader ecosystem (OkoSpyware alias tracking)",
        platform="Multi (vendor-reported)",
        disclosure="Kaspersky (investigation start Jan 2026)",
        why="20+ payloads; 25+ countries; broad geographic footprint",
        primary_org="Kaspersky",
        primary_url="UNVERIFIED — freeze primary URL before IOC ingest",
        comparator_note="Alias OkoSpyware tracked here only. Do not invent payload inventory.",
        tip="Broad multi-payload campaign; stub only until primary sources frozen.",
    ),
    dict(
        slug="matanbuchus",
        display="Matanbuchus",
        code="MAT",
        pkg="14-matanbuchus",
        pkg_id="ETW-MAT-IC3",
        status="CANDIDATE_COMPARATOR",
        kind="technique_comparator",
        category="MaaS loader+RAT (Teams/ClickFix; ChaCha20)",
        platform="Windows",
        disclosure="Elastic/Checkpoint/community; BelialDemon XSS/Exploit ads",
        why="Russian-linked MaaS; technique comparator for SynkLoader (Teams+ChaCha20)",
        primary_org="Multiple vendors",
        primary_url="UNVERIFIED — freeze primary URL before IOC ingest",
        comparator_note=(
            "COMMON TECHNIQUE comparator for SynkLoader only. authorship_link SynkLoader=NOT_ESTABLISHED. "
            "See docs/TECHNIQUE_COMPARATORS.md. AstarionRAT tracked as related MaaS note — not merged IOCs."
        ),
        tip="Do not claim Matanbuchus is SynkLoader lineage. Comparator folder for defensive tradecraft only.",
    ),
    dict(
        slug="starlandrat",
        display="StarlandRAT",
        code="STR",
        pkg="15-starlandrat",
        pkg_id="ETW-STR-IC3",
        status="CANDIDATE",
        kind="candidate",
        category="Python RAT / PowerShell implant (WLDR Agent companion tracking)",
        platform="Windows",
        disclosure="Cisco Talos UAT-11795 / public vendor coverage",
        why="Telegram + Polygon contract C2 fallback; fits ETW tracker/Telegram OSINT methodology",
        primary_org="Cisco Talos",
        primary_url="UNVERIFIED — freeze primary URL before IOC ingest",
        comparator_note=(
            "WLDR Agent is companion tracking under this case folder until distinct corpus warrants split. "
            "Do not attribute to active ETW families."
        ),
        tip="Telegram/Polygon C2 class is methodology-relevant; no contract addresses or bot handles invented.",
    ),
]

INV_DIRS = [
    "analysis/behavioral",
    "analysis/c2",
    "analysis/relationships",
    "analysis/signatures",
    "analysis/static",
    "analysis/strings",
    "attack/navigator",
    "claims",
    "detections/hunting",
    "detections/network",
    "detections/sigma",
    "detections/validation",
    "detections/yara",
    "docs/deep-pass",
    "evidence/certificates",
    "evidence/dns",
    "evidence/metadata",
    "evidence/observations",
    "evidence/repositories",
    "evidence/screenshots",
    "evidence/web",
    "gaps",
    "infrastructure",
    "iocs/STIX",
    "lineage",
    "references",
    "samples",
    "timelines",
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def touch_gitkeep(d: Path) -> None:
    d.mkdir(parents=True, exist_ok=True)
    gk = d / ".gitkeep"
    if not gk.exists():
        gk.write_text("", encoding="utf-8")


def scaffold_one(f: dict) -> None:
    slug, disp, code = f["slug"], f["display"], f["code"]
    inv = ROOT / "investigations" / slug
    for sub in INV_DIRS:
        touch_gitkeep(inv / sub)

    write(
        inv / "README.md",
        f"""# {disp} Investigation (Candidate Stub)

**Status:** `{f['status']}` — case folder stub  
**Case ID:** `{slug}`  
**Case code:** `{code}` / `{f['pkg_id']}`  
**Kind:** `{f['kind']}`  
**Independence:** Isolated from all other ETW families. Technique/market comparisons are COMMON TECHNIQUE / ASSOCIATION_ONLY only.  
**IOC policy:** No PRIMARY hashes, domains, or C2 IPs invented. Placeholders are UNVERIFIED until primary URL freeze.

## Research thesis (candidate — not promoted)

- First/major disclosure framing: **{f['disclosure']}**
- Why it fits Emerging Threat Watch: {f['why']}
- Primary research org (candidate catalog): {f['primary_org']}
- Primary URL: {f['primary_url']}
- {f['comparator_note']}

## Research emphasis

- {f['tip']}
- Promote only after: primary URL freeze, evidence-id prefixes assigned, human decision (see `docs/CANDIDATE_FAMILIES.md`).

## Status

Candidate / comparator **skeleton only**. Empty IOC ledgers are intentional. See `docs/CANDIDATE_FAMILIES.md` and `docs/TECHNIQUE_COMPARATORS.md`.
""",
    )

    write(
        inv / "PHASE1_BASELINE_REPORT.md",
        f"""# {disp} — Phase 1 Baseline (CANDIDATE STUB)

**Generated:** {NOW}  
**Status:** `{f['status']}` — not an active Phase-1 freeze corpus

## Summary

{disp} is tracked as a **candidate/comparator case folder** so Emerging Threat Watch can host notes, source freeze work, and passive collection seeds without inventing indicators.

| Field | Value |
|-------|-------|
| Family | {disp} |
| Case code | {code} |
| Disclosure framing | {f['disclosure']} |
| PRIMARY IOCs in this stub | **None** |
| Independently observed infra | **None** |
| Author attribution | **NOT_ESTABLISHED** |

## Next promotion gates

1. Freeze at least one PRIMARY-SOURCE URL into `evidence/source-index.csv`
2. Transcribe published IOCs only (never invent)
3. Human decision to mark priority `ADDED` in `docs/CANDIDATE_FAMILIES.md`

## Cross-references

- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
- Technique comparators: `docs/TECHNIQUE_COMPARATORS.md`
- CTI stub: `reports/law-enforcement/CTI-Evidence-Repository/families/{disp}/`
- LE stub package: `reports/law-enforcement/packages/{f['pkg']}/`
""",
    )

    write(
        inv / "claims" / "claims-ledger.csv",
        "claim_id,family,case_id,claim,source_organization,source_team,source_title,source_url,published,source_type,status,confidence,independently_verified,evidence_tags,related_evidence_ids,derives_from,notes,retrieval_date_utc,cutoff_applies\n"
        f'{code}-CLAIM-0001,{disp},{code},"Candidate catalog entry: {f["why"]}",Emerging Threat Watch candidate pipeline,,CANDIDATE_FAMILIES.md,docs/CANDIDATE_FAMILIES.md,2026,INTERNAL,UNVERIFIED,Low,false,pipeline,,,,ASSOCIATION_ONLY stub — freeze vendor PRIMARY before elevating.,{NOW},true\n',
    )

    write(
        inv / "evidence" / "published-indicators.csv",
        "evidence_id,family,indicator,type,first_seen,provenance,confidence,independently_verified,source_url,retrieval_date_utc,notes,status_label\n"
        f"{code}-IND-0000,{disp},NO_PRIMARY_IOCS_YET,placeholder,unspecified,UNVERIFIED,None,false,{f['primary_url']},{NOW},Intentional empty corpus — do not invent hashes/domains/IPs.,UNVERIFIED\n",
    )

    write(
        inv / "evidence" / "source-index.csv",
        "source_id,title,url,organization_or_author,publication_date,retrieval_date,source_tier,case_ids,notes\n"
        f'SOURCE-{code}-000,UNVERIFIED primary — freeze before IOC ingest,{f["primary_url"]},{f["primary_org"]},unspecified,{NOW},UNVERIFIED,{slug},"Candidate stub; primary URL not frozen"\n',
    )

    write(
        inv / "evidence" / "evidence-ledger.csv",
        "evidence_id,family,artifact_type,path_or_ref,retrieved_date_utc,sha256,provenance,notes\n"
        f"{code}-EV-0000,{disp},stub_note,investigations/{slug}/README.md,{NOW},,INTERNAL,Candidate skeleton only\n",
    )

    write(
        inv / "gaps" / "priority-gaps.csv",
        "priority,family,gap,why_crucial,status\n"
        f"P0,{disp},Freeze PRIMARY-SOURCE URL and archive HTML/PDF bytes,Cannot promote without primary freeze,OPEN\n"
        f"P0,{disp},Transcribe published IOCs into {code}-IND rows (no invention),Empty ledger is intentional until primary exists,OPEN\n"
        f"P1,{disp},Assess technique/market overlap labels vs active families,Must keep authorship_link=NOT_ESTABLISHED unless proven,OPEN\n",
    )

    ioc_header = "value,type,first_seen,last_seen,source,confidence,campaign_association,status,notes,case_id\n"
    for name in ("hashes.csv", "domains.csv", "urls.csv", "combined.csv"):
        write(
            inv / "iocs" / name,
            ioc_header + f"# No PRIMARY IOCs — UNVERIFIED candidate stub for {disp}\n",
        )

    write(
        inv / "iocs" / "STIX" / "README.md",
        f"# STIX — {disp}\n\nEmpty until PRIMARY indicators exist. Do not invent indicators for STIX export.\n",
    )
    write(
        inv / "timelines" / "master-timeline.csv",
        "event_id,timestamp_utc,event_type,summary,source,provenance,confidence,evidence_id\n"
        f'{code}-TL-0001,unspecified,candidate_catalog,"{disp} listed in docs/CANDIDATE_FAMILIES.md",ETW candidate pipeline,INTERNAL,Low,{code}-EV-0000\n',
    )
    write(
        inv / "attack" / "techniques.md",
        f"# ATT&CK — {disp} (UNVERIFIED stub)\n\n"
        f"No techniques mapped yet. Map only from PRIMARY-SOURCE reporting after URL freeze.\n\n"
        f"Status: `{f['status']}`\n",
    )
    write(
        inv / "detections" / "README.md",
        f"# Detections — {disp}\n\n"
        "**Do not deploy** placeholder rules. No YARA/Sigma content validated for this candidate stub.\n",
    )
    write(
        inv / "samples" / "README.md",
        f"# Samples — {disp}\n\n"
        "No malware binaries in-repo. Do not download samples without a Tier-1 gate "
        "(`shared/methodology/GATED_AUTONOMY.md`).\n",
    )
    write(
        inv / "docs" / "research-notes.md",
        f"""# {disp} — Research notes

**Status:** `{f['status']}`  
**Updated:** {NOW}

## Catalog basis

- Disclosure framing: {f['disclosure']}
- Fit: {f['why']}
- Comparator / isolation: {f['comparator_note']}

## Working rules

1. Do not invent IOCs.
2. Do not merge IC3 packages with active families.
3. Technique comparisons must set `authorship_link=NOT_ESTABLISHED` unless PRIMARY evidence says otherwise.
""",
    )

    cti = ROOT / "reports" / "law-enforcement" / "CTI-Evidence-Repository" / "families" / disp
    for sub in ("iocs", "network_captures", "memory_dumps", "rules", "actors_and_finance"):
        (cti / sub).mkdir(parents=True, exist_ok=True)

    write(
        cti / "SUMMARY.md",
        f"""# {disp} — Family Summary (CANDIDATE STUB)

**Case ID slug:** `{slug}`  
**Package:** `{f['pkg_id']}`  
**Status:** `{f['status']}`  
**Category:** {f['category']}  
**TLP:** TLP:AMBER+STRICT  
**Generated:** {NOW}  
**Source:** Candidate catalog only — **no invented IOCs**

## Executive overview

Defensive placeholder package for **{disp}**. This folder exists so the CTI tree mirrors investigation stubs.  
**PRIMARY indicator counts in this build: 0.** Author personal identity / home IP is **NOT ESTABLISHED**.

## Indicator counts (this build)

| Class | Count |
|-------|------:|
| Domains / URLs | 0 |
| IPs | 0 |
| Hashes | 0 |

## Evidence folders (placeholders)

| Folder | Status |
|--------|--------|
| `network_captures/` | Empty — lab PCAP only after approved Tier-1 gate |
| `memory_dumps/` | Empty |
| `rules/` | Stub YARA/Sigma placeholders — not deployable |
| `actors_and_finance/` | No crypto wallets established |

## Case isolation

{f['comparator_note']}

## Cross-references

- Investigation: `investigations/{slug}/`
- LE stub package: `reports/law-enforcement/packages/{f['pkg']}/`
- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
""",
    )

    empty_ioc = "indicator_type,value,first_seen_utc,last_seen_utc,confidence,provenance,evidence_id,notes\n"
    write(cti / "iocs" / "ips.csv", empty_ioc + f"# No IPs — UNVERIFIED candidate stub ({disp})\n")
    write(cti / "iocs" / "domains.csv", empty_ioc + f"# No domains — UNVERIFIED candidate stub ({disp})\n")
    write(cti / "iocs" / "hashes.csv", empty_ioc + f"# No hashes — UNVERIFIED candidate stub ({disp})\n")
    write(
        cti / "network_captures" / "README.md",
        f"# Network captures — {disp}\n\nEmpty. Requires human/licensed sandbox PCAP after Tier-1 approval.\n",
    )
    write(
        cti / "memory_dumps" / "README.md",
        f"# Memory dumps / configs — {disp}\n\nEmpty. No ETW decrypted stubs in-repo.\n",
    )
    write(cti / "rules" / "README.md", f"# Rules — {disp}\n\nPlaceholders only. Do not deploy.\n")
    write(
        cti / "rules" / "yara.yar",
        """rule ETW_PLACEHOLDER_DoNotDeploy
{
    meta:
        description = "Placeholder — replace with validated family signatures before operational use"
        author = "Emerging Threat Watch"
        tlp = "AMBER"
        reference = "investigations/"
    condition:
        false
}
""",
    )
    write(
        cti / "rules" / "sigma.yml",
        f"""title: ETW Placeholder Do Not Deploy — {disp}
status: experimental
description: Placeholder Sigma — not validated
logsource:
    product: windows
detection:
    selection:
        EventID: 0
    condition: selection
falsepositives:
    - Placeholder always matches nothing useful
level: informational
""",
    )
    write(
        cti / "actors_and_finance" / "wallets.txt",
        "# No cryptocurrency wallet addresses established in ETW corpus for this family.\n"
        "# Add BTC/XMR/USDT/ETH addresses only with PRIMARY-SOURCE or OBSERVED_PASSIVE provenance.\n",
    )
    write(
        cti / "actors_and_finance" / "ssl_jarm_pdb.md",
        f"# SSL / JARM / PDB — {disp}\n\nNone established. UNVERIFIED candidate stub.\n",
    )
    write(
        cti / "actors_and_finance" / "handle_correlations.json",
        json.dumps(
            {
                "family": disp,
                "status": f["status"],
                "handles": [],
                "notes": "ASSOCIATION_ONLY / empty — do not invent handles",
            },
            indent=2,
        )
        + "\n",
    )

    mid = f"malware--{uuid.uuid5(NS, 'etw-malware-' + slug)}"
    iid = f"identity--{uuid.uuid5(NS, 'etw-identity')}"
    bid = f"bundle--{uuid.uuid5(NS, 'etw-bundle-' + slug)}"
    ts = NOW.replace("Z", ".000000Z")
    stix = {
        "type": "bundle",
        "id": bid,
        "objects": [
            {
                "type": "identity",
                "spec_version": "2.1",
                "id": iid,
                "created": ts,
                "modified": ts,
                "name": "Emerging Threat Watch",
                "description": "Defensive threat-intelligence research package.",
                "identity_class": "organization",
            },
            {
                "type": "malware",
                "spec_version": "2.1",
                "id": mid,
                "created": ts,
                "modified": ts,
                "name": disp,
                "description": (
                    f"ETW {f['status']} stub for {disp}. "
                    "Author attribution NOT_ESTABLISHED. No PRIMARY indicators in bundle."
                ),
                "malware_types": ["unknown"],
                "is_family": True,
            },
        ],
    }
    write(cti / "stix_bundle.json", json.dumps(stix, indent=4) + "\n")

    pkg = ROOT / "reports" / "law-enforcement" / "packages" / f["pkg"]
    write(
        pkg / "00_COVER_SHEET.md",
        f"""# {disp} — Law Enforcement Package Cover Sheet (CANDIDATE STUB)

| Field | Value |
|-------|-------|
| **Package ID** | `{f['pkg_id']}` |
| **Family** | {disp} only (case-isolated) |
| **Status** | `{f['status']}` — **NOT READY TO FILE** |
| **Platform** | {f['platform']} |
| **Threat type** | {f['category']} |
| **Research cutoff** | 2026-09-19 |
| **Package status** | CANDIDATE STUB — human review + primary freeze required before any filing |
| **ETW independently observed infrastructure** | **None** |
| **PRIMARY IOCs in package** | **None** (intentional) |
| **Suggested IC3 crime-type language** | Malware (draft only — do not file) |
| **Primary research orgs** | {f['primary_org']} |
| **Primary publication window** | {f['disclosure']} |

## Package contents

| # | File | Purpose |
|---|------|---------|
| 00 | `00_COVER_SHEET.md` | This sheet |
| 01 | `01_NARRATIVE_PASTE.txt` | Placeholder — not for IC3 paste |
| 02 | `02_FBI_SUMMARY.md` | Stub summary |
| 03 | `03_INDICATORS.csv` | Header only — no invented IOCs |
| 04 | `04_SOURCES.md` | Candidate catalog pointers |
| 05 | `05_CAVEATS_AND_LIMITS.md` | Hard limits |
| 06 | `06_EVIDENCE_RETAINED.md` | Retention checklist |

## Filing rule

**Do not file this package** until primary sources are frozen and a human reviewer marks it ready. Do **not** combine with other Emerging Threat Watch family filings.

## Integrity gate

- [ ] Primary URL frozen
- [ ] No fabricated hashes, domains, or C2 hosts
- [ ] Narrative uses researchers-reported language
- [ ] Human reviewer name/date recorded before any submit
""",
    )
    write(
        pkg / "01_NARRATIVE_PASTE.txt",
        f"""DRAFT — DO NOT PASTE INTO IC3

Family: {disp}
Package: {f['pkg_id']}
Status: {f['status']}

Emerging Threat Watch maintains a candidate/comparator case folder for {disp} based on public vendor disclosure framing ({f['disclosure']}).
No independently observed infrastructure is claimed.
No indicators are included in this stub to avoid inventing hashes, domains, or C2 hosts.
Primary URL freeze and human review are required before any filing.
""",
    )
    write(
        pkg / "02_FBI_SUMMARY.md",
        f"""# {disp} — FBI Summary (CANDIDATE STUB)

**Package:** `{f['pkg_id']}`  
**Status:** `{f['status']}` — **not ready for referral**

## One-paragraph summary

Researchers (per ETW candidate catalog) have publicly discussed **{disp}** ({f['category']}; disclosure framing: {f['disclosure']}). Emerging Threat Watch has opened an isolated candidate folder for defensive tracking. **No PRIMARY IOCs are included in this stub.** Author attribution is **NOT_ESTABLISHED**.

## Contact block

| Field | Value |
|-------|-------|
| Project | Emerging Threat Watch |
| Contact | _[TO BE FILLED]_ |

## Do not

- File this stub as-is
- Merge with SynkLoader / Rapuncel / other active packages without linkage evidence
""",
    )
    write(
        pkg / "03_INDICATORS.csv",
        "evidence_id,family,indicator,type,first_seen,provenance,confidence,independently_verified,source_url,retrieval_date_utc,notes,status_label\n"
        f"{code}-IND-0000,{disp},NO_PRIMARY_IOCS_YET,placeholder,unspecified,UNVERIFIED,None,false,{f['primary_url']},{NOW},Intentional empty — ASSOCIATION_ONLY / UNVERIFIED candidate stub.,UNVERIFIED\n",
    )
    write(
        pkg / "04_SOURCES.md",
        f"""# {disp} — Sources

**Status:** `{f['status']}`

| ID | Role | URL / path |
|----|------|------------|
| CAT-001 | Candidate catalog | `docs/CANDIDATE_FAMILIES.md` |
| CAT-002 | Machine-readable candidates | `intelligence/candidate-families.csv` |
| CMP-001 | Technique comparators (if applicable) | `docs/TECHNIQUE_COMPARATORS.md` |

Primary vendor URL: **{f['primary_url']}**

Organization framing: {f['primary_org']}
""",
    )
    write(
        pkg / "05_CAVEATS_AND_LIMITS.md",
        f"""# {disp} — Caveats and Limits

**Package:** `{f['pkg_id']}`  
**Status:** `{f['status']}`

## Analytical caveats

- This is a **candidate/comparator stub**, not a filing-ready package.
- {f['comparator_note']}
- No hashes, domains, IPs, wallets, or handles were invented for this stub.

## This package does **not** claim

- No dollar loss figure
- No assertion that ETW discovered {disp}
- No fabricated indicators
- No independent actor attribution
- No readiness for IC3/FBI filing

## Provenance vocabulary

| Label | Meaning |
|-------|---------|
| UNVERIFIED | Lead only — not adequately substantiated |
| ASSOCIATION_ONLY | Contextual association — not ownership |
| PRIMARY-SOURCE | Published by cited vendor (none frozen yet here) |
""",
    )
    write(
        pkg / "06_EVIDENCE_RETAINED.md",
        f"""# {disp} — Evidence Retained

**Package:** `{f['pkg_id']}`

| Item | Status |
|------|--------|
| Primary HTML/PDF archive | Not yet — freeze required |
| Published IOC transcription | Empty by policy |
| Sandbox PCAP / memory | None |
| Crypto wallets | None established |

Retain local copies of primary sources once frozen; do not store malware binaries in git.
""",
    )


def main() -> None:
    for f in FAMILIES:
        scaffold_one(f)
        print(f"OK {f['slug']}")
    print(f"Done: {len(FAMILIES)} candidate/comparator case folders")


if __name__ == "__main__":
    main()
