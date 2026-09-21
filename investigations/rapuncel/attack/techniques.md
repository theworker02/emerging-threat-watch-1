# ATT&CK Mapping — rapuncel

**Status:** `ACTIVE`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** LastPass TIME + Delphos 2026-09-17  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1189` | Drive-by Compromise | Initial Access | SEO-oriented fraudulent GitHub/Pages lures directing users to stealer downloads | High | Windows | PRIMARY LastPass/Delphos |
| `T1204.002` | User Execution: Malicious File | Execution | Victim runs delivered installer/payload from GitHub SEO lure chain | High | Windows | PRIMARY |
| `T1574.002` | Hijack Execution Flow: DLL Side-Loading | Defense Evasion/Execution | Legitimate Microsoft vsdbg.exe loads malicious vsdbg.dll | High | Windows | PRIMARY |
| `T1027` | Obfuscated Files or Information | Defense Evasion | Cruciferra/PUROSANGUE-class crypter/loader context (tooling; not Rapuncel authorship) | Moderate | Windows | PRIMARY lineage note |
| `T1068` | Exploitation for Privilege Escalation | Privilege Escalation | Alinubx.sys / CcProtect-class BYOVD-style signed-driver abuse assessed in primary lineage analysis | Moderate | Windows | PRIMARY / LOLDrivers companion |
| `T1562.001` | Impair Defenses: Disable or Modify Tools | Defense Evasion | Kernel process terminate of security products via abused signed driver path | Moderate | Windows | PRIMARY |
| `T1555.003` | Credentials from Password Stores: Credentials from Web Browsers | Credential Access | Browser credential theft as stealer capability (wording per primary) | High | Windows | PRIMARY |
| `T1041` | Exfiltration Over C2 Channel | Exfiltration | Published exfil/C2 destinations including 2.26.126.50 in PRIMARY indicators | High | Windows | PRIMARY |
| `T1071.001` | Application Layer Protocol: Web Protocols | Command and Control | HTTPS/web C2 and delivery domains published by researchers | High | Windows | PRIMARY |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/rapuncel/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
