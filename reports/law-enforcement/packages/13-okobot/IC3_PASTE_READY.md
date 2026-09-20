# Okobot — IC3 Paste-Ready Pack (`ETW-OKO-IC3`)

**Status:** `PRIMARY_FROZEN` — **not filed** · ready for human filing  
**Portal:** https://www.ic3.gov/

Copy each section into the matching IC3 form field. Counts are under typical IC3 limits (description ≈3,500 · technical ≈5,000 · witnesses ≈1,000).

---

## 1. Subject line / title

```
Defensive TI referral — Okobot / OkoSpyware / TookPS (Kaspersky + Gridinsoft 2026) — ETW-OKO-IC3
```

## 2. Crime types

```
Malware; Unauthorized network intrusion / remote access; Credential theft; Cryptocurrency theft
```

## 3. Subject #1 fields

| Field | Value |
|-------|-------|
| Name | Unknown |
| Business | Unknown (OkoBot / TookPS cryptocurrency-theft framework) |
| Address / City / State / ZIP / Country | Unknown |
| Phone | Unknown |
| Email | Unknown |
| Website | 22tuk.digital; moonsand.store; 2baserec2.guru; recavb22.online |
| IP address | 104.243.43.16; 104.243.32.213; 62.210.188.209 |
| Notes | Author/operator NOT_ESTABLISHED; Russian-speaking signals = Kaspersky assessment only |

## 4. Financial / loss

| Field | Value |
|-------|-------|
| Total loss | **0** / None |
| Transactions | None / blank |
| Personal victimization | No |

## 5. Description (what happened)

*(2559 characters)*

```
I am reporting defensive threat-intelligence information concerning the OkoBot framework documented by Kaspersky GReAT on Securelist, with Kaspersky press and a Gridinsoft companion that publishes a previously unpublished TookPS callback. Filing as Emerging Threat Watch package ETW-OKO-IC3 — defensive TI referral, not a personal victimization or dollar-loss claim.

Kaspersky describes OkoBot as a multi-stage Windows framework (≥20 payloads) initiated via TookPS PowerShell, configuring an SSH bot and dispatching modules including OkoSpyware (window video + keylogging of crypto wallets/password managers), SeedHunter (hardware-wallet seed phishing overlays for Trezor/Ledger apps), MC Keylogger, and Chromium extension loaders (e.g., Rilide). Victims across 25+ countries; activity ongoing as of publication. Russian-speaking crimeware signals noted by Kaspersky — author identity remains NOT_ESTABLISHED by ETW. Rilide commodity stealer is not treated as OkoBot authorship proof.

Gridinsoft publishes high-confidence TookPS callback 22tuk.digital/online/took.php and scheduled task \GDrive Backup Sync, correlated to previously documented TookPS domains and OkoBot SSH destinations.

INDICATORS (PRIMARY-SOURCE; full CSV OKO-IND-0001–0033 on request):
MD5s (representative): B07D451EE65A1580F20A784C8F0E7A46; 187A1F68AE786E53D3831166DC84E6D2; D84E8DC509308523E0209D3CD3544619; 83E6B8FCB92A0B13E109301F8FF649CF; 7306885BB4C98F2A9F056104CF092BC9; B4C2E16CDB513BE4DC798F88E2527334. Domains: 2baserec2.guru; recavb22.online; kbeautyreviews.com; coffeesaloon.online; livewallpapers.online; thatwascringe.com; moonsand.store; 22tuk.digital. IPs: 104.243.43.16; 104.243.32.213; 62.210.188.209. Paths: %PROGRAMDATA%\HDVideo\HDUtil.exe; %PROGRAMDATA%\hwid.dat; %PROGRAMDATA%\oko_ver; %USERPROFILE%\.ssh\go.bat; ir-post.php; \GDrive Backup Sync.

Okobot-only — do not merge with other ETW filings. Prior separate IC3 IDs (no shared-operator claim): Rapuncel 208b747c6f7445f0af2b69a9d63acc36; Settra 631d8b4800d04bc19cdbfc6662e5c52c; RatHat f92c4c2f0dd3481f898fdd125e728adf; NodeRabbit dded86972e9347e0be27a6597b4cf08a; PollCat 98a4444754324e539dbbffcb10c70637; SynkLoader 3440d0c64dc240499ff66deaa3311a0b; Showboat db42033f319844c08ad103befebfca08; Abyssos a23f0a9d6799480e994284416d354713; SharkLoader 6ed57963d0c64750aa14b6fcbaa2e576.

Repo: https://github.com/theworker02/emerging-threat-watch-1 Path: reports/law-enforcement/packages/13-okobot/ Primary freeze 2026-09-20. No malware executed; no C2 contact; no binaries attached. Full CSV/dossier on request.
```

## 6. Technical details

*(2475 characters)*

