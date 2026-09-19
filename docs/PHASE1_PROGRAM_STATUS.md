# Phase 1 Program Status — Emerging Threat Watch

**Research cutoff (v1 freeze):** 2026-09-19  
**Status file updated (UTC):** 2026-09-19T20:15:00Z  
**PDF threat reports:** NOT DONE (deferred)  
**Active families:** **7** (Rapuncel, Settra, RatHat, NodeRabbit, **PollCat**, **SynkLoader**, **Showboat**)

## Expansion note (2026-09-19)

Three new independent investigation package stubs were opened:

| Family | Case | Primary URL | Primary artifact |
|--------|------|-------------|------------------|
| PollCat | POL / `ETW-POL-IC3` | https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/ | **Dual-ref** `PS-POL-001` ≡ `PS-NRB-001` bytes under `evidence/primary-sources/noderabbit/` — dual-list; **do not merge cases** |
| SynkLoader | SYN / `ETW-SYN-IC3` | https://expel.com/blog/synkloader-when-you-throw-in-everything-but-the-kitchen-sink/ | URL frozen; local HTML TBD |
| Showboat | SHO / `ETW-SHO-IC3` | https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms | URL frozen; local HTML TBD |

Candidate pipeline (not full trees): `docs/CANDIDATE_FAMILIES.md`, `intelligence/candidate-families.csv`. Technique comparators (COMMON TECHNIQUE; authorship NOT_ESTABLISHED): `docs/TECHNIQUE_COMPARATORS.md`, `intelligence/technique-comparators.csv`.

## URL fetch status (this build)

| URL | Role | Result |
|-----|------|--------|
| https://blog.lastpass.com/posts/lastpass-delphos-report-rapuncel-infostealer | SOURCE-RAP-001 primary | **403 Forbidden** (UA retry also 403) |
| https://www.pk-sharma.com/briefing/fake-lastpass-github-rapuncel-domains-still-resolve | Independent DNS/GitHub observation | **Fetched** |
| https://www.trendmicro.com/it_it/research/26/c/boryptgrab-stealer-targets-users-via-deceptive-github-pages.html | BoryptGrab comparator primary | **Fetched** |
| https://www.esentire.com/blog/malware-as-a-service-cocktail-errtraffic-and-cruciferra-killing-your-edr-since-2025 | Cruciferra | **Fetched** (200) |
| https://www.proofpoint.com/us/blog/threat-insight/unpacking-cruciferra-analysis-sophisticated-crypter-service | Cruciferra | **Fetched** (200) |
| https://www.recordedfuture.com/research/malware-crypting-services-threat-actors | Crypting marketplace | **Fetched** (200) |
| https://www.cynet.com/blog/inside-cynets-settra-ransomware-investigation/ | Settra primary | **Fetched** (prior) |
| https://www.cynet.com/settra-ransomware-inside-a-new-enterprise-grade-extortion-threat/ | Settra primary long-form | **Fetched** (prior) |
| https://www.huntress.com/blog/new-settra-ransomware-variant | Settra IR primary | **Fetched** (prior) |
| https://www.moxfive.com/blog/settra-ransomware-ttps-victims-and-defense-guide | Settra operator TTPs | **Fetched** |
| https://zimperium.com/blog/rathat-ai-powered-mobile-threat-is-here-for-your-credentials-bank-accounts | RatHat primary | **Fetched** (prior) |
| https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/ | NodeRabbit + PollCat primary | **Fetched** (prior; dual-listed `PS-NRB-001` / `PS-POL-001`) |
| https://expel.com/blog/synkloader-when-you-throw-in-everything-but-the-kitchen-sink/ | SynkLoader primary | **URL frozen** (HTML archive pending) |
| https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms | Showboat primary | **URL frozen** (HTML archive pending) |
| https://github.com/Zimperium/IOC/tree/master/2026-09-RatHat | RatHat IOC metadata | **Fetched** (API + CSV metadata; no APK download) |
| Sophos VM hostname literature (WIN-LIVFRVQFMKO) | Hostname mystery | **Search/snippet** (not full local archive) |
| Zimperium ToxicPanda / Group-IB RedHook | ADB technique comparison only | **Search + partial fetch** |

