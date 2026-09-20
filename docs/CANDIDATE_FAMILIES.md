# Candidate Families Pipeline

Emerging Threat Watch tracks **active investigation packages** separately from a **candidate pipeline**. Candidates are **not** full investigation trees until promoted.

## Strategic note

One-report / obscure families are high-value for autonomous CT / pDNS / archive collection that can produce **original defensive intelligence**. Mandiant publicly discussed discovering **714 new malware families in 2025** — cited here as **motivation for prioritizing sparse-corpus families**, not as a claim Emerging Threat Watch independently verified.

## Pipeline

| Family | First/major disclosure | Why it fits | Priority |
|--------|------------------------|-------------|----------|
| PollCat | Kaspersky Sept 2026 | JS RAT; co-disclosed with NodeRabbit; extremely sparse corpus | **ADDED** |
| SynkLoader | Expel Aug 2026 | Modular mixed-language loader; Teams/IT-helpdesk enterprise intrusion | **ADDED** |
| Showboat | Lumen BLL 2026 | Linux modular post-ex; telecoms; possible activity ≥2022 | **ADDED** |
| Abyssos | Zscaler Aug 2026 | Modular RAT; young corpus | **ADDED / FILED_IC3** `a23f0a9d6799480e994284416d354713` (2026-09-19 10:20:50 PM EST) |
| SharkLoader | Kaspersky June 2026 | Custom loader → Cobalt Strike | CANDIDATE |
| TencShell | Cato CTRL 2026 | Go implant; Rshell OSS lineage problem | CANDIDATE |
| MiniFast | Check Point May 2026 | Nimbus Manticore; Zoom installer trust abuse | CANDIDATE |
| Argamal | Kaspersky June 2026 | Trojanized adult games RAT | CANDIDATE |
| (unnamed) torrent campaign | Kaspersky Sept 17 2026 | Compromised torrents / film lures; mid-Aug start | CANDIDATE |
| Okobot/OkoSpyware | Kaspersky | 20+ payloads; 25+ countries; Jan 2026 investigation start | CANDIDATE |
| Matanbuchus & AstarionRAT | Elastic/Checkpoint/community; BelialDemon XSS/Exploit | MaaS loader+RAT; Teams/ClickFix; ChaCha20 — **technique comparator** for SynkLoader only | CANDIDATE |
| Starland RAT & WLDR Agent | Cisco Talos UAT-11795 / vendors | Python RAT / PS implant; Telegram + Polygon contract C2 fallback | CANDIDATE |
| RedLine / Vidar / Lumma Stealer | Multiple (Russian MaaS markets) | Commodity stealers; ransomware IA; TimeWeb/REG.RU panel context — **market comparator** for Rapuncel only | CANDIDATE |
| Pikabot & QakBot variants | Multiple (BlackBasta/Akira IA) | Initial-access loaders; CIS language checks; ClickFix-class paste/exec — **technique comparator** for SynkLoader delivery | CANDIDATE |

Machine-readable: [`intelligence/candidate-families.csv`](../intelligence/candidate-families.csv).

**Technique comparators (COMMON TECHNIQUE only; `authorship_link=NOT_ESTABLISHED`):** [`docs/TECHNIQUE_COMPARATORS.md`](TECHNIQUE_COMPARATORS.md) · [`intelligence/technique-comparators.csv`](../intelligence/technique-comparators.csv).

Do **not** claim Matanbuchus / Lumma / Pikabot / etc. are SynkLoader or Rapuncel lineage without primary evidence.

## Promotion rule

Promote a candidate only after: primary URL freeze, case-isolation ID prefixes assigned, and a human decision to open `investigations/<family>/`. Do **not** merge IC3 packages across families.

## Underground / tracker OSINT

Commodity RAT marketplace and tracker collection methodology (defensive only): [shared/methodology/UNDERGROUND_AND_COMMODITY_RAT_OSINT.md](../shared/methodology/UNDERGROUND_AND_COMMODITY_RAT_OSINT.md). Tracker query seeds: [shared/queries/tracker_collection_seeds.csv](../shared/queries/tracker_collection_seeds.csv). Bound by [AUTONOMOUS_COLLECTION_POLICY.md](../shared/methodology/AUTONOMOUS_COLLECTION_POLICY.md).
