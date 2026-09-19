# Passive Infrastructure Collection Instructions

1. Prefer `crt.sh`, RDAP, public VT/urlscan **metadata** views. Do not authenticate to attacker systems.
2. Record `retrieved_at` UTC for every query response archived.
3. Store CT rows only after real output is saved — never fabricate certificate IDs. Use `ct_results_template.csv` / `pdns_results_template.csv` schemas.
4. Labels: RESOLVING / NXDOMAIN / REACHABLE / SERVING CONTENT / CONFIRMED MALICIOUS are not interchangeable.
5. CDN (Cloudflare AS13335) and Azure Websites (AS8075) edge IPs are **low specificity** — prefer FQDN + behavioral path indicators. See `vendor_reported_dns_asn.csv` for vendor-stated ASN context (UNVERIFIED until ETW pDNS).
6. Seeds: `infrastructure_collection_seeds.csv`, `certificate_transparency_seeds.csv`, `github_repository_evidence.csv`, `wayback_github_pivots.md`, `tracker_collection_seeds.csv` (ThreatFox / MalwareBazaar / URLhaus / Triage / InQuest / Any.Run), `unconventional_staging_seeds.csv` (npm/paste/buckets/APK/bounded Shodan).
7. Provenance: article retrieval ≠ `OBSERVED`. Promote to `OBSERVED` only after passive validation with method + timestamp.
8. Underground / dark-web: monitor/cite only — see `shared/methodology/UNDERGROUND_AND_COMMODITY_RAT_OSINT.md`. Prefer tracker configs over forum screenshots. Do not join private E2EE rooms; no corp/personal IP for underground browsing.
9. Unconventional staging: see `shared/methodology/UNCONVENTIONAL_STAGING_OSINT.md`. Permit bounded Shodan/Censys/paste/npm/bucket **metadata**; prohibit panel login, malware exec, mass scanning. Staging object URL metadata = `OBSERVED_PASSIVE`; do not download/execute payloads without isolated-lab note.
