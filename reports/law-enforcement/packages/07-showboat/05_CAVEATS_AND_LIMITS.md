# Showboat — Caveats and Limits

**Package:** `ETW-SHO-IC3`

## Analytical caveats

- Historical activity (Pastebin Jan 2022; BLL IPs from 2023-04) vs May 2026 disclosure dating is an intelligence gap — do not collapse into first-seen 2026.
- IPv4/domain/hash rows are PRIMARY-SOURCE from Lumen article and BLL Showboat_IOCs.txt — not ETW live contact.
- 116.169.244.208 is ASSOCIATION_ONLY (possible upstream/dev) — not confirmed actor-owned C2.
- CDN demotion N/A for these BLL/Lumen-listed hosts; author identity remains NOT_ESTABLISHED (vendor cites PRC-aligned clusters — ETW does not independently establish).
- Hide-command strings SHO-IND-0023–0026 (`ukpkmkk.c` / `ukpkmkk.so` / `kworkers|dbus|autoupdate` / `/etc/ld.so.preload`) are **SECONDARY** (Picus; SHO-CLAIM-0009/0010) — corroborate Lumen Pastebin dead-drop class; prefer ETW paste retrieval before elevating to OBSERVED_PASSIVE.
- Do not invent additional telecom victim names or backdate beyond published ranges.

## This package does **not** claim

- No dollar loss figure.
- No assertion that ETW discovered Showboat.
- No fabricated hashes or C2 hosts.
- No independent actor attribution beyond vendor language.
- No claim that Pastebin Jan 2022 alone proves continuous Showboat operations through 2026.

## Potential impact (general; not a loss claim)

Persistent unauthorized access in Linux telecom/ISP environments, per Lumen framing.

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
