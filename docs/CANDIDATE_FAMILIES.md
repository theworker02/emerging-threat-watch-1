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
| SharkLoader | Kaspersky June 2026 | Custom loader → Cobalt Strike | **ADDED / FILED_IC3** `6ed57963d0c64750aa14b6fcbaa2e576` (2026-09-19 10:43:18 PM EST) |
| TencShell | Cato CTRL 2026 | Go implant; Rshell OSS lineage problem | **ADDED / PRIMARY_FROZEN** (15 TEN-IND; Cato CTRL) |
| MiniFast | Check Point May 2026 | Nimbus Manticore; Zoom installer trust abuse | **ADDED / PRIMARY_FROZEN** (30 MNF-IND; do not merge with PollCat) |
| Argamal | Kaspersky June 2026 | Trojanized adult games RAT | **ADDED / PRIMARY_FROZEN** (22 ARG-IND; Securelist 2026-06-03) |
| (unnamed) torrent campaign | Kaspersky Sept 17 2026 | Compromised torrents / film lures; mid-Aug start | CANDIDATE |
| Okobot/OkoSpyware | Kaspersky | 20+ payloads; 25+ countries; Jan 2026 investigation start | **ADDED / PRIMARY_FROZEN** (30 OKO-IND; Securelist) |
| Matanbuchus & AstarionRAT | Huntress / Zscaler; BelialDemon XSS/Exploit | MaaS loader+RAT; Teams/ClickFix; ChaCha20 — **technique comparator** for SynkLoader only | **ADDED / PRIMARY_FROZEN** (15 MAT-IND; comparator only — do not file jointly) |
| Starland RAT & WLDR Agent | Cisco Talos UAT-11795 | Python RAT / PS implant; Telegram + Polygon contract C2 fallback | **ADDED / PRIMARY_FROZEN** (17 STR-IND; Talos) |
| RedLine / Vidar / Lumma Stealer | Multiple (Russian MaaS markets) | Commodity stealers; ransomware IA; TimeWeb/REG.RU panel context — **market comparator** for Rapuncel only | CANDIDATE |
| Pikabot & QakBot variants | Multiple (BlackBasta/Akira IA) | Initial-access loaders; CIS language checks; ClickFix-class paste/exec — **technique comparator** for SynkLoader delivery | CANDIDATE |

Machine-readable: [`intelligence/candidate-families.csv`](../intelligence/candidate-families.csv).

**Technique comparators (COMMON TECHNIQUE only; `authorship_link=NOT_ESTABLISHED`):** [`docs/TECHNIQUE_COMPARATORS.md`](TECHNIQUE_COMPARATORS.md) · [`intelligence/technique-comparators.csv`](../intelligence/technique-comparators.csv).

Do **not** claim Matanbuchus / Lumma / Pikabot / etc. are SynkLoader or Rapuncel lineage without primary evidence.

## Promotion rule

Promote a candidate only after: primary URL freeze, case-isolation ID prefixes assigned, and a human decision to open `investigations/<family>/`. Do **not** merge IC3 packages across families.

## Underground / tracker OSINT

Commodity RAT marketplace and tracker collection methodology (defensive only): [shared/methodology/UNDERGROUND_AND_COMMODITY_RAT_OSINT.md](../shared/methodology/UNDERGROUND_AND_COMMODITY_RAT_OSINT.md). Tracker query seeds: [shared/queries/tracker_collection_seeds.csv](../shared/queries/tracker_collection_seeds.csv). Bound by [AUTONOMOUS_COLLECTION_POLICY.md](../shared/methodology/AUTONOMOUS_COLLECTION_POLICY.md).


## Sparse-corpus expansion (2026-09-21)

Packages are numbered independently of nationality. **Attribution is metadata** (`investigations/*/docs/attribution.md` and `packages/*/attribution.csv`).

### Packages 16–30 (priority young-corpus leads)

