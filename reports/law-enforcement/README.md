# Law Enforcement Handoff — FBI & IC3

**Status:** DRAFT packages · Human review required before any filing  
**Research cutoff:** 2026-09-19  
**Corpus retrieval:** 2026-09-19T18:07:48Z  
**Independently observed infrastructure by ETW:** none

This folder is the **only** place to assemble materials for IC3 complaints and FBI cyber referrals from Emerging Threat Watch. Investigation notebooks, claim ledgers, and landscape outlines stay elsewhere; this tree is the filing surface.

Comprehensive local submission dossier: `SUBMISSION_REPORT.md` (gitignored; see TEMPLATE if present).

**Machine-ingestible LE evidence tree (STIX + IOC CSVs + TLP):** [`CTI-Evidence-Repository/`](CTI-Evidence-Repository/) — rebuild with `python shared/tooling/build_cti_evidence_repository.py`.

External tips that may strengthen these packages: [`docs/SUBMIT_INTEL.md`](../../docs/SUBMIT_INTEL.md).

## Start here

| Step | Document |
|------|----------|
| 1 | Read [`HOW_TO_FILE.md`](HOW_TO_FILE.md) — IC3 vs FBI channels **and** hosting/registrar takedown packages (different audiences; both need technical telemetry) |
| 2 | Complete [`SUBMISSION_CHECKLIST.md`](SUBMISSION_CHECKLIST.md) per package |
| 3 | Open **one** family package under [`packages/`](packages/) |
| 4 | Paste `01_NARRATIVE_PASTE.txt` into IC3; attach or reference `03_INDICATORS.csv` + `04_SOURCES.md` |
| 5 | Use `02_FBI_SUMMARY.md` if referring to an FBI field office / tips channel |
| 6 | For hosting/registrar/chat abuse (not IC3 narrative): [`TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md) + [`shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`](../../shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md) |
| 7 | For STIX/CSV evidentiary repo (FBI/HSI/CISA ingest): [`CTI-Evidence-Repository/README.md`](CTI-Evidence-Repository/README.md) |

**Enforcement readiness (what each family has vs lacks for takedown):** [`docs/ENFORCEMENT_READINESS.md`](../../docs/ENFORCEMENT_READINESS.md).

## Fifteen packages (7 active drafts + 8 candidate stubs — do not merge)

### Active (may become filing-ready after human review)

| # | Package | Case code | Threat | Folder |
|---|---------|-----------|--------|--------|
| 1 | Rapuncel | `ETW-RAP-IC3` | Windows stealer / GitHub-SEO distribution | [`packages/01-rapuncel/`](packages/01-rapuncel/) |
| 2 | Settra | `ETW-SET-IC3` | Enterprise ransomware + operator intrusion | [`packages/02-settra/`](packages/02-settra/) |
| 3 | RatHat | `ETW-RAT-IC3` | Android Accessibility → Wireless ADB RAT | [`packages/03-rathat/`](packages/03-rathat/) |
| 4 | NodeRabbit | `ETW-NRB-IC3` | Cross-platform developer-targeted RAT | [`packages/04-noderabbit/`](packages/04-noderabbit/) |
| 5 | PollCat | `ETW-POL-IC3` | Cross-platform obfuscated JavaScript RAT | [`packages/05-pollcat/`](packages/05-pollcat/) |
| 6 | SynkLoader | `ETW-SYN-IC3` | Modular mixed-language loader / Teams phishing | [`packages/06-synkloader/`](packages/06-synkloader/) |
| 7 | Showboat | `ETW-SHO-IC3` | Linux modular post-exploitation (telecom) | [`packages/07-showboat/`](packages/07-showboat/) |

### Candidate / comparator stubs (**NOT READY TO FILE** — empty IOC ledgers)

| # | Package | Case code | Threat | Folder |
|---|---------|-----------|--------|--------|
| 8 | Abyssos | `ETW-ABY-IC3` | Modular RAT (candidate) | [`packages/08-abyssos/`](packages/08-abyssos/) |
| 9 | SharkLoader | `ETW-SHK-IC3` | Custom loader → Cobalt Strike (candidate) | [`packages/09-sharkloader/`](packages/09-sharkloader/) |
| 10 | TencShell | `ETW-TEN-IC3` | Go implant / Rshell lineage problem (candidate) | [`packages/10-tencshell/`](packages/10-tencshell/) |
| 11 | MiniFast | `ETW-MNF-IC3` | Zoom trust abuse; PollCat context only | [`packages/11-minifast/`](packages/11-minifast/) |
| 12 | Argamal | `ETW-ARG-IC3` | Trojanized adult games RAT (candidate) | [`packages/12-argamal/`](packages/12-argamal/) |
| 13 | Okobot | `ETW-OKO-IC3` | Multi-payload / OkoSpyware alias (candidate) | [`packages/13-okobot/`](packages/13-okobot/) |
| 14 | Matanbuchus | `ETW-MAT-IC3` | SynkLoader technique comparator (MaaS) | [`packages/14-matanbuchus/`](packages/14-matanbuchus/) |
| 15 | StarlandRAT | `ETW-STR-IC3` | Python RAT / WLDR companion (candidate) | [`packages/15-starlandrat/`](packages/15-starlandrat/) |

**PollCat and NodeRabbit** share a dual-referenced Securelist primary artifact but remain **separate** IC3 packages. Do not merge.

**Matanbuchus** is a technique-comparator stub for SynkLoader only — `authorship_link=NOT_ESTABLISHED`. Do not file jointly.

Master status table: [`MASTER_INDEX.csv`](MASTER_INDEX.csv)

## Standard file layout (every package)

```
packages/0N-family/
├── 00_COVER_SHEET.md          ← identity, crime-type language, integrity gate
├── 01_NARRATIVE_PASTE.txt     ← plain text for IC3 complaint description
├── 02_FBI_SUMMARY.md          ← short FBI / field-office brief + contact block
├── 03_INDICATORS.csv          ← PRIMARY-SOURCE indicators (not OBSERVED)
├── 04_SOURCES.md              ← exact public research URLs
├── 05_CAVEATS_AND_LIMITS.md   ← what you must not claim
└── 06_EVIDENCE_RETAINED.md    ← local retention checklist
```

## Hard rules

1. **One family = one filing** unless a human reviewer documents linkage evidence.  
2. **Never auto-submit.** These are drafts.  
3. Language must distinguish *“researchers reported”* from *“I observed.”* Baseline infrastructure is **PRIMARY-SOURCE**, not `OBSERVED`.  
4. **No malware binaries** in IC3 web forms. Retain samples offline if you have authorized access.  
5. **No invented dollar losses, victim names, hashes, or C2 hosts.**  
6. Rebuild packages after indicator changes: `python shared/tooling/build_le_packages.py`  
7. **Candidate stubs (08–15)** must not be filed until primary URL freeze + human promotion.

## Relationship to other repo paths

| Need | Path |
|------|------|
| Full investigation evidence | `investigations/<family>/` |
| Claim ledgers | `investigations/<family>/claims/` |
| Combined IOC index | `shared/combined_iocs.csv` |
| Legacy IC3 draft (points here) | `reports/<family>/*_IC3_BRIEF.md` |
| Case isolation policy | `shared/methodology/CASE_ISOLATION.md` |
| High-fidelity takedown / enforcement evidence | `shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md` |
| Takedown package template (tracked) | `reports/law-enforcement/TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md` |
| Takedown package metadata schema | `shared/schemas/takedown-evidence.schema.json` |
| Per-family enforcement readiness | `docs/ENFORCEMENT_READINESS.md` |
| Narrative dossier template | `reports/law-enforcement/SUBMISSION_REPORT.TEMPLATE.md` |
| Gated autonomy (Tier 1 lab) | `shared/methodology/GATED_AUTONOMY.md` |
