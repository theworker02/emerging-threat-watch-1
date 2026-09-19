# Cruciferra / PUROSANGUE Notes (Rapuncel ecosystem layer 2)

**Case scope:** Rapuncel investigation only — Cruciferra is a **commodity crypter service**, not a Rapuncel synonym.  
**Hypothesis:** RAP-H-CRY (see `docs/research-tracks.md`).  
**Cutoff:** 2026-09-19.

## Sources (crypter track)

| ID | Org | URL | Role |
|----|-----|-----|------|
| SOURCE-RAP-001 | LastPass/Delphos | https://blog.lastpass.com/posts/lastpass-delphos-report-rapuncel-infostealer | States Rapuncel loader built with Cruciferra PUROSANGUE (primary for Rapuncel link; ETW 403) |
| RF | Recorded Future | https://www.recordedfuture.com/research/malware-crypting-services-threat-actors | Marketplace listing / pricing tiers |
| ES | eSentire | https://www.esentire.com/blog/malware-as-a-service-cocktail-errtraffic-and-cruciferra-killing-your-edr-since-2025 | ErrTraffic + Cruciferra cocktail (fetched 200) |
| PP | Proofpoint | https://www.proofpoint.com/us/blog/threat-insight/unpacking-cruciferra-analysis-sophisticated-crypter-service | Crypter technical analysis (fetched 200) |

Do **not** treat adversary-simulation blogs as primary evidence of Rapuncel behavior.

## Feature split (as reported across crypter sources — verify per article)

| Product | Form | Reported emphasis | Rough pricing (varies by source — do not merge) |
|---------|------|-------------------|--------------------------------------------------|
| **PUROSANGUE** | Sideloaded DLL / AV-killer tier | AV/EDR process kill; pairs with legitimate host EXE | RF lists AV-Killer Purosangue ~$2000/mo; other writeups cite ~$1200/mo — **record variance** |
| **COCONUT** | Standalone EXE | Defender exclusion style evasion | RF ~$500/mo; other citations ~$650/mo — **record variance** |
| Shared Cruciferra | Base crypting | Shared build | RF ~$145/mo |

## Builder features to map against Rapuncel chain (OPEN)

Legitimate app selection · persistence options · COM Elevation Moniker UAC bypass · AV/EDR kill · file pumping · custom process targets · default ~145 AV/EDR names.

| Rapuncel observation | Possible Cruciferra feature | ETW layer attribution |
|----------------------|----------------------------|------------------------|
| vsdbg.exe + vsdbg.dll sideload | Legitimate app selection / sideload | OPEN (RAP-H-CRY) |
| 148MB / 127.9MB padded ZIPs | File pumping | OPEN |
| 145-name kernel kill via Alinubx | AV killer / process list | OPEN — driver may be operator BYOVD separate from crypter |
| Stealer collection + 2.26.126.50 | Not a crypter feature | Rapuncel payload layer |

## Rule

Never credit **stealer authors** with **crypter-supplied** capabilities without build-level evidence. Tag claims `track:cruciferra`.
