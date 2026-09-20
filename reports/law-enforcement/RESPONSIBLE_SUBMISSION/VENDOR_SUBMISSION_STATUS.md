# Vendor / CERT submission status (non-PII)

**Updated (UTC):** 2026-09-20T16:12:00Z  
**Rule:** Human-responsible defensive TI only. No auto-IC3. No malware attachments.  
**Private log (message IDs, full To/From):** `../private/VENDOR_SUBMISSION_LOG.md` (gitignored)  
**Ready-to-send packs:** `../private/vendor-submissions/<family>/` (gitignored)

## Environment blockers (this agent run)

| Channel | Status | Detail |
|---------|--------|--------|
| Resend MCP | **Blocked** | `list-domains` → no domains; `list-api-keys` → no keys; `mcp_auth` failed (`Interaction query handler is not initialized`) |
| IC3 auto-file | **Not attempted** (policy) | Human files only |
| Hosting/ASN abuse | **Blocked** | No ETW lab PCAP + SHA-256 gate |
| ThreatFox API | **Not submitted** | No abuse.ch Auth-Key in environment |

**Result:** All vendor/CERT items below are **PREPARED / PASTE-READY only** — none emailed from this environment.

## Per-family matrix

| Package | Family | Tracked brief | Non-PII email draft | Private pack | Actually emailed? |
|---------|--------|---------------|---------------------|--------------|-------------------|
| 10 | TencShell | [`briefs/10-tencshell.md`](briefs/10-tencshell.md) | [`email-drafts/10-tencshell.txt`](email-drafts/10-tencshell.txt) | `private/vendor-submissions/10-tencshell/` | No — prepared only |
| 11 | MiniFast | [`briefs/11-minifast.md`](briefs/11-minifast.md) | [`email-drafts/11-minifast.txt`](email-drafts/11-minifast.txt) | `private/vendor-submissions/11-minifast/` | No — prepared only |
| 12 | Argamal | [`briefs/12-argamal.md`](briefs/12-argamal.md) | [`email-drafts/12-argamal.txt`](email-drafts/12-argamal.txt) | `private/vendor-submissions/12-argamal/` | No — prepared only |
| 13 | Okobot | [`briefs/13-okobot.md`](briefs/13-okobot.md) | [`email-drafts/13-okobot.txt`](email-drafts/13-okobot.txt) | `private/vendor-submissions/13-okobot/` | No — prepared only |
| 14 | Matanbuchus | [`briefs/14-matanbuchus.md`](briefs/14-matanbuchus.md) | [`email-drafts/14-matanbuchus.txt`](email-drafts/14-matanbuchus.txt) | `private/vendor-submissions/14-matanbuchus/` | No — prepared only |
| 15 | StarlandRAT | [`briefs/15-starlandrat.md`](briefs/15-starlandrat.md) | [`email-drafts/15-starlandrat.txt`](email-drafts/15-starlandrat.txt) | `private/vendor-submissions/15-starlandrat/` | No — prepared only |
| 04 | NodeRabbit | [`briefs/04-noderabbit.md`](briefs/04-noderabbit.md) | [`email-drafts/04-noderabbit.txt`](email-drafts/04-noderabbit.txt) | `private/vendor-submissions/04-noderabbit/` | No — prepared only |
| 05 | PollCat | [`briefs/05-pollcat.md`](briefs/05-pollcat.md) | [`email-drafts/05-pollcat.txt`](email-drafts/05-pollcat.txt) | `private/vendor-submissions/05-pollcat/` | No — prepared only |
| 06 | SynkLoader | [`briefs/06-synkloader.md`](briefs/06-synkloader.md) | [`email-drafts/06-synkloader.txt`](email-drafts/06-synkloader.txt) | `private/vendor-submissions/06-synkloader/` | No — prepared only |
| 08 | Abyssos | [`briefs/08-abyssos.md`](briefs/08-abyssos.md) | [`email-drafts/08-abyssos.txt`](email-drafts/08-abyssos.txt) | `private/vendor-submissions/08-abyssos/` | No — prepared only |
| 09 | SharkLoader | [`briefs/09-sharkloader.md`](briefs/09-sharkloader.md) | [`email-drafts/09-sharkloader.txt`](email-drafts/09-sharkloader.txt) | `private/vendor-submissions/09-sharkloader/` | No — prepared only |

## How to continue filing (human)

1. Open `private/COMPLAINANT_PROFILE.md` for Reply-To / signature.
2. Open `private/vendor-submissions/<family>/EMAIL_DRAFT.txt` (includes To/Subject/Body).
3. Send **one family per message** from a mailbox you control.
4. Append Message-ID + timestamp to `private/VENDOR_SUBMISSION_LOG.md`.
5. Update this file’s “Actually emailed?” column (still no PII).
6. Optional: ThreatFox after Auth-Key — see [`VENDOR_CONTACTS.md`](VENDOR_CONTACTS.md).
7. IC3 for 10–15 remains human paste via `packages/*/IC3_PASTE_READY.md` — separate from vendor mail.
