# Technique Comparators (COMMON TECHNIQUE only)

Emerging Threat Watch may compare **shared technique classes** across families for defensive detection and tradecraft awareness. These rows are **not** authorship, operator, or lineage claims.

Machine-readable: [`../intelligence/technique-comparators.csv`](../intelligence/technique-comparators.csv).

| Family A | Family B | Shared technique | Class | Authorship link |
|----------|----------|------------------|-------|-----------------|
| SynkLoader | Matanbuchus | Microsoft Teams phishing; ChaCha20 crypto patterns | COMMON TECHNIQUE | **NOT_ESTABLISHED** |
| SynkLoader | ClickFix / Pikabot | Social-engineering paste/exec (user-assisted command run) | COMMON TECHNIQUE | **NOT_ESTABLISHED** |
| Rapuncel | Lumma / Vidar | Commodity stealer MaaS marketplace context | TECHNIQUE/MARKET CLASS | **NOT_ESTABLISHED** |

## Rules

1. Every comparator row must set `authorship_link=NOT_ESTABLISHED` unless a **PRIMARY-SOURCE** establishes shared implant authorship or operator identity.
2. Matanbuchus is a **comparator** for SynkLoader Teams + ChaCha20 tradecraft — not ETW-attributed SynkLoader lineage. See [`investigations/synkloader/docs/research-notes.md`](../investigations/synkloader/docs/research-notes.md).
3. Lumma / Vidar / RedLine remain **candidates** and market-context comparators for Rapuncel — do not merge IC3 packages or steal authorship.
4. ClickFix is a **technique class** (social-engineering paste/exec), not a malware family ownership claim.
5. Candidate catalog: [`CANDIDATE_FAMILIES.md`](CANDIDATE_FAMILIES.md). Underground / tracker methodology: [`../shared/methodology/UNDERGROUND_AND_COMMODITY_RAT_OSINT.md`](../shared/methodology/UNDERGROUND_AND_COMMODITY_RAT_OSINT.md).

## Related lineage notes

Family-specific lineage matrices (when present) live under `intelligence/lineage_comparison.csv` and investigation `docs/`. Those rows follow the same non-attributive default unless confidence and provenance say otherwise.
