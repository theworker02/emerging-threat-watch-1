# SmartRAT Investigation

**Status:** PRIMARY frozen — promoted for package `ETW-SMT-IC3`  
**Case ID:** `smartrat`  
**Case code:** `SMT` / `ETW-SMT-IC3`  
**Kind:** `candidate`  
**Independence:** Isolated from all other ETW families. Technique/market comparisons are COMMON TECHNIQUE / ASSOCIATION_ONLY only.  
**IOC policy:** PRIMARY-SOURCE transcription only — no invented IOCs.

## Research thesis

- First/major disclosure: **Zscaler ThreatLabz March 2026**
- Why it fits Emerging Threat Watch: AI-generated Brazilian bank ClickFix → PowerShell RAT with banking overlays/QR-swap; young corpus
- Primary URL: https://www.zscaler.com/blogs/security-research/clickfix-campaign-generated-ai-delivers-smartrat
- Local freeze: `evidence/primary-sources/smartrat/zscaler-smartrat-2026.html` (PS-SMT-001)

## Research emphasis

PowerShell RAT via AI-built ClickFix bank lure; TCP/51888 C2; banking overlays + QR-swap; weak C2 panel auth noted by vendor.

Banking overlay class distinct from RatHat (Android) — no merge. ClickFix comparator for SynkLoader only.

## Status

Primary URL frozen; **10 SMT-IND rows** transcribed. Package status `PRIMARY_FROZEN` — **not IC3-filed**. See [`reports/law-enforcement/packages/40-smartrat/`](../../reports/law-enforcement/packages/40-smartrat/).
