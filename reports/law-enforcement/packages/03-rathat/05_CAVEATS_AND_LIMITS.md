# RatHat — Caveats and Limits

**Package:** `ETW-RAT-IC3`

## Analytical caveats

- Blog body is architectural/URI-path heavy; C2 hosts and APK hashes come from Zimperium's published IOC tree — do not invent additional hosts, hashes, or package names.
- Android applicationId / signing certificates are still open gaps — do not fabricate package names.
- Prefer architectural/URI-path indicators and remediation facts over "AI malware" marketing framing.
- Uninstalling the visible APK may not remove compromise.
- Passive CT/urlscan on published apexes is not ownership or live C2 proof; ETW has not contacted C2.

## This package does **not** claim

- No invented Android package names or signing certificates.
- No dollar loss figure.
- No active probing of RatHat C2 by ETW.
- No authorship attribution beyond Zimperium's published assessment.
- No claim that passive CT/urlscan proves current C2 activity or ownership.

## Potential impact (general; not a loss claim)

Credential and banking-account compromise; remote shell/tunnel access; persistence that can survive naive APK removal.

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
