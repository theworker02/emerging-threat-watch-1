# MLTBackdoor Investigation

**Status:** PRIMARY frozen — promoted for package `ETW-MLT-IC3`  
**Case ID:** `mltbackdoor`  
**Case code:** `MLT` / `ETW-MLT-IC3`  
**Kind:** `candidate`  
**Independence:** Isolated from all other ETW families. Technique/market comparisons are COMMON TECHNIQUE / ASSOCIATION_ONLY only.  
**IOC policy:** PRIMARY-SOURCE transcription only — no invented IOCs.

## Research thesis

- First/major disclosure: **Zscaler ThreatLabz May 2026**
- Why it fits Emerging Threat Watch: New ClickFix→BOF-capable backdoor likely ransomware-adjacent; DGA + ECDH C2; young corpus
- Primary URL: https://www.zscaler.com/blogs/security-research/technical-analysis-mltbackdoor
- Local freeze: `evidence/primary-sources/mltbackdoor/zscaler-mltbackdoor-2026.html` (PS-MLT-001)

## Research emphasis

Multi-stage ClickFix loader → MLTBackdoor with BOF loading, ECDH/AES-GCM C2, DGA fallback. Likely ransomware foothold tool — operator NOT_ESTABLISHED.

ClickFix comparator for SynkLoader; BOF loader class distinct from SharkLoader — no merge.

## Status

Primary URL frozen; **12 MLT-IND rows** transcribed. Package status `PRIMARY_FROZEN` — **not IC3-filed**. See [`reports/law-enforcement/packages/38-mltbackdoor/`](../../reports/law-enforcement/packages/38-mltbackdoor/).
