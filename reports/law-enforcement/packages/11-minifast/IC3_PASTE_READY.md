# MiniFast — IC3 Paste-Ready Pack (`ETW-MNF-IC3`)

**Status:** `PRIMARY_FROZEN` — **not filed** · ready for human filing  
**Portal:** https://www.ic3.gov/

Copy each section into the matching IC3 form field. Counts are under typical IC3 limits (description ≈3,500 · technical ≈5,000 · witnesses ≈1,000).

---

## 1. Subject line / title

```
Defensive TI referral — MiniFast / Nimbus Manticore (Check Point + Unit 42 2026) — ETW-MNF-IC3
```

## 2. Crime types

```
Malware; Unauthorized network intrusion / remote access; Spear phishing
```

## 3. Subject #1 fields

| Field | Value |
|-------|-------|
| Name | Unknown |
| Business | Unknown (MiniFast / Nimbus Manticore / Screening Serpens campaign) |
| Address / City / State / ZIP / Country | Unknown |
| Phone | Unknown |
| Email | Unknown |
| Website | getsqldeveloper.com; business-startup.org; business-startup.azurewebsites.net |
| IP address | Unknown (Azure Web App hostnames published; no standalone C2 IPv4 prioritized) |
| Notes | Author/operator NOT_ESTABLISHED; IRGC/Nimbus = vendor assessment only; do not merge with PollCat |

## 4. Financial / loss

| Field | Value |
|-------|-------|
| Total loss | **0** / None |
| Transactions | None / blank |
| Personal victimization | No |

## 5. Description (what happened)

*(2810 characters)*

```
I am reporting defensive threat-intelligence information concerning the MiniFast backdoor documented by Check Point Research (2026-05-22) in “Fast and Furious – Nimbus Manticore Operations During the Iranian Conflict,” with companion Unit 42 reporting on Screening Serpens / UNC1549 that tracks overlapping UpdateChecker.dll samples as MiniUpdate. Filing as Emerging Threat Watch package ETW-MNF-IC3 — defensive TI referral, not a personal victimization or dollar-loss claim.

Check Point describes MiniFast as a previously undocumented 64-bit Windows PE DLL (export CheckForUpdates / UpdateChecker.dll) delivered via AppDomain hijacking and a trojanized Zoom installer flow (Zoominstall64.zip), with persistence by hijacking ZoomUpdateTaskUser scheduled tasks. C2 uses JSON/HTTPS endpoints with Chrome UA impersonation and Azure Web App hosts; SEO-poisoned SQL Developer lure domain getsqldeveloper.com is also published. Nimbus Manticore / UNC1549 / IRGC-linked framing is vendor assessment only — ETW does not independently establish attribution.

Unit 42 publishes overlapping UpdateChecker.dll hashes under the MiniUpdate name and additional MiniJunk V2 sibling hashes under Screening Serpens. MiniJunk V2 rows are sibling-family context only and are not merged as MiniFast authorship. Do NOT merge this package with PollCat despite Azure/C2 structural notes (ASSOCIATION_ONLY).

INDICATORS (PRIMARY-SOURCE; full CSV MNF-IND-0001–0044 on request):
Representative SHA-256: 10fd541674adadfbba99b54280f7e59732746faf2b10ce68521866f737f1e46d; eee657ffdb2af8ed6412221e7d5fbf4f5742f2ac2c88f43f12db46af0697de71; 781605ce9d4a9869e846f6c9657d71437cb6240ab27ffbc4cd550c0e06996690; 2c214494fd0bad31473ca8adce78a4f50847876584571e66aadeae70827ec2dc; f08b17856616d66492a24dced27f788e235f35f42fa7cd10f315000d3a2f4c03. Domains include getsqldeveloper.com; business-startup.org; business-startup.azurewebsites.net; QuantumWeave.azurewebsites.net; ElementShift.azurewebsites.net. Host: UpdateChecker.dll; CheckForUpdates; ZoomUpdateTaskUser; Zoominstall64.zip; %LOCALAPPDATA%\Zoom\bin\update.

MiniFast-only — do not merge with PollCat or other ETW filings. Prior separate IC3 IDs (no shared-operator claim): Rapuncel 208b747c6f7445f0af2b69a9d63acc36; Settra 631d8b4800d04bc19cdbfc6662e5c52c; RatHat f92c4c2f0dd3481f898fdd125e728adf; NodeRabbit dded86972e9347e0be27a6597b4cf08a; PollCat 98a4444754324e539dbbffcb10c70637; SynkLoader 3440d0c64dc240499ff66deaa3311a0b; Showboat db42033f319844c08ad103befebfca08; Abyssos a23f0a9d6799480e994284416d354713; SharkLoader 6ed57963d0c64750aa14b6fcbaa2e576.

Repo: https://github.com/theworker02/emerging-threat-watch-1 Path: reports/law-enforcement/packages/11-minifast/ Primary freeze 2026-09-20. No malware executed; no C2 contact; no binaries attached. Full CSV/dossier on request.
```

