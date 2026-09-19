# Underground, Dark Web & Commodity / APT-Adjacent OSINT

**Status:** Defensive collection methodology (Emerging Threat Watch)  
**Effective:** 2026-09-19  
**Binding policy:** [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md)  
**Alias / split:** APT-tier channel notes live **here** (not a separate contradictory policy). If a sibling `APT_AND_DARKWEB_OSINT.md` is added, it must only cross-link — not redefine permitted/prohibited actions. Developer-platform / cloud staging OSINT is a separate complementary layer: [`UNCONVENTIONAL_STAGING_OSINT.md`](UNCONVENTIONAL_STAGING_OSINT.md).

---

## Framing (mandatory)

This document describes **defensive intelligence collection**: how defenders monitor public, archival, and licensed surfaces that commodity RAT / crypter sellers and higher-tier operators use, and how to map those surfaces to ETW families.

It is **not** guidance for:

- buying or installing malware;
- joining criminal Discord/Telegram/Matrix rooms to operate panels;
- cracking forums, stealing tokens, or harvesting credentials;
- authenticating to attacker C2 panels;
- downloading or executing binaries from underground archives;
- autonomous collectors joining **private** E2EE rooms (Matrix/Jabber/Tox/OMEMO).

Classic Remcos / AsyncRAT / njRAT mentions in researcher notes are **methodology illustrations** of commodity-RAT marketplace patterns. ETW **active families** are Rapuncel, Settra, RatHat, NodeRabbit, PollCat, SynkLoader, and Showboat. Cruciferra / PUROSANGUE appear as **ASSOCIATION_ONLY** crypter-marketplace leads unless a primary source ties them to a specific family chain. Russian-linked commodity loaders/stealers (Matanbuchus, AstarionRAT, StarlandRAT, Lumma/Vidar/RedLine, Pikabot/QakBot) remain in the **CANDIDATE** pipeline with technique/market comparators only — see [`../../docs/CANDIDATE_FAMILIES.md`](../../docs/CANDIDATE_FAMILIES.md) and [`../../docs/TECHNIQUE_COMPARATORS.md`](../../docs/TECHNIQUE_COMPARATORS.md).

---

## 1) Underground forums (monitor / cite — do not buy)

Public or CTI-indexed forums often advertise commodity RATs, crypters, IAB/droppers, and Discord CDN loaders. **Monitor and cite only.** Default provenance for forum posts/screenshots is **`SECONDARY` / `UNVERIFIED`** until corroborated by tracker config IOC, sample sandbox report, or vendor PRIMARY-SOURCE.

| Forum (examples) | Defensive role | ETW relevance |
|------------------|----------------|---------------|
| XSS.is | Monitor/cite Russian-language malware/crypter marketplace leads | Cruciferra / PUROSANGUE ASSOCIATION_ONLY; general crypter chatter |
| Exploit.in | Monitor/cite higher-tier malware sales / affiliate / IAB chatter | Droppers and SynkLoader-relevant loader marketplace leads (SECONDARY until corroborated) |
| BreachForums | Monitor/cite breach dumps / access marketplace chatter | Context only; not family ownership |
| DarkForums | Monitor/cite successor / parallel forum chatter | Context only |
| RaidForums / archive clones | Historical research via archives / licensed CTI mirrors | Archival cite; do not recreate buyer accounts |
| HackForums | Monitor/cite commodity RAT / crypter sales threads | Commodity patterns |
| Cracked.io / Nulled.to | Monitor/cite cracked tooling ads | SECONDARY until corroborated |

**ETW agents do NOT:**

- create accounts to **buy** malware, crypters, or panels;
- provide setup, configuration, or operational help to sellers or buyers;
- scrape private sections behind login when that requires prohibited authentication to criminal services;
- treat a forum post as confirmed IOC ownership or operator identity.

**Permitted:** read publicly available pages or licensed CTI archives; preserve screenshots/HTML as evidence with provenance `SECONDARY` / `UNVERIFIED` until corroborated.

---

