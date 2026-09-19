# C2 IP Discovery (Lawful / Non-Attack)

**Status:** Defensive methodology  
**Effective:** 2026-09-19  
**Audience:** Human analysts (isolated lab) + autonomous agents processing **exported** sandbox/text artifacts  
**Binding:** [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md)

---

## Goal

Obtain **campaign C2 / check-in IP addresses** for evidence repositories and takedown packages **without** launching attacks, authenticating to panels, or sending commands to malware.

**Author / home IP of a person = NOT ESTABLISHED** from C2 infra alone.

---

## 1. Dynamic sandbox analysis & memory extraction (gated Tier 1)

**Who executes:** Human / licensed lab runner **after** you approve a gate.  
**Who stages:** Autonomous agent may prepare the job and stop.  
**Who not:** Collectors must not detonate without an approved `GATE-####` ([`GATED_AUTONOMY.md`](GATED_AUTONOMY.md)).

### Autonomy + gate flow

```text
Agent (Tier 0) exhausts CT / pDNS / public sandbox *reports*
        │
        ▼
Still need PCAP / decrypted config IP?
        │
        ▼
python shared/tooling/gate_ctl.py submit \
  --type sandbox_detonate --family <Family> \
  --summary "…" --payload gates/payloads/<id>.json
        │
        ▼
YOU: gate_ctl.py list → approve GATE-####
        │
        ▼
gate_ctl.py run GATE-####   → lab contract / receipt
        │
        ▼
Ingest PCAP/strings (Tier 0): extract_ips_from_text.py → ledger → STIX
```

### A. Automated C2 config extractors

| Platform | Use |
|----------|-----|
| Hatching Triage | Unpack + decrypted config / network IOCs |
| ANY.RUN | Interactive + export PCAP / process tree |
| CAPEv2 / Cuckoo | Self-hosted detonation + config modules |

**Family notes (ETW):**

| Family | Lab tip |
|--------|---------|
| **NodeRabbit** | Detonate lure `.zip` / Node implant in isolated VM with outbound logging; record HTTPS/WebSocket to Azure/Cloudflare hostnames **and** any direct IP if CDN bypass appears |
| **PollCat** | Same; capture `POST /beacon`, `/gate/*`, `/vault/*` destinations |
| **SynkLoader** | Prefer Expel SHA-256 modules already in ledger; sandbox to confirm C2 domain→IP |
| **Showboat** | Linux sample detonation; capture `SERVER_ADDRESS` / port 443 clusters |
| **Matanbuchus / AstarionRAT** (candidates) | Wait for memory injection; dump host process — decrypted `IP:Port` often in cleartext strings |

**Retain:** timed PCAP, TLS certs, extracted config JSON, video/screenshots, UTC timestamps → drop under `CTI-Evidence-Repository/families/<Family>/network_captures/` and `memory_dumps/`, then regenerate checksums.

### B. Memory dumping

After injection completes: **Volatility 3** or **System Informer / Process Hacker** → dump process → `strings` / YARA → extract IPv4/IPv6 and hostnames.

Feed dumps through `shared/tooling/extract_ips_from_text.py` (below).

---

## 2. Infrastructure footprinting (bounded internet scanning)

Query **Shodan / Censys / FOFA / ZoomEye** only against:

1. IPs already in `intelligence/infrastructure-ip-ledger.csv`, or  
2. JARM / cert / title fingerprints derived from **known** family samples/configs  

**Do not** mass-scan arbitrary internet ranges from ETW automation.

### Useful pivots

- **JARM** fingerprints of known Remcos/AsyncRAT/Matanbuchus-class listeners (candidate comparators)  
- **HTTP titles / headers** of admin panels (unauthenticated GET only)  
- **TLS subject CN** patterns (example illustration only — do not invent CNs for ETW families):

```text
services.tls.certificates.leaf_data.subject.common_name: "…"
OR services.jarm.fingerprint: "…"
```

Unauthenticated panel snapshots on **ledger** IPs are Tier 0; **new fleets** need `panel_snapshot_fleet` approval. **Panel login is Tier 2 / prohibited**.

See [`UNCONVENTIONAL_STAGING_OSINT.md`](UNCONVENTIONAL_STAGING_OSINT.md) and [`GATED_AUTONOMY.md`](GATED_AUTONOMY.md).

---

## 3. Passive DNS & historical mapping (CDN/Azure bypass)

Mirage Kitten–style ops (NodeRabbit / PollCat) often front with **Cloudflare / Azure**. True origin (if any) may appear only in **historical** A/AAAA before CDN enablement.

| Platform | Role |
|----------|------|
| VirusTotal Intelligence | Historical resolutions + communicating files |
| SecurityTrails | pDNS history |
| PassiveTotal (RiskIQ) | Historical DNS / hosting |
| Shodan historical DNS | Supplemental |

**Method:** Start from PRIMARY domains in published-indicators → pull history → label new IPs `OBSERVED_PASSIVE` with first/last seen → demote current CF/Azure edges as `ASSOCIATION_ONLY`.

---

## 4. Bulk API extraction (public CTI feeds)

| Platform | Method | Output |
|----------|--------|--------|
| ThreatFox | REST by `malware_alias` / tag | Live C2 IP:Port |
| URLhaus | Bulk CSV / API | Distribution URLs / staging |
| MalwareBazaar | API (Auth-Key) | Sample metadata → lab detonation queue |
| InQuest Labs | Deep file inspection API | Embedded network IOCs |

ETW seeds: `shared/queries/tracker_collection_seeds.csv`.  
Current blocker: abuse.ch **Auth-Key** (401) / captcha on browse — see tracker disposition ledgers under `evidence/passive-observations/trackers/`.

---

## 5. Automated IP extraction into evidence CSVs

Use:

```bash
python shared/tooling/extract_ips_from_text.py \
  --input path/to/memory_dump.str \
  --family PollCat \
  --output reports/law-enforcement/CTI-Evidence-Repository/families/PollCat/iocs/ips.csv \
  --append \
  --provenance LAB_SANDBOX \
  --source-ref "CAPEv2 run 2026-09-19 analyst=…"
```

Writes ETW-standard headers (`indicator_type,value,first_seen_utc,last_seen_utc,confidence,provenance,evidence_id,notes`). Filters loopback/private/link-local. Does **not** execute malware.

Then rebuild STIX/checksums:

```bash
python shared/tooling/build_cti_evidence_repository.py
```

---

## Provenance ladder (reminder)

| Observation | Label |
|-------------|-------|
| Sandbox/lab extracted C2 IP | `OBSERVED_PASSIVE` or `LAB_SANDBOX` (document mechanism) |
| Vendor published IP | `PRIMARY-SOURCE` |
| Same CDN edge as campaign domain | `ASSOCIATION_ONLY` |
| Same IP as known C2 domain | `INFRASTRUCTURE_OVERLAP` |
| “This is the malware author’s home IP” | **NOT ESTABLISHED** |

---

## Related

- [`TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`](TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md)  
- [`docs/ENFORCEMENT_READINESS.md`](../../docs/ENFORCEMENT_READINESS.md)  
- [`reports/law-enforcement/CTI-Evidence-Repository/`](../../reports/law-enforcement/CTI-Evidence-Repository/)
