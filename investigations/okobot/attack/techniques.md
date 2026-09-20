# ATT&CK Mapping — okobot

**Status:** `PRIMARY_FROZEN`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Kaspersky Securelist + Gridinsoft TookPS companion  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1204.002` | User Execution: Malicious File | Execution | ClickFix / fake software (e.g. SSMS) / GitHub lures executing TookPS | High | Windows | PRIMARY |
| `T1059.001` | Command and Scripting Interpreter: PowerShell | Execution | TookPS PowerShell downloader; Gridinsoft 22tuk.digital/online/took.php → iex | High | Windows | PRIMARY |
| `T1053.005` | Scheduled Task/Job: Scheduled Task | Persistence | \GDrive Backup Sync; Apple Sync RDP tunnel rebuild task | High | Windows | PRIMARY/Gridinsoft |
| `T1572` | Protocol Tunneling | Command and Control | Reverse SSH tunnel orchestration for module delivery | High | Windows | PRIMARY |
| `T1021.004` | Remote Services: SSH | Lateral Movement/C2 | SSH bot / reverse tunnel to published IPs | High | Windows | PRIMARY |
| `T1021.001` | Remote Services: Remote Desktop Protocol | Lateral Movement | RDP enablement + patched termsrv.dll concurrent sessions | High | Windows | PRIMARY |
| `T1548.002` | Abuse Elevation Control Mechanism: Bypass UAC | Privilege Escalation | Windows RPC UAC bypass (HDUtil) | High | Windows | PRIMARY |
| `T1176` | Browser Extensions | Persistence/Collection | Hidden Chromium extension loader (Rilide stealer) | High | Windows | PRIMARY |
| `T1055` | Process Injection | Defense Evasion | SeedHunter injects into Trezor/Ledger Electron apps | High | Windows | PRIMARY |
| `T1056.001` | Input Capture: Keylogging | Collection | MC Keylogger; OkoSpyware keystrokes | High | Windows | PRIMARY |
| `T1113` | Screen Capture | Collection | OkoSpyware FFmpeg video of wallet/password-manager windows; screenshots | High | Windows | PRIMARY |
| `T1555` | Credentials from Password Stores | Credential Access | Wallet files, cookies, credentials; seed-phrase phishing overlays | High | Windows | PRIMARY |
| `T1562.001` | Impair Defenses: Disable or Modify Tools | Defense Evasion | Disable Windows Defender notifications (registry) | High | Windows | PRIMARY |
| `T1071.001` | Application Layer Protocol: Web Protocols | Command and Control | TookPS/Volume2/SeedHunter domains; ir-post.php exfil | High | Windows | PRIMARY |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/okobot/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
