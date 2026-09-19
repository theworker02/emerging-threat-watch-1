# SETTRA — IC3 / FBI Brief (Pointer)

**Canonical filing package:** [`../law-enforcement/packages/02-settra/`](../law-enforcement/packages/02-settra/)  
**Package ID:** `ETW-SET-IC3`  
**Status:** DRAFT — do not auto-submit · **Cutoff:** 2026-09-19  
**Independently observed by ETW:** none

Use the law-enforcement package for all FBI/IC3 work. This file is a short index only.

| Need | File |
|------|------|
| Cover + integrity gate | `00_COVER_SHEET.md` |
| Paste into IC3 | `01_NARRATIVE_PASTE.txt` |
| FBI / field office | `02_FBI_SUMMARY.md` |
| Indicators CSV | `03_INDICATORS.csv` |
| Sources | `04_SOURCES.md` |
| Caveats | `05_CAVEATS_AND_LIMITS.md` |
| Retention | `06_EVIDENCE_RETAINED.md` |

**Filing guide:** [`../law-enforcement/HOW_TO_FILE.md`](../law-enforcement/HOW_TO_FILE.md) · **Checklist:** [`../law-enforcement/SUBMISSION_CHECKLIST.md`](../law-enforcement/SUBMISSION_CHECKLIST.md)

## Paste-ready factual core (same as package narrative)

I am reporting defensive threat-intelligence information concerning ransomware/extortion activity publicly tracked as Settra. Cynet, Huntress and MOXFIVE have independently published incident-response or technical findings related to this operation. Cynet reverse engineered a password-gated two-stage Windows encryptor and found that the encryptor itself did not contain file-exfiltration functionality. Huntress reported two incidents using MeshAgent and identified 45.13.122.7 and 193.5.65.114 as MeshAgent infrastructure during those incidents. Huntress also reported the workstation identifier WIN-LIVFRVQFMKO, which it had observed in other malicious activity before Settra's public emergence. I am retaining these historical relationships as investigative leads and am not attributing the older incidents to Settra without additional evidence.
