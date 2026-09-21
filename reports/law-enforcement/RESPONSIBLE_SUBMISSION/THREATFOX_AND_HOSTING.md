# ThreatFox / URLhaus submission guidance (paste-ready)

Status: NOT SUBMITTED — no abuse.ch Auth-Key in this environment.

When Auth-Key is available:
1. Login / key at https://auth.abuse.ch/
2. Prefer web UI https://threatfox.abuse.ch/share/ or API https://threatfox.abuse.ch/api/
3. Submit only PRIMARY-SOURCE malware IOCs already in packages/*/03_INDICATORS.csv
4. Set reference=PRIMARY article URL; confidence_level <= 50 unless you observed the IOC
5. One family per batch; comment includes ETW package ID
6. Do not invent IOCs; do not submit phishing-only rows to ThreatFox

Hosting abuse: BLOCKED without timed PCAP + SHA-256 + non-CDN IP:port.

See also [`VENDOR_CONTACTS.md`](VENDOR_CONTACTS.md) and [`../TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md`](../TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md).