## 2) Chat channels (Telegram vs private E2EE)

### Public / semi-public Telegram (malware channels)

Named as **examples of research tooling** used by defenders — not as a shopping list for operational crimeware work:

| Tool (examples) | Defensive use |
|-----------------|---------------|
| **Telepathy** | Telegram OSINT / archival enumeration (research accounts only) |
| **TGMind** | Telegram intelligence / archive-oriented tooling (research accounts only) |
| **TGScraper** | Public/semi-public channel archival scrape patterns (research accounts only) |

**Scope:** public and semi-public malware announcement / leak channels. Prefer licensed CTI indexes when available.

### Advanced ops channels (Showboat-tier and similar)

Matrix, Jabber (XMPP), Tox, and OMEMO-protected rooms are commonly used for **closed** operator coordination. Treat visibility into **private E2EE** rooms as a **commercial-CTI dependency** (Flashpoint, KELA, Intel471, ZeroFox, Flare.io, equivalents) — not as an autonomous ETW collection path.

| Surface | Autonomous collectors | Human researchers (licensed / authorized) |
|---------|----------------------|-------------------------------------------|
| Public Telegram channels / public Matrix rooms | May monitor via public APIs / archival tools under OpSec | Same + research-only accounts |
| Private E2EE (invite-only Matrix/Jabber/Tox/OMEMO) | **MUST NOT join** | Only via licensed CTI products or explicit legal authority — never via stolen invites/tokens |

### Specialized archives & commercial CTI

| Surface | Defensive use | ETW notes |
|---------|---------------|-----------|
| vx-underground chat / forum **leak archives** | Historical research into commodity RAT sales, crypter ads, Discord CDN drop patterns | Archival read only. Do **not** download malware samples for execution. Prefer metadata and tracker-corroborated IOCs. |
| Flashpoint, KELA, Intel471, ZeroFox, Flare.io | Licensed underground / Telegram / dark-web monitoring | Use only with a license. Cite PRIMARY-SOURCE or SECONDARY per vendor terms; do not invent access. |
| Public Discord Trust & Safety / abuse channels | Reporting malicious servers distributing RATs | Prefer Message Links / Server ID / Channel ID / PCAP (see OpSec & takedowns). |

Agents may **cite** publicly mirrored research about these archives. Agents must **not** authenticate to live criminal Telegram/Discord/Matrix communities.

### Safety rules (non-negotiable)

1. **Research-only** accounts and environments — never the analyst’s primary or work Discord/Telegram/Matrix.
2. **Never** run unknown bots, “cracked” clients, or untrusted Telegram/Discord “helpers.”
3. **Never** harvest, store, or reuse Discord/Telegram/Matrix **tokens**, session strings, or MFA secrets.
4. **Never** authenticate to attacker **C2 panels**, seller shops, or cracked control UIs — even “just to look.”
5. Prefer **public tracker APIs** and licensed CTI over live underground interaction whenever possible.
6. Autonomous collectors **do not join private rooms** — full stop.

If a task requires violating any of the above, **stop** and record the gap under autonomous collection policy.

---

## 3) Prefer concrete C2 / config IOCs from sandboxes & trackers

Prefer these for IPs, domains, mutexes, hashes, Discord CDN URLs, and **extracted configs** over forum/Telegram screenshots:

