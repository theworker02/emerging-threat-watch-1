# Phase 1 Program Summary — Emerging Threat Watch

**Date (UTC):** 2026-09-19
**Repository:** `emerging-threat-watch`

## What Was Built
- Multi-family research program with mandatory case isolation
- Shared schemas, templates, and passive tooling (including `check_case_isolation.py`)
- Four independent investigation packages + landscape comparison stub
- Separate IC3 briefs per family (not combined)
- Master intelligence index / timeline / relationship register (no SUPPORTED cross-links)

## Evidence / Sources Snapshot

| Case | Evidence rows | Primary source in hand? | Notable gap |
|------|---------------|-------------------------|-------------|
| Rapuncel | 15 | Title cited; full primary doc URL pending | Hash provenance; primary PDF/HTML |
| Settra | 9 | Yes (Cynet blog) | Full hash appendix harvest |
| RatHat | 8 | Yes (Zimperium) | APK hashes / C2 list harvest |
| NodeRabbit | 9 | Yes (Kaspersky Securelist) | Finish IOC section extraction |

## Independently Corroborated (ETW OBSERVED)
Infrastructure/sample execution: none.
Program observations limited to open-source document retrieval and repository construction.

## Cross-Case Relationships
All inter-family rows in `intelligence/campaign-relationships.csv` are UNKNOWN / NONE.
Comparative landscape only.

## Safety Limitations
Passive research only; no malware execution; no C2 interaction; no combined IC3 filing.

## Recommended Phase 2 (per case, still isolated)
1. Rapuncel: retrieve primary LastPass/Delphos document; passive DNS/CT; hash source tracing; BoryptGrab matrix update.
2. Settra: extract full IOC/ATT&CK appendix; ransom-artifact detections (UNVALIDATED).
3. RatHat: harvest APK/network IOCs; mobile hunting guidance; AI-control documentation precision.
4. NodeRabbit: finish Securelist IOC ingest; passive Azure/S3 status; persistence Sigma drafts.
5. Landscape: fill comparison tables after each case Phase 2; generate PDFs when content-complete.