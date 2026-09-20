# How to File — IC3 and FBI

**These steps are organizational guidance for defensive threat-intelligence reporting. They are not legal advice. A human reviewer must approve every filing.**

## Two package classes (different audiences)

| Package | Audience | What to emphasize | Template / guide |
|---------|----------|-------------------|------------------|
| **FBI / IC3 narrative** | IC3 complaint form; FBI tips / field office | Crime-type language, PRIMARY sources, caveats, indicator CSV on request | This file + `packages/0N-<family>/` |
| **Hosting / registrar / platform takedown** | ASN/hosting abuse desks, registrars, Discord/Telegram Trust & Safety | IP+port, timed PCAP, sample SHA-256, pDNS, chat IDs + timestamped logs | [`TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md) · methodology [`shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`](../../shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md) |

Both need **technical telemetry**. IC3 often cannot accept PCAPs — retain them offline and state availability. Hosting abuse tickets usually require traffic proof. Do not treat an IC3 narrative paste as a complete takedown package (or vice versa). Readiness gaps: [`docs/ENFORCEMENT_READINESS.md`](../../docs/ENFORCEMENT_READINESS.md).

## Which channel?

| Channel | Use when | Do not use for |
|---------|----------|----------------|
| **IC3** ([ic3.gov](https://www.ic3.gov/)) | You want a cyber complaint / tip on the public record for FBI Internet Crime Complaint Center correlation | Uploading malware binaries; claiming losses you cannot document |
| **FBI tips / field office** ([tips.fbi.gov](https://tips.fbi.gov/) or local field office cyber squad) | You have a structured TI package and want investigator attention beyond the IC3 web form | Substituting for IC3 if you still want an IC3 complaint number — file IC3 first when appropriate, then reference the number |
| **Hosting / registrar / platform abuse** | You have IP:port + PCAP (or equivalent) / domain + pDNS + sample hash / chat IDs + logs for infrastructure or account removal | Substituting for IC3 when you need a criminal complaint number; authenticating to attacker panels to “gather more” |

Many reporters file **IC3 first** (get a complaint number), then send the same package (or a pointer) to FBI tips / a field-office contact **referencing that IC3 number**. That is optional and depends on your situation. Parallel hosting-abuse tickets may cite the same IC3 number when useful.

## Recommended order per family

1. Open `packages/0N-<family>/` and read `02_FBI_SUMMARY.md` + `05_CAVEATS_AND_LIMITS.md`.  
2. Confirm case isolation (one family only).  
3. Run through `../SUBMISSION_CHECKLIST.md` if filing.  
4. **IC3:** use the local narrative helper at `private/filing-helpers/0N-<family>/01_NARRATIVE_PASTE.txt` (gitignored). Add high-value indicators from `03_INDICATORS.csv` only if the form has space — otherwise state that a CSV is retained and available on request. List primary URLs from `04_SOURCES.md` in the additional-information field.  
5. Save the IC3 confirmation / Submission ID into `IC3_FILING_RECORD.md`, `02_FBI_SUMMARY.md`, and `MASTER_INDEX.csv`.  
6. **FBI (optional):** submit or email `02_FBI_SUMMARY.md` + `03_INDICATORS.csv` + `04_SOURCES.md` + `05_CAVEATS_AND_LIMITS.md`, citing the IC3 Submission ID if you have one.

## What to say in the form (safe phrasing)

**Use**

- “I am reporting defensive threat-intelligence information concerning …”
- “Researchers at [Org] published … on [date] …”
- “I have retained the original public research and indicator records.”
- “I have not executed malware or contacted suspected command-and-control systems.”

**Avoid**

- “I discovered this malware family” (unless you independently discovered it)
- “Victims lost $X” without documented loss
- “Attributed to [APT]” without stating whose assessment
- Merging Rapuncel + Settra + RatHat + NodeRabbit into one complaint

## Attachments

IC3 web forms often limit uploads. Prefer:

1. Narrative text in the form  
2. Short indicator list in the form (hashes/domains that fit)  
3. Note: “Full PRIMARY-SOURCE indicator CSV and source list retained under package ID ETW-*-IC3 and available to investigators on request.”

If a field office requests files, send the entire `packages/0N-<family>/` folder (still no malware binaries).

## Five active filings, not one

| Package ID | Family | Why separate | Status |
|------------|--------|--------------|--------|
| ETW-RAP-IC3 | Rapuncel | Stealer + GitHub distribution; Cruciferra is shared tooling | `FILED_IC3` |
| ETW-SET-IC3 | Settra | Ransomware encryptor ≠ operator intrusion tooling | `FILED_IC3` |
| ETW-RAT-IC3 | RatHat | Android Accessibility/ADB chain | `FILED_IC3` |
| ETW-NRB-IC3 | NodeRabbit | Developer-targeted Node.js RAT; Mirage Kitten is Kaspersky’s attribution | `FILED_IC3` |
| ETW-POL-IC3 | PollCat | Obfuscated JS RAT; RankChallenge lure; co-disclosed with NodeRabbit but **separate implant** | **Next to file** (`DRAFT`) |

There is **no** evidence in this repository establishing that these campaigns share operators. A combined filing would be analytically incorrect unless new linkage evidence appears. PollCat and NodeRabbit share a dual-referenced Securelist primary artifact only — do **not** merge.
