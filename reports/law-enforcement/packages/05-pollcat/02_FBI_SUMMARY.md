# PollCat — Summary

**Package:** `ETW-POL-IC3` · **Status:** FILED_IC3 · **Cutoff:** 2026-09-19

## Overview

Defensive threat-intelligence package concerning the PollCat malware documented by Kaspersky GReAT (2026-09-01) in the same Securelist article that covers NodeRabbit. Kaspersky describes PollCat as a cross-platform obfuscated JavaScript RAT delivered through the RankChallenge-react coding-challenge archive (MD5 `795e053a990a1569ffdcb57f48f6d085`). Kaspersky reports registration C2 hosts including `sahi-finance.com` and Azure Web App hostnames, OTP validation via `lifespotify.com`, and persistence markers such as NetSync scheduled tasks, `requireObject.js` under AppData, `com.harsh.requireobject.plist`, and `~/.node_packages`. Kaspersky states PollCat's structure is substantially different from NodeRabbit. **This package is PollCat-only.** Co-disclosure and shared recruiter/coding-challenge delivery are COMMON TECHNIQUE only — not proof of shared implant authorship. **Mirage Kitten attribution is Kaspersky's assessment, not independently established by ETW.**

## IC3 filing

| Field | Value |
|-------|-------|
| Submission ID | `98a4444754324e539dbbffcb10c70637` |
| Date filed | 2026-09-19 9:52:51 PM EST |
| Date filed (UTC) | 2026-09-20T01:52:51Z |
| Record | [`IC3_FILING_RECORD.md`](IC3_FILING_RECORD.md) |
| Separate related filings | Rapuncel `208b747c6f7445f0af2b69a9d63acc36`; Settra `631d8b4800d04bc19cdbfc6662e5c52c`; RatHat `f92c4c2f0dd3481f898fdd125e728adf`; NodeRabbit `dded86972e9347e0be27a6597b4cf08a` (no shared-operator claim) |
| Not merged | NodeRabbit (`ETW-NRB-IC3`) |

## Why this may matter for FBI cyber / IC3 correlation

Co-disclosed with NodeRabbit in Kaspersky Securelist; packages remain separate. RankChallenge-react lure; distinct C2/persistence from NodeRabbit; stronger documented protocol overlap with MiniFast/Retrograde than with NodeRabbit.

## Highest-value indicators

- RankChallenge-react MD5 `POL-IND-0001`: `795e053a990a1569ffdcb57f48f6d085` (not NodeRabbit)
- C2 domains: `sahi-finance.com`; `gamebarappinformation.azurewebsites.net`; `gamebarapp.azurewebsites.net`; `lifespotify.com`
- OTP URL path under `lifespotify.com` (do not probe live)
- Persistence: `NetSync_*` task; `requireObject.js`; `com.harsh.requireobject.plist`; `~/.node_packages`
- Protocol markers: `POST /beacon`; `GET /gate/fetch`; `POST /gate/hello`; `POST /api/system-details/result`

Full table: `03_INDICATORS.csv` (15 rows, `POL-IND-0001`–`0015`).

## Critical analytical caveats

- Do not equate PollCat operators/authors with NodeRabbit — Moderate delivery overlap / High implant divergence (`shared/lineage/pollcat-noderabbit-lineage-note.md`).
- RankChallenge MD5 is PollCat (`POL-IND-0001`); any NodeRabbit cross-ref is `CROSS_REF_POLLCAT` only.
- PollCat C2 handshake (HTTP 400 + `socketId` `/gate/*`) aligns more with MiniFast/Retrograde than NodeRabbit AES-GCM — do not cite as PollCat≡NodeRabbit code reuse.
- Azure Web App / Cloudflare-backed hosts are shared-edge `ASSOCIATION_ONLY` for ownership.
- Mirage Kitten attribution remains Kaspersky's assessment — not an ETW conclusion.
- ETW has not independently OBSERVED live campaign infrastructure.

## Suggested handling

1. Treat as **defensive threat-intelligence referral**, not a completed criminal case file.
2. Correlate published domain / hash / URI-path indicators against existing FBI/IC3 holdings.
3. Request sample acquisition through normal vendor/legal channels if needed — this package does not contain malware binaries.
4. Keep this family **separate** from other Emerging Threat Watch packages (especially NodeRabbit `ETW-NRB-IC3` / `dded86972e9347e0be27a6597b4cf08a`) unless linkage evidence appears.

## Evidence inventory (ETW retained)

- **Package ID:** `ETW-POL-IC3` / folder `05-pollcat`
- **PRIMARY-SOURCE indicators in `03_INDICATORS.csv`:** **16** rows (**domain** ×4, **http_endpoint** ×4, **filename** ×3, **md5** ×1, **url** ×1, **scheduled_task_prefix** ×1, **path** ×1, **sha256** ×1)
- **Provenance rule:** Indicators are transcribed from public vendor research only. ETW has **not** executed malware and has **not** contacted suspected C2.
- **Local freezes:** `evidence/primary-sources/pollcat/` (and dual refs where noted)
- **Caveats:** See `05_CAVEATS_AND_LIMITS.md` — author/operator identity remains NOT_ESTABLISHED by ETW unless a court/LE source states otherwise.

## Additional primary / dual reference

- Dual-referenced with NodeRabbit Securelist disclosure — **do not merge** implant authorship.
- French Cyberveille mirror retained under `evidence/primary-sources/pollcat/`.
