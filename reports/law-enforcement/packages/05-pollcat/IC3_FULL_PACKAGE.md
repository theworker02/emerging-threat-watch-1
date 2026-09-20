# IC3 / FBI Full Complaint Package — PollCat

**Package ID:** `ETW-POL-IC3`  
**Family:** PollCat only (case-isolated)  
**Status:** DRAFT — human review required · do not auto-submit  
**Research cutoff:** 2026-09-19  
**Corpus retrieval:** 2026-09-19T18:07:48Z  
**Portal:** https://www.ic3.gov/

---

## 1. Filing identity

| Field | Value |
|-------|-------|
| Reporter purpose | Defensive threat-intelligence referral (not personal victimization claim) |
| Crime-type language | Malware; Spear-phishing / social engineering (recruitment / coding-challenge lure) |
| Suggested subject | Defensive TI referral — PollCat (Kaspersky Securelist 2026-09-01) — `ETW-POL-IC3` |
| Dollar loss claimed | None |
| Personal victimization claimed | No |
| Malware binaries attached | No (retained offline; available through normal channels on request) |
| ETW live C2 contact | None — policy forbids |
| Independently observed campaign ownership by ETW | None |

### Related prior IC3 Submission IDs (separate complaints — no shared-operator claim)

| Family | Package | Submission ID |
|--------|---------|---------------|
| Rapuncel | `ETW-RAP-IC3` | `208b747c6f7445f0af2b69a9d63acc36` |
| Settra | `ETW-SET-IC3` | `631d8b4800d04bc19cdbfc6662e5c52c` |
| RatHat | `ETW-RAT-IC3` | `f92c4c2f0dd3481f898fdd125e728adf` |
| NodeRabbit | `ETW-NRB-IC3` | `dded86972e9347e0be27a6597b4cf08a` |
| **PollCat (this filing)** | `ETW-POL-IC3` | *not yet filed* |

---

## 2. Complaint narrative (paste into IC3 description)

I am reporting defensive threat-intelligence information concerning the PollCat malware documented by Kaspersky GReAT on September 1, 2026 in the Securelist article “Mirage Kitten targeting aviation and FinTech sectors across the Middle East and Africa with a new malware set” (https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/). The same article also covers NodeRabbit; I am filing PollCat as a **separate** complaint (package `ETW-POL-IC3`). NodeRabbit was previously filed under IC3 Submission ID `dded86972e9347e0be27a6597b4cf08a`. Co-disclosure and shared recruiter/coding-challenge delivery are COMMON TECHNIQUE only — not proof of shared implant authorship.

Kaspersky describes PollCat as a previously undocumented cross-platform remote access trojan written in obfuscated JavaScript, delivered through trojanized coding-challenge archives. The analyzed sample resides inside RankChallenge-react (archive `RankChallenge-react-6uJSX3-main.zip`, MD5 `795e053a990a1569ffdcb57f48f6d085`). The package is labeled `ctf-server`. Execution starts with `npm i && node index.js`. The load chain is `app.js` → `requireAuth.js` → `requireObjects.js`, which begins C2 registration/polling **before** the user enters an OTP. Failed OTP does not stop PollCat. Successful OTP issues a JWT and a second worker; the first JWT-bearing request triggers persistence.

Kaspersky reports registration C2 hosts: `sahi-finance.com`, `gamebarappinformation.azurewebsites.net`, and `gamebarapp.azurewebsites.net`. OTP codes are validated at `https://lifespotify.com/api/users/b879746e-fed9-4211-a6da-4d8223681267/otp/validate` (Kaspersky: domain registered late June 2026 for this campaign use). Persistence markers include Windows `%APPDATA%\Microsoft\Network` with `package.json` + `requireObject.js` and daily scheduled task `NetSync_<username>` at 09:00; Linux/macOS `~/.node_packages` with daily 09:00 cron and `@reboot`; and macOS LaunchAgent `~/Library/LaunchAgents/com.harsh.requireobject.plist`.

