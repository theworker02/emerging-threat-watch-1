# Takedown Evidence Package (TEMPLATE)

**This file is tracked.** Filled packages for external abuse desks should live under `reports/law-enforcement/private/` (gitignored) or an investigator-controlled store — do not commit live PCAPs, binaries, or unredacted chat exports.

| Artifact | Path | Git |
|----------|------|-----|
| This template | `reports/law-enforcement/TAKEDOWN_EVIDENCE_PACKAGE.TEMPLATE.md` | tracked |
| Methodology | `shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md` | tracked |
| Metadata schema | `shared/schemas/takedown-evidence.schema.json` | tracked |
| FBI/IC3 narrative packages | `reports/law-enforcement/packages/0N-<family>/` | tracked drafts |
| Filled takedown package (local) | `reports/law-enforcement/private/takedown-<family>-<date>.md` | **gitignored** |

**Hard rules:** One family per package. No invented IOCs. No malware binaries in web forms. Autonomous agents do not execute malware. Never authenticate to attacker C2 panels. Human review before submit.

**Audience note:** This template is for **hosting / registrar / chat-platform abuse**. For FBI/IC3 narrative filing, use [`HOW_TO_FILE.md`](HOW_TO_FILE.md) and `packages/0N-<family>/`. Both audiences need technical telemetry; packaging differs.

---

## 0. Cover

| Field | Value |
|-------|-------|
| Family / case code | e.g. `ETW-SET-IC3` / Settra |
| Package ID | `ETW-<FAM>-TD-<YYYYMMDD>` |
| Target type | C2/Hosting · Registrar/DNS · Discord/Telegram · (other) |
| Prepared by | |
| Prepared date (UTC) | |
| Research cutoff | |
| Intended recipient | hosting abuse / registrar / Discord T&S / Telegram / ISAC / other |
| Related IC3 number (if any) | |
| Provenance summary | PRIMARY-SOURCE / OBSERVED_PASSIVE / human-lab OBSERVED (list) |

---

## 1. Safety & OpSec attestation

- [ ] No malware was executed by an autonomous agent for this package  
- [ ] Any sandbox run was human isolated lab **or** licensed platform; runner/license noted below  
- [ ] No authentication to attacker C2 / panel / seller shop  
- [ ] No Discord/Telegram tokens or sessions were stolen or reused  
- [ ] All indicators exist in case ledgers or cited PRIMARY sources (no invention)  
- [ ] CDN / shared-host edges labeled `ASSOCIATION_ONLY` where applicable  

Sandbox / lab note (if any):

```
Platform: (ANY.RUN | Triage | Hybrid Analysis | CAPEv2 | other)
Operator:
Date UTC:
Task / report URL or local evidence path:
Sample SHA-256:
```

---

## 2. Target type A — C2 / Hosting

Use when requesting hosting-provider or ASN abuse action.

### Required checklist

- [ ] **IP address** (from `intelligence/infrastructure-ip-ledger.csv` or PRIMARY IOC)  
- [ ] **Port**  
- [ ] **Timed PCAP** (human lab / licensed sandbox export) — path or retention note  
- [ ] **Extracted C2 config** (if obtained lawfully from memory/config) — or “not available”  
- [ ] **Sample SHA-256** linking traffic to malware  

### Fill

| Field | Value | Provenance | Evidence path / URL |
|-------|-------|------------|---------------------|
| IP | | | |
| Port | | | |
| First/last traffic time (UTC) | | | |
| PCAP filename / hash | | | |
| C2 config excerpt (redact secrets if sharing broadly) | | | |
| Sample SHA-256 | | | |
| TLS cert fingerprint / subject | | | |
| JARM / HTTP headers snapshot | | | |
| RDAP / ASN / abuse contact | | | |
| Role in ledger (`c2`, `meshagent`, `exfil`, …) | | | |
| Relationship type (`PRIMARY-SOURCE`, `ASSOCIATION_ONLY`, …) | | | |

