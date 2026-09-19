# Pre-Submission Checklist — FBI / IC3

Complete **one checklist per package**. Print or copy into the package folder as `REVIEW_<date>.md` if desired.

**Package ID:** _______________ (`ETW-RAP-IC3` / `ETW-SET-IC3` / `ETW-RAT-IC3` / `ETW-NRB-IC3`)  
**Reviewer name:** _______________  
**Review date (UTC):** _______________

## A. Case isolation

- [ ] This filing covers **one family only**
- [ ] No indicators or attribution copied from another ETW family without linkage evidence
- [ ] Landscape / trust-surface notes were **not** pasted as shared-operator claims

## B. Provenance language

- [ ] Narrative uses “researchers reported” / “I retained” where appropriate
- [ ] Does **not** claim ETW independently discovered the family (unless true)
- [ ] Does **not** label infrastructure `OBSERVED` unless an OBSERVED row exists with method + timestamp
- [ ] Vendor attribution (e.g., Mirage Kitten) is labeled as **that vendor’s assessment**



## C. Facts vs speculation

- [ ] No dollar-loss figure unless the reporter can document it
- [ ] No invented victim names or victim counts
- [ ] No fabricated SHA-256 / domains / C2 hosts
- [ ] Historical leads (e.g., WIN-LIVFRVQFMKO) are labeled leads, not confirmed campaign history
- [ ] Analytical caveats in `05_CAVEATS_AND_LIMITS.md` were read and accepted



## D. Package completeness

- [ ] `00_COVER_SHEET.md` reviewed
- [ ] `01_NARRATIVE_PASTE.txt` matches approved wording
- [ ] `02_FBI_SUMMARY.md` contact block filled
- [ ] `03_INDICATORS.csv` present and current
- [ ] `04_SOURCES.md` URLs verified reachable or archived locally
- [ ] `06_EVIDENCE_RETAINED.md` retention items completed



## E. Safety

- [ ] No malware binary attached to the web form
- [ ] No C2 interaction was performed to “confirm” indicators
- [ ] No credentials / private keys / session tokens included



## F. After filing

- [ ] IC3 complaint number recorded in `MASTER_INDEX.csv` and `02_FBI_SUMMARY.md`
- [ ] FBI tip / case number recorded if any
- [ ] Local archive of what was submitted (PDF/screenshot of confirmation)

**Decision:** ☐ Ready to file · ☐ Needs revision · ☐ Hold (gaps too material)

**Reviewer signature / initials:** _______________