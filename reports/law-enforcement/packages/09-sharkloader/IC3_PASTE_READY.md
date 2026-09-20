# SharkLoader — IC3 Paste-Ready Pack (`ETW-SHK-IC3`)

**Status:** `FILED_IC3` · Submission ID `6ed57963d0c64750aa14b6fcbaa2e576` · filed 2026-09-19 10:43:18 PM EST  
**Portal:** https://www.ic3.gov/

Copy each section into the matching IC3 form field. Counts are under typical IC3 limits (description ≈3,500 · technical ≈5,000 · witnesses ≈1,000).

---

## 1. Subject line / title

```
Defensive TI referral — SharkLoader / StrikeShark (Kaspersky Securelist 2026-06-24) — ETW-SHK-IC3
```

## 2. Crime types

```
Malware; Unauthorized network intrusion / remote access
```

## 3. Subject #1 fields

| Field | Value |
|-------|-------|
| Name | Unknown |
| Business | Unknown (StrikeShark campaign / SharkLoader malware) |
| Address / City / State / ZIP / Country | Unknown |
| Phone | Unknown |
| Email | Unknown |
| Website | connect-microsoft.com; ms-record.com; ms-record.top; ms-tray.top |
| IP address | Unknown (no C2 IPv4 in public Securelist IOC block) |
| Notes | Author/operator NOT_ESTABLISHED; Kaspersky APT attribution not high-confidence |

## 4. Financial / loss

| Field | Value |
|-------|-------|
| Total loss | **0** / None |
| Transactions | None / blank |
| Personal victimization | No |

## 5. Description (what happened)

*(3325 characters)*

```
I am reporting defensive threat-intelligence information concerning the SharkLoader malware documented by Kaspersky GReAT on June 24, 2026 in the Securelist article “StrikeShark: investigating a new campaign delivering Cobalt Strike through SharkLoader” (https://securelist.com/strikeshark-campaign/120326/). Filing as Emerging Threat Watch package ETW-SHK-IC3 — defensive TI referral, not a personal victimization or dollar-loss claim.

Kaspersky describes SharkLoader as a previously undocumented multi-component custom loader used in an intrusion cluster tracked as StrikeShark, used to deploy Cobalt Strike Beacon on Windows. Initial access includes exploitation of internet-facing applications (Microsoft Exchange, SharePoint, Openfire, and other PoC-available CVEs) and malware droppers posing as installers (e.g., Google Update / Cisco AnyConnect) or PDF decoys. Kaspersky reports victims including diplomatic entities in Indonesia, government agencies in Taiwan, and organizations in Hong Kong, Lebanon, Syria, Colombia, North Macedonia, Nepal, and Serbia.

The common chain copies legitimate SystemSettings.exe (from C:\Windows\ImmersiveControlPanel) into a writable directory and sideloads malicious SystemSettings.dll (SharkLoader), with encrypted modules DscCoreR.mui (Beacon + MinHook; Blowfish) and SyncRes.dat/SyncRest.dat (Detours API hooks; AES-128). Kaspersky documents reflective loading, ETW-related evasion, PPID spoofing, and sleep-time memory-permission flipping. Persistence includes HKCU Run value “MFUpdate” and scheduled task “\Microsoft\Windows\Edge\Edgeupdate”; droppers also create OneDrive/MicrosoftUpdate-style tasks under %APPDATA%\xwreg or %APPDATA%\xgdf.

Kaspersky does not attribute StrikeShark to a known APT with high confidence. Author/operator identity remains NOT_ESTABLISHED by Emerging Threat Watch. Cobalt Strike Beacon hashes are not invented here.

INDICATORS (PRIMARY-SOURCE; full CSV SHK-IND-0001–0019 on request):
MD5: C559CC68986933200FD5D9E4388E2F58; B3352B42432DEDC4A519F011DC8B5D5A; 24FCEBDEECBA65004FDB0923763D74FD; 9C872A0D5D5A38950E8B9AC9B488BE3F; AA3086BE652C8B20B0B29B2730D57119; A514D1BB62D7916475946FE7C07AC0AA; 9CBD560F820C95D7C38342CD558CB5C6; 1F65544978B8EA0E745E573B8EE9684B.
Domains: connect-microsoft.com; ms-record.com; ms-record.top; ms-tray.top.
Host: SystemSettings.dll; DscCoreR.mui; SyncRes.dat; %APPDATA%\xwreg; %APPDATA%\xgdf; MFUpdate; \Microsoft\Windows\Edge\Edgeupdate. Alternate sideloads noted: msedge.dll; PrintDialog.dll; miracastview.dll.

SharkLoader-only — do not merge with SynkLoader or other ETW filings (COMMON TECHNIQUE only). Prior separate IC3 IDs (no shared-operator claim): Rapuncel 208b747c6f7445f0af2b69a9d63acc36; Settra 631d8b4800d04bc19cdbfc6662e5c52c; RatHat f92c4c2f0dd3481f898fdd125e728adf; NodeRabbit dded86972e9347e0be27a6597b4cf08a; PollCat 98a4444754324e539dbbffcb10c70637; SynkLoader 3440d0c64dc240499ff66deaa3311a0b; Showboat db42033f319844c08ad103befebfca08; Abyssos a23f0a9d6799480e994284416d354713.

Repo: https://github.com/theworker02/emerging-threat-watch-1 Path: reports/law-enforcement/packages/09-sharkloader/ Primary freeze 2026-09-20. Local HTML SHA-256 c5af7fb5acf172632f63b9763e511d756564027cff5cf0ce8a6ffe2fa90934b2. No malware executed; no C2 contact; no binaries attached. Full CSV/dossier on request.
```