```
=== PACKAGE ===
ETW-OKO-IC3 | Okobot / OkoSpyware / TookPS | PRIMARY-SOURCE: Kaspersky Securelist + Gridinsoft
Securelist: https://securelist.com/okobot-framework-targets-cryptocurrency-wallets/120660/
Gridinsoft: https://blog.gridinsoft.com/okobot-seed-phrase-malware/
Repo path: reports/law-enforcement/packages/13-okobot/
CSV: 03_INDICATORS.csv (OKO-IND-0001 through OKO-IND-0033)
Local freezes: PS-OKO-001 SHA-256 04eb0610ddb6e36d4cb0c12917e90424741162b091b87426a5c4c3cc1bf431ec; PS-OKO-003 SHA-256 87af53222778a4d2436648fa387b7d7e25b5e530e681867f63fdbac0fd9eab5d
Provenance: PRIMARY-SOURCE only. Independently observed by ETW: none. Live C2 contact: none.

=== MD5 (Kaspersky public) ===
B07D451EE65A1580F20A784C8F0E7A46
187A1F68AE786E53D3831166DC84E6D2
D84E8DC509308523E0209D3CD3544619
83E6B8FCB92A0B13E109301F8FF649CF
7306885BB4C98F2A9F056104CF092BC9
B4C2E16CDB513BE4DC798F88E2527334
2157D2429124AD28DB7A26F2477CB985
77CECF5E2A622AE07D8AE9913457AB57
E0C3BC27A65750E740C4F1719E531C7D
3D2B43F91F65BFBF36A9C71B6B418876
70FEF9FD6E351F4D53CFEEE8DCDFCD99
ACD31C9941B6C1CABD4E45E6877B9038
DD52F5108A176C62AD807C327734AD12
AC93A821617AEA1F56D4BC0BEF4AF327
11DBC8A2BEA04B15F8F68F3F01E8FAF9

=== DOMAINS ===
2baserec2.guru
recavb22.online
kbeautyreviews.com
coffeesaloon.online
livewallpapers.online
thatwascringe.com
moonsand.store
22tuk.digital

=== IPV4 (SSH bot infra) ===
104.243.43.16
104.243.32.213
62.210.188.209

=== URL / TASK ===
https://22tuk.digital/online/took.php
\GDrive Backup Sync

=== PATHS / ARTIFACTS ===
%PROGRAMDATA%\HDVideo\HDUtil.exe
%PROGRAMDATA%\hwid.dat
%PROGRAMDATA%\oko_ver
%USERPROFILE%\.ssh\go.bat
ir-post.php

=== BEHAVIORAL SUMMARY ===
TookPS → SSH tunnel bot → modular plugin dispatcher (Volume2/protobuf|version.dll) → SeedHunter / OkoSpyware / keylogger / browser-extension injector. Crypto-wallet / seed-phrase theft focus per Kaspersky.

=== NOT IN THIS CORPUS ===
No actor legal name. No dollar loss. No ETW malware execution/C2 probing. Extended IoCs behind Kaspersky TI service not invented here.

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

*(470 characters)*

```
No firsthand fact witnesses known to the reporter beyond the public Kaspersky GReAT / Securelist and Gridinsoft disclosures. Reporter did not observe infections firsthand and did not interact with victims. Investigative contact for the public research is via the published Securelist article (and Kaspersky Intelligence Reporting Service for extended IoCs if needed) plus Gridinsoft. Emerging Threat Watch retained public article freezes and transcribed indicators only.
```

## 8. Other agencies

*(399 characters)*

```
No prior report of this Okobot package by the reporter to other law-enforcement agencies. Public research was published by Kaspersky GReAT and Gridinsoft. Related separate Emerging Threat Watch IC3 filings (different families; no shared-operator claim) are listed in the description and technical details. This complaint is not an update to a previously filed Okobot complaint (first Okobot filing).
```

## 9. Other information

*(896 characters)*

```
Primary sources:
https://securelist.com/okobot-framework-targets-cryptocurrency-wallets/120660/
https://blog.gridinsoft.com/okobot-seed-phrase-malware/
https://www.kaspersky.com/about/press-releases/kaspersky-reveals-a-new-malicious-framework-targeting-cryptocurrency-users-with-the-use-of-okospyware
Secondary: The Hacker News; BleepingComputer.
Research repository: https://github.com/theworker02/emerging-threat-watch-1
Package folder: reports/law-enforcement/packages/13-okobot/
Full structured dossier: IC3_FULL_PACKAGE.md
Machine-readable indicators: 03_INDICATORS.csv (33 OKO-IND rows)
Caveats: 05_CAVEATS_AND_LIMITS.md
Crime-type language: Malware; Unauthorized network intrusion / remote access; Credential theft; Cryptocurrency theft.
Dollar loss: $0 / none claimed. Personal victimization: No.
Is this an update to a previously filed complaint?: No (first Okobot / ETW-OKO-IC3 filing).
```

## 10. Date range

```
Beginning: TookPS activity from ~2025-03 per Kaspersky; OkoBot framework documented 2026; Gridinsoft callback ongoing as of publication
Ending: ongoing / unknown
```

## 11. Update to previous complaint?

**No** — first Okobot / `ETW-OKO-IC3` filing.

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
