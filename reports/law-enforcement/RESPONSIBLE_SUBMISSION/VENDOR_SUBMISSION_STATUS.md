# Vendor / CERT submission status (non-PII)

**Updated (UTC):** 2026-09-20T16:30:52Z  
**Rule:** Human-responsible defensive TI only. No auto-IC3. No malware attachments.  
**Private log (message IDs, full To/From):** `../private/vendor-submissions/SEND_LOG.md` (gitignored)

## Channel status

| Channel | Status | Detail |
|---------|--------|--------|
| Gmail MCP | **SENT** | 12 defensive TI referral emails sent 2026-09-20T16:30:52Z |
| Resend | Unused | No domain/API key required after Gmail auth succeeded |
| IC3 auto-file | **Not attempted** (policy) | Human files packages 10–15 via paste packs |
| Hosting/ASN abuse | **Blocked** | No ETW lab PCAP + SHA-256 gate |
| ThreatFox API | **Not submitted** | No abuse.ch Auth-Key in environment |

## Sent matrix (Gmail message IDs — no reporter PII)

| Package / draft | Recipients (public) | Gmail message ID | Actually emailed? |
|-----------------|---------------------|------------------|-------------------|
| 04 NodeRabbit | Kaspersky intelreports; CERT/CC | `1a0bfa699cc7afa2` | Yes |
| 05 PollCat | Kaspersky intelreports; CERT/CC | `1a0bfa69b965038a` | Yes |
| 06 SynkLoader | CERT/CC; CISA Contact | `1a0bfa69c3345c8d` | Yes |
| 08 Abyssos | CERT/CC; CISA Contact | `1a0bfa69eef8bdf9` | Yes |
| 09 SharkLoader | Kaspersky intelreports; CERT/CC | `1a0bfa736e8cbac0` | Yes |
| 10 TencShell | CERT/CC; CISA Contact | `1a0bfa739d838118` | Yes |
| 11 MiniFast | CERT/CC; CISA Contact | `1a0bfa73b1be1576` | Yes |
| 12 Argamal | Kaspersky; CERT/CC; CISA Contact | `1a0bfa73cdc0efcd` | Yes |
| 13 Okobot | Kaspersky; CERT/CC; CISA Contact | `1a0bfa7b34fceed0` | Yes |
| 14 Matanbuchus | CERT/CC; CISA Contact | `1a0bfa7b6d454ace` | Yes |
| 15 StarlandRAT | CERT/CC; CISA Contact | `1a0bfa7b991d6c72` | Yes |
| CISA Central corpus | central@cisa.dhs.gov | `1a0bfa7bae2947ed` | Yes |

## Notes

- One family per message (case isolation). Matanbuchus kept separate from SynkLoader; MiniFast separate from PollCat.
- No malware binaries attached.
- Check Sent folder in Gmail to confirm delivery; some gov mailboxes may auto-ack or filter.
