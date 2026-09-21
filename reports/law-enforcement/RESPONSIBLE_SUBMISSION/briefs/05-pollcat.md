# Vendor / CERT / infra brief — PollCat (`ETW-POL-IC3`)

**Audience:** Vendor PSIRT / CERT coordination (optional update after IC3)  
**IC3 status:** `FILED_IC3` `98a4444754324e539dbbffcb10c70637`  
**PRIMARY:** Kaspersky GReAT / Securelist (Mirage Kitten dual-ref with NodeRabbit)  
**Case isolation:** PollCat only — **do not merge with MiniFast or NodeRabbit**.

## One-paragraph referral

Emerging Threat Watch filed an IC3 complaint retaining PRIMARY-SOURCE public research on **PollCat**, an obfuscated JavaScript RAT documented by Kaspersky GReAT alongside NodeRabbit under the Mirage Kitten dual-referenced Securelist artifact. Implant divergence is high; delivery overlap is moderate only. ETW did **not** execute samples or contact suspected C2. Operator legal identity is **NOT_ESTABLISHED** by ETW.

## Useful pointers

- Package: `reports/law-enforcement/packages/05-pollcat/`
- Preferred public contacts: `intelreports@kaspersky.com`; `cert@cert.org` — see [`../VENDOR_CONTACTS.md`](../VENDOR_CONTACTS.md)
- Repo: https://github.com/theworker02/emerging-threat-watch-1

## Hosting abuse gate

Require non-CDN IP + port + timed PCAP + SHA-256. PCAP gap remains.
