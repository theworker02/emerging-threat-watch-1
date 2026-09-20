# SharkLoader — Summary

**Package:** `ETW-SHK-IC3` · **Status:** PRIMARY_FROZEN · **Primary freeze:** 2026-09-20

## Overview

Defensive threat-intelligence package concerning SharkLoader as publicly documented by Kaspersky GReAT (Securelist 2026-06-24) in the StrikeShark campaign. Kaspersky describes a multi-component custom loader that DLL-sideloads via abused legitimate binaries (commonly SystemSettings.exe → SystemSettings.dll), decrypts DscCoreR.mui / SyncRes.dat modules, installs API hooks (Detours/MinHook), and executes Cobalt Strike Beacon in memory. Delivery includes exploitation of internet-facing apps and malicious droppers. Kaspersky does not attribute StrikeShark to a known APT with high confidence. Author identity remains NOT_ESTABLISHED.

## Highest-value indicators

- `C559CC68986933200FD5D9E4388E2F58` (md5) — Installer sample (Kaspersky StrikeShark)
- `B3352B42432DEDC4A519F011DC8B5D5A` (md5) — Dropper sample
- `24FCEBDEECBA65004FDB0923763D74FD` (md5) — Dropper (Taiwan gov chain) — Chinese-filename pdf.exe
- `9C872A0D5D5A38950E8B9AC9B488BE3F` (md5) — SharkLoader DLL
- `AA3086BE652C8B20B0B29B2730D57119` (md5) — SharkLoader DLL SystemSettings.dll
- `A514D1BB62D7916475946FE7C07AC0AA` (md5) — Encrypted DscCoreR.mui
- `9CBD560F820C95D7C38342CD558CB5C6` (md5) — Encrypted SyncRest.dat / SyncRes.dat
- `1F65544978B8EA0E745E573B8EE9684B` (md5) — Dropper (Lebanon)

Full table: `03_INDICATORS.csv` (19 SHK-IND rows). Dossier: `IC3_FULL_PACKAGE.md`.

## Critical analytical caveats

- PRIMARY-SOURCE indicators only — no ETW live C2 contact.
- Cobalt Strike Beacon hashes are NOT transcribed here unless published as SharkLoader-specific; do not invent CS beacons.
- Kaspersky 'Chinese-speaking' assessment is low-confidence vendor framing — ETW does not independently establish attribution.
- Standalone — do not merge with other ETW loader packages (COMMON TECHNIQUE only).

## Suggested handling

1. Treat as defensive threat-intelligence referral material (not yet filed unless separately recorded).
2. Keep **separate** from other ETW packages.
3. Do not invent additional IOCs beyond the primary freeze.
