# IC3 / FBI Full Complaint Package — Showboat

**Status:** `FILED_IC3` · Submission ID `db42033f319844c08ad103befebfca08` · **Cutoff:** 2026-09-19  
**Family:** Showboat only (case-isolated)  
**Portal:** https://www.ic3.gov/

---

## 1. Filing identity

| Field | Value |
|-------|-------|
| Reporter purpose | Defensive threat-intelligence referral (not personal victimization claim) |
| Crime-type language | Malware; Unauthorized network intrusion (post-exploitation) |
| Suggested subject | Defensive TI referral — Showboat (Lumen BLL May 2026) — `ETW-SHO-IC3` |
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
| **Showboat (this filing)** | `ETW-SHO-IC3` | `db42033f319844c08ad103befebfca08` |

---

## 2. Technical indicator appendix (SHO-IND-0001–0026)

### SHA-256 / cert

| ID | Type | Value | Notes |
|----|------|-------|-------|
| SHO-IND-0008 | sha256 | `d6a4fad5448838dbc8cc6b33f1dbfbdc7a2fad36de58ff6a66dce96f729f7011` | Linux sample |
| SHO-IND-0009 | sha256 | `8fc0b205876923d35df436e666ec1506839ef3861422037490bae4daa63c1165` | Windows sample |
| SHO-IND-0010 | sha256 | `253cc9dbabeb0054f3d353cfff24f2aeb9cecd3e031333127d33cc4edacf2a56` | Windows sample |
| SHO-IND-0011 | x509_sha256 | `27df475626aafce2ea1548a9f35efb9ad951298c8b11a6adb3ccdfcd5170c677` | Primary cluster cert (My Organization) |
| SHO-IND-0012 | xor_key | `look me AV!` | Hardcoded XOR config key phrase |

### Domains

| ID | Domain | Role |
|----|--------|------|
| SHO-IND-0001 | `telecom.webredirect.org` | Primary C2 SERVER_ADDRESS |
| SHO-IND-0004 | `singtelcom.site` | Telecom impersonation |
| SHO-IND-0006 | `kaztelecom.shop` | Telecom impersonation |

### IPv4 (PRIMARY-SOURCE)

| ID | IP | Role |
|----|-----|------|
| SHO-IND-0002 | `139.84.227.139` | Primary C2 (telecom.webredirect.org) |
| SHO-IND-0003 | `194.135.25.132` | Second C2 |
| SHO-IND-0005 | `23.27.201.160` | singtelcom.site |
| SHO-IND-0007 | `101.36.105.222` | kaztelecom.shop |
| SHO-IND-0013 | `103.10.145.129` | ukpkmkk.bin host; first_seen 2023-04-04 |
| SHO-IND-0014 | `114.116.239.178` | ukpkmkk.bin host 2024-11–2025-02 |
| SHO-IND-0015 | `192.9.141.111` | Secondary cluster |
| SHO-IND-0016 | `64.176.43.209` | Secondary cluster |
| SHO-IND-0017 | `116.169.244.208` | **ASSOCIATION_ONLY** (possible upstream/dev) |
| SHO-IND-0018 | `45.76.157.243` | BLL C2 :443 |
| SHO-IND-0019 | `139.84.135.190` | BLL C2 :443 |
| SHO-IND-0020 | `139.180.223.193` | BLL C2 :443 |
| SHO-IND-0021 | `152.32.159.11` | BLL C2 :443 / singtelcom.site |
| SHO-IND-0022 | `38.246.73.120` | BLL C2 :443 |

### Host artifacts (SECONDARY — Picus)

| ID | Value |
|----|-------|
| SHO-IND-0023 | `ukpkmkk.c` |
| SHO-IND-0024 | `ukpkmkk.so` |
| SHO-IND-0025 | `kworkers\|dbus\|autoupdate` |
| SHO-IND-0026 | `/etc/ld.so.preload` |

### Compact paste block

```
=== SHA-256 ===
d6a4fad5448838dbc8cc6b33f1dbfbdc7a2fad36de58ff6a66dce96f729f7011  Linux
8fc0b205876923d35df436e666ec1506839ef3861422037490bae4daa63c1165  Windows
253cc9dbabeb0054f3d353cfff24f2aeb9cecd3e031333127d33cc4edacf2a56  Windows
X.509: 27df475626aafce2ea1548a9f35efb9ad951298c8b11a6adb3ccdfcd5170c677

=== DOMAINS ===
telecom.webredirect.org
singtelcom.site
kaztelecom.shop

=== IPv4 ===
139.84.227.139  primary C2
194.135.25.132  second C2
23.27.201.160   singtelcom.site
101.36.105.222  kaztelecom.shop
103.10.145.129  historical (2023-04-04)
114.116.239.178; 192.9.141.111; 64.176.43.209
45.76.157.243; 139.84.135.190; 139.180.223.193; 152.32.159.11; 38.246.73.120
116.169.244.208 ASSOCIATION_ONLY

=== OTHER ===
XOR key: look me AV!
Persistence: /etc/ld.so.preload; ukpkmkk.so
```

---

## 3. Dating caveat

Pastebin hide-code Jan 2022 and BLL first_seen from 2023-04-04 vs May 2026 disclosure = intelligence gap. Do not claim continuous operations solely from Pastebin date.

---

## 4. Subject fields

Unknown person/business. Websites = domains above. IPs = PRIMARY C2/impersonation list (exclude treating ASSOCIATION_ONLY `116.169.244.208` as confirmed actor-owned). Author identity NOT_ESTABLISHED.

---

## 5. Safety

No malware executed; no C2 contact; no binaries attached to IC3 web form.
