# C2Looper Investigation

**Status:** PRIMARY frozen — promoted for package `ETW-C2L-IC3`  
**Case ID:** `c2looper`  
**Case code:** `C2L` / `ETW-C2L-IC3`  
**Kind:** `candidate`  
**Independence:** Isolated from all other ETW families. Technique/market comparisons are COMMON TECHNIQUE / ASSOCIATION_ONLY only.  
**IOC policy:** PRIMARY-SOURCE transcription only — no invented IOCs.

## Research thesis

- First/major disclosure: **Zscaler ThreatLabz Aug 2026**
- Why it fits Emerging Threat Watch: New Rust backdoor; GitHub C2 variant; likely ransomware foothold; sparse corpus
- Primary URL: https://www.zscaler.com/blogs/security-research/c2looper-new-backdoor-likely-tied-ransomware-github-c2
- Local freeze: `evidence/primary-sources/c2looper/zscaler-c2looper-2026.html` (PS-C2L-001)

## Research emphasis

Rust backdoor with /api/beacon HTTP C2 and v2 GitHub dead-drop C2; OneDrive DLL sideload update path; low-med confidence ClickFix delivery.

Ransomware-adjacent foothold hypothesis from Zscaler — ETW does not elevate to confirmed RaaS link.

## Status

Primary URL frozen; **5 C2L-IND rows** transcribed. Package status `PRIMARY_FROZEN` — **not IC3-filed**. See [`reports/law-enforcement/packages/39-c2looper/`](../../reports/law-enforcement/packages/39-c2looper/).
