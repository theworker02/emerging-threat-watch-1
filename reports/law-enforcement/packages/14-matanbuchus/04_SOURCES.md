# Matanbuchus — Primary Sources

**Package:** `ETW-MAT-IC3` · **Role:** TECHNIQUE_COMPARATOR for SynkLoader (do **not** file jointly)

## Organizations

Huntress · Zscaler ThreatLabz · Morphisec · eSentire

## Primary source URLs

- https://www.huntress.com/blog/clickfix-matanbuchus-astarionrat-analysis
- https://www.zscaler.com/blogs/security-research/technical-analysis-matanbuchus-3-0
- https://www.morphisec.com/blog/ransomware-threat-matanbuchus-3-0-maas-levels-up/
- https://www.esentire.com/security-advisories/matanbuchus-malware

## Local archive

- `evidence/primary-sources/matanbuchus/huntress-matanbuchus-astarionrat.html` (PS-MAT-001)
  - SHA-256: `61db6ae84078463576b58b48bcf79d489adeeb5b05f4658fdb29e840a07904e7`
- `evidence/primary-sources/matanbuchus/zscaler-matanbuchus-3-0.html` (PS-MAT-002)
  - SHA-256: `e87ea40c35ccd224c6f4651de679b0ab81b4333e1519dcb9585c44aea2c2da7d`
- `evidence/primary-sources/matanbuchus/morphisec-matanbuchus-3-0-teams.html` (PS-MAT-003)
  - SHA-256: `02ed074df2016dfe30ed37c128fb2e35eb57c2fae627883d366f79bf4d84522f`
- `evidence/primary-sources/matanbuchus/esentire-matanbuchus.html` (PS-MAT-004)
  - SHA-256: `697dec7e62d556cda4075e193e06ca7e37beb3d9a76f65558795661614ab5422`

## Campaign isolation

Huntress documents ClickFix → Matanbuchus 3.0 → AstarionRAT. Morphisec documents Teams/Quick Assist → Matanbuchus 3.0 MaaS with distinct IOCs (`fixuplink.com`, `libcurl.dll` sideload). Both are valid Matanbuchus 3.0 evidence; do **not** merge operator identity with SynkLoader.

## Provenance rule

These URLs are **PRIMARY-SOURCE** publications. Retrieving or retaining them does **not** make infrastructure `OBSERVED` by the Emerging Threat Watch investigation.
