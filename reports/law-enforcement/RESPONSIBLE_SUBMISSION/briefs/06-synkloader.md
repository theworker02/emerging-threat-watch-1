# Vendor / CERT / infra brief — SynkLoader (`ETW-SYN-IC3`)

**Audience:** Vendor PSIRT / CERT coordination (optional update after IC3)  
**IC3 status:** `FILED_IC3` `3440d0c64dc240499ff66deaa3311a0b`  
**PRIMARY:** Expel  
**Case isolation:** SynkLoader only — **do not merge with Matanbuchus** (`COMMON TECHNIQUE` only).

## One-paragraph referral

Emerging Threat Watch filed an IC3 complaint retaining PRIMARY-SOURCE public research on **SynkLoader**, a modular loader / Teams IT-helpdesk phishing chain documented by Expel. ETW did **not** execute samples or contact suspected C2. Operator legal identity is **NOT_ESTABLISHED** by ETW. Technique overlap with Matanbuchus (ClickFix / Teams social engineering class) is **COMMON TECHNIQUE** — authorship link **NOT_ESTABLISHED**.

## Useful pointers

- Package: `reports/law-enforcement/packages/06-synkloader/`
- Preferred public contacts: `cert@cert.org`; CISA Central (`Contact@mail.cisa.dhs.gov`)
- Comparator package: `14-matanbuchus` (separate tickets only)
- Repo: https://github.com/theworker02/emerging-threat-watch-1

## Hosting abuse gate

Require non-CDN IP + port + timed PCAP + SHA-256.
