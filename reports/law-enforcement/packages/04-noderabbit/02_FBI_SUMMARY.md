# NodeRabbit — FBI / Field-Office Summary

**Package:** `ETW-NRB-IC3` · **Status:** DRAFT · **Cutoff:** 2026-09-19

## One-paragraph summary

I am reporting defensive threat-intelligence information concerning the cross-platform NodeRabbit malware documented by Kaspersky GReAT on September 1, 2026. Kaspersky reports that attackers posing as recruiters delivered malicious coding assessments containing bundled Node.js components. The malware supports Windows, Linux and macOS, with later variants adding enterprise-proxy support, WSL persistence, mutable command-and-control configuration, a fake local VS Code extension displayed as GitHub Copilot Helper, and persistence through local Git post-merge and post-checkout hooks. Kaspersky attributes the campaign to Mirage Kitten; I am identifying that attribution as Kaspersky's assessment rather than as an independently established conclusion. PollCat, co-disclosed in the same article, is filed separately (ETW-POL-IC3); RankChallenge-react is a PollCat lure, not a NodeRabbit IOC.

## Why this may matter to FBI cyber / IC3 correlation

Cross-platform spyware targeting MEA developer environments; Azure/Cloudflare-backed C2; mutable C2 lists; fake VS Code extension and Git-hook persistence

## Highest-value indicators (primary-source; not ETW-observed)

- 10 Kaspersky-published NodeRabbit archive MD5 values (Front-Technical-Challenge.zip etc.); RankChallenge MD5 lives under POL-IND-0001
- Non-Azure domains: visitfinancedentists.com; healthcomfsdpower.com; msmanagementgrp.com; msmanagementgrpmedia.com
- Multiple *.azurewebsites.net hosts (see 03_INDICATORS.csv)
- NameCheap pattern assets NRB-IND-0029–0039 (ASSOCIATION_ONLY); PolySwarm RELATED_SAMPLE SHA-256 NRB-IND-0040–0041
- Local-bundle npm launchers NRB-IND-0042–0044: `colorized_terminal@2.1.0`, `pretty-log@2.1.0`, `node_modules/.cache/.320697f1/index.js` (not PollCat; not public `pretty-log@0.1.0`)
- Host pivots: shepherd-persist Git hooks; fake GitHub Copilot Helper VS Code extension; Linux paths under ~/.config/microsoft-edge-update and ~/.config/intel-dsa

Full table: `03_INDICATORS.csv`

## Critical analytical caveats

- Mirage Kitten attribution is Kaspersky's assessment — not independently established by ETW.
- Git hooks are local persistence unless further evidence shows repository/supply-chain propagation.
- Preserve published MD5 archive hashes; SHA-256 enrichment still pending authorized metadata (OPEN).
- agent:servers can replace C2 lists — domain IOCs are perishable; prefer host artifacts.
- Azure/Cloudflare edge IPs are not actor-owned infrastructure.
- RankChallenge-react MD5 (795e053a…) is PollCat — NRB-IND-0011 is CROSS_REF_POLLCAT only; do not treat as NodeRabbit IOC.
- `colorized_terminal` / `pretty-log@2.1.0` are NodeRabbit local-bundle launchers (NRB-IND-0042–0044) — not PollCat; do not treat registry `pretty-log@0.1.0` as IOC.
- Pattern-based NameCheap domains (NRB-IND-0029–0039) and PolySwarm SHA-256s (NRB-IND-0040–0041) are ASSOCIATION_ONLY / RELATED_SAMPLE — not sample-bound NodeRabbit implant proof.
- COMMON TECHNIQUE overlap with PollCat (recruiter ZIP / Azure-CF C2) is Moderate; implant divergence is High — see shared/lineage/pollcat-noderabbit-lineage-note.md. Do not merge authorship.

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
