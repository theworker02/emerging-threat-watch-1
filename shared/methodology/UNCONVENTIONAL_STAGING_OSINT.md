# Unconventional Staging & Developer-Platform OSINT

**Status:** Defensive collection methodology (Emerging Threat Watch)  
**Effective:** 2026-09-19  
**Binding policy:** [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md)  
**Companion:** [`UNDERGROUND_AND_COMMODITY_RAT_OSINT.md`](UNDERGROUND_AND_COMMODITY_RAT_OSINT.md) (alias [`APT_AND_DARKWEB_OSINT.md`](APT_AND_DARKWEB_OSINT.md))

---

## Framing (mandatory)

This layer covers **public developer platforms, cloud object staging, mobile APK mirrors, and bounded internet-wide search** used by ETW families for delivery or staging — not underground marketplace participation.

It is **not** guidance for:

- authenticating to attacker C2 panels or seller shops;
- submitting credentials to suspected login pages;
- downloading or executing malware on analysis hosts without an isolated-lab note;
- mass-scanning arbitrary IP ranges;
- inventing IOCs or merging cases without linkage evidence.

**OpSec:** No corporate/personal IP for dark/underground surfaces (see underground methodology). Public GitHub / npm / Pastebin / bucket **metadata** OSINT is lower risk than underground browsing, but **still isolate** when downloading samples. Prefer metadata-only autonomous collection.

Seeds: [`../queries/unconventional_staging_seeds.csv`](../queries/unconventional_staging_seeds.csv).

---

## Summary matrix (hunt surfaces → families)

| Family | Primary unconventional staging surfaces | Notes (case isolation) |
|--------|------------------------------------------|------------------------|
| **PollCat** | GitHub/Gist/GitLab coding-challenge stubs; open cloud ZIPs (S3/Azure); public `node_modules` / challenge archives | Delivery class overlaps NodeRabbit recruiter lures — **do not auto-merge** IOCs |
| **NodeRabbit** | Locally bundled trojanized npm (`colorized_terminal`, `pretty-log` @ 2.1.0); Gists; coding-test repos | PRIMARY: packages often **not** on public npm registry — search registry + public archives |
| **Showboat** | Pastebin / paste sites (C source e.g. `ukpkmkk.c`); Linux forums as dead-drops | Monitor for `ld.so.preload` / process-filter strings |
| **RatHat** | APKPure / APKCombo / Aptoide **listings & metadata**; VT / Hybrid-Analysis Behavior / Screenshots / Dropped Files | Prefer UI evidence (fake banking, lock screens) from public sandbox tabs |
| **SynkLoader** | Azure Blob / open cloud MSI+PS1; Censys/Shodan **snapshots** of already-flagged C2 IPs | Open-bucket filename pivots via GrayhatWarfare-style queries |

Do **not** invent hits. Empty / 404 / zero-result searches are valid **NEGATIVE SEARCH RESULT** dispositions.

---

## 1) Developer code platforms

### GitHub / Gist / GitLab

| Pattern | Defensive use | ETW relevance |
|---------|---------------|---------------|
| Stub / staging / “coding test” repos | Metadata + public file tree search | PollCat `RankChallenge-react`-class lures; NodeRabbit TaskFlow-class challenges |
| Fake recruitment / job-lure repositories | Issue trackers and PRs posing as recruitment firms | Association leads only until lure archive hash or PRIMARY ties family |
| Public Gists with challenge ZIPs or `package.json` pins | Archive + hash when lawful | Do not execute `npm i` / `node` on analyst hosts |

**Permitted:** logged-out / public API code search; archive HTML/JSON under `evidence/passive-observations/github/`.  
**Prohibited:** cloning private repos via stolen tokens; interacting with attacker-controlled CI to “test” the lure.

### Pastebin & paste sites

| Pattern | Defensive use | ETW relevance |
|---------|---------------|---------------|
| Filenames / titles: `ukpkmkk.c`, `ukpkmkk.so` | Paste metadata + raw URL discovery (no compile/execute) | Showboat “hide” dead-drop (SECONDARY detail often from Picus; Lumen PRIMARY for Pastebin class) |
| Strings: `ld.so.preload`, `process_to_filter`, `kworkers\|dbus\|autoupdate` | Content search on paste indexes | Showboat process-hiding library |

Preserve paste **metadata** (post date, URL, title). Compiling or loading retrieved C on a host requires isolated-lab documentation and is **out of scope** for autonomous collectors.

### npm / PyPI registries

| Pattern | Defensive use | ETW relevance |
|---------|---------------|---------------|
| Exact package names from PRIMARY | Registry metadata GET; 404 is a useful negative | NodeRabbit: `colorized_terminal@2.1.0`, `pretty-log@2.1.0` (Kaspersky: bundled in `node_modules`, often **not** published) |
| Typosquat / lookalike packages | Registry search only | Leads — do not install |
| Public `node_modules` trees in GitHub / archives | Code search for package folder + `.cache/.320697f1` | NodeRabbit implant path per Securelist |

**Case note:** User hunt matrices sometimes list PollCat next to `colorized_terminal`. PRIMARY sources attribute **`colorized_terminal` / `pretty-log` to NodeRabbit**; PollCat uses a separate React lure (`RankChallenge-react` / `requireObjects.js`). Keep namespaces separate.

### Issue trackers / PRs

