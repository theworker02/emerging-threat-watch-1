# Argamal — IC3 Paste-Ready Pack (`ETW-ARG-IC3`)

**Status:** `PRIMARY_FROZEN` — **not filed** · ready for human filing  
**Portal:** https://www.ic3.gov/

Copy each section into the matching IC3 form field. Counts are under typical IC3 limits (description ≈3,500 · technical ≈5,000 · witnesses ≈1,000).

---

## 1. Subject line / title

```
Defensive TI referral — Argamal RAT (Kaspersky Securelist 2026-06-03) — ETW-ARG-IC3
```

## 2. Crime types

```
Malware; Unauthorized network intrusion / remote access; Credential theft
```

## 3. Subject #1 fields

| Field | Value |
|-------|-------|
| Name | Unknown |
| Business | Unknown (Argamal RAT / trojanized adult-game distribution) |
| Address / City / State / ZIP / Country | Unknown |
| Phone | Unknown |
| Email | Unknown |
| Website | asper1.freeddns.org; Winst0.kozow.com; country1.ignorelist.com |
| IP address | 186.158.223.35 |
| Notes | Author/operator NOT_ESTABLISHED; Spanish-language comments noted by Kaspersky only |

## 4. Financial / loss

| Field | Value |
|-------|-------|
| Total loss | **0** / None |
| Transactions | None / blank |
| Personal victimization | No |

## 5. Description (what happened)

*(2209 characters)*

```
I am reporting defensive threat-intelligence information concerning the Argamal RAT documented by Kaspersky GReAT on Securelist (2026-06-03), with Kaspersky blog/press companions. Filing as Emerging Threat Watch package ETW-ARG-IC3 — defensive TI referral, not a personal victimization or dollar-loss claim.

Kaspersky describes Argamal as a previously undocumented RAT distributed inside trojanized adult/hentai games (RenPy, RPG Maker MV, and other engines) via catalogue sites redirecting to PixelDrain and via torrent trackers (e.g., AniRena), plus at least one gaming-forum cheat lure. Infection uses a modified FFmpeg DLL and natives2_blob.bin PowerShell stages, COM hijacking of the Windows Color System Calibration Loader scheduled task, AES-CBC payload decrypt, UDP heartbeats, and TCP RAT mode. Published C2 domains include asper1.freeddns.org, Winst0.kozow.com, and country1.ignorelist.com. Spanish-language comments were noted by Kaspersky — author identity remains NOT_ESTABLISHED by ETW.

INDICATORS (PRIMARY-SOURCE; full CSV ARG-IND-0001–0022 on request):
SHA1 (representative): 42add9475e67a1ccc6a6af94b5475d3defc01b85 (ffmpeg.dll); edce72f59e4c1d136cd1946af70d334c19df858d (natives2_blob.bin); plus additional RAT/downloader SHA1s in CSV. Domains: asper1.freeddns.org; Winst0.kozow.com; country1.ignorelist.com. IP: 186.158.223.35. Ports/artifacts: UDP 57441/63559; TCP 3747. Host: COM CLSID {B210D694-C8DF-490D-9576-9E20CDBC20BD} / Windows Color System Calibration Loader.

Argamal-only — do not merge with other ETW filings. Prior separate IC3 IDs (no shared-operator claim): Rapuncel 208b747c6f7445f0af2b69a9d63acc36; Settra 631d8b4800d04bc19cdbfc6662e5c52c; RatHat f92c4c2f0dd3481f898fdd125e728adf; NodeRabbit dded86972e9347e0be27a6597b4cf08a; PollCat 98a4444754324e539dbbffcb10c70637; SynkLoader 3440d0c64dc240499ff66deaa3311a0b; Showboat db42033f319844c08ad103befebfca08; Abyssos a23f0a9d6799480e994284416d354713; SharkLoader 6ed57963d0c64750aa14b6fcbaa2e576.

Repo: https://github.com/theworker02/emerging-threat-watch-1 Path: reports/law-enforcement/packages/12-argamal/ Primary freeze 2026-09-20. No malware executed; no C2 contact; no binaries attached. Full CSV/dossier on request.
```

## 6. Technical details

*(2169 characters)*

