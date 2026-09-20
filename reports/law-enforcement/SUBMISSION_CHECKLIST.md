# Pre-Submission Checklist — FBI / IC3

Complete **one checklist per package**. Keep completed checklists offline if they contain complainant PII.

**Package ID:** _______________  
**Reviewer name:** _______________  
**Review date (UTC):** _______________

## A. Case isolation

- [ ] This filing covers **one family only**
- [ ] No indicators or attribution copied from another ETW family without linkage evidence
- [ ] Landscape / trust-surface notes were **not** used as shared-operator claims

## B. Provenance language

- [ ] Narrative uses “researchers reported” / “I retained” where appropriate
- [ ] Does **not** claim ETW independently discovered the family (unless true)
- [ ] Does **not** label infrastructure `OBSERVED` unless an OBSERVED row exists with method + timestamp
- [ ] Vendor attribution is labeled as **that vendor’s assessment**

## C. Facts vs speculation

- [ ] No dollar-loss figure unless the reporter can document it
- [ ] No invented victim names or victim counts
- [ ] No fabricated SHA-256 / domains / C2 hosts
- [ ] Analytical caveats in `05_CAVEATS_AND_LIMITS.md` were read and accepted

## D. Package completeness

- [ ] `02_FBI_SUMMARY.md` reviewed
- [ ] `03_INDICATORS.csv` present and PRIMARY-SOURCE labeled
- [ ] `04_SOURCES.md` lists exact primary URLs
- [ ] `05_CAVEATS_AND_LIMITS.md` accepted
- [ ] `IC3_FULL_PACKAGE.md` narrative reviewed
- [ ] No malware binaries included

## E. Channel choice

- [ ] IC3 vs FBI tips vs hosting abuse roles understood ([`HOW_TO_FILE.md`](HOW_TO_FILE.md))
- [ ] Hosting abuse **not** attempted without PCAP + SHA-256 gate

## F. After filing

- [ ] IC3 Submission ID recorded in `IC3_FILING_RECORD.md`
- [ ] `MASTER_INDEX.csv` updated
- [ ] Optional FBI tip cites the IC3 ID