| Pkg | Family | Status |
|-----|--------|--------|
| 16 | CountLoader | PRIMARY_FROZEN (Silent Push) |
| 17 | MAYBEROBOT | PRIMARY_FROZEN (Google GTIG) |
| 18 | NOROBOT | PRIMARY_FROZEN (Google GTIG) |
| 19 | YESROBOT | PRIMARY_FROZEN (lineage vs MAYBEROBOT) |
| 20 | Tsundere Bot | PRIMARY_FROZEN (Proofpoint) |
| 21 | MonsterV2 | PRIMARY_FROZEN (Proofpoint; IOC harvest OPEN) |
| 22 | PhantomHeart | PRIMARY_FROZEN (Kaspersky RU) |
| 23 | ABCDoor | PRIMARY_FROZEN (Kaspersky) |
| 24 | MiniUpdate | PRIMARY_FROZEN (Unit 42; not merged with MiniFast) |
| 25 | MiniJunk V2 | PRIMARY_FROZEN (Unit 42) |
| 26 | HEAVYGRAM | PRIMARY_FROZEN (FBI FLASH PDF) |
| 27 | CHOSEN BRICK | PRIMARY_FROZEN (NCSC); contested alias vs HEAVYGRAM — separate |
| 28 | PromptSpy | PRIMARY_FROZEN (ESET) |
| 29 | GhostChat | PRIMARY_FROZEN (ESET) |
| 30 | HybridPetya | PRIMARY_FROZEN (ESET) |

### Packages 31–42

Prior deep-research freezes (MovieReaper, Insomnia RAT, ARKTunnel, Docro, OfferLoader, GenieLocker, DenoRAT, MLTBackdoor, C2Looper, SmartRAT, PAPERMILL, kkRAT).

### Packages 43–66 (additional sparse leads)

| Pkg | Family | Notes |
|-----|--------|-------|
| 43 | Foxveil | Cato PRIMARY WAF-blocked; SOCPrime SECONDARY freeze |
| 44 | PhantomPyramid | PRIMARY_FROZEN (Kaspersky Securelist RU) |
| 45 | GhostContainer | Kaspersky Exchange backdoor |
| 46 | Dohdoor | Talos UAT-10027 DoH C2 |
| 47–48 | LaxGopher / FriendDelivery | ESET GopherWhisper |
| 49–50 | NosyDoor / NosyHistorian | ESET LongNosedGoblin |
| 51–53 | TernDoor / PeerTime / BruteEntry | Talos UAT-9244 |
| 54–56 | SILENCELIFT / DEEPBREATH / CHROMEPUSH | PRIMARY_FROZEN (Mandiant / Google Cloud UNC1069) |
| 57–59 | NightLedger / ArcBridge / BridgeHead | Mirage Kitten; isolated from NodeRabbit/PollCat |
| 60–61 | Fooder / MuddyViper | ESET MuddyWater |
| 62 | MiniBrowse | Unit 42 Screening Serpens context |
| 63–66 | ZeronetKit / PaperGrabber / PowerLoader / Atlas RAT | PRIMARY_FROZEN (Kaspersky / BI.ZONE / Proofpoint) |

**Argamal** remains package `12-argamal` (already PRIMARY_FROZEN) — not duplicated as 40.


### IOC / WHOIS enrichment (2026-09-21)

Non-redundant harvest from frozen primaries + vendor GitHub IoC corpora; passive RDAP/WHOIS in [`intelligence/infra-ownership.csv`](../intelligence/infra-ownership.csv). Findings summary: [`intelligence/INFRA_OWNERSHIP_FINDINGS.md`](../intelligence/INFRA_OWNERSHIP_FINDINGS.md). Gap families upgraded to PRIMARY_FROZEN (2026-09-21): PhantomPyramid, ZeronetKit, PaperGrabber, PowerLoader, Atlas RAT, UNC1069 trio.

### South Asia branch (follow-on)

APT36 / Transparent Tribe tooling evolution (Linux `.desktop` delivery; Go Poseidon-class backdoors when PRIMARY confirms) tracked as future package after dedicated PRIMARY freeze — do not invent Poseidon IOCs from older PoSeidon POS malware.

Machine-readable: [`intelligence/candidate-families.csv`](../intelligence/candidate-families.csv).
