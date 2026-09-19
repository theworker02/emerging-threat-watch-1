# PollCat — Evidence Retained (Reporter Checklist)

**Package:** `ETW-POL-IC3`

Retain locally (do not upload malware binaries to IC3 web forms):

- [ ] Saved copies / screenshots of primary research pages listed in `04_SOURCES.md` (HTML + timestamp)
- [ ] This package folder (all seven files)
- [ ] Full ETW investigation folder if available: `investigations/pollcat/`
- [ ] Any **independent** OBSERVED validation results (CT/pDNS/hash enrichment) — label clearly as OBSERVED with date/method
- [ ] Reporter contact information and any related complaint/tip numbers

## Do not include in public IC3 text fields unless asked

- Full malware binaries or packed archives
- Victim PII beyond what IC3 explicitly requests
- Credentials, session tokens, or private keys obtained from any environment
- Active C2 interaction logs (ETW policy forbids C2 contact)

## Repository cross-reference (Emerging Threat Watch)

| Artifact | Path |
|----------|------|
| Indicators | `investigations/pollcat/evidence/published-indicators.csv` |
| Claims | `investigations/pollcat/claims/claims-ledger.csv` |
| Gaps | `investigations/pollcat/gaps/priority-gaps.csv` |
| Lineage note | `shared/lineage/pollcat-noderabbit-lineage-note.md` |
| IC3 draft (repo) | `reports/pollcat/POLLCAT_IC3_BRIEF.md` |
| This LE package | `reports/law-enforcement/packages/05-pollcat/` |
