# Docro Hijacker Investigation

**Status:** PRIMARY frozen — promoted for package `ETW-DOC-IC3`  
**Case ID:** `docrohijacker`  
**Case code:** `DOC` / `ETW-DOC-IC3`  
**Kind:** `candidate`  
**Independence:** Isolated from all other ETW families. Technique/market comparisons are COMMON TECHNIQUE / ASSOCIATION_ONLY only.  
**IOC policy:** PRIMARY-SOURCE transcription only — no invented IOCs.

## Research thesis

- First/major disclosure: **Unit 42 Sept 2026 — first modern in-wild observation**
- Why it fits Emerging Threat Watch: Chrome Secure Preferences HMAC bypass + browser hijack; revived 2015 technique class; sparse dedicated tracking
- Primary URL: https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/
- Local freeze: `evidence/primary-sources/docrohijacker/unit42-cl-cri-1171-ppi-2026.html` (PS-DOC-001)

## Research emphasis

Chrome backdoor bypassing Secure Preferences HMAC-SHA256 via Adblock.dll; search-provider hijack for monetization.

OfferLoader delivery ASSOCIATION_ONLY; do not merge with Insomnia/ARKTunnel.

## Status

Primary URL frozen; **4 DOC-IND rows** transcribed. Package status `PRIMARY_FROZEN` — **not IC3-filed**. See [`reports/law-enforcement/packages/34-docrohijacker/`](../../reports/law-enforcement/packages/34-docrohijacker/).
