# ATT&CK Mapping — abyssos

**Status:** `ACTIVE`  
**Matrix:** MITRE ATT&CK Enterprise  
**Primary source basis:** Zscaler ThreatLabz 2026-08-10  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1204.002` | User Execution: Malicious File | Execution | Delivery vector under investigation; execution of modular C++ RAT | Moderate | Windows | PRIMARY — delivery not established |
| `T1055` | Process Injection | Defense Evasion | Modular C++ RAT capabilities including stealthy module load | Moderate | Windows | PRIMARY |
| `T1555` | Credentials from Password Stores | Credential Access | Credential theft modules | High | Windows | PRIMARY |
| `T1550` | Use Alternate Authentication Material | Credential Access | Browser-session hijacking | High | Windows | PRIMARY |
| `T1021` | Remote Services | Lateral Movement/C2 | HVNC remote access | High | Windows | PRIMARY |
| `T1041` | Exfiltration Over C2 Channel | Exfiltration | File exfiltration over custom AES-GCM TCP protocol | High | Windows | PRIMARY |
| `T1573.002` | Encrypted Channel: Asymmetric Cryptography | Command and Control | Custom AES-GCM TCP C2 protocol | High | Windows | PRIMARY |
| `T1105` | Ingress Tool Transfer | Command and Control | Downloadable modules | High | Windows | PRIMARY |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/abyssos/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
