# ATT&CK Mapping — matanbuchus

**Status:** `PRIMARY_FROZEN_COMPARATOR`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Huntress + Morphisec + Zscaler (TECHNIQUE_COMPARATOR for SynkLoader — authorship NOT_ESTABLISHED)  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1204.001` | User Execution: Malicious Link | Execution | ClickFix social engineering prompting victim to run installer command | High | Windows | Huntress |
| `T1566.002` | Phishing: Spearphishing Link | Initial Access | Teams IT-helpdesk / Quick Assist social engineering (Morphisec campaign) | High | Windows | Morphisec |
| `T1218.005` | System Binary Proxy Execution: Mshta / MSI | Execution | Silent MSI install path (Huntress); scripted archive unpack (Morphisec) | High | Windows | Huntress/Morphisec |
| `T1574.002` | Hijack Execution Flow: DLL Side-Loading | Defense Evasion/Execution | Zillya-style / Notepad++ GUP sideload of malicious libcurl.dll / jli.dll | High | Windows | Huntress/Morphisec |
| `T1053.005` | Scheduled Task/Job: Scheduled Task | Persistence | EventLogBackupTask (Morphisec) | High | Windows | Morphisec |
| `T1027` | Obfuscated Files or Information | Defense Evasion | ChaCha20 Matanbuchus 3.0; encrypted main module from marle.io | High | Windows | Huntress/Zscaler |
| `T1055` | Process Injection | Defense Evasion | Reflective PE loader → AstarionRAT | High | Windows | Huntress |
| `T1056` | Input Capture | Credential Access | AstarionRAT credential theft / impersonation commands | High | Windows | Huntress |
| `T1090` | Proxy | Command and Control | AstarionRAT SOCKS5 proxy | High | Windows | Huntress |
| `T1046` | Network Service Discovery | Discovery | AstarionRAT port scanning | High | Windows | Huntress |
| `T1071.001` | Application Layer Protocol: Web Protocols | Command and Control | marle.io; ndibstersoft.com telemetry-like path; fixuplink.com | High | Windows | Huntress/Morphisec |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/matanbuchus/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
