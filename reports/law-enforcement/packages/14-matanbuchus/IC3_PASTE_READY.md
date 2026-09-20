# Matanbuchus — IC3 Paste-Ready Pack (`ETW-MAT-IC3`)

**Status:** `PRIMARY_FROZEN` — **not filed** · ready for human filing · **TECHNIQUE_COMPARATOR — do not file jointly with SynkLoader**  
**Portal:** https://www.ic3.gov/

Copy each section into the matching IC3 form field. Counts are under typical IC3 limits (description ≈3,500 · technical ≈5,000 · witnesses ≈1,000).

---

## 1. Subject line / title

```
Defensive TI referral — Matanbuchus 3.0 / AstarionRAT (Huntress + Morphisec) — ETW-MAT-IC3 [SynkLoader comparator only]
```

## 2. Crime types

```
Malware; Unauthorized network intrusion / remote access; Credential theft; Social engineering
```

## 3. Subject #1 fields

| Field | Value |
|-------|-------|
| Name | Unknown |
| Business | Unknown (Matanbuchus 3.0 MaaS / AstarionRAT) |
| Address / City / State / ZIP / Country | Unknown |
| Phone | Unknown |
| Email | Unknown |
| Website | marle.io; ndibstersoft.com; binclloudapp.com; fixuplink.com |
| IP address | 192.121.23.146; 94.159.113.33 |
| Notes | Author/operator NOT_ESTABLISHED; TECHNIQUE_COMPARATOR for SynkLoader only — do not claim shared operators |

## 4. Financial / loss

| Field | Value |
|-------|-------|
| Total loss | **0** / None |
| Transactions | None / blank |
| Personal victimization | No |

## 5. Description (what happened)

*(2319 characters)*

```
I am reporting defensive threat-intelligence information concerning Matanbuchus 3.0 / AstarionRAT as documented by Huntress (ClickFix delivery), Morphisec (Teams/Quick Assist MaaS delivery), and Zscaler ThreatLabz (Matanbuchus 3.0 internals), with an eSentire advisory companion. Filing as Emerging Threat Watch package ETW-MAT-IC3 — defensive TI referral, not a personal victimization or dollar-loss claim.

Huntress describes ClickFix → silent MSI → DLL sideload → Matanbuchus 3.0 → Lua/reflective loader → AstarionRAT (24-command RAT with credential theft, SOCKS5, reflective loading). Morphisec documents a separate Teams IT-helpdesk / Quick Assist chain delivering Matanbuchus 3.0 via Notepad++ GUP sideload (malicious libcurl.dll) with distinct IOCs (fixuplink.com, EventLogBackupTask). This package is a TECHNIQUE COMPARATOR for SynkLoader (Teams/ClickFix/loader class) only — authorship_link SynkLoader = NOT_ESTABLISHED. Do NOT file jointly with SynkLoader (already filed separately as ETW-SYN-IC3 3440d0c64dc240499ff66deaa3311a0b). Author/operator identity remains NOT_ESTABLISHED.

INDICATORS (PRIMARY-SOURCE; full CSV MAT-IND-0001–0028 on request):
Huntress: http://binclloudapp.com/466943; https://marle.io/check/updprofile.aspx; www.ndibstersoft.com; Beacon.exe SHA-256 eecc83add16f3d513a9701e9a646b1885014229ac6f86addd6b10afb64d1d2af; SystemStatus.dll 6ffae128e0dbf14c00e35d9ca17c9d6c81743d1fc5f8dd4272a03c66ecc1ad1f. Morphisec: 94.159.113.33; fixuplink.com; bretux.com; nicewk.com; emorista.org; notepad-plus-plu.org; EventLogBackupTask; libcurl.dll hashes in CSV.

Matanbuchus-only comparator package — do not merge with SynkLoader. Prior separate IC3 IDs (no shared-operator claim): Rapuncel 208b747c6f7445f0af2b69a9d63acc36; Settra 631d8b4800d04bc19cdbfc6662e5c52c; RatHat f92c4c2f0dd3481f898fdd125e728adf; NodeRabbit dded86972e9347e0be27a6597b4cf08a; PollCat 98a4444754324e539dbbffcb10c70637; SynkLoader 3440d0c64dc240499ff66deaa3311a0b; Showboat db42033f319844c08ad103befebfca08; Abyssos a23f0a9d6799480e994284416d354713; SharkLoader 6ed57963d0c64750aa14b6fcbaa2e576.

Repo: https://github.com/theworker02/emerging-threat-watch-1 Path: reports/law-enforcement/packages/14-matanbuchus/ Primary freeze 2026-09-20. No malware executed; no C2 contact; no binaries attached. Full CSV/dossier on request.
```

## 6. Technical details

*(2809 characters)*

