# TencShell — IC3 Paste-Ready Pack (`ETW-TEN-IC3`)

**Status:** `PRIMARY_FROZEN` — **not filed** · ready for human filing  
**Portal:** https://www.ic3.gov/

Copy each section into the matching IC3 form field. Counts are under typical IC3 limits (description ≈3,500 · technical ≈5,000 · witnesses ≈1,000).

---

## 1. Subject line / title

```
Defensive TI referral — TencShell (Cato CTRL + Hunt.io 2026) — ETW-TEN-IC3
```

## 2. Crime types

```
Malware; Unauthorized network intrusion / remote access; Credential theft
```

## 3. Subject #1 fields

| Field | Value |
|-------|-------|
| Name | Unknown |
| Business | Unknown (TencShell / customized Rshell implant campaign) |
| Address / City / State / ZIP / Country | Unknown |
| Phone | Unknown |
| Email | Unknown |
| Website | gin-tne-fahcesmukw.cn-hangzhou.fcapp.run |
| IP address | 45.64.52.242; 192.238.134.166; 45.115.38.27; 112.213.124.132 |
| Notes | Author/operator NOT_ESTABLISHED; China-linked = Cato suspected only; OSS Rshell ≠ IOC |

## 4. Financial / loss

| Field | Value |
|-------|-------|
| Total loss | **0** / None |
| Transactions | None / blank |
| Personal victimization | No |

## 5. Description (what happened)

*(2648 characters)*

```
I am reporting defensive threat-intelligence information concerning the TencShell malware documented by Cato CTRL (April–May 2026) and a Hunt.io follow-on (2026-07-14) that pivoted from the same C2 fingerprint. Filing as Emerging Threat Watch package ETW-TEN-IC3 — defensive TI referral, not a personal victimization or dollar-loss claim.

Cato CTRL describes TencShell as a previously undocumented Go-based implant customized from the open-source Rshell C2 framework, observed in an attempted intrusion against a global manufacturer (India site / third-party access context). The chain used a first-stage dropper, Donut shellcode staged as a masqueraded .woff resource, reflective in-memory load, and web-like C2 that imitates Tencent-style API paths. Persistence used Registry Run value OneDriveHealthTask. Cato’s “suspected China-linked” assessment is vendor framing only; ETW does not independently establish attribution. Public Rshell OSS repositories are NOT IOCs for this family.

Hunt.io later pivoted on TencShell C2 HTTP header fingerprints (port 1111) and published a Hong Kong infrastructure cluster including an open directory at 112.213.124.132, plus related Gshell TLS certificate matches. Hunt.io Linux/ARM samples from that pivot are infra-related and are not confirmed Windows TencShell code-level matches.

INDICATORS (PRIMARY-SOURCE; full CSV TEN-IND-0001–0081 on request):
Cato IPs: 45.64.52.242; 192.238.134.166; 45.115.38.27. Domain: gin-tne-fahcesmukw.cn-hangzhou.fcapp.run. Host: OneDriveHealthTask; Reacon; .woff. Representative Cato SHA-256: c3ecb90c9915daa23aec51f93ff8665778866f0592b2413578c8ba9708df6091; 660af53acdc505f333f6d4f4269cec740a5eb05e41a4c7926742606b18f22d33; 37facbbd0047c19f4efdea75ccb9e3ec793cb9b1d7846afa4fb8e900d6e9ed95; 01dc3e7e673b4f2682f29b19ecabf9a6ec9c3042c9b1cfb39dbdddf1dda680ab. Hunt.io cluster IPs include 112.213.124.132/159/163 and 45.64.52.245/246 (full list in CSV).

TencShell-only — do not merge with other ETW filings. Prior separate IC3 IDs (no shared-operator claim): Rapuncel 208b747c6f7445f0af2b69a9d63acc36; Settra 631d8b4800d04bc19cdbfc6662e5c52c; RatHat f92c4c2f0dd3481f898fdd125e728adf; NodeRabbit dded86972e9347e0be27a6597b4cf08a; PollCat 98a4444754324e539dbbffcb10c70637; SynkLoader 3440d0c64dc240499ff66deaa3311a0b; Showboat db42033f319844c08ad103befebfca08; Abyssos a23f0a9d6799480e994284416d354713; SharkLoader 6ed57963d0c64750aa14b6fcbaa2e576.

Repo: https://github.com/theworker02/emerging-threat-watch-1 Path: reports/law-enforcement/packages/10-tencshell/ Primary freeze 2026-09-20. No malware executed; no C2 contact; no binaries attached. Full CSV/dossier on request.
```

## 6. Technical details

*(3135 characters)*

