# Showboat — Summary

**Package:** `ETW-SHO-IC3` · **Status:** DRAFT — ready for human IC3 filing · **Cutoff:** 2026-09-19

## Overview

Defensive threat-intelligence package concerning Showboat as publicly documented by Lumen Black Lotus Labs (May 2026 disclosure). Lumen describes a modular Linux post-exploitation framework used against telecommunications organizations. Published artifacts support historical activity (Pastebin hide-code January 2022; BLL hosts first seen as early as 2023-04-04). Historical activity versus disclosure date remains an intelligence gap. **Author identity remains NOT_ESTABLISHED** (vendor PRC-aligned language is not independently confirmed by ETW).

## Pre-filing cross-references (separate IC3 complaints — no shared-operator claim)

| Family | Package | Submission ID |
|--------|---------|---------------|
| Rapuncel | `ETW-RAP-IC3` | `208b747c6f7445f0af2b69a9d63acc36` |
| Settra | `ETW-SET-IC3` | `631d8b4800d04bc19cdbfc6662e5c52c` |
| RatHat | `ETW-RAT-IC3` | `f92c4c2f0dd3481f898fdd125e728adf` |
| NodeRabbit | `ETW-NRB-IC3` | `dded86972e9347e0be27a6597b4cf08a` |
| PollCat | `ETW-POL-IC3` | `98a4444754324e539dbbffcb10c70637` |
| SynkLoader | `ETW-SYN-IC3` | `3440d0c64dc240499ff66deaa3311a0b` |
| **Showboat (this package)** | `ETW-SHO-IC3` | *not yet filed* |

## Why this may matter for FBI cyber / IC3 correlation

Telecom-oriented Linux post-exploitation; historical activity may predate 2026 public disclosure.

## Highest-value indicators

- Primary C2: `telecom.webredirect.org` → `139.84.227.139`; second C2 `194.135.25.132`
- Impersonation: `singtelcom.site` @ `23.27.201.160`; `kaztelecom.shop` @ `101.36.105.222`
- Linux SHA-256: `d6a4fad5448838dbc8cc6b33f1dbfbdc7a2fad36de58ff6a66dce96f729f7011`
- XOR key: `look me AV!`
- See `03_INDICATORS.csv` (SHO-IND-0001–0026) and `IC3_FULL_PACKAGE.md`

## Critical analytical caveats

- Dating gap: Pastebin Jan 2022 / BLL 2023-04 vs May 2026 disclosure — do not collapse to first-seen 2026.
- `116.169.244.208` is ASSOCIATION_ONLY — not confirmed actor-owned C2.
- Do not invent telecom victim names.

## Suggested handling

1. Treat as defensive threat-intelligence referral.
2. Keep **separate** from other ETW packages.
3. After filing: record Submission ID in `IC3_FILING_RECORD.md`, this summary, `MASTER_INDEX.csv`, and root `README.md`.
