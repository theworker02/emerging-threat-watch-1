# SynkLoader — FBI / Field-Office Summary

**Package:** `ETW-SYN-IC3` · **Status:** DRAFT · **Cutoff:** 2026-09-19

## One-paragraph summary

I am reporting defensive threat-intelligence information concerning SynkLoader as publicly documented by Expel on August 20, 2026. Expel describes a modular mixed-language loader delivered through Microsoft Teams phishing posing as IT helpdesk (external *.onmicrosoft.com tenant, display name IT Service Desk), with initial MSI hosted on Azure Blob Storage (filereserve.blob.core.windows.net/.../331.msi, product name PowershellCleaner). Expel reports nested PowerShell decryption into an in-memory Python loader (ss.py), fake Visual C++ DLLs (msvcp150.dll / msvcp160.dll), a fake Windows 11 lock-screen credential-theft module (PhishLocker), and additional modules including TrafficRedirector and StreamMaster VNC. Expel published loader C2 domains neversoftmain.net, rootfarmapp.net, and tripinupdate.net; TrafficRedirector C2 dondermicapp.net; StreamMaster C2 aroclenetapp.net; and modified ChaCha20 sigma constants mlswgtppayebtezk / lwifnrfiosmfrubf. I have retained the public research and indicator records. Passive DNS A mappings for selected published domains are labeled OBSERVED_PASSIVE and are not live command-and-control contact. I have not executed malware samples and have not contacted suspected command-and-control systems.

## Why this may matter to FBI cyber / IC3 correlation

Teams helpdesk phishing with fake lock-screen credential theft and tunneling into enterprise environments.

## Highest-value indicators (primary-source; not ETW-observed)

- Delivery URL (Expel): https://filereserve.blob.core.windows.net/vgnghuyk/331/331.msi
- SHA-256 (Expel): 331.msi; cleaner.ps1; archive6.zip; ss.py; msvcp150/160.dll; module loaders — see 03_INDICATORS.csv
- C2 domains (Expel PRIMARY): neversoftmain.net; rootfarmapp.net; tripinupdate.net; dondermicapp.net; aroclenetapp.net
- C2 IPv4 (OBSERVED_PASSIVE A): 149.248.76.220; 162.33.177.8; 216.245.184.14; 64.94.85.67
- ChaCha sigma constants (Expel): mlswgtppayebtezk; lwifnrfiosmfrubf
- PDB path (Expel): C:\Users\genry\source\repos\pwshnewdll\...\pwshnewdll.pdb
- See 03_INDICATORS.csv (SYN-IND-0001–0029)

Full table: `03_INDICATORS.csv`

## Critical analytical caveats

- Domain/hash/URL rows are PRIMARY-SOURCE (Expel); IPv4 rows SYN-IND-0026–0029 are OBSERVED_PASSIVE DNS A mappings — not live C2 contact.
- CDN demotion N/A for these non-CDN C2 A records; author identity remains NOT_ESTABLISHED.
- Shared ASN AS399629 across multiple apexes is INFRASTRUCTURE_OVERLAP candidate only — not operator identity.
- Azure Blob MSI host edge IP is ASSOCIATION_ONLY (not actor-owned).
- Secondary ransomware-follow-on / IAB framing is Expel low–medium confidence or secondary press — not established by ETW.
- Resolving a published domain != proof C2 is currently active.

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
