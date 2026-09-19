# PollCat — Deep Passive Pass (2026-09-19)

**Scope:** Maximize PollCat-specific defensive intelligence distinct from NodeRabbit. Passive only.  
**Primary freeze:** `PS-POL-001` ≡ Securelist HTML dual-ref (`PS-NRB-001` bytes).  
**Isolation:** Do not merge with NodeRabbit ledgers / `ETW-NRB-IC3`.

---

## NEW facts (with provenance)

### Implant structure & execution (PRIMARY-SOURCE)

| Fact | Provenance | URL |
|------|------------|-----|
| Lure project `RankChallenge-react`; start `npm i && node index.js` | PRIMARY-SOURCE | https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/ |
| Package labeled `ctf-server`; prints `CTF server running`; frontend `ctf-*` storage keys; tutorial `path/to/ctf` — Kaspersky notes AI/template smell | PRIMARY-SOURCE | same |
| Load chain: `app.js` → `requireAuth.js` → `requireObjects.js` starts C2 **before** OTP | PRIMARY-SOURCE | same |
| Failed OTP does **not** stop PollCat; successful OTP issues JWT + second worker; first JWT-bearing request triggers persistence | PRIMARY-SOURCE | same |
| OTP forwarded to `https://lifespotify.com/api/users/b879746e-fed9-4211-a6da-4d8223681267/otp/validate` (domain “late June 2026” per Kaspersky) | PRIMARY-SOURCE | same |
| Host identity format `129--<hostname>` | PRIMARY-SOURCE | same |

### Persistence (PRIMARY-SOURCE) — distinct from NodeRabbit

| OS | Mechanism |
|----|-----------|
| Windows | `%APPDATA%\Microsoft\Network` ← `package.json` + `requireObject.js`; `npm install`; daily task `NetSync_<username>` @ 09:00 |
| Linux | `~/.node_packages`; `npm i`; daily 09:00 cron **and** `@reboot` |
| macOS | same `~/.node_packages` + cron; LaunchAgent `~/Library/LaunchAgents/com.harsh.requireobject.plist` (RunAtLoad + daily 09:00) |

### C2 protocol (PRIMARY-SOURCE) — distinct from NodeRabbit AES-GCM

| Item | Value |
|------|-------|
| Registration C2s | `sahi-finance.com`, `GamebarAppinformation.azurewebsites.net`, `GamebarApp.azurewebsites.net` |
| Register | `POST /beacon` JSON `clientId,type=poll,pcName,userName` |
| Success signal | **HTTP 400** body `{socketId, pollInterval, jitterTime}` |
| Ops | `POST /gate/hello`, `GET /gate/fetch?token=`, `POST /gate/submit`, `GET /vault/<uuid>`, `PUT /vault/push/`, `POST /gate/track` |
| Inventory exfil | `POST /api/system-details/result` |
| Defaults | poll 120000 ms, jitter ≤5000 ms |
| Command set | 22 declared; unimplemented: `0xA1 WS_DOWNLOAD`, `0xB0 REQUEST_ELEVATION`, `0xB1 PERSIST` |
| Notable cmds | `0x20 EVAL_JS`, `0x30 SYSTEM_CHECK` (24 security-vendor folder strings), `0x0B RUNDLL` |

### Hash ledger correction

| MD5 | Filename | Correct case |
|-----|----------|--------------|
| `795e053a990a1569ffdcb57f48f6d085` | `RankChallenge-react-6uJSX3-main.zip` | **PollCat** (`POL-IND-*`), not NodeRabbit |

Previously listed as `NRB-IND-0011` — retain cross-ref note; new authoritative row is `POL-IND-0001`.

### Passive observations (OBSERVED_PASSIVE)

| Indicator | Observation | Notes |
|-----------|-------------|-------|
| `lifespotify.com` | CT cert_count=47; RDAP 200 | CT ≠ ownership. Wayback CDX shows 302 captures 2023–2025 — **domain reuse possible**; Kaspersky says late-June-2026 registration for this campaign use |
| `sahi-finance.com` | RDAP 200; CT intermittently failed | Retry CT later |
| `gamebarapp*.azurewebsites.net` | CT count=0 | Shared Azure edge — ASSOCIATION_ONLY hosting class |
| GitHub code search (logged-out) for `requireObjects.js`, `com.harsh.requireobject`, `/gate/fetch?token=`+socketId, `129--`+PollCat | `result_count=0` | Negative public-code hit |

### Foreign-language secondary (SECONDARY)

- French CyberVeille summary cites PollCat C2s / endpoints and links ThreatFox/URLhaus for `lifespotify.com`, `sahi-finance.com` — **no unique hashes beyond Securelist**. Artifact: `evidence/primary-sources/pollcat/cyberveille-pollcat-fr.html`.

### Attribution note (do not climb ladder)

Kaspersky ties PollCat C2 handshake / command IDs / beacon timing to **Retrograde/MiniFast**, not to NodeRabbit code lineage. Shared Mirage Kitten attribution ≠ shared implant authorship with NodeRabbit.

---

## Artifacts produced this pass

- Dual Securelist mining notes (this file)
- `POL-IND-*` transcription
- Passive CT/RDAP/Wayback/GitHub under `evidence/passive-observations/{certificate-transparency,rdap,archives,github}/pollcat/`
- Companion freeze: CyberVeille FR HTML

## Attribution note (staging follow-up)

Do not ledger `colorized_terminal` / `pretty-log` under POL-* — those are NodeRabbit local-bundle packages (NRB-IND-0042–0044). See `docs/research-notes.md` correction.