### Hosting abuse narrative (short)

```
We are reporting suspected malicious command-and-control / staging hosting at <IP>:<port>.
Traffic was observed in a lawful isolated sandbox / licensed analysis platform at <UTC>.
Associated sample SHA-256: <hash>.
We have not authenticated to any administrative panel on this host.
PCAP and technical annex available to the abuse team on request.
```

---

## 3. Target type B — Registrar / DNS

Use when requesting domain suspension or registrar investigation.

### Required checklist

- [ ] **Domain**  
- [ ] **Active resolution** (A/AAAA/NS as of date)  
- [ ] **pDNS history** (summary + source)  
- [ ] **Sample hash showing check-in** to this domain (sandbox or PRIMARY network table cited)  

### Fill

| Field | Value | Provenance | Evidence path / URL |
|-------|-------|------------|---------------------|
| Domain | | | |
| Active A/AAAA (UTC stamped) | | | |
| NS / registrar (RDAP) | | | |
| pDNS first/last seen | | | |
| CT / certificate notes | | | |
| Sample SHA-256 (check-in) | | | |
| Related URL paths (do not live-probe if interactive) | | | |

### Registrar abuse narrative (short)

```
We are reporting domain <domain> resolving to <IP> as of <UTC>, used as malware C2 / staging
per <PRIMARY source or sandbox report>. Sample SHA-256: <hash>. Passive DNS history attached.
We request review under your acceptable-use / malware policy.
```

---

## 4. Target type C — Discord / Telegram (chat platform)

Use for Trust & Safety / platform abuse — not a substitute for IC3 when criminal activity is alleged.

### Required checklist

- [ ] **Message or channel links**  
- [ ] **Server ID / Channel ID / User ID** (as applicable)  
- [ ] **Timestamped logs** (export or archival copy)  
- [ ] Screenshots attached only as **supplementary**  

### Fill

| Field | Value | Provenance | Evidence path / URL |
|-------|-------|------------|---------------------|
| Platform | Discord / Telegram / other | | |
| Invite or channel URL | | | |
| Server / chat ID | | | |
| Channel ID | | | |
| User ID(s) | | | |
| Message ID(s) / time range (UTC) | | | |
| Log export path | | | |
| Related malware hash / C2 (if any) | | | |

**Do not** include session tokens, cookies, or credentials.

---

## 5. Collaboration / sharing log

| Destination | Date UTC | Submission ID | What was shared | Notes |
|-------------|----------|---------------|-----------------|-------|
| abuse.ch ThreatFox / URLhaus / MB | | | | Auth-Key used: Y/N |
| ISAC | | | | |
| STIX 2.1 / TAXII partner | | | | |
| Hosting / registrar ticket | | | | |
| Discord / Telegram T&S | | | | |

---

## 6. Cross-links (repo)

| Need | Path |
|------|------|
| Methodology | `shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md` |
| Autonomy / prohibit list | `shared/methodology/AUTONOMOUS_COLLECTION_POLICY.md` |
| Staging / bounded Shodan | `shared/methodology/UNCONVENTIONAL_STAGING_OSINT.md` |
| Underground / tracker OSINT | `shared/methodology/UNDERGROUND_AND_COMMODITY_RAT_OSINT.md` |
| IC3 / FBI how-to | `reports/law-enforcement/HOW_TO_FILE.md` |
| Narrative dossier template | `reports/law-enforcement/SUBMISSION_REPORT.TEMPLATE.md` |
| Family indicators | `investigations/<family>/evidence/published-indicators.csv` |
| IP ledger | `intelligence/infrastructure-ip-ledger.csv` |
| Enforcement readiness | `docs/ENFORCEMENT_READINESS.md` |

---

## 7. Human approval

| Role | Name | Date | Approved to send? |
|------|------|------|-------------------|
| Analyst | | | |
| Reviewer | | | |

**Never auto-submit.**
