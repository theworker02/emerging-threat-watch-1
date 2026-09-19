# NodeRabbit — Deep Passive Pass (2026-09-19)

**Scope:** Deepen non-Azure CT, MD5→SHA-256 hunt, NightLedger chronology (context only), GitHub string negatives.  
**Isolation:** PollCat dual-lists Securelist; do not merge cases.

---

## NEW facts

### MD5 → SHA-256 status (critical gap update)

| Source | Result | Provenance |
|--------|--------|------------|
| MalwareBazaar API `get_info` for all 11 Securelist MD5s | HTTP **401 Unauthorized** (auth now required) | OBSERVED_PASSIVE attempt recorded |
| Kaspersky OpenTIP HTML for `1ea83e4e…` / RankChallenge MD5 | Page retrieved (~2853 B); **no 64-hex SHA-256** in body | OBSERVED_PASSIVE |
| Hybrid Analysis search UI for Front-Technical MD5 | Page retrieved; no usable public SHA-256 extracted | OBSERVED_PASSIVE |
| tria.ge API | 401 | OBSERVED_PASSIVE |
| ThreatFox API | fail | OBSERVED_PASSIVE |
| **PolySwarm blog** (2026-09) publishes two SHA-256s “associated with this activity” / “samples of NodeRabbit” | `123289b3680c1d693db0e3702137cc55862dbe8b9a34376bcdf08bd0514b98e7`, `307ce2448211a5f5d122643f2a739aff33ede72c1858518c8de098f3148bbd00` | PRIMARY-SOURCE (PolySwarm) — **not** verified as hashes of `Front-Technical-Challenge.zip` MD5; treat as related samples until MD5↔SHA256 map exists |

**Verdict:** Archive MD5→SHA-256 for `Front-Technical-Challenge.zip` and siblings remains **OPEN**. PolySwarm hashes are new defensive leads, not MD5 resolutions.

### Additional Kaspersky infrastructure (PRIMARY-SOURCE) — previously incomplete in domains.csv

Non-Azure / NameCheap “pattern” assets (creation dates May–Jul 2026 per Securelist):

`healthful-hub.com`, `neumedicahealthcare.com`, `optimumhealthcredit.com`, `healthfullyrecipes.com`, `refreshhealthandwellness.com`, `healthvitalitycare.com`, `aceofspadesmanagement.com`, `glmediaagency.com`, `digimediaskill.com`, `healthyweightplan.com`, `mens-health-online.com`

Plus previously ledgered: `visitfinancedentists.com`, `healthcomfsdpower.com`, `msmanagementgrp.com`, `msmanagementgrpmedia.com`.

Additional Azure hosts from sample-6/7 table not fully in early domains.csv: `greenyjsgfd`, `helptellerbls`, `timedrv`, `userwellgtfs`, `hecowime-aqdphyd4bbdef6es.westeurope-01` azurewebsites.

### Passive CT deepening (OBSERVED_PASSIVE) — non-Azure focus

| Domain | CT cert_count (this pass) |
|--------|---------------------------|
| `msmanagementgrp.com` | 49 (prior pass had 502 — **resolved**) |
| `msmanagementgrpmedia.com` | 2 |
| `neumedicahealthcare.com` | 45 |
| `refreshhealthandwellness.com` | 131 |
| `healthvitalitycare.com` | 51 |
| `aceofspadesmanagement.com` | 39 |
| `glmediaagency.com` | 59 |
| `digimediaskill.com` | 22 |
| `healthyweightplan.com` | 206 |
| `mens-health-online.com` | 39 |
| `optimumhealthcredit.com` | 17 |
| `healthfullyrecipes.com` | 45 |
| `healthful-hub.com` | 21 |
| `visitfinancedentists.com` | 25 (prior) |
| `healthcomfsdpower.com` | 2 (prior) |

CT facts ≠ actor ownership. Use for chronology hunting only.

### Wayback (OBSERVED_PASSIVE)

- `oracle-challenge.s3.us-east-1.amazonaws.com/*` CDX: sparse/empty useful lure snapshots (artifact retained).
- No public lure page freeze beyond Securelist screenshots.

### GitHub distinctive strings (OBSERVED_PASSIVE)

Logged-out code search `result_count=0` for: `shepherd-persist`, `msedge_update.js`, `GitHub Copilot Helper`, `colorized_terminal`+`2.1.0`. Useful negative for public source leakage.

### NightLedger July 2026 — infrastructure chronology (context only)

Source: https://securelist.com/mirage-kitten-new-tools/120811/ (`PS-NRB-002`)

| Tool | Relevant infra / note |
|------|----------------------|
| NightLedger | C2 `realhealthshop.com` (+ fallback `tjconsultingservices.com`); masquerades `SspiCli.dll` via AppVShNotify |
| BridgeHead | WebSocket tunneler; Egypt + Pakistan aerospace; corporate proxy NTLM/Negotiate — **same design family** Kaspersky later cites for NodeRabbit proxy + PollCat/MiniFast |
| ArcBridge | First seen Apr 2026 ME; mutex `F56E68DA-4A89-46B4-9AC8-7290A7651000` |
| Ops shift | July article notes gradual shift **away from Azure websites toward Cloudflare-backed domains** in some malware — contrasts Sept NodeRabbit/PollCat still heavy on Azure |

**Do not** transfer NightLedger IOCs into NodeRabbit CAMPAIGN_ASSOCIATED without separate evidence.

### RankChallenge misfile

`795e053a…` RankChallenge ZIP is PollCat lure — see POL ledger. Keep `NRB-IND-0011` as cross-ref only / mark superseded.

---

## Artifacts

- PolySwarm HTML freeze under `evidence/primary-sources/noderabbit/polyswarm-noderabbit-pollcat.html`
- NightLedger HTML under `evidence/primary-sources/noderabbit/securelist-mirage-kitten-nightledger-2026-07-28.html`
- Sample-metadata attempt tree under `evidence/passive-observations/sample-metadata/noderabbit/`
- CT/RDAP batch JSON + per-domain responses
