# ATT&CK Corpus Map — Emerging Threat Watch

**Generated (UTC):** 2026-09-20T16:03:04Z  
**Rule:** PRIMARY-SOURCE behaviors only; case isolation enforced; no invented TTPs.

Canonical per-family files: `investigations/<family>/attack/techniques.md`  
Machine-readable matrix: [`intelligence/attack-mappings-matrix.csv`](../intelligence/attack-mappings-matrix.csv)

## Coverage

| Family | Status | # techniques | Matrix |
|--------|--------|-------------:|--------|
| rapuncel | `ACTIVE` | 9 | enterprise |
| settra | `ACTIVE` | 14 | enterprise |
| rathat | `ACTIVE` | 8 | mobile |
| noderabbit | `ACTIVE` | 9 | enterprise |
| pollcat | `ACTIVE` | 7 | enterprise |
| synkloader | `ACTIVE` | 9 | enterprise |
| showboat | `ACTIVE` | 6 | enterprise |
| abyssos | `ACTIVE` | 8 | enterprise |
| sharkloader | `ACTIVE` | 11 | enterprise |
| tencshell | `PRIMARY_FROZEN` | 12 | enterprise |
| minifast | `PRIMARY_FROZEN` | 10 | enterprise |
| argamal | `PRIMARY_FROZEN` | 8 | enterprise |
| okobot | `PRIMARY_FROZEN` | 14 | enterprise |
| matanbuchus | `PRIMARY_FROZEN_COMPARATOR` | 11 | enterprise |
| starlandrat | `PRIMARY_FROZEN` | 16 | enterprise |

**Total mapped technique rows:** 152 (duplicates across families expected — do not merge cases).

## Cross-family COMMON TECHNIQUE classes (not shared authorship)

| Class | Families (examples) | Notes |
|-------|---------------------|-------|
| Teams IT-helpdesk / social engineering | SynkLoader, Matanbuchus (Morphisec) | technique-comparators.csv |
| ClickFix paste/exec | Matanbuchus (Huntress), StarlandRAT, Okobot (TookPS) | COMMON TECHNIQUE only |
| DLL sideloading | Rapuncel, SharkLoader, Matanbuchus, Argamal | COMMON TECHNIQUE only |
| AppDomain hijacking | MiniFast / Unit 42 MiniUpdate | related actor naming variance |
| Recruiter / coding-challenge delivery | NodeRabbit, PollCat | co-disclosure ≠ shared implant authorship |
| Crypto-wallet targeting | Okobot, StarlandRAT | market/technique class only |

See also [`docs/TECHNIQUE_COMPARATORS.md`](../docs/TECHNIQUE_COMPARATORS.md).
