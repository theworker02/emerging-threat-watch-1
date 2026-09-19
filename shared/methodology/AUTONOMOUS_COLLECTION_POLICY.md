# Autonomous Collection Policy

**Status:** Binding for Emerging Threat Watch collectors and agents  
**Effective:** 2026-09-19  
**Supersedes:** Ad-hoc per-query human approval for permitted passive collection

---

## Operating rule

The research system operates **without** per-query, per-pivot, per-artifact, or per-report human approval for actions listed under **Permitted autonomous actions** (**Tier 0**).

**High-risk lab / egress actions** are **Tier 1**: the agent stages them autonomously via `shared/tooling/gate_ctl.py`, then **stops that workstream until you approve**. See [`GATED_AUTONOMY.md`](GATED_AUTONOMY.md). Approval does **not** authorize Tier-2 prohibited actions.

Autonomy does **not** imply certainty. Every collected object must carry full provenance. A passive observation must **never** automatically become an attribution claim.

---

## Permitted autonomous actions

Collectors and agents **may**, without waiting for approval:

- Query certificate-transparency datasets
- Query passive/historical DNS datasets
- Query RDAP/WHOIS
- Query public URL-analysis services
- Query public malware/sample metadata services (MalwareBazaar, ThreatFox, URLhaus, Triage public reports, InQuest Labs, Any.Run public reports)
- Query public threat-intelligence feeds
- Query public abuse.ch APIs for family tag seeds in `shared/queries/tracker_collection_seeds.csv`
- Search public GitHub / Gist / GitLab metadata and repository history
- Query npm / PyPI registry **metadata** (including 404 negatives) per unconventional staging methodology
- Query paste-site indexes and paste **metadata** (titles, URLs, post dates; no compile/execute)
- Query public open-bucket indexes (GrayhatWarfare-style) and cloud-object **metadata** (HEAD/listing/urlscan) without downloading payloads by default
- Query APK-mirror **listing** metadata and public sandbox Behavior/Screenshots/Dropped Files tabs
- Query **bounded** Shodan / Censys / FOFA on IPs already in `intelligence/infrastructure-ip-ledger.csv` (prefer non-CDN; ports 80/443/8080/8443; depth ≤1)
- Capture unauthenticated HTTP(S) GET screenshots of public pages on hosts **already** in `intelligence/infrastructure-ip-ledger.csv` (webscreenshot/gowitness-style); **new IP fleets** require a Tier-1 `panel_snapshot_fleet` gate ([`GATED_AUTONOMY.md`](GATED_AUTONOMY.md))
- Query Internet Archive / public web archives
- Retrieve publicly available vendor research
- Retrieve public security advisories
- Retrieve public IOC feeds
- Cite publicly reachable underground forum / archive pages as leads (`SECONDARY` / `UNVERIFIED` until corroborated)
- Monitor **public / semi-public** Telegram malware channels via research-oriented OSINT tooling (research accounts only; no token theft)
- Read/archive publicly reachable underground forum or leak-mirror pages (metadata only; no malware execution)
- Calculate hashes of retrieved research artifacts
- Preserve raw API/HTTP responses
- Timestamp observations
- Normalize indicators
- Deduplicate indicators
- Correlate certificates, domains, IPs, hashes and URLs
- Perform **bounded** recursive passive pivots
- Compare observations with vendor-published indicators
- Revisit indicators on a schedule
- Detect infrastructure changes
- Generate timelines and relationship graphs
- Generate evidence ledgers
- Generate source ledgers
- Generate IOC tables
- Generate candidate ATT&CK mappings
- Generate investigative hypotheses
- Generate defensive detection opportunities
- Generate threat-intelligence reports

---

## Prohibited collection actions

Collectors and agents **must not**:

