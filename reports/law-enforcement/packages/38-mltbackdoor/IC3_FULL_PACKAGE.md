# IC3 / FBI Full Complaint Package — MLTBackdoor

**Status:** `PRIMARY_FROZEN` · **Primary freeze:** 2026-09-21  
**Family:** MLTBackdoor only (case-isolated)  
**Portal:** https://www.ic3.gov/

## Filing identity

| Field | Value |
|-------|-------|
| Suggested subject | Defensive TI referral — MLTBackdoor (Zscaler ThreatLabz May 2026) — `ETW-MLT-IC3` |
| Dollar loss claimed | None |
| Malware binaries attached | No |
| Independently observed by ETW | None |

## Indicators

See `03_INDICATORS.csv` (12 MLT-IND rows).

## Narrative

Multi-stage ClickFix loader → MLTBackdoor with BOF loading, ECDH/AES-GCM C2, DGA fallback. Likely ransomware foothold tool — operator NOT_ESTABLISHED.

Primary: https://www.zscaler.com/blogs/security-research/technical-analysis-mltbackdoor
