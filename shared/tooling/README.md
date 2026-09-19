# Shared Tooling

Passive utilities only. **Never** automatically contact suspected C2, authenticate to attacker infrastructure, or download/execute live malware.

| Script | Purpose |
|--------|---------|
| `normalize_iocs.py` | Normalize and dedupe IOC CSVs within a single case |
| `validate_iocs.py` | Schema/field validation |
| `generate_tables.py` | Build markdown tables from CSV |
| `build_timeline.py` | Merge case timeline events |
| `verify_hashes.py` | Format/validate hash strings (no sample acquisition) |
| `generate_report_data.py` | Assemble report data blobs |
| `check_case_isolation.py` | Fail if IOCs appear in multiple cases without XT-REL evidence |
| `build_cti_evidence_repository.py` | Build LE STIX/CSV evidentiary tree |
| `rebuild_stix_bundles.py` | Regenerate family STIX 2.1 with `stix2` library |
| `extract_ips_from_text.py` | Extract public IPv4 from sandbox/memory text exports → `ips.csv` |
| `freeze_primary_sources.py` | Fetch+hash primary research HTML |
| `passive_collect.py` | Bounded CT/RDAP passive collection |
| `build_le_packages.py` | Rebuild FBI/IC3 narrative packages |

All automated observations must record UTC timestamps and provenance.

**Lab only (human):** malware detonation / memory dump — see `shared/methodology/C2_IP_DISCOVERY.md`. Do not wire detonation into autonomous collectors.
