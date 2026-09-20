# Okobot — Phase 1 Baseline

**Generated:** 2026-09-20T02:25:00Z  
**Status:** `PRIMARY_FROZEN`

## Summary

Defensive threat-intelligence package concerning the OkoBot framework as publicly documented by Kaspersky GReAT (Securelist). Kaspersky describes a multi-stage campaign (≥20 payloads) initiated via TookPS PowerShell, configuring an SSH bot and dispatching modules including OkoSpyware (window video + keylogging of crypto wallets/password managers), SeedHunter (hardware-wallet seed phishing overlays), MC Keylogger, and browser extension loaders (e.g. Rilide). Victims across 25+ countries; activity ongoing as of publication. Russian-speaking crimeware signals noted by Kaspersky — author identity remains NOT_ESTABLISHED.

| Field | Value |
|-------|-------|
| Family | Okobot |
| Case code | OKO |
| Disclosure | Kaspersky GReAT / Securelist 2026 |
| PRIMARY IOCs in this build | **30** |
| Independently observed infra | **None** |
| Author attribution | **NOT_ESTABLISHED** |
| Primary freeze | `evidence/primary-sources/okobot/securelist-okobot-2026.html` |
| SHA-256 | `04eb0610ddb6e36d4cb0c12917e90424741162b091b87426a5c4c3cc1bf431ec` |

## Cross-references

- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
- LE package: `reports/law-enforcement/packages/13-okobot/`
- CTI tree: `reports/law-enforcement/CTI-Evidence-Repository/families/Okobot/`
