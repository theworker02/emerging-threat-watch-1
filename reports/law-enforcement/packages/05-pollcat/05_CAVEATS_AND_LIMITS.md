# PollCat — Caveats and Limits

**Package:** `ETW-POL-IC3`

## Analytical caveats

- Do not equate PollCat operators/authors with NodeRabbit — Moderate delivery overlap / High implant divergence (shared/lineage/pollcat-noderabbit-lineage-note.md).
- RankChallenge MD5 is PollCat (POL-IND-0001); any NodeRabbit cross-ref is CROSS_REF_POLLCAT only.
- PollCat C2 handshake (HTTP 400 + socketId /gate/*) aligns more with MiniFast/Retrograde than NodeRabbit AES-GCM — do not cite as PollCat≡NodeRabbit code reuse.
- Azure Web App / Cloudflare-backed hosts are shared-edge ASSOCIATION_ONLY for ownership.
- Mirage Kitten attribution remains Kaspersky's assessment — not an ETW conclusion.
- ETW has not independently OBSERVED live campaign infrastructure.

## This package does **not** claim

- No claim that PollCat and NodeRabbit share implant authors/operators.
- No dollar loss figure.
- No assertion that ETW discovered PollCat.
- No fabricated hashes or C2 hosts.
- No independent Mirage Kitten attribution by ETW.

## Potential impact (general; not a loss claim)

Unauthorized access to developer workstations via coding-challenge social engineering, per Kaspersky framing.

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
