# IC3 / FBI Full Complaint Package — DenoRAT / DinDoor / NightshadeC2

**Status:** `PRIMARY_FROZEN` · **Primary freeze:** 2026-09-21  
**Family:** DenoRAT / DinDoor / NightshadeC2 only (case-isolated)  
**Portal:** https://www.ic3.gov/

## Filing identity

| Field | Value |
|-------|-------|
| Suggested subject | Defensive TI referral — DenoRAT / DinDoor / NightshadeC2 (eSentire TRU June 2026 (TAG-150)) — `ETW-DEN-IC3` |
| Dollar loss claimed | None |
| Malware binaries attached | No |
| Independently observed by ETW | None |

## Indicators

See `03_INDICATORS.csv` (18 DEN-IND rows).

## Narrative

TAG-150 ClickFix → MSI → Deno runtime → DinDoor loader → DenoRAT → in-memory NightshadeC2. Tracked as one ETW case for the disclosed chain; NightshadeC2 may have broader use — do not expand IOCs beyond PRIMARY.

Primary: https://www.esentire.com/blog/dindoor-denorat-and-nightshadec2-analyzing-tag-150s-evolving-tradecraft
