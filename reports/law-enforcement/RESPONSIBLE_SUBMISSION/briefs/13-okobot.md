# Vendor / CERT / infra brief — Okobot (`ETW-OKO-IC3`)

**Audience:** Vendor PSIRT / CERT / hosting abuse (after IC3)  
**IC3 paste pack:** [`../../packages/13-okobot/IC3_PASTE_READY.md`](../../packages/13-okobot/IC3_PASTE_READY.md)  
**PRIMARY:** Kaspersky GReAT / Securelist; Gridinsoft companion  
**Case isolation:** Okobot only. Extended IoCs behind Kaspersky TI service are not invented here.

## One-paragraph referral

Emerging Threat Watch is retaining PRIMARY-SOURCE public research on **Okobot** as documented by Kaspersky GReAT (Securelist) with Gridinsoft companion coverage. ETW transcribed published indicators into package `ETW-OKO-IC3` and has **not** executed samples or contacted suspected C2. Operator legal identity is **NOT_ESTABLISHED** by ETW.

## Useful pointers

- Package: `reports/law-enforcement/packages/13-okobot/`
- Indicators: `03_INDICATORS.csv` (OKO-IND rows)
- Caveats: `05_CAVEATS_AND_LIMITS.md`
- Repo: https://github.com/theworker02/emerging-threat-watch-1

## Preferred public contacts

- Kaspersky Intelligence Reporting: `intelreports@kaspersky.com`
- CERT/CC: `cert@cert.org` · CISA Central: `Contact@mail.cisa.dhs.gov`
- Draft: [`../email-drafts/13-okobot.txt`](../email-drafts/13-okobot.txt) · private pack: `../../private/vendor-submissions/13-okobot/`

## Hosting abuse gate

Published IPv4 exist in package CSV; still require timed PCAP + SHA-256 for ASN abuse packages.
