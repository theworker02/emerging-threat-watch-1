# IC3 / FBI Full Complaint Package — TencShell

**Status:** `PRIMARY_FROZEN` — **not filed** (primary frozen; ready for human filing review) · **Primary freeze:** 2026-09-20  
**Family:** TencShell only (case-isolated)  
**Portal:** https://www.ic3.gov/

---

## 1. Filing identity

| Field | Value |
|-------|-------|
| Reporter purpose | Defensive threat-intelligence referral (not personal victimization claim) |
| Crime-type language | Malware; Unauthorized network intrusion / remote access; Credential theft |
| Suggested subject | Defensive TI referral — TencShell (Cato CTRL 2026-04/2026-05) — `ETW-TEN-IC3` |
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
| **TencShell (this package)** | `ETW-TEN-IC3` | *not filed* |

---

## 2. Technical indicator appendix (TEN-IND-0001–0015)

### Compact paste block

```
=== SHA256 ===
c3ecb90c9915daa23aec51f93ff8665778866f0592b2413578c8ba9708df6091
660af53acdc505f333f6d4f4269cec740a5eb05e41a4c7926742606b18f22d33
37facbbd0047c19f4efdea75ccb9e3ec793cb9b1d7846afa4fb8e900d6e9ed95
01dc3e7e673b4f2682f29b19ecabf9a6ec9c3042c9b1cfb39dbdddf1dda680ab
750a707084839fe970266964957b8eaa7e25b4d9ca1050cd7ab19e4a2add707d
12f76f48727916d6c05f53f8cd94915db5de5ffcbfa02c4807c27e090cfa47c1
4ae8de40153c66455d972e6e98fe06fb68db7301ba126557e96599527bc5509c
1ba73df60e12b3feb8b5574e65cfceb6910460ab7fae2cf5554769fafdad049e

=== IPV4 ===
45.64.52.242
192.238.134.166
45.115.38.27

=== DOMAIN ===
gin-tne-fahcesmukw.cn-hangzhou.fcapp.run

=== FILENAME ===
.woff

=== STRING ===
OneDriveHealthTask
Reacon

```

Full structured table: [`03_INDICATORS.csv`](03_INDICATORS.csv).

---

## 3. Narrative (short)

Defensive threat-intelligence package concerning TencShell as publicly documented by Cato CTRL (2026). Cato describes a previously undocumented Go-based implant customized from the open-source Rshell C2 framework, delivered via a dropper → masqueraded .woff (Donut shellcode) → reflective in-memory load chain against a global manufacturer (India site / third-party access context). C2 traffic imitates Tencent-like web/API paths. Persistence via Run key value OneDriveHealthTask. Suspected China-linked assessment is vendor framing only. Author identity remains NOT_ESTABLISHED. Public Rshell OSS is NOT an IOC for this family.

---

## 4. Case isolation

OSS lineage similarity ≠ shared operators. Authorship NOT_ESTABLISHED. Standalone.

---

## 5. Sources

See [`04_SOURCES.md`](04_SOURCES.md). Local freeze: `evidence/primary-sources/tencshell/cato-tencshell-2026.md.txt` SHA-256 `742dedea94fc4a0d35a1c549447d3dc21f65f903ca41c33543fce471d5259c28`.
