# StarlandRAT — Family Summary

**Case ID slug:** `starlandrat`  
**Package:** `ETW-STR-IC3`  
**Status:** `PRIMARY_FROZEN`  
**Category:** Python RAT + WLDR PowerShell C2 (UAT-11795)  
**TLP:** TLP:AMBER+STRICT  
**Generated:** 2026-09-20T02:25:00Z  
**Source:** PRIMARY freeze `PS-STR-001`

## Executive overview

Defensive threat-intelligence package concerning Starland RAT and the companion WLDR PowerShell C2 agent as publicly documented by Cisco Talos (UAT-11795 financially motivated campaign). Talos describes ClickFix / trojanized installer delivery (Webex/Zoom/MobaXterm/DBeaver-class lures), a memory-resident Python RAT with crypto-wallet recon, Telegram notification bots, and Polygon smart-contract fallback C2, plus optional CastleStealer/Remcos follow-ons and WLDR in-memory PowerShell post-ex. UAT-11795 / Russian-speaking framing is vendor assessment — ETW does not independently establish attribution. Author identity remains NOT_ESTABLISHED. WLDR tracked as companion under this case until distinct corpus warrants split.

## Indicator counts (this build)

| Class | Count |
|-------|------:|
| Domains / URLs | 7 |
| IPs | 0 |
| Hashes | 0 |
| Total IND rows | 17 |

## Case isolation

WLDR Agent companion tracking under this case folder until distinct corpus warrants split. Do not attribute to active ETW families.

## Cross-references

- Investigation: `investigations/starlandrat/`
- LE package: `reports/law-enforcement/packages/15-starlandrat/`
- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
