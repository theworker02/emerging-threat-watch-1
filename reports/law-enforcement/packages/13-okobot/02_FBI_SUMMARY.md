# Okobot — Summary

**Package:** `ETW-OKO-IC3` · **Status:** PRIMARY_FROZEN · **Primary freeze:** 2026-09-20

## Overview

Defensive threat-intelligence package concerning the OkoBot framework as publicly documented by Kaspersky GReAT (Securelist). Kaspersky describes a multi-stage campaign (≥20 payloads) initiated via TookPS PowerShell, configuring an SSH bot and dispatching modules including OkoSpyware (window video + keylogging of crypto wallets/password managers), SeedHunter (hardware-wallet seed phishing overlays), MC Keylogger, and browser extension loaders (e.g. Rilide). Victims across 25+ countries; activity ongoing as of publication. Russian-speaking crimeware signals noted by Kaspersky — author identity remains NOT_ESTABLISHED.

## Highest-value indicators

- `B07D451EE65A1580F20A784C8F0E7A46` (md5) — Dispatcher protobuf.dll
- `187A1F68AE786E53D3831166DC84E6D2` (md5) — Dispatcher protobuf.dll
- `D84E8DC509308523E0209D3CD3544619` (md5) — Dispatcher protobuf.dll
- `83E6B8FCB92A0B13E109301F8FF649CF` (md5) — Dispatcher version.dll
- `7306885BB4C98F2A9F056104CF092BC9` (md5) — Plugin PowerShell wrapper
- `B4C2E16CDB513BE4DC798F88E2527334` (md5) — Plugin CMD wrapper
- `2157D2429124AD28DB7A26F2477CB985` (md5) — Plugin environment enumerator
- `77CECF5E2A622AE07D8AE9913457AB57` (md5) — Plugin dropper

Full table: `03_INDICATORS.csv` (33 OKO-IND rows). Dossier: `IC3_FULL_PACKAGE.md`.

## Critical analytical caveats

- PRIMARY-SOURCE indicators only — no ETW live C2 contact.
- Comprehensive IoC list / decryption scripts are behind Kaspersky TI service — this ledger transcribes only publicly published MD5s, domains, IPs, and paths.
- Do not treat Rilide commodity stealer as Okobot authorship proof.
- Standalone — do not merge with other ETW filings.

## Suggested handling

1. Treat as defensive threat-intelligence referral material (not yet filed unless separately recorded).
2. Keep **separate** from other ETW packages.
3. Do not invent additional IOCs beyond the primary freeze.

## Evidence inventory (ETW retained)

- **Package ID:** `ETW-OKO-IC3` / folder `13-okobot`
- **PRIMARY-SOURCE indicators in `03_INDICATORS.csv`:** **38** rows (**md5** ×18, **domain** ×8, **path** ×4, **ipv4** ×3, **string** ×2, **sha256** ×2, **url** ×1)
- **Provenance rule:** Indicators are transcribed from public vendor research only. ETW has **not** executed malware and has **not** contacted suspected C2.
- **Local freezes:** `evidence/primary-sources/okobot/` (and dual refs where noted)
- **Caveats:** See `05_CAVEATS_AND_LIMITS.md` — author/operator identity remains NOT_ESTABLISHED by ETW unless a court/LE source states otherwise.
