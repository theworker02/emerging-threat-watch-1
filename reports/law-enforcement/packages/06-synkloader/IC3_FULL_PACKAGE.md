# IC3 / FBI Full Complaint Package — SynkLoader

**Status:** `FILED_IC3` · Submission ID `3440d0c64dc240499ff66deaa3311a0b` · **Cutoff:** 2026-09-19  
**Family:** SynkLoader only (case-isolated)  
**Portal:** https://www.ic3.gov/

---

## 1. Filing identity

| Field | Value |
|-------|-------|
| Reporter purpose | Defensive threat-intelligence referral (not personal victimization claim) |
| Crime-type language | Malware; Phishing / social engineering (Teams IT-helpdesk lure); Credential theft |
| Suggested subject | Defensive TI referral — SynkLoader (Expel 2026-08-20) — `ETW-SYN-IC3` |
| Dollar loss claimed | None |
| Personal victimization claimed | No |
| Malware binaries attached | No |
| ETW live C2 contact | None |
| Independently observed campaign ownership by ETW | None (DNS A rows are OBSERVED_PASSIVE only) |

### Related prior IC3 Submission IDs (separate — no shared-operator claim)

| Family | Package | Submission ID |
|--------|---------|---------------|
| Rapuncel | `ETW-RAP-IC3` | `208b747c6f7445f0af2b69a9d63acc36` |
| Settra | `ETW-SET-IC3` | `631d8b4800d04bc19cdbfc6662e5c52c` |
| RatHat | `ETW-RAT-IC3` | `f92c4c2f0dd3481f898fdd125e728adf` |
| NodeRabbit | `ETW-NRB-IC3` | `dded86972e9347e0be27a6597b4cf08a` |
| PollCat | `ETW-POL-IC3` | `98a4444754324e539dbbffcb10c70637` |
| **SynkLoader (this filing)** | `ETW-SYN-IC3` | `3440d0c64dc240499ff66deaa3311a0b` |

---

## 2. Complaint narrative (short form paste — see also private helper)

I am filing a defensive threat-intelligence referral on SynkLoader (package ETW-SYN-IC3), not a personal loss claim. Research cutoff 2026-09-19.

Repository: https://github.com/theworker02/emerging-threat-watch-1
Package: reports/law-enforcement/packages/06-synkloader/ (IC3_FULL_PACKAGE.md; 03_INDICATORS.csv)

Expel (2026-08-20, Marcus Hutchins) describes SynkLoader as a modular mixed-language loader delivered via Microsoft Teams phishing posing as IT helpdesk (external *.onmicrosoft.com tenant, display name IT Service Desk), with MSI on Azure Blob Storage. Primary: https://expel.com/blog/synkloader-when-you-throw-in-everything-but-the-kitchen-sink/

Do not merge with other ETW filings. Author identity NOT_ESTABLISHED. Matanbuchus is technique-comparator only.

Key indicators: SHA-256 151d2a7f52f047638ca8ad80c859c6bfe04d7510fb10933817fa0e3ba5d07a11 (331.msi) plus 10 additional module SHA-256s in CSV. Delivery URL: https://filereserve.blob.core.windows.net/vgnghuyk/331/331.msi. Domains: neversoftmain.net; rootfarmapp.net; tripinupdate.net; dondermicapp.net; aroclenetapp.net. OBSERVED_PASSIVE A: 149.248.76.220; 162.33.177.8; 216.245.184.14; 64.94.85.67 (not live C2 contact). ChaCha sigma: mlswgtppayebtezk / lwifnrfiosmfrubf. PDB: C:\Users\genry\source\repos\pwshnewdll\...\pwshnewdll.pdb.

Prior separate IC3 IDs: Rapuncel 208b747c6f7445f0af2b69a9d63acc36; Settra 631d8b4800d04bc19cdbfc6662e5c52c; RatHat f92c4c2f0dd3481f898fdd125e728adf; NodeRabbit dded86972e9347e0be27a6597b4cf08a; PollCat 98a4444754324e539dbbffcb10c70637.