```
=== PACKAGE ===
ETW-MAT-IC3 | Matanbuchus 3.0 + AstarionRAT | TECHNIQUE_COMPARATOR for SynkLoader (do not file jointly)
Huntress: https://www.huntress.com/blog/clickfix-matanbuchus-astarionrat-analysis
Morphisec: https://www.morphisec.com/blog/ransomware-threat-matanbuchus-3-0-maas-levels-up/
Zscaler: https://www.zscaler.com/blogs/security-research/technical-analysis-matanbuchus-3-0
Repo path: reports/law-enforcement/packages/14-matanbuchus/
CSV: 03_INDICATORS.csv (MAT-IND-0001 through MAT-IND-0028)
Local freezes: PS-MAT-001 SHA-256 61db6ae84078463576b58b48bcf79d489adeeb5b05f4658fdb29e840a07904e7; PS-MAT-003 SHA-256 02ed074df2016dfe30ed37c128fb2e35eb57c2fae627883d366f79bf4d84522f
Provenance: PRIMARY-SOURCE only. Independently observed by ETW: none. Live C2 contact: none.

=== SHA256 ===
de81e2155d797ff729ed3112fd271aa2728e75fc71b023d0d9bb0f62663f33b3
6ffae128e0dbf14c00e35d9ca17c9d6c81743d1fc5f8dd4272a03c66ecc1ad1f
68858d3cbc9b8abaed14e85fc9825bc4fffc54e8f36e96ddda09e853a47e3e31
03c624d251e9143e1c8d90ba9b7fa1f2c5dc041507fd0955bdd4048a0967a829
8e54cd12591d67dfbe72e94c1bde6059e1cba157e6786aec63f8f9e3c71fb925
c31c8edbf94c85cc9bc46a5665c45a3556c48d5ad615c0a44e14e5406d80df12
eecc83add16f3d513a9701e9a646b1885014229ac6f86addd6b10afb64d1d2af
ea378496135318ac5ad667a032fa4a9686add9d27fe4a7c549c937611b5099e5
da9585d578f367cd6cd4b0e6821e67ff02eab731ae78593ab69674f649514872
2ee3a202233625cdcdec9f687d74271ac0f9cb5877c96cf08cf1ae88087bec2e
19fb41244558f3a7d469b79b9d91cd7d321b6c82d1660738256ecf39fe3c8421
211cea7a5fe12205fee4e72837279409ace663567c5b8c36828a3818aabef456
0f41536cd9982a5c1d6993fac8cd5eb4e7f8304627f2019a17e1aa283ac3f47c

=== URL / DOMAIN / IP ===
http://binclloudapp.com/466943
https://marle.io/check/updprofile.aspx
www.ndibstersoft.com
binclloudapp.com
fixuplink.com
bretux.com
nicewk.com
emorista.org
notepad-plus-plu.org
treasuryfinance.org
192.121.23.146
94.159.113.33

=== STRING / PATH ===
/intake/organizations/events?channel=app
EventLogBackupTask
%LOCALAPPDATA%\Temp\ndvyxgdriggmarrf

=== CAMPAIGN ISOLATION ===
Huntress = ClickFix→AstarionRAT chain. Morphisec = Teams/Quick Assist→GUP/libcurl sideload. Both Matanbuchus 3.0; do not assert shared operators with SynkLoader (COMMON TECHNIQUE only).

=== NOT IN THIS CORPUS ===
No actor legal name. No dollar loss. No ETW malware execution/C2 probing. Do not merge with SynkLoader filing.

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

*(378 characters)*

```
No firsthand fact witnesses known to the reporter beyond the public Huntress, Morphisec, Zscaler, and eSentire disclosures. Reporter did not observe the intrusion firsthand and did not interact with victims. Investigative contact for the public research is via the published vendor articles. Emerging Threat Watch retained public article freezes and transcribed indicators only.
```

## 8. Other agencies

*(521 characters)*

```
No prior report of this Matanbuchus package by the reporter to other law-enforcement agencies. Public research was published by Huntress, Morphisec, Zscaler ThreatLabz, and eSentire. Related separate Emerging Threat Watch IC3 filings (different families; no shared-operator claim) are listed in the description and technical details — including SynkLoader 3440d0c64dc240499ff66deaa3311a0b, which must remain separate. This complaint is not an update to a previously filed Matanbuchus complaint (first Matanbuchus filing).
```

## 9. Other information

*(948 characters)*

```
Primary sources:
https://www.huntress.com/blog/clickfix-matanbuchus-astarionrat-analysis
https://www.morphisec.com/blog/ransomware-threat-matanbuchus-3-0-maas-levels-up/
https://www.zscaler.com/blogs/security-research/technical-analysis-matanbuchus-3-0
https://www.esentire.com/security-advisories/matanbuchus-malware
Research repository: https://github.com/theworker02/emerging-threat-watch-1
Package folder: reports/law-enforcement/packages/14-matanbuchus/
Full structured dossier: IC3_FULL_PACKAGE.md
Machine-readable indicators: 03_INDICATORS.csv (28 MAT-IND rows)
Caveats: 05_CAVEATS_AND_LIMITS.md — TECHNIQUE_COMPARATOR for SynkLoader only.
Crime-type language: Malware; Unauthorized network intrusion / remote access; Credential theft; Social engineering.
Dollar loss: $0 / none claimed. Personal victimization: No.
Is this an update to a previously filed complaint?: No (first Matanbuchus / ETW-MAT-IC3 filing). Not an update to SynkLoader.
```

## 10. Date range

```
Beginning: Matanbuchus 3.0 campaigns ~2025; Huntress AstarionRAT chain and Morphisec Teams case as published
Ending: ongoing / unknown
```

## 11. Update to previous complaint?

**No** — first Matanbuchus / `ETW-MAT-IC3` filing (not an update to SynkLoader).

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
