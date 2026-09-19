# NODERABBIT — IC3 / FBI Brief (Pointer)

**Canonical filing package:** [`../law-enforcement/packages/04-noderabbit/`](../law-enforcement/packages/04-noderabbit/)  
**Package ID:** `ETW-NRB-IC3`  
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

I am reporting defensive threat-intelligence information concerning the cross-platform NodeRabbit malware documented by Kaspersky GReAT on September 1, 2026. Kaspersky reports that attackers posing as recruiters delivered malicious coding assessments containing bundled Node.js components. The malware supports Windows, Linux and macOS, with later variants adding enterprise-proxy support, WSL persistence, mutable command-and-control configuration, a fake local VS Code extension displayed as GitHub Copilot Helper, and persistence through local Git post-merge and post-checkout hooks. Kaspersky attributes the campaign to Mirage Kitten; I am identifying that attribution as Kaspersky's assessment rather than as an independently established conclusion.