- Execute malware
- Authenticate to attacker-controlled services
- Submit credentials
- Exploit systems
- Brute-force services
- Bypass access controls
- Interact with ransomware negotiation systems
- Send commands to malware C2
- Deploy payloads
- Modify remote infrastructure
- Perform destructive testing
- Purchase malware / crypters / panels
- Join underground communities to operate crimeware
- Scrape or steal Discord / Telegram / Matrix tokens or sessions
- Join **private** E2EE rooms (Matrix / Jabber / Tox / OMEMO) or invite-only criminal channels
- Authenticate to seller panels or attacker C2 UIs
- Download or execute binaries from underground malware archives
- Browse underground / dark-web surfaces from corporate or personal residential IP (human researchers: isolated VM + VPN/Tor only)
- Mass-scan arbitrary IP ranges or perform unsolicited internet-wide port sweeps
- Submit credentials to, or authenticate against, suspected attacker login panels (including “just looking”)
- Download/execute staging payloads (MSI/PS1/ZIP/APK/npm tarballs) onto analysis hosts without an isolated-lab note
- JARM / SSL pivots from certificates that are not already known-bad in evidence or PRIMARY sources

If a task would require any prohibited action, **stop** and record the gap. Do not ask for an exception under this policy.

**Gated carve-out (Tier 1 only):** Isolated-lab malware detonation, MalwareBazaar binary download, memory dump after detonation, abuse.ch IOC submission, and expansion scans beyond ledger seeds may be **staged** with `gate_ctl.py submit` and executed **only after** your explicit `approve`. That is human-authorized lab work, not autonomous execution. Agents must never silently escalate.

---

## Underground / dark-web OSINT (Telegram / Discord / forums / trackers)

Defensive monitoring of commodity RAT, crypter, and APT-adjacent **marketplace / channel surfaces** is permitted only as described in [`UNDERGROUND_AND_COMMODITY_RAT_OSINT.md`](UNDERGROUND_AND_COMMODITY_RAT_OSINT.md) (canonical; includes APT-tier dark-web notes). Framing is collection methodology — not operational crimeware participation. Stub alias: [`APT_AND_DARKWEB_OSINT.md`](APT_AND_DARKWEB_OSINT.md).

### Permitted (autonomous)

- Public malware-tracker queries (ThreatFox, MalwareBazaar, URLhaus, Triage metadata, InQuest Labs, Any.Run **public** reports) and abuse.ch API tag searches from `tracker_collection_seeds.csv`
- Licensed commercial CTI underground feeds (Flashpoint, KELA, Intel471, ZeroFox, Flare.io, equivalents) when the organization already has access
- Archival leak / public-mirror **research** of Telegram/Discord/forum dumps including vx-underground archives (read metadata; no malware execution)
- Public underground-forum **read/archive** (XSS.is, Exploit.in, BreachForums, DarkForums, RaidForums archives, etc.) when publicly reachable without prohibited authentication — provenance `SECONDARY` / `UNVERIFIED` until corroborated
- Public / semi-public Telegram malware-channel monitoring via research OSINT tooling (Telepathy / TGMind / TGScraper examples; research accounts only)
- Citing forum/Telegram ads as `ASSOCIATION_ONLY` / `UNVERIFIED` leads pending corroboration

### Prohibited

- Purchase malware, crypters, panels, or cracked tooling
- Join underground Discord/Telegram communities in order to **operate** crimeware or assist sellers/buyers
- Autonomous join of **private** E2EE rooms (Matrix / Jabber / Tox / OMEMO) — private-channel intel is a **commercial-CTI dependency** (Showboat-tier)
- Scrape, steal, or reuse Discord / Telegram / Matrix tokens or sessions
- Authenticate to seller shops or attacker C2 panels (“just looking” is still prohibited)
- Download/execute malware binaries from vx-underground or similar archives
- Provide setup, cracking, or operational help for RATs
- Use corporate or personal residential IP for underground browsing (human researchers: isolated VM + VPN/Tor)

### Takedown evidence quality

Prefer Message Links, Server/Channel IDs, and lawfully obtained PCAP over screenshots alone when preparing Trust & Safety or LE referrals.

Seeds: [`../queries/tracker_collection_seeds.csv`](../queries/tracker_collection_seeds.csv).

---

## Unconventional staging OSINT (developer platforms / cloud / APK / bounded footprinting)

