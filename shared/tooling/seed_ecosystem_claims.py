#!/usr/bin/env python3
"""Seed Phase 1+ ecosystem claim ledgers and matrices. Local only; cutoff 2026-09-19."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RET = "2026-09-19T17:52:00Z"
CUTOFF = "true"


def wcsv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})
    print(f"wrote {path.relative_to(ROOT)} ({len(rows)} rows)")


CLAIM_FIELDS = [
    "claim_id", "family", "case_id", "claim", "source_organization", "source_team",
    "source_title", "source_url", "published", "source_type", "status", "confidence",
    "independently_verified", "evidence_tags", "related_evidence_ids", "derives_from",
    "notes", "retrieval_date_utc", "cutoff_applies",
]


def claim(**kw):
    kw.setdefault("independently_verified", "false")
    kw.setdefault("cutoff_applies", CUTOFF)
    kw.setdefault("retrieval_date_utc", RET)
    kw.setdefault("source_team", "")
    kw.setdefault("related_evidence_ids", "")
    kw.setdefault("derives_from", "")
    kw.setdefault("notes", "")
    return kw


# --- RAPUNCEL ---
LP = "https://blog.lastpass.com/posts/lastpass-delphos-report-rapuncel-infostealer"
LP_TITLE = "Threat Intel | One Kit, Forty Companies: How a Malware-as-a-Service Platform Used GitHub as a Distribution Network for its Campaign"
PK = "https://www.pk-sharma.com/briefing/fake-lastpass-github-rapuncel-domains-still-resolve"
BC = "https://www.bleepingcomputer.com/news/security/fake-lastpass-authenticator-github-repos-push-new-rapuncel-infostealer/"
TM = "https://www.trendmicro.com/it_it/research/26/c/boryptgrab-stealer-targets-users-via-deceptive-github-pages.html"
ES = "https://www.esentire.com/blog/malware-as-a-service-cocktail-errtraffic-and-cruciferra-killing-your-edr-since-2025"
PP = "https://www.proofpoint.com/us/blog/threat-insight/unpacking-cruciferra-analysis-sophisticated-crypter-service"
RF = "https://www.recordedfuture.com/research/malware-crypting-services-threat-actors"

rap_claims = [
    claim(claim_id="RAP-CLAIM-0001", family="Rapuncel", case_id="RAP",
          claim="LastPass TIME identified fraudulent GitHub org LastPass-Authenticator on 2026-08-13; joint report with Delphos Labs published 2026-09-17 reflecting investigation state as of 2026-09-10.",
          source_organization="LastPass", source_team="TIME + Delphos Labs", source_title=LP_TITLE, source_url=LP,
          published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="track:distribution|GitHub/SEO|timeline", notes="SOURCE-RAP-001 URL returned HTTP 403 on ETW retrieval 2026-09-19; claim reconstructed from carefully attributed secondary briefings (pk-sharma/BleepingComputer). Primary remains authoritative."),
    claim(claim_id="RAP-CLAIM-0002", family="Rapuncel", case_id="RAP",
          claim="Campaign uses SEO-optimized fake GitHub repositories/pages impersonating LastPass Authenticator and serving at least 40 branded impersonation lure pages from shared payload infrastructure.",
          source_organization="LastPass", source_team="TIME + Delphos Labs", source_title=LP_TITLE, source_url=LP,
          published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="track:distribution|GitHub/SEO|MaaS", notes="Secondary press often says '39 other companies'; primary wording per pk-sharma is at least 40 other branded lure pages / forty companies headline — brand-count drift flagged."),
    claim(claim_id="RAP-CLAIM-0003", family="Rapuncel", case_id="RAP",
          claim="Download chain: fake GitHub portal → GitHub Pages redirect waypoints → traffic director → terminal domain → payload server.",
          source_organization="LastPass", source_team="TIME + Delphos Labs", source_title=LP_TITLE, source_url=LP,
          published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="track:infra|GitHub/SEO|distribution"),
    claim(claim_id="RAP-CLAIM-0004", family="Rapuncel", case_id="RAP",
          claim="Named delivery domains include albinofennel.com, icansamyope.com, hanselarinmusky.com, zaffersnouty.com, istatlmenus.com (traffic director), macperformancetools.com.",
          source_organization="LastPass", source_team="TIME + Delphos Labs", source_title=LP_TITLE, source_url=LP,
          published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="track:infra|domains", related_evidence_ids="RAP-EV-DNS"),
    claim(claim_id="RAP-CLAIM-0005", family="Rapuncel", case_id="RAP",
          claim="Archives padded to large sizes (e.g., LastPass-Authenticator-download-1.66.2.zip ~148 MB; lastpass-authenticator-2.78.7.zip ~127.9 MB) using filler DLLs to evade size-limited scanners.",
          source_organization="LastPass", source_team="TIME + Delphos Labs", source_title=LP_TITLE, source_url=LP,
          published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="track:distribution|file-pumping|track:cruciferra", notes="File pumping also advertised as Cruciferra builder feature — layer attribution OPEN (RAP-H-CRY)."),
    claim(claim_id="RAP-CLAIM-0006", family="Rapuncel", case_id="RAP",
          claim="Installer is renamed legitimate Microsoft Visual Studio CoreCLR debugger vsdbg.exe sideloading malicious vsdbg.dll.",
          source_organization="LastPass", source_team="TIME + Delphos Labs", source_title=LP_TITLE, source_url=LP,
          published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="track:cruciferra|sideload|TRUSTED_BINARY", notes="RAP-H-CRY: sideload may be Cruciferra/PUROSANGUE-supplied rather than stealer-authored."),
    claim(claim_id="RAP-CLAIM-0007", family="Rapuncel", case_id="RAP",
          claim="Alinubx.sys is identity-swapped CcProtect.sys (Henan Dafeng / CnCrypt), Microsoft WHCP-signed (~Mar 2023 timestamp), deployed as nvfsflt64.sys / NvFsFilter; kills processes matching 145 hardcoded AV/EDR names via kernel ObOpenObjectByPointer AccessMode=KernelMode.",
          source_organization="LastPass", source_team="TIME + Delphos Labs", source_title=LP_TITLE, source_url=LP,
          published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="track:Alinubx|SIGNED_DRIVER|BYOVD|145-EDR"),
    claim(claim_id="RAP-CLAIM-0008", family="Rapuncel", case_id="RAP",
          claim="Alinubx.sys reportedly scored 0/72 on VirusTotal as of 2026-08-20 (unchanged since ~2025-07) and was not on Microsoft vulnerable driver blocklist at publication; Delphos reported 0/20 SHA-256 matches vs DriverPolicy_Enforced.xml on 2026-08-20.",
          source_organization="LastPass", source_team="TIME + Delphos Labs", source_title=LP_TITLE, source_url=LP,
          published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="Moderate",
          evidence_tags="track:Alinubx|driver-trust-chain", notes="Signed ≠ trusted ≠ blocklisted. ETW did not re-query VT/blocklist."),
    claim(claim_id="RAP-CLAIM-0009", family="Rapuncel", case_id="RAP",
          claim="Rapuncel stealer collects credentials from >25 browsers and >30 crypto wallets, Discord/Steam/Telegram sessions, Windows Credential Manager, sensitive-named documents, screenshots; ABE bypass via helper DLL + Elevation Service; exfils ZIP to 2.26.126.50 over HTTP-shaped raw TCP; persists via Windows service.",
          source_organization="LastPass", source_team="TIME + Delphos Labs", source_title=LP_TITLE, source_url=LP,
          published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="track:stealer|exfil|infra"),
    claim(claim_id="RAP-CLAIM-0010", family="Rapuncel", case_id="RAP",
          claim="LastPass systems/services/customer vaults were not compromised; GitHub is not an official LastPass Authenticator distribution channel.",
          source_organization="LastPass", source_team="TIME", source_title=LP_TITLE, source_url=LP,
          published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="track:brand-trust|scope"),
    claim(claim_id="RAP-CLAIM-0011", family="Rapuncel", case_id="RAP",
          claim="LastPass/Delphos assess with moderate confidence that Rapuncel is a BoryptGrab-related variant/sibling; loader built with Cruciferra PUROSANGUE crypter.",
          source_organization="LastPass", source_team="TIME + Delphos Labs", source_title=LP_TITLE, source_url=LP,
          published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="Moderate",
          evidence_tags="track:BoryptGrab-lineage|track:cruciferra|RAP-H-CRY", notes="Lineage OPEN. Crypter capability attribution must not auto-credit stealer authors."),
    claim(claim_id="RAP-CLAIM-0012", family="Rapuncel", case_id="RAP",
          claim="OBSERVED 2026-09-19 (pk-sharma UK vantage): GitHub orgs LastPass-Authenticator and LastPass-S, portal lastpass-authenticator.github.io, and Pages redirect accounts return HTTP 404.",
          source_organization="P.K. Sharma", source_team="", source_title="GitHub removed the fake LastPass repositories. Four of the six Rapuncel domains still resolve",
          source_url=PK, published="2026-09-19", source_type="INDEPENDENT_CORROBORATION", status="CORROBORATED", confidence="High",
          independently_verified="false", evidence_tags="track:infra|GitHub/SEO|OBSERVED-by-author",
          notes="ETW did not independently re-check; treat as author's OBSERVED. NOT an ETW OBSERVED claim."),
    claim(claim_id="RAP-CLAIM-0013", family="Rapuncel", case_id="RAP",
          claim="OBSERVED 2026-09-19 resolver check: 4 of 6 campaign domains still resolve (hanselarinmusky, zaffersnouty, istatlmenus, macperformancetools); albinofennel and icansamyope NXDOMAIN on tested resolvers. Resolving ≠ malicious/C2-active.",
          source_organization="P.K. Sharma", source_title="GitHub removed the fake LastPass repositories. Four of the six Rapuncel domains still resolve",
          source_url=PK, published="2026-09-19", source_type="INDEPENDENT_CORROBORATION", status="CORROBORATED", confidence="High",
          independently_verified="false", evidence_tags="track:infra|DNS|RESOLVING-not-MALICIOUS",
          notes="Preserve exact observation. Do NOT paraphrase as 'four C2 active'."),
    claim(claim_id="RAP-CLAIM-0014", family="Rapuncel", case_id="RAP",
          claim="BoryptGrab (Trend Micro Mar 2026) uses SEO fake GitHub + GitHub Pages delivery, oversized ZIPs, browser/wallet collection; includes passathook-cs2 lure names; NOT a Rapuncel IOC source.",
          source_organization="Trend Micro", source_title="New BoryptGrab Stealer Targets Windows Users via Deceptive GitHub Pages",
          source_url=TM, published="2026-03-05", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="track:BoryptGrab-lineage|comparator-only", notes="Case isolation: BoryptGrab IOCs stay in comparator track only."),
    claim(claim_id="RAP-CLAIM-0015", family="Rapuncel", case_id="RAP",
          claim="Recorded Future lists Cruciferra crypter service (since ~Oct 2025) with Shared Cruciferra ~$145/mo; AV-Killer PUROSANGUE ~$2000/mo (pricing may vary by source); Coconut single EXE ~$500/mo — commodity crypting marketplace.",
          source_organization="Recorded Future", source_title="Malware Crypting Services Used by Threat Actors",
          source_url=RF, published="UNKNOWN", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="Moderate",
          evidence_tags="track:cruciferra|MaaS|pricing", notes="Pricing figures differ across eSentire/RF — record per-source; do not merge."),
    claim(claim_id="RAP-CLAIM-0016", family="Rapuncel", case_id="RAP",
          claim="Hypothesis RAP-H-CRY: Rapuncel infection-chain layers (1) distribution/MaaS GitHub-SEO (2) Cruciferra/PUROSANGUE loader/crypter (sideload, AV kill, file pumping, UAC bypass) (3) Rapuncel stealer payload — may involve different operators; do not assume unity.",
          source_organization="Emerging Threat Watch", source_title="Internal hypothesis RAP-H-CRY",
          source_url="investigations/rapuncel/docs/research-tracks.md", published="2026-09-19",
          source_type="UNVERIFIED", status="INFERRED", confidence="Low",
          evidence_tags="track:cruciferra|RAP-H-CRY|ecosystem", notes="Analytical model only."),
    claim(claim_id="RAP-CLAIM-0017", family="Rapuncel", case_id="RAP",
          claim="User-seeded SHA-256 hashes (ea8c31a86fa785ab...; aefbc6e04320e9a0...; 611b3ba687b7f463...; 26db14b956e33f69...; 75018b06c7105a1d...) remain UNVERIFIED until located in SOURCE-RAP-001 primary body.",
          source_organization="ETW seed", source_title="User seed hashes", source_url="UNVERIFIED",
          published="UNKNOWN", source_type="UNVERIFIED", status="UNVERIFIED", confidence="Low",
          evidence_tags="track:hashes|UNVERIFIED", notes="Do not invent primary URLs for hashes."),
    claim(claim_id="RAP-CLAIM-0018", family="Rapuncel", case_id="RAP",
          claim="BleepingComputer secondary (2026-09-18) summarizes LastPass/Delphos Rapuncel findings including vsdbg sideload, Alinubx 145-process kill, exfil 2.26.126.50, Cruciferra PUROSANGUE, moderate BoryptGrab assessment — derives_from SOURCE-RAP-001; not independent corroboration.",
          source_organization="BleepingComputer", source_team="Bill Toulas", source_title="Fake LastPass Authenticator GitHub repos push new Rapuncel infostealer",
          source_url=BC, published="2026-09-18", source_type="SECONDARY", status="SECONDARY", confidence="Moderate",
          derives_from="SOURCE-RAP-001", evidence_tags="track:secondary-lineage"),
]

# --- SETTRA ---
CY1 = "https://www.cynet.com/blog/inside-cynets-settra-ransomware-investigation/"
CY2 = "https://www.cynet.com/settra-ransomware-inside-a-new-enterprise-grade-extortion-threat/"
HU = "https://www.huntress.com/blog/new-settra-ransomware-variant"
MX = "https://www.moxfive.com/blog/settra-ransomware-ttps-victims-and-defense-guide"

set_claims = [
    claim(claim_id="SET-CLAIM-0001", family="Settra", case_id="SET",
          claim="Settra outer loader is password-gated (--pass); ~200k SHA-256 KDF → AES-256-CTR decrypt of ~1.4MB blob → LP77 decompress → process hollowing; missing/wrong password or debugger yields benign-looking exit.",
          source_organization="Cynet", source_team="CyOps Research Labs", source_title="Inside Cynet's Settra Ransomware Investigation",
          source_url=CY1, published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="encryptor|loader|anti-analysis"),
    claim(claim_id="SET-CLAIM-0002", family="Settra", case_id="SET",
          claim="Inner encryptor has no exfil stack (no WinHTTP/WinINet upload); network limited to SMB for encryption; ransom-note data-theft claims are not implemented inside encryptor binary.",
          source_organization="Cynet", source_team="CyOps Research Labs", source_title=CY1.split("/")[-2],
          source_url=CY1, published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="encryptor|no-exfil|extortion-narrative"),
    claim(claim_id="SET-CLAIM-0003", family="Settra", case_id="SET",
          claim="Per-file symmetric keys wrapped with embedded 4096-bit RSA public key; private key never on host; offline encryption possible without C2 during encrypt phase; extensions .locked / intermediate .locked_wip.",
          source_organization="Cynet", source_team="CyOps Research Labs", source_title="Settra Ransomware: Inside a New Enterprise-Grade Extortion Threat",
          source_url=CY2, published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="encryptor|crypto"),
    claim(claim_id="SET-CLAIM-0004", family="Settra", case_id="SET",
          claim="Pre-encryption: Hyper-V VM power-off via WMI; WinRE disable; backup/restore destruction; VSS resize to purge shadows; clear ~12 event logs; Prefetch/PS history/USN wipe; Restart Manager terminate holders.",
          source_organization="Cynet", source_team="CyOps Research Labs", source_title="Settra long-form",
          source_url=CY2, published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="encryptor|recovery-destruction|anti-forensics"),
    claim(claim_id="SET-CLAIM-0005", family="Settra", case_id="SET",
          claim="Operators in Huntress-investigated Settra-associated intrusions deployed MeshAgent RMM (July: mvtcs.exe → 45.13.122.7; Sept: MeshAgent → 193.5.65.114); ransomware named <domain>_win64.exe.",
          source_organization="Huntress", source_team="Harlan Carvey / Lindsey O'Donnell-Welch",
          source_title="Ready, Settra, Go: New Settra Ransomware Variant Deploys MeshAgent RMM",
          source_url=HU, published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="operator-activity|RMM|MeshAgent", notes="Never phrase as 'Settra malware uses MeshAgent' — operator intrusion TTP."),
    claim(claim_id="SET-CLAIM-0006", family="Settra", case_id="SET",
          claim="Huntress Sept incident: gdrv.sys BYOVD observed; encrypted extension .locked_wip; ransom note RESTORE_FILES.txt; Defender log clear attempt misspelled (Microsoft-Windows-Defender/Operational vs correct Microsoft-Windows-Windows-Defender/Operational) so Defender log not cleared.",
          source_organization="Huntress", source_title="Ready, Settra, Go",
          source_url=HU, published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="operator-activity|BYOVD|contradiction-typo"),
    claim(claim_id="SET-CLAIM-0007", family="Settra", case_id="SET",
          claim="Workstation name WIN-LIVFRVQFMKO associated with Huntress Sept Settra incident and prior Huntress incidents back to 2024-12-24; also linked to 193.5.65.114 since ~2025-11. Hostname alone does not prove Settra-unique attribution.",
          source_organization="Huntress", source_title="Ready, Settra, Go",
          source_url=HU, published="2026-09-17", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="Moderate",
          evidence_tags="WIN-LIVFRVQFMKO|infra-mystery", notes="See win-livfrvqfmko.md — multi-campaign hostname reuse documented elsewhere (Sophos)."),
    claim(claim_id="SET-CLAIM-0008", family="Settra", case_id="SET",
          claim="MOXFIVE casework: operators in Settra-associated intrusions used compromised VPN credentials, NetExec/Netscan, ProcDump/Mimikatz, PAExec, edr_blind, STProcessMonitor_v114.sys BYOVD, Mesh Agent — dual-use tools, not Settra.exe features.",
          source_organization="MOXFIVE", source_team="Luke Moran", source_title="Settra Ransomware: TTPs, Victims, and Defense Guide",
          source_url=MX, published="UNKNOWN", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="operator-activity|dual-use", notes="Distinguish operator tools from encryptor."),
    claim(claim_id="SET-CLAIM-0009", family="Settra", case_id="SET",
          claim="SET-H1..H5 operator-model hypotheses remain OPEN; default SET-H5 insufficient evidence to choose RaaS multi-affiliate vs small team vs access-broker model. Leak-site volume (SET-H4) unvalidated by ETW.",
          source_organization="Emerging Threat Watch", source_title="operator-model-hypotheses.md",
          source_url="investigations/settra/docs/operator-model-hypotheses.md", published="2026-09-19",
          source_type="UNVERIFIED", status="INFERRED", confidence="Low",
          evidence_tags="operator-model|SET-H5"),
]

# --- RATHAT ---
ZI = "https://zimperium.com/blog/rathat-ai-powered-mobile-threat-is-here-for-your-credentials-bank-accounts"
TP = "https://zimperium.com/blog/the-toxicpanda-never-sleeps-toxicpanda-2-0-prepares-its-next-strike-on-mobile"
RH = "https://www.group-ib.com/blog/redhook-android-rat-upgraded/"

rat_claims = [
    claim(claim_id="RAT-CLAIM-0001", family="RatHat", case_id="RAT",
          claim="RatHat three-component architecture: Android app (Accessibility orchestration) + Go agent liblocal-service.so + FRP client libmedia_codec.so.",
          source_organization="Zimperium", source_team="zLabs", source_title="RatHat: AI-Powered Mobile Threat...",
          source_url=ZI, published="2026-09-16", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="architecture|three-component"),
    claim(claim_id="RAT-CLAIM-0002", family="RatHat", case_id="RAT",
          claim="SystemHelperService uses Accessibility to unlock Developer Options, enable Wireless Debugging, scrape pairing code/port, then libadb-android self-pairs to local ADB for shell UID 2000.",
          source_organization="Zimperium", source_team="zLabs", source_title="RatHat",
          source_url=ZI, published="2026-09-16", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="self-ADB|Accessibility|privileged-agent"),
    claim(claim_id="RAT-CLAIM-0003", family="RatHat", case_id="RAT",
          claim="After APK uninstall, Go local-service outside package lifecycle can reinstall APK and re-enable Accessibility via pm install / settings put — application persistence ≠ privileged-agent persistence ≠ FRP remote-connectivity persistence.",
          source_organization="Zimperium", source_team="zLabs", source_title="RatHat",
          source_url=ZI, published="2026-09-16", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="persistence-taxonomy|privileged-agent"),
    claim(claim_id="RAT-CLAIM-0004", family="RatHat", case_id="RAT",
          claim="Hardware-input keylogging: Go agent AdbTouchCapture uses getevent on /dev/input/* + locateValues.json keypad geometry to reconstruct PIN/pattern — distinct from Accessibility text-event keylogging.",
          source_organization="Zimperium", source_team="zLabs", source_title="RatHat",
          source_url=ZI, published="2026-09-16", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="hardware-input|getevent|keylogging"),
    claim(claim_id="RAT-CLAIM-0005", family="RatHat", case_id="RAT",
          claim="Generative AI UI automation: Accessibility tree serialized to XML sent to popular GenAI assistant for coordinate/text/scroll resolution — investigate what is AI-delegated vs deterministic Accessibility workflows; do not sensationalize 'AI malware'.",
          source_organization="Zimperium", source_team="zLabs", source_title="RatHat",
          source_url=ZI, published="2026-09-16", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="Moderate",
          evidence_tags="AI-UI|careful-wording"),
    claim(claim_id="RAT-CLAIM-0006", family="RatHat", case_id="RAT",
          claim="Anti-analysis: container ZIP tamper, 61MB Manifest bomb (0x9999 chunks), DEX bytecode poisoning, dual string encryption, six anti-debug checks (JDWP/ptrace/Frida/Xposed/root/emulator).",
          source_organization="Zimperium", source_team="zLabs", source_title="RatHat",
          source_url=ZI, published="2026-09-16", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="anti-analysis"),
    claim(claim_id="RAT-CLAIM-0007", family="RatHat", case_id="RAT",
          claim="TECHNIQUE COMPARISON ONLY (not lineage): ToxicPanda 2.0 and RedHook also implement Accessibility-driven Wireless ADB self-pairing to shell — suggests reusable design pattern / OS-feature trust-surface, not shared authorship.",
          source_organization="Emerging Threat Watch", source_title="adb-technique-comparison.md",
          source_url="investigations/rathat/docs/adb-technique-comparison.md", published="2026-09-19",
          source_type="UNVERIFIED", status="INFERRED", confidence="Moderate",
          evidence_tags="COMMON_TECHNIQUE|ADB|ToxicPanda|RedHook", notes="Case isolation: no IOC transfer. Sources: Zimperium ToxicPanda; Group-IB RedHook."),
]

# --- NODERABBIT ---
KS = "https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/"

nrb_claims = [
    claim(claim_id="NRB-CLAIM-0001", family="NodeRabbit", case_id="NRB",
          claim="Kaspersky attributes NodeRabbit/PollCat activity to Mirage Kitten with high confidence (Kaspersky's assessment). ETW does not independently establish attribution. Aliases UNC1549/Smoke Sandstorm/Nimbus Manticore researched but not auto-equated by ETW.",
          source_organization="Kaspersky", source_team="GReAT", source_title="Mirage Kitten targeting aviation and FinTech...",
          source_url=KS, published="2026-09-01", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="attribution-KASPERSKY|Mirage-Kitten", notes="Report as THEIR attribution."),
    claim(claim_id="NRB-CLAIM-0002", family="NodeRabbit", case_id="NRB",
          claim="Delivery via fake recruiter coding-challenge ZIPs on S3 with trojanized local npm packages colorized_terminal / pretty-log v2.1.0 (not npm registry).",
          source_organization="Kaspersky", source_team="GReAT", source_title="Mirage Kitten NodeRabbit",
          source_url=KS, published="2026-09-01", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="social-engineering|developer|npm-local"),
    claim(claim_id="NRB-CLAIM-0003", family="NodeRabbit", case_id="NRB",
          claim="Three NodeRabbit variants: V1 fixed port 48739 + EdgeUpdate persistence + 11 cmds; V2 anti-analysis decoy HEAD + proxy/PAC/NTLM via curl --proxy-anyauth + host-derived port 41984-46983 + Intel DSA persistence; V3 new /sdk/v2 C2 API + 23 cmds including Outlook, VS Code, Git hooks, agent:servers.",
          source_organization="Kaspersky", source_team="GReAT", source_title="Mirage Kitten NodeRabbit",
          source_url=KS, published="2026-09-01", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="evolution|V1-V2-V3|enterprise-proxy"),
    claim(claim_id="NRB-CLAIM-0004", family="NodeRabbit", case_id="NRB",
          claim="V3 persist:vscode installs fake VS Code extension displayed as 'GitHub Copilot Helper' borrowing trusted publisher name from local metadata WITHOUT copying signature/trusted status; may disable Workspace Trust.",
          source_organization="Kaspersky", source_team="GReAT", source_title="Mirage Kitten NodeRabbit",
          source_url=KS, published="2026-09-01", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="VS-Code|developer-persistence|brand-trust"),
    claim(claim_id="NRB-CLAIM-0005", family="NodeRabbit", case_id="NRB",
          claim="V3 Git hook injection appends marked launcher (# shepherd-persist) to post-merge/post-checkout — LOCAL persistence on developer workstation; hooks normally not committed — do NOT call supply-chain propagation without evidence.",
          source_organization="Kaspersky", source_team="GReAT", source_title="Mirage Kitten NodeRabbit",
          source_url=KS, published="2026-09-01", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="Git-hooks|local-persistence|NOT-supply-chain"),
    claim(claim_id="NRB-CLAIM-0006", family="NodeRabbit", case_id="NRB",
          claim="agent:servers can replace in-memory C2 list and write .sv.json — static domain IOCs have limited durability vs behavioral detection of NodeRabbit command protocol / persistence paths.",
          source_organization="Kaspersky", source_team="GReAT", source_title="Mirage Kitten NodeRabbit",
          source_url=KS, published="2026-09-01", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="C2-durability|behavioral-IOC"),
    claim(claim_id="NRB-CLAIM-0007", family="NodeRabbit", case_id="NRB",
          claim="PollCat is related per Kaspersky same investigation but kept under separate claim tags; do not merge PollCat IOCs into Rapuncel/Settra/RatHat.",
          source_organization="Kaspersky", source_team="GReAT", source_title="Mirage Kitten NodeRabbit",
          source_url=KS, published="2026-09-01", source_type="PRIMARY", status="PRIMARY_SOURCE", confidence="High",
          evidence_tags="PollCat|case-isolation"),
]


def main():
    wcsv(ROOT / "investigations/rapuncel/claims/claims-ledger.csv", CLAIM_FIELDS, rap_claims)
    wcsv(ROOT / "investigations/settra/claims/claims-ledger.csv", CLAIM_FIELDS, set_claims)
    wcsv(ROOT / "investigations/rathat/claims/claims-ledger.csv", CLAIM_FIELDS, rat_claims)
    wcsv(ROOT / "investigations/noderabbit/claims/claims-ledger.csv", CLAIM_FIELDS, nrb_claims)

    # Settra dual ATT&CK matrices
    atk_fields = ["matrix", "tactic", "technique_id", "technique_name", "behavior_summary", "actor_framing", "evidence_source", "confidence", "notes"]
    malware_rows = [
        {"matrix": "settra-malware", "tactic": "Defense Evasion", "technique_id": "T1622", "technique_name": "Debugger Evasion",
         "behavior_summary": "Outer loader exits on BeingDebugged / missing --pass", "actor_framing": "Settra encryptor/loader behavior",
         "evidence_source": CY2, "confidence": "High", "notes": "Cynet RE"},
        {"matrix": "settra-malware", "tactic": "Defense Evasion", "technique_id": "T1027", "technique_name": "Obfuscated Files or Information",
         "behavior_summary": "Encrypted 1.4MB blob; XOR string obfuscation in inner PE", "actor_framing": "Settra encryptor/loader behavior",
         "evidence_source": CY2, "confidence": "High", "notes": ""},
        {"matrix": "settra-malware", "tactic": "Defense Evasion", "technique_id": "T1055.012", "technique_name": "Process Hollowing",
         "behavior_summary": "Hollow suspended self-copy after LP77 inflate", "actor_framing": "Settra encryptor/loader behavior",
         "evidence_source": CY2, "confidence": "High", "notes": ""},
        {"matrix": "settra-malware", "tactic": "Impact", "technique_id": "T1486", "technique_name": "Data Encrypted for Impact",
         "behavior_summary": "AES/CNG per-file encrypt; RSA-4096 wrap; .locked", "actor_framing": "Settra encryptor behavior",
         "evidence_source": CY2, "confidence": "High", "notes": ""},
        {"matrix": "settra-malware", "tactic": "Impact", "technique_id": "T1490", "technique_name": "Inhibit System Recovery",
         "behavior_summary": "reagentc/bcdedit/wbadmin/VSS resize/Hyper-V shutdown", "actor_framing": "Settra encryptor behavior",
         "evidence_source": CY2, "confidence": "High", "notes": ""},
        {"matrix": "settra-malware", "tactic": "Defense Evasion", "technique_id": "T1070.001", "technique_name": "Clear Windows Event Logs",
         "behavior_summary": "wevtutil clear of ~12 channels (embedded)", "actor_framing": "Settra encryptor behavior",
         "evidence_source": CY2, "confidence": "High", "notes": "Huntress notes Defender channel typo in observed clear list"},
        {"matrix": "settra-malware", "tactic": "Impact", "technique_id": "T1489", "technique_name": "Service Stop",
         "behavior_summary": "Restart Manager terminates processes holding files", "actor_framing": "Settra encryptor behavior",
         "evidence_source": CY1, "confidence": "High", "notes": ""},
    ]
    op_rows = [
        {"matrix": "settra-operator", "tactic": "Initial Access", "technique_id": "T1078", "technique_name": "Valid Accounts",
         "behavior_summary": "Compromised VPN / valid credentials", "actor_framing": "Operators in Settra-associated intrusions",
         "evidence_source": MX, "confidence": "High", "notes": "MOXFIVE casework; Huntress did not confirm IA"},
        {"matrix": "settra-operator", "tactic": "Discovery", "technique_id": "T1046", "technique_name": "Network Service Discovery",
         "behavior_summary": "NetExec / Netscan", "actor_framing": "Operators in Settra-associated intrusions",
         "evidence_source": MX, "confidence": "High", "notes": "Dual-use tool"},
        {"matrix": "settra-operator", "tactic": "Credential Access", "technique_id": "T1003", "technique_name": "OS Credential Dumping",
         "behavior_summary": "ProcDump / Mimikatz observed", "actor_framing": "Operators in Settra-associated intrusions",
         "evidence_source": MX, "confidence": "High", "notes": "NOT 'Settra uses Mimikatz'"},
        {"matrix": "settra-operator", "tactic": "Lateral Movement", "technique_id": "T1021.002", "technique_name": "SMB/Windows Admin Shares",
         "behavior_summary": "PAExec / NetExec lateral", "actor_framing": "Operators in Settra-associated intrusions",
         "evidence_source": MX, "confidence": "High", "notes": ""},
        {"matrix": "settra-operator", "tactic": "Defense Evasion", "technique_id": "T1562.001", "technique_name": "Disable or Modify Tools",
         "behavior_summary": "edr_blind; BYOVD STProcessMonitor_v114.sys (MOXFIVE); gdrv.sys (Huntress Sept)", "actor_framing": "Operators in Settra-associated intrusions",
         "evidence_source": f"{MX} | {HU}", "confidence": "High", "notes": "Different drivers across sources"},
        {"matrix": "settra-operator", "tactic": "Command and Control", "technique_id": "T1219", "technique_name": "Remote Access Software",
         "behavior_summary": "Mesh Agent / MeshAgent RMM", "actor_framing": "Operators in Settra-associated intrusions",
         "evidence_source": f"{MX} | {HU}", "confidence": "High", "notes": "Legitimate RMM trust surface"},
        {"matrix": "settra-operator", "tactic": "Impact", "technique_id": "T1486", "technique_name": "Data Encrypted for Impact",
         "behavior_summary": "Deploy domain_win64.exe Settra encryptor", "actor_framing": "Operators deploy Settra encryptor",
         "evidence_source": HU, "confidence": "High", "notes": "Bridge to malware matrix"},
    ]
    wcsv(ROOT / "investigations/settra/attack/settra-malware-matrix.csv", atk_fields, malware_rows)
    wcsv(ROOT / "investigations/settra/attack/settra-operator-activity-matrix.csv", atk_fields, op_rows)

    # Browser target matrix RatHat
    br_fields = ["browser", "package", "resource_id", "URL_collection", "credential_collection", "overlay_target", "evidence_source", "confidence"]
    browsers = [
        ("Chrome", "com.android.chrome", "com.android.chrome:id/url_bar", "yes", "via Accessibility/overlays", "banking overlays separate", ZI, "High"),
        ("Brave", "com.brave.browser", "com.brave.browser:id/url_bar", "yes", "via Accessibility", "unknown", ZI, "High"),
        ("Opera", "com.opera.browser", "com.opera.browser:id/url_field", "yes", "via Accessibility", "unknown", ZI, "High"),
        ("Opera Mini", "com.opera.mini.native", "com.opera.mini.native:id/url_field", "yes", "via Accessibility", "unknown", ZI, "High"),
        ("Edge", "com.microsoft.emmx", "com.microsoft.emmx:id/url_bar", "yes", "via Accessibility", "unknown", ZI, "High"),
        ("DuckDuckGo", "com.duckduckgo.mobile.android", "com.duckduckgo.mobile.android:id/omnibarTextInput", "yes", "via Accessibility", "unknown", ZI, "High"),
        ("Samsung Internet", "com.sec.android.app.sbrowser", "com.sec.android.app.sbrowser:id/location_bar_edit_text", "yes", "via Accessibility", "unknown", ZI, "High"),
        ("AOSP/ColorOS browsers", "varies", "per Zimperium list", "yes", "via Accessibility", "unknown", ZI, "Moderate"),
        ("WeChat/Alipay (payment)", "payment apps", "N/A-overlay", "no", "PIN overlays embedded", "yes", ZI, "High"),
        ("Banking apps (generic)", "targeted packages", "N/A-HTML injection", "no", "WebView overlay injection", "yes", ZI, "High"),
    ]
    br_rows = [dict(zip(br_fields, b)) for b in browsers]
    wcsv(ROOT / "investigations/rathat/analysis/browser-target-matrix.csv", br_fields, br_rows)

    # Trust surface matrix
    ts_fields = [
        "family", "stage", "component", "trust_class", "legitimate_purpose", "abuse_method",
        "vuln_vs_intended", "privilege_boundary", "why_detection_trusts_it", "remaining_telemetry",
        "blocking_realism", "behavioral_detection_hook", "uniqueness", "seen_in_other_families_technique_only",
        "evidence_ids_or_claims", "comparison_confidence", "notes",
    ]
    ts = [
        {"family": "Rapuncel", "stage": "delivery", "component": "GitHub org/Pages + SEO ranking", "trust_class": "USER/BRAND TRUST",
         "legitimate_purpose": "Host/distribute open-source software", "abuse_method": "Fake brand orgs, fabricated badges, SEO",
         "vuln_vs_intended": "Intended platform features", "privilege_boundary": "User download decision",
         "why_detection_trusts_it": "github.com reputation / HTTPS", "remaining_telemetry": "Org verified badge; download referrer",
         "blocking_realism": "Hard to block GitHub wholesale", "behavioral_detection_hook": "Unverified org + Authenticator Windows lure",
         "uniqueness": "Common SEO/GitHub abuse class", "seen_in_other_families_technique_only": "BoryptGrab (comparator); not Settra/RatHat/NRB",
         "evidence_ids_or_claims": "RAP-CLAIM-0002|0003", "comparison_confidence": "High", "notes": "Technique class only"},
        {"family": "Rapuncel", "stage": "execution", "component": "vsdbg.exe (MS Visual Studio debugger)", "trust_class": "TRUSTED BINARY",
         "legitimate_purpose": "Debug CoreCLR apps", "abuse_method": "DLL sideload vsdbg.dll",
         "vuln_vs_intended": "Intended load-adjacent-DLL behavior", "privilege_boundary": "User→process",
         "why_detection_trusts_it": "Valid Microsoft Authenticode", "remaining_telemetry": "Module load of unexpected DLL; parent/child",
         "blocking_realism": "Allowlist apps not signatures", "behavioral_detection_hook": "vsdbg outside Visual Studio install path",
         "uniqueness": "Specific LOLBIN choice", "seen_in_other_families_technique_only": "Sideload class common; this binary not transferred",
         "evidence_ids_or_claims": "RAP-CLAIM-0006", "comparison_confidence": "High", "notes": "May be Cruciferra-supplied (RAP-H-CRY)"},
        {"family": "Rapuncel", "stage": "defense-evasion", "component": "Alinubx.sys / CcProtect WHCP-signed", "trust_class": "SIGNED DRIVER",
         "legitimate_purpose": "Third-party protect driver (CnCrypt)", "abuse_method": "Identity swap + kernel process kill",
         "vuln_vs_intended": "Abused capable signed driver (BYOVD-class)", "privilege_boundary": "Kernel",
         "why_detection_trusts_it": "WHCP signature; not on blocklist at pub", "remaining_telemetry": "Driver load; NvFsFilter service; signer Henan Dafeng",
         "blocking_realism": "HVCI/blocklist lag; hash rename defeats naive lists", "behavioral_detection_hook": "Kernel process terminate of security products",
         "uniqueness": "145-name list + WHCP path", "seen_in_other_families_technique_only": "Settra operators use different BYOVD drivers (technique class)",
         "evidence_ids_or_claims": "RAP-CLAIM-0007|0008", "comparison_confidence": "Moderate", "notes": "signed≠malicious≠blocklisted"},
        {"family": "Rapuncel", "stage": "crypter", "component": "Cruciferra PUROSANGUE/COCONUT", "trust_class": "OPEN-SOURCE DUAL-USE",
         "legitimate_purpose": "N/A — criminal crypting service", "abuse_method": "MaaS crypter wraps payloads",
         "vuln_vs_intended": "Commodity crimeware", "privilege_boundary": "Depends on build",
         "why_detection_trusts_it": "May inherit sideloaded legit host EXE trust", "remaining_telemetry": "Builder fingerprints; PUROSANGUE vs COCONUT artifacts",
         "blocking_realism": "Target infrastructure/panels if known", "behavioral_detection_hook": "File pumping + sideload + AV kill combo",
         "uniqueness": "Marketplace service", "seen_in_other_families_technique_only": "Unknown for other ETW families — do not invent",
         "evidence_ids_or_claims": "RAP-CLAIM-0011|0015|0016", "comparison_confidence": "Moderate", "notes": "First-class ecosystem object"},
        {"family": "Settra", "stage": "C2/persistence", "component": "MeshAgent RMM", "trust_class": "RMM",
         "legitimate_purpose": "IT remote management", "abuse_method": "Unauthorized deploy for hands-on access",
         "vuln_vs_intended": "Intended remote control", "privilege_boundary": "Admin equivalent",
         "why_detection_trusts_it": "Signed/legitimate RMM binary", "remaining_telemetry": "Unexpected MeshAgent; C2 IPs in cert/connections",
         "blocking_realism": "Allowlist approved RMM only", "behavioral_detection_hook": "New RMM in environment",
         "uniqueness": "Common ransomware precursor class", "seen_in_other_families_technique_only": "RMM abuse common; no cross-IOC",
         "evidence_ids_or_claims": "SET-CLAIM-0005", "comparison_confidence": "High", "notes": "Operator activity matrix"},
        {"family": "Settra", "stage": "defense-evasion", "component": "STProcessMonitor_v114.sys / gdrv.sys", "trust_class": "SIGNED DRIVER",
         "legitimate_purpose": "Vendor drivers with vulnerable primitives", "abuse_method": "BYOVD to blind EDR",
         "vuln_vs_intended": "Vulnerable signed drivers", "privilege_boundary": "Kernel",
         "why_detection_trusts_it": "Valid signature until blocklisted", "remaining_telemetry": "Driver install events",
         "blocking_realism": "Microsoft vulnerable driver blocklist", "behavioral_detection_hook": "Unexpected driver load pre-encryption",
         "uniqueness": "Driver choice differs by incident", "seen_in_other_families_technique_only": "BYOVD class also Rapuncel Alinubx — NOT same driver",
         "evidence_ids_or_claims": "SET-CLAIM-0006|0008", "comparison_confidence": "High", "notes": "Technique comparison only"},
        {"family": "Settra", "stage": "credential-access", "component": "Mimikatz / ProcDump", "trust_class": "SECURITY/DEBUGGING FEATURE",
         "legitimate_purpose": "Security research / dump debugging", "abuse_method": "LSASS credential theft",
         "vuln_vs_intended": "Intended tools misused", "privilege_boundary": "Admin",
         "why_detection_trusts_it": "Sometimes allowlisted in IT", "remaining_telemetry": "LSASS access",
         "blocking_realism": "Credential Guard; block tools", "behavioral_detection_hook": "LSASS handle access",
         "uniqueness": "Commodity", "seen_in_other_families_technique_only": "Common across ransomware ops",
         "evidence_ids_or_claims": "SET-CLAIM-0008", "comparison_confidence": "High", "notes": "Never 'Settra uses Mimikatz'"},
        {"family": "RatHat", "stage": "privilege", "component": "Accessibility Service", "trust_class": "OS FEATURE",
         "legitimate_purpose": "Assistive technology", "abuse_method": "UI automation for ADB enable + overlays",
         "vuln_vs_intended": "Intended powerful API", "privilege_boundary": "User-granted sensitive permission",
         "why_detection_trusts_it": "User consent dialog", "remaining_telemetry": "Accessibility enable events",
         "blocking_realism": "User education; MTD", "behavioral_detection_hook": "Accessibility + Developer Options toggles",
         "uniqueness": "Common Android malware class", "seen_in_other_families_technique_only": "ToxicPanda/RedHook same class",
         "evidence_ids_or_claims": "RAT-CLAIM-0002", "comparison_confidence": "High", "notes": "Trust-surface theme"},
        {"family": "RatHat", "stage": "privilege", "component": "Wireless ADB / adbd", "trust_class": "DEVELOPER TOOL",
         "legitimate_purpose": "App debugging without USB", "abuse_method": "Self-pair via Accessibility-scraped PIN",
         "vuln_vs_intended": "Intended debug feature", "privilege_boundary": "shell UID 2000",
         "why_detection_trusts_it": "Local loopback / developer mode", "remaining_telemetry": "Wireless debugging enable; pairing",
         "blocking_realism": "Enterprise: restrict developer options", "behavioral_detection_hook": "Accessibility→Wireless Debugging sequence",
         "uniqueness": "Emerging reusable pattern", "seen_in_other_families_technique_only": "ToxicPanda 2.0; RedHook — technique only",
         "evidence_ids_or_claims": "RAT-CLAIM-0002|0007", "comparison_confidence": "High", "notes": "NOT shared authorship"},
        {"family": "RatHat", "stage": "persistence-tunnel", "component": "frpc (fatedier/frp)", "trust_class": "OPEN-SOURCE DUAL-USE",
         "legitimate_purpose": "Expose local services via reverse proxy", "abuse_method": "Masqueraded libmedia_codec.so tunnel to C2",
         "vuln_vs_intended": "Intended tool", "privilege_boundary": "Network egress",
         "why_detection_trusts_it": "Known open-source binary patterns", "remaining_telemetry": "frp config fetch; unexpected native lib names",
         "blocking_realism": "Egress allowlists", "behavioral_detection_hook": "frpc + ADB exposure",
         "uniqueness": "Common dual-use", "seen_in_other_families_technique_only": "Unknown in other ETW cases — no transfer",
         "evidence_ids_or_claims": "RAT-CLAIM-0001", "comparison_confidence": "Moderate", "notes": ""},
        {"family": "NodeRabbit", "stage": "delivery", "component": "Amazon S3 coding-challenge ZIP", "trust_class": "CLOUD SERVICE",
         "legitimate_purpose": "Object storage", "abuse_method": "Host trojanized assessment archives",
         "vuln_vs_intended": "Intended hosting", "privilege_boundary": "User download/run",
         "why_detection_trusts_it": "AWS domain reputation", "remaining_telemetry": "S3 bucket names; recruiter lure context",
         "blocking_realism": "Hard to block S3 wholesale", "behavioral_detection_hook": "Unexpected S3 + npm local import",
         "uniqueness": "Mirage Kitten historical cloud lure hosting", "seen_in_other_families_technique_only": "Cloud lure hosting common",
         "evidence_ids_or_claims": "NRB-CLAIM-0002", "comparison_confidence": "High", "notes": ""},
        {"family": "NodeRabbit", "stage": "execution", "component": "Local Node.js / node.exe", "trust_class": "DEVELOPER TOOL",
         "legitimate_purpose": "Run JS apps", "abuse_method": "Launch implant; clone to nodew.exe / IntelDSA.exe GUI subsystem",
         "vuln_vs_intended": "Intended runtime", "privilege_boundary": "User",
         "why_detection_trusts_it": "Developer workstation normal", "remaining_telemetry": "node launching from AppData cache paths",
         "blocking_realism": "Low on developer endpoints", "behavioral_detection_hook": "node + hidden cache implant paths",
         "uniqueness": "Targets developers specifically", "seen_in_other_families_technique_only": "Living-off-the-land interpreters common",
         "evidence_ids_or_claims": "NRB-CLAIM-0003", "comparison_confidence": "High", "notes": "Developer beachhead theme"},
        {"family": "NodeRabbit", "stage": "persistence", "component": "VS Code extension host + Git hooks", "trust_class": "DEVELOPER TOOL",
         "legitimate_purpose": "IDE extensions; VCS hooks", "abuse_method": "Fake Copilot Helper; post-merge launcher",
         "vuln_vs_intended": "Intended extensibility", "privilege_boundary": "User/dev context",
         "why_detection_trusts_it": "Extensions/hooks expected on workstations", "remaining_telemetry": "Unsigned extension; shepherd-persist marker",
         "blocking_realism": "Extension allowlists; hook auditing", "behavioral_detection_hook": "Untrusted publisher name borrow",
         "uniqueness": "VS Code + Git combo in V3", "seen_in_other_families_technique_only": "Not observed in RAP/SET/RAT — no transfer",
         "evidence_ids_or_claims": "NRB-CLAIM-0004|0005", "comparison_confidence": "High", "notes": "Local hooks ≠ supply chain"},
        {"family": "NodeRabbit", "stage": "C2", "component": "Azure Websites / Cloudflare domains", "trust_class": "CLOUD SERVICE",
         "legitimate_purpose": "App hosting / CDN", "abuse_method": "Blend C2 into enterprise-allowed cloud",
         "vuln_vs_intended": "Intended hosting", "privilege_boundary": "Network",
         "why_detection_trusts_it": "Corporate allowlists for Azure", "remaining_telemetry": "Unusual azurewebsites paths; beacon timing",
         "blocking_realism": "Difficult; need behavioral", "behavioral_detection_hook": "/api/rabbit/* or /sdk/v2/* patterns",
         "uniqueness": "Kaspersky notes Azure+CF hallmark", "seen_in_other_families_technique_only": "Cloud C2 blend common",
         "evidence_ids_or_claims": "NRB-CLAIM-0003|0006", "comparison_confidence": "Moderate", "notes": "agent:servers reduces static IOC life"},
    ]
    wcsv(ROOT / "research/trust-surface-matrix.csv", ts_fields, ts)
    wcsv(ROOT / "intelligence/trust-surface-matrix.csv", ts_fields, ts)

    print("DONE seed")
    print(f"RAP claims={len(rap_claims)} SET={len(set_claims)} RAT={len(rat_claims)} NRB={len(nrb_claims)}")


if __name__ == "__main__":
    main()
