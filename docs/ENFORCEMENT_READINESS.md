# Enforcement Readiness — Takedown Evidence Gaps

**Status:** Snapshot vs high-fidelity standard in [`shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`](../shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md)  
**Cutoff:** 2026-09-20  
**Rule:** ETW autonomous collectors do **not** produce sandbox PCAPs. Rows below reflect ledger / published-indicator state, not invented IOCs.

**Multi-channel filing:** [`reports/law-enforcement/RESPONSIBLE_SUBMISSION/`](../reports/law-enforcement/RESPONSIBLE_SUBMISSION/) (IC3 → optional FBI tips → vendor/CERT briefs → hosting only when PCAP-ready). Complainant PII is gitignored under `reports/law-enforcement/private/COMPLAINANT_PROFILE.md`.

**STIX / IOC evidentiary package (LE ingest):** [`reports/law-enforcement/CTI-Evidence-Repository/`](../reports/law-enforcement/CTI-Evidence-Repository/) — standardized family folders, STIX 2.1 bundles, checksums, TLP:AMBER+STRICT. PCAPs still require human/licensed lab (see readiness table below).

**Standard (minimum for hosting/registrar packages):**

| Target | Need |
|--------|------|
| C2/Hosting | IP+port, timed PCAP, C2 config (if available), SHA-256 |
| Registrar/DNS | Domain, active resolution, pDNS history, sample hash showing check-in |
| Chat | Links + Server/Channel/User IDs + timestamped logs |

---

## Per-family matrix

