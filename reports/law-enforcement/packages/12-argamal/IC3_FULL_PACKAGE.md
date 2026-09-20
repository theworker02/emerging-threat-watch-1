# IC3 / FBI Full Complaint Package — Argamal

**Status:** `PRIMARY_FROZEN` — **not filed** (primary frozen; ready for human filing review) · **Primary freeze:** 2026-09-20  
**Family:** Argamal only (case-isolated)  
**Portal:** https://www.ic3.gov/

---

## 1. Filing identity

| Field | Value |
|-------|-------|
| Reporter purpose | Defensive threat-intelligence referral (not personal victimization claim) |
| Crime-type language | Malware; Unauthorized network intrusion / remote access; Credential theft |
| Suggested subject | Defensive TI referral — Argamal (Kaspersky GReAT / Securelist 2026-06-03) — `ETW-ARG-IC3` |
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
| SharkLoader | `ETW-SHK-IC3` | `6ed57963d0c64750aa14b6fcbaa2e576` |
| **Argamal (this package)** | `ETW-ARG-IC3` | *not filed* |

---

## 2. Technical indicator appendix (ARG-IND-0001–0022)

### Compact paste block

```
=== SHA1 ===
42add9475e67a1ccc6a6af94b5475d3defc01b85
edce72f59e4c1d136cd1946af70d334c19df858d
76253fb55aed707440e808ea78e7101318436b1c
1405a3c5e0aeb08012484134e16cdec4ab29b4a4
535f4337f261b6da20a3c614eb13270bed2d533a
d2cb0d7a9ad2b5d4ea7c2da8aec62beb37cf36d6
9803604ec45f31f9ef75bcca1e1310d8ac1fc3a6
02819d200d1424882af81cb504b3e8614b32397a

=== DOMAIN ===
asper1.freeddns.org
Winst0.kozow.com
country1.ignorelist.com

=== IPV4 ===
186.158.223.35
181.116.218.56

=== FILENAME ===
natives2_blob.bin
zaesdl.dat

=== CRYPTO_CONSTANT ===
zbcd1j9234r670eh

=== PATH ===
HKCU\SOFTWARE\Classes\CLSID\{B210D694-C8DF-490D-9576-9E20CDBC20BD}

=== URL ===
github.com/gmz159/u
github.com/DnyP/files
github.com/mgzv/p

=== PORT ===
57441
3747

```

Full structured table: [`03_INDICATORS.csv`](03_INDICATORS.csv).

---

## 3. Narrative (short)

Defensive threat-intelligence package concerning Argamal as publicly documented by Kaspersky GReAT (Securelist 2026-06-03). Kaspersky describes a RAT distributed inside trojanized adult/hentai games (RenPy/RPG Maker etc.) via catalogue sites→PixelDrain and torrents (e.. AniRena). Infection uses modified FFmpeg DLL + natives2_blob.bin PowerShell stages, COM hijacking of Windows Color System Calibration Loader, AES-CBC payload decrypt (key zbcd1j9234r670eh), UDP heartbeats (57441) and TCP RAT mode (3747). C2 domains include asper1.freeddns.org / Winst0.kozow.com. Spanish-language comments noted by Kaspersky — author identity remains NOT_ESTABLISHED.

---

## 4. Case isolation

Standalone candidate. Case-isolated from all active families.

---

## 5. Sources

See [`04_SOURCES.md`](04_SOURCES.md). Primary freezes: Securelist (PS-ARG-001) + Kaspersky blog/press (PS-ARG-002/003).
