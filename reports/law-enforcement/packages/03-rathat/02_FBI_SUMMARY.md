# RatHat — FBI / Field-Office Summary

**Package:** `ETW-RAT-IC3` · **Status:** DRAFT · **Cutoff:** 2026-09-19

## One-paragraph summary

I am reporting defensive threat-intelligence information concerning Android malware publicly named RatHat by Zimperium zLabs on September 16, 2026. Zimperium reports that the malware abuses Android Accessibility (Accessibility engine class SystemHelperService) to enable Wireless Debugging, retrieve the device's local ADB pairing information, self-pair with the local ADB daemon and obtain shell-level execution. It then stages native Go components outside the ordinary APK lifecycle, including a local service and an FRP-derived reverse-tunnel component (fatedier/frp; runtime FrpsAddr/FrpsPort/FrpsToken via main.fetchFrpcConfigFromServer). Zimperium reports keypad-geometry artifact locateValues.json and that the surviving service can reinstall the APK after removal and restore Accessibility configuration. Zimperium published companion IOC files under github.com/Zimperium/IOC/tree/master/2026-09-RatHat (apks.csv, c2.csv, phishing.csv). I have not actively connected to suspected RatHat command-and-control infrastructure. Android applicationId / package names remain unpublished in reachable primary sources and are not invented here.

## Why this may matter to FBI cyber / IC3 correlation

Mobile malware obtaining Android shell via Wireless Debugging self-pair; persistence outside APK lifecycle; credential and banking targeting

## Highest-value indicators (primary-source; not ETW-observed)

- Native / service: liblocal-service.so; libmedia_codec.so (FRP-derived); SystemHelperService; locateValues.json
- Local service: 127.0.0.1:7910; staging /data/local/tmp
- URI paths: /api/adbk/upload; /api/tun/config; /api/data/credentials; /api/node/register
- Zimperium c2.csv examples: fegrs.adidasabc.com; admin.xiongmaocs.help; oop.uuokxx.com; andxxxo.com
- Zimperium phishing.csv examples: kingbss.com; app.tmgg01.top; primevoria.com; S3 APK URL (do not download)
- Representative APK SHA-256 from apks.csv (162 total listed by vendor): see RAT-IND-0040
- Anti-analysis: Frida probe 27042/tcp; getevent on /dev/input
- Package names: not published — do not invent

Full table: `03_INDICATORS.csv`

## Critical analytical caveats

- Blog body is architectural/URI-path heavy; C2 hosts and APK hashes come from Zimperium's published IOC tree — do not invent additional hosts, hashes, or package names.
- Android applicationId / signing certificates are still open gaps — do not fabricate package names.
- Prefer architectural/URI-path indicators and remediation facts over "AI malware" marketing framing.
- Uninstalling the visible APK may not remove compromise.
- Passive CT/urlscan on published apexes is not ownership or live C2 proof; ETW has not contacted C2.

## Suggested handling

1. Treat as **defensive threat-intelligence referral**, not a completed criminal case file.
2. Correlate MeshAgent / domain / hash / URI-path indicators against existing FBI/IC3 holdings.
3. Request sample acquisition through normal vendor/legal channels if needed — this package does not contain malware binaries.
4. Keep this family **separate** from other Emerging Threat Watch packages unless linkage evidence appears.
