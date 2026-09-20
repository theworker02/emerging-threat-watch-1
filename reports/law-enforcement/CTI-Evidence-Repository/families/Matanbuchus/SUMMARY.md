# Matanbuchus — Family Summary

**Case ID slug:** `matanbuchus`  
**Package:** `ETW-MAT-IC3`  
**Status:** `PRIMARY_FROZEN`  
**Category:** MaaS loader 3.0 + AstarionRAT (ClickFix / Teams comparator)  
**TLP:** TLP:AMBER+STRICT  
**Generated:** 2026-09-20T02:25:00Z  
**Source:** PRIMARY freeze `PS-MAT-001`

## Executive overview

Defensive threat-intelligence package concerning Matanbuchus 3.0 / AstarionRAT as publicly documented by Huntress (ClickFix delivery chain) with supporting technical context from Zscaler ThreatLabz Matanbuchus 3.0 analysis. Huntress describes ClickFix → silent MSI → Zillya-style DLL sideload → Matanbuchus 3.0 (ChaCha20) → Lua/reflective loader → AstarionRAT. This package is a TECHNIQUE COMPARATOR for SynkLoader (Teams/ClickFix/ChaCha20 class) only. authorship_link SynkLoader=NOT_ESTABLISHED. Do NOT file jointly with SynkLoader. Author/operator identity remains NOT_ESTABLISHED.

## Indicator counts (this build)

| Class | Count |
|-------|------:|
| Domains / URLs | 4 |
| IPs | 1 |
| Hashes | 8 |
| Total IND rows | 15 |

## Case isolation

COMMON TECHNIQUE comparator for SynkLoader only. authorship_link SynkLoader=NOT_ESTABLISHED. See docs/TECHNIQUE_COMPARATORS.md.

## Cross-references

- Investigation: `investigations/matanbuchus/`
- LE package: `reports/law-enforcement/packages/14-matanbuchus/`
- Candidate catalog: `docs/CANDIDATE_FAMILIES.md`
