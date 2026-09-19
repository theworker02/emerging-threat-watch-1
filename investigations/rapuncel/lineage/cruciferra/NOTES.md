# Cruciferra / PUROSANGUE Notes (Rapuncel lineage track)

**Sources:** SOURCE-RAP-001 · SOURCE-RAP-ESE-001 (eSentire 2026-08-19) · Proofpoint/Recorded Future cited by primaries  
**Isolation:** Cruciferra ErrTraffic/Remus delivery IOCs are **not** Rapuncel campaign IOCs unless independently linked.

## Packages (eSentire)

| Package | Form | Advertised capability | Price (reported) |
|---------|------|----------------------|------------------|
| PUROSANGUE | Side-loaded DLL (NativeAOT) | AV/EDR killing | ~$1,200/month |
| COCONUT | Standalone EXE | Windows Defender exclusion | ~$650/month |

## Builder options (PUROSANGUE)

Legitimate app for DLL sideload · persistence · COM Elevation Moniker UAC bypass · AV/EDR kill · file pumping · custom process targets · default **145** AV/EDR names · process hollowing targets (e.g. ServiceModelReg.exe).

## Overlap with Rapuncel loader

Delphos high confidence: Rapuncel `vsdbg.dll` is PUROSANGUE or close derivative (`.reloc`/Base16, NativeAOT, 145 targets, `purosangue.tx`).

**Operational difference:** driver selection (Alinubx vs DCRCVDrv).

## Driver / sideload artifacts (2026-09-19 deep pass)

| Artifact | SHA-256 / note | Source | Role vs Rapuncel |
|----------|----------------|--------|------------------|
| `DCRCVDrv.sys` | `87e8d39db624f37d3e77aedf487a2dfd197f71a4730ea74f4e7a4341deaec2ff` | eSentire IOC file `PS-RAP-002` | Cruciferra BYOVD — **not** Rapuncel campaign IOC |
| Cruciferra `mscoree.dll` | `0ae0a7f118b80e4655b8b86bb421c151a8f17930e76e714b2fa199409f3af9ce` | same | Crypter stub — lineage only |
| Device | `\\.\DCRCVDRV_U` vs Rapuncel `\\.\Alinubx` | eSentire blog / LastPass | Same kill primitive family; different driver |
| Sideload host | `vsdbg.exe` listed in `cruciferra_sideloaded_apps.csv` | `PS-RAP-003` | Catalog overlap with Rapuncel delivery host binary |
| Reference CcProtect | `5f0cfe83…` (LOLDrivers; PE ts 2022-03-04) | `PS-RAP-004` | Baseline for Alinubx identity-swap |

**Rule:** shared Cruciferra/BYOVD tooling ≠ same actor. Do not merge ErrTraffic domains (`karmactive.com`, Remus C2s) into Rapuncel IOCs.

## RAP-H-CRY status

Open. Treat loader/EDR-kill sophistication as **likely crypter-supplied** unless proven otherwise; treat GitHub/SEO kit and stealer collection artifacts as **campaign/ecosystem** layers pending further evidence.
