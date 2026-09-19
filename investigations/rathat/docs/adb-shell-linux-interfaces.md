# RatHat — ADB Shell / Linux-Kernel Interface Track

**Primary:** Zimperium zLabs — [RatHat](https://zimperium.com/blog/rathat-ai-powered-mobile-threat-is-here-for-your-credentials-bank-accounts) (2026-09-16)  
**Cutoff:** 2026-09-19  
**Literal `whoami` in primary:** **No**  
**Linux/Unix research value:** **High** — but **not** as desktop Linux malware

---

## Explicit wording rule (mandatory)

RatHat is **Android malware** that obtains an **ADB shell context** (UID **2000**) and then interacts with **Linux-kernel-backed interfaces** on the device (`/data/local/tmp`, `/dev/input/*`, Android `getevent`, `pm`/`am`/`settings`/`dumpsys`).

**Do NOT call RatHat “Linux malware.”**  
Acceptable: *Android malware obtaining ADB shell context interacting with Linux-kernel-backed interfaces.*

---

## Privilege path (PRIMARY)

1. Victim grants **Accessibility**  
2. Synthetic UI automation enables **Developer Options** + **Wireless Debugging**  
3. Accessibility scrapes 6-digit pairing code + dynamic port  
4. Embedded **libadb-android** self-pairs to local `adbd`  
5. Result: **shell UID 2000** without an external PC  

---

## Staging paths (shell-writable)

| Artifact | Path / name | Role |
|----------|-------------|------|
| Go agent | `/data/local/tmp/liblocal-service.so` | C2 brain in shell context; local HTTP `127.0.0.1:7910` |
| FRP client | `/data/local/tmp/frpc` (from masqueraded `libmedia_codec.so`) | Reverse tunnel (fatedier/frp) |
| Update staging | `/data/local/tmp/local-service.update` | Agent self-update (PRIMARY endpoint description) |
| APK restage | `/data/local/tmp/app.apk` | Reinstall after fake uninstall |

---

## Shell commands reported (PRIMARY)

Executed from the elevated **ADB shell / Go agent** context:

| Command pattern | Purpose |
|-----------------|---------|
| `dumpsys deviceidle whitelist +%s` | Doze exemption |
| `am set-standby-bucket %s active` | Keep app in active standby bucket |
| `pm disable-user --user 0 %s` | Disable arbitrary packages |
| `pm uninstall -k --user 0 %s` | Uninstall (e.g. security apps) |
| `pm install -r -g … /data/local/tmp/app.apk` | Reinstall malware APK |
| `pm grant …` | Grant permissions from shell |
| `settings put secure enabled_accessibility_services '…'` | Re-enable Accessibility |
| `settings put secure accessibility_enabled 1` | Accessibility on |

These are **Android shell utilities** on a Linux kernel — not evidence of a Linux desktop implant.

---

## Hardware input → PIN reconstruction

| Step | Detail |
|------|--------|
| Tool | `getevent` (Android debug utility) |
| Interface | `/dev/input/*` (kernel input event nodes) |
| Privilege | Normal apps cannot read; **shell UID 2000 can** |
| Output | `EV_ABS` X/Y + timestamps |
| Reconstruction | Combine with known keypad geometry (`locateValues.json`) → PIN/pattern |

This channel is **distinct** from Accessibility text-event keylogging (see `persistence-taxonomy.md`).

---

## Why this is still a “Unix/shell-context” research track

- Host/account-style discovery and control happen via **shell** and **kernel interfaces**, not via a literal `whoami` binary call in the write-up.  
- Paths and tools (`/data/local/tmp`, `/dev/input`, `getevent`) are familiar to Linux responders — but the **platform classification remains Android**.

---

## Related artifacts

- Persistence layers: `docs/persistence-taxonomy.md`  
- Browser resource IDs: `analysis/browser-target-matrix.csv`  
- IOC metadata (Zimperium IOC repo): `iocs/zimperium-ioc-repo-index.md` + CSV ledgers  
- Claims: `RAT-CLAIM-0013` … `RAT-CLAIM-0017`  
