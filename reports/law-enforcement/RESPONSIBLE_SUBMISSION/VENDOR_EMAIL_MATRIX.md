# Vendor / CERT email matrix (non-PII)

**Status:** Gmail drafts prepared under gitignored `../private/vendor-submissions/`  
**Automated send:** Blocked until a verified Resend sending domain exists (Gmail cannot be used as Resend `from`).

## Confirmed public reporting addresses used in drafts

| Recipient | Channel purpose | Draft IDs (private) | Confidence |
|-----------|-----------------|---------------------|------------|
| `intelreports@kaspersky.com` | Kaspersky TI Reporting (PRIMARY articles cite this) | sharkloader, okobot, argamal, noderabbit, pollcat | High — published mailto on Securelist |
| `central@cisa.dhs.gov` | CISA Central defensive TI / incident share | cisa-central-etw-corpus | High — CISA public contact |
| `Contact@mail.cisa.dhs.gov` | CISA 24/7 cyber reporting mailbox | cisa-contact-mail | High — CISA contact page |
| `cert@cert.org` | CERT/CC coordination pointer | cert-cc | High — longstanding CERT/CC address |

## Portals (prefer over inventing vendor inboxes)

| Portal | Use |
|--------|-----|
| https://www.ic3.gov/ | Criminal cyber complaint numbers |
| https://tips.fbi.gov/ | Optional FBI tip after IC3 |
| https://www.cisa.gov/report | CISA incident/malware report |
| https://www.cisa.gov/forms/share-indicators | Encrypted indicator share |
| https://threatfox.abuse.ch/share/ | IOC share (abuse.ch login + Auth-Key) |
| https://urlhaus.abuse.ch/ | Malware URL share |

## Not emailed from agent (no verified public mailbox in PRIMARY / or wrong channel)

Vendor research teams (Cato, Hunt.io, Check Point, Unit 42, Cisco Talos research blogs, Huntress, Morphisec, Zscaler, eSentire, LastPass/Delphos, etc.) — use published article contact forms / PSIRT pages rather than guessed `security@` addresses. Talos email sample classification addresses (`*@access.ironport.com`) are for spam/phish sample submission, not family TI packages.

## To enable auto-send via Resend

1. Provide a domain you control (e.g. `yourdomain.com`).
2. Agent creates the Resend domain and shows DNS records.
3. You add DNS → verify → agent can send with `from: reports@yourdomain.com` and `replyTo: matthewlooney5@gmail.com` (reply-to only after you confirm).
