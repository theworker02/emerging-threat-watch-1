# ATT&CK Mapping — noderabbit

**Status:** `ACTIVE`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Kaspersky GReAT Securelist 2026-09-01  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1566.003` | Phishing: Spearphishing via Service | Initial Access | Recruiter-posed coding assessments delivering malware | High | Windows/Linux/macOS | PRIMARY |
| `T1204.002` | User Execution: Malicious File | Execution | Victim executes coding-challenge archive / Node components | High | cross-platform | PRIMARY |
| `T1059.007` | Command and Scripting Interpreter: JavaScript | Execution | Node.js RAT components | High | cross-platform | PRIMARY |
| `T1546` | Event Triggered Execution | Persistence | Local Git hook persistence | High | cross-platform | PRIMARY |
| `T1547` | Boot or Logon Autostart Execution | Persistence | WSL / platform persistence variants reported | Moderate | Windows/Linux | PRIMARY |
| `T1036` | Masquerading | Defense Evasion | Fake local VS Code extension (“GitHub Copilot Helper”) | High | Windows | PRIMARY |
| `T1573` | Encrypted Channel | Command and Control | Mutable C2 configuration; enterprise-proxy support in later variants | High | cross-platform | PRIMARY |
| `T1071.001` | Application Layer Protocol: Web Protocols | Command and Control | Azure / web C2 hosts published | High | cross-platform | PRIMARY |
| `T1082` | System Information Discovery | Discovery | Host profiling for developer/enterprise environments | Moderate | cross-platform | PRIMARY |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/noderabbit/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
