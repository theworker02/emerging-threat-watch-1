# StarlandRAT — IC3 Paste-Ready Pack (`ETW-STR-IC3`)

**Status:** `PRIMARY_FROZEN` — **not filed** · ready for human filing  
**Portal:** https://www.ic3.gov/

Copy each section into the matching IC3 form field. Counts are under typical IC3 limits (description ≈3,500 · technical ≈5,000 · witnesses ≈1,000).

---

## 1. Subject line / title

```
Defensive TI referral — Starland RAT / WLDR / UAT-11795 (Cisco Talos 2026-07) — ETW-STR-IC3
```

## 2. Crime types

```
Malware; Unauthorized network intrusion / remote access; Credential theft; Cryptocurrency theft; Social engineering
```

## 3. Subject #1 fields

| Field | Value |
|-------|-------|
| Name | Unknown |
| Business | Unknown (UAT-11795 / Starland RAT / WLDR campaign) |
| Address / City / State / ZIP / Country | Unknown |
| Phone | Unknown |
| Email | Unknown |
| Website | windowscreenrepairnearme.com; aipythondevs.com; eorthopaedics.com; web-devtools.com; zynaris.io |
| IP address | 104.248.233.104; 192.81.216.250; 74.114.119.201; 178.255.126.39; 193.149.176.254; 185.238.191.234 |
| Notes | Author/operator NOT_ESTABLISHED; UAT-11795 Russian-speaking financially motivated = Talos assessment only |

## 4. Financial / loss

| Field | Value |
|-------|-------|
| Total loss | **0** / None |
| Transactions | None / blank |
| Personal victimization | No |

## 5. Description (what happened)

*(2362 characters)*

```
I am reporting defensive threat-intelligence information concerning Starland RAT and the companion WLDR PowerShell C2 agent documented by Cisco Talos as UAT-11795 (July 2026), including the official Talos IOC appendix with sample SHA-256s. Filing as Emerging Threat Watch package ETW-STR-IC3 — defensive TI referral, not a personal victimization or dollar-loss claim.

Talos describes a financially motivated, Russian-speaking actor (vendor assessment only) delivering trojanized installers (MobaXterm, WebEx, Zoom, DBeaver, FACEIT) and ClickFix/HTA staging that loads a Python-based Starland RAT in memory (LICENSE.txt / pythonw.exe) with crypto-wallet recon, Telegram bots, and Polygon smart-contract fallback C2, plus optional CastleStealer/Remcos follow-ons and the in-memory WLDR PowerShell agent. Author identity remains NOT_ESTABLISHED by ETW. UAT-11795 Russian-speaking financially motivated framing is Talos assessment only.

INDICATORS (PRIMARY-SOURCE; full CSV STR-IND-0001–0035 on request):
Domains: eorthopaedics.com; sastoro.com; web-devtools.com; zynaris.io; windowscreenrepairnearme.com; aipythondevs.com; alphabitcapital.info. IPs: 104.248.233.104; 192.81.216.250; 74.114.119.201; 178.255.126.39; 193.149.176.254; 185.238.191.234. Sample SHA-256: 162e436f18fe6099c57855c8d63fd747493624e87702dc749b242eb9a6b758ca (Starland RAT); d52540621dec5ed56cac8532f0e4fe10a7575c3e17e984f59646909fa587dd35 (WLDR); 47dedb08385449d48d8b6543030310317c92cddafa25e14ee0cb9a32d53ced5c (Python_Loader). Polygon contract 0x6ae382ed2154cc84c6672e4e908cd2c69c1b35ba; polygon-rpc.com. Host: LICENSE.txt; PythonLauncher-*; odg5t8mvssvh; helo1.

StarlandRAT-only — do not merge with other ETW filings. Prior separate IC3 IDs (no shared-operator claim): Rapuncel 208b747c6f7445f0af2b69a9d63acc36; Settra 631d8b4800d04bc19cdbfc6662e5c52c; RatHat f92c4c2f0dd3481f898fdd125e728adf; NodeRabbit dded86972e9347e0be27a6597b4cf08a; PollCat 98a4444754324e539dbbffcb10c70637; SynkLoader 3440d0c64dc240499ff66deaa3311a0b; Showboat db42033f319844c08ad103befebfca08; Abyssos a23f0a9d6799480e994284416d354713; SharkLoader 6ed57963d0c64750aa14b6fcbaa2e576.

Repo: https://github.com/theworker02/emerging-threat-watch-1 Path: reports/law-enforcement/packages/15-starlandrat/ Primary freeze 2026-09-20. No malware executed; no C2 contact; no binaries attached. Full CSV/dossier on request.
```

## 6. Technical details

*(2837 characters)*

