# GenieLocker Investigation

**Status:** PRIMARY frozen — promoted for package `ETW-GNL-IC3`  
**Case ID:** `genielocker`  
**Case code:** `GNL` / `ETW-GNL-IC3`  
**Kind:** `candidate`  
**Independence:** Isolated from all other ETW families. Technique/market comparisons are COMMON TECHNIQUE / ASSOCIATION_ONLY only.  
**IOC policy:** PRIMARY-SOURCE transcription only — no invented IOCs.

## Research thesis

- First/major disclosure: **Kaspersky Securelist 2026 (Toy Ghouls / Bearlyfy)**
- Why it fits Emerging Threat Watch: Custom Win+Linux+ESXi ransomware; replaces third-party encryptors for Toy Ghouls; sparse public corpus
- Primary URL: https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/
- Local freeze: `evidence/primary-sources/genielocker/securelist-genielocker-2026.html` (PS-GNL-001)

## Research emphasis

Custom encryptor (libsodium / XChaCha20-Poly1305) for Windows PE and Linux/ESXi ELF; Toy Ghouls attributed by OSINT — ETW author identity NOT_ESTABLISHED beyond vendor citation.

Technique comparator for Settra (enterprise ransomware class) only — authorship NOT_ESTABLISHED.

## Status

Primary URL frozen; **11 GNL-IND rows** transcribed. Package status `PRIMARY_FROZEN` — **not IC3-filed**. See [`reports/law-enforcement/packages/36-genielocker/`](../../reports/law-enforcement/packages/36-genielocker/).
