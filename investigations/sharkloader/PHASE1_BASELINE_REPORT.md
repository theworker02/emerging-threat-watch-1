# SharkLoader — Phase 1 Baseline

**Generated:** 2026-09-20T02:25:00Z  
**Status:** `PRIMARY_FROZEN`

## Summary

Defensive threat-intelligence package concerning SharkLoader as publicly documented by Kaspersky GReAT (Securelist 2026-06-24) in the StrikeShark campaign. Kaspersky describes a multi-component custom loader that DLL-sideloads via abused legitimate binaries (commonly SystemSettings.exe → SystemSettings.dll), decrypts DscCoreR.mui / SyncRes.dat modules, installs API hooks (Detours/MinHook), and executes Cobalt Strike Beacon in memory. Delivery includes exploitation of internet-facing apps and malicious droppers. Kaspersky does not attribute StrikeShark to a known APT with high confidence. Author identity remains NOT_ESTABLISHED.

| Field | Value |
|-------|-------|
| Family | SharkLoader |
| Case code | SHK |
| Disclosure | Kaspersky GReAT / Securelist 2026-06-24 |
| PRIMARY IOCs in this build | **19** |
| Independently observed infra | **None** |
| Author attribution | **NOT_ESTABLISHED** |
| Primary freeze | `evidence/primary-sources/sharkloader/securelist-strikeshark-2026-06-24.html` |
| SHA-256 | `c5af7fb5acf172632f63b9763e511d756564027cff5cf0ce8a6ffe2fa90934b2` |

## Cross-references

- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
- LE package: `reports/law-enforcement/packages/09-sharkloader/`
- CTI tree: `reports/law-enforcement/CTI-Evidence-Repository/families/SharkLoader/`
