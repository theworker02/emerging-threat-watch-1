# IC3 / FBI Full Complaint Package — MiniFast

**Status:** `PRIMARY_FROZEN` — **not filed** (primary frozen; ready for human filing review) · **Primary freeze:** 2026-09-20  
**Family:** MiniFast only (case-isolated)  
**Portal:** https://www.ic3.gov/

---

## 1. Filing identity

| Field | Value |
|-------|-------|
| Reporter purpose | Defensive threat-intelligence referral (not personal victimization claim) |
| Crime-type language | Malware; Unauthorized network intrusion / remote access; Credential theft |
| Suggested subject | Defensive TI referral — MiniFast (Check Point Research 2026-05) — `ETW-MNF-IC3` |
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
| **MiniFast (this package)** | `ETW-MNF-IC3` | *not filed* |

---

## 2. Technical indicator appendix (MNF-IND-0001–0044)

### Compact paste block

```
=== SHA256 ===
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

=== DOMAIN ===
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

=== PATH ===
%LOCALAPPDATA%\Zoom\bin\update

=== FILENAME ===
UpdateChecker.dll
Zoominstall64.zip

=== STRING ===
CheckForUpdates
ZoomUpdateTaskUser

```

Full structured table: [`03_INDICATORS.csv`](03_INDICATORS.csv).

---

## 3. Narrative (short)

Defensive threat-intelligence package concerning MiniFast as publicly documented by Check Point Research in Fast and Furious — Nimbus Manticore operations (2026). Check Point describes a previously undocumented 64-bit .NET backdoor (export CheckForUpdates / UpdateChecker.dll) delivered via AppDomain hijacking and a trojanized Zoom installer flow (Zoominstall64.zip), with persistence by hijacking ZoomUpdateTaskUser. C2 uses JSON/HTTPS with Chrome UA impersonation and Azure Web App hosts. Actor framing (Nimbus Manticore / UNC1549 / IRGC-linked) is vendor assessment — ETW does not independently establish attribution. Structural C2 notes vs PollCat are ASSOCIATION_ONLY — do NOT merge into POL case. Authorship link NOT_ESTABLISHED.

---

## 4. Case isolation

Context for PollCat lineage assessment only — do NOT auto-merge into POL case. authorship_link=NOT_ESTABLISHED.

---

## 5. Sources

See [`04_SOURCES.md`](04_SOURCES.md). Primary freezes: Check Point (PS-MNF-001) + Unit 42 Screening Serpens / MiniUpdate (PS-MNF-002).
