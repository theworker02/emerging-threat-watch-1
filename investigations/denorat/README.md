# DenoRAT / DinDoor / NightshadeC2 Investigation

**Status:** PRIMARY frozen — promoted for package `ETW-DEN-IC3`  
**Case ID:** `denorat`  
**Case code:** `DEN` / `ETW-DEN-IC3`  
**Kind:** `candidate`  
**Independence:** Isolated from all other ETW families. Technique/market comparisons are COMMON TECHNIQUE / ASSOCIATION_ONLY only.  
**IOC policy:** PRIMARY-SOURCE transcription only — no invented IOCs.

## Research thesis

- First/major disclosure: **eSentire TRU June 2026 (TAG-150)**
- Why it fits Emerging Threat Watch: Deno-runtime loader+RAT chain → NightshadeC2; ClickFix; sparse Deno-based crimeware class
- Primary URL: https://www.esentire.com/blog/dindoor-denorat-and-nightshadec2-analyzing-tag-150s-evolving-tradecraft
- Local freeze: `evidence/primary-sources/denorat/esentire-dindoor-denorat-nightshade-2026.html` (PS-DEN-001)

## Research emphasis

TAG-150 ClickFix → MSI → Deno runtime → DinDoor loader → DenoRAT → in-memory NightshadeC2. Tracked as one ETW case for the disclosed chain; NightshadeC2 may have broader use — do not expand IOCs beyond PRIMARY.

ClickFix technique comparator for SynkLoader delivery class only — authorship NOT_ESTABLISHED.

## Status

Primary URL frozen; **18 DEN-IND rows** transcribed. Package status `PRIMARY_FROZEN` — **not IC3-filed**. See [`reports/law-enforcement/packages/37-denorat/`](../../reports/law-enforcement/packages/37-denorat/).
