# ATT&CK Mapping — starlandrat

**Status:** `PRIMARY_FROZEN`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Cisco Talos UAT-11795 + IOC appendix  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1204.001` | User Execution: Malicious Link | Execution | ClickFix → mshta HTA staging | High | Windows | Talos |
| `T1204.002` | User Execution: Malicious File | Execution | Trojanized NSIS installers (WebEx/Zoom/MobaXterm/DBeaver/FACEIT) | High | Windows | Talos |
| `T1218.005` | System Binary Proxy Execution: Mshta | Execution | mshta.exe fetches weaponized HTA | High | Windows | Talos |
| `T1059.006` | Command and Scripting Interpreter: Python | Execution | pythonw.exe loads LICENSE.txt Python loader → Starland RAT in memory | High | Windows | Talos |
| `T1059.001` | Command and Scripting Interpreter: PowerShell | Execution | WLDR PowerShell stager/loader/agent chain | High | Windows | Talos |
| `T1547.001` | Boot or Logon Autostart Execution: Registry Run Keys | Persistence | HKCU Run\MyApp → mshta.exe | High | Windows | Talos |
| `T1053.005` | Scheduled Task/Job: Scheduled Task | Persistence | PythonLauncher-* AtLogOn Highest | High | Windows | Talos |
| `T1547.001` | Startup Folder | Persistence | Startup LNK launching pythonw.exe with LICENSE.txt | High | Windows | Talos |
| `T1497.001` | Virtualization/Sandbox Evasion: System Checks | Defense Evasion | Sandbox username/hostname checks; Zone.Identifier ADS check | High | Windows | Talos |
| `T1562.001` | Impair Defenses: Disable or Modify Tools | Defense Evasion | AMSI/ETW patching before shellcode inject | High | Windows | Talos |
| `T1055` | Process Injection | Defense Evasion | APC-based shellcode injection; reflective CastleStealer/Remcos | High | Windows | Talos |
| `T1555` | Credentials from Password Stores | Credential Access | Browser + 40+ crypto wallet recon/theft | High | Windows | Talos |
| `T1113` | Screen Capture | Collection | Desktop screenshots | High | Windows | Talos |
| `T1071.001` | Application Layer Protocol: Web Protocols | Command and Control | Primary C2 domains; WLDR encrypted HTTPS beaconing | High | Windows | Talos |
| `T1102` | Web Service | Command and Control | Telegram bot notification/beacon path | High | Windows | Talos |
| `T1608` | Stage Capabilities | Resource Development | Polygon smart-contract dead-drop for fallback C2 domain | High | Windows | Talos — novel resolver |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/starlandrat/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
