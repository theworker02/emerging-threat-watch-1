# NodeRabbit — Family Summary

**Case ID slug:** `noderabbit`  
**Category:** Cross-platform Node.js developer-targeted RAT  
**TLP:** TLP:AMBER+STRICT (see repository `TLP-LICENSE.md`)  
**Generated:** 2026-09-19T19:25:39Z  
**Source:** Emerging Threat Watch published-indicators (no invented IOCs)

## Executive overview

Defensive threat-intelligence package for **NodeRabbit**. Indicators below are transcribed from vendor PRIMARY-SOURCE reporting and/or ETW OBSERVED_PASSIVE collection. **Author personal identity / home IP is NOT ESTABLISHED.**

## Indicator counts (this build)

| Class | Count |
|-------|------:|
| Domains / URLs / URI paths (domain-class export) | 28 |
| IPs | 0 |
| Hashes (SHA-256/MD5) | 13 |
| Total published-indicator rows | 44 |

## Machine-readable

- STIX 2.1: `stix_bundle.json`
- IOCs: `iocs/ips.csv`, `iocs/domains.csv`, `iocs/hashes.csv`

## Evidence folders (placeholders until lab fills)

| Folder | Status |
|--------|--------|
| `network_captures/` | Empty — requires human/licensed sandbox PCAP (see ENFORCEMENT_READINESS) |
| `memory_dumps/` | Empty — no ETW decrypted stubs in-repo |
| `rules/` | Stub YARA/Sigma placeholders — expand when signatures are validated |
| `actors_and_finance/` | No crypto wallets established for this family in ETW corpus |

## Case isolation

Do not merge with other ETW families without linkage evidence. PollCat ↔ NodeRabbit: COMMON TECHNIQUE / Moderate delivery overlap only — **not** shared authorship.

## Cross-references (full research corpus)

- Investigation: `investigations/noderabbit/`
- LE narrative package: `reports/law-enforcement/packages/`
- Enforcement readiness: `docs/ENFORCEMENT_READINESS.md`