## 6. Technical details

*(4012 characters)*

```
=== PACKAGE ===
ETW-SHK-IC3 | SharkLoader / StrikeShark | PRIMARY-SOURCE: Kaspersky GReAT Securelist 2026-06-24
URL: https://securelist.com/strikeshark-campaign/120326/
Repo: https://github.com/theworker02/emerging-threat-watch-1
Path: reports/law-enforcement/packages/09-sharkloader/
CSV: 03_INDICATORS.csv (SHK-IND-0001 through SHK-IND-0019)
Local freeze SHA-256: c5af7fb5acf172632f63b9763e511d756564027cff5cf0ce8a6ffe2fa90934b2
Provenance: PRIMARY-SOURCE only. Independently observed by ETW: none. Live C2 contact: none.

=== MD5 (Kaspersky published) ===
C559CC68986933200FD5D9E4388E2F58  Installer
B3352B42432DEDC4A519F011DC8B5D5A  Dropper
24FCEBDEECBA65004FDB0923763D74FD  Dropper (Taiwan government entity chain; Chinese-filename pdf.exe lure)
9C872A0D5D5A38950E8B9AC9B488BE3F  SharkLoader DLL
AA3086BE652C8B20B0B29B2730D57119  SharkLoader DLL (SystemSettings.dll)
A514D1BB62D7916475946FE7C07AC0AA  Encrypted module DscCoreR.mui
9CBD560F820C95D7C38342CD558CB5C6  Encrypted module SyncRest.dat / SyncRes.dat
1F65544978B8EA0E745E573B8EE9684B  Dropper (Lebanon)

=== DOMAINS (Kaspersky published; defanged in article) ===
connect-microsoft.com
ms-record.com
ms-record.top
ms-tray.top
NOTE: PRIMARY-SOURCE infrastructure indicators only. ETW has not performed live C2 contact and does not assert current ownership or activity. No C2 IPv4 was published in the public Securelist IOC block transcribed by ETW.

=== FILENAMES / MODULES ===
SystemSettings.exe   Legitimate ImmersiveControlPanel binary abused for DLL sideload
SystemSettings.dll   Malicious SharkLoader main DLL
DscCoreR.mui         Encrypted module: Cobalt Strike Beacon + MinHook (Blowfish; MZ stripped)
SyncRes.dat          Encrypted Detours API-hook DLL (AES-128 key+IV in first 32 bytes; also SyncRest.dat)
Alternate sideload targets: msedge.dll; PrintDialog.dll; miracastview.dll
Other module/decoy names noted: GameInputInboxs32.mui; diagerr.xml; NtfsLog.etl; Ignored.Dat; VistaCompat.nls
Dropper lure names noted: GoogleUpdateStepup.exe; AnyConnect-win-4.10.04071-predeploy-k9exe; AutoUpdate.exe

=== PATHS / WORKING DIRECTORIES ===
%APPDATA%\xwreg
%APPDATA%\xgdf
%APPDATA%\reports\AnyConnect-win-4.msi (legitimate Cisco MSI decoy path in one dropper)
%TEMP%\aswerf\ (decoy PDF output path in some droppers)
C:\ProgramData\ (incl. vendor-named camouflage dirs such as KasperskyLab)
C:\Windows\ImmersiveControlPanel\SystemSettings.exe (legitimate binary source)

=== PERSISTENCE ===
HKCU\...\Run value "MFUpdate" -> SystemSettings.exe (Hong Kong incident)
Scheduled task \Microsoft\Windows\Edge\Edgeupdate -> SystemSettings.exe (Indonesia diplomatic incident)
Dropper-created tasks (examples): "OneDrive Standalone Update Task-..." and "MicrosoftUpdateTaskUser..." (5-minute persistence task retained; 1-second immediate-exec task removed after ~1.5s)

=== BEHAVIORAL SUMMARY (Kaspersky) ===
Exploit/webshell or dropper -> DLL sideload -> decrypt/load DscCoreR.mui -> decrypt/load SyncRes.dat -> Detours + MinHook (VirtualAlloc/Sleep) -> VEH for 0xC0000005 -> in-memory Cobalt Strike Beacon. Post-compromise recon includes AD enumeration (net group /domain; Get-ADGroupMember; dsquery/dsget). Public CVE examples cited by Kaspersky for opportunistic internet-facing access include Exchange/SharePoint/Openfire/Fortinet/Cisco/F5/Zimbra classes (PoC-available); ETW did not independently exploit or validate those CVEs.

=== NOT IN THIS CORPUS ===
No public SHA-256 sample hashes in Securelist IOC block (MD5s only). No invented Beacon hashes. No actor legal name/phone/email/address. No dollar loss claimed. No ETW malware execution or C2 probing.

=== RELATED SEPARATE IC3 IDS (no shared-operator claim) ===
Rapuncel 208b747c6f7445f0af2b69a9d63acc36
Settra 631d8b4800d04bc19cdbfc6662e5c52c
RatHat f92c4c2f0dd3481f898fdd125e728adf
NodeRabbit dded86972e9347e0be27a6597b4cf08a
PollCat 98a4444754324e539dbbffcb10c70637
SynkLoader 3440d0c64dc240499ff66deaa3311a0b
Showboat db42033f319844c08ad103befebfca08
Abyssos a23f0a9d6799480e994284416d354713
```

