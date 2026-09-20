# Vendor / CERT email matrix (non-PII)

**Status:** Gmail MCP sends completed (Rounds 1–4). See [`VENDOR_SUBMISSION_STATUS.md`](VENDOR_SUBMISSION_STATUS.md).  
**Resend:** Unused (Gmail auth succeeded).

## Confirmed public reporting addresses used

| Recipient | Channel purpose | Draft IDs / rounds | Confidence |
|-----------|-----------------|---------------------|------------|
| `intelreports@kaspersky.com` | Kaspersky TI Reporting (PRIMARY articles cite this) | Round 1 family packs | High — published mailto on Securelist |
| `central@cisa.dhs.gov` | CISA Central defensive TI / incident share | Round 1 corpus | High — CISA public contact |
| `Contact@mail.cisa.dhs.gov` | CISA 24/7 cyber reporting mailbox | Round 1–2 family packs | High — CISA contact page |
| `cert@cert.org` | CERT/CC coordination pointer | Round 1–2 | High — longstanding CERT/CC address |
| `cpr@checkpoint.com` | Check Point Research MiniFast | Round 2 | High — published CPR contact |
| `security@github.com` | GitHub SIRT / Trust & Safety | Round 2 Rapuncel | High — GitHub security contact |
| `securitydisclosure@lastpass.com` | LastPass / Delphos Rapuncel dossier | Round 3 | High — LastPass disclosure mailbox |
| `security@esentire.com` | eSentire Matanbuchus / Cruciferra | Round 3 | High — published security contact |
| `unit42-investigations@paloaltonetworks.com` | Unit 42 MiniFast awareness (not breach) | Round 3 | High — Unit 42 investigations alias |
| `security@cymru.com` | Team Cymru community TI correlation | Round 3 | High — Team Cymru security |
| `abuse@shadowserver.org` | Shadowserver network reporting correlation | Round 3 | High — Shadowserver abuse |
| `support@cynet.com` | Cynet Settra detection feedback | Round 3 | High — Cynet RD page guidance |
| `security@android.com` | Android malware (Okobot) | Round 4 | High — Android Security FAQ |
| `samples@eset.com` | ESET Research Lab IOC / suspicious-site dossier | Round 5 | High — ESET KB141 |
| `labs@sentinelone.com` | SentinelLabs researcher TI dossier | Round 5 | High — SentinelLabs GitHub org email |

## Portals (prefer over inventing vendor inboxes)

| Portal | Use |
|--------|-----|
| https://www.ic3.gov/ | Criminal cyber complaint numbers |
| https://tips.fbi.gov/ | Optional FBI tip after IC3 |
| https://www.cisa.gov/report | CISA incident/malware report |
| https://www.cisa.gov/forms/share-indicators | Encrypted indicator share |
| https://threatfox.abuse.ch/share/ | IOC share (abuse.ch login + Auth-Key) |
| https://urlhaus.abuse.ch/ | Malware URL share |

## Not emailed from agent (no suitable public TI mailbox / wrong channel)

Remaining PRIMARY publishers without a verified **malware-TI** intake (Expel, Zscaler ThreatLabz, Huntress VDP, Morphisec, Cisco Talos ESA sample aliases, Cato CNA, Hunt.io): use their web forms / PSIRT only when the channel matches product vulns or sample portals — do **not** guess `security@` or misuse VDP. Microsoft WDSI is portal-only (no email). Hosting/ASN abuse remains blocked without ETW PCAP + SHA-256.

## To enable auto-send via Resend

1. Provide a domain you control (e.g. `yourdomain.com`).
2. Agent creates the Resend domain and shows DNS records.
3. You add DNS → verify → agent can send with `from: reports@yourdomain.com` and `replyTo:` from the gitignored complainant profile (confirm reply-to before first send).
