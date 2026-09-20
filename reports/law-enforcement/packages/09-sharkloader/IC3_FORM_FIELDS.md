# SharkLoader — Complete IC3 Form Field Map

**Package:** `ETW-SHK-IC3`  
**Portal:** https://www.ic3.gov/ → complaint form  
**Rule:** Human files only. Never auto-submit. One family = one complaint.  
**Limits (typical):** Description ≈ 3,500 chars · Technical details ≈ 5,000 chars · Witnesses ≈ 1,000 chars

Character counts for pastes below (verify before submit):
- Description: 4643 chars
- Technical details: 3770 chars
- Witnesses: 478 chars
- Other agencies: 427 chars
- Other information: 900 chars

---

## Step — Complainant / filing identity (you fill personal contact)

| Field | Suggested content |
|-------|-------------------|
| Filing capacity | Individual / researcher filing defensive TI (or “on behalf of” if applicable to your situation) |
| Your name / phone / email / address | **Your real contact info** (required by IC3) |
| Business victim? | No — this is not a claim that your business was breached by SharkLoader |
| Critical infrastructure disruption? | No / unknown — reporter is referring public research, not an active IR engagement |
| SSN / DOB | **Do not enter** (IC3 instructs not to) |

---

## Step — Financial transactions / loss

| Field | Paste / value |
|-------|----------------|
| Total loss to complainant | **0** / None |
| Transaction rows | **None** — leave blank |
| Payment type / wallets / accounts | **None** |
| Notes | Defensive TI referral only. No personal or business dollar loss is claimed in package ETW-SHK-IC3. |

---

## Step — Subject #1 (unknown operator / campaign infrastructure)

| Field | Paste |
|-------|-------|
| Name | Unknown |
| Business / organization name | Unknown (campaign tracked by Kaspersky as **StrikeShark**; malware family **SharkLoader**) |
| Address | Unknown / blank |
| City / State / ZIP / Country | Unknown / blank · Country: Unknown |
| Phone | Unknown / blank |
| Email | Unknown / blank |
| Website | connect-microsoft.com; ms-record.com; ms-record.top; ms-tray.top |
| IP address | Unknown / blank (public Securelist IOC block published domains + MD5s; no C2 IPv4 in the public IOC appendix transcribed by ETW) |
| Additional subject notes | Operator legal identity **NOT_ESTABLISHED**. Kaspersky does not attribute StrikeShark to a known APT with high confidence. Low-confidence “Chinese-speaking” press framing is vendor assessment only — not independently established by Emerging Threat Watch. |

