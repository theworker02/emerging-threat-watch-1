# Vendor / CERT / infra brief — MiniFast (`ETW-MNF-IC3`)

**Audience:** Vendor PSIRT / CERT / cloud abuse (after IC3)  
**IC3 paste pack:** [`../../packages/11-minifast/IC3_PASTE_READY.md`](../../packages/11-minifast/IC3_PASTE_READY.md)  
**PRIMARY:** Check Point Research; Unit 42  
**Case isolation:** MiniFast only — **do not merge with PollCat**. IRGC/Nimbus attribution = vendor only.

## One-paragraph referral

Emerging Threat Watch is retaining PRIMARY-SOURCE public research on **MiniFast** / related MiniUpdate AppDomain-hijack tooling documented by Check Point Research and Unit 42. ETW transcribed published indicators into package `ETW-MNF-IC3` and has **not** executed samples or contacted suspected C2. Operator legal identity is **NOT_ESTABLISHED** by ETW.

## Useful pointers

- Package: `reports/law-enforcement/packages/11-minifast/`
- Indicators: `03_INDICATORS.csv` (MNF-IND rows)
- Caveats: `05_CAVEATS_AND_LIMITS.md`
- Repo: https://github.com/theworker02/emerging-threat-watch-1

## Preferred public contacts

- CERT/CC: `cert@cert.org`
- CISA Central: `Contact@mail.cisa.dhs.gov`
- Draft: [`../email-drafts/11-minifast.txt`](../email-drafts/11-minifast.txt) · private pack: `../../private/vendor-submissions/11-minifast/`

## Hosting abuse gate

Azure Web App hostnames dominate public IOCs; standalone C2 IPv4 may be sparse. Require SHA-256 + timed check-in evidence before provider tickets.
