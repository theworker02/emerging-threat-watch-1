# Settra — Summary

**Package:** `ETW-SET-IC3` · **Status:** FILED_IC3 · **Cutoff:** 2026-09-19

## Overview

Defensive threat-intelligence package concerning ransomware/extortion activity publicly tracked as Settra. Cynet, Huntress, and MOXFIVE have published IR/technical findings. Cynet reverse engineered a password-gated two-stage Windows encryptor and reported that the encryptor itself did not contain file-exfiltration functionality. Huntress reported MeshAgent infrastructure `45.13.122.7` and `193.5.65.114` and workstation lead `WIN-LIVFRVQFMKO` (also seen by Kaspersky GERT as an SSL CN in unrelated FortiClient EMS research — **not Settra-exclusive**). Passive observations on `193.5.65.114` (MeshCentral chronology / Rapid Seedbox RDAP) are investigative leads only — **not exclusive ownership**.

## IC3 filing

| Field | Value |
|-------|-------|
| Submission ID | `631d8b4800d04bc19cdbfc6662e5c52c` |
| Date filed | 2026-09-19 4:59:46 PM EST |
| Record | [`IC3_FILING_RECORD.md`](IC3_FILING_RECORD.md) |
| Separate related filing | Rapuncel `208b747c6f7445f0af2b69a9d63acc36` (no shared-operator claim) |

## Why this may matter for FBI cyber / IC3 correlation

Enterprise ransomware with documented MeshAgent C2 IPs and BYOVD/defense-impairment tooling in IR reporting.

## Highest-value indicators

- MeshAgent C2 IPv4: `45.13.122.7` (July 2026 Huntress); `193.5.65.114` (Sept 2026 Huntress; earlier MeshCentral OBSERVED_PASSIVE — not exclusive)
- Workstation lead: `WIN-LIVFRVQFMKO` (Huntress + Kaspersky SSL CN — not Settra-exclusive)
- Overlap leads: `id-manulife.com`; tlsIssuer `MeshCentralRoot-eca57f`
- Ransom notes: `RESTORE_FILES.txt` / `RESTORE_FILES.html`
- Extensions: `.locked` / `.locked_wip`; naming pattern `*_win64.exe`
- BYOVD filenames: `gdrv.sys`; `STProcessMonitor_v114.sys` (operator tooling context)

Full table: `03_INDICATORS.csv` (16 rows). No usable Settra sample SHA-256 list in retained public pages.

## Critical analytical caveats

- Encryptor (malware) and operator intrusion tooling are separate — do not say "Settra uses Mimikatz."
- `WIN-LIVFRVQFMKO` is an investigative lead — UNKNOWN / not Settra-exclusive; do not backdate Settra to 2024.
- `193.5.65.114` MeshCentral chronology and Rapid Seedbox RDAP are INFRASTRUCTURE_OVERLAP leads — not Settra-exclusive ownership.
- OBSERVED_PASSIVE MeshCentral/RDAP facts are not campaign-ownership claims.

## Suggested handling

1. Treat as defensive threat-intelligence referral, not a completed criminal case file.
2. Correlate MeshAgent / hostname / artifact indicators against existing holdings.
3. Request sample acquisition through normal vendor/legal channels if needed — this package does not contain malware binaries.
4. Keep this family separate from other Emerging Threat Watch packages unless linkage evidence appears.