Defensive monitoring of **public** developer-platform staging, open-bucket delivery, APK-mirror listings, and **bounded** internet search of already-flagged C2 IPs is permitted only as described in [`UNCONVENTIONAL_STAGING_OSINT.md`](UNCONVENTIONAL_STAGING_OSINT.md). This layer is complementary to underground OSINT — it does not authorize dark-web participation.

### Permitted (autonomous)

- Bounded Shodan / Censys / FOFA queries against IPs already in `intelligence/infrastructure-ip-ledger.csv` (prefer non-`cdn_edge`; ports 80/443/8080/8443; fan-out depth ≤1)
- Paste-site / npm / PyPI / GitHub / GitLab **metadata** queries (including registry 404 negatives)
- Public open-bucket **metadata** and filename-index queries (GrayhatWarfare-style); urlscan/VT URL metadata for object URLs
- APK-mirror listing metadata; public VT / Hybrid-Analysis Behavior / Screenshots / Dropped Files tabs
- Unauthenticated HTTP(S) GET page snapshots of public endpoints on flagged hosts
- JARM / SSL fingerprint pivots **only** from known-bad certificates already in evidence or PRIMARY sources

### Prohibited

- Authenticate to attacker C2 panels or submit credentials to suspected login UIs
- Execute malware or compile/load retrieved staging source (e.g. Pastebin C) on analysis hosts without isolated-lab documentation
- Mass unsolicited scanning of arbitrary ranges / random internet hosts
- Treat shared CDN/cloud edges as actor-owned seeds for fan-out
- Cross-seed PollCat ↔ NodeRabbit (or other families) from shared lure-class techniques without linkage evidence

**Provenance:** discovered object URL or registry response retrieved by ETW = `OBSERVED_PASSIVE` (metadata fact). Do **not** download/execute payloads into the analysis host by default.

Seeds: [`../queries/unconventional_staging_seeds.csv`](../queries/unconventional_staging_seeds.csv).

---

## Required fields on every collected object

| Field | Requirement |
|-------|-------------|
| `collected_utc` | Collection timestamp (UTC) |
| `collection_mechanism` | How it was obtained (e.g. `crt.sh JSON`, `RDAP GET`) |
| `originating_service` | Service/API name |
| `original_query` | Exact query string or URL |
| `raw_response_ref` | Path to preserved raw response |
| `sha256` | SHA-256 of preserved evidence bytes |
| `provenance` | Classification from vocabulary below |
| `confidence` | High / Moderate / Low |
| `relationship_type` | How this object relates to a family/indicator (see below) |
| `first_seen` / `last_seen` | When available from the source |

---

## Provenance classification (collection layer)

| Code | Meaning |
|------|---------|
| `OBSERVED_PASSIVE` | Independently collected by ETW via permitted passive methods |
| `PRIMARY-SOURCE` | Published by the original analyzing organization/researcher |
| `CORROBORATED` | Independent ETW passive evidence supports a vendor-published relationship |
| `SECONDARY` | Repeats or summarizes another source |
| `INFERRED` | Analytical conclusion derived from evidence; not directly demonstrated |
| `UNVERIFIED` | Exists as claim/lead; insufficient substantiation |
| `CONTRADICTED` | Reliable evidence conflicts |
| `ASSOCIATION_ONLY` | Weak co-occurrence (e.g. same hosting provider) — not ownership |
| `INFRASTRUCTURE_OVERLAP` | Shared technical artifact (e.g. same IP as a known campaign domain) — not actor identity |

### Legacy alias

`OBSERVED` in older ledgers means **independently observed by this investigation**. New passive collection rows **must** use `OBSERVED_PASSIVE` so vendor-retrieved articles are never confused with CT/pDNS observations.

**Retrieving a vendor page = `PRIMARY-SOURCE` artifact preservation. It is never `OBSERVED_PASSIVE` infrastructure.**

---

## Relationship type (mandatory ladder)

Use the narrowest true statement. Do not climb the ladder without evidence.