## 7. Witnesses

*(477 characters)*

```
No firsthand fact witnesses known to the reporter beyond the public Kaspersky GReAT / Securelist disclosure. Reporter did not observe the intrusion firsthand and did not interact with victims. Investigative contact for the public research is Kaspersky GReAT via the published Securelist article and Kaspersky Intelligence Reporting Service (intelreports@kaspersky.com) for extended IoCs. Emerging Threat Watch retained the public article freeze and transcribed indicators only.
```

## 8. Other agencies

*(426 characters)*

```
No prior report of this SharkLoader / StrikeShark package by the reporter to other law-enforcement agencies. Public research was published by Kaspersky GReAT (Securelist). Related separate Emerging Threat Watch IC3 filings (different families; no shared-operator claim) are listed in the description and technical details. This complaint is not an update to a previously filed SharkLoader complaint (first SharkLoader filing).
```

## 9. Other information

*(899 characters)*

```
Primary source: https://securelist.com/strikeshark-campaign/120326/ (Kaspersky GReAT, 2026-06-24).
Companion press: https://www.kaspersky.com/about/press-releases/kaspersky-warns-of-a-new-strikeshark-campaign-targeting-organizations-in-asia-latin-america-and-europe-with-advanced-malware
Research repository: https://github.com/theworker02/emerging-threat-watch-1
Package folder: reports/law-enforcement/packages/09-sharkloader/
Full structured dossier: IC3_FULL_PACKAGE.md
Machine-readable indicators: 03_INDICATORS.csv (19 SHK-IND rows)
Caveats: 05_CAVEATS_AND_LIMITS.md
Local HTML freeze SHA-256: c5af7fb5acf172632f63b9763e511d756564027cff5cf0ce8a6ffe2fa90934b2
Crime-type language: Malware; Unauthorized network intrusion / remote access.
Dollar loss: $0 / none claimed. Personal victimization: No.
Is this an update to a previously filed complaint?: No (first SharkLoader / ETW-SHK-IC3 filing).
```

## 10. Date range

```
Beginning: 2026-06-24 (Kaspersky public disclosure; earlier activity per Kaspersky telemetry — not independently dated by ETW)
Ending: ongoing / unknown
```

## 11. Update to previous complaint?

**No** — first SharkLoader / `ETW-SHK-IC3` filing.

## 12. Complainant contact

Paste from the **gitignored** local profile (do not commit PII):

`reports/law-enforcement/private/COMPLAINANT_PROFILE.md`

Per-package copy: `reports/law-enforcement/private/filing-helpers/<NN-family>/00_COMPLAINANT_CONTACT.md`

| Field | Source |
|-------|--------|
| Full legal name / phone / email / mailing address | `COMPLAINANT_PROFILE.md` (filled) |
| Filing capacity | Individual / researcher — defensive TI (Emerging Threat Watch) |
| Business victim? | No |
| Critical infrastructure disruption? | No / unknown |
| Personal victimization? | No |
| Total loss | 0 / None |
| SSN / DOB | **Do not enter** |

## After filing

Send the Submission ID (and timestamp) so it can be recorded on `main`.
