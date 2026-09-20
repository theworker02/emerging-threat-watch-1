# StarlandRAT — Summary

**Package:** `ETW-STR-IC3` · **Status:** PRIMARY_FROZEN · **Primary freeze:** 2026-09-20

## Overview

Defensive threat-intelligence package concerning Starland RAT and the companion WLDR PowerShell C2 agent as publicly documented by Cisco Talos (UAT-11795 financially motivated campaign). Talos describes ClickFix / trojanized installer delivery (Webex/Zoom/MobaXterm/DBeaver-class lures), a memory-resident Python RAT with crypto-wallet recon, Telegram notification bots, and Polygon smart-contract fallback C2, plus optional CastleStealer/Remcos follow-ons and WLDR in-memory PowerShell post-ex. UAT-11795 / Russian-speaking framing is vendor assessment — ETW does not independently establish attribution. Author identity remains NOT_ESTABLISHED. WLDR tracked as companion under this case until distinct corpus warrants split.

## Highest-value indicators

- `eorthopaedics.com` (domain) — Staging / HWID C2 (Talos; possibly hijacked)
- `sastoro.com` (domain) — Parallel staging / HWID C2 under /alpha/
- `web-devtools.com` (domain) — Shellcode staging (/starlandfox /x32remka /dopfile)
- `zynaris.io` (domain) — HTA stager / trojanized installer lures
- `windowscreenrepairnearme.com` (domain) — Primary Starland RAT C2 (possibly hijacked)
- `aipythondevs.com` (domain) — Primary Starland RAT C2
- `0x6ae382ed2154cc84c6672e4e908cd2c69c1b35ba` (crypto_constant) — Polygon smart-contract address for XOR-encrypted fallback C2
- `polygon-rpc.com` (domain) — Public Polygon JSON-RPC used for fallback domain retrieval

Full table: `03_INDICATORS.csv` (17 STR-IND rows). Dossier: `IC3_FULL_PACKAGE.md`.

## Critical analytical caveats

- PRIMARY-SOURCE indicators only — no ETW live C2 contact.
- Talos public article emphasizes infrastructure/host artifacts; sample SHA hashes were not published in the primary HTML freeze — do not invent hashes.
- UAT-11795 Russian-speaking financially motivated framing is Talos assessment only.
- Standalone — do not attribute to active ETW families without primary linkage evidence.

## Suggested handling

1. Treat as defensive threat-intelligence referral material (not yet filed unless separately recorded).
2. Keep **separate** from other ETW packages.
3. Do not invent additional IOCs beyond the primary freeze.
