# PollCat — Law Enforcement Package Cover Sheet

| Field | Value |
|-------|-------|
| **Package ID** | `ETW-POL-IC3` |
| **Family** | PollCat only (case-isolated) |
| **Platform** | Windows / Linux / macOS |
| **Threat type** | Cross-platform obfuscated JavaScript RAT (coding-challenge delivery) |
| **Research cutoff** | 2026-09-19 |
| **Corpus retrieval** | 2026-09-19T18:07:48Z |
| **Package status** | DRAFT — human review required before any filing |
| **ETW independently observed infrastructure** | **None** |
| **Suggested IC3 crime-type language** | Malware; Spear-phishing / social engineering (recruitment lure) |
| **FBI relevance (defensive TI)** | Co-disclosed with NodeRabbit in Kaspersky Securelist; packages remain separate. RankChallenge-react lure; distinct C2/persistence from NodeRabbit; stronger documented protocol overlap with MiniFast/Retrograde than with NodeRabbit. |
| **Primary research orgs** | Kaspersky GReAT / Securelist |
| **Primary publication window** | 2026-09-01 (Securelist) |

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
