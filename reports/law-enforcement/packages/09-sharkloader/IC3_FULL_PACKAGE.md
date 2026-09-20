# IC3 / FBI Full Complaint Package — SharkLoader

**Status:** `PRIMARY_FROZEN` — **not filed** (primary frozen; ready for human filing review) · **Primary freeze:** 2026-09-20  
**Family:** SharkLoader only (case-isolated)  
**Portal:** https://www.ic3.gov/

---

## 1. Filing identity

| Field | Value |
|-------|-------|
| Reporter purpose | Defensive threat-intelligence referral (not personal victimization claim) |
| Crime-type language | Malware; Unauthorized network intrusion / remote access; Credential theft |
| Suggested subject | Defensive TI referral — SharkLoader (Kaspersky GReAT / Securelist 2026-06-24) — `ETW-SHK-IC3` |
| Dollar loss claimed | None |
| Personal victimization claimed | No |
| Malware binaries attached | No |
| ETW live C2 contact | None |
| Independently observed campaign ownership by ETW | None |

### Related prior IC3 Submission IDs (separate — no shared-operator claim)

| Family | Package | Submission ID |
|--------|---------|---------------|
| Rapuncel | `ETW-RAP-IC3` | `208b747c6f7445f0af2b69a9d63acc36` |
| Settra | `ETW-SET-IC3` | `631d8b4800d04bc19cdbfc6662e5c52c` |
| RatHat | `ETW-RAT-IC3` | `f92c4c2f0dd3481f898fdd125e728adf` |
| NodeRabbit | `ETW-NRB-IC3` | `dded86972e9347e0be27a6597b4cf08a` |
| PollCat | `ETW-POL-IC3` | `98a4444754324e539dbbffcb10c70637` |
| SynkLoader | `ETW-SYN-IC3` | `3440d0c64dc240499ff66deaa3311a0b` |
| Showboat | `ETW-SHO-IC3` | `db42033f319844c08ad103befebfca08` |
| Abyssos | `ETW-ABY-IC3` | `a23f0a9d6799480e994284416d354713` |
| **SharkLoader (this package)** | `ETW-SHK-IC3` | *not filed* |

---

## 2. Technical indicator appendix (SHK-IND-0001–0019)

### Compact paste block

```
=== MD5 ===
C559CC68986933200FD5D9E4388E2F58
B3352B42432DEDC4A519F011DC8B5D5A
24FCEBDEECBA65004FDB0923763D74FD
9C872A0D5D5A38950E8B9AC9B488BE3F
AA3086BE652C8B20B0B29B2730D57119
A514D1BB62D7916475946FE7C07AC0AA
9CBD560F820C95D7C38342CD558CB5C6
1F65544978B8EA0E745E573B8EE9684B

=== DOMAIN ===
connect-microsoft.com
ms-record.com
ms-record.top
ms-tray.top

=== PATH ===
%APPDATA%\xwreg
%APPDATA%\xgdf

=== FILENAME ===
SystemSettings.dll
DscCoreR.mui
SyncRes.dat

=== STRING ===
MFUpdate
\Microsoft\Windows\Edge\Edgeupdate

```

Full structured table: [`03_INDICATORS.csv`](03_INDICATORS.csv).

---

## 3. Narrative (short)

Defensive threat-intelligence package concerning SharkLoader as publicly documented by Kaspersky GReAT (Securelist 2026-06-24) in the StrikeShark campaign. Kaspersky describes a multi-component custom loader that DLL-sideloads via abused legitimate binaries (commonly SystemSettings.exe → SystemSettings.dll), decrypts DscCoreR.mui / SyncRes.dat modules, installs API hooks (Detours/MinHook), and executes Cobalt Strike Beacon in memory. Delivery includes exploitation of internet-facing apps and malicious droppers. Kaspersky does not attribute StrikeShark to a known APT with high confidence. Author identity remains NOT_ESTABLISHED.

---

## 4. Case isolation

Standalone candidate promoted after primary freeze. Loader→CS is COMMON TECHNIQUE class only vs other loaders.

---

## 5. Sources

See [`04_SOURCES.md`](04_SOURCES.md). Local freeze: `evidence/primary-sources/sharkloader/securelist-strikeshark-2026-06-24.html` SHA-256 `c5af7fb5acf172632f63b9763e511d756564027cff5cf0ce8a6ffe2fa90934b2`.
