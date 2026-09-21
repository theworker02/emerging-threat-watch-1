# IC3 / FBI Full Complaint Package — SmartRAT

**Status:** `PRIMARY_FROZEN` · **Primary freeze:** 2026-09-21  
**Family:** SmartRAT only (case-isolated)  
**Portal:** https://www.ic3.gov/

## Filing identity

| Field | Value |
|-------|-------|
| Suggested subject | Defensive TI referral — SmartRAT (Zscaler ThreatLabz March 2026) — `ETW-SMT-IC3` |
| Dollar loss claimed | None |
| Malware binaries attached | No |
| Independently observed by ETW | None |

## Indicators

See `03_INDICATORS.csv` (10 SMT-IND rows).

## Narrative

PowerShell RAT via AI-built ClickFix bank lure; TCP/51888 C2; banking overlays + QR-swap; weak C2 panel auth noted by vendor.

Primary: https://www.zscaler.com/blogs/security-research/clickfix-campaign-generated-ai-delivers-smartrat
