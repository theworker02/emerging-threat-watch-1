# IC3 / FBI Full Complaint Package — Okobot

**Status:** `PRIMARY_FROZEN` — **not filed** (primary frozen; ready for human filing review) · **Primary freeze:** 2026-09-20  
**Family:** Okobot only (case-isolated)  
**Portal:** https://www.ic3.gov/

---

## 1. Filing identity

| Field | Value |
|-------|-------|
| Reporter purpose | Defensive threat-intelligence referral (not personal victimization claim) |
| Crime-type language | Malware; Unauthorized network intrusion / remote access; Credential theft |
| Suggested subject | Defensive TI referral — Okobot (Kaspersky GReAT / Securelist 2026) — `ETW-OKO-IC3` |
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
| **Okobot (this package)** | `ETW-OKO-IC3` | *not filed* |

---

## 2. Technical indicator appendix (OKO-IND-0001–0030)

### Compact paste block

```
=== MD5 ===
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

=== IPV4 ===
104.243.43.16
104.243.32.213
62.210.188.209

=== DOMAIN ===
2baserec2.guru
recavb22.online
kbeautyreviews.com
coffeesaloon.online
livewallpapers.online
thatwascringe.com
moonsand.store

=== PATH ===
%PROGRAMDATA%\HDVideo\HDUtil.exe
%PROGRAMDATA%\hwid.dat
%PROGRAMDATA%\oko_ver
%USERPROFILE%\.ssh\go.bat

=== STRING ===
ir-post.php

```

Full structured table: [`03_INDICATORS.csv`](03_INDICATORS.csv).

---

## 3. Narrative (short)

Defensive threat-intelligence package concerning the OkoBot framework as publicly documented by Kaspersky GReAT (Securelist). Kaspersky describes a multi-stage campaign (≥20 payloads) initiated via TookPS PowerShell, configuring an SSH bot and dispatching modules including OkoSpyware (window video + keylogging of crypto wallets/password managers), SeedHunter (hardware-wallet seed phishing overlays), MC Keylogger, and browser extension loaders (e.g. Rilide). Victims across 25+ countries; activity ongoing as of publication. Russian-speaking crimeware signals noted by Kaspersky — author identity remains NOT_ESTABLISHED.

---

## 4. Case isolation

Standalone candidate. Case-isolated from all active families.

---

## 5. Sources

See [`04_SOURCES.md`](04_SOURCES.md). Local freeze: `evidence/primary-sources/okobot/securelist-okobot-2026.html` SHA-256 `04eb0610ddb6e36d4cb0c12917e90424741162b091b87426a5c4c3cc1bf431ec`.
