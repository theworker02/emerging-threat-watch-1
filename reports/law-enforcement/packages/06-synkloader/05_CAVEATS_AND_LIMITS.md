# SynkLoader — Caveats and Limits

**Package:** `ETW-SYN-IC3`

## Analytical caveats

- Domain/hash/URL rows are PRIMARY-SOURCE (Expel); IPv4 rows SYN-IND-0026–0029 are OBSERVED_PASSIVE DNS A mappings — not live C2 contact.
- CDN demotion N/A for these non-CDN C2 A records; author identity remains NOT_ESTABLISHED.
- Shared ASN AS399629 across multiple apexes is INFRASTRUCTURE_OVERLAP candidate only — not operator identity.
- Azure Blob MSI host edge IP is ASSOCIATION_ONLY (not actor-owned).
- Secondary ransomware-follow-on / IAB framing is Expel low–medium confidence or secondary press — not established by ETW.
- Resolving a published domain != proof C2 is currently active.

## This package does **not** claim

- No dollar loss figure.
- No assertion that ETW discovered SynkLoader.
- No fabricated hashes or C2 hosts.
- No confirmed ransomware follow-on by ETW.
- No author identity claim (NOT_ESTABLISHED).

## Potential impact (general; not a loss claim)

Credential theft and potential tunnel-enabled access to internal/external systems via the infected host, per Expel framing.

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
