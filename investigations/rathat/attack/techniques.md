# ATT&CK Mapping — rathat

**Status:** `ACTIVE`  
**Matrix:** MITRE ATT&CK Mobile  
**Primary source basis:** Zimperium zLabs 2026-09-16  
**Mapped (UTC):** 2026-09-20T16:03:04Z  

Provenance: techniques are mapped only from **PRIMARY-SOURCE** (or clearly labeled companion PRIMARY) behaviors documented in ETW packages. Retrieving vendor articles ≠ ETW observation. Author attribution remains **NOT_ESTABLISHED** unless a public LE/court source states otherwise.

| Technique ID | Name | Tactic | Documented behavior | Confidence | Platform | Source note |
|--------------|------|--------|---------------------|------------|----------|-------------|
| `T1626.001` | Abuse Elevation Control Mechanism: Device Administrator/Accessibility | Privilege Escalation | Accessibility service (SystemHelperService) abused to control device settings | High | Android | PRIMARY |
| `T1516` | Input Injection | Execution | Accessibility-driven UI automation to enable Wireless Debugging and pair | High | Android | PRIMARY |
| `T1424` | Software Discovery / Debug Abuse | Discovery/Execution | Wireless ADB self-pair using scraped PIN; shell UID via adbd | High | Android | PRIMARY — map as ADB abuse |
| `T1407` | Download New Code at Runtime | Persistence/Execution | Native Go components staged outside ordinary APK lifecycle | High | Android | PRIMARY |
| `T1575` | Native Code | Defense Evasion | Native libs (e.g. liblocal-service.so) for post-APK capabilities | High | Android | PRIMARY |
| `T1521` | Encrypted Channel | Command and Control | FRP-derived reverse-tunnel component for remote access | High | Android | PRIMARY |
| `T1417.001` | Input Capture: Keylogging | Collection | Credential/PIN reconstruction via getevent / locateValues.json patterns | High | Android | PRIMARY |
| `T1636` | Protected User Data | Collection | Banking/credential targeting per Zimperium narrative | Moderate | Android | PRIMARY |

## Case isolation

- Do **not** transfer these technique rows to other families without direct linkage evidence.
- COMMON TECHNIQUE overlaps (e.g., SynkLoader↔Matanbuchus Teams/ClickFix) are labeled in `intelligence/technique-comparators.csv` with `authorship_link=NOT_ESTABLISHED`.

## Detection pointers

See `investigations/rathat/detections/` (where present) and law-enforcement package `03_INDICATORS.csv`.