```
=== PACKAGE ===
ETW-STR-IC3 | Starland RAT + WLDR | PRIMARY-SOURCE: Cisco Talos UAT-11795 + IOC appendix
Blog: https://blog.talosintelligence.com/uat-11795-deploys-novel-starland-rat-and-bespoke-wldr-c2-implant-in-financially-motivated-campaign/
IOC file: https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/07/new-starland-rat-and-WLDR-implant-campaign.txt
Repo path: reports/law-enforcement/packages/15-starlandrat/
CSV: 03_INDICATORS.csv (STR-IND-0001 through STR-IND-0035)
Local freezes: PS-STR-001 SHA-256 0eff5ee5f2e32d8cc50ea58a9a4f6bf94b4919a9f997112d88f199e6a735eb84; PS-STR-002 SHA-256 af756bf25110749ddcb27cea532c2fb4274e1f0945587b892cb559d38e34ac5a
Provenance: PRIMARY-SOURCE only. Independently observed by ETW: none. Live C2 contact: none.

=== SHA256 (Talos IOC appendix — key samples) ===
162e436f18fe6099c57855c8d63fd747493624e87702dc749b242eb9a6b758ca
d52540621dec5ed56cac8532f0e4fe10a7575c3e17e984f59646909fa587dd35
47dedb08385449d48d8b6543030310317c92cddafa25e14ee0cb9a32d53ced5c
6ca7a458985350ac082a9c9820d7f8d39128a4c4bda2f5d32f169a45b7b22bc6
6ae334ce60d1a9b7fb96d1d0d0eda5ec7c2c31d3f0cf3e4d7e3056504d50043d
f4491736743a16f1278b8ba01649ee93343764e35ae5e1c0d5e0c0e1d7e32c14
896185a89bd7eb0520b03fdcfb8db0be98b43cf15f14041d73b23d3988c1bcab
a1835d333ac3db961a8ff1f4864e3c10a6f73a872c040599091390a009ac7804
2a27b3415114b874da295c19cce5227a8b8d9525cc2da331034a1f45528eecae
17e41d66ebfd56edc960f58f4285697ceceaa812514bb15092672c747979896e

=== DOMAINS ===
eorthopaedics.com
sastoro.com
web-devtools.com
zynaris.io
windowscreenrepairnearme.com
aipythondevs.com
polygon-rpc.com
alphabitcapital.info
niggerdemon.in

=== IPV4 ===
104.248.233.104
192.81.216.250
74.114.119.201
178.255.126.39
193.149.176.254
185.238.191.234

=== CRYPTO / HOST ARTIFACTS ===
0x6ae382ed2154cc84c6672e4e908cd2c69c1b35ba
odg5t8mvssvh
helo1
$m7*rYpry3
f2j398fj239d8j23dkkskskkkkkkkkk
LICENSE.txt
skuefq_bot
komandastuk_bot
stuk komanda
PythonLauncher

=== BEHAVIORAL SUMMARY ===
ClickFix/HTA or trojanized NSIS installer → pythonw.exe + LICENSE.txt loader → Starland RAT in memory (wallet recon, shellcode, optional CastleStealer/Remcos) → optional WLDR PowerShell memory C2 with HWID-bound encrypted beaconing; Polygon eth_call fallback C2 resolver.

=== NOT IN THIS CORPUS ===
No actor legal name. No dollar loss. No ETW malware execution/C2 probing. UAT-11795 attribution = Talos assessment only.

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

*(365 characters)*

```
No firsthand fact witnesses known to the reporter beyond the public Cisco Talos disclosure. Reporter did not observe infections firsthand and did not interact with victims. Investigative contact for the public research is Cisco Talos via the published blog and IOC appendix. Emerging Threat Watch retained public article/IOC freezes and transcribed indicators only.
```

## 8. Other agencies

*(395 characters)*

```
No prior report of this StarlandRAT package by the reporter to other law-enforcement agencies. Public research was published by Cisco Talos. Related separate Emerging Threat Watch IC3 filings (different families; no shared-operator claim) are listed in the description and technical details. This complaint is not an update to a previously filed StarlandRAT complaint (first StarlandRAT filing).
```

## 9. Other information

*(889 characters)*

```
Primary sources:
https://blog.talosintelligence.com/uat-11795-deploys-novel-starland-rat-and-bespoke-wldr-c2-implant-in-financially-motivated-campaign/
https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/07/new-starland-rat-and-WLDR-implant-campaign.txt
Secondary: BleepingComputer; Security Affairs.
Research repository: https://github.com/theworker02/emerging-threat-watch-1
Package folder: reports/law-enforcement/packages/15-starlandrat/
Full structured dossier: IC3_FULL_PACKAGE.md
Machine-readable indicators: 03_INDICATORS.csv (35 STR-IND rows)
Caveats: 05_CAVEATS_AND_LIMITS.md
Crime-type language: Malware; Unauthorized network intrusion / remote access; Credential theft; Cryptocurrency theft; Social engineering.
Dollar loss: $0 / none claimed. Personal victimization: No.
Is this an update to a previously filed complaint?: No (first StarlandRAT / ETW-STR-IC3 filing).
```

## 10. Date range

```
Beginning: Talos tracks activity since at least 2025-06; public disclosure 2026-07-16
Ending: ongoing / unknown
```

## 11. Update to previous complaint?

**No** — first StarlandRAT / `ETW-STR-IC3` filing.

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
