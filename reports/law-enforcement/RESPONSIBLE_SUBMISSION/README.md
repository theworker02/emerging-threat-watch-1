# Responsible Multi-Channel Submission Framework

**Status:** Active guidance (Emerging Threat Watch)  
**Rule:** Human files only. Never auto-submit. One family = one complaint / ticket.  
**PII:** Complainant identity lives only in `../private/COMPLAINANT_PROFILE.md` (gitignored).

## Channel matrix

| Channel | Audience | When ready | Minimum evidence | ETW status |
|---------|----------|------------|------------------|------------|
| **IC3** | FBI Internet Crime Complaint Center | Narrative + PRIMARY IOCs + caveats | Paste pack / form fields; no malware binaries | Packages 01–09 `FILED_IC3`; 10–15 paste-ready |
| **FBI tips / field office** | tips.fbi.gov or local cyber squad | After IC3 ID (preferred) | `02_FBI_SUMMARY.md` + CSV + sources + IC3 ID | Optional follow-on |
| **Hosting / ASN abuse** | ISP / VPS / cloud abuse desks | Non-CDN IP + port + timed PCAP + SHA-256 | See takedown template | **Blocked** — no ETW lab PCAP yet |
| **Registrar / DNS** | Domain registrar abuse | Domain + active/pDNS + sample hash showing check-in | Domain list + hash | Partial for some families |
| **Vendor / CERT coordination** | Vendor PSIRT / national CERTs | Public research confirmation; infra still live | Pointer to PRIMARY article + ETW CSV | Briefs under `briefs/` · contacts [`VENDOR_CONTACTS.md`](VENDOR_CONTACTS.md) · status [`VENDOR_SUBMISSION_STATUS.md`](VENDOR_SUBMISSION_STATUS.md) · drafts `email-drafts/` · private packs `../private/vendor-submissions/` |
| **Platform Trust & Safety** | GitHub / Discord / Telegram / etc. | Platform-hosted lure or seller channel with IDs | Repo/URL/IDs + timestamps | Family-specific when PRIMARY has them |
| **Cybercrime trackers** | abuse.ch / ThreatFox / URLhaus (Auth-Key) | PRIMARY or OBSERVED with clear provenance | Hash / URL / IP per tracker rules | When Auth-Key available |

## Filing order (per family)

1. Confirm case isolation and `05_CAVEATS_AND_LIMITS.md`.
2. Paste complainant from `../private/COMPLAINANT_PROFILE.md`.
3. File **IC3** using `packages/NN-<family>/IC3_PASTE_READY.md` (or private narrative helpers).
4. Record Submission ID on `main` (`IC3_FILING_RECORD.md`, `MASTER_INDEX.csv`).
5. Optional: FBI tips citing IC3 ID.
6. Parallel: vendor/CERT brief from `briefs/` (no shared-operator claim across families).
7. Hosting/registrar only when PCAP + SHA-256 + non-CDN IP:port exist ([`docs/ENFORCEMENT_READINESS.md`](../../../docs/ENFORCEMENT_READINESS.md)).

## Package readiness snapshot

| Package | Family | IC3 | Vendor/CERT brief | Hosting abuse | Notes |
|---------|--------|-----|-------------------|---------------|-------|
| 04 | NodeRabbit | `FILED_IC3` | `briefs/04-noderabbit.md` | Gap: PCAP | Kaspersky intelreports / CERT |
| 05 | PollCat | `FILED_IC3` | `briefs/05-pollcat.md` | Gap: PCAP | ≠ MiniFast |
| 06 | SynkLoader | `FILED_IC3` | `briefs/06-synkloader.md` | Gap: PCAP | ≠ Matanbuchus |
| 08 | Abyssos | `FILED_IC3` | `briefs/08-abyssos.md` | Gap: PCAP | |
| 09 | SharkLoader | `FILED_IC3` | `briefs/09-sharkloader.md` | Gap: PCAP | |
| 01–03, 07 | (filed) | `FILED_IC3` | Optional update | Gap: PCAP | Do not re-file without update flag |
| 10 | TencShell | Paste-ready | `briefs/10-tencshell.md` | IPs published; PCAP lack | |
| 11 | MiniFast | Paste-ready | `briefs/11-minifast.md` | Azure hostnames; few IPv4 | Do not merge PollCat |
| 12 | Argamal | Paste-ready | `briefs/12-argamal.md` | Limited IPv4 | |
| 13 | Okobot | Paste-ready | `briefs/13-okobot.md` | IPs published; PCAP lack | |
| 14 | Matanbuchus | Paste-ready | `briefs/14-matanbuchus.md` | Comparator ≠ SynkLoader | Separate from SynkLoader filing |
| 15 | StarlandRAT | Paste-ready | `briefs/15-starlandrat.md` | Multiple IPs; PCAP lack | |

**Send status (2026-09-20):** **30** defensive TI referral emails sent via Gmail MCP (Rounds 1–5), including ESET `samples@eset.com`, CERT/CC + CISA Round-5 updates, and SentinelLabs `labs@sentinelone.com`. Microsoft WDSI and Cisco Talos Reputation Center remain **portal-only** (no campaign-TI email). See [`VENDOR_SUBMISSION_STATUS.md`](VENDOR_SUBMISSION_STATUS.md) · [`VENDOR_EMAIL_MATRIX.md`](VENDOR_EMAIL_MATRIX.md) · [`VENDOR_CONTACTS.md`](VENDOR_CONTACTS.md). Private message IDs: `../private/vendor-submissions/SEND_LOG.md`.

## Safe phrasing (all channels)

- “Defensive threat-intelligence referral / public-research retention.”
- “PRIMARY-SOURCE indicators transcribed from [vendor]; ETW did not execute malware or contact C2.”
- “Author/operator identity NOT_ESTABLISHED unless a court/LE source states otherwise.”
- Never invent dollar loss, victim names, Beacon hashes, or shared-operator links.

## Related

- [`VENDOR_CONTACTS.md`](VENDOR_CONTACTS.md)
- [`VENDOR_EMAIL_MATRIX.md`](VENDOR_EMAIL_MATRIX.md)
- [`VENDOR_SUBMISSION_STATUS.md`](VENDOR_SUBMISSION_STATUS.md)
- [`THREATFOX_AND_HOSTING.md`](THREATFOX_AND_HOSTING.md)
- [`../HOW_TO_FILE.md`](../HOW_TO_FILE.md)
- [`../SUBMISSION_CHECKLIST.md`](../SUBMISSION_CHECKLIST.md)
- [`../TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](../TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md)
- [`../../../docs/ENFORCEMENT_READINESS.md`](../../../docs/ENFORCEMENT_READINESS.md)
- ATT&CK maps: [`../../../reports/landscape/ATTACK_CORPUS_MAP.md`](../../landscape/ATTACK_CORPUS_MAP.md)