| Observation | Classification |
|-------------|----------------|
| CT certificate contains `example.com` | `OBSERVED_PASSIVE` |
| Historical DNS maps `example.com` → `192.0.2.10` | `OBSERVED_PASSIVE` |
| Vendor says `example.com` belongs to Rapuncel | `PRIMARY-SOURCE` |
| Our CT/pDNS independently supports that relationship | `CORROBORATED` |
| Same hosting provider as Rapuncel infrastructure | `ASSOCIATION_ONLY` |
| Same IP as a known Rapuncel domain | `INFRASTRUCTURE_OVERLAP` |
| Therefore operated by the Rapuncel actor | **NOT ESTABLISHED** without additional evidence |

Attribution, operator identity, and campaign authorship are **never** auto-emitted by collectors.

---

## Bounded recursive pivots

Autonomous pivots are allowed only when:

1. The seed indicator is already in a family ledger or vendor PRIMARY-SOURCE list  
2. Depth is capped (default **depth ≤ 2** unless a research plan raises it)  
3. Shared CDN/cloud edges (Cloudflare, Azure Websites, etc.) are **not** treated as actor-owned seeds for fan-out  
4. Each hop writes a raw response + manifest row before the next hop  
5. Case isolation is preserved — Rapuncel pivots do not seed Settra/RatHat/NodeRabbit/PollCat/SynkLoader/Showboat unless linkage evidence exists. **PollCat pivots do not auto-seed NodeRabbit** (and vice versa), even when the seed appears in the shared Securelist article.

---

## Evidence tree (physical enforcement)

```
evidence/
├── primary-sources/{rapuncel,settra,rathat,noderabbit,pollcat,synkloader,showboat}/
├── passive-observations/
│   ├── certificate-transparency/
│   ├── rdap/
│   ├── dns/
│   ├── urlscan/
│   ├── github/
│   ├── archives/
│   ├── sample-metadata/
│   ├── trackers/
│   ├── staging/          # npm/paste/bucket metadata (optional)
│   └── shodan-censys/    # bounded ledger-IP queries (optional)
└── manifests/
    ├── primary-source-manifest.csv
    └── passive-observation-manifest.csv
```

- Primary retrieval → primary-sources/ + PRIMARY-SOURCE  
- Passive CT/pDNS/RDAP/… → passive-observations/ + OBSERVED_PASSIVE  
- Tracker API queries → passive-observations/trackers/ + OBSERVED_PASSIVE  
- Staging registry/paste/bucket metadata → passive-observations/ (+ optional staging/) + OBSERVED_PASSIVE  
- Empty passive manifests are correct until collection runs  
- PollCat may dual-reference the NodeRabbit Securelist HTML (PS-POL-001 ≡ PS-NRB-001 bytes) without merging cases

---

## Reporting and IC3

Autonomous report generation is permitted. **Filing** to IC3/FBI still requires human review (`reports/law-enforcement/SUBMISSION_CHECKLIST.md`). Collectors must not auto-submit complaints.

---

## Related documents

- [`METHODOLOGY.md`](../../METHODOLOGY.md)  
- [`UNDERGROUND_AND_COMMODITY_RAT_OSINT.md`](UNDERGROUND_AND_COMMODITY_RAT_OSINT.md)  
- [`UNCONVENTIONAL_STAGING_OSINT.md`](UNCONVENTIONAL_STAGING_OSINT.md)  
- [`APT_AND_DARKWEB_OSINT.md`](APT_AND_DARKWEB_OSINT.md)  
- [`TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`](TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md) — high-fidelity lawful PCAP/sandbox/hosting-abuse evidence (human lab; agents do not execute malware)  
- [`CASE_ISOLATION.md`](CASE_ISOLATION.md)  
- [`EVIDENCE_ID_POLICY.md`](EVIDENCE_ID_POLICY.md)  
- [`../queries/collection_instructions.md`](../queries/collection_instructions.md)  
- [`../queries/tracker_collection_seeds.csv`](../queries/tracker_collection_seeds.csv)  
- [`../queries/unconventional_staging_seeds.csv`](../queries/unconventional_staging_seeds.csv)  
- [`../../evidence/README.md`](../../evidence/README.md)  
- [`../../docs/ENFORCEMENT_READINESS.md`](../../docs/ENFORCEMENT_READINESS.md)
