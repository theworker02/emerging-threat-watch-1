# Responsible Multi-Channel Submission

**Rule:** Human files only. Never auto-submit. One family = one complaint / ticket.  
**PII:** Complainant identity stays offline in `../private/COMPLAINANT_PROFILE.md` (gitignored).

## Channel matrix

| Channel | Audience | When ready | Minimum evidence | ETW status |
|---------|----------|------------|------------------|------------|
| **IC3** | FBI Internet Crime Complaint Center | Narrative + PRIMARY IOCs + caveats | Structured dossier (`IC3_FULL_PACKAGE.md`); no malware binaries | Packages 01–09 `FILED_IC3`; 10–15 `PRIMARY_FROZEN` |
| **FBI tips / field office** | tips.fbi.gov or local cyber squad | After IC3 ID (preferred) | `02_FBI_SUMMARY.md` + CSV + sources + IC3 ID | Optional follow-on |
| **Hosting / ASN abuse** | ISP / VPS / cloud abuse desks | Non-CDN IP + port + timed PCAP + SHA-256 | Takedown template | **Blocked** — no ETW lab PCAP yet |
| **Registrar / DNS** | Domain registrar abuse | Domain + pDNS + sample hash | Domain list + hash | Partial for some families |
| **Vendor / CERT coordination** | Vendor research / national CERTs | Public research confirmation | PRIMARY article pointer + ETW package | Briefs under `briefs/` · [`VENDOR_CONTACTS.md`](VENDOR_CONTACTS.md) |
| **Platform Trust & Safety** | GitHub / Discord / Telegram / etc. | Platform-hosted lure with IDs | Repo/URL/IDs + timestamps | Family-specific when PRIMARY has them |
| **Cybercrime trackers** | abuse.ch ThreatFox / URLhaus | Auth-Key + PRIMARY provenance | Hash / URL / IP per tracker rules | When Auth-Key available |

## Filing order (per family)

1. Confirm case isolation and `05_CAVEATS_AND_LIMITS.md`.  
2. Use offline complainant profile (never commit PII).  
3. File **IC3** from `IC3_FULL_PACKAGE.md` + `02`–`05` materials.  
4. Record Submission ID in `IC3_FILING_RECORD.md` and `MASTER_INDEX.csv`.  
5. Optional: FBI tips citing IC3 ID.  
6. Parallel: vendor/CERT brief from `briefs/` (no shared-operator claims across families).  
7. Hosting/registrar only when PCAP + SHA-256 + non-CDN IP:port exist ([`docs/ENFORCEMENT_READINESS.md`](../../../docs/ENFORCEMENT_READINESS.md)).

## Package readiness

| Package | Family | IC3 | Vendor brief | Hosting abuse |
|---------|--------|-----|--------------|---------------|
| 01–09 | (see MASTER_INDEX) | `FILED_IC3` | Optional update | Gap: PCAP |
| 10 | TencShell | `PRIMARY_FROZEN` | `briefs/10-tencshell.md` | IPs published; no ETW PCAP |
| 11 | MiniFast | `PRIMARY_FROZEN` | `briefs/11-minifast.md` | ≠ PollCat |
| 12 | Argamal | `PRIMARY_FROZEN` | `briefs/12-argamal.md` | Limited IPv4 |
| 13 | Okobot | `PRIMARY_FROZEN` | `briefs/13-okobot.md` | IPs published; no ETW PCAP |
| 14 | Matanbuchus | `PRIMARY_FROZEN` | `briefs/14-matanbuchus.md` | ≠ SynkLoader |
| 15 | StarlandRAT | `PRIMARY_FROZEN` | `briefs/15-starlandrat.md` | Multiple IPs; no ETW PCAP |

Defensive TI referrals to verified vendor/CERT contacts are ongoing. Public contact list: [`VENDOR_CONTACTS.md`](VENDOR_CONTACTS.md) · matrix: [`VENDOR_EMAIL_MATRIX.md`](VENDOR_EMAIL_MATRIX.md).

## Safe phrasing

- “Defensive threat-intelligence referral / public-research retention.”  
- “PRIMARY-SOURCE indicators transcribed from [vendor]; ETW did not execute malware or contact C2.”  
- “Author/operator identity NOT_ESTABLISHED unless a court/LE source states otherwise.”  
- Never invent dollar loss, victim names, or shared-operator links across families.

## Related

- [`VENDOR_CONTACTS.md`](VENDOR_CONTACTS.md)  
- [`VENDOR_EMAIL_MATRIX.md`](VENDOR_EMAIL_MATRIX.md)  
- [`THREATFOX_AND_HOSTING.md`](THREATFOX_AND_HOSTING.md)  
- [`../HOW_TO_FILE.md`](../HOW_TO_FILE.md)  
- [`../SUBMISSION_CHECKLIST.md`](../SUBMISSION_CHECKLIST.md)  
- [`../../../docs/ENFORCEMENT_READINESS.md`](../../../docs/ENFORCEMENT_READINESS.md)  
- ATT&CK: [`../../landscape/ATTACK_CORPUS_MAP.md`](../../landscape/ATTACK_CORPUS_MAP.md)  
