# NodeRabbit — Summary

**Package:** `ETW-NRB-IC3` · **Status:** FILED_IC3 · **Cutoff:** 2026-09-19

## Overview

Defensive threat-intelligence package concerning cross-platform NodeRabbit malware documented by Kaspersky GReAT (2026-09-01). Kaspersky reports recruiter-posed coding assessments delivering bundled Node.js components supporting Windows, Linux, and macOS, with later variants adding enterprise-proxy support, WSL persistence, mutable C2 configuration, a fake local VS Code extension (“GitHub Copilot Helper”), and local Git hook persistence. **Mirage Kitten attribution is Kaspersky's assessment, not independently established by ETW.** PollCat (co-disclosed in the same article) is **not** included in this filing.

## IC3 filing

| Field | Value |
|-------|-------|
| Submission ID | `dded86972e9347e0be27a6597b4cf08a` |
| Date filed | 2026-09-19 5:15:51 PM EST |
| Record | [`IC3_FILING_RECORD.md`](IC3_FILING_RECORD.md) |
| Separate related filings | Rapuncel `208b747c6f7445f0af2b69a9d63acc36`; Settra `631d8b4800d04bc19cdbfc6662e5c52c`; RatHat `f92c4c2f0dd3481f898fdd125e728adf` (no shared-operator claim) |
| Not included | PollCat (`ETW-POL-IC3`) |

## Why this may matter for FBI cyber / IC3 correlation

Cross-platform spyware targeting developer environments; Azure/Cloudflare-backed C2 patterns; mutable C2 lists; fake VS Code extension and Git-hook persistence.

## Highest-value indicators

- Kaspersky-published NodeRabbit archive MD5 values (see `03_INDICATORS.csv`); RankChallenge MD5 is PollCat — not a NodeRabbit IOC
- Non-Azure domains: `visitfinancedentists.com`; `healthcomfsdpower.com`; `msmanagementgrp.com`; `msmanagementgrpmedia.com`
- Multiple `*.azurewebsites.net` hosts (see CSV)
- Host pivots: shepherd-persist Git hooks; fake GitHub Copilot Helper VS Code extension; Linux paths under `~/.config/microsoft-edge-update` and `~/.config/intel-dsa`

Full table: `03_INDICATORS.csv` (44 rows).

## Critical analytical caveats

- Mirage Kitten attribution is Kaspersky's assessment — not independently established by ETW.
- Git hooks are local persistence unless further evidence shows repository/supply-chain propagation.
- Azure/Cloudflare edge IPs are not actor-owned infrastructure.
- COMMON TECHNIQUE overlap with PollCat does **not** establish shared authorship — do not merge cases.

## Suggested handling

1. Treat as defensive threat-intelligence referral, not a completed criminal case file.
2. Correlate published domains / MD5s / host artifacts against existing holdings.
3. Request sample acquisition through normal vendor/legal channels if needed — this package does not contain malware binaries.
4. Keep this family separate from other Emerging Threat Watch packages unless linkage evidence appears.