Monitor public issues/PRs that impersonate recruitment firms or attach “assessment” archives. Cite as `SECONDARY` / `UNVERIFIED` until hash or vendor PRIMARY links the artifact to a family.

---

## 2) Cloud staging (open buckets)

| Surface | Defensive use | ETW relevance |
|---------|---------------|---------------|
| Open S3 / Azure Blob | **Metadata** listing / HEAD / public object URL discovery | PollCat challenge ZIPs; SynkLoader MSI/PS1 (e.g. `filereserve.blob.core.windows.net` Expel PRIMARY) |
| [GrayhatWarfare](https://buckets.grayhatwarfare.com/) (or equivalent) | Query by filename patterns (`*.msi`, `RankChallenge*.zip`, `PowershellCleaner`, SynkLoader path fragments) | Lead generation only |
| urlscan / VT URL metadata | Corroborate object URLs without downloading payloads | SynkLoader Azure delivery already has OBSERVED_PASSIVE urlscan rows |

### Provenance rule (cloud objects)

| Action | Provenance |
|--------|------------|
| ETW retrieves **metadata** (listing JSON, HEAD, urlscan page record, public object URL string) | `OBSERVED_PASSIVE` |
| Vendor publishes the object URL | `PRIMARY-SOURCE` artifact; promote URL to OBSERVED_PASSIVE only after ETW metadata retrieval |
| Download binary into analysis host | **Requires isolated-lab note**; autonomous collectors **must not** download/execute payloads by default |

Discovered object URL ≠ permission to run the payload.

---

## 3) Mobile / APK mirrors

| Surface | Defensive use | ETW relevance |
|---------|---------------|---------------|
| APKPure, APKCombo, Aptoide | Listing title, package name, version, publisher metadata | RatHat-like banking / remote-access apps |
| VirusTotal / Hybrid-Analysis | Public **Behavior / Screenshots / Dropped Files** tabs | UI evidence (fake banking, lock screens) without executing APK locally |

Do not sideload APKs onto personal devices. Prefer sandbox screenshots already published in public reports.

---

## 4) Infrastructure footprinting (BOUNDED)

Seeds: non-CDN rows in [`../../intelligence/infrastructure-ip-ledger.csv`](../../intelligence/infrastructure-ip-ledger.csv) that are already flagged (C2 / exfil / meshagent / PRIMARY unknown hosting). **Do not** fan out from Cloudflare/Azure CDN edges.

| Technique | Bound | Prohibited |
|-----------|-------|------------|
| Shodan / Censys / FOFA | Query **already flagged** ledger IPs only; ports **80 / 443 / 8080 / 8443** | Mass scan of random ranges; treating CDN edges as actor-owned seeds |
| JARM / SSL fingerprint pivots | From **known-bad certs** already in evidence or PRIMARY | Blind internet-wide JARM hunting without a seed cert |
| webscreenshot / gowitness-style captures | Unauthenticated HTTP(S) GET of **public** login/banner pages | Submitting credentials; authenticating to attacker panels; interacting beyond GET |
| Recursive fan-out | Depth **≤ 1** from ledger seed | Depth >1 without a research-plan exception |

Unauthenticated snapshot of a public page ≠ panel login. “Just looking” after auth is still prohibited under autonomous collection policy.

---

## Provenance quick-reference

| Artifact | Default |
|----------|---------|
| npm/PyPI registry GET (including 404) retrieved by ETW | `OBSERVED_PASSIVE` (query fact) |
| GitHub/Gist public code-search result | `OBSERVED_PASSIVE` |
| Open-bucket / paste **metadata** retrieved by ETW | `OBSERVED_PASSIVE` |
| Vendor article describing staging | `PRIMARY-SOURCE` |
| Picus / secondary write-ups of Showboat strings | `SECONDARY` until Lumen PRIMARY or ETW paste retrieval |
| Shodan/Censys banner for ledger IP | `OBSERVED_PASSIVE` |
| Screenshot of attacker panel after login | **Do not collect** |

---

## Policy cross-walk

See **Unconventional staging OSINT** in [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md):

| Permitted (autonomous) | Prohibited |
|------------------------|------------|
| Bounded Shodan/Censys/FOFA on ledger IPs | Panel login / credential submission |
| Paste / npm / PyPI / GitHub **metadata** queries | Malware execution on analysis host |
| Public bucket **metadata** / GrayhatWarfare filename queries | Mass unsolicited internet scanning |
| Unauthenticated HTTP GET screenshots of public pages | Download+execute samples without isolated-lab note |
| APK mirror listing metadata; public sandbox UI tabs | Auth to C2; JARM pivots from non-seed certs |

---

## Related documents

- [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md)  
- [`UNDERGROUND_AND_COMMODITY_RAT_OSINT.md`](UNDERGROUND_AND_COMMODITY_RAT_OSINT.md)  
- [`APT_AND_DARKWEB_OSINT.md`](APT_AND_DARKWEB_OSINT.md)  
- [`TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`](TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md) — hosting abuse needs JARM/banners only on ledger IPs; PCAP is human-lab path  
- [`CASE_ISOLATION.md`](CASE_ISOLATION.md)  
- [`../queries/unconventional_staging_seeds.csv`](../queries/unconventional_staging_seeds.csv)  
- [`../queries/collection_instructions.md`](../queries/collection_instructions.md)  
- [`../../intelligence/infrastructure-ip-ledger.csv`](../../intelligence/infrastructure-ip-ledger.csv)
