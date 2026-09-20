# Argamal — Family Summary

**Case ID slug:** `argamal`  
**Package:** `ETW-ARG-IC3`  
**Status:** `PRIMARY_FROZEN`  
**Category:** RAT via trojanized adult/hentai games (COM hijack)  
**TLP:** TLP:AMBER+STRICT  
**Generated:** 2026-09-20T02:25:00Z  
**Source:** PRIMARY freeze `PS-ARG-001`

## Executive overview

Defensive threat-intelligence package concerning Argamal as publicly documented by Kaspersky GReAT (Securelist 2026-06-03). Kaspersky describes a RAT distributed inside trojanized adult/hentai games (RenPy/RPG Maker etc.) via catalogue sites→PixelDrain and torrents (e.. AniRena). Infection uses modified FFmpeg DLL + natives2_blob.bin PowerShell stages, COM hijacking of Windows Color System Calibration Loader, AES-CBC payload decrypt (key zbcd1j9234r670eh), UDP heartbeats (57441) and TCP RAT mode (3747). C2 domains include asper1.freeddns.org / Winst0.kozow.com. Spanish-language comments noted by Kaspersky — author identity remains NOT_ESTABLISHED.

## Indicator counts (this build)

| Class | Count |
|-------|------:|
| Domains / URLs | 6 |
| IPs | 2 |
| Hashes | 8 |
| Total IND rows | 22 |

## Case isolation

Standalone candidate. Case-isolated from all active families.

## Cross-references

- Investigation: `investigations/argamal/`
- LE package: `reports/law-enforcement/packages/12-argamal/`
- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
