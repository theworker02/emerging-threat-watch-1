# Law Enforcement Handoff — FBI & IC3

**Status:** Rapuncel, Settra, RatHat, NodeRabbit, PollCat, SynkLoader, Showboat `FILED_IC3` · candidates remain unfiled  
**Research cutoff:** 2026-09-19  
**Independently observed campaign ownership by ETW:** none

This folder holds **investigator-facing** law-enforcement materials for Emerging Threat Watch. IC3 form-fill helpers (cover sheets, narrative pastes, retention checklists) are **local-only** under `private/filing-helpers/` (gitignored).

Comprehensive local submission dossier: `SUBMISSION_REPORT.md` (gitignored; see TEMPLATE if present).

**Machine-ingestible LE evidence tree (STIX + IOC CSVs + TLP):** [`CTI-Evidence-Repository/`](CTI-Evidence-Repository/) — rebuild with `python shared/tooling/build_cti_evidence_repository.py`.

External tips: [`docs/SUBMIT_INTEL.md`](../../docs/SUBMIT_INTEL.md).

## Start here

| Step | Document |
|------|----------|
| 1 | Read [`HOW_TO_FILE.md`](HOW_TO_FILE.md) — IC3 vs FBI vs hosting/registrar takedown |
| 2 | Open **one** family package under [`packages/`](packages/) |
| 3 | Use `02_FBI_SUMMARY.md` + `03_INDICATORS.csv` + `04_SOURCES.md` + `05_CAVEATS_AND_LIMITS.md` |
| 4 | If filing IC3 yourself: local helpers in `private/filing-helpers/<package>/` (not in git) |
| 5 | STIX/CSV evidentiary repo: [`CTI-Evidence-Repository/README.md`](CTI-Evidence-Repository/README.md) |

**Enforcement readiness:** [`docs/ENFORCEMENT_READINESS.md`](../../docs/ENFORCEMENT_READINESS.md).

## Fifteen packages (7 active + 8 candidate stubs — do not merge)

### Active

| # | Package | Case code | Threat | Folder |
|---|---------|-----------|--------|--------|
| 1 | Rapuncel | `ETW-RAP-IC3` | Windows stealer / GitHub-SEO distribution | [`packages/01-rapuncel/`](packages/01-rapuncel/) — **FILED_IC3** `208b747c6f7445f0af2b69a9d63acc36` (2026-09-19 4:44:37 PM EST); [`IC3_FILING_RECORD.md`](packages/01-rapuncel/IC3_FILING_RECORD.md) |
| 2 | Settra | `ETW-SET-IC3` | Enterprise ransomware + operator intrusion | [`packages/02-settra/`](packages/02-settra/) — **FILED_IC3** `631d8b4800d04bc19cdbfc6662e5c52c` (2026-09-19 4:59:46 PM EST); [`IC3_FILING_RECORD.md`](packages/02-settra/IC3_FILING_RECORD.md) |
| 3 | RatHat | `ETW-RAT-IC3` | Android Accessibility → Wireless ADB RAT | [`packages/03-rathat/`](packages/03-rathat/) — **FILED_IC3** `f92c4c2f0dd3481f898fdd125e728adf` (2026-09-19 5:08:29 PM EST); [`IC3_FILING_RECORD.md`](packages/03-rathat/IC3_FILING_RECORD.md) |
| 4 | NodeRabbit | `ETW-NRB-IC3` | Cross-platform developer-targeted RAT | [`packages/04-noderabbit/`](packages/04-noderabbit/) — **FILED_IC3** `dded86972e9347e0be27a6597b4cf08a` (2026-09-19 5:15:51 PM EST); [`IC3_FILING_RECORD.md`](packages/04-noderabbit/IC3_FILING_RECORD.md) |
| 5 | PollCat | `ETW-POL-IC3` | Cross-platform obfuscated JavaScript RAT | [`packages/05-pollcat/`](packages/05-pollcat/) — **FILED_IC3** `98a4444754324e539dbbffcb10c70637` (2026-09-19 9:52:51 PM EST); [`IC3_FILING_RECORD.md`](packages/05-pollcat/IC3_FILING_RECORD.md) · pointer [`reports/pollcat/POLLCAT_IC3_BRIEF.md`](../pollcat/POLLCAT_IC3_BRIEF.md) |
| 6 | SynkLoader | `ETW-SYN-IC3` | Modular mixed-language loader / Teams phishing | [`packages/06-synkloader/`](packages/06-synkloader/) — **FILED_IC3** `3440d0c64dc240499ff66deaa3311a0b` (2026-09-19 10:04:35 PM EST); [`IC3_FILING_RECORD.md`](packages/06-synkloader/IC3_FILING_RECORD.md) |
| 7 | Showboat | `ETW-SHO-IC3` | Linux modular post-exploitation (telecom) | [`packages/07-showboat/`](packages/07-showboat/) — **FILED_IC3** `db42033f319844c08ad103befebfca08` (2026-09-19 10:13:28 PM EST); [`IC3_FILING_RECORD.md`](packages/07-showboat/IC3_FILING_RECORD.md) |

### Candidate / comparator stubs (**NOT READY TO FILE**)

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

## Standard public package layout

```
packages/0N-family/
├── 02_FBI_SUMMARY.md          ← investigator-facing summary
├── 03_INDICATORS.csv          ← PRIMARY-SOURCE / labeled OBSERVED_PASSIVE indicators
├── 04_SOURCES.md              ← exact public research URLs
├── 05_CAVEATS_AND_LIMITS.md   ← what this package does not claim
├── FILING_SETUP.md            ← optional; present for PollCat (next active filing)
├── REVIEW_CHECKLIST.md        ← optional; pre-submit review copy
└── IC3_FILING_RECORD.md       ← only after an IC3 filing is recorded (Rapuncel–NodeRabbit have this)
```

Local filing helpers (gitignored): `private/filing-helpers/0N-family/` (`00_COVER_SHEET.md`, `01_NARRATIVE_PASTE.txt`, `06_EVIDENCE_RETAINED.md`). Regenerate with `python shared/tooling/build_le_packages.py`.

## Hard rules

1. **One family = one filing** unless a human reviewer documents linkage evidence.  
2. **Never auto-submit.**  
3. Language must distinguish *“researchers reported”* from *“I observed.”*  
4. **No malware binaries** in IC3 web forms.  
5. **No invented dollar losses, victim names, hashes, or C2 hosts.**  
6. Rebuild public packages after indicator changes: `python shared/tooling/build_le_packages.py`  
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
| Local IC3 form helpers | `reports/law-enforcement/private/filing-helpers/` (gitignored) |
