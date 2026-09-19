# Evidence ID Policy

**Updated:** 2026-09-19

## Two parallel ID namespaces (do not silently overwrite)

| Namespace | Location | Purpose |
|-----------|----------|---------|
| `RAP-EV-*` / `SET-EV-*` / `RAT-EV-*` / `NRB-EV-*` / `POL-EV-*` / `SYN-EV-*` / `SHO-EV-*` | `evidence/evidence-ledger.csv` | Chronological **publication / observation / claim** evidence rows (Phase 1+) |
| `RAP-IND-*` / `SET-IND-*` / `RAT-IND-*` / `NRB-IND-*` / `POL-IND-*` / `SYN-IND-*` / `SHO-IND-*` | `evidence/published-indicators.csv` | **Published indicators** from primary sources (executive research pass 2026-09-19+) |

The executive seed corpus used `RAP-EV-0001` for `vsdbg.dll` SHA-256. That numbering **collides** with Phase 1 publication evidence already assigned `RAP-EV-0001`. Per methodology, historical rows are not rewritten.

**Crosswalk:** Seed `RAP-EV-0001` (vsdbg.dll) ≡ ETW `RAP-IND-0001`. Seed `NOD-EV-*` ≡ ETW `NRB-IND-*`.

## Provenance rule (mandatory)

**None of the campaign infrastructure in the baseline is labeled `OBSERVED` / `OBSERVED_PASSIVE` until passive collection writes a manifest row.**

Retrieving a primary research article is **not** independent observation of attacker infrastructure. Status remains `PRIMARY-SOURCE` until ETW performs passive validation and records an `OBSERVED_PASSIVE` row with method, timestamp, raw response, and SHA-256.

### Relationship ladder (do not auto-attribute)

| Observation | Label |
|-------------|-------|
| CT/pDNS/RDAP fact collected by ETW | `OBSERVED_PASSIVE` |
| Vendor published indicator | `PRIMARY-SOURCE` |
| Passive evidence supports vendor relationship | `CORROBORATED` |
| Same CDN/hosting provider | `ASSOCIATION_ONLY` |
| Same IP as known campaign domain | `INFRASTRUCTURE_OVERLAP` |
| “Operated by [actor]” | **NOT ESTABLISHED** without more evidence |

Full autonomy rules: [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md).

### Evidence ID additions

| Namespace | Location | Purpose |
|-----------|----------|---------|
| `PS-*` | `evidence/manifests/primary-source-manifest.csv` | Preserved primary HTML/PDF artifacts |
| `*-PO-*` | `evidence/manifests/passive-observation-manifest.csv` | Passive OBSERVED_PASSIVE rows (CT/pDNS/…) |

### Family ID prefixes (case codes)

| Family | Case | Claims | Indicators | Passive | IC3 package |
|--------|------|--------|------------|--------|-------------|
| Rapuncel | RAP | `RAP-CLAIM-####` | `RAP-IND-####` | `RAP-PO-####` | `ETW-RAP-IC3` |
| Settra | SET | `SET-CLAIM-####` | `SET-IND-####` | `SET-PO-####` | `ETW-SET-IC3` |
| RatHat | RAT | `RAT-CLAIM-####` | `RAT-IND-####` | `RAT-PO-####` | `ETW-RAT-IC3` |
| NodeRabbit | NRB | `NRB-CLAIM-####` | `NRB-IND-####` | `NRB-PO-####` | `ETW-NRB-IC3` |
| PollCat | POL | `POL-CLAIM-####` | `POL-IND-####` | `POL-PO-####` | `ETW-POL-IC3` |
| SynkLoader | SYN | `SYN-CLAIM-####` | `SYN-IND-####` | `SYN-PO-####` | `ETW-SYN-IC3` |
| Showboat | SHO | `SHO-CLAIM-####` | `SHO-IND-####` | `SHO-PO-####` | `ETW-SHO-IC3` |

`PS-POL-001` dual-lists the same Securelist HTML bytes as `PS-NRB-001` — dual-list in manifests/source indexes; **do not merge** cases.
