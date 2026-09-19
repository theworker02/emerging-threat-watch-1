# Campaign infrastructure IP research note

**Scope:** Emerging Threat Watch catalogs **lawfully obtainable campaign-infrastructure IP addresses** associated with published malware families (Rapuncel, Settra, RatHat, NodeRabbit, PollCat, SynkLoader, Showboat).

**Not in scope:** Personal / residential IPs of named individuals; geolocation-to-person claims; “this is the malware author’s home IP”; active exploitation; authenticating to C2; malware execution.

**Ledger:** `intelligence/infrastructure-ip-ledger.csv`  
**Policy:** `shared/methodology/AUTONOMOUS_COLLECTION_POLICY.md`

---

## What this corpus establishes

| Statement | Status |
|-----------|--------|
| Vendors published specific IPs as campaign exfil / MeshAgent / Showboat infra | **Yes** (PRIMARY-SOURCE rows) |
| ETW passively resolved some campaign domains to current A/AAAA | **Yes** (OBSERVED_PASSIVE; raw under `evidence/passive-observations/dns/`) |
| Shared Cloudflare / Azure edges appear in front of campaign domains | **Yes** — labeled `cdn_edge` / `ASSOCIATION_ONLY` (low specificity) |
| Any IP “belongs to” a named malware author / creator as a personal endpoint | **NOT ESTABLISHED** — default for every row unless a public court / LE filing says otherwise |

**Author / personal-identity attribution from this IP ledger: NOT ESTABLISHED.**

RDAP/WHOIS contacts on IP allocations are typically **ISP, hosting, or network-admin roles**. They are **not** proof of malware authorship and must not be treated as doxing leads.

---

## Provenance ladder (applied)

1. **PRIMARY-SOURCE** — IP named in a vendor/LE-published report or official IOC list (e.g. LastPass/Delphos, Huntress, Black Lotus Labs `Showboat_IOCs.txt`).
2. **OBSERVED_PASSIVE** — ETW historical/current DNS A/AAAA or public RDAP/urlscan of an already-seeded indicator.
3. **ASSOCIATION_ONLY** — Same CDN/cloud edge as a campaign domain (Cloudflare 104.21/172.67/188.114, Azure App Service / Blob). Useful for chronology only; **do not promote as actor-owned**.
4. **INFRASTRUCTURE_OVERLAP** — Same non-CDN IP as a known campaign domain (still not personal identity).
5. **“Therefore this is the author’s home IP”** — **NOT ESTABLISHED** without a public court/LE primary naming that fact.

---

## Highest-value (non-CDN) infrastructure leads

These are the best FBI/IC3 **infrastructure correlation** leads in the corpus — not identity conclusions:

| Family | IP | Role | Provenance |
|--------|-----|------|------------|
| Rapuncel | `2.26.126.50` | Exfil (`/upload`) | PRIMARY (LastPass/Delphos) |
| Settra | `45.13.122.7` | MeshAgent C2 (July IR) | PRIMARY (Huntress) |
| Settra | `193.5.65.114` | MeshAgent C2 (Sept IR) | PRIMARY (Huntress) |
| SynkLoader | `149.248.76.220` | C2 A for `neversoftmain.net` | OBSERVED_PASSIVE (domain PRIMARY Expel) |
| SynkLoader | `162.33.177.8` | C2 A for `rootfarmapp.net` | OBSERVED_PASSIVE |
| SynkLoader | `216.245.184.14` | C2 A for `tripinupdate.net` | OBSERVED_PASSIVE |
| SynkLoader | `64.94.85.67` | A for `aroclenetapp.net` | OBSERVED_PASSIVE |
| Showboat | `114.116.239.178` and peers in BLL IOC file | Malware hosting / C2 table | PRIMARY (Black Lotus Labs) |

Rapuncel clustering-lead domain `ryanpresbrey.cc` currently resolves to non-CDN `207.207.210.23/36/50` (**INFRASTRUCTURE_OVERLAP**, Moderate) — useful pivot only; LastPass marks the domain itself as a clustering lead, not confirmed ownership.

---

## Families still lacking usable host IPs

| Family | Gap |
|--------|-----|
| **RatHat** | Zimperium publishes URI paths + local `127.0.0.1:7910` only. No remote C2/FRP host IPs in the primary article. Community IOC domains are ASSOCIATION_ONLY until a PRIMARY source corroborates. |
| **PollCat** | Co-disclosed with NodeRabbit; public Securelist IOC list is domain/MD5-heavy with no PollCat-only IPv4 rows in ETW `POL-IND` (published-indicators still header-only). |
| **NodeRabbit** | Vendor domains are almost entirely Azure Websites or Cloudflare-fronted; edge IPs are demoted. Prefer domains + `agent:servers` mutability caveats. |

---

## How LE should use this

- Treat rows as **campaign infrastructure leads** for correlation (sinkholing history, hosting abuse, certificate timelines, victim telemetry).
- Prefer **non-CDN** PRIMARY and high-confidence OBSERVED_PASSIVE IPs.
- Do **not** convert CDN edges or RDAP registrant names into personal attribution.
- ETW has **not** filed IC3 as part of this research pass; this note does not authorize identity claims.

---

## Collection artifacts (this pass)

- Passive DNS raw: `evidence/passive-observations/dns/{family}/`
- IP RDAP raw: `evidence/passive-observations/rdap/{family}/rdap_ip_*`
- Manifest: `evidence/manifests/passive-observation-manifest.csv` (`OBSERVED_PASSIVE`)
- Showboat vendor IOC: `evidence/primary-sources/showboat/Showboat_IOCs_2026-09-19T190009Z.txt`
- Collector: `shared/tooling/collect_infra_ips.py`

Cutoff: 2026-09-19.

---

## Commodity RAT panels on Telegram (methodology)

Seller panels for commodity RATs (classic Remcos / AsyncRAT / njRAT patterns — **illustrations only**) often display C2 IPs in Telegram/Discord screenshots.

| Claim type | Provenance |
|------------|------------|
| C2 IP visible only in a panel screenshot | SECONDARY / UNVERIFIED until corroborated |
| C2 extracted from sample configs via Triage / ThreatFox / vendor PRIMARY | Prefer PRIMARY-SOURCE or ETW OBSERVED_PASSIVE per retrieval path |
| "Author home IP" from a panel screenshot | **NOT ESTABLISHED** — never emit |

See shared/methodology/UNDERGROUND_AND_COMMODITY_RAT_OSINT.md. ETW active families remain Rapuncel / Settra / RatHat / NodeRabbit / PollCat / SynkLoader / Showboat — do not invent tracker hits.

