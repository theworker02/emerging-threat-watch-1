<p align="center">
  <img src="assets/etw-logo.svg" alt="Emerging Threat Watch official logo" width="280"/>
</p>

<h1 align="center">Emerging Threat Watch</h1>

<p align="center">
  <strong>Independent, evidence-driven threat intelligence for emerging malware families</strong><br/>
  Defensive research only Â· Case-isolated packages Â· Law-enforcement and industry handoff
</p>

<p align="center">
  <a href="https://github.com/theworker02/emerging-threat-watch-1"><img alt="Repository" src="https://img.shields.io/badge/repo-emerging--threat--watch--1-22D3EE?style=flat-square&logo=github&logoColor=white"/></a>
  <img alt="Families" src="https://img.shields.io/badge/families-66-3B82F6?style=flat-square"/>
  <img alt="IC3 filed" src="https://img.shields.io/badge/IC3%20filed-9%20packages-10B981?style=flat-square"/>
  <img alt="Scope" src="https://img.shields.io/badge/scope-defensive%20CTI%20only-0EA5E9?style=flat-square"/>
</p>

---

## Start here

| Audience | Go to |
|----------|--------|
| **Law enforcement / IC3 investigators** | [`reports/law-enforcement/README.md`](reports/law-enforcement/README.md) Â· [`MASTER_INDEX.csv`](reports/law-enforcement/MASTER_INDEX.csv) |
| **Cybersecurity vendors / CERT / CTI teams** | [`reports/INDEX.md`](reports/INDEX.md) Â· [`intelligence/combined_iocs.csv`](intelligence/combined_iocs.csv) Â· [`RESPONSIBLE_SUBMISSION/`](reports/law-enforcement/RESPONSIBLE_SUBMISSION/) |
| **Full corpus map** | [`reports/INDEX.md`](reports/INDEX.md) |
| **ATT&CK / landscape** | [`reports/landscape/ATTACK_CORPUS_MAP.md`](reports/landscape/ATTACK_CORPUS_MAP.md) Â· [`EVIDENCE_COMPLETENESS.md`](reports/landscape/EVIDENCE_COMPLETENESS.md) |

---

## Mission

**Emerging Threat Watch (ETW)** produces reproducible, provenance-graded investigation packages for emerging malware families. Each family is an **independent case**: indicators, attribution, and infrastructure conclusions are never transferred across cases without **direct connecting evidence**.

Priorities:

- Evidence before narrative â€” claims are ledgered with source class and confidence
- Passive collection by default â€” no malware execution or C2 contact during research
- Defender and LE utility â€” summaries, IOC CSVs, ATT&CK maps, STIX where available
- Honest uncertainty â€” explicit non-authorship defaults when techniques overlap

---

## What this repository is (and is not)

| This repository **is** | This repository **is not** |
|------------------------|----------------------------|
| Defensive CTI research packages | A malware sample archive |
| Claim ledgers, sources, IOC corpora | Live C2 monitoring or tasking |
| Independent family case files | A merged â€œmega-campaignâ€ attribution dump |
| Structured LE packages for human review | Automated law-enforcement filing |

> **Hard boundary:** This repository must never contain functionality intended to improve, weaponize, deploy, propagate, conceal, or operationalize malware.

See [`DISCLAIMER.md`](DISCLAIMER.md) and [`SECURITY.md`](SECURITY.md).

---

## Family corpus (15 packages)

| # | Family | Case ID | Status | Package |
|---|--------|---------|--------|---------|
| 01 | Rapuncel | `ETW-RAP-IC3` | `FILED_IC3` | [`packages/01-rapuncel`](reports/law-enforcement/packages/01-rapuncel/) |
| 02 | Settra | `ETW-SET-IC3` | `FILED_IC3` | [`packages/02-settra`](reports/law-enforcement/packages/02-settra/) |
| 03 | RatHat | `ETW-RAT-IC3` | `FILED_IC3` | [`packages/03-rathat`](reports/law-enforcement/packages/03-rathat/) |
| 04 | NodeRabbit | `ETW-NRB-IC3` | `FILED_IC3` | [`packages/04-noderabbit`](reports/law-enforcement/packages/04-noderabbit/) |
| 05 | PollCat | `ETW-POL-IC3` | `FILED_IC3` | [`packages/05-pollcat`](reports/law-enforcement/packages/05-pollcat/) |
| 06 | SynkLoader | `ETW-SYN-IC3` | `FILED_IC3` | [`packages/06-synkloader`](reports/law-enforcement/packages/06-synkloader/) |
| 07 | Showboat | `ETW-SHO-IC3` | `FILED_IC3` | [`packages/07-showboat`](reports/law-enforcement/packages/07-showboat/) |
| 08 | Abyssos | `ETW-ABY-IC3` | `FILED_IC3` | [`packages/08-abyssos`](reports/law-enforcement/packages/08-abyssos/) |
| 09 | SharkLoader | `ETW-SHK-IC3` | `FILED_IC3` | [`packages/09-sharkloader`](reports/law-enforcement/packages/09-sharkloader/) |
| 10 | TencShell | `ETW-TEN-IC3` | `PRIMARY_FROZEN` | [`packages/10-tencshell`](reports/law-enforcement/packages/10-tencshell/) |
| 11 | MiniFast | `ETW-MNF-IC3` | `PRIMARY_FROZEN` | [`packages/11-minifast`](reports/law-enforcement/packages/11-minifast/) |
| 12 | Argamal | `ETW-ARG-IC3` | `PRIMARY_FROZEN` | [`packages/12-argamal`](reports/law-enforcement/packages/12-argamal/) |
| 13 | Okobot | `ETW-OKO-IC3` | `PRIMARY_FROZEN` | [`packages/13-okobot`](reports/law-enforcement/packages/13-okobot/) |
| 14 | Matanbuchus | `ETW-MAT-IC3` | `PRIMARY_FROZEN` (comparator) | [`packages/14-matanbuchus`](reports/law-enforcement/packages/14-matanbuchus/) |
| 15 | StarlandRAT | `ETW-STR-IC3` | `PRIMARY_FROZEN` | [`packages/15-starlandrat`](reports/law-enforcement/packages/15-starlandrat/) |