## Claim corpus counts (validated)

| Family | Claims | Notes |
|--------|--------|-------|
| Rapuncel | **34** | Cruciferra track, DNS observation lineage, UNVERIFIED seed hashes |
| Settra | **15** | Dual ATT&CK framing; operator-model H5 default |
| RatHat | **17** | +5 shell/path/IOC-repo claims this Linux pass (`RAT-CLAIM-0013`–`0017`) |
| NodeRabbit | **19** | +8 Linux/WSL/account-discovery claims (`NRB-CLAIM-0012`–`0019`) |
| PollCat | **8** | Seeded from Securelist PollCat section; non-authorship default vs NodeRabbit |
| SynkLoader | **3** | Thin seed pending Expel HTML freeze |
| Showboat | **3** | Thin seed pending Lumen HTML freeze; dating gap noted |
| **Total** | **99** | Prior 85 + 14 new stub claims |

### Claim delta this Linux / shell-context pass

| Family | Before | After | Delta |
|--------|--------|-------|-------|
| NodeRabbit | 11 | 19 | **+8** |
| RatHat | 12 | 17 | **+5** |
| Settra | 15 | 15 | 0 (negative search only) |
| Rapuncel | 34 | 34 | 0 (negative search only) |
| **Total** | **72** | **85** | **+13** |

### Claim delta — family expansion stubs (2026-09-19)

| Family | Claims added |
|--------|--------------|
| PollCat | +8 |
| SynkLoader | +3 |
| Showboat | +3 |
| **Expansion subtotal** | **+14** |

## Unix / Linux / shell-context pass (2026-09-19)

Executive disposition ingested as evidence (not speculation):

| Family | Literal whoami in primary? | Linux/Unix research value | Assessment |
|--------|---------------------------|---------------------------|------------|
| NodeRabbit | No | Very high | Native Win/Linux/macOS; Linux persistence all 3 variants + WSL in V3 |
| RatHat | No | High | Android ADB shell + `/data/local/tmp` + `/dev/input` — **not** “Linux malware” |
| Settra | No | Low | Windows enterprise ransomware — `SEARCH-SET-LINUX-001` **NEGATIVE SEARCH RESULT** |
| Rapuncel | No defensible hit | Low presently | Windows-oriented chain — `SEARCH-RAP-LINUX-001` **NEGATIVE SEARCH RESULT** |

Artifacts:

- `intelligence/unix-search-ledger.csv` (+ family `evidence/unix-search-ledger.csv` copies)
- `intelligence/linux-artifact-matrix.csv`
- `investigations/noderabbit/analysis/linux-artifact-matrix.csv`
- `investigations/noderabbit/docs/linux-unix-track.md`
- `investigations/noderabbit/detections/hunting/linux-node-persistence.md` (**EXPERIMENTAL/UNVALIDATED**)
- `investigations/noderabbit/docs/shepherd-persist-detection-catalog.md`
- `investigations/rathat/docs/adb-shell-linux-interfaces.md`
- RatHat IOC metadata: `iocs/domains.csv`, `urls.csv`, `hashes-zimperium-ioc.csv` (162 SHA-256, **UNVERIFIED**)
- Methodology: `shared/methodology/UNIX_LINUX_HUNTING.md` + `METHODOLOGY.md` addendum

## Evidence / IOC snapshot

| Family | Notable artifacts |
|--------|-------------------|
| Rapuncel | research-tracks, driver-trust-chain, Cruciferra NOTES; negative Linux search |
| Settra | Dual ATT&CK CSVs; operator-model hypotheses; win-livfrvqfmko; negative Linux search |
| RatHat | persistence taxonomy; browser-target-matrix; ADB comparison; **adb-shell-linux-interfaces**; Zimperium IOC metadata |
| NodeRabbit | variant-evolution; VS Code; Git hooks; **linux-unix-track**; Linux hunting hypothesis |
| PollCat | Securelist dual-ref; 8 PRIMARY-SOURCE claims; published-indicators header-only |
| SynkLoader | Expel URL frozen; 3 claims; published-indicators header-only |
| Showboat | Lumen URL frozen; 3 claims; dating gap ≥2022 vs 2026 disclosure |