Evidence retained offline; no binaries attached; no malware execution or C2 contact. Full CSV/dossier available on request.

---

## 3. Technical indicator appendix (SYN-IND-0001–0029)

### 3.1 Delivery URL

| ID | Value |
|----|-------|
| SYN-IND-0001 | `https://filereserve.blob.core.windows.net/vgnghuyk/331/331.msi` |

### 3.2 SHA-256 hashes (PRIMARY-SOURCE — Expel)

| ID | SHA-256 | Artifact |
|----|---------|----------|
| SYN-IND-0002 | `151d2a7f52f047638ca8ad80c859c6bfe04d7510fb10933817fa0e3ba5d07a11` | `331.msi` |
| SYN-IND-0003 | `80f08360ba768b152b71abb1cab557f552a13de18c83fe8e6396a197feec9185` | `cleaner.ps1` |
| SYN-IND-0004 | `209f69a6ca859f05c954096b30391a43fda33c9ed264dfdccf806697f04b06a8` | `archive6.zip` |
| SYN-IND-0005 | `d150c70d2732df17aa77991b9ebf4c896f044445e900978581d9598dfa5dc98c` | `ss.py` main loader |
| SYN-IND-0006 | `61f961cfebdf9967844526649b4b75bba5b1b83210b70aa1bffe3f64e6ac3112` | `msvcp150.dll` |
| SYN-IND-0007 | `8207d8d949530ea063ffd5d47ee81b74bf718ec0a4755e2349e6af9b91e92dc1` | `msvcp160.dll` |
| SYN-IND-0008 | `c4acda412774c292f0db5d64467a2dd09282cdea43c41967e8bf90f6298accf3` | Profiling module loader |
| SYN-IND-0009 | `63622c1ddb3e2a9f11cac192e13ac7494f558516b19d5d8f140f6d0d4d38ea84` | Persistence module loader |
| SYN-IND-0010 | `a335e75b78b601ebc5c258975d95fd79aa21f836fc6b79d82e9a22c596133f07` | Fake lock screen loader |
| SYN-IND-0011 | `0428fbdefa8dda10ce8fc12b1b516641e83cd5088388168e3f1a0be1432b4077` | Persistence module DLL |
| SYN-IND-0012 | `cb1c657f74b9e57f5e81126179128e8db949d1d4196be9dcb890341e222fd384` | Fake lock screen DLL |

### 3.3 Domains (PRIMARY-SOURCE — Expel)

| ID | Domain | Role |
|----|--------|------|
| SYN-IND-0013 | `neversoftmain.net` | Loader C2 |
| SYN-IND-0014 | `rootfarmapp.net` | Loader C2 |
| SYN-IND-0015 | `tripinupdate.net` | Loader C2 |
| SYN-IND-0016 | `dondermicapp.net` | TrafficRedirector C2 |
| SYN-IND-0017 | `aroclenetapp.net` | StreamMaster VNC C2 |

### 3.4 Filenames / paths / crypto / PDB

| ID | Value | Notes |
|----|-------|-------|
| SYN-IND-0018 | `PowershellCleaner` | MSI product/folder name |
| SYN-IND-0019 | `ss.py` | Main Python loader |
| SYN-IND-0020 | `msvcp150.dll` | Fake VC++ / RunPowerShell |
| SYN-IND-0021 | `msvcp160.dll` | In-memory DLL mapper |
| SYN-IND-0022 | `C:\Windows\Web\Screen` | PhishLocker wallpaper source |
| SYN-IND-0023 | `mlswgtppayebtezk` | Modified ChaCha20 SIGMA_128 |
| SYN-IND-0024 | `lwifnrfiosmfrubf` | Modified ChaCha20 SIGMA_256 |
| SYN-IND-0025 | `C:\Users\genry\source\repos\pwshnewdll\x64\Release\pwshnewdll.pdb` | Developer PDB in msvcp150.dll — **username is a build artifact, not confirmed operator identity** |

### 3.5 IPv4 (OBSERVED_PASSIVE DNS A — not live C2 contact; author NOT_ESTABLISHED)

