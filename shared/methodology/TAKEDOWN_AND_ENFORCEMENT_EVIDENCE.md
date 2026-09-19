# Takedown & Enforcement Evidence (High-Fidelity Lawful Collection)

**Status:** Defensive methodology (Emerging Threat Watch)  
**Effective:** 2026-09-19  
**Audience:** Human analysts assembling hosting-provider / registrar / platform abuse packages and LE technical annexes  
**Binding autonomy:** [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md)

---

## Framing (mandatory)

This document defines **high-fidelity evidence** useful for lawful enforcement and infrastructure takedown. It does **not** authorize autonomous malware execution, C2 panel login, credential submission, exploitation, or inventing IOCs.

| Path | Who collects | What ETW agents may do |
|------|--------------|------------------------|
| **Passive / metadata** | Autonomous collectors | CT, pDNS, RDAP, tracker APIs, public sandbox *report* metadata, bounded Shodan/Censys/FOFA on ledger IPs, unauthenticated banners/snapshots |
| **Interactive sandbox telemetry & PCAPs** | Human isolated lab **or** licensed commercial platforms (ANY.RUN, Triage, Hybrid Analysis, Cuckoo/CAPEv2) | Agents may **cite** public sandbox reports and retain licensed-platform exports provided by a human; agents **must not** execute malware |

**Still never:** authenticate to attacker C2 panels, send commands to malware, purchase panels, or scrape Discord/Telegram tokens.

**OpSec (human lab):** Use isolated analysis networks; no corporate/personal accounts on attacker surfaces; prefer licensed sandboxes over raw internet detonation; retain chain-of-custody notes (who ran what, when, under which license).

**Related:** [`C2_IP_DISCOVERY.md`](C2_IP_DISCOVERY.md) (sandbox config extract, pDNS behind CDN, ThreatFox bulk, IP extractor script).

**Package templates:** [`../../reports/law-enforcement/TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](../../reports/law-enforcement/TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md)  
**Schema (optional metadata):** [`../schemas/takedown-evidence.schema.json`](../schemas/takedown-evidence.schema.json)  
**Readiness gaps:** [`../../docs/ENFORCEMENT_READINESS.md`](../../docs/ENFORCEMENT_READINESS.md)

---

## A. Interactive sandbox telemetry & PCAPs

**Platforms (human / licensed):** ANY.RUN · Joe Sandbox / Triage · Hybrid Analysis · Cuckoo / CAPEv2 (air-gapped or controlled lab).

**Capture checklist (retain with timestamps, UTC):**

| Artifact | Why it matters for takedown / LE |
|----------|----------------------------------|
| Timed PCAP | Proves check-in to IP:port; supports hosting abuse with concrete traffic |
| HTTP request/response headers | Host, User-Agent, URI paths, status codes without panel auth |
| TLS certificate material | Leaf/issuer fingerprints, SNI, JA3/JARM where available |
| Memory dumps | Config extraction (C2 host, ports, keys) when lawful |
| Execution video / behavior log | Corroborates process tree and network timing |
| Sample SHA-256 | Anchors all other artifacts to one binary |

**ETW autonomous collectors do NOT execute malware.** Sandbox PCAP is a **human-lab / licensed-platform** path. Autonomous agents may:

- Query **public** Triage / ANY.RUN / Hybrid Analysis **report pages** and metadata APIs (per autonomous policy);
- Record report URLs, published network IOCs, and public screenshots;
- Attach human-exported PCAP/config packages under investigation evidence with clear provenance (`OBSERVED` only if ETW human lab produced them; else `PRIMARY-SOURCE` / licensed-platform export note).

Do **not** treat vendor blog network tables as ETW-owned PCAPs.

---

## B. Direct infrastructure & SSL scanning

**Scope:** Only IPs **already flagged** in [`../../intelligence/infrastructure-ip-ledger.csv`](../../intelligence/infrastructure-ip-ledger.csv). Prefer non-`cdn_edge` rows. Fan-out depth ≤1. Ports typically 80/443/8080/8443 (and family-documented ports such as MeshCentral/MeshAgent when already published).

**Tools:** Shodan · Censys · FOFA · ZoomEye (licensed where required).

**Allowed outputs:**

- JARM / JA3S / header fingerprints  
- Unauthenticated banner grabs  
- TLS cert serial / subject / issuer snapshots  
- Public HTTP(S) GET screenshots (webscreenshot/gowitness-style)  

**Prohibited:** Panel login, credential stuffing, authenticated API probes, mass scanning of arbitrary ranges, inventing IPs not in ledgers or PRIMARY sources.

Complementary methodology: [`UNCONVENTIONAL_STAGING_OSINT.md`](UNCONVENTIONAL_STAGING_OSINT.md) § internet-wide search.

---

## C. Passive DNS & hash repositories

Use these to **correlate** sample identity and historical resolution — not to invent new campaign membership.

| Source | Typical use |
|--------|-------------|
| VirusTotal Intelligence | Hash reputation, community comments, historical resolutions (authorized access) |
| ThreatFox (abuse.ch) | IOC search/submit; Auth-Key required for current APIs |
| MalwareBazaar (abuse.ch) | Sample metadata / hash presence |
| SecurityTrails / PassiveTotal | pDNS history for domains already in case ledgers |
| URLhaus (abuse.ch) | Malicious URL correlation |

Empty / 401 / captcha-blocked queries are valid **NEGATIVE SEARCH RESULT** dispositions — not proof of absence. See [`UNDERGROUND_AND_COMMODITY_RAT_OSINT.md`](UNDERGROUND_AND_COMMODITY_RAT_OSINT.md) for Auth-Key notes.

---

## Standardized evidence packages

Minimum fields by **target type**. Screenshots alone are insufficient for hosting/registrar packages.

| Target type | Required technical core | Supplementary |
|-------------|-------------------------|---------------|
| **C2 / Hosting** | IP + port; timed PCAP (or licensed sandbox network export); extracted C2 config (when available); sample **SHA-256** | TLS cert snapshot; JARM/headers; RDAP/ASN abuse contact (hosting admin ≠ author) |
| **Registrar / DNS** | Domain; active resolution (A/AAAA/NS); pDNS history; sample hash showing check-in to that name | CT logs; WHOIS/RDAP redacted as published; registrar abuse template |
| **Discord / Telegram** | Message or channel links; Server / Channel / User IDs; timestamped message logs (export or archival copy) | Screenshots (supplementary only); never stolen tokens/sessions |

**Provenance vocabulary** must match [`../../METHODOLOGY.md`](../../METHODOLOGY.md): distinguish `PRIMARY-SOURCE` vendor IOCs from `OBSERVED_PASSIVE` ETW enrichment and from human-lab `OBSERVED` sandbox runs.

Fillable checklist: [`../../reports/law-enforcement/TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](../../reports/law-enforcement/TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md).

