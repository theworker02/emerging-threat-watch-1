# Gated Autonomy

**Status:** Binding  
**Effective:** 2026-09-19  

Emerging Threat Watch collectors run **autonomously by default**, with **security gates** only for high-risk actions. You approve gates; you do not approve every CT/pDNS query.

---

## Tiers

| Tier | Name | Approval | Examples |
|------|------|----------|----------|
| **0** | Passive / metadata | **None** — fully autonomous | CT, pDNS, RDAP, urlscan, public sandbox *report* metadata, npm/paste metadata, IOC normalize, STIX rebuild, LE package rebuild, IP extract from *already exported* text |
| **1** | High-risk lab / egress | **Required** — stage job → you approve → runner executes | Malware detonation (CAPEv2/ANY.RUN/Triage upload), live sample download from MalwareBazaar, memory dump of running implant, unauthenticated mass scan beyond ledger IPs, abuse.ch IOC *submission*, gowitness against new IP fleets |
| **2** | Hard prohibited | **Never approved** | C2 panel login, send malware commands, exploit, brute-force, buy crimeware, token theft, ransomware negotiation |

Tier 0 matches [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md) permitted list.  
Tier 2 matches that policy’s prohibited list (cannot be gated into existence).

---

## How gates work

```
Agent autonomously prepares work
        │
        ▼
 Tier 0? ──yes──► run immediately, write OBSERVED_PASSIVE / artifacts
        │
        no (Tier 1)
        ▼
 gate_ctl.py submit  →  gates/queue/<id>.json  (status=pending)
        │
        ▼
 You review: gate_ctl.py list
        │
        ├─ approve → gates/approved/<id>.json
        │                 │
        │                 ▼
        │          gate_ctl.py run <id>   (or agent continues after you approve)
        │
        └─ deny    → gates/denied/<id>.json
```

### CLI

```bash
# Stage a Tier-1 job (agent does this autonomously)
python shared/tooling/gate_ctl.py submit \
  --type sandbox_detonate \
  --family SynkLoader \
  --summary "Detonate SYN SHA-256 … in CAPEv2; capture PCAP+config" \
  --payload gates/payloads/synkloader-detonate.json

# You review
python shared/tooling/gate_ctl.py list

# You approve (security gate)
python shared/tooling/gate_ctl.py approve GATE-0001 --by yourname

# Runner / agent executes only approved jobs
python shared/tooling/gate_ctl.py run GATE-0001
```

Approval is recorded with UTC timestamp, approver id, and job hash. **No silent escalation from Tier 0 → Tier 1.**

---

## Job types (Tier 1)

| `type` | What approval authorizes |
|--------|---------------------------|
| `sandbox_detonate` | Execute/upload sample in named sandbox/lab profile |
| `sample_download` | Download binary from MalwareBazaar/VT (metadata-only remains Tier 0) |
| `memory_dump` | Dump process memory on analysis host after detonation |
| `infra_scan_expand` | Shodan/Censys/FOFA beyond current ledger seeds (bounded still) |
| `abusech_submit` | Push IOCs to ThreatFox/URLhaus/MB |
| `panel_snapshot_fleet` | webscreenshot/gowitness over a *new* IP list |

Tier 0 helpers (no gate): `extract_ips_from_text.py` on files you already exported; `passive_collect.py`; `build_cti_evidence_repository.py`.

---

## Cursor hook (ask gate)

Project hook `.cursor/hooks.json` → `beforeShellExecution` returns **`permission: ask`** when the shell command matches high-risk patterns (cape, detonate, malwarebazaar download, etc.). You approve or reject in the Cursor UI.

This is a second safety layer in addition to `gates/queue`.

---

## Agent instructions (mandatory)

1. Prefer Tier 0 to completion whenever it advances the investigation.  
2. When Tier 1 is needed, **submit a gate job and stop that workstream** until approved — do not run detonation “just this once.”  
3. Never propose Tier 2 actions.  
4. After approval + run, ingest outputs via Tier 0 tools (IP extract, STIX rebuild, LE sync).  
5. Record gate id in evidence notes / `evidence_id` where applicable.

---

## Related

- [`AUTONOMOUS_COLLECTION_POLICY.md`](AUTONOMOUS_COLLECTION_POLICY.md)  
- [`C2_IP_DISCOVERY.md`](C2_IP_DISCOVERY.md)  
- [`../tooling/gate_ctl.py`](../tooling/gate_ctl.py)