| ID | IPv4 | Resolves (Expel PRIMARY domain) |
|----|------|----------------------------------|
| SYN-IND-0026 | `149.248.76.220` | `neversoftmain.net` |
| SYN-IND-0027 | `162.33.177.8` | `rootfarmapp.net` |
| SYN-IND-0028 | `216.245.184.14` | `tripinupdate.net` |
| SYN-IND-0029 | `64.94.85.67` | `aroclenetapp.net` |

Shared ASN **AS399629 (BL Networks)** across multiple apexes = INFRASTRUCTURE_OVERLAP candidate only — not operator identity. Azure Blob edge `57.150.140.65` (AS8075) is ASSOCIATION_ONLY.

### 3.6 Compact paste block

```
=== SHA-256 ===
151d2a7f52f047638ca8ad80c859c6bfe04d7510fb10933817fa0e3ba5d07a11  331.msi
80f08360ba768b152b71abb1cab557f552a13de18c83fe8e6396a197feec9185  cleaner.ps1
209f69a6ca859f05c954096b30391a43fda33c9ed264dfdccf806697f04b06a8  archive6.zip
d150c70d2732df17aa77991b9ebf4c896f044445e900978581d9598dfa5dc98c  ss.py
61f961cfebdf9967844526649b4b75bba5b1b83210b70aa1bffe3f64e6ac3112  msvcp150.dll
8207d8d949530ea063ffd5d47ee81b74bf718ec0a4755e2349e6af9b91e92dc1  msvcp160.dll
c4acda412774c292f0db5d64467a2dd09282cdea43c41967e8bf90f6298accf3  profiling loader
63622c1ddb3e2a9f11cac192e13ac7494f558516b19d5d8f140f6d0d4d38ea84  persistence loader
a335e75b78b601ebc5c258975d95fd79aa21f836fc6b79d82e9a22c596133f07  lockscreen loader
0428fbdefa8dda10ce8fc12b1b516641e83cd5088388168e3f1a0be1432b4077  persistence DLL
cb1c657f74b9e57f5e81126179128e8db949d1d4196be9dcb890341e222fd384  lockscreen DLL

=== URL ===
https://filereserve.blob.core.windows.net/vgnghuyk/331/331.msi

=== DOMAINS ===
neversoftmain.net
rootfarmapp.net
tripinupdate.net
dondermicapp.net
aroclenetapp.net

=== IPv4 (OBSERVED_PASSIVE A only) ===
149.248.76.220  neversoftmain.net
162.33.177.8    rootfarmapp.net
216.245.184.14  tripinupdate.net
64.94.85.67     aroclenetapp.net

=== OTHER ===
ChaCha: mlswgtppayebtezk / lwifnrfiosmfrubf
PDB: C:\Users\genry\source\repos\pwshnewdll\x64\Release\pwshnewdll.pdb
```

---

## 4. Delivery / modules (Expel PRIMARY)

Teams lure → MSI `PowershellCleaner` → `%LocalAppData%\PowershellCleaner\script\` (`cleaner.ps1` + `archive6.zip`) → nested PowerShell AES → bundled Python `ss.py` → modules: Profiler, Persistence (scheduled task), PhishLocker (fake Win11 lock screen credential theft), TrafficRedirector, interactive shell, StreamMaster VNC. C2 URL shape `https://<domain>/<token>/<victim_id>/`; beacon 90–120s.

---

## 5. Subject fields (IC3)

Unknown person/business. Websites = C2 domains above. IP = OBSERVED_PASSIVE A list (label as DNS resolution, not confirmed actor identity). PDB username `genry` is a build artifact only — do not treat as confirmed legal identity.

---

## 6. What this package does **not** claim

- Dollar loss / named victims  
- Author / operator identity (NOT_ESTABLISHED)  
- Confirmed ransomware follow-on by ETW  
- That DNS resolution proves C2 is currently active  
- Shared operators with other ETW families (including Matanbuchus technique comparator)

---

## 7. Safety

No malware executed; no C2 contact; no binaries attached to IC3 web form.
