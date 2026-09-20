# MiniFast — Family Summary

**Case ID slug:** `minifast`  
**Package:** `ETW-MNF-IC3`  
**Status:** `PRIMARY_FROZEN`  
**Category:** AI-assisted .NET backdoor via Zoom trust abuse (Nimbus Manticore)  
**TLP:** TLP:AMBER+STRICT  
**Generated:** 2026-09-20T02:25:00Z  
**Source:** PRIMARY freeze `PS-MNF-001`

## Executive overview

Defensive threat-intelligence package concerning MiniFast as publicly documented by Check Point Research in Fast and Furious — Nimbus Manticore operations (2026). Check Point describes a previously undocumented 64-bit .NET backdoor (export CheckForUpdates / UpdateChecker.dll) delivered via AppDomain hijacking and a trojanized Zoom installer flow (Zoominstall64.zip), with persistence by hijacking ZoomUpdateTaskUser. C2 uses JSON/HTTPS with Chrome UA impersonation and Azure Web App hosts. Actor framing (Nimbus Manticore / UNC1549 / IRGC-linked) is vendor assessment — ETW does not independently establish attribution. Structural C2 notes vs PollCat are ASSOCIATION_ONLY — do NOT merge into POL case. Authorship link NOT_ESTABLISHED.

## Indicator counts (this build)

| Class | Count |
|-------|------:|
| Domains / URLs | 13 |
| IPs | 0 |
| Hashes | 12 |
| Total IND rows | 30 |

## Case isolation

Context for PollCat lineage assessment only — do NOT auto-merge into POL case. authorship_link=NOT_ESTABLISHED.

## Cross-references

- Investigation: `investigations/minifast/`
- LE package: `reports/law-enforcement/packages/11-minifast/`
- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
