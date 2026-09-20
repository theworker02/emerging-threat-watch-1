# SynkLoader — Summary

**Package:** `ETW-SYN-IC3` · **Status:** FILED_IC3 · **Cutoff:** 2026-09-19

## Overview

Defensive threat-intelligence package concerning SynkLoader as publicly documented by Expel (2026-08-20, Marcus Hutchins). Expel describes a modular mixed-language loader delivered through Microsoft Teams phishing posing as IT helpdesk (external `*.onmicrosoft.com` tenant, display name IT Service Desk), with initial MSI hosted on Azure Blob Storage (`filereserve.blob.core.windows.net/.../331.msi`, product name PowershellCleaner). Expel reports nested PowerShell decryption into an in-memory Python loader (`ss.py`), fake Visual C++ DLLs (`msvcp150.dll` / `msvcp160.dll`), a fake Windows 11 lock-screen credential-theft module (PhishLocker), and additional modules including TrafficRedirector and StreamMaster VNC. **Author identity remains NOT_ESTABLISHED.** Matanbuchus is a technique comparator only — do not file jointly.

## IC3 filing

| Field | Value |
|-------|-------|
| Submission ID | `3440d0c64dc240499ff66deaa3311a0b` |
| Date filed | 2026-09-19 10:04:35 PM EST |
| Date filed (UTC) | 2026-09-20T02:04:35Z |
| Record | [`IC3_FILING_RECORD.md`](IC3_FILING_RECORD.md) |
| Separate related filings | Rapuncel `208b747c6f7445f0af2b69a9d63acc36`; Settra `631d8b4800d04bc19cdbfc6662e5c52c`; RatHat `f92c4c2f0dd3481f898fdd125e728adf`; NodeRabbit `dded86972e9347e0be27a6597b4cf08a`; PollCat `98a4444754324e539dbbffcb10c70637` (no shared-operator claim) |
| Not merged | Matanbuchus (`ETW-MAT-IC3`) — technique comparator only |

## Why this may matter for FBI cyber / IC3 correlation

Teams helpdesk phishing with fake lock-screen credential theft and tunneling into enterprise environments.

## Highest-value indicators

- Delivery URL: `https://filereserve.blob.core.windows.net/vgnghuyk/331/331.msi`
- SHA-256 `331.msi`: `151d2a7f52f047638ca8ad80c859c6bfe04d7510fb10933817fa0e3ba5d07a11` (+ 10 more module hashes — see CSV)
- Domains: `neversoftmain.net`; `rootfarmapp.net`; `tripinupdate.net`; `dondermicapp.net`; `aroclenetapp.net`
- OBSERVED_PASSIVE A: `149.248.76.220`; `162.33.177.8`; `216.245.184.14`; `64.94.85.67`
- ChaCha sigma: `mlswgtppayebtezk` / `lwifnrfiosmfrubf`
- PDB (build artifact only): `C:\Users\genry\source\repos\pwshnewdll\...\pwshnewdll.pdb`

Full table: `03_INDICATORS.csv` (29 rows). Structured dossier: `IC3_FULL_PACKAGE.md`.

## Critical analytical caveats

- Domain/hash/URL rows are PRIMARY-SOURCE (Expel); IPv4 rows SYN-IND-0026–0029 are OBSERVED_PASSIVE DNS A — not live C2 contact.
- Shared ASN AS399629 is INFRASTRUCTURE_OVERLAP candidate only — not operator identity.
- Azure Blob MSI host edge IP is ASSOCIATION_ONLY.
- Secondary ransomware-follow-on / IAB framing is not established by ETW.
- Resolving a published domain ≠ proof C2 is currently active.

## Suggested handling

1. Treat as defensive threat-intelligence referral, not a completed criminal case file.
2. Correlate hashes / domains / OBSERVED_PASSIVE IPs against existing holdings.
3. Keep **separate** from other ETW packages unless linkage evidence appears.
