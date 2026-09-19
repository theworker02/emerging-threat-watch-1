# Zimperium IOC Repo — RatHat Index (Metadata Only)

**Source URL:** https://github.com/Zimperium/IOC/tree/master/2026-09-RatHat  
**Retrieved (UTC):** 2026-09-19  
**Provenance:** Vendor IOC repository (treat as **PRIMARY metadata** for published indicators; **UNVERIFIED** by ETW until passively checked)  
**Safety:** Hashes/domains/URLs listed only — **no APK/malware download**

## Files in repo tree

| File | Content type | Local mirror |
|------|--------------|--------------|
| `apks.csv` | SHA-256 hashes (one per line) | `iocs/hashes-zimperium-ioc.csv` |
| `c2.csv` | C2 HTTP/WSS URLs/hosts | `iocs/domains.csv` + `iocs/urls.csv` |
| `phishing.csv` | Phishing / distribution URLs | `iocs/urls.csv` |

## Deep-pass refresh (2026-09-19)

| Check | Status |
|-------|--------|
| Repo path listed / API contents fetched | Done; raw files preserved under `evidence/passive-observations/github/rathat/` |
| File inventory | **Only** `apks.csv` (162 SHA-256), `c2.csv`, `phishing.csv` — **no** package-name or cert CSVs |
| CT / RDAP on published domains | Done for seed apexes (`RAT-PO-*`) |
| urlscan on selected hosts | Done (adidasabc / xiongmaocs.help / kingbss) |
| urlscan on API path strings | Done — **0 hits** |
| Hash→sample acquisition | **Forbidden / not done** |
| Unauth MalwareBazaar / VT package metadata | Failed (401/Unauthorized) |

All vendor IOC rows: `status=UNVERIFIED` until independently_verified flips after corroboration policy is met.
