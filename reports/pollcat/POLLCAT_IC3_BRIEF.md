# POLLCAT — IC3 / FBI Brief (Pointer)

**Canonical filing package:** [`../law-enforcement/packages/05-pollcat/`](../law-enforcement/packages/05-pollcat/)  
**Package ID:** `ETW-POL-IC3`  
**Status:** DRAFT — ready for human IC3 filing · do not auto-submit · **Cutoff:** 2026-09-19  
**Independently observed by ETW:** none

Use the law-enforcement package for all FBI/IC3 work. This file is a short index only.

| Need | File |
|------|------|
| Cover + integrity gate | `00_COVER_SHEET.md` (local: `private/filing-helpers/05-pollcat/`) |
| Paste into IC3 | `01_NARRATIVE_PASTE.txt` (local helper) |
| FBI / field office | `02_FBI_SUMMARY.md` |
| Indicators CSV | `03_INDICATORS.csv` |
| Sources | `04_SOURCES.md` |
| Caveats | `05_CAVEATS_AND_LIMITS.md` |
| Retention | `06_EVIDENCE_RETAINED.md` (local helper) |
| Form field map | `07_IC3_FORM_FIELDS.md` (local helper) |

**Filing guide:** [`../law-enforcement/HOW_TO_FILE.md`](../law-enforcement/HOW_TO_FILE.md) · **Checklist:** [`../law-enforcement/SUBMISSION_CHECKLIST.md`](../law-enforcement/SUBMISSION_CHECKLIST.md)

## Case isolation (mandatory)

Do **not** merge with NodeRabbit (`ETW-NRB-IC3`, Submission ID `dded86972e9347e0be27a6597b4cf08a`). Same Securelist primary artifact; separate implants.

## Paste-ready factual core (same as package narrative)

I am reporting defensive threat-intelligence information concerning the PollCat malware documented by Kaspersky GReAT on September 1, 2026 in the same Securelist article that covers NodeRabbit. Kaspersky describes PollCat as a cross-platform obfuscated JavaScript RAT delivered through the RankChallenge-react coding-challenge archive (MD5 795e053a990a1569ffdcb57f48f6d085). Kaspersky reports registration C2 hosts including sahi-finance.com and Azure Web App hostnames, OTP validation via lifespotify.com, and persistence markers such as NetSync scheduled tasks, requireObject.js under AppData, com.harsh.requireobject.plist, and ~/.node_packages. Kaspersky states PollCat's structure is substantially different from NodeRabbit. I am retaining PollCat as a separate case. Co-disclosure and shared recruiter/coding-challenge delivery are COMMON TECHNIQUE only — not proof of shared implant authorship. I have not executed malware samples and have not contacted suspected command-and-control systems.
