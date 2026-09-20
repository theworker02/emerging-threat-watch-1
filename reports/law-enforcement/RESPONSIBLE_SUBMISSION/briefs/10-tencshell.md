# Vendor / CERT / infra brief — TencShell (`ETW-TEN-IC3`)

**Audience:** Vendor PSIRT / CERT / hosting abuse (after IC3)  
**IC3 paste pack:** [`../../packages/10-tencshell/IC3_PASTE_READY.md`](../../packages/10-tencshell/IC3_PASTE_READY.md)  
**PRIMARY:** Cato CTRL; Hunt.io follow-on  
**Case isolation:** TencShell only — no shared-operator claim with other ETW families.

## One-paragraph referral

Emerging Threat Watch is retaining PRIMARY-SOURCE public research on **TencShell**, a remote-access / intrusion toolset documented by Cato CTRL (2026) with Hunt.io infrastructure follow-on. ETW transcribed published indicators into package `ETW-TEN-IC3` and has **not** executed samples or contacted suspected C2. Operator legal identity is **NOT_ESTABLISHED** by ETW; China-linked framing is vendor assessment only.

## Useful pointers

- Package: `reports/law-enforcement/packages/10-tencshell/`
- Indicators: `03_INDICATORS.csv` (TEN-IND rows)
- Caveats: `05_CAVEATS_AND_LIMITS.md`
- Repo: https://github.com/theworker02/emerging-threat-watch-1

## Hosting abuse gate

Require non-CDN IP + port + timed PCAP + sample SHA-256 before ASN tickets. See [`docs/ENFORCEMENT_READINESS.md`](../../../../docs/ENFORCEMENT_READINESS.md).
