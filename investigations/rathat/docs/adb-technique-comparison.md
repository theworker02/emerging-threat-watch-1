# Wireless ADB Self-Pairing — Technique Comparison (NOT Lineage)

**Scope:** Technique / trust-surface comparison only.  
**Forbidden:** Shared authorship, IOC transfer, merged attribution.  
**Cutoff:** 2026-09-19

## Pattern under study

Accessibility abuse → enable Developer Options / Wireless Debugging → scrape pairing code + port from UI → local SPAKE2/TLS pair to `127.0.0.1` adbd → **shell UID 2000** without USB/host PC.

## Family notes

| Family | Primary source | Self-ADB? | Post-shell stack (reported) | Comparison confidence |
|--------|----------------|-----------|-----------------------------|------------------------|
| **RatHat** | Zimperium 2026-09-16 | Yes (`SystemHelperService` + libadb-android) | Go agent + FRP; hardware getevent keylog | High (in-scope primary) |
| **ToxicPanda 2.0** | Zimperium ToxicPanda blog | Yes (`startAutoPair` / `manualPair` style flows) | Broad command set; VPN Play block in some reporting | High for technique; **not** RatHat lineage |
| **RedHook** | Group-IB (Wireless ADB upgrade) | Yes | Shizuku-based privileged server (`libmx.so`) | High for technique; **not** RatHat lineage |

## Analytical question

Is autonomous Wireless ADB self-pairing becoming a **reusable Android malware design pattern** (shared OS trust-surface) rather than a single-actor signature?

**ETW answer (Phase 1):** **Likely yes as a technique class** — multiple independent primaries describe the same OS feature abuse. That is **COMMON TECHNIQUE**, not evidence of common operators.

## Trust-surface takeaway

Wireless Debugging is a **DEVELOPER TOOL** that detection often under-weights because it is “local” and user-toggled. Once Accessibility is granted, the pairing secret is UI-scrapable.

## Google / Play Protect note (deep-pass 2026-09-19)

Passive review of the Android Security Bulletin index and a Google security-blog search for “Wireless Debugging” did **not** yield an official Google Play Protect / ASB advisory that names RatHat-style on-device ADB self-pairing. Defenders currently rely on vendor primaries (Zimperium / Group-IB / etc.) for this technique class. Negative search ≠ proof Google has never discussed related abuse; it means no grounded Google-named RatHat advisory was located in this pass.
