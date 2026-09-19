# Showboat — FBI / Field-Office Summary

**Package:** `ETW-SHO-IC3` · **Status:** DRAFT · **Cutoff:** 2026-09-19

## One-paragraph summary

I am reporting defensive threat-intelligence information concerning Showboat as publicly documented by Lumen Black Lotus Labs (May 2026 disclosure). Lumen describes a modular Linux post-exploitation framework used against telecommunications organizations. Published artifacts support historical activity: a Pastebin hide-code drop first posted in January 2022 and Black Lotus Labs IOC hosts first seen as early as 2023-04-04. Historical activity versus disclosure date remains an intelligence gap. Lumen publishes C2 and impersonation infrastructure including telecom.webredirect.org resolving to 139.84.227.139, related hosts, sample SHA-256 values (including Linux d6a4fad5448838dbc8cc6b33f1dbfbdc7a2fad36de58ff6a66dce96f729f7011), and a hardcoded XOR config key. I have retained the public research URL and the published Showboat_IOCs.txt appendix. I have not executed malware samples and have not contacted suspected command-and-control systems.

## Why this may matter to FBI cyber / IC3 correlation

Telecom-oriented Linux post-exploitation; historical activity may predate 2026 public disclosure.

## Highest-value indicators (primary-source; not ETW-observed)

- Primary C2: telecom.webredirect.org → 139.84.227.139; second C2 194.135.25.132
- Impersonation: singtelcom.site @ 23.27.201.160; kaztelecom.shop @ 101.36.105.222
- Linux sample SHA-256: d6a4fad5448838dbc8cc6b33f1dbfbdc7a2fad36de58ff6a66dce96f729f7011
- Historical hosting: 103.10.145.129 (first_seen 2023-04-04); Pastebin hide-code Jan 2022
- BLL C2 table IPv4 set plus secondary cluster 192.9.141.111 / 64.176.43.209
- Picus SECONDARY hide strings SHO-IND-0023–0026: `ukpkmkk.c` / `ukpkmkk.so` / `kworkers|dbus|autoupdate` / `/etc/ld.so.preload`
- See 03_INDICATORS.csv (SHO-IND-0001–0026)

Full table: `03_INDICATORS.csv`

## Critical analytical caveats

- Historical activity (Pastebin Jan 2022; BLL IPs from 2023-04) vs May 2026 disclosure dating is an intelligence gap — do not collapse into first-seen 2026.
- IPv4/domain/hash rows are PRIMARY-SOURCE from Lumen article and BLL Showboat_IOCs.txt — not ETW live contact.
- 116.169.244.208 is ASSOCIATION_ONLY (possible upstream/dev) — not confirmed actor-owned C2.
- CDN demotion N/A for these BLL/Lumen-listed hosts; author identity remains NOT_ESTABLISHED (vendor cites PRC-aligned clusters — ETW does not independently establish).
- SHO-IND-0023–0026 hide strings are Picus SECONDARY (SHO-CLAIM-0009/0010) — not Lumen PRIMARY; do not elevate without independent paste freeze.
- Do not invent additional telecom victim names or backdate beyond published ranges.

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
