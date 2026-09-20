# TencShell — Summary

**Package:** `ETW-TEN-IC3` · **Status:** PRIMARY_FROZEN · **Primary freeze:** 2026-09-20

## Overview

Defensive threat-intelligence package concerning TencShell as publicly documented by Cato CTRL (2026). Cato describes a previously undocumented Go-based implant customized from the open-source Rshell C2 framework, delivered via a dropper → masqueraded .woff (Donut shellcode) → reflective in-memory load chain against a global manufacturer (India site / third-party access context). C2 traffic imitates Tencent-like web/API paths. Persistence via Run key value OneDriveHealthTask. Suspected China-linked assessment is vendor framing only. Author identity remains NOT_ESTABLISHED. Public Rshell OSS is NOT an IOC for this family.

## Highest-value indicators

- `45.64.52.242` (ipv4) — Cato CTRL network indicator (defanged 45[.]64[.]52[.]242)
- `192.238.134.166` (ipv4) — Cato CTRL network indicator
- `45.115.38.27` (ipv4) — Cato CTRL network indicator
- `gin-tne-fahcesmukw.cn-hangzhou.fcapp.run` (domain) — Observed C2 / staging domain (Alibaba FC-style)
- `c3ecb90c9915daa23aec51f93ff8665778866f0592b2413578c8ba9708df6091` (sha256) — Cato CTRL published sample hash
- `660af53acdc505f333f6d4f4269cec740a5eb05e41a4c7926742606b18f22d33` (sha256) — Cato CTRL published sample hash
- `37facbbd0047c19f4efdea75ccb9e3ec793cb9b1d7846afa4fb8e900d6e9ed95` (sha256) — Cato CTRL published sample hash
- `01dc3e7e673b4f2682f29b19ecabf9a6ec9c3042c9b1cfb39dbdddf1dda680ab` (sha256) — Cato CTRL published sample hash

Full table: `03_INDICATORS.csv` (30 TEN-IND rows). Dossier: `IC3_FULL_PACKAGE.md`.

## Critical analytical caveats

- PRIMARY-SOURCE indicators only — no ETW live C2 contact.
- HTML freeze blocked by Incapsula; markdown content freeze retained from vendor page retrieval (PS-TEN-001).
- OSS Rshell similarity ≠ shared operators; do not treat public Rshell repos as TencShell IOCs.
- China-linked assessment is suspected/not confirmed by Cato — ETW does not independently establish attribution.
- Hunt.io follow-on (PS-TEN-002/003) expands HK cluster IPs; ARM/Gshell rows are infra-pivot related, not confirmed Windows TencShell code matches.

## Suggested handling

1. Treat as defensive threat-intelligence referral material (not yet filed unless separately recorded).
2. Keep **separate** from other ETW packages.
3. Do not invent additional IOCs beyond the primary freeze.
