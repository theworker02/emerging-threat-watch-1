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
| Check Point Research | `cpr@checkpoint.com` | MiniFast / Screening Serpens research correlation | Documented CPR research contact |
| GitHub Security | `security@github.com` | Platform Trust & Safety when PRIMARY cites GitHub-hosted lure/infra | Rapuncel package context |
| LastPass securitydisclosure | `securitydisclosure@lastpass.com` | Rapuncel (LastPass TIME / Delphos PRIMARY) researcher dossier | Not a LastPass product-vuln claim |
| eSentire security | `security@esentire.com` | Matanbuchus + Cruciferra/Rapuncel lineage dossiers | Not an MDR customer ticket |
| Unit 42 investigations | `unit42-investigations@paloaltonetworks.com` | MiniFast awareness only — **not** a breach/IR request | Explicit non-incident framing required |
| Team Cymru | `security@cymru.com` | Community / network TI correlation of full repo | Not an abuse complaint against Cymru |
| Shadowserver | `abuse@shadowserver.org` | Network-reporting correlation of PRIMARY IOC catalog | Not `report_admin@` subscription admin |
| Cynet support | `support@cynet.com` | Settra detection-coverage feedback | Prefer over `responsible-disclosure@` (product vulns) |
| Android Security | `security@android.com` | Android malware reports (Okobot Accessibility abuse) | Android Security FAQ malware reporting channel |
| ESET Research Lab | `samples@eset.com` | Suspicious file/site / IOC researcher dossiers | [KB141](https://support.eset.com/en/kb141-submit-a-virus-website-or-potential-false-positive-sample-to-the-eset-lab) — **no binaries from ETW** |
| SentinelLabs | `labs@sentinelone.com` | Researcher malware-family / TI correlation | GitHub org public email; not `security@` VDP |
| Microsoft WDSI | [File submission portal](https://www.microsoft.com/en-us/wdsi/filesubmission) | Samples / hashes / detection gaps | **No email** — portal only |
| Cisco Talos Reputation | [Reputation Center](https://talosintelligence.com/reputation_center/) | File / Web / IP / Domain reputation tickets | Cisco account required; not ESA sample aliases |
| Sekoia CERT / TDR | `cert@sekoia.com` · `tdr@sekoia.io` | CERT (RFC 2350) + Threat Detection & Research collaboration | Prefer CERT for incidents; TDR for research |
| Datadog Security Labs | `securitylabs@datadoghq.com` | Researcher / detection-engineering correlation | Not `security@` (product VDP) |
| CERT-GIB (Group-IB) | `response@cert-gib.com` | Malware intelligence / CERT referral | FIRST-listed CERT-GIB |
| Infoblox Threat | `reportthreat@infoblox.com` | Malicious domain/IP reporting (non-customer) | Not `security-report@` (product VDP) |
| G DATA CSIRT | `csirt@gdata.de` | Malware / CSIRT correlation | Prefer over `psirt@` for TI |
| Expel | `security@expel.io` | SynkLoader publisher / TI correlation | Distinct from `bug-reports@` VDP |
| ANY.RUN | `newvirus@any.run` | New malware / IOC awareness | No binaries from ETW |
| GreyNoise Labs | `labs@greynoise.io` · `research@greynoise.io` | Internet / infra IOC correlation | Labs public contact |
| Orange Cyberdefense CERT | `cert-contact.ocd@orange.com` | CERT TI / incident correlation | FIRST Global CERT OCD |
| Gridinsoft | `virus@gridinsoft.com` · `antimalware@gridinsoft.com` | Okobot companion / malware TI | FP form also exists — frame as TI not FP |
| IBM X-Force Exchange | `xfe@us.ibm.com` | TI platform awareness | Not `psirt@us.ibm.com` |
| Cybereason | `security@cybereason.com` | Campaign / malware research liaison | Redirect if VDP-only |
| HarfangLab | `contact@harfanglab.fr` | CTR research forward | General intake — request CTR routing |
| Bitdefender Labs | `virus_submission@bitdefender.com` | Labs IOC correlation | Portal preferred for samples; no ETW binaries |

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
