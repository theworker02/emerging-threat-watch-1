# ATT&CK Mapping — minifast

**Status:** `PRIMARY_FROZEN`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Check Point Research + Unit 42 Screening Serpens  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1566.001` | Phishing: Spearphishing Attachment | Initial Access | Career/aviation lures; trojanized Zoominstall64.zip | High | Windows | Check Point |
| `T1608.006` | Stage Capabilities: SEO Poisoning | Resource Development/Initial Access | SEO-poisoned SQL Developer lure getsqldeveloper.com | High | Windows | Check Point |
| `T1204.002` | User Execution: Malicious File | Execution | Victim runs trojanized installer | High | Windows | Check Point |
| `T1574.014` | Hijack Execution Flow: AppDomainManager | Defense Evasion/Execution | AppDomain hijacking via .config / UpdateConfig.xml | High | Windows | Check Point / Unit 42 |
| `T1553.002` | Subvert Trust Controls: Code Signing | Defense Evasion | SSL.com-issued code-signing certificates abused (Gray Matter / Kirubel) | High | Windows | Check Point |
| `T1053.005` | Scheduled Task/Job: Scheduled Task | Persistence | Hijack ZoomUpdateTaskUser-*; WindowsSecurityUpdate persistence | High | Windows | Check Point |
| `T1548.002` | Abuse Elevation Control Mechanism: Bypass UAC | Privilege Escalation | UAC elevation opcode in MiniFast command set | High | Windows | Check Point |
| `T1105` | Ingress Tool Transfer | Command and Control | DLL load / file download commands | High | Windows | Check Point |
| `T1071.001` | Application Layer Protocol: Web Protocols | Command and Control | JSON HTTPS C2 (/agent/init,/agent/poll,/upload/) + Azure Web Apps | High | Windows | Check Point |
| `T1036` | Masquerading | Defense Evasion | UpdateChecker.dll / CheckForUpdates export; Chrome UA impersonation | High | Windows | Check Point |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/minifast/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
