# IC3 / FBI Full Complaint Package — StarlandRAT

**Status:** `PRIMARY_FROZEN` — **not filed** (primary frozen; ready for human filing review) · **Primary freeze:** 2026-09-20  
**Family:** StarlandRAT only (case-isolated)  
**Portal:** https://www.ic3.gov/

---

## 1. Filing identity

| Field | Value |
|-------|-------|
| Reporter purpose | Defensive threat-intelligence referral (not personal victimization claim) |
| Crime-type language | Malware; Unauthorized network intrusion / remote access; Credential theft |
| Suggested subject | Defensive TI referral — StarlandRAT (Cisco Talos 2026-07) — `ETW-STR-IC3` |
| Dollar loss claimed | None |
| Personal victimization claimed | No |
| Malware binaries attached | No |
| ETW live C2 contact | None |
| Independently observed campaign ownership by ETW | None |

### Related prior IC3 Submission IDs (separate — no shared-operator claim)

| Family | Package | Submission ID |
|--------|---------|---------------|
| Rapuncel | `ETW-RAP-IC3` | `208b747c6f7445f0af2b69a9d63acc36` |
| Settra | `ETW-SET-IC3` | `631d8b4800d04bc19cdbfc6662e5c52c` |
| RatHat | `ETW-RAT-IC3` | `f92c4c2f0dd3481f898fdd125e728adf` |
| NodeRabbit | `ETW-NRB-IC3` | `dded86972e9347e0be27a6597b4cf08a` |
| PollCat | `ETW-POL-IC3` | `98a4444754324e539dbbffcb10c70637` |
| SynkLoader | `ETW-SYN-IC3` | `3440d0c64dc240499ff66deaa3311a0b` |
| Showboat | `ETW-SHO-IC3` | `db42033f319844c08ad103befebfca08` |
| Abyssos | `ETW-ABY-IC3` | `a23f0a9d6799480e994284416d354713` |
| SharkLoader | `ETW-SHK-IC3` | `6ed57963d0c64750aa14b6fcbaa2e576` |
| **StarlandRAT (this package)** | `ETW-STR-IC3` | *not filed* |

---

## 2. Technical indicator appendix (STR-IND-0001–0035)

### Compact paste block

```
=== DOMAIN ===
eorthopaedics.com
sastoro.com
web-devtools.com
zynaris.io
windowscreenrepairnearme.com
aipythondevs.com
polygon-rpc.com
alphabitcapital.info
niggerdemon.in

=== CRYPTO_CONSTANT ===
0x6ae382ed2154cc84c6672e4e908cd2c69c1b35ba
odg5t8mvssvh
helo1
$m7*rYpry3

=== STRING ===
skuefq_bot
komandastuk_bot
stuk komanda
PythonLauncher

=== MUTEX ===
f2j398fj239d8j23dkkskskkkkkkkkk

=== FILENAME ===
LICENSE.txt

=== SHA256 ===
162e436f18fe6099c57855c8d63fd747493624e87702dc749b242eb9a6b758ca
d52540621dec5ed56cac8532f0e4fe10a7575c3e17e984f59646909fa587dd35
47dedb08385449d48d8b6543030310317c92cddafa25e14ee0cb9a32d53ced5c
6ca7a458985350ac082a9c9820d7f8d39128a4c4bda2f5d32f169a45b7b22bc6
6ae334ce60d1a9b7fb96d1d0d0eda5ec7c2c31d3f0cf3e4d7e3056504d50043d
f4491736743a16f1278b8ba01649ee93343764e35ae5e1c0d5e0c0e1d7e32c14
896185a89bd7eb0520b03fdcfb8db0be98b43cf15f14041d73b23d3988c1bcab
a1835d333ac3db961a8ff1f4864e3c10a6f73a872c040599091390a009ac7804
2a27b3415114b874da295c19cce5227a8b8d9525cc2da331034a1f45528eecae
17e41d66ebfd56edc960f58f4285697ceceaa812514bb15092672c747979896e

=== IPV4 ===
104.248.233.104
192.81.216.250
74.114.119.201
178.255.126.39
193.149.176.254
185.238.191.234

```

Full structured table: [`03_INDICATORS.csv`](03_INDICATORS.csv).

---

## 3. Narrative (short)

Defensive threat-intelligence package concerning Starland RAT and the companion WLDR PowerShell C2 agent as publicly documented by Cisco Talos (UAT-11795 financially motivated campaign). Talos describes ClickFix / trojanized installer delivery (Webex/Zoom/MobaXterm/DBeaver-class lures), a memory-resident Python RAT with crypto-wallet recon, Telegram notification bots, and Polygon smart-contract fallback C2, plus optional CastleStealer/Remcos follow-ons and WLDR in-memory PowerShell post-ex. UAT-11795 / Russian-speaking framing is vendor assessment — ETW does not independently establish attribution. Author identity remains NOT_ESTABLISHED. WLDR tracked as companion under this case until distinct corpus warrants split.

---

## 4. Case isolation

WLDR Agent companion tracking under this case folder until distinct corpus warrants split. Do not attribute to active ETW families.

---

## 5. Sources

See [`04_SOURCES.md`](04_SOURCES.md). Primary freezes: Talos blog (PS-STR-001) + Talos IOC appendix (PS-STR-002).
