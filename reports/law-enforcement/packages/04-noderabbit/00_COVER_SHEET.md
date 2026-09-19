# NodeRabbit — Law Enforcement Package Cover Sheet

| Field | Value |
|-------|-------|
| **Package ID** | `ETW-NRB-IC3` |
| **Family** | NodeRabbit only (case-isolated) |
| **Platform** | Windows / Linux / macOS / WSL |
| **Threat type** | Cross-platform RAT (developer workstation targeting via fake coding assessments) |
| **Research cutoff** | 2026-09-19 |
| **Corpus retrieval** | 2026-09-19T18:07:48Z |
| **Package status** | DRAFT — human review required before any filing |
| **ETW independently observed infrastructure** | **None** |
| **Suggested IC3 crime-type language** | Malware; Spear-phishing / social engineering (recruitment lure); Espionage-oriented unauthorized access |
| **FBI relevance (defensive TI)** | Cross-platform spyware targeting MEA developer environments; Azure/Cloudflare-backed C2; mutable C2 lists; fake VS Code extension and Git-hook persistence |
| **Primary research orgs** | Kaspersky GReAT / Securelist (primary); Kaspersky press (campaign summary) |
| **Primary publication window** | 2026-09-01 (Securelist); 2026-09 (press); PolySwarm companion |

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
