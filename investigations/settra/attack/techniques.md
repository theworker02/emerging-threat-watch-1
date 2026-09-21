# ATT&CK Mapping — settra

**Status:** `ACTIVE`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Cynet + Huntress + MOXFIVE  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

**Analytical note:** Separate malware encryptor matrix from operator intrusion matrix (case isolation within family).

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1497` | Virtualization/Sandbox Evasion | Defense Evasion | Debugger checks; inert exit without --pass (encryptor) | High | Windows | Cynet malware |
| `T1027` | Obfuscated Files or Information | Defense Evasion | ~1.4MB encrypted blob; AES-256-CTR after iterated SHA-256 | High | Windows | Cynet malware |
| `T1055` | Process Injection | Defense Evasion | Process hollowing of inner encryptor (reported) | Moderate | Windows | Cynet malware |
| `T1486` | Data Encrypted for Impact | Impact | Per-file keys + 4096-bit RSA wrap; .locked extensions | High | Windows | Cynet/Huntress malware |
| `T1490` | Inhibit System Recovery | Impact | reagentc/diskpart/cipher; WinRE/VSS/System Restore interference | High | Windows | Cynet/Huntress malware |
| `T1489` | Service Stop | Impact | Hyper-V VM power-off / recovery inhibition patterns | High | Windows | Cynet malware |
| `T1070.001` | Indicator Removal: Clear Windows Event Logs | Defense Evasion | Clears multiple event logs | High | Windows | Cynet malware |
| `T1078` | Valid Accounts | Initial Access/Persistence | Compromised VPN / valid credentials (operator IR) | High | Windows | MOXFIVE operator |
| `T1046` | Network Service Discovery | Discovery | NetExec / Netscan mapping | High | Windows | MOXFIVE operator |
| `T1003` | OS Credential Dumping | Credential Access | Procdump / Mimikatz observed in IR (operator tooling — not Settra.exe) | High | Windows | MOXFIVE operator |
| `T1021` | Remote Services | Lateral Movement | PAExec / NetExec lateral movement | High | Windows | MOXFIVE operator |
| `T1219` | Remote Access Software | Command and Control | MeshAgent RMM abuse (45.13.122.7 / 193.5.65.114) | High | Windows | Huntress/MOXFIVE operator |
| `T1562` | Impair Defenses | Defense Evasion | edr_blind; BYOVD drivers (gdrv.sys / STProcessMonitor) in operator stage | High | Windows | Huntress/MOXFIVE operator |
| `T1657` | Financial Theft | Impact | Tor leak site + Tox negotiations (extortion workflow) | Moderate | Network | MOXFIVE operator |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/settra/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
