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
| **StarlandRAT (this package)** | `ETW-STR-IC3` | *not filed* |

---

## 2. Technical indicator appendix (STR-IND-0001–0017)

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

=== FILENAME ===
LICENSE.txt

=== STRING ===
skuefq_bot
komandastuk_bot
stuk komanda
PythonLauncher

=== CRYPTO_CONSTANT ===
0x6ae382ed2154cc84c6672e4e908cd2c69c1b35ba
odg5t8mvssvh
helo1
$m7*rYpry3

=== MUTEX ===
f2j398fj239d8j23dkkskskkkkkkkkk

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

See [`04_SOURCES.md`](04_SOURCES.md). Local freeze: `evidence/primary-sources/starlandrat/talos-uat-11795-starland-wldr.html` SHA-256 `0eff5ee5f2e32d8cc50ea58a9a4f6bf94b4919a9f997112d88f199e6a735eb84`.