Kaspersky documents PollCat C2 registration via `POST /beacon` (JSON `clientId,type=poll,pcName,userName`) treating **HTTP 400** with body `{socketId, pollInterval, jitterTime}` as success; subsequent operations use `/gate/hello`, `/gate/fetch`, `/gate/submit`, `/vault/*`, `/gate/track`, and inventory exfil `POST /api/system-details/result`. Host identity format is `129--<hostname>`. Default poll interval 120000 ms with jitter ≤5000 ms. Kaspersky states PollCat’s structure is substantially different from NodeRabbit and documents structural C2 handshake / command-ID / beacon-timing overlap with Retrograde/MiniFast rather than NodeRabbit. Mirage Kitten attribution is **Kaspersky’s assessment**, not an independently established Emerging Threat Watch conclusion.

I have retained the original public research and a 15-row PRIMARY-SOURCE indicator table (`POL-IND-0001`–`0015`) under package `ETW-POL-IC3`. Full indicator CSV and source archives are available to investigators on request. I have not executed malware samples and have not contacted suspected command-and-control systems. No personal dollar loss is claimed in this package.

Research cutoff: 2026-09-19. Repository: https://github.com/theworker02/emerging-threat-watch-1 · Path: `reports/law-enforcement/packages/05-pollcat/`.

---

## 3. Technical indicator appendix (all collected POL-IND rows)

**Provenance rule:** All rows below are **PRIMARY-SOURCE** (Kaspersky Securelist) unless noted. They are **not** independently re-validated live observations by ETW unless labeled OBSERVED_PASSIVE. Do not invent additional hashes or IPs.

### 3.1 File hashes

| ID | Type | Value | Artifact | Notes |
|----|------|-------|----------|-------|
| POL-IND-0001 | **MD5** | `795e053a990a1569ffdcb57f48f6d085` | `RankChallenge-react-6uJSX3-main.zip` | PollCat lure archive. Was briefly mis-tagged as NodeRabbit `NRB-IND-0011`; authoritative case is PollCat. **SHA-256: unresolved / OPEN** (MalwareBazaar 401; OpenTIP no SHA-256 as of 2026-09-19). |

**SHA-256:** none in corpus.  
**SHA-1:** none in corpus.  
**IPv4 / IPv6 actor-owned C2 addresses:** none in corpus (0 IP rows).

### 3.2 Domains / hostnames

| ID | Value | Role | Notes |
|----|-------|------|-------|
| POL-IND-0002 | `sahi-finance.com` | Registration C2 #1 | NOT OBSERVED ownership by ETW. RDAP 200; CT intermittently failed (OBSERVED_PASSIVE metadata only). |
| POL-IND-0003 | `gamebarappinformation.azurewebsites.net` | Registration C2 #2 | Azure Web App — shared-edge ASSOCIATION_ONLY for ownership. CT count=0. |
| POL-IND-0004 | `gamebarapp.azurewebsites.net` | Registration C2 #3 | Azure Web App — ASSOCIATION_ONLY. |
| POL-IND-0005 | `lifespotify.com` | OTP validation host | Kaspersky: late-June-2026 registration for campaign use. ETW OBSERVED_PASSIVE: CT cert_count=47; RDAP 200; Wayback shows older captures (domain-reuse possible). CT ≠ ownership. |

### 3.3 URLs

| ID | Value | Role | Notes |
|----|-------|------|-------|
| POL-IND-0006 | `https://lifespotify.com/api/users/b879746e-fed9-4211-a6da-4d8223681267/otp/validate` | OTP validate API | **Do not probe live.** UUID path segment as published by Kaspersky. |

### 3.4 Filenames / paths / persistence markers

| ID | Value | Platform | Role |
|----|-------|----------|------|
| POL-IND-0007 | `requireObjects.js` | Cross-platform | Malicious component started via `requireAuth.js` |
| POL-IND-0008 | `requireObject.js` | Windows | Persistence worker under `%APPDATA%\Microsoft\Network` (with `package.json`; `npm install`) |
| POL-IND-0009 | `com.harsh.requireobject.plist` | macOS | LaunchAgent: `~/Library/LaunchAgents/com.harsh.requireobject.plist` (RunAtLoad + daily 09:00) |
| POL-IND-0010 | `NetSync_` (prefix) | Windows | Scheduled task `NetSync_<username>` daily 09:00 |
| POL-IND-0011 | `~/.node_packages` | Linux / macOS | Persistence directory; `npm i`; daily 09:00 cron and `@reboot` |

### 3.5 HTTP / C2 protocol markers

