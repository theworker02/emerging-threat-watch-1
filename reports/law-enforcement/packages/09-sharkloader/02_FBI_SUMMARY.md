# SharkLoader — Summary

**Package:** `ETW-SHK-IC3` · **Status:** FILED_IC3 · **Primary freeze:** 2026-09-20

## Overview

Defensive threat-intelligence package concerning SharkLoader as publicly documented by Kaspersky GReAT (Securelist 2026-06-24) in the StrikeShark campaign. Kaspersky describes a multi-component custom loader that DLL-sideloads via abused legitimate binaries (commonly SystemSettings.exe → SystemSettings.dll), decrypts DscCoreR.mui / SyncRes.dat modules, installs API hooks (Detours/MinHook), and executes Cobalt Strike Beacon in memory. Delivery includes exploitation of internet-facing apps and malicious droppers. Kaspersky does not attribute StrikeShark to a known APT with high confidence. Author identity remains NOT_ESTABLISHED.

## IC3 filing

| Field | Value |
|-------|-------|
| Submission ID | `6ed57963d0c64750aa14b6fcbaa2e576` |
| Date filed | 2026-09-19 10:43:18 PM EST |
| Date filed (UTC) | 2026-09-20T02:43:18Z |
| Record | [`IC3_FILING_RECORD.md`](IC3_FILING_RECORD.md) |
| Separate related filings | Rapuncel `208b747c6f7445f0af2b69a9d63acc36`; Settra `631d8b4800d04bc19cdbfc6662e5c52c`; RatHat `f92c4c2f0dd3481f898fdd125e728adf`; NodeRabbit `dded86972e9347e0be27a6597b4cf08a`; PollCat `98a4444754324e539dbbffcb10c70637`; SynkLoader `3440d0c64dc240499ff66deaa3311a0b`; Showboat `db42033f319844c08ad103befebfca08`; Abyssos `a23f0a9d6799480e994284416d354713` (no shared-operator claim) |

## Highest-value indicators

- `C559CC68986933200FD5D9E4388E2F58` (md5) — Installer sample (Kaspersky StrikeShark)
- `B3352B42432DEDC4A519F011DC8B5D5A` (md5) — Dropper sample
- `24FCEBDEECBA65004FDB0923763D74FD` (md5) — Dropper (Taiwan gov chain)
- `AA3086BE652C8B20B0B29B2730D57119` (md5) — SystemSettings.dll
- Domains: `connect-microsoft.com`; `ms-record.com`; `ms-record.top`; `ms-tray.top`
- Host: `SystemSettings.dll`; `DscCoreR.mui`; `SyncRes.dat`; `%APPDATA%\xwreg`; `%APPDATA%\xgdf`

Full table: `03_INDICATORS.csv` (19 SHK-IND rows). Dossier: `IC3_FULL_PACKAGE.md`.

## Critical analytical caveats

- PRIMARY-SOURCE indicators only — no ETW live C2 contact.
- Cobalt Strike Beacon hashes are NOT transcribed here unless published as SharkLoader-specific; do not invent CS beacons.
- Kaspersky 'Chinese-speaking' assessment is low-confidence vendor framing — ETW does not independently establish attribution.
- Standalone — do not merge with other ETW loader packages (COMMON TECHNIQUE only).

## Suggested handling

1. Treat as defensive threat-intelligence referral.
2. Keep **separate** from other ETW packages.

## Evidence inventory (ETW retained)

- **Package ID:** `ETW-SHK-IC3` / folder `09-sharkloader`
- **PRIMARY-SOURCE indicators in `03_INDICATORS.csv`:** **21** rows (**md5** ×10, **domain** ×4, **filename** ×3, **path** ×2, **string** ×2)
- **Provenance rule:** Indicators are transcribed from public vendor research only. ETW has **not** executed malware and has **not** contacted suspected C2.
- **Local freezes:** `evidence/primary-sources/sharkloader/` (and dual refs where noted)
- **Caveats:** See `05_CAVEATS_AND_LIMITS.md` — author/operator identity remains NOT_ESTABLISHED by ETW unless a court/LE source states otherwise.
