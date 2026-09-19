# RatHat Intelligence Gaps

| Gap | Priority | Current evidence | Required evidence | Status |
|-----|----------|------------------|-------------------|--------|
| Public APK hashes from Zimperium IOC | P0 | 162 SHA-256 in `apks.csv` (metadata) | Package names / signing certs still missing | PARTIAL |
| APK package names / signing certificates | P0 | Not in blog or IOC CSVs; MB/VT unauth failed | Authorized sample metadata | OPEN |
| C2 domains/IPs | P0 | Zimperium c2.csv + urlscan IPs for subset | Broader pDNS; FRP endpoint values | PARTIAL |
| FRP FrpsAddr/Port/Token concrete hosts | P0 | Protocol fields named in primary | Config capture without C2 interaction | OPEN |
| Named generative AI service | P1 | Explicitly unnamed | Do not speculate | UNKNOWN |
| Official Play Protect/ASB on ADB self-pair | P2 | Negative search 2026-09-19 | Google-authored advisory if published | OPEN |
| Geographic attribution strength | P2 | Researcher assessment | Independent corroboration | OPEN |
| Overlap with ToxicPanda/RedHook beyond technique | P2 | Secondary comparison | Code-level evidence | OPEN |
