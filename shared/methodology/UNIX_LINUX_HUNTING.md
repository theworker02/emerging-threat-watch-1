# Unix / Linux / Shell-Context Hunting

**Status:** Program methodology addendum  
**Cutoff:** 2026-09-19  
**Ledgers:** `intelligence/unix-search-ledger.csv`, `intelligence/linux-artifact-matrix.csv`

---

## Problem

Limiting host-discovery research to the literal shell command `whoami` is **too narrow**. Modern implants often:

- compute identity via **runtime/API** fields (hostname, username, MAC → hash);
- expose structured C2 commands (`sys:info`, `net:config`);
- offer **arbitrary shell execution** (`proc:start`) without hardcoding `whoami`;
- obtain **platform shell context** (e.g. Android ADB UID 2000) and then touch **Linux-kernel-backed** paths (`/data/local/tmp`, `/dev/input/*`).

---

## Required search practice

1. Record **literal** matches for `whoami` / `id` / `who` when present.  
2. Also record **semantic** matches: agent IDs, `sys:info`-class commands, OS username APIs, ADB shell privilege paths.  
3. Preserve **NEGATIVE SEARCH RESULT** dispositions (e.g. `SEARCH-SET-LINUX-001`, `SEARCH-RAP-LINUX-001`) as information — do not invent Linux TTPs.  
4. Distinguish capability classes: literal shell | runtime/API | C2 arbitrary exec | persistence artifact | observed Linux execution | merely cross-platform-compatible.

---

## RatHat wording rule

Describe RatHat as **Android malware obtaining ADB shell context interacting with Linux-kernel-backed interfaces**.  
**Do not** call it “Linux malware.”

---

## Family research values (2026-09-19 disposition)

| Family | Literal whoami in primary? | Linux/Unix research value |
|--------|---------------------------|---------------------------|
| NodeRabbit | No | Very high |
| RatHat | No | High (shell-context / Android) |
| Settra | No | Low |
| Rapuncel | No defensible hit | Low presently |

---

## Cross-links

- NodeRabbit track: `investigations/noderabbit/docs/linux-unix-track.md`  
- RatHat track: `investigations/rathat/docs/adb-shell-linux-interfaces.md`  
- Case isolation still applies (`CASE_ISOLATION.md`) — technique similarity ≠ shared authorship  
