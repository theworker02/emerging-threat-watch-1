# Settra — Caveats and Limits

**Package:** `ETW-SET-IC3`

## Analytical caveats

- Encryptor (malware) and operator intrusion tooling are separate — do not say "Settra uses Mimikatz."
- WIN-LIVFRVQFMKO is an investigative lead (Huntress + Kaspersky SSL CN) — UNKNOWN / not Settra-exclusive; do not backdate Settra to 2024.
- 193.5.65.114 MeshCentral chronology and Rapid Seedbox RDAP are INFRASTRUCTURE_OVERLAP leads — not Settra-exclusive ownership.
- Public pages analyzed for this corpus did not yield a usable Settra sample SHA-256 list.
- OBSERVED_PASSIVE MeshCentral/RDAP facts are not campaign-ownership claims.

## This package does **not** claim

- No victim organization names invented.
- No dollar loss figure.
- No claim that pre-2026 hostname sightings prove Settra existed then.
- No claim that Kaspersky FortiClient EMS activity is Settra.
- No claim that encryptor itself performs exfiltration.
- No claim that Rapid Seedbox RDAP contacts identify malware authors.

## Potential impact (general; not a loss claim)

Enterprise encryption/extortion; recovery destruction; possible data theft by operators using tooling separate from the encryptor binary.

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
