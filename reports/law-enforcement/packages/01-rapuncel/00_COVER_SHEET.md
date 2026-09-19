# Rapuncel — Law Enforcement Package Cover Sheet

| Field | Value |
|-------|-------|
| **Package ID** | `ETW-RAP-IC3` |
| **Family** | Rapuncel only (case-isolated) |
| **Platform** | Windows |
| **Threat type** | Information stealer / MaaS distribution (credential theft) |
| **Research cutoff** | 2026-09-19 |
| **Corpus retrieval** | 2026-09-19T18:07:48Z |
| **Package status** | DRAFT — human review required before any filing |
| **ETW independently observed infrastructure** | OBSERVED_PASSIVE only (not campaign ownership): additional GitHub Pages lure massimolongqdoj.github.io→albinofennel.com; passathook-cs2 path on albinofennel; CT chronology; DoH NXDOMAIN for albinofennel.com as of 2026-09-19. Cruciferra DCRCVDrv/vsdbg sideload catalog and LOLDrivers CcProtect are lineage comparators — not Rapuncel-author identity. |
| **Suggested IC3 crime-type language** | Malware; Phishing / social engineering (SEO/GitHub lure); Identity theft facilitation |
| **FBI relevance (defensive TI)** | Interstate cyber intrusion facilitation; credential theft targeting financial/password vault ecosystem; fraudulent brand impersonation on GitHub |
| **Primary research orgs** | LastPass TIME + Delphos (primary); eSentire / Proofpoint (Cruciferra crypter context); Trend Micro (BoryptGrab comparator only) |
| **Primary publication window** | 2026-09-17 (LastPass/Delphos primary) |

## Package contents (file in this order)

| # | File | Purpose |
|---|------|---------|
| 00 | `00_COVER_SHEET.md` | This sheet |
| 01 | `01_NARRATIVE_PASTE.txt` | Plain-text paste into IC3 complaint description |
| 02 | `02_FBI_SUMMARY.md` | Short FBI / field-office oriented summary |
| 03 | `03_INDICATORS.csv` | Source-attributed indicators (PRIMARY-SOURCE; not OBSERVED) |
| 04 | `04_SOURCES.md` | Exact public URLs and roles |
| 05 | `05_CAVEATS_AND_LIMITS.md` | What this package does **not** claim |
| 06 | `06_EVIDENCE_RETAINED.md` | What the reporter should retain locally |

## Filing rule

Submit **this package alone**. Do **not** combine with other Emerging Threat Watch family filings unless a human reviewer documents linkage evidence and decides a joint filing is appropriate.

## Integrity gate (must all pass)

- [ ] Narrative uses "researchers reported" / "I retained" language — not "I discovered" unless true
- [ ] No unsupported victimization or dollar-loss claims
- [ ] No fabricated hashes, domains, or C2 hosts
- [ ] Attribution provenance preserved (vendor assessment vs ETW conclusion)
- [ ] Current vs historical infrastructure distinguished
- [ ] Human reviewer name/date recorded before submit
