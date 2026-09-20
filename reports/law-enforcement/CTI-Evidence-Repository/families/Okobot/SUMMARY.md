# Okobot — Family Summary

**Case ID slug:** `okobot`  
**Package:** `ETW-OKO-IC3`  
**Status:** `PRIMARY_FROZEN`  
**Category:** Multi-payload crypto-theft framework (OkoSpyware / SeedHunter)  
**TLP:** TLP:AMBER+STRICT  
**Generated:** 2026-09-20T02:25:00Z  
**Source:** PRIMARY freeze `PS-OKO-001`

## Executive overview

Defensive threat-intelligence package concerning the OkoBot framework as publicly documented by Kaspersky GReAT (Securelist). Kaspersky describes a multi-stage campaign (≥20 payloads) initiated via TookPS PowerShell, configuring an SSH bot and dispatching modules including OkoSpyware (window video + keylogging of crypto wallets/password managers), SeedHunter (hardware-wallet seed phishing overlays), MC Keylogger, and browser extension loaders (e.g. Rilide). Victims across 25+ countries; activity ongoing as of publication. Russian-speaking crimeware signals noted by Kaspersky — author identity remains NOT_ESTABLISHED.

## Indicator counts (this build)

| Class | Count |
|-------|------:|
| Domains / URLs | 7 |
| IPs | 3 |
| Hashes | 15 |
| Total IND rows | 30 |

## Case isolation

Standalone candidate. Case-isolated from all active families.

## Cross-references

- Investigation: `investigations/okobot/`
- LE package: `reports/law-enforcement/packages/13-okobot/`
- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
