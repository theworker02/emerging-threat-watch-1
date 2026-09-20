# IC3 / FBI Full Complaint Package — Abyssos

**Status:** `FILED_IC3` · Submission ID `a23f0a9d6799480e994284416d354713` · **Primary freeze:** 2026-09-20  
**Family:** Abyssos only (case-isolated)  
**Portal:** https://www.ic3.gov/

---

## 1. Filing identity

| Field | Value |
|-------|-------|
| Reporter purpose | Defensive threat-intelligence referral (not personal victimization claim) |
| Crime-type language | Malware; Unauthorized network intrusion / remote access; Credential theft |
| Suggested subject | Defensive TI referral — Abyssos (Zscaler ThreatLabz 2026-08-10) — `ETW-ABY-IC3` |
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
| **Abyssos (this filing)** | `ETW-ABY-IC3` | `a23f0a9d6799480e994284416d354713` |

---

## 2. Technical indicator appendix (ABY-IND-0001–0010)

### SHA-256

| ID | Value | Notes |
|----|-------|-------|
| ABY-IND-0001 | `52b400c5be1557a8df146f62fde76d906e7e0a92ed76788717ef61c758f315aa` | Abyssos v2.4F |
| ABY-IND-0002 | `ca94d95413210a2a325155740eb8a5c58627ad5c4e704478621e7fc8165fe173` | Abyssos v2.1F |

### IPv4 C2 (PRIMARY — not ETW live contact)

| ID | Value |
|----|-------|
| ABY-IND-0003 | `213.145.86.42` |
| ABY-IND-0004 | `209.99.184.223` |

### Host / protocol artifacts

| ID | Value | Notes |
|----|-------|-------|
| ABY-IND-0005 | `windows_update_cache.json` | Keylogger log under TEMP |
| ABY-IND-0006 | `%TEMP%\fontconfigs` | Browser clone / cookies.json |
| ABY-IND-0007 | `1234567890abcdef` | Module XOR / AES-CBC key·IV |
| ABY-IND-0008 | `Global\68AA60E5-6C45-4C01-9F0E-E25FC57C652F` | Example mutex (`Global\[UUID4]`) |
| ABY-IND-0009 | `HELLO\|%s\|%s\|%s\|%s\|%s\|v2.4F\|%s\|%s\|%s` | Registration format |
| ABY-IND-0010 | `Win64.PWS.Abyssos` | Zscaler detection name |

### Compact paste block

```
=== SHA-256 ===
52b400c5be1557a8df146f62fde76d906e7e0a92ed76788717ef61c758f315aa  v2.4F
ca94d95413210a2a325155740eb8a5c58627ad5c4e704478621e7fc8165fe173  v2.1F

=== C2 IPv4 ===
213.145.86.42
209.99.184.223

=== HOST ARTIFACTS ===
%TEMP%\fontconfigs
%TEMP%\windows_update_cache.json
Mutex: Global\[UUID4]
Crypto const: 1234567890abcdef
```

---

## 3. Primary source

- https://www.zscaler.com/blogs/security-research/abyssos-technical-analysis-new-modular-rat  
- Local: `evidence/primary-sources/abyssos/zscaler-abyssos-2026-08-10.html`  
- Archive SHA-256: `e374eed951febbdf8f18ae435669f8c2b6b6871c1c63e28aacdd28e97f80ba6c`

---

## 4. Subject fields

Unknown person/business. No published domains — use C2 IPs above. Author identity NOT_ESTABLISHED.

---

## 5. Safety

No malware executed; no C2 contact; no binaries attached to IC3 web form.
