# IC3 / FBI Full Complaint Package — Matanbuchus

**Status:** `PRIMARY_FROZEN` — **not filed** (primary frozen; ready for human filing review) · **Primary freeze:** 2026-09-20  
**Family:** Matanbuchus only (case-isolated)  
**Portal:** https://www.ic3.gov/

---

## 1. Filing identity

| Field | Value |
|-------|-------|
| Reporter purpose | Defensive threat-intelligence referral (not personal victimization claim) |
| Crime-type language | Malware; Unauthorized network intrusion / remote access; Credential theft |
| Suggested subject | Defensive TI referral — Matanbuchus (Huntress (+ Zscaler ThreatLabz Matanbuchus 3.0 analysis) 2025-07/2026) — `ETW-MAT-IC3` |
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
| **Matanbuchus (this package)** | `ETW-MAT-IC3` | *not filed* |

---

## 2. Technical indicator appendix (MAT-IND-0001–0015)

### Compact paste block

```
=== SHA256 ===
de81e2155d797ff729ed3112fd271aa2728e75fc71b023d0d9bb0f62663f33b3
6ffae128e0dbf14c00e35d9ca17c9d6c81743d1fc5f8dd4272a03c66ecc1ad1f
68858d3cbc9b8abaed14e85fc9825bc4fffc54e8f36e96ddda09e853a47e3e31
03c624d251e9143e1c8d90ba9b7fa1f2c5dc041507fd0955bdd4048a0967a829
8e54cd12591d67dfbe72e94c1bde6059e1cba157e6786aec63f8f9e3c71fb925
c31c8edbf94c85cc9bc46a5665c45a3556c48d5ad615c0a44e14e5406d80df12
eecc83add16f3d513a9701e9a646b1885014229ac6f86addd6b10afb64d1d2af
ea378496135318ac5ad667a032fa4a9686add9d27fe4a7c549c937611b5099e5

=== IPV4 ===
192.121.23.146

=== DOMAIN ===
www.ndibstersoft.com
binclloudapp.com

=== URL ===
http://binclloudapp.com/466943
https://marle.io/check/updprofile.aspx

=== PATH ===
%LOCALAPPDATA%\Temp\ndvyxgdriggmarrf

=== STRING ===
/intake/organizations/events?channel=app

```

Full structured table: [`03_INDICATORS.csv`](03_INDICATORS.csv).

---

## 3. Narrative (short)

Defensive threat-intelligence package concerning Matanbuchus 3.0 / AstarionRAT as publicly documented by Huntress (ClickFix delivery chain) with supporting technical context from Zscaler ThreatLabz Matanbuchus 3.0 analysis. Huntress describes ClickFix → silent MSI → Zillya-style DLL sideload → Matanbuchus 3.0 (ChaCha20) → Lua/reflective loader → AstarionRAT. This package is a TECHNIQUE COMPARATOR for SynkLoader (Teams/ClickFix/ChaCha20 class) only. authorship_link SynkLoader=NOT_ESTABLISHED. Do NOT file jointly with SynkLoader. Author/operator identity remains NOT_ESTABLISHED.

---

## 4. Case isolation

COMMON TECHNIQUE comparator for SynkLoader only. authorship_link SynkLoader=NOT_ESTABLISHED. See docs/TECHNIQUE_COMPARATORS.md.

---

## 5. Sources

See [`04_SOURCES.md`](04_SOURCES.md). Local freeze: `evidence/primary-sources/matanbuchus/huntress-matanbuchus-astarionrat.html` SHA-256 `61db6ae84078463576b58b48bcf79d489adeeb5b05f4658fdb29e840a07904e7`.
