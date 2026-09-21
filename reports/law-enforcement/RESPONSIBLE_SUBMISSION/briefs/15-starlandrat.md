# Vendor / CERT / infra brief — StarlandRAT (`ETW-STR-IC3`)

**Audience:** Vendor PSIRT / CERT / hosting abuse (after IC3)  
**Structured dossier:** see package `IC3_FULL_PACKAGE.md` + `02_FBI_SUMMARY.md`
**PRIMARY:** Cisco Talos (UAT-11795 assessment)  
**Case isolation:** StarlandRAT only. UAT-11795 attribution = Talos assessment only.

## One-paragraph referral

Emerging Threat Watch is retaining PRIMARY-SOURCE public research on **StarlandRAT** / related WLDR C2 implant activity documented by Cisco Talos. ETW transcribed published indicators into package `ETW-STR-IC3` and has **not** executed samples or contacted suspected C2. Operator legal identity is **NOT_ESTABLISHED** by ETW; UAT-11795 naming is the vendor’s cluster assessment.

## Useful pointers

- Package: `reports/law-enforcement/packages/15-starlandrat/`
- Indicators: `03_INDICATORS.csv` (STR-IND rows)
- Caveats: `05_CAVEATS_AND_LIMITS.md`
- Repo: https://github.com/theworker02/emerging-threat-watch-1

## Preferred public contacts

- CERT/CC: `cert@cert.org` · CISA Central: `Contact@mail.cisa.dhs.gov`
- Do **not** use Cisco PSIRT / Talos ESA sample inboxes for this campaign TI referral
- Draft: [`../email-drafts/15-starlandrat.txt`](../email-drafts/15-starlandrat.txt) · private pack: `../../private/vendor-submissions/15-starlandrat/`

## Hosting abuse gate

Multiple published IPv4 exist; still require timed PCAP + sample SHA-256 for strong ASN packages. Crypto-contract address is CAMPAIGN_ASSOCIATED metadata, not a hosting takedown target by itself.
