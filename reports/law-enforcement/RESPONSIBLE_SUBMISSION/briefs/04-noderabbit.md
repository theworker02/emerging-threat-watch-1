# Vendor / CERT / infra brief — NodeRabbit (`ETW-NRB-IC3`)

**Audience:** Vendor PSIRT / CERT coordination (optional update after IC3)  
**IC3 status:** `FILED_IC3`  
**PRIMARY:** Kaspersky GReAT / Securelist  
**Case isolation:** NodeRabbit only — **do not merge with PollCat**.

## One-paragraph referral

Emerging Threat Watch filed an IC3 complaint retaining PRIMARY-SOURCE public research on **NodeRabbit**, a developer-targeted Node.js RAT documented by Kaspersky GReAT (Mirage Kitten framing is vendor attribution). ETW transcribed published indicators and did **not** execute samples or contact suspected C2. Operator legal identity is **NOT_ESTABLISHED** by ETW.

## Useful pointers

- Package: `reports/law-enforcement/packages/04-noderabbit/`
- Preferred public contacts: `intelreports@kaspersky.com`; `cert@cert.org`
- Repo: https://github.com/theworker02/emerging-threat-watch-1

## Hosting abuse gate

Require non-CDN IP + port + timed PCAP + SHA-256.
