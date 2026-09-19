# Showboat — Deep Passive Pass (2026-09-19)

**Scope:** Freeze Lumen primary + companion IOC appendix; extract Linux/telecom IOCs; evidence for ≥2022 activity; FIRST/CERT hunt.

---

## Primary freezes

| ID | Artifact | SHA-256 | URL |
|----|----------|---------|-----|
| PS-SHO-001 | `lumen-showboat.html` | `02de634758ad3fbc83de5d1250ed4c7a4c194d83b2aa6860d00d578940688a05` | https://www.lumen.com/blog/en-us/introducing-showboat-a-new-malware-family-taunts-defenses-and-targets-international-telecom-firms |
| PS-SHO-002 | `Showboat_IOCs.txt` | `2da4ab57dc4d2060f1dfb89e9b20fc74881dc7c4d9ec4d7c94c08bbc4aa20377` | https://raw.githubusercontent.com/blacklotuslabs/IOCs/main/Showboat_IOCs.txt |
| PS-SHO-003 | THN companion | `db11730146169ac59e73eb64e3e31caa924dc8c2a353684eb97e4e862c2925b5` | https://thehackernews.com/2026/05/showboat-linux-malware-hits-middle-east.html |
| PS-SHO-004 | Malpedia | `628a4834b70470228b797ee6d35e7ea2e338301df4bfb495d63b239661e20e64` | https://malpedia.caad.fkie.fraunhofer.de/details/elf.showboat |
| PS-SHO-005 | threat.wiki | `c652904591be0f3e2f9f1cb8e185427f706c3fdf48bfa8a34882de5f6a755d2f` | https://threat.wiki/tools/showboat/ |
| PS-SHO-006 | 1275.ru (RU) | `91ef74e3165f08f6fe4ef1487d1f4521b2ee3bb783579e5d95e6cbca21219df0` | https://1275.ru/ioc/obnaruzhen-novyy-linux-vredonos-showboat-telekommunikatsionnye-kompanii-pod-pritselom-kitayskih-hakerov_26365 |
| PS-SHO-007 | Lumen APAC mirror | `458940d106cf427cf57e267c703121a139827fd6bf807970cacc9363075dd077` | https://apac.lumen.com/en/blog/showboat-malware-targeting-telecom-providers/ |

Publication meta from primary HTML: **blogpublisheddate May 21, 2026**; authors Danny Adamitis, Steve Rudd; edit Ryan English; PwC CTI collaboration referenced (PwC report URL not inline-resolved this pass).

---

## NEW IOCs / technical facts

### From Lumen article (PRIMARY-SOURCE)

| Indicator / fact | Notes |
|------------------|-------|
| XOR config key `look me, AV!` | Hardcoded per-byte XOR |
| Config: `SERVER_ADDRESS=telecom.webredirect.org`, port 80, sleep 5–10 / slow 20–25 | Decrypted config excerpt |
| C2 IP `139.84.227.139` | Resolves from telecom.webredirect.org |
| X.509 SHA256 `27df475626aafce2ea1548a9f35efb9ad951298c8b11a6adb3ccdfcd5170c677` | “My Organization” metadata; primary cluster pivot |
| Cert on :53 `A72427af3c046fd90999a6505b2372dc4ffde122227f30ed21621ecd4f2d3e8b` | Mar 15–17 2025 window noted |
| Cert on :80 `E28a96f983b8605decd2ac1db16ebad5fa741a6aa4e585a38ade0e5ad7d6cec0` → second C2 `194.135.25.132` | |
| Secondary cluster fingerprint `2229e7f3cabbce4d67cd79c89fd5a100b20e8a99f4a2bf9aac77a978f49eb520` | |
| Impersonation: `singtelcom.site` @ `23.27.201.160`; `kaztelecom.shop` @ `101.36.105.222` | Telecom lookalikes |
| Possible upstream `116.169.244.208:2096` China Unicom / Chengdu | ASSOCIATION_ONLY / upstream hypothesis |
| Secondary C2 `192.9.141.111` (US victims port 9999); `64.176.43.209` (Ukraine/Donbas geoloc) | Vendor telemetry |
| SOCKS5 / portmap URL markers append ` SKS` / ` MAP` | Detection strings |
| Pastebin dead-drop for hide-code **first posted January 2022** | **Strongest ≥2022 historical activity evidence** |
| VT ELF discovery May 5, 2025; 0 detections at submission; still ~0 through Apr 2026 | |
| Beacon: host info in PNG field as encrypted+base64 | |
| Victims: ME telecom; Afghanistan ISP Outlook → `194.135.25.132` Dec 1 2025–Feb 3 2026; Azerbaijan | |
| Attribution | “at least one, and likely several, PRC-aligned activity clusters” — **not** single named APT |

