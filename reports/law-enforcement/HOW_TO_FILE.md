# How to File — IC3 and FBI

**Organizational guidance for defensive threat-intelligence reporting. Not legal advice. A human reviewer must approve every filing.**

## Two package classes

| Package | Audience | Emphasize | Guide |
|---------|----------|-----------|-------|
| **FBI / IC3 narrative** | IC3 form; FBI tips / field office | Crime-type language, PRIMARY sources, caveats, indicator CSV on request | This file + `packages/NN-<family>/` |
| **Hosting / registrar / platform takedown** | ASN/hosting abuse, registrars, platform Trust & Safety | IP+port, timed PCAP, sample SHA-256, pDNS, chat IDs + logs | [`TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md) |

IC3 often cannot accept PCAPs — retain them offline and state availability. Hosting abuse usually requires traffic proof. An IC3 narrative is not a complete takedown package. Readiness: [`docs/ENFORCEMENT_READINESS.md`](../../docs/ENFORCEMENT_READINESS.md).

## Which channel?

| Channel | Use when | Do not use for |
|---------|----------|----------------|
| **IC3** ([ic3.gov](https://www.ic3.gov/)) | Cyber complaint / tip for FBI IC3 correlation | Uploading malware binaries; undocumented loss claims |
| **FBI tips / field office** ([tips.fbi.gov](https://tips.fbi.gov/)) | Structured TI package needing investigator attention beyond the web form | Substituting for IC3 when you still need a complaint number — file IC3 first when appropriate |
| **Hosting / registrar / platform abuse** | IP:port + PCAP (or equivalent) / domain + pDNS + sample hash | Substituting for a criminal complaint number |

Many reporters file **IC3 first**, then reference the complaint number in FBI tips or abuse tickets.

## Recommended order per family

1. Open `packages/NN-<family>/` and read `02_FBI_SUMMARY.md` + `05_CAVEATS_AND_LIMITS.md`.  
2. Confirm case isolation (one family only).  
3. Review [`SUBMISSION_CHECKLIST.md`](SUBMISSION_CHECKLIST.md).  
4. Complainant identity stays in offline `private/COMPLAINANT_PROFILE.md` (never commit PII; no SSN/DOB).  
5. **IC3:** use `IC3_FULL_PACKAGE.md` as the structured narrative source; add high-value indicators from `03_INDICATORS.csv` only if space allows — otherwise state that a CSV is retained and available on request. List primary URLs from `04_SOURCES.md`.  
6. Record the IC3 Submission ID in `IC3_FILING_RECORD.md`, `02_FBI_SUMMARY.md`, and `MASTER_INDEX.csv`.  
7. **FBI (optional):** provide `02_FBI_SUMMARY.md` + `03_INDICATORS.csv` + `04_SOURCES.md` + `05_CAVEATS_AND_LIMITS.md`, citing the IC3 ID if available.

## Safe phrasing

**Use**

- “I am reporting defensive threat-intelligence information concerning …”
- “Researchers at [Org] published … on [date] …”
- “I have retained the original public research and indicator records.”
- “I have not executed malware or contacted suspected command-and-control systems.”

**Avoid**

- “I discovered this malware family” (unless independently true)
- Undocumented dollar-loss claims
- Attribution without stating whose assessment
- Merging multiple ETW families into one complaint

## Attachments

IC3 web forms often limit uploads. Prefer:

1. Narrative text in the form  
2. Short indicator list (hashes/domains that fit)  
3. Note: “Full PRIMARY-SOURCE indicator CSV and source list retained under package ID ETW-*-IC3 and available to investigators on request.”

If a field office requests files, send the public `packages/NN-<family>/` folder (no malware binaries).

## Filed packages (01–09)

| Package ID | Family | Status |
|------------|--------|--------|
| ETW-RAP-IC3 | Rapuncel | `FILED_IC3` |
| ETW-SET-IC3 | Settra | `FILED_IC3` |
| ETW-RAT-IC3 | RatHat | `FILED_IC3` |
| ETW-NRB-IC3 | NodeRabbit | `FILED_IC3` |
| ETW-POL-IC3 | PollCat | `FILED_IC3` |
| ETW-SYN-IC3 | SynkLoader | `FILED_IC3` |
| ETW-SHO-IC3 | Showboat | `FILED_IC3` |
| ETW-ABY-IC3 | Abyssos | `FILED_IC3` |
| ETW-SHK-IC3 | SharkLoader | `FILED_IC3` |

Complaint numbers: [`MASTER_INDEX.csv`](MASTER_INDEX.csv) and each `IC3_FILING_RECORD.md`.

There is **no** evidence in this repository that these campaigns share operators. PollCat ≠ NodeRabbit ≠ MiniFast. Matanbuchus is a SynkLoader technique comparator only — do **not** file jointly.

## Primary-frozen packages (10–15)

Structured dossiers (`IC3_FULL_PACKAGE.md` + `02`–`05`) are ready for human filing. Not auto-filed.

| Package ID | Family | Status |
|------------|--------|--------|
| ETW-TEN-IC3 | TencShell | `PRIMARY_FROZEN` |
| ETW-MNF-IC3 | MiniFast | `PRIMARY_FROZEN` |
| ETW-ARG-IC3 | Argamal | `PRIMARY_FROZEN` |
| ETW-OKO-IC3 | Okobot | `PRIMARY_FROZEN` |
| ETW-MAT-IC3 | Matanbuchus | `PRIMARY_FROZEN` (comparator) |
| ETW-STR-IC3 | StarlandRAT | `PRIMARY_FROZEN` |

Vendor briefs: [`RESPONSIBLE_SUBMISSION/briefs/`](RESPONSIBLE_SUBMISSION/briefs/).

## Vendor / CERT coordination

- Contacts: [`RESPONSIBLE_SUBMISSION/VENDOR_CONTACTS.md`](RESPONSIBLE_SUBMISSION/VENDOR_CONTACTS.md)  
- Email matrix: [`RESPONSIBLE_SUBMISSION/VENDOR_EMAIL_MATRIX.md`](RESPONSIBLE_SUBMISSION/VENDOR_EMAIL_MATRIX.md)  
- Family briefs: [`RESPONSIBLE_SUBMISSION/briefs/`](RESPONSIBLE_SUBMISSION/briefs/)  

Human-only sends. No malware binaries. Verified public contacts only.
