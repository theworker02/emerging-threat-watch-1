# Evidentiary Threat Intelligence Package

## Executive Summary

This repository folder contains **actionable technical telemetry** structured for automated ingestion and federal analyst review (FBI / HSI / CISA and partners). It covers Emerging Threat Watch **active cases**:

**Rapuncel, Settra, RatHat, NodeRabbit, PollCat, SynkLoader, Showboat.**

Commodity/MaaS families such as AsyncRAT, Remcos, Lumma Stealer, and Matanbuchus are tracked as **candidates / technique comparators** in the parent repo (`docs/CANDIDATE_FAMILIES.md`) and are **not** full evidence trees here until promoted.

## Chain of Custody & Integrity

- **Collection / research cutoff (v1):** 2026-09-19 (ongoing passive enrichment may append newer `retrieved_utc` stamps)
- **Integrity verification:** SHA-256 of package text/CSV/STIX artifacts listed in `CHECKSUMS.sha256`. When GPG-signed, also see `CHECKSUMS.asc` (gitignored if present).
- **Classification / TLP:** **TLP:AMBER+STRICT** — see `TLP-LICENSE.md`
- **Provenance:** Indicators carry PRIMARY-SOURCE / OBSERVED_PASSIVE labels. Retrieving vendor articles ≠ independent infra observation. **Author attribution = NOT ESTABLISHED** unless a public LE/court source says otherwise.
- **No malware binaries** are stored in this package (see parent `.gitignore`). PCAPs/memory dumps are placeholders until human-lab fills them.

## Key Threat Summary Matrix

| Threat Family | Category | Primary C2 / Infra leads | Crypto / Financial Identifiers | STIX 2.1 File |
| :--- | :--- | :--- | :--- | :--- |
| **Rapuncel** | Windows info stealer / GitHub-SEO distribution | `2.26.126.50` | N/A (none established) | `./families/Rapuncel/stix_bundle.json` |
| **Settra** | Enterprise ransomware + operator intrusion | `45.13.122.7, 193.5.65.114` | N/A (none established) | `./families/Settra/stix_bundle.json` |
| **RatHat** | Android Accessibility / Wireless ADB RAT | `liblocal-service.so` | N/A (none established) | `./families/RatHat/stix_bundle.json` |
| **NodeRabbit** | Cross-platform Node.js developer-targeted RAT | `plugplay.azurewebsites.net` | N/A (none established) | `./families/NodeRabbit/stix_bundle.json` |
| **PollCat** | Obfuscated JavaScript RAT (Mirage Kitten co-disclosure) | `sahi-finance.com` | N/A (none established) | `./families/PollCat/stix_bundle.json` |
| **SynkLoader** | Teams phishing modular loader | `https://filereserve.blob.core.windows.net/vgnghuyk/331/331.msi` | N/A (none established) | `./families/SynkLoader/stix_bundle.json` |
| **Showboat** | Linux modular post-exploitation / telecom targeting | `139.84.227.139, 194.135.25.132, 101.36.105.222` | N/A (none established) | `./families/Showboat/stix_bundle.json` |

### Indicator inventory (this build)

| Family | IPs | Domains/URLs | Hashes |
|--------|----:|-------------:|-------:|
| Rapuncel | 6 | 15 | 9 |
| Settra | 2 | 9 | 0 |
| RatHat | 0 | 35 | 1 |
| NodeRabbit | 0 | 28 | 13 |
| PollCat | 0 | 9 | 1 |
| SynkLoader | 4 | 11 | 11 |
| Showboat | 14 | 5 | 3 |

## Directory map

```
CTI-Evidence-Repository/
├── README.md                 ← this cover sheet
├── TLP-LICENSE.md
├── CHECKSUMS.sha256
├── schemas/
└── families/<Family>/
    ├── SUMMARY.md
    ├── stix_bundle.json
    ├── iocs/{ips,domains,hashes}.csv
    ├── network_captures/     ← lab PCAPs (placeholder)
    ├── memory_dumps/         ← configs/dumps (placeholder)
    ├── rules/{yara.yar,sigma.yml}
    └── actors_and_finance/
```

## Point of Contact

For law enforcement inquiries, raw unredacted `.pcap` files (when available), or encrypted GPG communication:

| Field | Value |
|-------|-------|
| Project | Emerging Threat Watch |
| GitHub tips | See parent `docs/SUBMIT_INTEL.md` |
| Contact name | _[TO BE FILLED]_ |
| Email / Signal | _[TO BE FILLED]_ |
| PGP fingerprint | _[TO BE FILLED]_ |
| Related IC3 / FBI tip numbers | See `../MASTER_INDEX.csv` |

## Related parent-repo paths

- Narrative IC3/FBI packages: `../packages/`
- Comprehensive private dossier: `../SUBMISSION_REPORT.md` (gitignored)
- Takedown template: `../TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`
- Methodology: `../../../shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`
- Enforcement readiness: `../../../docs/ENFORCEMENT_READINESS.md`

## Rebuild

```bash
python shared/tooling/build_cti_evidence_repository.py
```

Generated: 2026-09-19T19:25:39Z
