# kkRAT Investigation

**Status:** PRIMARY frozen — promoted for package `ETW-KKR-IC3`  
**Case ID:** `kkrat`  
**Case code:** `KKR` / `ETW-KKR-IC3`  
**Kind:** `candidate`  
**Independence:** Isolated from all other ETW families. Technique/market comparisons are COMMON TECHNIQUE / ASSOCIATION_ONLY only.  
**IOC policy:** PRIMARY-SOURCE transcription only — no invented IOCs.

## Research thesis

- First/major disclosure: **Zscaler ThreatLabz 2025/2026**
- Why it fits Emerging Threat Watch: Previously unknown RAT blending Ghost RAT + Big Bad Wolf; Chinese-speaking targets; crypto clipboard + RMM install
- Primary URL: https://www.zscaler.com/blogs/security-research/technical-analysis-kkrat
- Local freeze: `evidence/primary-sources/kkrat/zscaler-kkrat.html` (PS-KKR-001)

## Research emphasis

New RAT with Ghost RAT protocol lineage + Big Bad Wolf plugin exports; campaign also drops ValleyRAT/FatalRAT — keep those IOCs ASSOCIATION_ONLY to campaign, not kkRAT identity.

ValleyRAT/FatalRAT C2s in same campaign article are ASSOCIATION_ONLY — do not promote as kkRAT-owned.

## Status

Primary URL frozen; **13 KKR-IND rows** transcribed. Package status `PRIMARY_FROZEN` — **not IC3-filed**. See [`reports/law-enforcement/packages/42-kkrat/`](../../reports/law-enforcement/packages/42-kkrat/).
