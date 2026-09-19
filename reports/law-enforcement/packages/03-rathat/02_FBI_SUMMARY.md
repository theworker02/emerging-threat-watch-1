# RatHat — Summary

**Package:** `ETW-RAT-IC3` · **Status:** FILED_IC3 · **Cutoff:** 2026-09-19

## Overview

Defensive threat-intelligence package concerning Android malware publicly named RatHat by Zimperium zLabs (2026-09-16). Zimperium reports Accessibility abuse (`SystemHelperService`) to enable Wireless Debugging, self-pair with local ADB, obtain shell execution, and stage native Go components outside the ordinary APK lifecycle, including an FRP-derived reverse-tunnel component. Companion IOC files were published under `github.com/Zimperium/IOC/tree/master/2026-09-RatHat`. Android `applicationId` / package names remain unpublished in reachable primaries and are **not invented**. No active C2 contact by ETW.

## IC3 filing

| Field | Value |
|-------|-------|
| Submission ID | `f92c4c2f0dd3481f898fdd125e728adf` |
| Date filed | 2026-09-19 5:08:29 PM EST |
| Record | [`IC3_FILING_RECORD.md`](IC3_FILING_RECORD.md) |
| Separate related filings | Rapuncel `208b747c6f7445f0af2b69a9d63acc36`; Settra `631d8b4800d04bc19cdbfc6662e5c52c` (no shared-operator claim) |

## Why this may matter for FBI cyber / IC3 correlation

Mobile malware obtaining Android shell via Wireless Debugging self-pair; persistence outside APK lifecycle; credential and banking targeting.

## Highest-value indicators

- Native / service: `liblocal-service.so`; `libmedia_codec.so` (FRP-derived); `SystemHelperService`; `locateValues.json`
- Local service: `127.0.0.1:7910` (on-device — not remote C2 ownership); staging `/data/local/tmp`
- URI paths: `/api/adbk/upload`; `/api/tun/config`; `/api/data/credentials`; `/api/node/register`
- C2 examples: `fegrs.adidasabc.com`; `admin.xiongmaocs.help`; `oop.uuokxx.com`; `andxxxo.com`
- Phishing examples: `kingbss.com`; `app.tmgg01.top`; `primevoria.com`; S3 APK URL (do not download)
- Representative APK SHA-256: `00ba0d5aea129f098b5a609633ac77cd642fddba8b64f6332e49e6d33294992e`
- Package names: **not published — not invented**

Full table: `03_INDICATORS.csv` (40 rows).

## Critical analytical caveats

- Prefer architectural/URI-path indicators and published IOC-tree hosts/hashes over marketing framing.
- Uninstalling the visible APK may not remove compromise (per Zimperium).
- Passive CT/urlscan on published apexes is not ownership or live C2 proof.

## Suggested handling

1. Treat as defensive threat-intelligence referral, not a completed criminal case file.
2. Correlate published domains / hashes / URI paths against existing holdings.
3. Request sample acquisition through normal vendor/legal channels if needed — this package does not contain malware binaries.
4. Keep this family separate from other Emerging Threat Watch packages unless linkage evidence appears.
