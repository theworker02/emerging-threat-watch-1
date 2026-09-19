# RatHat — Law Enforcement Package Cover Sheet

| Field | Value |
|-------|-------|
| **Package ID** | `ETW-RAT-IC3` |
| **Family** | RatHat only (case-isolated) |
| **Platform** | Android |
| **Threat type** | Android banking RAT / credential theft (Accessibility + Wireless ADB abuse) |
| **Research cutoff** | 2026-09-19 |
| **Corpus retrieval** | 2026-09-19T18:07:48Z |
| **Package status** | DRAFT — human review required before any filing |
| **ETW independently observed infrastructure** | None as live C2 contact. Passive CT/urlscan rows exist for selected Zimperium-published apexes (facts only; not ownership). |
| **Suggested IC3 crime-type language** | Malware (mobile); Online banking fraud facilitation; Unauthorized access to devices |
| **FBI relevance (defensive TI)** | Mobile malware obtaining Android shell via Wireless Debugging self-pair; persistence outside APK lifecycle; credential and banking targeting |
| **Primary research orgs** | Zimperium zLabs |
| **Primary publication window** | 2026-09-16 (Zimperium) |

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
