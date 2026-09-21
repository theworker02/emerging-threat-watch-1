# ATT&CK Mapping — sharkloader

**Status:** `ACTIVE`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Kaspersky GReAT Securelist 2026-06-24 (StrikeShark)  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1190` | Exploit Public-Facing Application | Initial Access | Exploitation of internet-facing apps (Exchange/SharePoint/Openfire-class CVEs cited) | High | Windows | PRIMARY |
| `T1204.002` | User Execution: Malicious File | Execution | Malicious droppers posing as Google Update / Cisco AnyConnect / PDF decoys | High | Windows | PRIMARY |
| `T1574.002` | Hijack Execution Flow: DLL Side-Loading | Defense Evasion/Execution | SystemSettings.exe sideloads SystemSettings.dll (SharkLoader); alt msedge/PrintDialog/miracastview | High | Windows | PRIMARY |
| `T1027.002` | Obfuscated Files or Information: Software Packing | Defense Evasion | Encrypted modules DscCoreR.mui (Blowfish) / SyncRes.dat (AES-128) | High | Windows | PRIMARY |
| `T1055` | Process Injection | Defense Evasion | Reflective load of Cobalt Strike Beacon in memory | High | Windows | PRIMARY |
| `T1562.006` | Impair Defenses: Indicator Blocking | Defense Evasion | ETW-related evasion; Detours/MinHook API hooks; sleep memory-permission flipping | High | Windows | PRIMARY |
| `T1134.004` | Access Token Manipulation: Parent PID Spoofing | Defense Evasion | PPID spoofing documented | High | Windows | PRIMARY |
| `T1547.001` | Boot or Logon Autostart Execution: Registry Run Keys | Persistence | HKCU Run value MFUpdate | High | Windows | PRIMARY |
| `T1053.005` | Scheduled Task/Job: Scheduled Task | Persistence | \Microsoft\Windows\Edge\Edgeupdate and OneDrive/MicrosoftUpdate-style tasks | High | Windows | PRIMARY |
| `T1071.001` | Application Layer Protocol: Web Protocols | Command and Control | Domains connect-microsoft.com; ms-record.com; ms-record.top; ms-tray.top | High | Windows | PRIMARY |
| `T1003` | OS Credential Dumping | Credential Access | Post-compromise AD enumeration tooling context (Beacon follow-on) | Moderate | Windows | PRIMARY post-ex |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/sharkloader/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
