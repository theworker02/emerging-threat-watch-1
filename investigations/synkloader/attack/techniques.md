# ATT&CK Mapping — synkloader

**Status:** `ACTIVE`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Expel 2026-08-20  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1566.002` | Phishing: Spearphishing Link | Initial Access | Microsoft Teams IT-helpdesk phishing (external *.onmicrosoft.com tenant) | High | Windows | PRIMARY |
| `T1204.002` | User Execution: Malicious File | Execution | Victim runs MSI (PowershellCleaner) from Azure Blob | High | Windows | PRIMARY |
| `T1059.001` | Command and Scripting Interpreter: PowerShell | Execution | Nested PowerShell decryption into in-memory Python loader (ss.py) | High | Windows | PRIMARY |
| `T1059.006` | Command and Scripting Interpreter: Python | Execution | In-memory Python loader | High | Windows | PRIMARY |
| `T1036.005` | Masquerading: Match Legitimate Name or Location | Defense Evasion | Fake VC++ DLLs msvcp150.dll / msvcp160.dll | High | Windows | PRIMARY |
| `T1056.002` | Input Capture: GUI Input Capture | Credential Access | PhishLocker fake Windows 11 lock-screen credential theft | High | Windows | PRIMARY |
| `T1219` | Remote Access Software | Command and Control | StreamMaster VNC module | High | Windows | PRIMARY |
| `T1090` | Proxy | Command and Control | TrafficRedirector tunneling module | High | Windows | PRIMARY |
| `T1071.001` | Application Layer Protocol: Web Protocols | Command and Control | Modular C2 over HTTPS to published domains/IPs | High | Windows | PRIMARY |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/synkloader/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