### From Black Lotus Labs `Showboat_IOCs.txt` (PRIMARY-SOURCE companion)

| Type | Value |
|------|-------|
| Linux sample SHA-256 | `d6a4fad5448838dbc8cc6b33f1dbfbdc7a2fad36de58ff6a66dce96f729f7011` |
| Windows sample SHA-256 | `8fc0b205876923d35df436e666ec1506839ef3861422037490bae4daa63c1165` |
| Windows sample SHA-256 | `253cc9dbabeb0054f3d353cfff24f2aeb9cecd3e031333127d33cc4edacf2a56` |
| Hosting `ukpkmkk.bin` | `114.116.239.178` (2024-11-01–2025-02-19) + cert `494676b9255d8c65499c1d5148e34440d27de2e26ad7dd7162dd8e683dba2790` |
| Hosting | `103.10.145.129` (2023-04-04) same cert — **2023 historical infra** |
| Extra TLS | `f5359f23eafe7c0f9a445d654dd94c31e982f02c48ac59d1cacf6d6f9f594425` on 114.116.239.178 |
| Additional IPs | `45.76.157.243`, `139.84.135.190`, `139.180.223.193`, `152.32.159.11` (singtelcom.site), `38.246.73.120` — first-seen from **2023-04** onward |

### From The Hacker News (SECONDARY; cites Lumen + interview)

| Claim | Notes |
|-------|-------|
| Kaspersky tracks ELF as **EvaRAT** | Alias lead — SECONDARY |
| Pastebin created **January 11, 2022** | Corroborates mid-2022+ activity framing |
| Calypso / Bronze Medley / Red Lamassu + **JFMBackdoor** Windows DLL side-load in Afghanistan telecom campaign | Actor linkage — report as THN/Lumen narrative; not ETW-established |
| Initial access unknown; Calypso historically ASPX webshell | Context |

### Passive CT (OBSERVED_PASSIVE)

| Domain | cert_count |
|--------|------------|
| `telecom.webredirect.org` | 0 |
| `singtelcom.site` | 28 |
| `kaztelecom.shop` | 22 (retry succeeded) |

### FIRST / Telecom CERT hunt

No FIRST.org note or national telecom CERT advisory uniquely naming Showboat located this pass. Gap remains OPEN (negative result recorded).

### Foreign language

Russian 1275.ru repeats Lumen findings (modular Linux, Socks5, mid-2022, ME telecom, PRC-aligned) — **no unique IOCs** beyond Lumen set. SECONDARY.

CybersecurityNews page fetch failed earlier; Picus article retrieved 2026-09-19 (staging OSINT pass). Filenames `ukpkmkk.c` / `ukpkmkk.so`, `ld.so.preload`, and process filter `kworkers|dbus|autoupdate` ledgered as SECONDARY (`SHO-CLAIM-0009/0010`, `SHO-IND-0023`–`0026`). Pastebin raw actor URL still OPEN.

---

## Historical activity evidence (≥2022)

1. Pastebin hide-code post **Jan 2022** (Lumen + THN Jan 11, 2022) — PRIMARY/SECONDARY corroboration.  
2. BLL IOC appendix IP `103.10.145.129` first seen **2023-04-04**.  
3. Lumen narrative “active since at least mid-2022”.  
4. Disclosure May 2026 ≠ first activity.

---

## Gaps remaining

- PwC companion report URL not archived.  
- Full primary-cluster IP list beyond appendix (article says “full list… in our GitHub” — appendix present but may be incomplete vs figure).  
- FIRST/CERT still absent.  
- No interaction with C2 (policy).
