# Vendor / CERT / infra brief — Matanbuchus (`ETW-MAT-IC3`)

**Audience:** Vendor PSIRT / CERT / hosting abuse (after IC3)  
**IC3 paste pack:** [`../../packages/14-matanbuchus/IC3_PASTE_READY.md`](../../packages/14-matanbuchus/IC3_PASTE_READY.md)  
**PRIMARY:** Huntress; Morphisec; Zscaler; eSentire  
**Case isolation:** Matanbuchus only — **technique comparator** to SynkLoader (`COMMON TECHNIQUE`); **do not merge** with SynkLoader IC3 `3440d0c64dc240499ff66deaa3311a0b`.

## One-paragraph referral

Emerging Threat Watch is retaining PRIMARY-SOURCE public research on **Matanbuchus** loader activity documented by Huntress, Morphisec, Zscaler ThreatLabz, and eSentire. ETW transcribed published indicators into package `ETW-MAT-IC3` and has **not** executed samples or contacted suspected C2. Operator legal identity is **NOT_ESTABLISHED** by ETW. Overlaps with SynkLoader (e.g., Teams IT-helpdesk / ClickFix-class social engineering) are **COMMON TECHNIQUE** only — authorship link **NOT_ESTABLISHED**.

## Useful pointers

- Package: `reports/law-enforcement/packages/14-matanbuchus/`
- Indicators: `03_INDICATORS.csv` (MAT-IND rows)
- Caveats: `05_CAVEATS_AND_LIMITS.md`
- Comparator: `docs/TECHNIQUE_COMPARATORS.md` / `intelligence/technique-comparators.csv`
- Repo: https://github.com/theworker02/emerging-threat-watch-1

## Preferred public contacts

- CERT/CC: `cert@cert.org` · CISA Central: `Contact@mail.cisa.dhs.gov`
- Draft: [`../email-drafts/14-matanbuchus.txt`](../email-drafts/14-matanbuchus.txt) · private pack: `../../private/vendor-submissions/14-matanbuchus/`

## Hosting abuse gate

Require non-CDN IP + port + timed PCAP + SHA-256. Keep SynkLoader tickets analytically separate.
