# Abyssos Investigation

**Status:** PRIMARY frozen — promoted for IC3 package `ETW-ABY-IC3`  
**Case ID:** `abyssos`  
**Case code:** `ABY` / `ETW-ABY-IC3`  
**Independence:** Isolated from all other ETW families.  
**IOC policy:** PRIMARY-SOURCE transcription from Zscaler only — no invented IOCs.

## Research thesis

- First major disclosure: **Zscaler ThreatLabz 2026-08-10** (identified late June 2026)
- Modular C++ Windows RAT: credential theft, HVNC, file exfil, downloadable modules
- Primary URL: https://www.zscaler.com/blogs/security-research/abyssos-technical-analysis-new-modular-rat
- Local freeze: `evidence/primary-sources/abyssos/zscaler-abyssos-2026-08-10.html` (PS-ABY-001)

## Research emphasis

- Custom AES-GCM TCP C2 + HELLO registration
- HVNC / browser session hijack (`%TEMP%\fontconfigs`, Chrome CDP 9222)
- Module crypto constant `1234567890abcdef`
- Published sample hashes + C2 IPv4 only

## Status

Primary URL frozen; **10 ABY-IND rows** transcribed. IC3 package ready for human filing — see [`reports/law-enforcement/packages/08-abyssos/`](../../reports/law-enforcement/packages/08-abyssos/).
