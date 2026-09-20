# ATT&CK Mapping — showboat

**Status:** `ACTIVE`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Lumen Black Lotus Labs May 2026  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1190` | Exploit Public-Facing Application | Initial Access | Post-exploitation framework against telecom (initial access may vary; historical activity noted) | Moderate | Linux | PRIMARY |
| `T1105` | Ingress Tool Transfer | Command and Control | Modular post-exploitation component download | High | Linux | PRIMARY |
| `T1071.001` | Application Layer Protocol: Web Protocols | Command and Control | C2 to published IPs/domains (telecom.webredirect-class) | High | Linux | PRIMARY |
| `T1027` | Obfuscated Files or Information | Defense Evasion | Modular Linux implant design with staging (Pastebin historical hide-code noted) | Moderate | Linux | PRIMARY |
| `T1041` | Exfiltration Over C2 Channel | Exfiltration | Post-exploitation data access capabilities implied by framework class | Moderate | Linux | PRIMARY |
| `T1082` | System Information Discovery | Discovery | Host/network discovery typical of modular post-ex frameworks | Moderate | Linux | PRIMARY |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/showboat/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
