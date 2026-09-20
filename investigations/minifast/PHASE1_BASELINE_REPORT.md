# MiniFast — Phase 1 Baseline

**Generated:** 2026-09-20T02:25:00Z  
**Status:** `PRIMARY_FROZEN`

## Summary

Defensive threat-intelligence package concerning MiniFast as publicly documented by Check Point Research in Fast and Furious — Nimbus Manticore operations (2026). Check Point describes a previously undocumented 64-bit .NET backdoor (export CheckForUpdates / UpdateChecker.dll) delivered via AppDomain hijacking and a trojanized Zoom installer flow (Zoominstall64.zip), with persistence by hijacking ZoomUpdateTaskUser. C2 uses JSON/HTTPS with Chrome UA impersonation and Azure Web App hosts. Actor framing (Nimbus Manticore / UNC1549 / IRGC-linked) is vendor assessment — ETW does not independently establish attribution. Structural C2 notes vs PollCat are ASSOCIATION_ONLY — do NOT merge into POL case. Authorship link NOT_ESTABLISHED.

| Field | Value |
|-------|-------|
| Family | MiniFast |
| Case code | MNF |
| Disclosure | Check Point Research 2026-05 |
| PRIMARY IOCs in this build | **30** |
| Independently observed infra | **None** |
| Author attribution | **NOT_ESTABLISHED** |
| Primary freeze | `evidence/primary-sources/minifast/checkpoint-nimbus-manticore-minifast-2026.html` |
| SHA-256 | `a3d4d4a8346aaef3b9af65ac6a6290da63e1d85cc961d4b8fca7b50b065e93e9` |

## Cross-references

- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
- LE package: `reports/law-enforcement/packages/11-minifast/`
- CTI tree: `reports/law-enforcement/CTI-Evidence-Repository/families/MiniFast/`