---

## Collaboration channels

| Channel | Use |
|---------|-----|
| **abuse.ch** (ThreatFox / URLhaus / MalwareBazaar) | Submit verified IOCs with Auth-Key when available; retain submission IDs |
| **ISACs** | Sector sharing of high-fidelity packages (no binaries in mail unless channel policy allows) |
| **STIX 2.1 / TAXII** | Package indicators, observables, and sightings for partner TI platforms |

STIX packaging should reference ETW evidence IDs and provenance codes; do not upgrade `ASSOCIATION_ONLY` CDN edges to actor-owned infrastructure.

---

## Two audiences (do not confuse)

| Package class | Audience | Emphasis |
|---------------|----------|----------|
| **FBI / IC3 narrative** | Law enforcement tip / complaint channels | Crime-type language, narrative, PRIMARY sources, caveats; see [`../../reports/law-enforcement/HOW_TO_FILE.md`](../../reports/law-enforcement/HOW_TO_FILE.md) |
| **Hosting / registrar / platform takedown** | Abuse desks, registrars, Discord/Telegram Trust & Safety | IP:port + PCAP + hash + timestamps; less narrative, more telemetry |

Both need **technical telemetry**. IC3 forms often cannot accept PCAPs — retain them offline and state availability. Hosting abuse tickets usually **require** IP/port and proof of malicious traffic.

---

## Safety recapitulation

1. No malware execution by autonomous agents.  
2. No authentication to attacker C2 panels or seller shops.  
3. No invented hashes, domains, IPs, or chat IDs.  
4. One family = one package unless linkage evidence is documented.  
5. Human review before any external submission (IC3, FBI, abuse.ch, registrar, ISAC).  
6. OpSec for any human lab detonation or underground-adjacent browsing.

---

## Related documents

- [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md)  
- [`UNCONVENTIONAL_STAGING_OSINT.md`](UNCONVENTIONAL_STAGING_OSINT.md)  
- [`UNDERGROUND_AND_COMMODITY_RAT_OSINT.md`](UNDERGROUND_AND_COMMODITY_RAT_OSINT.md)  
- [`../../reports/law-enforcement/HOW_TO_FILE.md`](../../reports/law-enforcement/HOW_TO_FILE.md)  
- [`../../reports/law-enforcement/SUBMISSION_REPORT.TEMPLATE.md`](../../reports/law-enforcement/SUBMISSION_REPORT.TEMPLATE.md)  
- [`../../reports/law-enforcement/TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](../../reports/law-enforcement/TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md)  
- [`../../docs/ENFORCEMENT_READINESS.md`](../../docs/ENFORCEMENT_READINESS.md)  
- [`../../intelligence/infrastructure-ip-ledger.csv`](../../intelligence/infrastructure-ip-ledger.csv)  
- [`../../intelligence/priority-gaps.csv`](../../intelligence/priority-gaps.csv)