| ID | Value | Role |
|----|-------|------|
| POL-IND-0012 | `POST /beacon` | Registration; expects HTTP **400** + `{socketId, pollInterval, jitterTime}` |
| POL-IND-0013 | `GET /gate/fetch` | Command poll with `token=socketId` |
| POL-IND-0014 | `POST /gate/hello` | Host registration after socketId |
| POL-IND-0015 | `POST /api/system-details/result` | SYSTEM_CHECK inventory exfil |

**Additional protocol details (PRIMARY-SOURCE; not separate IND rows):**

| Item | Value |
|------|-------|
| Register body fields | `clientId`, `type=poll`, `pcName`, `userName` |
| Additional ops paths | `POST /gate/submit`, `GET /vault/<uuid>`, `PUT /vault/push/`, `POST /gate/track` |
| Host ID format | `129--<hostname>` |
| Default poll | 120000 ms |
| Jitter | ≤ 5000 ms |
| Declared commands | 22 |
| Notable opcodes | `0x20 EVAL_JS`; `0x30 SYSTEM_CHECK` (24 security-vendor folder strings); `0x0B RUNDLL` |
| Unimplemented (per Kaspersky) | `0xA1 WS_DOWNLOAD`; `0xB0 REQUEST_ELEVATION`; `0xB1 PERSIST` |

### 3.6 Delivery / lure details (PRIMARY-SOURCE)

| Item | Value |
|------|-------|
| Lure project | `RankChallenge-react` (React code-fixing challenge / time-limited developer assessment) |
| Start command | `npm i && node index.js` |
| Package label | `ctf-server` |
| UI markers | Prints `CTF server running`; frontend `ctf-*` storage keys; tutorial `path/to/ctf` (Kaspersky notes AI/template smell) |
| Execution chain | `app.js` → `requireAuth.js` → `requireObjects.js` (C2 starts **before** OTP) |
| OTP behavior | Failed OTP does not stop PollCat; successful OTP → JWT + second worker; first JWT-bearing request triggers persistence |

### 3.7 Copy-paste IOC block (compact)

```
=== HASHES ===
MD5  795e053a990a1569ffdcb57f48f6d085  RankChallenge-react-6uJSX3-main.zip  (SHA-256 UNKNOWN)

=== DOMAINS ===
sahi-finance.com
gamebarappinformation.azurewebsites.net
gamebarapp.azurewebsites.net
lifespotify.com

=== URL ===
https://lifespotify.com/api/users/b879746e-fed9-4211-a6da-4d8223681267/otp/validate

=== HOST ARTIFACTS ===
requireObjects.js
requireObject.js
%APPDATA%\Microsoft\Network\requireObject.js
NetSync_<username>  (daily 09:00)
~/Library/LaunchAgents/com.harsh.requireobject.plist
~/.node_packages

=== C2 PATHS ===
POST /beacon
POST /gate/hello
GET  /gate/fetch?token=
POST /gate/submit
GET  /vault/<uuid>
PUT  /vault/push/
POST /gate/track
POST /api/system-details/result

=== IDENTITY / TIMING ===
Host ID: 129--<hostname>
Poll: 120s  Jitter: <=5s
```

---

## 4. Timeline

| ID | Timestamp (UTC) | Event |
|----|-----------------|-------|
| — | ~late June 2026 | Kaspersky: `lifespotify.com` registered for campaign OTP use |
| POL-TL-0001 | 2026-09-01 | Kaspersky Securelist discloses PollCat (co-disclosed with NodeRabbit) |
| POL-TL-0002 | 2026-09-19 | ETW Phase 1 PollCat package / POL-IND transcription |

---

## 5. Key claims retained (PRIMARY-SOURCE summary)

