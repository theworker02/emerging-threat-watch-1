# RatHat Persistence Taxonomy

**Primary:** Zimperium zLabs 2026-09-16  
**Cutoff:** 2026-09-19

Uninstalling the visible APK is **not** remediation if privileged-agent or tunnel layers remain.

| Layer | Mechanism (reported) | Survives APK uninstall? | Remediation implication |
|-------|----------------------|-------------------------|-------------------------|
| **Application persistence** | Fake uninstall failure overlay; Device Admin anti-uninstall; heartbeat redeploy of local-service while app present | Partially (UI tricks) | Remove admin rights; force uninstall from clean state |
| **Privileged-agent persistence** | Go agent `liblocal-service.so` staged under `/data/local/tmp`, runs outside package lifecycle; can `pm install -r -g` and re-enable Accessibility via `settings put secure` | **Yes** | Kill shell-uid processes; disable Wireless Debugging; wipe staged binaries; revoke ADB keys |
| **Remote-connectivity persistence** | FRP client `libmedia_codec.so` / `frpc` reverse tunnel using C2-fetched FrpsAddr/Port/Token | **Yes** (if agent alive) | Block egress; remove frpc; rotate network path |

## Architecture reminder

App (Accessibility) → self-ADB pair → stage Go agent + FRP → agent grants perms / Doze exemptions → tunnel exposes device.

## Hardware-input vs Accessibility keylogging

| Channel | Sensor | Output | Bypasses |
|---------|--------|--------|----------|
| Accessibility text-event | UI events | Reconstructed typed text | Limited by FLAG_SECURE / custom keyboards |
| Browser URL harvest | Resource IDs | Address bar strings | App-specific |
| **Hardware getevent** | `/dev/input/*` via shell | X/Y + timestamp → PIN/pattern via `locateValues.json` geometry | FLAG_SECURE, custom IME, lock-screen digit hiding |

Corroboration across channels increases confidence in recovered credentials; each channel alone has gaps.
