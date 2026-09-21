# ATT&CK Mapping — argamal

**Status:** `PRIMARY_FROZEN`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Kaspersky GReAT Securelist 2026-06-03  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1189` | Drive-by Compromise | Initial Access | Trojanized adult/hentai games via catalogue sites→PixelDrain and torrents | High | Windows | PRIMARY |
| `T1204.002` | User Execution: Malicious File | Execution | Victim launches infected game loading modified ffmpeg.dll | High | Windows | PRIMARY |
| `T1574.001` | Hijack Execution Flow: DLL Search Order Hijacking | Defense Evasion/Execution | Modified FFmpeg DLL loaded by legitimate game | High | Windows | PRIMARY |
| `T1059.001` | Command and Scripting Interpreter: PowerShell | Execution | natives2_blob.bin PowerShell stages | High | Windows | PRIMARY |
| `T1546.015` | Event Triggered Execution: Component Object Model Hijacking | Persistence | COM hijack InprocServer32 CLSID used by Windows Color System Calibration Loader task | High | Windows | PRIMARY |
| `T1027.013` | Obfuscated Files or Information: Encrypted/Encoded File | Defense Evasion | AES-CBC payload decrypt | High | Windows | PRIMARY |
| `T1071` | Application Layer Protocol | Command and Control | UDP heartbeats (57441/63559) and TCP RAT mode (3747) | High | Windows | PRIMARY |
| `T1555` | Credentials from Password Stores | Credential Access | Credential/data theft goals per Kaspersky | High | Windows | PRIMARY |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/argamal/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
