# Infrastructure ownership enrichment (packages 16–66)

Passive RDAP/WHOIS only (`intelligence/infra-ownership.csv`). Privacy-redacted WHOIS does **not** establish operator identity. Cloud hostnames (Azure App Service, Vultr Objects, Cloudflare Pages) are infrastructure, not actor orgs.

## High-signal net IOC harvest (new)

| Family | What was added (non-redundant) |
|--------|--------------------------------|
| PhantomHeart | 12 C2 IPs + OpenTIP domains; ASN clustering on AS56971 / SmartApe / MT Finance |
| NightLedger / ArcBridge / BridgeHead | Campaign-shared domains/IPs + tool-specific MD5s from Securelist IoC section |
| TernDoor / PeerTime / BruteEntry | Talos UAT-9244 IoC split (C2 IPs, PeerTime domains `bloopencil.net` / `xtibh.com` / `xcit76.com`) |
| ABCDoor | Residual OpenTIP IPs (ANTBOX / Cloud Innovation / Vultr) beyond prior 5 INDs |
| PromptSpy | `mgardownload.com`, `m-mgarg.com`, `54.67.2.84` (AWS) |
| GhostChat | `hitpak.org` |
| HybridPetya | Installer / UEFI SHA-1s + EFI paths (no C2 — ransomware) |
| LaxGopher / FriendDelivery | `43.231.113.50` (iTools LLC / Intelligent Tools, Mongolia ASN AS63962) |
| NosyDoor / NosyHistorian | NosyDownloader C2s (IP ServerOne / Shinjiru / Furcop MY/SG hosting) |
| Fooder / MuddyViper | `processplanet.org` + MuddyWater C2/staging IP set from ESET IoC repo |
| Dohdoor | DoH domains under `*.mswinsoftupdload.design` / `*.deepinspectionsystem.online` / `*.software` |
| HEAVYGRAM | Embedded credential string `ghazalehmehrjo@gmail.com` (**not** confirmed operator ID); Vultr Objects staging; Handala-related domains |
| MonsterV2 | Proofpoint SHA-256 sample set (network thin) |
| GhostContainer | Exchange backdoor MD5s |
| MiniUpdate / MiniJunk / MiniBrowse | Screening Serpens related domains (shared campaign context — case-isolated notes) |

## Ownership caveats

- Most domains are privacy-proxy registered (Contact Privacy / whoisproxy / Cloudflare Registrar).
- Recurring bulletproof/VPS patterns: **AS56971 (CGI Global / GoldIP)**, **SmartApe (AS56694)**, **Cloud Innovation**, **ANTBOX NETWORKS**, **Vultr/Choopa**, **iTools LLC**.
- LaxGopher C2 `43.231.113.50` WHOIS aligns with ESET’s “Intelligent Tools” hosting note.
- HEAVYGRAM email is a **string inside a sample**, not a verified operator mailbox.

## Tooling

Re-run: `python3 shared/tooling/enrich_sparse_iocs_whois.py` (skips duplicate values).