```
=== PACKAGE ===
ETW-ARG-IC3 | Argamal | PRIMARY-SOURCE: Kaspersky GReAT Securelist (+ blog/press)
URL: https://securelist.com/argamal-rat-distributed-with-hentai-games/119999/
Blog: https://www.kaspersky.com/blog/argamal-hentai-games-rat-trojan/55944/
Repo path: reports/law-enforcement/packages/12-argamal/
CSV: 03_INDICATORS.csv (ARG-IND-0001 through ARG-IND-0022)
Local freeze PS-ARG-001 SHA-256 d3aa8cee046058d5c449ac23b759e8a6c2e26c2c0105d55d1f95a9d6e976e7ef
Provenance: PRIMARY-SOURCE only. Independently observed by ETW: none. Live C2 contact: none.

=== SHA1 (Kaspersky published — representative) ===
42add9475e67a1ccc6a6af94b5475d3defc01b85
edce72f59e4c1d136cd1946af70d334c19df858d
76253fb55aed707440e808ea78e7101318436b1c
1405a3c5e0aeb08012484134e16cdec4ab29b4a4
535f4337f261b6da20a3c614eb13270bed2d533a
d2cb0d7a9ad2b5d4ea7c2da8aec62beb37cf36d6
9803604ec45f31f9ef75bcca1e1310d8ac1fc3a6
02819d200d1424882af81cb504b3e8614b32397a

=== DOMAINS ===
asper1.freeddns.org
Winst0.kozow.com
country1.ignorelist.com

=== IPV4 ===
186.158.223.35
181.116.218.56

=== OTHER ===
filename: natives2_blob.bin
filename: zaesdl.dat
crypto_constant: zbcd1j9234r670eh
path: HKCU\SOFTWARE\Classes\CLSID\{B210D694-C8DF-490D-9576-9E20CDBC20BD}
url: github.com/gmz159/u
url: github.com/DnyP/files
url: github.com/mgzv/p
port: 57441
port: 3747

=== BEHAVIORAL SUMMARY ===
Trojanized adult-game archive → modified ffmpeg.dll / natives2_blob → COM hijack Calibration Loader → delayed download of Argamal RAT → UDP heartbeat / TCP remote control; credential/data theft goals per Kaspersky.

=== NOT IN THIS CORPUS ===
No actor legal name. No dollar loss. No ETW malware execution/C2 probing. Do not invent lure URLs beyond published staging paths.

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

*(457 characters)*

```
No firsthand fact witnesses known to the reporter beyond the public Kaspersky GReAT / Securelist disclosure. Reporter did not observe infections firsthand and did not interact with victims. Investigative contact for the public research is Kaspersky GReAT via the published Securelist article (and Kaspersky Intelligence Reporting Service for extended IoCs if needed). Emerging Threat Watch retained the public article freeze and transcribed indicators only.
```

## 8. Other agencies

*(400 characters)*

```
No prior report of this Argamal package by the reporter to other law-enforcement agencies. Public research was published by Kaspersky GReAT (Securelist). Related separate Emerging Threat Watch IC3 filings (different families; no shared-operator claim) are listed in the description and technical details. This complaint is not an update to a previously filed Argamal complaint (first Argamal filing).
```

## 9. Other information

*(805 characters)*

```
Primary sources:
https://securelist.com/argamal-rat-distributed-with-hentai-games/119999/
https://www.kaspersky.com/blog/argamal-hentai-games-rat-trojan/55944/
https://www.kaspersky.com/about/press-releases/kaspersky-discovers-argamal-a-new-malware-hidden-in-games-for-adults
Research repository: https://github.com/theworker02/emerging-threat-watch-1
Package folder: reports/law-enforcement/packages/12-argamal/
Full structured dossier: IC3_FULL_PACKAGE.md
Machine-readable indicators: 03_INDICATORS.csv (22 ARG-IND rows)
Caveats: 05_CAVEATS_AND_LIMITS.md
Crime-type language: Malware; Unauthorized network intrusion / remote access; Credential theft.
Dollar loss: $0 / none claimed. Personal victimization: No.
Is this an update to a previously filed complaint?: No (first Argamal / ETW-ARG-IC3 filing).
```

## 10. Date range

```
Beginning: 2026-04 (Kaspersky discovery window); public disclosure 2026-06-03
Ending: ongoing / unknown
```

## 11. Update to previous complaint?

**No** — first Argamal / `ETW-ARG-IC3` filing.

## 12. Complainant contact

Use **your** real name, phone, email, and mailing address (IC3 required). Do not enter SSN/DOB.

## After filing

Send the Submission ID (and timestamp) so it can be recorded on `main`.
