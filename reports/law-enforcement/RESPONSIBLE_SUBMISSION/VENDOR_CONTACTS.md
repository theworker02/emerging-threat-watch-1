# Public vendor / CERT reporting contacts

**Rule:** Only use addresses documented on vendor/CERT public pages. Do not invent contacts.  
**PII:** Reporter identity stays in `../private/COMPLAINANT_PROFILE.md` — never commit it here.  
**Send status:** See [`VENDOR_SUBMISSION_STATUS.md`](VENDOR_SUBMISSION_STATUS.md). Ready-to-send packs (with reply-to): `../private/vendor-submissions/` (gitignored).

## Cross-cutting CERT / national channels

| Channel | Address / portal | Use for | Notes |
|---------|------------------|---------|-------|
| CERT/CC | `cert@cert.org` · [VINCE](https://vince.cert.org/) | Coordinated disclosure / sensitive TI | Prefer VINCE when possible ([PGP note](https://certcc.github.io/pgp/)) |
| CISA Central | `Contact@mail.cisa.dhs.gov` · `central@cisa.dhs.gov` · [Incident Reporting System](https://www.cisa.gov/resources-tools/resources/incident-reporting-system) | Voluntary cyber activity / TI referral | Public CISA contact pages; not a substitute for IC3 |
| Kaspersky Intelligence Reporting | `intelreports@kaspersky.com` | Extended IoC / TI product inquiries (Securelist footnote) | Documented on Securelist articles; **not** a malware-binary drop box |
| Kaspersky ICS CERT | `ics-cert@kaspersky.com` | ICS/OT-scoped questions | [ICS CERT services](https://ics-cert.kaspersky.com/services/) |
| Kaspersky incident form | [Report an incident](https://www.kaspersky.com/enterprise-security/contact-investigation) | Customer incident response | Web form — not email from this environment |
| abuse.ch ThreatFox | [Share IOCs](https://threatfox.abuse.ch/share/) · [API](https://threatfox.abuse.ch/api/) | Community malware IOC share (Auth-Key) | Requires Auth-Key; submit **PRIMARY** IOCs only with provenance; no invented IoCs |

## Family → preferred public contacts

| Package | Family | Primary publishers | Preferred public contact(s) | Suitability |
|---------|--------|--------------------|----------------------------|-------------|
| 10 | TencShell | Cato CTRL; Hunt.io | CERT/CC `cert@cert.org`; CISA Central; (Cato product PSIRT `vulnerability-report@catonetworks.com` is **product vuln only** — not malware TI referral) | CERT/CISA referral OK; do **not** misuse Cato CNA mailbox for TI |
| 11 | MiniFast | Check Point Research; Unit 42 | CERT/CC; CISA Central; vendor web research contact forms if used | Email only to verified CERT/CISA unless vendor publishes a TI inbox |
| 12 | Argamal | Kaspersky GReAT / Securelist | `intelreports@kaspersky.com`; CERT/CC; CISA Central | Kaspersky TI mailbox documented on Securelist |
| 13 | Okobot | Kaspersky GReAT; Gridinsoft | `intelreports@kaspersky.com`; CERT/CC; CISA Central | Same as Argamal; keep case isolated |
| 14 | Matanbuchus | Huntress; Morphisec; Zscaler; eSentire | CERT/CC; CISA Central | Separate from SynkLoader; no shared-operator claim |
| 15 | StarlandRAT | Cisco Talos | CERT/CC; CISA Central; Cisco PSIRT `psirt@cisco.com` **only for Cisco product vulns** — not campaign TI | Talos spam/virus sample inboxes are for ESA customers — not this use case |
| 04 | NodeRabbit | Kaspersky GReAT | `intelreports@kaspersky.com`; CERT/CC | Filed IC3 — optional vendor update |
| 05 | PollCat | Kaspersky GReAT | `intelreports@kaspersky.com`; CERT/CC | Filed IC3 — **≠ MiniFast** |
| 06 | SynkLoader | Expel | CERT/CC; CISA Central | Filed IC3 — **≠ Matanbuchus** |
| 08 | Abyssos | Zscaler ThreatLabz | CERT/CC; CISA Central | Filed IC3 |
| 09 | SharkLoader | Kaspersky GReAT (StrikeShark) | `intelreports@kaspersky.com`; CERT/CC | Filed IC3 |

## Hosting / ASN / registrar

**Blocked for ETW lab packages** until non-CDN IP + port + timed PCAP + sample SHA-256 exist. See [`docs/ENFORCEMENT_READINESS.md`](../../../docs/ENFORCEMENT_READINESS.md) and [`../TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](../TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md).

## ThreatFox / URLhaus (when Auth-Key available)

1. Obtain Auth-Key at [auth.abuse.ch](https://auth.abuse.ch/).
2. Submit only PRIMARY-SOURCE malware IOCs (hash / domain / IP / URL) with `reference` = Securelist/Talos/etc. URL.
3. Confidence: start ≤50 unless you independently observed the IOC.
4. Do **not** submit phishing-only or spam IOCs to ThreatFox.
5. One family per batch; tag with ETW package ID in comment (e.g. `ETW-ARG-IC3 PRIMARY transcription`).

## Do not send

- Malware binaries or archives
- Complainant SSN/DOB
- Invented dollar loss
- Shared-operator claims across families
- Auto-filed IC3 content as if already accepted by vendors
