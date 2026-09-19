# Emerging Threats — Program Index

**As of:** 2026-09-19 UTC  
**Rule:** Families below are co-located for research logistics only. Co-location ≠ relationship.

| Case | Family | Type | Primary disclosure (reported) | Disclosure date (reported) | Platform | Phase |
|------|--------|------|-------------------------------|----------------------------|----------|-------|
| rapuncel | Rapuncel | Infostealer | LastPass TIME / Delphos Labs — *One Kit, Forty Companies…* | 2026-09-17 | Windows | Phase 1 baseline |
| settra | Settra | Ransomware | Cynet Research Labs | 2026-09-17 (deep dive); first seen ~2026-06 | Windows enterprise | Phase 1 baseline |
| rathat | RatHat | Android banking RAT | Zimperium zLabs | 2026-09-16 | Android | Phase 1 baseline |
| noderabbit | NodeRabbit | Cross-platform RAT | Kaspersky Securelist (Mirage Kitten) | 2026-09-01 | Win/Linux/macOS (Node.js) | Phase 1 baseline |

## Cross-case status

`intelligence/campaign-relationships.csv` currently contains **no SUPPORTED** inter-family links.

Comparative synthesis only: `reports/landscape/` and `reports/_landscape/TRUST_SURFACE_PROBLEM_OUTLINE.md`.

| Dimension | Rapuncel | Settra | RatHat | NodeRabbit |
|-----------|----------|--------|--------|------------|
| Delivery trust | GitHub/brand SEO | Valid VPN/creds (operators) | Smishing/malvertising APKs | Fake recruiter + S3 ZIP |
| Notable trust surface | vsdbg sideload; WHCP driver; Cruciferra layer | MeshAgent RMM; BYOVD drivers | Accessibility; Wireless ADB | Node; Azure; VS Code; Git hooks |
| Primary depth | High (primary URL 403 to ETW) | High (Cynet+Huntress+MOXFIVE) | High (Zimperium) | Very high (Kaspersky) |
| Relatedness to others | None established | None established | ADB technique class ↔ ToxicPanda/RedHook only | PollCat same Kaspersky paper (tagged separate) |

Trust-surface rows: `intelligence/trust-surface-matrix.csv` (technique comparison — **not** shared authorship).