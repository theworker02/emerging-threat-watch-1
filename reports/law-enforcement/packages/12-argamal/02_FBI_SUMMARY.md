# Argamal — Summary

**Package:** `ETW-ARG-IC3` · **Status:** PRIMARY_FROZEN · **Primary freeze:** 2026-09-20

## Overview

Defensive threat-intelligence package concerning Argamal as publicly documented by Kaspersky GReAT (Securelist 2026-06-03). Kaspersky describes a RAT distributed inside trojanized adult/hentai games (RenPy/RPG Maker etc.) via catalogue sites→PixelDrain and torrents (e.g. AniRena). Infection uses modified FFmpeg DLL + natives2_blob.bin PowerShell stages, COM hijacking of Windows Color System Calibration Loader, AES-CBC payload decrypt (key zbcd1j9234r670eh), UDP heartbeats (57441) and TCP RAT mode (3747). C2 domains include asper1.freeddns.org / Winst0.kozow.com. Spanish-language comments noted by Kaspersky — author identity remains NOT_ESTABLISHED.

## Highest-value indicators

- `42add9475e67a1ccc6a6af94b5475d3defc01b85` (sha1) — Modified FFmpeg DLL (SHA1)
- `edce72f59e4c1d136cd1946af70d334c19df858d` (sha1) — natives2_blob.bin / Trojan downloader (SHA1)
- `76253fb55aed707440e808ea78e7101318436b1c` (sha1) — RAT payload (SHA1)
- `1405a3c5e0aeb08012484134e16cdec4ab29b4a4` (sha1) — RAT payload (SHA1)
- `535f4337f261b6da20a3c614eb13270bed2d533a` (sha1) — RAT payload (SHA1)
- `d2cb0d7a9ad2b5d4ea7c2da8aec62beb37cf36d6` (sha1) — RAT payload (SHA1)
- `9803604ec45f31f9ef75bcca1e1310d8ac1fc3a6` (sha1) — Trojan downloader (SHA1)
- `02819d200d1424882af81cb504b3e8614b32397a` (sha1) — Trojan downloader (SHA1)

Full table: `03_INDICATORS.csv` (22 ARG-IND rows). Dossier: `IC3_FULL_PACKAGE.md`.

## Critical analytical caveats

- PRIMARY-SOURCE indicators only — no ETW live C2 contact.
- Additional RAT SHA1s appear in primary IoC appendix — ledger includes representative payloads + all published network IOCs.
- Do not invent lure URLs beyond published GitHub staging paths.
- Standalone — case-isolated from all active ETW families.

## Suggested handling

1. Treat as defensive threat-intelligence referral material (not yet filed unless separately recorded).
2. Keep **separate** from other ETW packages.
3. Do not invent additional IOCs beyond the primary freeze.
