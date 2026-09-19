# PollCat — FBI / Field-Office Summary

**Package:** `ETW-POL-IC3` · **Status:** DRAFT · **Cutoff:** 2026-09-19

## One-paragraph summary

I am reporting defensive threat-intelligence information concerning the PollCat malware documented by Kaspersky GReAT on September 1, 2026 in the same Securelist article that covers NodeRabbit. Kaspersky describes PollCat as a cross-platform obfuscated JavaScript RAT delivered through the RankChallenge-react coding-challenge archive (MD5 795e053a990a1569ffdcb57f48f6d085). Kaspersky reports registration C2 hosts including sahi-finance.com and Azure Web App hostnames, OTP validation via lifespotify.com, and persistence markers such as NetSync scheduled tasks, requireObject.js under AppData, com.harsh.requireobject.plist, and ~/.node_packages. Kaspersky states PollCat's structure is substantially different from NodeRabbit. I am retaining PollCat as a separate case. Co-disclosure and shared recruiter/coding-challenge delivery are COMMON TECHNIQUE only — not proof of shared implant authorship. I have not executed malware samples and have not contacted suspected command-and-control systems.

## Why this may matter to FBI cyber / IC3 correlation

Co-disclosed with NodeRabbit in Kaspersky Securelist; packages remain separate. RankChallenge-react lure; distinct C2/persistence from NodeRabbit; stronger documented protocol overlap with MiniFast/Retrograde than with NodeRabbit.

## Highest-value indicators (primary-source; not ETW-observed)

- RankChallenge-react MD5 POL-IND-0001: 795e053a990a1569ffdcb57f48f6d085 (not NodeRabbit)
- C2 domains: sahi-finance.com; gamebarappinformation.azurewebsites.net; gamebarapp.azurewebsites.net; lifespotify.com
- OTP URL path under lifespotify.com (do not probe live)
- Persistence: NetSync_* task; requireObject.js; com.harsh.requireobject.plist; ~/.node_packages
- Protocol markers: POST /beacon; GET /gate/fetch; POST /gate/hello; POST /api/system-details/result
- See 03_INDICATORS.csv (POL-IND-0001–0015)

Full table: `03_INDICATORS.csv`

## Critical analytical caveats

- Do not equate PollCat operators/authors with NodeRabbit — Moderate delivery overlap / High implant divergence (shared/lineage/pollcat-noderabbit-lineage-note.md).
- RankChallenge MD5 is PollCat (POL-IND-0001); any NodeRabbit cross-ref is CROSS_REF_POLLCAT only.
- PollCat C2 handshake (HTTP 400 + socketId /gate/*) aligns more with MiniFast/Retrograde than NodeRabbit AES-GCM — do not cite as PollCat≡NodeRabbit code reuse.
- Azure Web App / Cloudflare-backed hosts are shared-edge ASSOCIATION_ONLY for ownership.
- Mirage Kitten attribution remains Kaspersky's assessment — not an ETW conclusion.
- ETW has not independently OBSERVED live campaign infrastructure.

## Suggested handling

1. Treat as **defensive threat-intelligence referral**, not a completed criminal case file.
2. Correlate MeshAgent / domain / hash / URI-path indicators against existing FBI/IC3 holdings.
3. Request sample acquisition through normal vendor/legal channels if needed — this package does not contain malware binaries.
4. Keep this family **separate** from other Emerging Threat Watch packages unless linkage evidence appears.

## Contact block (reporter fills before filing)

| Field | Value |
|-------|-------|
| Reporter name | _[TO BE FILLED]_ |
| Organization (if any) | _[TO BE FILLED]_ |
| Email / phone | _[TO BE FILLED]_ |
| Preferred contact method | _[TO BE FILLED]_ |
| Related IC3 complaint number(s) | _[IF ANY]_ |
| Related FBI tip / case number(s) | _[IF ANY]_ |
