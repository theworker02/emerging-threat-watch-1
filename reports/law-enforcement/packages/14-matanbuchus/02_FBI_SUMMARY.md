# Matanbuchus — Summary

**Package:** `ETW-MAT-IC3` · **Status:** PRIMARY_FROZEN · **Primary freeze:** 2026-09-20

## Overview

Defensive threat-intelligence package concerning Matanbuchus 3.0 / AstarionRAT as publicly documented by Huntress (ClickFix delivery chain) with supporting technical context from Zscaler ThreatLabz Matanbuchus 3.0 analysis. Huntress describes ClickFix → silent MSI → Zillya-style DLL sideload → Matanbuchus 3.0 (ChaCha20) → Lua/reflective loader → AstarionRAT. This package is a TECHNIQUE COMPARATOR for SynkLoader (Teams/ClickFix/ChaCha20 class) only. authorship_link SynkLoader=NOT_ESTABLISHED. Do NOT file jointly with SynkLoader. Author/operator identity remains NOT_ESTABLISHED.

## Highest-value indicators

- `http://binclloudapp.com/466943` (url) — ClickFix MSI delivery URL (Huntress)
- `https://marle.io/check/updprofile.aspx` (url) — Matanbuchus C2 — encrypted main module
- `www.ndibstersoft.com` (domain) — AstarionRAT C2 host
- `/intake/organizations/events?channel=app` (string) — AstarionRAT beacon polling path
- `de81e2155d797ff729ed3112fd271aa2728e75fc71b023d0d9bb0f62663f33b3` (sha256) — INFO encrypted shellcode
- `6ffae128e0dbf14c00e35d9ca17c9d6c81743d1fc5f8dd4272a03c66ecc1ad1f` (sha256) — SystemStatus.dll Matanbuchus 3.0 loader
- `68858d3cbc9b8abaed14e85fc9825bc4fffc54e8f36e96ddda09e853a47e3e31` (sha256) — jli.dll stage-2 loader
- `03c624d251e9143e1c8d90ba9b7fa1f2c5dc041507fd0955bdd4048a0967a829` (sha256) — SySUpd XOR-encrypted Lua script

Full table: `03_INDICATORS.csv` (15 MAT-IND rows). Dossier: `IC3_FULL_PACKAGE.md`.

## Critical analytical caveats

- PRIMARY-SOURCE indicators only — no ETW live C2 contact.
- TECHNIQUE COMPARATOR for SynkLoader only — COMMON TECHNIQUE / ASSOCIATION_ONLY. Do not claim shared operators.
- AstarionRAT IOCs are companion-chain notes under this comparator folder — not merged into SynkLoader.
- Companion freeze: evidence/primary-sources/matanbuchus/zscaler-matanbuchus-3-0.html (PS-MAT-002).

## Suggested handling

1. Treat as defensive threat-intelligence referral material (not yet filed unless separately recorded).
2. Keep **separate** from other ETW packages.
3. Do not invent additional IOCs beyond the primary freeze.
