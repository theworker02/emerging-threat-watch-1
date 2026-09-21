# ATT&CK Mapping — pollcat

**Status:** `ACTIVE`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Kaspersky GReAT Securelist 2026-09-01 (PollCat-only; co-disclosure ≠ authorship)  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1566.003` | Phishing: Spearphishing via Service | Initial Access | RankChallenge-react coding-challenge delivery | High | cross-platform | PRIMARY |
| `T1204.002` | User Execution: Malicious File | Execution | Victim opens RankChallenge archive (MD5 795e053a…) | High | cross-platform | PRIMARY |
| `T1059.007` | Command and Scripting Interpreter: JavaScript | Execution | Obfuscated JavaScript RAT | High | cross-platform | PRIMARY |
| `T1027` | Obfuscated Files or Information | Defense Evasion | Heavy JS obfuscation | High | cross-platform | PRIMARY |
| `T1053.005` | Scheduled Task/Job: Scheduled Task | Persistence | NetSync scheduled tasks (Windows) | High | Windows | PRIMARY |
| `T1543` | Create or Modify System Process | Persistence | requireObject.js under AppData; com.harsh.requireobject.plist (macOS); ~/.node_packages | High | cross-platform | PRIMARY |
| `T1071.001` | Application Layer Protocol: Web Protocols | Command and Control | sahi-finance.com; Azure Web Apps; lifespotify.com OTP validation | High | cross-platform | PRIMARY |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/pollcat/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
