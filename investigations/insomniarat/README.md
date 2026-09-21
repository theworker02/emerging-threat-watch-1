# Insomnia RAT Investigation

**Status:** PRIMARY frozen — promoted for package `ETW-INS-IC3`  
**Case ID:** `insomniarat`  
**Case code:** `INS` / `ETW-INS-IC3`  
**Kind:** `candidate`  
**Independence:** Isolated from all other ETW families. Technique/market comparisons are COMMON TECHNIQUE / ASSOCIATION_ONLY only.  
**IOC policy:** PRIMARY-SOURCE transcription only — no invented IOCs.

## Research thesis

- First/major disclosure: **Unit 42 Sept 2026 (CL-CRI-1171 / OfferLoader delivery)**
- Why it fits Emerging Threat Watch: Cross-platform Node.js+Python dual-agent RAT; sparse corpus; Node.js trust surface overlaps PollCat/NodeRabbit technique class only
- Primary URL: https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/
- Local freeze: `evidence/primary-sources/insomniarat/unit42-cl-cri-1171-ppi-2026.html` (PS-INS-001)

## Research emphasis

Dual Node.js + Python backdoor (UA insomnia/2023.4.0); installs Node/Python runtimes; CrowdStrike typosquat C2; delivered via OfferLoader PPI — do NOT merge authorship with OfferLoader/ARKTunnel/Docro.

COMMON TECHNIQUE with PollCat/NodeRabbit (Node.js RAT class) only — authorship NOT_ESTABLISHED. OfferLoader delivery ASSOCIATION_ONLY.

## Status

Primary URL frozen; **12 INS-IND rows** transcribed. Package status `PRIMARY_FROZEN` — **not IC3-filed**. See [`reports/law-enforcement/packages/32-insomniarat/`](../../reports/law-enforcement/packages/32-insomniarat/).