## Independently corroborated by ETW (OBSERVED)

**None** at host/malware level. Passive-source document retrieval only. pk-sharma DNS/GitHub checks are **author-observed**, recorded as independent corroboration lineage — **not** re-executed by ETW this session. Zimperium IOC hashes/domains listed but **not** passively re-validated beyond repo fetch.

## Unresolved / contradictions

- SOURCE-RAP-001 body unreachable (403) — claim text depends on attributed reconstructions  
- User-seed Rapuncel hashes UNVERIFIED until seen in primary  
- Secondary “39 other companies” vs primary “40 other lure pages / forty companies” brand-count drift  
- BoryptGrab “variant” vs “sibling” — OPEN  
- Settra Defender log name typo (Huntress) vs intended clear list  
- Cruciferra pricing figures disagree across RF vs other writeups — do not merge  
- WIN-LIVFRVQFMKO: **UNKNOWN** / not Settra-exclusive (multi-campaign reuse)  
- RatHat Zimperium IOC rows: **UNVERIFIED** pending passive DNS/hash checks  
- PollCat↔NodeRabbit relationship class: **OPEN** (non-authorship default)  
- SynkLoader / Showboat local HTML archives: **PENDING**  

## Open hypotheses (key)

| ID | Statement | Default |
|----|-----------|---------|
| RAP-H-CRY | Loader/evasion = Cruciferra commodity vs Rapuncel-authored? | OPEN |
| SET-H1..H4 | RaaS / small team / brokers / inflated leak volume | OPEN |
| SET-H5 | Insufficient evidence for operator model | **DEFAULT** |
| WIN-LIVFRVQFMKO | Operator vs shared VM template vs coincidence | **UNKNOWN** |
| RatHat AI | What is GenAI-delegated vs deterministic Accessibility? | OPEN |
| NRB enterprise | Built for corp developer proxy environments? | OPEN (motivated) |
| ADB pattern | Self-pair reusable design pattern across Android malware? | Likely technique-class YES; lineage NO |
| NRB-Linux-hunt | Node + fake edge-update/intel-dsa/`~/.local/share` + @reboot | **EXPERIMENTAL/UNVALIDATED** |
| POL-NRB-REL | Parallel / generation / specialized / co-deployed only? | **OPEN; non-authorship default** |

## Trust-surface program layer

- Matrix: `research/trust-surface-matrix.csv` (+ copy under `intelligence/`) — **completed**  
- Outline: `reports/_landscape/TRUST_SURFACE_PROBLEM_OUTLINE.md` — **completed (outline only; PDF deferred)**  
- Cross-family technique comparison allowed **only** as trust-surface / COMMON TECHNIQUE — no authorship claims  
- PollCat↔NodeRabbit comparison is a **P1** COMMON TECHNIQUE / lineage workstream — still no IOC transfer  

## Safety limitations

No malware execution; no C2 interaction; no attacker-infra auth; no live samples in repo; DNS≠malicious; case isolation except explicit technique comparison (ADB / BYOVD class / trust surfaces). RatHat APKs from IOC repo **not downloaded**. Do not describe Settra as RaaS without evidence. Do not claim NodeRabbit≡PollCat operators/authors.

## Phase 2 recommendations

