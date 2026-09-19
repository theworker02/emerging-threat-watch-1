# PollCat ↔ NodeRabbit — Lineage / Technique Comparison

**Updated:** 2026-09-19 (deep passive)  
**Rule:** COMMON TECHNIQUE comparison allowed. **Do NOT** assume shared authorship. Separate ledgers / `ETW-POL-IC3` vs `ETW-NRB-IC3`.

| Signal | Assessment | Confidence | Provenance | Notes |
|--------|------------|------------|------------|-------|
| Co-disclosure in same Securelist article (2026-09-01) | Shared **investigation** only | High | PRIMARY-SOURCE | Dual-list HTML; do not merge cases |
| Kaspersky Mirage Kitten attribution for both | Shared **actor assessment** (vendor) | High (vendor) / Moderate (ETW adopts as vendor claim) | PRIMARY-SOURCE | ETW does not independently establish |
| Fake-recruiter + trojanized coding-challenge ZIP delivery | COMMON TECHNIQUE / shared delivery class | High | PRIMARY-SOURCE | Not automatic IOC transfer |
| Azure Websites + Cloudflare-backed domains | COMMON TECHNIQUE / infra style | Moderate | PRIMARY-SOURCE | Shared cloud edges ≠ ownership |
| Cross-platform scripting (Win/Linux/macOS) | COMMON TECHNIQUE (tooling shift vs native) | High | PRIMARY-SOURCE | First JS/Node tooling for cluster per Kaspersky |
| Implant language/runtime | **Divergent** — Node.js modular RAT vs obfuscated JS poller | High | PRIMARY-SOURCE | Kaspersky: “substantially different structure” |
| C2 crypto / handshake | **Divergent** — AES-256-GCM JSON wrap vs clear JSON `/beacon` expecting HTTP 400 + `socketId` | High | PRIMARY-SOURCE | PollCat handshake aligns with MiniFast/Retrograde, not NodeRabbit |
| Beacon timing defaults (120s / 5s jitter) | PollCat ≡ MiniFast; NodeRabbit not claimed identical | Moderate | PRIMARY-SOURCE | Do not cite as PollCat↔NodeRabbit code reuse |
| Persistence markers | **Divergent** — `shepherd-persist` Git hooks / fake Copilot VS Code / EdgeUpdate|IntelDSA paths vs `NetSync_*` / `requireObject.js` / `com.harsh.requireobject.plist` / `~/.node_packages` | High | PRIMARY-SOURCE | Distinct hunt catalogs |
| Host ID scheme | **Divergent** — SHA-256 truncate 32 hex vs `129--<hostname>` | High | PRIMARY-SOURCE | |
| Command model | **Divergent** — string cmds (`sys:info`, `persist:vscode`, …) vs hex opcodes (`0x20 EVAL_JS`, …) | High | PRIMARY-SOURCE | |
| Corporate proxy NTLM via curl | NodeRabbit ↔ MiniFast/Retrograde design parallel | Moderate | PRIMARY-SOURCE | Actor-level tradecraft; not PollCat≡NodeRabbit |
| Shared lure archive hashes | RankChallenge MD5 is **PollCat**; Front-Technical* are **NodeRabbit** | High | PRIMARY-SOURCE | Correct IND namespace |
| Trojanized local npm (`colorized_terminal` / `pretty-log` @ 2.1.0) | **NodeRabbit only** — not PollCat | High | PRIMARY-SOURCE | Correction 2026-09-19; NRB-IND-0042–0044. PollCat uses RankChallenge/requireObjects |
| Public GitHub code hits for distinctive strings | None observed (logged-out) for either family’s unique markers | Low (negative) | OBSERVED_PASSIVE | Does not prove absence |

### Bottom line

| Question | Answer |
|----------|--------|
| Same campaign ecosystem / actor (Kaspersky)? | Vendor **High**; ETW reports as Kaspersky attribution |
| Same implant lineage / shared authorship? | **Not established** — default **non-equivalence** |
| Technique overlap worth joint defensive briefings? | Yes — recruiter/coding-challenge + Azure/CF C2 (**Moderate** COMMON TECHNIQUE) |
| Auto-seed pivots across cases? | **No** per `AUTONOMOUS_COLLECTION_POLICY` |
