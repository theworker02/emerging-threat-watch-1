# ATT&CK Mapping — tencshell

**Status:** `PRIMARY_FROZEN`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Cato CTRL + Hunt.io follow-on  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1199` | Trusted Relationship | Initial Access | Third-party user connection into manufacturer environment (India site) | High | Windows | Cato PRIMARY |
| `T1204.002` | User Execution: Malicious File | Execution | Dropper → masqueraded .woff Donut shellcode chain | High | Windows | Cato PRIMARY |
| `T1055` | Process Injection | Defense Evasion | Reflective / in-memory load of Go implant | High | Windows | Cato PRIMARY |
| `T1036.005` | Masquerading: Match Legitimate Name or Location | Defense Evasion | Masqueraded .woff web-font staging; Tencent-like API path impersonation | High | Windows | Cato PRIMARY |
| `T1548.002` | Abuse Elevation Control Mechanism: Bypass User Account Control | Privilege Escalation | UAC_BYPASS opcode/module | High | Windows | Cato PRIMARY |
| `T1547.001` | Boot or Logon Autostart Execution: Registry Run Keys | Persistence | Run value OneDriveHealthTask | High | Windows | Cato PRIMARY |
| `T1113` | Screen Capture | Collection | Screen capture / live screen streaming over WebSocket | High | Windows | Cato PRIMARY |
| `T1056.001` | Input Capture: Keylogging | Collection | Keyboard/mouse simulation and input routines | High | Windows | Cato PRIMARY |
| `T1555.003` | Credentials from Password Stores: Credentials from Web Browsers | Credential Access | Chrome/Edge artifact access (sessions/cookies/logins) | High | Windows | Cato PRIMARY |
| `T1090` | Proxy | Command and Control | SOCKS5 proxying | High | Windows | Cato PRIMARY |
| `T1071.001` | Application Layer Protocol: Web Protocols | Command and Control | Web/API-like C2; Tencent-themed paths; Hunt.io port 1111 cluster | High | Windows | Cato + Hunt.io |
| `T1105` | Ingress Tool Transfer | Command and Control | In-memory payload execution / additional tooling path | High | Windows | Cato PRIMARY |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/tencshell/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
