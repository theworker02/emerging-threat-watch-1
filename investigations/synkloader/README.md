# SynkLoader Investigation

**Case ID:** `synkloader`  
**Case code:** `SYN` / `ETW-SYN-IC3`  
**Independence:** Isolated from all other ETW families.

## Research thesis (locked)

- **Expel**, August 2026 disclosure; modular loader; mixed-language / memory-resident components.
- Delivery: Microsoft **Teams / IT-helpdesk** phishing; fake lock-screen credential theft; tunneling.
- Compile/distribution timing reported as **~late July 2026** per Expel.
- Research surface: **Windows enterprise / social-engineering intrusion**.
- Primary URL: https://expel.com/blog/synkloader-when-you-throw-in-everything-but-the-kitchen-sink/

## Research emphasis

- Teams helpdesk social engineering and Azure-hosted installer trust abuse
- Multi-language loader modules (Python / PowerShell / C# / C++)
- PhishLocker-style fake Windows lock screen
- Tunneling / proxy for post-credential access
- Passive-grained IOC freeze from Expel primary (do not invent)

## Status

Phase 1 package stub. Primary URL frozen in source-index; claim corpus intentionally thin until deeper extraction.