| Service | Typical IOC types | ETW use |
|---------|-------------------|---------|
| [Triage (hatching.io)](https://tria.ge/) | Sandbox reports, config extraction | C2 from **sample configs** (stronger than chat screenshots) |
| [MalwareBazaar](https://bazaar.abuse.ch/) | Sample hashes, tags, download metadata | Tag search for ETW family names; do not execute downloads |
| [ThreatFox](https://threatfox.abuse.ch/) | IPs, domains, URLs, hashes by malware tag | Preferred IOC feed for family tag queries |
| [InQuest Labs](https://labs.inquest.net/) | File / URL / IOC search | Metadata and reputation pivots |
| [Any.Run](https://any.run/) | Public interactive sandbox reports | Cite public report configs / network IOCs; do not upload samples that require prohibited auth or live C2 interaction beyond public report views |
| [URLhaus](https://urlhaus.abuse.ch/) | Malicious URL distribution | Payload / Discord CDN URL leads |

**Family tag seeds (query; do not invent hits):** PollCat, SynkLoader, RatHat, Showboat, Rapuncel, NodeRabbit, Settra (+ Cruciferra / PUROSANGUE as ASSOCIATION_ONLY).

Seeds: [`../queries/tracker_collection_seeds.csv`](../queries/tracker_collection_seeds.csv).  
Optional autonomous queries: public abuse.ch APIs (ThreatFox / MalwareBazaar / URLhaus) under [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md). **Auth-Key required** for current abuse.ch APIs (HTTP 401 without key). Public browse HTML may present hCaptcha — captcha interstitials are **not** NEGATIVE SEARCH RESULT evidence.

When ETW retrieves a tracker API response itself → provenance **`OBSERVED_PASSIVE`** (query fact) with raw JSON under `evidence/passive-observations/`.  
When citing a tracker page already published in a vendor report without ETW retrieval → treat the **vendor** as PRIMARY-SOURCE and the tracker citation as supporting SECONDARY unless ETW re-queries.

---

## 4) OpSec & takedown evidence quality

### Researcher OpSec

| Rule | Requirement |
|------|-------------|
| No corp / personal IP | Do **not** browse underground forums, Tor dark-web mirrors, or malware Telegram channels from corporate or home residential IP |
| Isolated research environment | Human researchers use an **isolated VM** plus **VPN and/or Tor** as appropriate for the surface |
| Account separation | Research-only identities; never reuse work SSO, personal phone numbers, or primary messengers |
| Samples | Metadata / tracker reports only in autonomous flows; no sample execution on analyst workstations |

### Takedown / Trust & Safety submissions

When preparing defensive reports of malicious Discord / Telegram / Matrix distribution:

| Prefer | Avoid relying on alone |
|--------|------------------------|
| Message Links (permalinks) | Spoofable screenshots without IDs |
| Server ID / Channel ID | Cropped UI without permalinks |
| PCAP or other network artifacts (where lawfully obtained) | Unverified “someone said” paraphrases |

Screenshots remain useful **corroboration** but are easy to forge; IDs, message links, and network captures are what platform Trust & Safety and LE workflows typically need. Still classify unsourced chat chatter as **SECONDARY / UNVERIFIED** until linked to a tracker IOC or sample config.

---

## Mapping to Emerging Threat Watch families

| ETW family / association | Tracker / channel practice |
|--------------------------|----------------------------|
| Rapuncel, Settra, RatHat, NodeRabbit, PollCat, SynkLoader, Showboat | Search ThreatFox / MalwareBazaar / URLhaus / Triage / Any.Run / InQuest by **family name and known aliases** when those tags appear |
| SynkLoader | Exploit.in / IAB-dropper marketplace cites are leads only (SECONDARY) until config IOC or PRIMARY ties the loader |
| Showboat | Private E2EE / closed-channel leads are commercial-CTI or vendor PRIMARY; autonomous agents do not join rooms |
| Cruciferra / PUROSANGUE | ASSOCIATION_ONLY marketplace / crypter leads; XSS/Exploit-style forum cites OK as leads; do not merge into Rapuncel operator identity |
| Matanbuchus / AstarionRAT / StarlandRAT / Lumma / Vidar / Pikabot / QakBot (CANDIDATE) | Tracker tag seeds in `tracker_collection_seeds.csv`; **candidates only** — no investigation trees until promoted. BelialDemon XSS/Exploit ads are SECONDARY marketplace leads |
| Remcos / AsyncRAT / njRAT (illustrations only) | Use to understand **commodity panel screenshot** patterns — not active ETW cases |

**Technique comparators (COMMON TECHNIQUE; authorship NOT_ESTABLISHED):** [`../../docs/TECHNIQUE_COMPARATORS.md`](../../docs/TECHNIQUE_COMPARATORS.md) · [`../../intelligence/technique-comparators.csv`](../../intelligence/technique-comparators.csv). SynkLoader ↔ Matanbuchus (Teams + ChaCha20) and Rapuncel ↔ Lumma/Vidar (stealer MaaS market) are **not** lineage claims.

Do not invent tags or IOCs. Empty tracker results are valid **NEGATIVE SEARCH RESULT** dispositions.

---

## Provenance rules (underground → ETW)

| Artifact | Default provenance |
|----------|--------------------|
| Forum / Telegram / Discord **screenshot** of a panel or sale | `SECONDARY` / `UNVERIFIED` until corroborated |
| ThreatFox / URLhaus / MalwareBazaar / Triage / Any.Run public report IOC **retrieved by ETW** | `OBSERVED_PASSIVE` (query/response fact); promote relationship to family only with tag match + case isolation |
| Tracker IOC **as published inside a vendor report** ETW archived | Vendor artifact = `PRIMARY-SOURCE`; do not auto-label infrastructure `OBSERVED_PASSIVE` without ETW re-query |
| Licensed CTI excerpt (Flashpoint / KELA / Intel471 / ZeroFox / Flare.io) | `PRIMARY-SOURCE` or `SECONDARY` per vendor terms; never fabricate license access |
| C2 IP visible only in a Telegram panel screenshot | `SECONDARY` until extracted from sample configs via Triage / ThreatFox / Any.Run / vendor PRIMARY |
| Private E2EE room content without licensed CTI | **Do not collect autonomously** — gap only |
| “Author home IP” / personal residential attribution from panel screenshots | **NOT ESTABLISHED** — never emit |

Cross-link: [`../../investigations/_shared/docs/operator-ip-research-note.md`](../../investigations/_shared/docs/operator-ip-research-note.md) and [`../../intelligence/operator-ip-research-note.md`](../../intelligence/operator-ip-research-note.md).

---

## Policy cross-walk

See **Underground / dark-web OSINT** in [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md):

| Permitted | Prohibited |
|-----------|------------|
| Public tracker queries (ThreatFox, MalwareBazaar, URLhaus, Triage metadata, InQuest, Any.Run public reports) | Purchase malware / crypters / panels |
| Licensed commercial CTI underground feeds | Join underground communities to **operate** crimeware |
| Archival leak / public mirror **research** (read metadata; no malware execution) | Scrape / steal Discord, Telegram, or Matrix tokens |
| Public forum **read/archive** when content is publicly reachable | Interact with seller panels / authenticate to C2 |
| Cite forum ads as ASSOCIATION_ONLY / UNVERIFIED leads | Provide setup help or operational instructions |
| Public/semi-public Telegram channel monitoring via research tooling | Autonomous join of **private** E2EE rooms (Matrix/Jabber/Tox/OMEMO) |

---

## Related documents

- [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md)  
- [`UNCONVENTIONAL_STAGING_OSINT.md`](UNCONVENTIONAL_STAGING_OSINT.md) — developer platforms / open buckets / APK mirrors / bounded Shodan (complementary; not underground)  
- [`APT_AND_DARKWEB_OSINT.md`](APT_AND_DARKWEB_OSINT.md)  
- [`TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`](TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md) — Discord/Telegram takedown fields; abuse.ch submission  
- [`../queries/tracker_collection_seeds.csv`](../queries/tracker_collection_seeds.csv)  
- [`../queries/unconventional_staging_seeds.csv`](../queries/unconventional_staging_seeds.csv)  
- [`../queries/collection_instructions.md`](../queries/collection_instructions.md)  
- [`../../docs/CANDIDATE_FAMILIES.md`](../../docs/CANDIDATE_FAMILIES.md)  
- [`../../docs/TECHNIQUE_COMPARATORS.md`](../../docs/TECHNIQUE_COMPARATORS.md)  
- [`EVIDENCE_ID_POLICY.md`](EVIDENCE_ID_POLICY.md)
