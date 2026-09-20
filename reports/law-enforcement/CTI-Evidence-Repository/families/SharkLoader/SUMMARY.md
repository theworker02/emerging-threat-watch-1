# SharkLoader — Family Summary

**Case ID slug:** `sharkloader`  
**Package:** `ETW-SHK-IC3`  
**Status:** `FILED_IC3` · `6ed57963d0c64750aa14b6fcbaa2e576`  
**Category:** Custom loader → Cobalt Strike (StrikeShark campaign)  
**TLP:** TLP:AMBER+STRICT  
**Generated:** 2026-09-20T02:25:00Z  
**Source:** PRIMARY freeze `PS-SHK-001`

## Executive overview

Defensive threat-intelligence package concerning SharkLoader as publicly documented by Kaspersky GReAT (Securelist 2026-06-24) in the StrikeShark campaign. Kaspersky describes a multi-component custom loader that DLL-sideloads via abused legitimate binaries (commonly SystemSettings.exe → SystemSettings.dll), decrypts DscCoreR.mui / SyncRes.dat modules, installs API hooks (Detours/MinHook), and executes Cobalt Strike Beacon in memory. Delivery includes exploitation of internet-facing apps and malicious droppers. Kaspersky does not attribute StrikeShark to a known APT with high confidence. Author identity remains NOT_ESTABLISHED.

## Indicator counts (this build)

| Class | Count |
|-------|------:|
| Domains / URLs | 4 |
| IPs | 0 |
| Hashes | 8 |
| Total IND rows | 19 |

## Case isolation

Standalone candidate promoted after primary freeze. Loader→CS is COMMON TECHNIQUE class only vs other loaders.

## Cross-references

- Investigation: `investigations/sharkloader/`
- LE package: `reports/law-enforcement/packages/09-sharkloader/`
- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
