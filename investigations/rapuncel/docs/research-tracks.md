# Rapuncel Research Tracks

**Case:** RAP · **Cutoff:** 2026-09-19 · **Baseline:** SOURCE-RAP-001

Rapuncel is modeled as an **ecosystem**, not a single binary.

```text
Distribution / MaaS infrastructure
   ├── fake GitHub brands + SEO
   └── redirect infrastructure
            │
            ▼
     Cruciferra / PUROSANGUE
     loader / crypter layer
            │
            ▼
         Rapuncel
      stealer payload
```

These layers may involve overlapping people. **Do not assume** shared operators without direct evidence (CASE_ISOLATION + LastPass open gaps on MaaS backend structure).

## Tracks

| Track | Focus | Key claim IDs |
|-------|--------|---------------|
| A — Stealer | Collection targets, ABE helper, C2 `2.26.126.50`, persistence service | RAP-CLAIM-0020–0021 |
| B — GitHub/SEO | Fake orgs, Pages portal, fabricated badges, 40+ brands | RAP-CLAIM-0001–0003, 0007 |
| C — Infrastructure | Redirectors, traffic director, payload/terminal domains | RAP-CLAIM-0004–0007, 0032–0034 |
| D — Alinubx.sys | Driver trust chain, CcProtect lineage, blocklist gap | RAP-CLAIM-0015–0018, 0026–0027 |
| E — Cruciferra/PUROSANGUE | Commodity crypter vs stealer authorship | RAP-CLAIM-0019, 0028–0031 |
| F — BoryptGrab lineage | Shared artifacts vs distinct hashes/C2/driver | RAP-CLAIM-0022–0024 |

## Hypothesis RAP-H-CRY

**How much of Rapuncel's sophisticated loader/evasion belongs to Rapuncel vs commodity Cruciferra?**

Evidence for crypter contribution (PRIMARY): NativeAOT sideload DLL, `.reloc`/Base16 container, COM Elevation Moniker UAC bypass, 145 default AV/EDR names, `purosangue.tx` string, Delphos high-confidence PUROSANGUE assessment; eSentire independent PUROSANGUE panel analysis.

Evidence for campaign-specific choices: Alinubx/CcProtect driver instead of eSentire's DCRCVDrv.sys; GitHub/SEO MaaS kit with `albinofennel.com` multi-brand pages.

**Rule:** Do not credit stealer authors with crypter-supplied capabilities without evidence.

## Post-disclosure DNS (SOURCE-RAP-PK-001)

Four of six domains still **resolved** from one UK vantage on 2026-09-19. That is **not** “four C2 servers are active.” Labels: RESOLVING / NXDOMAIN / REACHABLE / SERVING CONTENT — never conflated with CONFIRMED MALICIOUS.
