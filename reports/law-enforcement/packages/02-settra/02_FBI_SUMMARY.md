# Settra — FBI / Field-Office Summary

**Package:** `ETW-SET-IC3` · **Status:** DRAFT · **Cutoff:** 2026-09-19

## One-paragraph summary

I am reporting defensive threat-intelligence information concerning ransomware/extortion activity publicly tracked as Settra. Cynet, Huntress and MOXFIVE have independently published incident-response or technical findings related to this operation. Cynet reverse engineered a password-gated two-stage Windows encryptor and found that the encryptor itself did not contain file-exfiltration functionality. Huntress reported two incidents using MeshAgent and identified 45.13.122.7 and 193.5.65.114 as MeshAgent infrastructure during those incidents. Huntress also reported the workstation identifier WIN-LIVFRVQFMKO, which it had observed in other malicious activity before Settra's public emergence. Kaspersky GERT separately documented WIN-LIVFRVQFMKO as an SSL certificate common name on port 7777 of a Hetzner-hosted host during FortiClient EMS exploitation research — that sighting is a multi-campaign hostname lead and is not Settra-exclusive. Passive urlscan observations show MeshCentral panels on 193.5.65.114 earlier than the Huntress association window (including id-manulife.com overlap), and RDAP lists the address under Rapid Seedbox allocation NL-RAPIDSEEDBOX-20250306. I am retaining these historical relationships as investigative leads and am not attributing the older incidents or hosting allocation to Settra without additional evidence.

## Why this may matter to FBI cyber / IC3 correlation

Enterprise ransomware with documented MeshAgent C2 IPs and BYOVD/defense-impairment tooling in IR reporting

## Highest-value indicators (primary-source; not ETW-observed)

- MeshAgent C2 IPv4: 45.13.122.7 (July 2026 Huntress); 193.5.65.114 (Sept 2026 Huntress; earlier MeshCentral OBSERVED_PASSIVE — not exclusive)
- Workstation lead: WIN-LIVFRVQFMKO (Huntress + Kaspersky SSL CN — not Settra-exclusive proof)
- Overlap leads: id-manulife.com; tlsIssuer MeshCentralRoot-eca57f (SET-IND-0015/0016)
- Ransom notes: RESTORE_FILES.txt / RESTORE_FILES.html
- Extensions: .locked / .locked_wip; naming pattern *_win64.exe
- BYOVD filenames: gdrv.sys; STProcessMonitor_v114.sys (operator tooling context)

Full table: `03_INDICATORS.csv`

## Critical analytical caveats

- Encryptor (malware) and operator intrusion tooling are separate — do not say "Settra uses Mimikatz."
- WIN-LIVFRVQFMKO is an investigative lead (Huntress + Kaspersky SSL CN) — UNKNOWN / not Settra-exclusive; do not backdate Settra to 2024.
- 193.5.65.114 MeshCentral chronology and Rapid Seedbox RDAP are INFRASTRUCTURE_OVERLAP leads — not Settra-exclusive ownership.
- Public pages analyzed for this corpus did not yield a usable Settra sample SHA-256 list.
- OBSERVED_PASSIVE MeshCentral/RDAP facts are not campaign-ownership claims.

## Suggested handling

1. Treat as **defensive threat-intelligence referral**, not a completed criminal case file.
2. Correlate MeshAgent / domain / hash / URI-path indicators against existing FBI/IC3 holdings.
3. Request sample acquisition through normal vendor/legal channels if needed — this package does not contain malware binaries.
4. Keep this family **separate** from other Emerging Threat Watch packages unless linkage evidence appears.

## Contact block (reporter fills before filing)

| Field | Value |
|-------|-------|
| Reporter name | _[TO BE FILLED]_ |
| Organization (if any) | _[TO BE FILLED]_ |
| Email / phone | _[TO BE FILLED]_ |
| Preferred contact method | _[TO BE FILLED]_ |
| Related IC3 complaint number(s) | _[IF ANY]_ |
| Related FBI tip / case number(s) | _[IF ANY]_ |