**Case isolation (mandatory):** MiniFast â‰  PollCat. Matanbuchus â‰  SynkLoader (technique comparator only). NodeRabbit â‰  PollCat. NightLedger/ArcBridge/BridgeHead â‰  NodeRabbit/PollCat. MiniUpdate/MiniJunk/MiniBrowse â‰  MiniFast.

### Sparse-corpus expansion (packages 16â€“66)

- **16â€“30:** CountLoader, MAYBEROBOT/NOROBOT/YESROBOT, Tsundere, MonsterV2, PhantomHeart, ABCDoor, MiniUpdate/MiniJunk V2, HEAVYGRAM, CHOSEN BRICK, PromptSpy, GhostChat, HybridPetya
- **31â€“42:** MovieReaper â€¦ kkRAT (prior deep-research freezes)
- **43â€“66:** Foxveil â†’ Atlas RAT (GhostContainer, Dohdoor, GopherWhisper, LongNosedGoblin, UAT-9244, UNC1069, Mirage Kitten, MuddyWater, MiniBrowse, plus CANDIDATE stubs)
- Network IOC + passive WHOIS enrichment: [`intelligence/infra-ownership.csv`](intelligence/infra-ownership.csv) Â· [`INFRA_OWNERSHIP_FINDINGS.md`](intelligence/INFRA_OWNERSHIP_FINDINGS.md)
- Attribution is metadata only (`attribution.csv`) â€” not nationality-based folders. Catalog: [`docs/CANDIDATE_FAMILIES.md`](docs/CANDIDATE_FAMILIES.md) Â· [`intelligence/candidate-families.csv`](intelligence/candidate-families.csv)

---

## Repository layout

```
reports/law-enforcement/packages/   Investigator packages (02â€“05 core + filing records)
reports/law-enforcement/CTI-Evidence-Repository/   STIX / CSV LE ingest tree
reports/landscape/                  Cross-family ATT&CK and evidence completeness
investigations/<family>/            Analyst evidence workspace
intelligence/                       Combined IOC and ATT&CK rollups (canonical CSVs)
docs/                               Methodology catalogs and enforcement readiness
```

Each public LE package contains:

| File | Purpose |
|------|---------|
| `02_FBI_SUMMARY.md` | Investigator-facing summary |
| `03_INDICATORS.csv` | PRIMARY-SOURCE indicators |
| `04_SOURCES.md` | Primary research URLs |
| `05_CAVEATS_AND_LIMITS.md` | Explicit non-claims |
| `IC3_FULL_PACKAGE.md` | Structured complaint narrative / dossier |
| `IC3_FILING_RECORD.md` | Present when an IC3 submission is recorded |

---

## Contribute intelligence

External tips: [`docs/SUBMIT_INTEL.md`](docs/SUBMIT_INTEL.md). Prefer PRIMARY public research with clear provenance. Do not submit malware binaries to this repository.

---

## Governance

| Document | Role |
|----------|------|
| [`METHODOLOGY.md`](METHODOLOGY.md) | Research methodology |
| [`DISCLAIMER.md`](DISCLAIMER.md) | Scope and liability |
| [`SECURITY.md`](SECURITY.md) | Security handling |
| [`LICENSE`](LICENSE) | Proprietary commercial license (all rights reserved) |
| [`ACQUISITION_NOTICE.md`](ACQUISITION_NOTICE.md) | Acquisition notice and Acquirer enforcement warning |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Contribution guidance |

**License:** **Proprietary / commercial** â€” see [`LICENSE`](LICENSE), [`LICENSE_TRANSITION_NOTICE.md`](LICENSE_TRANSITION_NOTICE.md), and [`ACQUISITION_NOTICE.md`](ACQUISITION_NOTICE.md). Not open source. Historical MIT snapshots remain under MIT for those copies where applicable; current contents are proprietary. Commercial use requires a written license. Research cutoff for Phase 1 freezes: **2026-09-19** unless a package notes otherwise.


---

## License & acquisition

This project is **proprietary**. Production use, redistribution, and commercial deployment require a written commercial license or completed acquisition. See [LICENSE](./LICENSE) and [ACQUISITION.md](./ACQUISITION.md). Contact [@theworker02](https://github.com/theworker02).
