# Chain of Custody Notes

**Package root:** `reports/law-enforcement/CTI-Evidence-Repository/`  
**Built:** 2026-09-19T19:25:39Z  
**Builder:** `shared/tooling/build_cti_evidence_repository.py`

## What is attested

1. CSV/STIX/SUMMARY text artifacts listed in `CHECKSUMS.sha256` (SHA-256 of file bytes at build time).
2. Provenance columns on IOC CSVs (PRIMARY-SOURCE / OBSERVED_PASSIVE).
3. Empty `network_captures/` and `memory_dumps/` — **no** binary evidence claimed until files are added and checksums regenerated.

## What is not attested

- Live malware execution by ETW autonomous collectors
- Authentication to attacker C2 panels
- Cryptocurrency wallet ownership
- Personal author/home IP attribution

## Adding lab evidence

1. Drop `.pcapng` / dumps into the family folders.
2. Re-run `build_cti_evidence_repository.py` **or** append hashes manually to `CHECKSUMS.sha256`.
3. Optionally GPG-sign: `gpg --clearsign CHECKSUMS.sha256` → `CHECKSUMS.asc` (keep private/gitignored if desired).