## 6. Technical details

*(3784 characters)*

```
=== PACKAGE ===
ETW-MNF-IC3 | MiniFast | PRIMARY-SOURCE: Check Point Research + Unit 42 Screening Serpens
Check Point: https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/
Unit 42: https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/
Repo path: reports/law-enforcement/packages/11-minifast/
CSV: 03_INDICATORS.csv (MNF-IND-0001 through MNF-IND-0044)
Local freezes: PS-MNF-001 SHA-256 a3d4d4a8346aaef3b9af65ac6a6290da63e1d85cc961d4b8fca7b50b065e93e9; PS-MNF-002 SHA-256 019694ad7abd1ae0a2da9a9354bbad44cbc10a197586551e07bb36d3173e88c3
Provenance: PRIMARY-SOURCE only. Independently observed by ETW: none. Live C2 contact: none.

=== SHA256 (Check Point MiniFast / campaign samples — representative) ===
10fd541674adadfbba99b54280f7e59732746faf2b10ce68521866f737f1e46d
eee657ffdb2af8ed6412221e7d5fbf4f5742f2ac2c88f43f12db46af0697de71
781605ce9d4a9869e846f6c9657d71437cb6240ab27ffbc4cd550c0e06996690
2c214494fd0bad31473ca8adce78a4f50847876584571e66aadeae70827ec2dc
f08b17856616d66492a24dced27f788e235f35f42fa7cd10f315000d3a2f4c03
a57ffb819fe8d98ff925c5d7b239598fe302acf5a13193d7a535040a71298fdf
63d0d3c4a7f71bdbca720903d6a99b832089cc093c64d2938e7e001e56c17ab4
74882085db2088356ed7f72f01e0404a0a98cda88ef56fb15ce74c1f36b26d27
bc3b44154518c5794ce639108e7b9c5fecb0c189607a26de1aaed518d890c7ad
ecaf493c320d201d285ef5f61d75744216e47cf1115b4af528f9a78883cc446e
44f4f7aca7f1d9bfdaf7b3736934cbe19f851a707662f8f0b0c49b383e054250
0db36a04d304ad96f9e6f97b531934594cd95a5cea9ff2c9af249201089dc864

=== SHA256 (Unit 42 MiniUpdate / MiniJunk V2 companion — labeled in CSV) ===
332ba2f0297dfb1599adecc3e9067893e7cf243aa23aedce4906a4c480574c17
38bd137c672bd58d08c4f0502f993a6561e2c3411773d1ae57ee0151a0a9d11d
d4a7e9f107fe40c1a5d0139c6c6e25bf6bf57f61feff090bee28f476bb3cc3c2
9cf029daca89523d917dafed0568d11d00e45ec96b5b90b4a1f7fd4018c7da84
B19e06da580cf91691eda066ac9ee4b09c6e5dc26c367af12660fe1f9306eec4
8808c794c24367438f183e4be941876f1d3ecd0c8d2eb43b10d2380841d2283b
43dc62cef52ebdd69e79f10015b3e13890f26c058325c0ff139c70f8d8eadcfa
9e4a658e6d831c9e9bdfe11884a75b7c64812ed0a80e8495ddf6b316505acac1

=== DOMAINS (subset; full list in CSV) ===
business-startup.org
business-startup.azurewebsites.net
businessstartup.azurewebsites.net
buisness-centeral.azurewebsites.net
buisness-centeral-transportation.azurewebsites.net
buisness-centeral-transportation.com
licencemanagers.azurewebsites.net
licencesupporting.azurewebsites.net
peerdistsvcmanagers.azurewebsites.net
nanomatrix.azurewebsites.net
PremierHealthAdvisory.com
ramiltonsfinance.com
getsqldeveloper.com
QuantumWeave.azurewebsites.net
ElementShift.azurewebsites.net
ThemesManagers.azurewebsites.net
ThemesProviderManagers.azurewebsites.net
docspace-twpf0e.onlyoffice.com

=== HOST ARTIFACTS ===
UpdateChecker.dll | CheckForUpdates export
Zoominstall64.zip | Trojanized Zoom lure archive
ZoomUpdateTaskUser-* | Hijacked Zoom scheduled-task persistence prefix
%LOCALAPPDATA%\Zoom\bin\update | Staging path

=== NAMING NOTE ===
Check Point = MiniFast; Unit 42 = MiniUpdate for UpdateChecker.dll. MiniJunk V2 = sibling under Screening Serpens — not MiniFast merge.

=== NOT IN THIS CORPUS ===
No actor legal name. No dollar loss. No ETW malware execution/C2 probing. IRGC/Nimbus attribution = vendor only. Do not merge with PollCat.

=== RELATED SEPARATE IC3 IDS (no shared-operator claim) ===
Rapuncel 208b747c6f7445f0af2b69a9d63acc36
Settra 631d8b4800d04bc19cdbfc6662e5c52c
RatHat f92c4c2f0dd3481f898fdd125e728adf
NodeRabbit dded86972e9347e0be27a6597b4cf08a
PollCat 98a4444754324e539dbbffcb10c70637
SynkLoader 3440d0c64dc240499ff66deaa3311a0b
Showboat db42033f319844c08ad103befebfca08
Abyssos a23f0a9d6799480e994284416d354713
SharkLoader 6ed57963d0c64750aa14b6fcbaa2e576
```

