# StarlandRAT — Phase 1 Baseline

**Generated:** 2026-09-20T02:25:00Z  
**Status:** `PRIMARY_FROZEN`

## Summary

Defensive threat-intelligence package concerning Starland RAT and the companion WLDR PowerShell C2 agent as publicly documented by Cisco Talos (UAT-11795 financially motivated campaign). Talos describes ClickFix / trojanized installer delivery (Webex/Zoom/MobaXterm/DBeaver-class lures), a memory-resident Python RAT with crypto-wallet recon, Telegram notification bots, and Polygon smart-contract fallback C2, plus optional CastleStealer/Remcos follow-ons and WLDR in-memory PowerShell post-ex. UAT-11795 / Russian-speaking framing is vendor assessment — ETW does not independently establish attribution. Author identity remains NOT_ESTABLISHED. WLDR tracked as companion under this case until distinct corpus warrants split.

| Field | Value |
|-------|-------|
| Family | StarlandRAT |
| Case code | STR |
| Disclosure | Cisco Talos 2026-07 |
| PRIMARY IOCs in this build | **17** |
| Independently observed infra | **None** |
| Author attribution | **NOT_ESTABLISHED** |
| Primary freeze | `evidence/primary-sources/starlandrat/talos-uat-11795-starland-wldr.html` |
| SHA-256 | `0eff5ee5f2e32d8cc50ea58a9a4f6bf94b4919a9f997112d88f199e6a735eb84` |

## Cross-references

- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
- LE package: `reports/law-enforcement/packages/15-starlandrat/`
- CTI tree: `reports/law-enforcement/CTI-Evidence-Repository/families/StarlandRAT/`
