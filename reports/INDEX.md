# Emerging Threat Watch — Corpus Index

Single entry point for investigators and industry partners. Each family is **case-isolated**.

## Law-enforcement packages

| # | Family | Case ID | Status | Package | STIX / CTI tree |
|---|--------|---------|--------|---------|-----------------|
| 01 | Rapuncel | `ETW-RAP-IC3` | `FILED_IC3` | [01-rapuncel](law-enforcement/packages/01-rapuncel/) | [CTI-Evidence-Repository](law-enforcement/CTI-Evidence-Repository/) |
| 02 | Settra | `ETW-SET-IC3` | `FILED_IC3` | [02-settra](law-enforcement/packages/02-settra/) | same |
| 03 | RatHat | `ETW-RAT-IC3` | `FILED_IC3` | [03-rathat](law-enforcement/packages/03-rathat/) | same |
| 04 | NodeRabbit | `ETW-NRB-IC3` | `FILED_IC3` | [04-noderabbit](law-enforcement/packages/04-noderabbit/) | same |
| 05 | PollCat | `ETW-POL-IC3` | `FILED_IC3` | [05-pollcat](law-enforcement/packages/05-pollcat/) | same |
| 06 | SynkLoader | `ETW-SYN-IC3` | `FILED_IC3` | [06-synkloader](law-enforcement/packages/06-synkloader/) | same |
| 07 | Showboat | `ETW-SHO-IC3` | `FILED_IC3` | [07-showboat](law-enforcement/packages/07-showboat/) | same |
| 08 | Abyssos | `ETW-ABY-IC3` | `FILED_IC3` | [08-abyssos](law-enforcement/packages/08-abyssos/) | same |
| 09 | SharkLoader | `ETW-SHK-IC3` | `FILED_IC3` | [09-sharkloader](law-enforcement/packages/09-sharkloader/) | same |
| 10 | TencShell | `ETW-TEN-IC3` | `PRIMARY_FROZEN` | [10-tencshell](law-enforcement/packages/10-tencshell/) | same |
| 11 | MiniFast | `ETW-MNF-IC3` | `PRIMARY_FROZEN` | [11-minifast](law-enforcement/packages/11-minifast/) | same |
| 12 | Argamal | `ETW-ARG-IC3` | `PRIMARY_FROZEN` | [12-argamal](law-enforcement/packages/12-argamal/) | same |
| 13 | Okobot | `ETW-OKO-IC3` | `PRIMARY_FROZEN` | [13-okobot](law-enforcement/packages/13-okobot/) | same |
| 14 | Matanbuchus | `ETW-MAT-IC3` | `PRIMARY_FROZEN` | [14-matanbuchus](law-enforcement/packages/14-matanbuchus/) | same |
| 15 | StarlandRAT | `ETW-STR-IC3` | `PRIMARY_FROZEN` | [15-starlandrat](law-enforcement/packages/15-starlandrat/) | same |

Machine status table: [`law-enforcement/MASTER_INDEX.csv`](law-enforcement/MASTER_INDEX.csv)

## Recommended reading order (per family)

1. `02_FBI_SUMMARY.md` — narrative summary  
2. `03_INDICATORS.csv` — indicators  
3. `04_SOURCES.md` — primary research URLs  
4. `05_CAVEATS_AND_LIMITS.md` — non-claims  
5. `IC3_FULL_PACKAGE.md` — structured dossier  
6. `IC3_FILING_RECORD.md` — only when filed  

## Cross-cutting intelligence

| Resource | Path |
|----------|------|
| Combined IOCs | [`../intelligence/combined_iocs.csv`](../intelligence/combined_iocs.csv) |
| ATT&CK mappings matrix | [`../intelligence/attack-mappings-matrix.csv`](../intelligence/attack-mappings-matrix.csv) |
| ATT&CK corpus map | [`landscape/ATTACK_CORPUS_MAP.md`](landscape/ATTACK_CORPUS_MAP.md) |
| Evidence completeness | [`landscape/EVIDENCE_COMPLETENESS.md`](landscape/EVIDENCE_COMPLETENESS.md) |
| Vendor / CERT contacts | [`law-enforcement/RESPONSIBLE_SUBMISSION/VENDOR_CONTACTS.md`](law-enforcement/RESPONSIBLE_SUBMISSION/VENDOR_CONTACTS.md) |
| Analyst investigations | [`../investigations/`](../investigations/) |

## Hard rules

- One family = one case unless linkage evidence is documented.  
- No malware binaries in this repository or in IC3 web forms.  
- Distinguish *“researchers reported”* from *“ETW observed.”*  
- Operator identity is `NOT_ESTABLISHED` unless a court or LE source states otherwise.  
