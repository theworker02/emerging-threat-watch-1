# Law Enforcement Handoff

**Audience:** FBI / IC3 investigators, cybercrime units, and partner CERTs  
**Status:** Packages 01–09 `FILED_IC3` · Packages 10–15 `PRIMARY_FROZEN` (structured dossiers ready; not auto-filed)  
**Research cutoff:** 2026-09-19 (unless a package notes otherwise)  
**Independently observed campaign ownership by ETW:** none

This folder is the **investigator front door**. Complainant PII and local filing worksheets remain offline under `private/` (gitignored).

Machine-ingestible evidence (STIX + IOC CSVs): [`CTI-Evidence-Repository/`](CTI-Evidence-Repository/).  
Corpus index: [`../INDEX.md`](../INDEX.md).  
External tips: [`../../docs/SUBMIT_INTEL.md`](../../docs/SUBMIT_INTEL.md).

## Start here

| Step | Action |
|------|--------|
| 1 | Read [`HOW_TO_FILE.md`](HOW_TO_FILE.md) — IC3 vs FBI tips vs hosting abuse gates |
| 2 | Open **one** family under [`packages/`](packages/) |
| 3 | Use `02_FBI_SUMMARY.md` + `03_INDICATORS.csv` + `04_SOURCES.md` + `05_CAVEATS_AND_LIMITS.md` |
| 4 | Review `IC3_FULL_PACKAGE.md` for the structured narrative |
| 5 | Check [`MASTER_INDEX.csv`](MASTER_INDEX.csv) for filing status / complaint numbers |
| 6 | Optional STIX/CSV: [`CTI-Evidence-Repository/README.md`](CTI-Evidence-Repository/README.md) |

**Enforcement readiness (PCAP / takedown gates):** [`../../docs/ENFORCEMENT_READINESS.md`](../../docs/ENFORCEMENT_READINESS.md).

## Packages

### Filed (`FILED_IC3`)

| # | Family | Case code | Threat | Folder |
|---|--------|-----------|--------|--------|
| 1 | Rapuncel | `ETW-RAP-IC3` | Windows stealer / GitHub-SEO distribution | [`packages/01-rapuncel/`](packages/01-rapuncel/) |
| 2 | Settra | `ETW-SET-IC3` | Enterprise ransomware + operator intrusion | [`packages/02-settra/`](packages/02-settra/) |
| 3 | RatHat | `ETW-RAT-IC3` | Android Accessibility → Wireless ADB RAT | [`packages/03-rathat/`](packages/03-rathat/) |
| 4 | NodeRabbit | `ETW-NRB-IC3` | Cross-platform developer-targeted RAT | [`packages/04-noderabbit/`](packages/04-noderabbit/) |
| 5 | PollCat | `ETW-POL-IC3` | Cross-platform obfuscated JavaScript RAT | [`packages/05-pollcat/`](packages/05-pollcat/) |
| 6 | SynkLoader | `ETW-SYN-IC3` | Modular mixed-language loader / Teams phishing | [`packages/06-synkloader/`](packages/06-synkloader/) |
| 7 | Showboat | `ETW-SHO-IC3` | Linux modular post-exploitation (telecom) | [`packages/07-showboat/`](packages/07-showboat/) |
| 8 | Abyssos | `ETW-ABY-IC3` | Modular RAT (Zscaler) | [`packages/08-abyssos/`](packages/08-abyssos/) |
| 9 | SharkLoader | `ETW-SHK-IC3` | Custom loader → Cobalt Strike (StrikeShark) | [`packages/09-sharkloader/`](packages/09-sharkloader/) |

Complaint numbers are recorded in each package’s `IC3_FILING_RECORD.md` and in [`MASTER_INDEX.csv`](MASTER_INDEX.csv).

### Primary-frozen (structured dossiers; not IC3-filed by ETW automation)

| # | Family | Case code | Threat | Folder |
|---|--------|-----------|--------|--------|
| 10 | TencShell | `ETW-TEN-IC3` | Go implant / customized Rshell | [`packages/10-tencshell/`](packages/10-tencshell/) |
| 11 | MiniFast | `ETW-MNF-IC3` | Zoom trust abuse; **≠ PollCat** | [`packages/11-minifast/`](packages/11-minifast/) |
| 12 | Argamal | `ETW-ARG-IC3` | Trojanized adult games RAT | [`packages/12-argamal/`](packages/12-argamal/) |
| 13 | Okobot | `ETW-OKO-IC3` | Multi-payload / OkoSpyware | [`packages/13-okobot/`](packages/13-okobot/) |
| 14 | Matanbuchus | `ETW-MAT-IC3` | SynkLoader **technique comparator only** | [`packages/14-matanbuchus/`](packages/14-matanbuchus/) |
| 15 | StarlandRAT | `ETW-STR-IC3` | Python RAT / WLDR companion | [`packages/15-starlandrat/`](packages/15-starlandrat/) |

**Do not merge** PollCat with NodeRabbit or MiniFast. **Do not file** Matanbuchus jointly with SynkLoader.

## Standard package layout

```
packages/NN-family/
├── 02_FBI_SUMMARY.md
├── 03_INDICATORS.csv
├── 04_SOURCES.md
├── 05_CAVEATS_AND_LIMITS.md
├── IC3_FULL_PACKAGE.md
└── IC3_FILING_RECORD.md      ← after a recorded IC3 filing
```

## Hard rules

1. **One family = one filing** unless a human reviewer documents linkage evidence.  
2. **Never auto-submit** IC3 or vendor portals from this repository.  
3. Language must distinguish *“researchers reported”* from *“I observed.”*  
4. **No malware binaries** in IC3 web forms or this repository.  
5. **No invented** dollar losses, victim names, hashes, or C2 hosts.  
6. Hosting / ASN abuse requires ETW lab PCAP + sample SHA-256 — see enforcement readiness.

## Vendor / CERT coordination

Public contacts and family briefs: [`RESPONSIBLE_SUBMISSION/`](RESPONSIBLE_SUBMISSION/).

## Related paths

| Need | Path |
|------|------|
| Full investigation evidence | `investigations/<family>/` |
| Combined IOC index | `intelligence/combined_iocs.csv` |
| Case isolation policy | `shared/methodology/CASE_ISOLATION.md` |
| Takedown evidence template | [`TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md) |
| Narrative dossier template | [`SUBMISSION_REPORT.TEMPLATE.md`](SUBMISSION_REPORT.TEMPLATE.md) |