```
=== PACKAGE ===
ETW-TEN-IC3 | TencShell | PRIMARY-SOURCE: Cato CTRL + Hunt.io follow-on
Cato: https://www.catonetworks.com/blog/cato-ctrl-suspected-china-linked-threat-actor-targets-global-manufacturer/
Hunt.io: https://hunt.io/blog/chinese-operators-claude-deepseek-government-intrusion
Repo: https://github.com/theworker02/emerging-threat-watch-1
Path: reports/law-enforcement/packages/10-tencshell/
CSV: 03_INDICATORS.csv (TEN-IND-0001 through TEN-IND-0030)
Local freezes: PS-TEN-001 (Cato md) SHA-256 742dedea94fc4a0d35a1c549447d3dc21f65f903ca41c33543fce471d5259c28; PS-TEN-002 Hunt.io HTML SHA-256 81ac15a579b9877d0a72a72e7f64582fd81a3c915a25fb28baaaeba4a84a027a
Provenance: PRIMARY-SOURCE only. Independently observed by ETW: none. Live C2 contact: none.

=== SHA256 (Cato published samples) ===
c3ecb90c9915daa23aec51f93ff8665778866f0592b2413578c8ba9708df6091
660af53acdc505f333f6d4f4269cec740a5eb05e41a4c7926742606b18f22d33
37facbbd0047c19f4efdea75ccb9e3ec793cb9b1d7846afa4fb8e900d6e9ed95
01dc3e7e673b4f2682f29b19ecabf9a6ec9c3042c9b1cfb39dbdddf1dda680ab
750a707084839fe970266964957b8eaa7e25b4d9ca1050cd7ab19e4a2add707d
12f76f48727916d6c05f53f8cd94915db5de5ffcbfa02c4807c27e090cfa47c1
4ae8de40153c66455d972e6e98fe06fb68db7301ba126557e96599527bc5509c
1ba73df60e12b3feb8b5574e65cfceb6910460ab7fae2cf5554769fafdad049e

=== SHA256 (Hunt.io pivot samples — infra-related; not confirmed Windows TencShell code match) ===
90b7b2c6f3d05234dc55678243039d7e51f0d54190239e5234a0005533337dc8
643de2a1cf9148b896efecf560c9476fa56118ec477c4e15eb5c2da4b318061f

=== IPV4 (Cato) ===
45.64.52.242
192.238.134.166
45.115.38.27

=== IPV4 (Hunt.io TencShell cluster / open directory; Gshell rows labeled related) ===
112.213.124.132
112.213.124.159
112.213.124.163
45.64.52.245
45.64.52.246
134.122.200.153
134.122.200.154
134.122.200.155
192.229.115.229
192.229.115.230
38.55.105.143
192.163.167.5
134.122.200.114

=== DOMAIN ===
gin-tne-fahcesmukw.cn-hangzhou.fcapp.run

=== HOST ARTIFACTS ===
OneDriveHealthTask (Run key value)
Reacon (embedded Go project/artifact name)
.woff (masqueraded Donut staging extension)

=== BEHAVIORAL SUMMARY ===
Dropper → masqueraded .woff / Donut shellcode → reflective load → Go implant (Rshell-derived) with Tencent-like web/API C2, screen/input, browser artifact access, SOCKS5, UAC bypass, Run-key persistence. Hunt.io: header-fingerprint pivot → HK ASN cluster + open directory operational tooling; Claude Code / DeepSeek noted as operator workflow aids (vendor narrative).

=== NOT IN THIS CORPUS ===
No actor legal name/phone/email/address. No dollar loss claimed. No ETW malware execution or C2 probing. Public Rshell OSS ≠ IOC. China-linked = vendor suspected only.

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

*(372 characters)*

```
No firsthand fact witnesses known to the reporter beyond the public Cato CTRL and Hunt.io disclosures. Reporter did not observe the intrusion firsthand and did not interact with victims. Investigative contact for the public research is via the published Cato CTRL and Hunt.io articles. Emerging Threat Watch retained public article freezes and transcribed indicators only.
```

## 8. Other agencies

*(399 characters)*

```
No prior report of this TencShell package by the reporter to other law-enforcement agencies. Public research was published by Cato CTRL and Hunt.io. Related separate Emerging Threat Watch IC3 filings (different families; no shared-operator claim) are listed in the description and technical details. This complaint is not an update to a previously filed TencShell complaint (first TencShell filing).
```

## 9. Other information

*(822 characters)*

```
Primary sources:
https://www.catonetworks.com/blog/cato-ctrl-suspected-china-linked-threat-actor-targets-global-manufacturer/
https://hunt.io/blog/chinese-operators-claude-deepseek-government-intrusion
Secondary: https://www.infosecurity-magazine.com/news/china-hackers-tencshell-malware/
Research repository: https://github.com/theworker02/emerging-threat-watch-1
Package folder: reports/law-enforcement/packages/10-tencshell/
Full structured dossier: IC3_FULL_PACKAGE.md
Machine-readable indicators: 03_INDICATORS.csv (81 TEN-IND rows)
Caveats: 05_CAVEATS_AND_LIMITS.md
Crime-type language: Malware; Unauthorized network intrusion / remote access; Credential theft.
Dollar loss: $0 / none claimed. Personal victimization: No.
Is this an update to a previously filed complaint?: No (first TencShell / ETW-TEN-IC3 filing).
```

## 10. Date range

```
Beginning: 2026-04 (Cato observed activity) / 2026-05 (Cato public disclosure); Hunt.io follow-on 2026-07-14
Ending: ongoing / unknown
```

## 11. Update to previous complaint?

**No** — first TencShell / `ETW-TEN-IC3` filing.

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
