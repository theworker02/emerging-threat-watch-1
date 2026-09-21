# RATHAT — IC3 / FBI Brief (Pointer)

**Canonical filing package:** [`../law-enforcement/packages/03-rathat/`](../law-enforcement/packages/03-rathat/)  
**Package ID:** `ETW-RAT-IC3`  
**Status:** Human review required — do not auto-submit · **Cutoff:** 2026-09-19  
**Independently observed by ETW:** none

Use the law-enforcement package for all FBI/IC3 work. This file is a short index only.

| Need | File |
|------|------|
| Cover + integrity gate | `00_COVER_SHEET.md` |
| See structured dossier | `01_NARRATIVE_PASTE.txt` |
| FBI / field office | `02_FBI_SUMMARY.md` |
| Indicators CSV | `03_INDICATORS.csv` |
| Sources | `04_SOURCES.md` |
| Caveats | `05_CAVEATS_AND_LIMITS.md` |
| Retention | `06_EVIDENCE_RETAINED.md` |

**Filing guide:** [`../law-enforcement/HOW_TO_FILE.md`](../law-enforcement/HOW_TO_FILE.md) · **Checklist:** [`../law-enforcement/SUBMISSION_CHECKLIST.md`](../law-enforcement/SUBMISSION_CHECKLIST.md)

## Paste-ready factual core (same as package narrative)

I am reporting defensive threat-intelligence information concerning Android malware publicly named RatHat by Zimperium zLabs on September 16, 2026. Zimperium reports that the malware abuses Android Accessibility to enable Wireless Debugging, retrieve the device's local ADB pairing information, self-pair with the local ADB daemon and obtain shell-level execution. It then stages native Go components outside the ordinary APK lifecycle, including a local service and an FRP-derived reverse-tunnel component. Zimperium reports that the surviving service can reinstall the APK after removal and restore Accessibility configuration. I have not actively connected to suspected RatHat command-and-control infrastructure.