1. **Rapuncel:** Obtain SOURCE-RAP-001; bind hashes; passive DNS/CT; deepen Cruciferra feature↔chain mapping; driver signer hunts  
2. **Settra:** Keep dual matrices; passive MeshAgent infra; do not overfit hostname; validate leak-site methodology separately  
3. **RatHat:** Passive-check Zimperium IOC domains; test AI-vs-deterministic question on samples in isolated lab only  
4. **NodeRabbit:** Validate Linux Node+cron hunting hypothesis; behavioral detections for sdk/v2 + VS Code + shepherd-persist; passive Azure domain status  
5. **PollCat:** Transcribe POL-IND from Securelist; P1 lineage comparison vs NodeRabbit; sparse-corpus CT/pDNS  
6. **SynkLoader:** Archive Expel HTML; seed SYN-IND; Teams/PhishLocker detection hypotheses (UNVALIDATED)  
7. **Showboat:** Archive Lumen HTML; document dating gap; Linux telecom hunting  
8. **Landscape:** Expand trust-surface report from outline — still no PDF until content-complete  

## Executive research pass (2026-09-19T18:07:48Z) — ingested as new evidence

Seed corpus treated as **PRIMARY-SOURCE structured evidence**, not OBSERVED infrastructure.

| Artifact | Path | Count / note |
|----------|------|--------------|
| Published indicators | `investigations/*/evidence/published-indicators.csv` | RAP 30 / SET 14 / RAT 17 / NRB 28; POL/SYN/SHO header-only |
| Combined IOC index | `shared/combined_iocs.csv` (+ `intelligence/`) | **89** rows; none `OBSERVED` |
| ID policy | `shared/methodology/EVIDENCE_ID_POLICY.md` | Seed `*-EV-*` → ETW `*-IND-*`; POL/SYN/SHO prefixes added |
| Candidate pipeline | `docs/CANDIDATE_FAMILIES.md` | 3 ADDED + 12 CANDIDATE (incl. Matanbuchus/AstarionRAT, Starland/WLDR, RedLine/Vidar/Lumma, Pikabot/QakBot) |
| Technique comparators | `docs/TECHNIQUE_COMPARATORS.md` + `intelligence/technique-comparators.csv` | 3 rows; all `authorship_link=NOT_ESTABLISHED` |
| Lineage | `shared/lineage/lineage_comparison.csv` | 8 comparison rows |
| Priority gaps | `intelligence/priority-gaps.csv` | 12 OPEN/PARTIAL/IN_PROGRESS |
| CT / pDNS / GitHub / Wayback seeds | `shared/queries/` | CT/pDNS result templates empty until passive retrieval |
| Vendor ASN context | `shared/queries/vendor_reported_dns_asn.csv` | UNVERIFIED vendor-reported only |
| Source corpus | `shared/source_corpus.jsonl` | 11 primary/role sources |
| Mermaid chains | `shared/diagrams/infection-chains.md` | 4 family chains |
| IC3 paste-ready cores | `reports/*/ *_IC3_BRIEF.md` | Source-attributed; no independent discovery claims |
| **FBI / IC3 filing packages** | `reports/law-enforcement/` | Canonical handoff: 4 separate packages + HOW_TO_FILE + checklist + MASTER_INDEX |
| Research plan | `research_plan.md` | P0→P2 collection sequence locked |

**Fix applied this pass:** NRB-IND-0012..0028 domain rows had shifted CSV columns (family missing); rewritten and combined IOCs rebuilt.

## Law-enforcement organization (FBI / IC3)

Canonical path: `reports/law-enforcement/`

| Package | ID | Folder |
|---------|-----|--------|
| Rapuncel | ETW-RAP-IC3 | `packages/01-rapuncel/` |
| Settra | ETW-SET-IC3 | `packages/02-settra/` |
| RatHat | ETW-RAT-IC3 | `packages/03-rathat/` |
| NodeRabbit | ETW-NRB-IC3 | `packages/04-noderabbit/` |

Each package contains numbered files `00`–`06` (cover, IC3 narrative paste, FBI summary, indicators CSV, sources, caveats, evidence retained). Rebuild with `python shared/tooling/build_le_packages.py`. **Do not merge filings.** Status: all DRAFT.

## Campaign relationships

No defended cross-family links. `intelligence/campaign-relationships.csv` remains empty of invented edges.
