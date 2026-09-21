# IC3 / FBI Full Complaint Package — Insomnia RAT

**Status:** `PRIMARY_FROZEN` · **Primary freeze:** 2026-09-21  
**Family:** Insomnia RAT only (case-isolated)  
**Portal:** https://www.ic3.gov/

## Filing identity

| Field | Value |
|-------|-------|
| Suggested subject | Defensive TI referral — Insomnia RAT (Unit 42 Sept 2026 (CL-CRI-1171 / OfferLoader delivery)) — `ETW-INS-IC3` |
| Dollar loss claimed | None |
| Malware binaries attached | No |
| Independently observed by ETW | None |

## Indicators

See `03_INDICATORS.csv` (12 INS-IND rows).

## Narrative

Dual Node.js + Python backdoor (UA insomnia/2023.4.0); installs Node/Python runtimes; CrowdStrike typosquat C2; delivered via OfferLoader PPI — do NOT merge authorship with OfferLoader/ARKTunnel/Docro.

Primary: https://unit42.paloaltonetworks.com/ppi-network-malware-campaign-analysis/
