# Abyssos — Caveats and Limits

**Package:** `ETW-ABY-IC3`

## Analytical caveats

- Domain/hash/IP rows are PRIMARY-SOURCE (Zscaler ThreatLabz) — not ETW live C2 contact.
- Initial delivery vector remains under investigation per Zscaler — do not invent lures.
- Author identity remains **NOT_ESTABLISHED**.
- Standalone family — do not merge with other ETW IC3 filings.
- Mutex UUID example is sample-specific; format `Global\[UUID4]` is the durable marker.
- Module XOR/AES constant `1234567890abcdef` is a published crypto constant, not a wallet or account credential.

## This package does **not** claim

- No dollar loss figure.
- No assertion that ETW discovered Abyssos.
- No fabricated hashes or C2 hosts.
- No confirmed initial-access method.
- No independent actor attribution.

## Potential impact (general; not a loss claim)

Credential/cookie theft, browser-session hijacking, file exfiltration, and remote control (HVNC/shell) on Windows hosts, per Zscaler framing.

## Provenance vocabulary

| Label | Meaning in this package |
|-------|-------------------------|
| PRIMARY-SOURCE | Published by the cited vendor/researcher |
| OBSERVED_PASSIVE | Passive fact retrieved by ETW — not ownership |
| OBSERVED | Independently observed campaign ownership (not claimed) |
| UNVERIFIED | Lead only — not adequately substantiated |

## Safety statement

No malware was executed and no suspected command-and-control system was contacted during preparation of this package.
