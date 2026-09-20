# Abyssos — Summary

**Package:** `ETW-ABY-IC3` · **Status:** DRAFT — ready for human IC3 filing · **Primary freeze:** 2026-09-20

## Overview

Defensive threat-intelligence package concerning Abyssos as publicly documented by Zscaler ThreatLabz (2026-08-10). Zscaler describes a modular C++ RAT identified in late June 2026 with credential theft, file exfiltration, HVNC remote access, browser-session hijacking, and downloadable modules over a custom AES-GCM TCP protocol. **Author identity remains NOT_ESTABLISHED.** Initial delivery vector is not established in the primary report.

## Pre-filing cross-references (separate IC3 complaints — no shared-operator claim)

| Family | Package | Submission ID |
|--------|---------|---------------|
| Rapuncel | `ETW-RAP-IC3` | `208b747c6f7445f0af2b69a9d63acc36` |
| Settra | `ETW-SET-IC3` | `631d8b4800d04bc19cdbfc6662e5c52c` |
| RatHat | `ETW-RAT-IC3` | `f92c4c2f0dd3481f898fdd125e728adf` |
| NodeRabbit | `ETW-NRB-IC3` | `dded86972e9347e0be27a6597b4cf08a` |
| PollCat | `ETW-POL-IC3` | `98a4444754324e539dbbffcb10c70637` |
| SynkLoader | `ETW-SYN-IC3` | `3440d0c64dc240499ff66deaa3311a0b` |
| Showboat | `ETW-SHO-IC3` | `db42033f319844c08ad103befebfca08` |
| **Abyssos (this package)** | `ETW-ABY-IC3` | *not yet filed* |

## Highest-value indicators

- SHA-256 v2.4F: `52b400c5be1557a8df146f62fde76d906e7e0a92ed76788717ef61c758f315aa`
- SHA-256 v2.1F: `ca94d95413210a2a325155740eb8a5c58627ad5c4e704478621e7fc8165fe173`
- C2: `213.145.86.42`; `209.99.184.223`
- Host: `%TEMP%\fontconfigs`; `windows_update_cache.json`; crypto `1234567890abcdef`

Full table: `03_INDICATORS.csv` (10 ABY-IND rows). Dossier: `IC3_FULL_PACKAGE.md`.

## Critical analytical caveats

- PRIMARY-SOURCE indicators only — no ETW live C2 contact.
- Delivery vector under investigation — do not invent.
- Standalone — do not merge with other ETW filings.

## Suggested handling

1. Treat as defensive threat-intelligence referral.
2. Keep **separate** from other ETW packages.
3. After filing: record Submission ID in `IC3_FILING_RECORD.md`, this summary, `MASTER_INDEX.csv`, and root `README.md`.
