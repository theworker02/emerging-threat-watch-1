# Buyer evaluation â€” emerging-threat-watch-1

## Goal

In 15â€“45 minutes, verify the Product builds or runs as documented and that proprietary notices are present.

## Steps

1. Confirm root `LICENSE` is proprietary and `ACQUISITION.md` exists.
2. Skim `README.md` install/run claims.
3. Execute:

```
```
reports/law-enforcement/packages/   Investigator packages (02Ã¢â‚¬â€œ05 core + filing records)
reports/law-enforcement/CTI-Evidence-Repository/   STIX / CSV LE ingest tree
reports/landscape/                  Cross-family ATT&CK and evidence completeness
investigations/<family>/            Analyst evidence workspace
intelligence/                       Combined IOC and ATT&CK rollups (canonical CSVs)
docs/                               Methodology catalogs and enforcement readiness
```
```

4. Run tests if present (`npm test`, `pytest`, `cargo test`, `go test ./...`, etc.).
5. Record README vs observed behavior gaps in workpapers.

## Pass criteria

- [ ] Clone succeeds
- [ ] Documented happy path works **or** failure is explained
- [ ] Minimal path needs no surprise secrets
- [ ] License notices intact

*Updated: 2026-09-22*
