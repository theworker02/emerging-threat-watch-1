# PollCat Investigation

**Case ID:** `pollcat`  
**Case code:** `POL` / `ETW-POL-IC3`  
**Independence:** Isolated from Rapuncel, Settra, RatHat, NodeRabbit, SynkLoader, and Showboat.

## Research thesis (locked)

- Kaspersky Securelist disclosure **2026-09-01**; discovered **alongside NodeRabbit** during the Mirage Kitten investigation.
- Cross-platform **obfuscated JavaScript RAT**; same **recruiter / coding-challenge** delivery ecosystem as NodeRabbit.
- Public research corpus is **extremely sparse** beyond the primary Securelist article.
- **CRITICAL research question (do NOT assume shared authorship):** Are NodeRabbit and PollCat parallel implants, different generations, specialized payloads, or merely co-deployed by the same intrusion cluster?
- Comparison with NodeRabbit is allowed **only** as `COMMON TECHNIQUE` / lineage assessment. Direct linkage requires artifact-level evidence. **Default: non-authorship / non-shared-operator** until proven.
- July 2026 Mirage Kitten NightLedger report is **attribution/context for Mirage Kitten ops**, not proof that PollCat ≡ NodeRabbit code lineage.
- Primary URL: https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/

## Research emphasis

- Obfuscated JavaScript RAT behavior and C2 polling model
- `RankChallenge-react` / coding-challenge lure forensics
- Persistence (Windows NetSync scheduled task; Linux cron; macOS LaunchAgent) **as published**
- Relationship to NodeRabbit: structure divergence vs co-disclosure — **case isolation still applies for IOC/attribution transfer**
- Sparse-corpus collection (CT/pDNS/archive) for original defensive intel

## Status

Phase 1 package seeded from Kaspersky Securelist primary (dual-referenced with NodeRabbit artifact `PS-NRB-001`). Cases remain separate. **IC3 package `ETW-POL-IC3` filed** — Submission ID `98a4444754324e539dbbffcb10c70637` (2026-09-19 9:52:51 PM EST). See [`reports/law-enforcement/packages/05-pollcat/IC3_FILING_RECORD.md`](../../reports/law-enforcement/packages/05-pollcat/IC3_FILING_RECORD.md).
