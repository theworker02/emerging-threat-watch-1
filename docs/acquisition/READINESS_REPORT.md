# Acquisition Readiness Report — Emerging Threat Watch

**Date:** 2026-09-21  
**No numeric score.** Statuses reflect evidence available in-repo and this program.

| Section | Status | Notes |
|---------|--------|-------|
| BUILD | READY | N/A product binary; corpus validation in TEST_EVIDENCE |
| TESTS | READY | Corpus checks verified; no unit test suite |
| SECURITY | READY_WITH_DISCLOSURE | No malware binaries by extension/magic scan (prior audit). No SECRET_FOUND. Do not package malware as acquisition assets. |
| DOCUMENTATION | READY_WITH_DISCLOSURE | Data room created this program |
| IP OWNERSHIP | REQUIRES_LEGAL_REVIEW | Heavy Cursor Agent authorship in git shortlog. No CLA/DCO. Prior ACQUISITION_NOTICE incorrectly clai… |
| LICENSE CLARITY | READY_WITH_DISCLOSURE | Current LICENSE clear; history documented; ETW revocation language corrected if applicable |
| DEPENDENCIES | READY_WITH_DISCLOSURE | No package manager lockfile for a product runtime. Content is docs/CSV/evidence.… |
| THIRD-PARTY ASSETS | READY_WITH_DISCLOSURE / REQUIRES_LEGAL_REVIEW | See diligence |
| DATA RIGHTS | REQUIRES_LEGAL_REVIEW | Especially federated/operator/vendor data |
| REPRODUCIBILITY | READY_WITH_DISCLOSURE | BUYER_DEMO provided |
| TRANSFERABILITY | READY_WITH_DISCLOSURE | See TRANSFER_MANIFEST |
| OPERATIONS | READY_WITH_DISCLOSURE | Handoff + ops docs |
| BUYER DEMO | READY_WITH_DISCLOSURE | Commands verified where stack runnable; see TEST_EVIDENCE |
| KNOWN LIABILITIES | READY_WITH_DISCLOSURE | See DISCLOSURE_SCHEDULE |

## Blockers

### Before outreach
- Fix revocation language (this program)
- Create proper LICENSE_TRANSITION_NOTICE
- NOTICE/THIRD_PARTY inventory incomplete

### Before diligence
- MIT→proprietary irrevocability doctrines
- Bulk vendor HTML republication rights
- AI authorship chain of title
- Detection rules are placeholders

### Before signing
- Counsel opinion on third-party evidence corpus
- Clear schedule of OWNED vs THIRD_PARTY files
- No malware / no stolen-cred warranties

### Before closing
- Do NOT transfer live unauthorized access or malware binaries (none should exist)
- Evidence republication policy agreement
- SPA/APA
