# NodeRabbit — Linux / Unix / Shell-Context Track

**Primary:** Kaspersky GReAT — [Mirage Kitten / NodeRabbit](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/) (2026-09-01)  
**Cutoff:** 2026-09-19  
**Related ledgers:** `intelligence/unix-search-ledger.csv`, `analysis/linux-artifact-matrix.csv`  
**Literal `whoami` in primary:** **No**  
**Linux/Unix research value:** **Very high** (native Win/Linux/macOS; explicit Linux persistence all three variants; WSL in V3)

---

## Disposition

NodeRabbit is **not** Windows-only. Securelist documents a single Node.js codebase with **OS-specific persistence** including full Linux paths and cron, plus a **WSL bridge** in Variant 3. Account/host discovery uses **agent ID hashing** and **C2 commands** (`sys:info`, `net:config`, `proc:start`) — semantic equivalents of host/account enumeration without a hardcoded `whoami`.

---

## Capability classes (use these labels)

| Class | Meaning |
|-------|---------|
| **literal shell command** | Hardcoded shell string in implant (e.g. `whoami`) — **not observed** for whoami |
| **runtime/API equivalent** | Node/OS APIs or structured C2 replies that return host/user identity |
| **C2 arbitrary exec** | Operator can run any shell via `proc:start` / `proc:exec` |
| **persistence artifact** | Paths cron LaunchAgents Run keys WSL bridge |
| **observed Linux execution** | Primary documents Linux-specific persistence/execution behavior |
| **merely cross-platform-compatible** | Same JS capability that *could* run on Linux without Linux-specific evidence |

---

## Variant 1 — Linux persistence

| Artifact | Detail | Class |
|----------|--------|-------|
| Path | `~/.config/microsoft-edge-update/msedge_update.js` | persistence artifact / observed Linux execution |
| Mechanism | `@reboot` cron entry invoking the script with the current Node.js executable | persistence artifact |

Windows contrast (same masquerade theme): `%APPDATA%\Microsoft\EdgeUpdate\msedge_update.js` + `nodew.exe` + Run key `MicrosoftEdgeUpdate`.

---

## Variant 2 — Linux persistence

| Artifact | Detail | Class |
|----------|--------|-------|
| Path | `~/.config/intel-dsa/idriver_support.js` | persistence artifact / observed Linux execution |
| Mechanism | `@reboot` cron entry | persistence artifact |

Windows contrast: `%LOCALAPPDATA%\Intel\DSA\idriver_support.js` + `IntelDSA.exe` + scheduled task `IntelDriverSupportUpdate`.

Enterprise proxy/PAC/NTLM stack is documented primarily for Windows; it **motivates** the corporate-developer hypothesis but is thinner for Linux in the primary write-up.

---

## Variant 3 — Linux + WSL

### Linux

| Artifact | Detail | Class |
|----------|--------|-------|
| Path | Payload copied under `~/.local/share` | persistence artifact / observed Linux execution |
| Mechanism | Attempt `@reboot` cron; **if `crontab -l` fails, persistence is skipped** | persistence artifact |

### WSL bridge

| Step | Detail | Class |
|------|--------|-------|
| Linux side | Uses the Linux payload already staged for persistence (`~/.local/share` path) | observed Linux execution |
| Windows side | Writes `launcher.vbs` under the Windows user profile | persistence artifact |
| Scheduler | Daily **10AM** Windows task → `wscript.exe` → `wsl.exe` → Linux payload | persistence bridge |

---

## Account / host discovery **without** literal `whoami`

| Mechanism | What it returns / does | Class |
|-----------|------------------------|-------|
| **Agent ID** | SHA-256 of hostname + username + OS version + architecture + MAC; truncate to first 32 hex chars | runtime/API equivalent |
| **`sys:info`** | hostname, domain-user information, username, PID | runtime/API equivalent |
| **`net:config`** | adapters, MAC addresses, IPs, DNS | runtime/API equivalent |
| **`proc:start`** | arbitrary shell execution (operator *may* run `whoami`) | C2 arbitrary exec |

**Assessment:** Searching only for the string `whoami` would **miss** the entire Linux track and most identity collection.

---

## C2 durability (Linux-relevant)

V3 `agent:servers` can replace the in-memory C2 list and persist to `.sv.json`. Static Azure/Cloudflare domains have a **short half-life**. Longer-lived hunting signal on Linux: Node + fake `microsoft-edge-update` / `intel-dsa` paths / suspicious `~/.local/share` + `@reboot` cron (see `detections/hunting/linux-node-persistence.md` — **EXPERIMENTAL/UNVALIDATED**).

---

## Git marker (separate catalog)

`# shepherd-persist;` in `.git/hooks/post-merge` and `post-checkout` is **Kaspersky PRIMARY**. Community KQL/GitHub queries are **SECONDARY detection material only** — see `docs/shepherd-persist-detection-catalog.md`.

---

## Claims

`NRB-CLAIM-0012` … `NRB-CLAIM-0019` in `claims/claims-ledger.csv` (`independently_verified=false`, `status=PRIMARY_SOURCE`, `retrieval_date_utc=2026-09-19`).

---

## What this track does **not** claim

- Independent ETW malware execution on Linux  
- That operators always run `whoami` via `proc:start`  
- Shared authorship with RatHat/Settra/Rapuncel  
