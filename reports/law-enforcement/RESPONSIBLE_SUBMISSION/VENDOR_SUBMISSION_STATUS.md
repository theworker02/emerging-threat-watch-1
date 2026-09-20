# Vendor / CERT submission status (non-PII)

**Updated (UTC):** 2026-09-20T16:55:20Z  
**Rule:** Human-responsible defensive TI only. No auto-IC3. No malware attachments.  
**Private log (message IDs, full To/From):** `../private/vendor-submissions/SEND_LOG.md` (gitignored)

## Channel status

| Channel | Status | Detail |
|---------|--------|--------|
| Gmail MCP | **SENT** | **30** defensive TI referral emails (12 R1 + 7 R2 + 6 R3 + 1 R4 + 4 R5) as of 2026-09-20T16:55:20Z |
| Resend | Unused | No domain/API key required after Gmail auth succeeded |
| IC3 auto-file | **Not attempted** (policy) | Human files packages 10–15 via paste packs |
| Hosting/ASN abuse | **Blocked** | No ETW lab PCAP + SHA-256 gate |
| ThreatFox API | **Not submitted** | No abuse.ch Auth-Key in environment |
| Microsoft WDSI | **Portal only** | No email — https://www.microsoft.com/en-us/wdsi/filesubmission · private helper `../private/vendor-submissions/round5-portals/` |
| Cisco Talos Reputation | **Portal only** | Cisco login required — https://talosintelligence.com/reputation_center/ · no campaign-TI email |

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

## Round 2 — detailed dossiers / new vendors

Sent 2026-09-20T16:50:23Z via Gmail MCP `send_message`. Non-PII recipients and message IDs only.

| Package / draft | Recipients (public) | Gmail message ID | Actually emailed? |
|-----------------|---------------------|------------------|-------------------|
| 01 Rapuncel dossier | CERT/CC; CISA Contact | `1a0bfb9386a38986` | Yes |
| 02 Settra dossier | CERT/CC; CISA Contact | `1a0bfb93bdace761` | Yes |
| 03 RatHat dossier | CERT/CC; CISA Contact | `1a0bfb93da658146` | Yes |
| 07 Showboat dossier | CERT/CC; CISA Contact | `1a0bfb93de7d45c3` | Yes |
| Check Point CPR MiniFast | cpr@checkpoint.com | `1a0bfb9ae61547df` | Yes |
| GitHub SIRT Rapuncel | security@github.com | `1a0bfb9b0c296f98` | Yes |
| CERT/CC full repo index | cert@cert.org | `1a0bfb9b205135d7` | Yes |

## Round 3 — additional verified orgs / affected-publisher dossiers

Sent 2026-09-20T16:52:35Z. Targets are PRIMARY publishers, detection vendors, and community correlation desks with documented public intakes.

| Package / draft | Recipients (public) | Gmail message ID | Actually emailed? |
|-----------------|---------------------|------------------|-------------------|
| LastPass Rapuncel dossier | securitydisclosure@lastpass.com | `1a0bfbb92fbe1d2a` | Yes |
| eSentire Matanbuchus + Cruciferra | security@esentire.com | `1a0bfbb945e88c06` | Yes |
| Unit 42 MiniFast (NOT breach) | unit42-investigations@paloaltonetworks.com | `1a0bfbb974a3cc5a` | Yes |
| Team Cymru full repo dossier | security@cymru.com | `1a0bfbb96cc44cd7` | Yes |
| Shadowserver IOC catalog | abuse@shadowserver.org | `1a0bfbb986649d6b` | Yes |
| Cynet Settra detection feedback | support@cynet.com | `1a0bfbb9aa8c3cc9` | Yes |

## Round 4 — platform / OS vendor affected by mobile malware

Sent 2026-09-20T16:53:30Z.

| Package / draft | Recipients (public) | Gmail message ID | Actually emailed? |
|-----------------|---------------------|------------------|-------------------|
| Android Security Okobot | security@android.com | `1a0bfbcb35187409` | Yes |

## Round 5 — ESET / CERT / CISA / SentinelLabs (+ MS/Talos portals)

Sent 2026-09-20T16:55:20Z.

| Package / draft | Recipients (public) | Gmail message ID | Actually emailed? |
|-----------------|---------------------|------------------|-------------------|
| ESET Research Lab IOC dossier | samples@eset.com | `1a0bfbe1d2e12e14` | Yes (no binaries) |
| CERT/CC Round-5 infra update | cert@cert.org | `1a0bfbe1f0e07b89` | Yes |
| CISA Round-5 material findings | Contact@mail.cisa.dhs.gov; central@cisa.dhs.gov | `1a0bfbe202d3ba9a` | Yes |
| SentinelLabs research dossier | labs@sentinelone.com | `1a0bfbe20a9cb33c` | Yes |
| Microsoft Security Intelligence | WDSI portal | — | **Portal only** (no email) |
| Cisco Talos File/Web/IP reputation | Reputation Center portals | — | **Portal only** (Cisco login) |

## Intentionally not emailed (no suitable public TI mailbox)

| Org / channel | Why skipped |
|---------------|-------------|
| Expel (SynkLoader PRIMARY) | Blog/phone contact only; no published TI intake email |
| Zscaler ThreatLabz (Abyssos) | Public blog + IOC GitHub; no published TI mailbox |
| Huntress / Morphisec (Matanbuchus) | VDP / legal contacts only — product-vuln channel misuse avoided |
| Cisco Talos ESA / `psirt@cisco.com` | Customer sample aliases / product PSIRT — wrong channel for campaign TI email |
| Microsoft WDSI | Portal-only; FAQ: no email samples |
| Cato / Hunt.io | Product CNA / no TI mailbox |
| Hosting / ASN / registrar abuse | Blocked until ETW PCAP + SHA-256 gate |

## Notes

- One family per message where applicable (case isolation). Matanbuchus kept separate from SynkLoader; MiniFast separate from PollCat.
- Round 5: ESET `samples@eset.com` received IOC/URL dossier **without** passworded malware archives (ETW no-binary policy). Microsoft + Talos documented as human portal follow-ups.
- No malware binaries attached to any email.
- Check Sent folder in Gmail to confirm delivery; some gov/vendor mailboxes may auto-ack or filter.