## 7. Witnesses

*(385 characters)*

```
No firsthand fact witnesses known to the reporter beyond the public Check Point Research and Unit 42 disclosures. Reporter did not observe the intrusion firsthand and did not interact with victims. Investigative contact for the public research is via the published Check Point and Unit 42 articles. Emerging Threat Watch retained public article freezes and transcribed indicators only.
```

## 8. Other agencies

*(407 characters)*

```
No prior report of this MiniFast package by the reporter to other law-enforcement agencies. Public research was published by Check Point Research and Unit 42. Related separate Emerging Threat Watch IC3 filings (different families; no shared-operator claim) are listed in the description and technical details. This complaint is not an update to a previously filed MiniFast complaint (first MiniFast filing).
```

## 9. Other information

*(776 characters)*

```
Primary sources:
https://research.checkpoint.com/2026/fast-and-furious-nimbus-manticore-operations-during-the-iranian-conflict/
https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/
Secondary: CyberVeille (FR); The Hacker News.
Research repository: https://github.com/theworker02/emerging-threat-watch-1
Package folder: reports/law-enforcement/packages/11-minifast/
Full structured dossier: IC3_FULL_PACKAGE.md
Machine-readable indicators: 03_INDICATORS.csv (44 MNF-IND rows)
Caveats: 05_CAVEATS_AND_LIMITS.md
Crime-type language: Malware; Unauthorized network intrusion / remote access; Spear phishing.
Dollar loss: $0 / none claimed. Personal victimization: No.
Is this an update to a previously filed complaint?: No (first MiniFast / ETW-MNF-IC3 filing).
```

## 10. Date range

```
Beginning: 2026-02/2026-04 (campaign waves per Check Point / Unit 42); public disclosure 2026-05
Ending: ongoing / unknown
```

## 11. Update to previous complaint?

**No** — first MiniFast / `ETW-MNF-IC3` filing.

## 12. Complainant contact

Use **your** real name, phone, email, and mailing address (IC3 required). Do not enter SSN/DOB.

## After filing

Send the Submission ID (and timestamp) so it can be recorded on `main`.
