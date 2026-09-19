# NodeRabbit — Caveats and Limits

**Package:** `ETW-NRB-IC3`

## Analytical caveats

- Mirage Kitten attribution is Kaspersky's assessment — not independently established by ETW.
- Git hooks are local persistence unless further evidence shows repository/supply-chain propagation.
- Preserve published MD5 archive hashes; SHA-256 enrichment still pending authorized metadata (OPEN).
- agent:servers can replace C2 lists — domain IOCs are perishable; prefer host artifacts.
- Azure/Cloudflare edge IPs are not actor-owned infrastructure.
- RankChallenge-react MD5 (795e053a…) is PollCat — NRB-IND-0011 is CROSS_REF_POLLCAT only; do not treat as NodeRabbit IOC.
- `colorized_terminal@2.1.0` / `pretty-log@2.1.0` (NRB-IND-0042–0043) and implant path `node_modules/.cache/.320697f1/index.js` (NRB-IND-0044) are **NodeRabbit** local-bundle launchers per Kaspersky — **not** PollCat. Registry GET 404 / absent 2.1.0 are OBSERVED_PASSIVE negatives (NRB-CLAIM-0021–0022 / NRB-PO-0200–0201).
- Do **not** treat public registry `pretty-log@0.1.0` as a NodeRabbit IOC — name collision only; malicious pin is local `@2.1.0`.
- Pattern-based NameCheap domains (NRB-IND-0029–0039) and PolySwarm SHA-256s (NRB-IND-0040–0041) are ASSOCIATION_ONLY / RELATED_SAMPLE — not sample-bound NodeRabbit implant proof.
- COMMON TECHNIQUE overlap with PollCat (recruiter ZIP / Azure-CF C2) is Moderate; implant divergence is High — see shared/lineage/pollcat-noderabbit-lineage-note.md. Do not merge authorship.

## This package does **not** claim

- No independent Mirage Kitten attribution by ETW.
- No confirmed supply-chain propagation via Git hooks.
- No dollar loss figure.
- No claim that current Azure edge IPs are exclusive actor property.
- No claim that NodeRabbit and PollCat share implant authors/operators (Moderate delivery overlap only).
- No claim that public npm `pretty-log@0.1.0` is a NodeRabbit artifact (malicious pin is local `@2.1.0` only).
- No confirmed MD5→SHA-256 map for Kaspersky archive MD5s (including PolySwarm RELATED_SAMPLE rows).

## Potential impact (general; not a loss claim)

Unauthorized access to developer workstations and potentially corporate environments via proxy-aware C2; espionage risk per Kaspersky campaign framing.

## Provenance vocabulary (for reviewers)

| Label | Meaning in this package |
|-------|-------------------------|
| PRIMARY-SOURCE | Published by the cited vendor/researcher |
| OBSERVED_PASSIVE | Passive fact retrieved by ETW (CT/DNS/urlscan/RDAP) — not ownership |
| OBSERVED | Independently observed campaign ownership (not claimed in baseline) |
| INFERRED | Analytical conclusion — labeled as such |
| UNVERIFIED | Exists as lead but not adequately substantiated |

## Safety statement

No malware was executed and no suspected command-and-control system was contacted during preparation of this package.