| Family | Sample SHA-256 | Non-CDN / usable infra IP | Domains for DNS package | ETW / lab PCAP | C2 config extract | Chat-platform IDs | Enforcement readiness | P0 gap |
|--------|----------------|---------------------------|-------------------------|----------------|-------------------|-------------------|----------------------|--------|
| **Rapuncel** | **Have** (PRIMARY; multiple LastPass/Delphos hashes) | **Partial** — `2.26.126.50` exfil PRIMARY; non-CDN `207.207.210.x` OBSERVED_PASSIVE clustering; many CF edges ASSOCIATION_ONLY | **Have** (PRIMARY delivery / C2 domains) | **Lack** | **Lack** (no ETW lab extract) | N/A (stealer targets Discord/Telegram data; not seller-channel package) | **Moderate** for DNS/hash narrative; **weak** for hosting abuse without PCAP | Human/licensed sandbox PCAP against known SHA-256 + timed check-in |
| **Settra** | **Lack** (no usable SHA-256 in published-indicators; filenames/extensions only) | **Have** MeshAgent IPs `45.13.122.7`, `193.5.65.114` (latter exclusivity UNKNOWN) | Sparse (hostname lead `WIN-LIVFRVQFMKO`, not registrar package) | **Lack** | **Lack** | N/A | **Low** — infra leads without sample hash/PCAP | **P0:** verified outer/inner SHA-256 + sandbox PCAP to MeshAgent IP:port |
| **RatHat** | **Partial** — Zimperium IOC repo lists APK SHA-256s (e.g. RAT-IND-0040 representative of 162); PRIMARY article body lacked hashes | **Lack** confirmed remote C2 — PRIMARY is `127.0.0.1:7910`; community domains ASSOCIATION_ONLY | Package **names / applicationId** still open | **Lack** | **Lack** (FRP hosts runtime-fetched) | N/A | **Low–Moderate** for sample identity; **low** for hosting takedown | **P0:** package names + concrete FRP/C2 hosts without interaction; APK sandbox network export |
| **NodeRabbit** | **Partial** — Kaspersky lure archives are **MD5**; PolySwarm SHA-256s are RELATED_SAMPLE (not confirmed MD5 maps) | **Lack** actor-owned — mostly Cloudflare edges ASSOCIATION_ONLY; Azure App Service domains | **Have** PRIMARY domains | **Lack** | **Lack** | N/A | **Low–Moderate** for domain narrative; hash correlation blocked | **P0:** MD5→SHA-256 resolution + sandbox PCAP on non-CDN resolution if/when available |
| **PollCat** | **Lack** SHA-256 — lure zip is **MD5** only (POL-IND-0001) | **Lack** — no PollCat rows in infrastructure-ip-ledger | **Have** PRIMARY C2 domains (`sahi-finance.com`, Azure hosts, `lifespotify.com`) | **Lack** | **Lack** | N/A | **Low** for hosting; **Moderate** domain leads without check-in hash | **P0:** RankChallenge MD5→SHA-256; PollCat-only host IPv4; sandbox PCAP |
| **SynkLoader** | **Have** (Expel PRIMARY; multiple module SHA-256s) | **Have** OBSERVED_PASSIVE A records for PRIMARY C2 domains (non-CDN) | **Have** | **Lack** | **Lack** | N/A (Teams phishing is channel narrative, not Discord/Telegram ID package) | **Moderate–High** pending PCAP | Licensed sandbox PCAP to ledger C2 IP:443 tying SHA-256↔host |
| **Showboat** | **Have** (BLL / Lumen PRIMARY sample hashes) | **Have** multiple PRIMARY C2 IPs in ledger | **Have** (e.g. telecom impersonation domains) | **Lack** | **Lack** (no ETW extract) | N/A (Pastebin staging ≠ chat T&S package) | **Moderate–High** pending PCAP | Human/licensed PCAP + optional config extract for priority C2 IP:443 |
| **Abyssos** | **Have** (Zscaler PRIMARY SHA-256s) | **Have** PRIMARY C2 IPv4 in package CSV | Sparse / campaign domains as published | **Lack** | **Lack** | N/A | **Moderate** pending PCAP | Licensed PCAP tying published SHA-256 ↔ C2 IP:port |
| **SharkLoader** | **Partial** — public Securelist IOC block is **MD5**-heavy | **Lack** C2 IPv4 in public IOC appendix | **Have** PRIMARY domains (`connect-microsoft.com`, `ms-record.*`, `ms-tray.top`) | **Lack** | **Lack** | N/A | **Moderate** for DNS narrative; **low** for hosting | MD5→SHA-256 where possible; PCAP to resolved non-CDN hosts |
| **TencShell** | **Partial / Have** per Cato–Hunt.io published set | **Have** PRIMARY IPv4 (e.g. `45.64.52.242`, `192.238.134.166`, …) | Sparse hostnames as published | **Lack** | **Lack** | N/A | **Moderate** pending PCAP | Timed PCAP on published IP:port + sample hash anchor |
| **MiniFast** | **Partial** — Azure Web App staging; hash coverage varies by source | **Lack** prioritized standalone C2 IPv4 | **Have** Azure Web App hostnames | **Lack** | **Lack** | N/A | **Low–Moderate** (cloud hostname narrative) | SHA-256 + provider abuse package; do **not** merge PollCat |
| **Argamal** | **Partial** per Securelist published set | **Partial** — limited PRIMARY IPv4 (e.g. `186.158.223.35`) | Staging paths / domains as published | **Lack** | **Lack** | N/A | **Low–Moderate** | Expand hash identity; PCAP if non-CDN IP remains live |
| **Okobot** | **Partial** — public vs Kaspersky TI-extended IoCs | **Have** PRIMARY IPv4 in package CSV | Domains as published | **Lack** | **Lack** | N/A | **Moderate** pending PCAP | Do not invent TI-service-only IoCs; PCAP on published IPs |
| **Matanbuchus** | **Have / Partial** across Huntress–Morphisec–Zscaler–eSentire | **Have** PRIMARY IPv4 in package CSV | Domains as published | **Lack** | **Lack** | N/A (Teams = channel narrative) | **Moderate** pending PCAP | Keep **separate** from SynkLoader (COMMON TECHNIQUE only) |
| **StarlandRAT** | **Partial / Have** per Talos appendix | **Have** multiple PRIMARY IPv4 | Domains / WLDR hosts as published | **Lack** | **Lack** | N/A | **Moderate** pending PCAP | PCAP + SHA-256; crypto-contract address ≠ hosting target |

**Global gap:** No family currently retains an **ETW human-lab or licensed-platform timed PCAP** in-repo. That is expected under autonomous policy and is a **program P0 for enforcement readiness**, not a collector bug.

---

## Priority actions (program)

1. **Settra / RatHat / PollCat / NodeRabbit / SharkLoader hash identity** — close SHA-256 (or APK package identity) gaps already listed in `intelligence/priority-gaps.csv`.  
2. **Sandbox PCAP campaign (human)** — for families with SHA-256 + non-CDN IP (Rapuncel exfil, SynkLoader / Showboat / Abyssos / TencShell / Okobot / StarlandRAT C2s first).  
3. **Bounded passive enrichment** — JARM/headers/screenshots on ledger non-CDN IPs only (`UNCONVENTIONAL_STAGING_OSINT`).  
4. **abuse.ch submissions** — when Auth-Key available and indicators are PRIMARY or OBSERVED with clear provenance.  
5. **IC3 packages 10–15** — file paste-ready packs (`IC3_PASTE_READY.md`) using private complainant profile; then optional vendor/CERT briefs under `RESPONSIBLE_SUBMISSION/briefs/`.

Track operational gaps in [`../intelligence/priority-gaps.csv`](../intelligence/priority-gaps.csv). Package fill: [`../reports/law-enforcement/TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](../reports/law-enforcement/TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md).
