# Emerging Threat Watch — Submission Report (TEMPLATE)

**This file is tracked.** The filled dossier is **not**.

| Artifact | Path | Git |
|----------|------|-----|
| Filled master dossier | `reports/law-enforcement/SUBMISSION_REPORT.md` | **gitignored** |
| Alternate local name | `reports/law-enforcement/SUBMISSION_REPORT.local.md` | **gitignored** |
| Private working copies | `reports/law-enforcement/private/**` | **gitignored** |
| This template | `reports/law-enforcement/SUBMISSION_REPORT.TEMPLATE.md` | tracked |

## How to generate / refresh the private report

1. Confirm research cutoff and package status in `MASTER_INDEX.csv` and each `packages/0N-*/00_COVER_SHEET.md`.
2. For each in-scope family under `investigations/`, pull:
   - LE package: `reports/law-enforcement/packages/0N-<family>/`
   - Indicators: `investigations/<family>/evidence/published-indicators.csv` (do not invent IOCs)
   - Gaps: `investigations/<family>/gaps/priority-gaps.csv` (P0 rows)
   - Claims / evidence: `investigations/<family>/claims/`, `investigations/<family>/evidence/`
3. Cite manifests if present:
   - `evidence/manifests/primary-source-manifest.csv` (freeze / CONTENT-VERIFIED status)
   - `evidence/manifests/passive-observation-manifest.csv` (OBSERVED_PASSIVE CT/RDAP row counts — not attribution)
4. For families without a package or investigation scaffold (e.g. PollCat expansion incomplete), write **scaffold pending** — do not invent claims or indicators.
5. Copy this template structure into `SUBMISSION_REPORT.md` (or ask an agent to rebuild from repo state).
6. Complete the human filing checklist and contact placeholders **before** any IC3/FBI submission.
7. Follow [`HOW_TO_FILE.md`](HOW_TO_FILE.md) and [`SUBMISSION_CHECKLIST.md`](SUBMISSION_CHECKLIST.md). **Never auto-file.**  
8. For hosting/registrar/chat **takedown** packages (separate from this IC3 narrative dossier), use [`TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md) and [`shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`](../../shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md).

## Required section outline (filled report)

1. Cover / classification  
2. Program overview (purpose, case isolation, provenance vocabulary)  
3. Autonomous collection policy summary  
4. Per-family sections (one section each; one filing each)  
5. Cross-family note (no shared-operator claim)  
6. OBSERVED_PASSIVE status  
7. Primary-source freeze status  
8. Human filing checklist  
9. How-to-file pointer  
10. Safety statement  
11. FBI/IC3 reporting intent  
12. Appendix — paths index  

## Hard rules

- Do not commit filled `SUBMISSION_REPORT.md` or anything under `private/`.
- Do not invent hashes, domains, C2 hosts, victim names, or dollar losses.
- One family = one filing unless a human documents linkage evidence.
