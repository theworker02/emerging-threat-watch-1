# TencShell — Family Summary

**Case ID slug:** `tencshell`  
**Package:** `ETW-TEN-IC3`  
**Status:** `PRIMARY_FROZEN`  
**Category:** Go implant / customized Rshell C2 (Tencent-like paths)  
**TLP:** TLP:AMBER+STRICT  
**Generated:** 2026-09-20T02:25:00Z  
**Source:** PRIMARY freeze `PS-TEN-001`

## Executive overview

Defensive threat-intelligence package concerning TencShell as publicly documented by Cato CTRL (2026). Cato describes a previously undocumented Go-based implant customized from the open-source Rshell C2 framework, delivered via a dropper → masqueraded .woff (Donut shellcode) → reflective in-memory load chain against a global manufacturer (India site / third-party access context). C2 traffic imitates Tencent-like web/API paths. Persistence via Run key value OneDriveHealthTask. Suspected China-linked assessment is vendor framing only. Author identity remains NOT_ESTABLISHED. Public Rshell OSS is NOT an IOC for this family.

## Indicator counts (this build)

| Class | Count |
|-------|------:|
| Domains / URLs | 1 |
| IPs | 3 |
| Hashes | 8 |
| Total IND rows | 15 |

## Case isolation

OSS lineage similarity ≠ shared operators. Authorship NOT_ESTABLISHED. Standalone.

## Cross-references

- Investigation: `investigations/tencshell/`
- LE package: `reports/law-enforcement/packages/10-tencshell/`
- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
