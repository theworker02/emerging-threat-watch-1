# Transfer Manifest — Emerging Threat Watch

**Date:** 2026-09-21

| Asset | Category | Notes |
|-------|----------|-------|
| repository | TRANSFERABLE | github.com/theworker02/emerging-threat-watch-1 |
| original analysis / indices / methodology | REQUIRES_LEGAL_REVIEW | AI authorship + MIT history |
| evidence/primary-sources/* | PUBLIC/THIRD-PARTY | Vendor copyrights — not exclusive ETW property |
| IOC CSV compilations | REQUIRES_LEGAL_REVIEW | Compilation copyright possible; underlying indicators often public facts |
| LE package templates | TRANSFERABLE | Original forms; no auto-submit |
| malware binaries | NONTRANSFERABLE | Not present; must not be added as assets |
| secrets | NONTRANSFERABLE | Rotate; private/ gitignored |

## Credentials migration checklist (no secrets committed)

- [ ] Inventory GitHub secrets / Actions secrets
- [ ] Inventory cloud API tokens (Cloudflare, etc.)
- [ ] Inventory package registry tokens
- [ ] Inventory signing keys
- [ ] Rotate all of the above at closing — **ROTATE_IMMEDIATELY** if any exposure suspected
- [ ] Buyer creates replacement secrets in buyer-controlled accounts

**NEVER commit credentials.**
