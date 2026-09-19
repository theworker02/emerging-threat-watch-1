# Driver Trust-Chain Case Study — Alinubx.sys

**Evidence:** SOURCE-RAP-001 (LastPass TIME / Delphos) · Claims RAP-CLAIM-0015–0018, 0026–0027  
**Cutoff:** 2026-09-19

## Vocabulary (do not interchange)

| Term | Meaning in this case study |
|------|----------------------------|
| **Signed** | Authenticode signature present |
| **Trusted** | OS policy allows load based on signature/trust store |
| **Attested** | Passed Microsoft Windows Hardware Compatibility Publisher pipeline |
| **Vulnerable** | Exposes abuseable primitives (e.g., kill IOCTL); may be LOLDrivers-listed |
| **Malicious** | Used with hostile intent in a campaign |
| **Abused** | Legitimate/vulnerable component used off-purpose by an attacker |
| **Blocklisted** | Present on Microsoft vulnerable-driver hash blocklist (or equivalent) |

Microsoft attestation proves a driver passed a **trust pipeline**. It does **not** prove the driver is safe.

## Observed facts (PRIMARY)

- Deployed as `C:\Windows\System32\drivers\nvfsflt64.sys`, service `NvFsFilter` (NVIDIA-style disguise).
- Device interface `\\.\Alinubx`; IOCTL `0x222024`; `ObOpenObjectByPointer(..., KernelMode)` + `ZwTerminateProcess`.
- Hardcoded **145** AV/EDR process names (matches Cruciferra PUROSANGUE default count).
- WHCP-chain signature; signing timestamp **March 2023**.
- VirusTotal **0/72** as of 2026-08-20 (last analysis date reported as 2025-07-21); not on MS blocklist at publication.
- Identity-swapped **CcProtect.sys** (CnCrypt 1.32, Henan Dafeng): same product/version/submitter/kill primitive; `OriginalFilename` changed CcProtect → Alinubx.
- Delphos: 18 public BYOVD drivers + CcProtect + Alinubx vs `DriverPolicy_Enforced.xml` (2026-08-20) → **0/20** SHA-256 matches.
- Broader rootkit/WFP features present in code but **inactive** without `Alinubx.ccf`.
- MSRC (2026-08-19): not a Microsoft-owned vulnerability; WDSI blocklist channel; still not blocklisted at publication.

## Analytical thesis

**Identity-based driver blocking vs behavior/provenance-based detection.**

A filename/hash swap defeated hash blocklists and VT reputation while preserving the abuseable process-kill interface. Durable hunts: CnCrypt/Henan Dafeng identity, `NvFsFilter`/`nvfsflt64.sys`, `\\.\Alinubx`, vsdbg sideload chain — not only the string `Alinubx.sys`.

## Related Cruciferra note

eSentire’s PUROSANGUE analysis used **DCRCVDrv.sys**; this campaign used **Alinubx**. Same crypter *class*, different driver *choice* — supports separating crypter commodity features from campaign-specific operator decisions (RAP-H-CRY).
