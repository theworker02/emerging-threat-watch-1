# Showboat — Summary

**Package:** `ETW-SHO-IC3` · **Status:** FILED_IC3 · **Cutoff:** 2026-09-19

## Overview

Defensive threat-intelligence package concerning Showboat as publicly documented by Lumen Black Lotus Labs (May 2026 disclosure). Lumen describes a modular Linux post-exploitation framework used against telecommunications organizations. Published artifacts support historical activity (Pastebin hide-code January 2022; BLL hosts first seen as early as 2023-04-04). Historical activity versus disclosure date remains an intelligence gap. **Author identity remains NOT_ESTABLISHED** (vendor PRC-aligned language is not independently confirmed by ETW).

## IC3 filing

| Field | Value |
|-------|-------|
| Submission ID | `db42033f319844c08ad103befebfca08` |
| Date filed | 2026-09-19 10:13:28 PM EST |
| Date filed (UTC) | 2026-09-20T02:13:28Z |
| Record | [`IC3_FILING_RECORD.md`](IC3_FILING_RECORD.md) |
| Separate related filings | Rapuncel `208b747c6f7445f0af2b69a9d63acc36`; Settra `631d8b4800d04bc19cdbfc6662e5c52c`; RatHat `f92c4c2f0dd3481f898fdd125e728adf`; NodeRabbit `dded86972e9347e0be27a6597b4cf08a`; PollCat `98a4444754324e539dbbffcb10c70637`; SynkLoader `3440d0c64dc240499ff66deaa3311a0b` (no shared-operator claim) |

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

## Evidence inventory (ETW retained)

- **Package ID:** `ETW-SHO-IC3` / folder `07-showboat`
- **PRIMARY-SOURCE indicators in `03_INDICATORS.csv`:** **28** rows (**ip** ×14, **sha256** ×5, **domain** ×3, **filename** ×2, **x509_sha256** ×1, **xor_key** ×1, **string** ×1, **file_path** ×1)
- **Provenance rule:** Indicators are transcribed from public vendor research only. ETW has **not** executed malware and has **not** contacted suspected C2.
- **Local freezes:** `evidence/primary-sources/showboat/` (and dual refs where noted)
- **Caveats:** See `05_CAVEATS_AND_LIMITS.md` — author/operator identity remains NOT_ESTABLISHED by ETW unless a court/LE source states otherwise.
