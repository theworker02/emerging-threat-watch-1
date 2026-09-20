# TencShell — Phase 1 Baseline

**Generated:** 2026-09-20T02:25:00Z  
**Status:** `PRIMARY_FROZEN`

## Summary

Defensive threat-intelligence package concerning TencShell as publicly documented by Cato CTRL (2026). Cato describes a previously undocumented Go-based implant customized from the open-source Rshell C2 framework, delivered via a dropper → masqueraded .woff (Donut shellcode) → reflective in-memory load chain against a global manufacturer (India site / third-party access context). C2 traffic imitates Tencent-like web/API paths. Persistence via Run key value OneDriveHealthTask. Suspected China-linked assessment is vendor framing only. Author identity remains NOT_ESTABLISHED. Public Rshell OSS is NOT an IOC for this family.

| Field | Value |
|-------|-------|
| Family | TencShell |
| Case code | TEN |
| Disclosure | Cato CTRL 2026-04/2026-05 |
| PRIMARY IOCs in this build | **15** |
| Independently observed infra | **None** |
| Author attribution | **NOT_ESTABLISHED** |
| Primary freeze | `evidence/primary-sources/tencshell/cato-tencshell-2026.md.txt` |
| SHA-256 | `742dedea94fc4a0d35a1c549447d3dc21f65f903ca41c33543fce471d5259c28` |

## Cross-references

- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
- LE package: `reports/law-enforcement/packages/10-tencshell/`
- CTI tree: `reports/law-enforcement/CTI-Evidence-Repository/families/TencShell/`
