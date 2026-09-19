# Linux Node.js Persistence Hunting — EXPERIMENTAL / UNVALIDATED

**Status:** INFERRED detection hypothesis — **UNVALIDATED** by ETW  
**Family:** NodeRabbit (Mirage Kitten tooling per Kaspersky)  
**Primary behavior source:** Securelist 2026-09-01  
**Cutoff:** 2026-09-19  
**Do not** treat this document as a production detection rule pack.

---

## Hypothesis (INFERRED)

On developer / workstation fleets, the combination of:

1. **Node.js** executing a script from a **masquerade path**, and/or  
2. **`@reboot` cron** launching Node against that script,

is a **high-priority triage** signal when the path matches known NodeRabbit Linux masquerades.

### Path classes of interest

| Priority | Path / pattern | Variant (PRIMARY) |
|----------|----------------|-------------------|
| High | `~/.config/microsoft-edge-update/msedge_update.js` | V1 |
| High | `~/.config/intel-dsa/idriver_support.js` | V2 |
| High | Suspicious JS under `~/.local/share/` + `@reboot` cron invoking `node` | V3 |
| Medium | Any `@reboot` cron line: `node` / `nodejs` + hidden/masquerade config dirs | Evolution-agnostic |

### Supporting (non-path) signals

- Local listener ports in `41984–46983` (V2 host-derived) or fixed `127.0.0.1:48739` (V1) — may be noisy  
- Beacon shapes toward `/api/rabbit/*` or `/sdk/v2/*` — static domains rotate via `agent:servers`  
- WSL: Windows task launching `wscript.exe` → `wsl.exe` with unexpected args (V3)

---

## Why UNVALIDATED

- No ETW lab replay of samples  
- No confirmed false-positive baseline against legitimate Edge Update / Intel DSA packaging on Linux (those products are primarily Windows; still, path collisions and admin scripts exist)  
- Cron `@reboot` + Node is also used by benign developer tooling  

---

## Suggested triage questions (analyst)

1. Is the JS file present under the exact masquerade directory?  
2. Does crontab `@reboot` point at that file with a bundled/local `node` binary?  
3. Is there a matching Windows/WSL bridge (`launcher.vbs` + `wsl.exe`)?  
4. Any `# shepherd-persist` Git hooks on the same host? (separate marker — see catalog)

---

## Labeling

Every alert derived from this doc must be tagged **EXPERIMENTAL** until validated against benign baselining and sample replay in an isolated lab.