(Add Subject #2+ only if you personally have separate confirmed identities — ETW package does not.)

---

## Step — Describe what happened (complaint description)

**One-line subject / title if asked separately:**
```
Defensive TI referral — SharkLoader / StrikeShark (Kaspersky Securelist 2026-06-24) — ETW-SHK-IC3
```

**Crime-type language:**
```
Malware; Unauthorized network intrusion / remote access
```

**Date range (approx):**
```
Beginning: 2026-06-24 (Kaspersky public disclosure; activity observed by Kaspersky prior — exact first-seen per victim not established by ETW)
Ending: ongoing / unknown (Kaspersky: campaign broader than initially identified; ETW has no independent end date)
```

**Paste full description from `01_NARRATIVE_PASTE.txt`:**

```
I am reporting defensive threat-intelligence information concerning the SharkLoader malware documented by Kaspersky GReAT on June 24, 2026 in the Securelist article “StrikeShark: investigating a new campaign delivering Cobalt Strike through SharkLoader” (https://securelist.com/strikeshark-campaign/120326/). I am filing SharkLoader as a separate complaint under Emerging Threat Watch package ETW-SHK-IC3. This is a defensive threat-intelligence referral, not a personal victimization or dollar-loss claim.

Kaspersky describes SharkLoader as a previously undocumented multi-component custom loader used in an intrusion cluster Kaspersky tracks as StrikeShark. SharkLoader’s role is to deploy Cobalt Strike Beacon on compromised Windows systems. Kaspersky reports initial access through exploitation of internet-facing applications (including Microsoft Exchange, Microsoft SharePoint, and Openfire Server) and through malware-based droppers. Confirmed victim sectors/regions in Kaspersky’s public reporting include diplomatic entities (Indonesia), government agencies (Taiwan), and software-development and other organizations in Hong Kong, Lebanon, Syria, Colombia, North Macedonia, Nepal, and Serbia.

Kaspersky’s infection chain commonly abuses legitimate Windows binaries for DLL sideloading. A frequently observed pattern copies SystemSettings.exe from C:\Windows\ImmersiveControlPanel into a writable directory (examples include C:\ProgramData\ or %APPDATA%\xwreg / %APPDATA%\xgdf) and executes it alongside a malicious SystemSettings.dll (SharkLoader). Encrypted companion modules include DscCoreR.mui (contains embedded Cobalt Strike Beacon material and MinHook) and SyncRes.dat / SyncRest.dat (Detours-based API hooks). Kaspersky documents Perfect DLL Hijacking / loader-lock escape, Blowfish decryption of DscCoreR.mui, AES-128 decryption of SyncRes.dat, reflective PE loading, ETW-related evasion hooks, PPID spoofing, and memory-permission flipping during Beacon sleep. Persistence observed in incidents includes HKCU Run value “MFUpdate” launching SystemSettings.exe and scheduled task “\Microsoft\Windows\Edge\Edgeupdate”.

Kaspersky does not attribute StrikeShark to a known APT group with high confidence. A low-confidence “Chinese-speaking” assessment appears in Kaspersky press framing; Emerging Threat Watch does not independently establish operator identity. Author / operator identity remains NOT_ESTABLISHED. Cobalt Strike Beacon sample hashes are not transcribed in this package unless published as SharkLoader-specific artifacts — do not invent Beacon hashes.

INDICATORS RETAINED (PRIMARY-SOURCE from Kaspersky Securelist; full CSV SHK-IND-0001–0019 available on request):
MD5: C559CC68986933200FD5D9E4388E2F58 (Installer); B3352B42432DEDC4A519F011DC8B5D5A (Dropper); 24FCEBDEECBA65004FDB0923763D74FD (Dropper, Taiwan gov chain); 9C872A0D5D5A38950E8B9AC9B488BE3F (SharkLoader DLL); AA3086BE652C8B20B0B29B2730D57119 (SystemSettings.dll); A514D1BB62D7916475946FE7C07AC0AA (DscCoreR.mui); 9CBD560F820C95D7C38342CD558CB5C6 (SyncRest.dat); 1F65544978B8EA0E745E573B8EE9684B (Dropper, Lebanon).
Domains: connect-microsoft.com; ms-record.com; ms-record.top; ms-tray.top.
Host artifacts: SystemSettings.dll; DscCoreR.mui; SyncRes.dat; %APPDATA%\xwreg; %APPDATA%\xgdf; Run key MFUpdate; scheduled task \Microsoft\Windows\Edge\Edgeupdate.
Alternate sideload DLL names also noted by Kaspersky: msedge.dll; PrintDialog.dll; miracastview.dll.

This package is SharkLoader / StrikeShark only. Do not merge with SynkLoader or other ETW loader filings (COMMON TECHNIQUE class only). Separate prior ETW IC3 filings (no shared-operator claim): Rapuncel 208b747c6f7445f0af2b69a9d63acc36; Settra 631d8b4800d04bc19cdbfc6662e5c52c; RatHat f92c4c2f0dd3481f898fdd125e728adf; NodeRabbit dded86972e9347e0be27a6597b4cf08a; PollCat 98a4444754324e539dbbffcb10c70637; SynkLoader 3440d0c64dc240499ff66deaa3311a0b; Showboat db42033f319844c08ad103befebfca08; Abyssos a23f0a9d6799480e994284416d354713.

Repository: https://github.com/theworker02/emerging-threat-watch-1
Package path: reports/law-enforcement/packages/09-sharkloader/ (see IC3_FULL_PACKAGE.md and 03_INDICATORS.csv).
Primary freeze: 2026-09-20. Local archive: evidence/primary-sources/sharkloader/securelist-strikeshark-2026-06-24.html (SHA-256 c5af7fb5acf172632f63b9763e511d756564027cff5cf0ce8a6ffe2fa90934b2).
I have retained the public research and indicator records offline. I have not executed malware samples and have not contacted suspected command-and-control systems. No malware binaries are attached to this IC3 web form. Full CSV/dossier available to investigators on request.
```

---

## Step — Other Information / Technical Details

**Paste technical details from `02_TECHNICAL_DETAILS_PASTE.txt`:**

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

=== DOMAINS (Kaspersky published; defanged in article as connect-microsoft[.]com etc.) ===
connect-microsoft.com
ms-record.com
ms-record.top
ms-tray.top
NOTE: These are PRIMARY-SOURCE infrastructure indicators. ETW has not performed live C2 contact and does not assert current ownership or activity.

=== FILENAMES / MODULES ===
SystemSettings.exe   Legitimate Windows ImmersiveControlPanel binary abused for DLL sideload
SystemSettings.dll   Malicious SharkLoader main DLL
DscCoreR.mui         Encrypted module: Cobalt Strike Beacon + MinHook (Blowfish-encrypted PE; MZ stripped)
SyncRes.dat          Encrypted Detours API-hook DLL (AES-128 key+IV in first 32 bytes; also named SyncRest.dat in sample table)
Alternate sideload targets noted: msedge.dll; PrintDialog.dll; miracastview.dll
Other encrypted/companion names noted in report: GameInputInboxs32.mui; diagerr.xml; NtfsLog.etl; Ignored.Dat; VistaCompat.nls

=== PATHS / WORKING DIRECTORIES ===
%APPDATA%\xwreg
%APPDATA%\xgdf
C:\ProgramData\ (and vendor-named subdirs such as KasperskyLab used as camouflage in some incidents)
C:\Windows\ImmersiveControlPanel\SystemSettings.exe  (source of legitimate binary copy)

=== PERSISTENCE ===
HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run  value "MFUpdate" -> SystemSettings.exe under AppData\Identities (Hong Kong incident)
Scheduled task: \Microsoft\Windows\Edge\Edgeupdate  -> SystemSettings.exe (Indonesia diplomatic incident; daily)

=== BEHAVIORAL / PROTOCOL SUMMARY (Kaspersky) ===
DLL sideloading -> decrypt/load DscCoreR.mui -> decrypt/load SyncRes.dat -> Detours API hooks + MinHook on VirtualAlloc/Sleep -> VEH for 0xC0000005 -> suspended thread + zlib MinHook + in-memory Cobalt Strike Beacon execution.
Post-compromise recon commands observed in incident telemetry include AD enumeration (net group /domain; Get-ADGroupMember; dsquery/dsget) and credential-oriented follow-on — still under vendor investigation for espionage/information-gathering objectives.

=== WHAT IS NOT IN THIS CORPUS ===
No SHA-256 sample hashes published in the public Securelist IOC block (MD5s only).
No Cobalt Strike Beacon hashes invented by ETW.
No actor legal name, phone, email, or residential address established.
No dollar loss claimed by reporter.
No ETW live malware execution or C2 probing.

=== RELATED SEPARATE IC3 SUBMISSION IDS (no shared-operator claim) ===
Rapuncel 208b747c6f7445f0af2b69a9d63acc36
Settra 631d8b4800d04bc19cdbfc6662e5c52c
RatHat f92c4c2f0dd3481f898fdd125e728adf
NodeRabbit dded86972e9347e0be27a6597b4cf08a
PollCat 98a4444754324e539dbbffcb10c70637
SynkLoader 3440d0c64dc240499ff66deaa3311a0b
Showboat db42033f319844c08ad103befebfca08
Abyssos a23f0a9d6799480e994284416d354713
```

---

## Step — Witnesses

```
No firsthand fact witnesses known to the reporter beyond the public Kaspersky GReAT / Securelist disclosure. Reporter did not observe the intrusion firsthand and did not interact with victims. Investigative contact for the public research is Kaspersky GReAT via the published Securelist article and Kaspersky Intelligence Reporting Service (intelreports@kaspersky.com) for extended IoCs. Emerging Threat Watch retained the public article freeze and transcribed indicators only.
```

---

## Step — Other agencies / prior reports

```
No prior report of this SharkLoader / StrikeShark package by the reporter to other law-enforcement agencies. Public research was published by Kaspersky GReAT (Securelist). Related separate Emerging Threat Watch IC3 filings (different families; no shared-operator claim) are listed in the description and technical details. This complaint is not an update to a previously filed SharkLoader complaint (first SharkLoader filing).
```

---

## Step — Additional / Other information (if a separate box)

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

---

## Step — Update to previous complaint?

| Field | Value |
|-------|-------|
| Is this an update to a previously filed complaint? | **No** |
| Prior Submission ID for SharkLoader | None (first ETW-SHK-IC3 filing) |
| Related separate family IDs | Listed in description/tech (do **not** treat as the same complaint) |

---

## Integrity gate (must be true before submit)

- [ ] SharkLoader only — SynkLoader / other loaders not merged
- [ ] Language is “Kaspersky reports” / “I retained” — not “I discovered SharkLoader”
- [ ] No dollar loss / victim names invented
- [ ] No malware binary attached
- [ ] No C2 probing performed
- [ ] No invented Cobalt Strike Beacon hashes
- [ ] `05_CAVEATS_AND_LIMITS.md` accepted
- [ ] Character counts within form limits

## After submit

1. Save confirmation / Submission ID screenshot.
2. Reply with the Submission ID (and EST timestamp if shown).
3. Maintainer will record `IC3_FILING_RECORD.md` + `MASTER_INDEX.csv` on **main**.
