# MiniFast — Summary

**Package:** `ETW-MNF-IC3` · **Status:** PRIMARY_FROZEN · **Primary freeze:** 2026-09-20

## Overview

Defensive threat-intelligence package concerning MiniFast as publicly documented by Check Point Research in Fast and Furious — Nimbus Manticore operations (2026). Check Point describes a previously undocumented 64-bit .NET backdoor (export CheckForUpdates / UpdateChecker.dll) delivered via AppDomain hijacking and a trojanized Zoom installer flow (Zoominstall64.zip), with persistence by hijacking ZoomUpdateTaskUser. C2 uses JSON/HTTPS with Chrome UA impersonation and Azure Web App hosts. Actor framing (Nimbus Manticore / UNC1549 / IRGC-linked) is vendor assessment — ETW does not independently establish attribution. Structural C2 notes vs PollCat are ASSOCIATION_ONLY — do NOT merge into POL case. Authorship link NOT_ESTABLISHED.

## Highest-value indicators

- `10fd541674adadfbba99b54280f7e59732746faf2b10ce68521866f737f1e46d` (sha256) — Check Point MiniFast / Nimbus Manticore campaign sample
- `eee657ffdb2af8ed6412221e7d5fbf4f5742f2ac2c88f43f12db46af0697de71` (sha256) — Check Point MiniFast / Nimbus Manticore campaign sample
- `781605ce9d4a9869e846f6c9657d71437cb6240ab27ffbc4cd550c0e06996690` (sha256) — Check Point MiniFast / Nimbus Manticore campaign sample
- `2c214494fd0bad31473ca8adce78a4f50847876584571e66aadeae70827ec2dc` (sha256) — Check Point MiniFast / Nimbus Manticore campaign sample
- `f08b17856616d66492a24dced27f788e235f35f42fa7cd10f315000d3a2f4c03` (sha256) — Check Point MiniFast / Nimbus Manticore campaign sample
- `a57ffb819fe8d98ff925c5d7b239598fe302acf5a13193d7a535040a71298fdf` (sha256) — Check Point MiniFast / Nimbus Manticore campaign sample
- `63d0d3c4a7f71bdbca720903d6a99b832089cc093c64d2938e7e001e56c17ab4` (sha256) — Check Point MiniFast / Nimbus Manticore campaign sample
- `74882085db2088356ed7f72f01e0404a0a98cda88ef56fb15ce74c1f36b26d27` (sha256) — Check Point MiniFast / Nimbus Manticore campaign sample

Full table: `03_INDICATORS.csv` (44 MNF-IND rows). Dossier: `IC3_FULL_PACKAGE.md`.

## Critical analytical caveats

- PRIMARY-SOURCE indicators only — no ETW live C2 contact.
- Additional SHA-256 / Azure domains appear in primary IOC section beyond this curated ledger — see freeze HTML.
- Nimbus Manticore / IRGC attribution is Check Point framing — NOT independently established by ETW.
- Do NOT auto-merge MiniFast into PollCat despite Azure/C2 structural notes (ASSOCIATION_ONLY).

## Suggested handling

1. Treat as defensive threat-intelligence referral material (not yet filed unless separately recorded).
2. Keep **separate** from other ETW packages.
3. Do not invent additional IOCs beyond the primary freeze.
