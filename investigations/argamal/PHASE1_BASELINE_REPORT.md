# Argamal — Phase 1 Baseline

**Generated:** 2026-09-20T02:25:00Z  
**Status:** `PRIMARY_FROZEN`

## Summary

Defensive threat-intelligence package concerning Argamal as publicly documented by Kaspersky GReAT (Securelist 2026-06-03). Kaspersky describes a RAT distributed inside trojanized adult/hentai games (RenPy/RPG Maker etc.) via catalogue sites→PixelDrain and torrents (e.. AniRena). Infection uses modified FFmpeg DLL + natives2_blob.bin PowerShell stages, COM hijacking of Windows Color System Calibration Loader, AES-CBC payload decrypt (key zbcd1j9234r670eh), UDP heartbeats (57441) and TCP RAT mode (3747). C2 domains include asper1.freeddns.org / Winst0.kozow.com. Spanish-language comments noted by Kaspersky — author identity remains NOT_ESTABLISHED.

| Field | Value |
|-------|-------|
| Family | Argamal |
| Case code | ARG |
| Disclosure | Kaspersky GReAT / Securelist 2026-06-03 |
| PRIMARY IOCs in this build | **22** |
| Independently observed infra | **None** |
| Author attribution | **NOT_ESTABLISHED** |
| Primary freeze | `evidence/primary-sources/argamal/securelist-argamal-2026.html` |
| SHA-256 | `d3aa8cee046058d5c449ac23b759e8a6c2e26c2c0105d55d1f95a9d6e976e7ef` |

## Cross-references

- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
- LE package: `reports/law-enforcement/packages/12-argamal/`
- CTI tree: `reports/law-enforcement/CTI-Evidence-Repository/families/Argamal/`