| Claim ID | Summary |
|----------|---------|
| POL-CLAIM-0001 | Discovered during same Mirage Kitten investigation as NodeRabbit; previously undocumented family |
| POL-CLAIM-0002 | Cross-platform obfuscated JavaScript RAT |
| POL-CLAIM-0003 | Trojanized coding-challenge / recruiter delivery ecosystem (COMMON TECHNIQUE class) |
| POL-CLAIM-0004 | Analyzed sample inside RankChallenge-react |
| POL-CLAIM-0005 | Substantially different structure from NodeRabbit |
| POL-CLAIM-0006 | C2 starts before OTP (`app.js` → `requireAuth.js` → `requireObjects.js`) |
| POL-CLAIM-0007 | Cross-platform persistence (NetSync / cron / LaunchAgent) |
| POL-CLAIM-0008 | Framed as first JS/Node tooling for Mirage Kitten vs prior native C/C++/Go (vendor assessment) |
| POL-CLAIM-0009 | C2 protocol: `/beacon` HTTP 400 + socketId; `/gate/*` / `/vault/*` |
| POL-CLAIM-0010 | Host ID `129--<hostname>`; 22 commands; EVAL_JS / SYSTEM_CHECK |
| POL-CLAIM-0011 | Handshake / command-ID / beacon timing overlap with Retrograde/MiniFast (not NodeRabbit) |
| POL-CLAIM-0012 | OTP validate via lifespotify.com path; late-June-2026 registration claim |

---

## 6. Case isolation / lineage (mandatory)

| Question | ETW position |
|----------|--------------|
| Same Securelist article as NodeRabbit? | Yes — dual-referenced primary HTML |
| Same implant / shared authorship? | **Not established** — default **non-equivalence** |
| Shared delivery technique? | Yes — recruiter / coding-challenge (**COMMON TECHNIQUE**) |
| Stronger protocol parallel | PollCat ↔ MiniFast/Retrograde (vendor), **not** PollCat ≡ NodeRabbit |
| Auto-merge IOCs with NodeRabbit? | **No** |
| RankChallenge MD5 | **PollCat only** (`POL-IND-0001`) |
| `colorized_terminal` / `pretty-log` npm | **NodeRabbit only** — do not ledger under POL-* |

Prior NodeRabbit IC3: `dded86972e9347e0be27a6597b4cf08a` — cite as related separate filing only.

---

## 7. OBSERVED_PASSIVE notes (ETW — not ownership)

| Indicator | Observation | Limit |
|-----------|-------------|-------|
| `lifespotify.com` | CT cert_count=47; RDAP 200; Wayback 302 captures 2023–2025 | Domain reuse possible; CT ≠ ownership |
| `sahi-finance.com` | RDAP 200; CT intermittently failed | Retry later |
| `gamebarapp*.azurewebsites.net` | CT count=0 | Shared Azure edge ASSOCIATION_ONLY |
| GitHub code search (logged-out) for distinctive PollCat strings | `result_count=0` | Negative public-code hit only |

---

## 8. Known gaps (do not invent)

| Priority | Gap | Status |
|----------|-----|--------|
| P1 | RankChallenge MD5 → SHA-256 | **OPEN** |
| — | Actor-owned C2 IPv4/IPv6 | **None in corpus** |
| — | ETW sandbox PCAP / config extract | **Lack** |
| P0/P1 | Broader secondary corpus beyond Securelist | PARTIAL (CyberVeille FR summary; no unique hashes) |

---

## 9. Primary sources

| Org | Title / note | URL |
|-----|--------------|-----|
| Kaspersky GReAT / Securelist | Mirage Kitten / NodeRabbit / PollCat (2026-09-01) | https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/ |

Lineage note (internal): `shared/lineage/pollcat-noderabbit-lineage-note.md`  
Indicator CSV: `reports/law-enforcement/packages/05-pollcat/03_INDICATORS.csv`  
Investigation: `investigations/pollcat/`  
STIX/IOC export: `reports/law-enforcement/CTI-Evidence-Repository/families/PollCat/`

---

## 10. What this package does **not** claim

- Shared PollCat ↔ NodeRabbit implant authors/operators  
- Independent Mirage Kitten attribution by ETW  
- Dollar loss / named victims  
- Fabricated SHA-256, IPs, or C2 hosts  
- Ownership of Azure / Cloudflare edge infrastructure  
- That ETW discovered PollCat  

---

## 11. Safety statement

No malware was executed and no suspected command-and-control system was contacted during preparation of this package. No malware binaries are included for IC3 web-form upload.

---

## 12. After filing checklist

1. Save IC3 Submission ID + confirmation screenshot.  
2. Create `IC3_FILING_RECORD.md` in this folder.  
3. Set status `FILED_IC3` in `02_FBI_SUMMARY.md` and `MASTER_INDEX.csv`.  
4. Update `reports/law-enforcement/README.md` status line.
