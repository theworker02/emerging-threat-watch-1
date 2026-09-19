# Evidence Tree — Emerging Threat Watch

Two tracks. Do not conflate them.

## `primary-sources/`
Immutable (or pending-freeze) copies of vendor/research publications.
Provenance: **PRIMARY-SOURCE**. Retrieval does **not** make campaign infrastructure `OBSERVED`.

Family dirs: `rapuncel/`, `settra/`, `rathat/`, `noderabbit/`, `pollcat/`, `synkloader/`, `showboat/`.

**PollCat dual-reference:** `pollcat/` documents a dual-list of the same Securelist HTML bytes already archived under `noderabbit/` (`PS-POL-001` ≡ `PS-NRB-001`). Dual-list in manifests; **do not merge** cases.

## `passive-observations/`
Independent passive collection (CT, RDAP, DNS, urlscan, GitHub metadata, archives, sample metadata, tracker queries).
Only these results may be labeled **OBSERVED** — and only after method + timestamp are recorded.

Tracker tag searches: `passive-observations/trackers/` (see README there). Captcha interstitials and API 401s are collection gaps — not empty-tag IOC claims.

## `manifests/`
- `primary-source-manifest.csv` — every primary fetch attempt
- `passive-observation-manifest.csv` — stays empty until passive collection runs

Status vocabulary for primary rows:
| Status | Meaning |
|--------|---------|
| UNRETRIEVED | Not obtained |
| RETRIEVED | Bytes saved locally |
| CONTENT-VERIFIED | Distinctive primary strings present in saved bytes |
| FROZEN | CONTENT-VERIFIED + intentional immutable retention (hash locked in ledger) |
