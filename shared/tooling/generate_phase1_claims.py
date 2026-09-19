#!/usr/bin/env python3
"""Generate Phase 1 claim ledgers and update key IOC status (local only)."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RET = "2026-09-19T18:00:00Z"
CUTOFF = "true"

HDR = [
    "claim_id", "family", "case_id", "claim", "source_organization", "source_team",
    "source_title", "source_url", "published", "source_type", "status", "confidence",
    "independently_verified", "evidence_tags", "related_evidence_ids", "derives_from",
    "notes", "retrieval_date_utc", "cutoff_applies",
]

RAP_URL = "https://blog.lastpass.com/posts/lastpass-delphos-report-rapuncel-infostealer"
RAP_TITLE = "Threat Intel | One Kit, Forty Companies: How a Malware-as-a-Service Platform Used GitHub as a Distribution Network for its Campaign"
ESE_URL = "https://www.esentire.com/blog/malware-as-a-service-cocktail-errtraffic-and-cruciferra-killing-your-edr-since-2025"
ESE_TITLE = "Malware-as-a-Service Cocktail: ErrTraffic and Cruciferra - Killing Your EDR Since 2025"
PK_URL = "https://www.pk-sharma.com/briefing/fake-lastpass-github-rapuncel-domains-still-resolve"
PK_TITLE = "GitHub removed the fake LastPass repositories. Four of the six Rapuncel domains still resolve"
TM_URL = "https://www.trendmicro.com/en_us/research/26/c/boryptgrab-stealer-targets-users-via-deceptive-github-pages.html"
CYN_URL = "https://www.cynet.com/blog/inside-cynets-settra-ransomware-investigation/"
CYN_TITLE = "Inside Cynet's Settra Ransomware Investigation"
HUN_URL = "https://www.huntress.com/blog/new-settra-ransomware-variant"
HUN_TITLE = "Ready, Settra, Go: New Settra Ransomware Variant Deploys MeshAgent RMM"
MOX_URL = "https://www.moxfive.com/blog/settra-ransomware-ttps-victims-and-defense-guide"
MOX_TITLE = "Settra Ransomware: TTPs, Victims, and Defense Guide"
ZIM_URL = "https://zimperium.com/blog/rathat-ai-powered-mobile-threat-is-here-for-your-credentials-bank-accounts"
ZIM_TITLE = "RatHat: AI-Powered Mobile Threat is Here for Your Credentials & Bank Accounts"
KAS_URL = "https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/"
KAS_TITLE = "Mirage Kitten targeting aviation and FinTech sectors across the Middle East and Africa with a new malware set"


def row(cid, family, case, claim, org, team, title, url, pub, stype, status, conf, verified, tags, evid, derives, notes):
    return {
        "claim_id": cid, "family": family, "case_id": case, "claim": claim,
        "source_organization": org, "source_team": team or "", "source_title": title,
        "source_url": url, "published": pub, "source_type": stype, "status": status,
        "confidence": conf, "independently_verified": "true" if verified else "false",
        "evidence_tags": tags, "related_evidence_ids": evid or "", "derives_from": derives or "",
        "notes": notes or "", "retrieval_date_utc": RET, "cutoff_applies": CUTOFF,
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HDR)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {path} ({len(rows)} claims)")


def rapuncel() -> list[dict]:
    o, t = "LastPass", "TIME + Delphos Labs"
    claims = [
        ("RAP-CLAIM-0001", "LastPass TIME discovered fraudulent GitHub org github.com/LastPass-Authenticator on 2026-08-13 that redirected to attacker infrastructure serving an installer.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "distribution|GitHub/SEO", "SOURCE-RAP-001", "", "Baseline discovery date."),
        ("RAP-CLAIM-0002", "Campaign impersonates at least 40 companies via SEO-optimized fraudulent GitHub organizations/repositories.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "distribution|GitHub/SEO|MaaS", "SOURCE-RAP-001", "", "LastPass lure is one of many."),
        ("RAP-CLAIM-0003", "Fake GitHub Pages portal displays fabricated trust signals including Authorized Access, VirusTotal Approved, and Secure Archive badges.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "distribution|brand-trust", "SOURCE-RAP-001", "", ""),
        ("RAP-CLAIM-0004", "Hidden redirect chain uses edgarcostartqd.github.io and dallikilic54.github.io via custom 404.html JavaScript waypoints.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "infrastructure|GitHub Pages", "SOURCE-RAP-001", "", ""),
        ("RAP-CLAIM-0005", "Cloudflare-fronted istatlmenus.com acts as dynamic traffic director via /mandua.wonted; content changed between 2026-08-27 and 2026-09-10.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "infrastructure", "SOURCE-RAP-001", "", "Runtime destination fetch."),
        ("RAP-CLAIM-0006", "Terminal domains macperformancetools.com and zaffersnouty.com were parked/redirecting at analysis time; both Cloudflare-fronted.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "infrastructure", "SOURCE-RAP-001", "", "RESOLVING/parked != serving malware."),
        ("RAP-CLAIM-0007", "Payload servers include albinofennel.com and hanselarinmusky.com; albinofennel served 40+ branded lure pages.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "infrastructure|MaaS", "SOURCE-RAP-001", "", ""),
        ("RAP-CLAIM-0008", "Observed ZIPs ~127.9–148 MB with junk TitanStorage.dll and ProManager.dll for scanner size-limit evasion.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "evasion|distribution", "SOURCE-RAP-001", "", ""),
        ("RAP-CLAIM-0009", "Installer is renamed Microsoft vsdbg.exe that DLL-sideloads malicious vsdbg.dll from the same folder.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "execution|DLL-sideload|trust-surface", "SOURCE-RAP-001", "", ""),
        ("RAP-CLAIM-0010", "vsdbg.dll SHA-256 ea8c31a86fa785ab514022c278a2f6e571c86aac9283745a96605c44d88382d6 is the NativeAOT loader.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "ioc|loader", "SOURCE-RAP-001", "", "Upgrades prior UNVERIFIED seed."),
        ("RAP-CLAIM-0011", "Rapuncel stealer SHA-256 aefbc6e04320e9a0e80f2323f8a897c4fdb222a37b0b87d76e850109decbfadd.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "ioc|stealer", "SOURCE-RAP-001", "", ""),
        ("RAP-CLAIM-0012", "Alinubx.sys SHA-256 611b3ba687b7f46319a19609605ddfe5225e6d85277d8e923eea3fdb6f7b5b61 is the kernel AV killer.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "ioc|driver|Alinubx", "SOURCE-RAP-001", "", "Also listed in eSentire Cruciferra IOC table as Alinubx.sys."),
        ("RAP-CLAIM-0013", "Browser injection DLL SHA-256 75018b06c7105a1dca391805d17b402aed35ebd515b92d461236eafbd606cb40.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "ioc|browser", "SOURCE-RAP-001", "", ""),
        ("RAP-CLAIM-0014", "ProtectR3.dll x64 unpacked SHA-256 26db14b956e33f69b3397a36387d32e01eb63613acff91069dc76b6ed7de45a8 present inside driver; injection not activated in this deployment.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "ioc|rootkit-helper", "SOURCE-RAP-001", "", "Capability present but unconfigured."),
        ("RAP-CLAIM-0015", "Alinubx dropped as nvfsflt64.sys / NvFsFilter NVIDIA-style service; terminates 145 AV/EDR process names via ObOpenObjectByPointer KernelMode + ZwTerminateProcess.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "driver|defense-evasion|PPL", "SOURCE-RAP-001", "", ""),
        ("RAP-CLAIM-0016", "Alinubx is identity-swapped CcProtect.sys (CnCrypt v1.32, Henan Dafeng); OriginalFilename changed; same kill IOCTL 0x222024 primitive.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "driver|CcProtect|BYOVD", "SOURCE-RAP-001", "", "signed/attested != safe."),
        ("RAP-CLAIM-0017", "Alinubx WHCP signature timestamp March 2023; VT 0/72 on 2026-08-20 (unchanged since 2025-07); not on MS vulnerable-driver blocklist at publication.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "driver|trust-chain", "SOURCE-RAP-001", "", ""),
        ("RAP-CLAIM-0018", "Delphos checked 18 public BYOVD drivers + CcProtect + Alinubx against DriverPolicy_Enforced.xml (2026-08-20): 0/20 SHA-256 matches.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "driver|blocklist-gap", "SOURCE-RAP-001", "", "Identity-based blocking limitation."),
        ("RAP-CLAIM-0019", "Delphos assesses with HIGH confidence vsdbg.dll was produced by Cruciferra PUROSANGUE or close derivative; string C:\\ExploitTests\\purosangue.tx present.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "track:cruciferra|loader|RAP-H-CRY", "SOURCE-RAP-001", "", "Do not credit stealer authors with crypter features."),
        ("RAP-CLAIM-0020", "Rapuncel collects 25+ browsers, 30+ wallets, Discord/Steam/Telegram, Credential Manager, password/seed/wallet/recovery docs, screenshots; exfils to 2.26.126.50 as HTTP-over-raw-TCP.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "stealer|c2", "SOURCE-RAP-001", "", "Loader/driver do not C2 in this deployment."),
        ("RAP-CLAIM-0021", "Browser ABE: injects helper into Chrome/Edge and calls Elevation Service DecryptData from inside browser process.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "browser|ABE", "SOURCE-RAP-001", "", "Prefer 'researchers reported' wording for bypass claims."),
        ("RAP-CLAIM-0022", "passathook-cs2 lure brand appears in both Rapuncel albinofennel URL data and Trend Micro BoryptGrab IOC file.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "lineage|BoryptGrab", "SOURCE-RAP-001", "", "Primary observed link."),
        ("RAP-CLAIM-0023", "Shared artifacts with BoryptGrab: UserInformation.txt BUILD NAME, installed_applications.txt, misspelled Filegraber directory, similar collection targets, Chrome Elevation Service workflow, oversized ZIP padding.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "Moderate", False, "lineage|BoryptGrab", "SOURCE-RAP-001", "", "Strong lineage signals; not byte-identical."),
        ("RAP-CLAIM-0024", "Delphos assesses Rapuncel is BoryptGrab-related variant/sibling with MODERATE confidence; insufficient evidence same campaign/operator; no shared C2; Alinubx absent from TM BoryptGrab reporting.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "Moderate", False, "lineage|BoryptGrab", "SOURCE-RAP-001", "", "Keep probabilistic."),
        ("RAP-CLAIM-0025", "LastPass systems/services/customer vaults were not compromised; GitHub is not an official LastPass Authenticator channel.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "scope", "SOURCE-RAP-001", "", ""),
        ("RAP-CLAIM-0026", "Driver broader features (file/registry hiding, ProtectR3 injection, WFP redirect) require Alinubx.ccf; not activated in this deployment.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "driver|capability-vs-active", "SOURCE-RAP-001", "", ""),
        ("RAP-CLAIM-0027", "MSRC (2026-08-19) said Alinubx behavior is not a Microsoft-owned vulnerability; directed to WDSI blocklist channel; still not blocklisted at publication.", "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "driver|disclosure", "SOURCE-RAP-001", "", ""),
        # Cruciferra independent
        ("RAP-CLAIM-0028", "eSentire: Cruciferra PUROSANGUE is sideloaded NativeAOT DLL package (~$1200/mo) with AV/EDR kill; COCONUT is standalone EXE (~$650/mo) with Defender exclusion.", "2026-08-19", "PRIMARY", "PRIMARY_SOURCE", "High", False, "track:cruciferra|PUROSANGUE|COCONUT", "SOURCE-RAP-ESE-001", "", "Independent of Rapuncel delivery."),
        ("RAP-CLAIM-0029", "eSentire: PUROSANGUE builder allows legitimate app sideload target, persistence, COM Elevation Moniker UAC bypass, AV/EDR kill, file pumping, custom process targets; default 145 AV/EDR names.", "2026-08-19", "PRIMARY", "PRIMARY_SOURCE", "High", False, "track:cruciferra|RAP-H-CRY", "SOURCE-RAP-ESE-001", "", "Matches Rapuncel 145 count."),
        ("RAP-CLAIM-0030", "eSentire Cruciferra sample used DCRCVDrv.sys BYOVD; Rapuncel campaign used Alinubx/CcProtect instead — same crypter class, different driver choice.", "2026-08-19", "PRIMARY", "PRIMARY_SOURCE", "High", False, "track:cruciferra|driver", "SOURCE-RAP-ESE-001", "SOURCE-RAP-001", "Supports RAP-H-CRY separation."),
        ("RAP-CLAIM-0031", "eSentire IOC table includes Alinubx.sys hash 611b3ba687b7f46319a19609605ddfe5225e6d85277d8e923eea3fdb6f7b5b61.", "2026-08-19", "PRIMARY", "CORROBORATED", "High", False, "ioc|Alinubx|track:cruciferra", "SOURCE-RAP-ESE-001", "SOURCE-RAP-001", "Independent listing of same hash."),
        # pk-sharma independent observation
        ("RAP-CLAIM-0032", "On 2026-09-19 from UK vantage: LastPass-Authenticator and LastPass-S GitHub orgs/pages return 404.", "2026-09-19", "INDEPENDENT_CORROBORATION", "PRIMARY_SOURCE", "High", False, "infrastructure|GitHub|OBSERVED-by-researcher", "SOURCE-RAP-PK-001", "", "Independent post-disclosure check."),
        ("RAP-CLAIM-0033", "On 2026-09-19: four of six report domains still resolved on some/all of 1.1.1.1,1.1.1.2,8.8.8.8,9.9.9.9; albinofennel.com and icansamyope.com NXDOMAIN all four.", "2026-09-19", "INDEPENDENT_CORROBORATION", "PRIMARY_SOURCE", "High", False, "infrastructure|dns", "SOURCE-RAP-PK-001", "", "RESOLVING != serving malware / C2 active."),
        ("RAP-CLAIM-0034", "istatlmenus.com and macperformancetools.com resolved on all four tested resolvers including malware-blocking resolvers.", "2026-09-19", "INDEPENDENT_CORROBORATION", "PRIMARY_SOURCE", "High", False, "infrastructure|dns", "SOURCE-RAP-PK-001", "", "Do not equate with active payload delivery."),
    ]
    out = []
    for c in claims:
        out.append(row(c[0], "Rapuncel", "RAP", c[1], o if c[0] < "RAP-CLAIM-0028" else ("eSentire" if c[0] < "RAP-CLAIM-0032" else "P.K. Sharma"),
                       t if c[0] < "RAP-CLAIM-0028" else ("TRU" if c[0] < "RAP-CLAIM-0032" else ""),
                       RAP_TITLE if c[0] < "RAP-CLAIM-0028" else (ESE_TITLE if c[0] < "RAP-CLAIM-0032" else PK_TITLE),
                       RAP_URL if c[0] < "RAP-CLAIM-0028" else (ESE_URL if c[0] < "RAP-CLAIM-0032" else PK_URL),
                       c[2], c[3], c[4], c[5], c[6], c[7], c[8], c[9] if len(c) > 9 else "", c[10] if len(c) > 10 else ""))
    # fix org/team for mixed - rebuild cleanly
    out = []
    for item in claims:
        cid = item[0]
        if cid.startswith("RAP-CLAIM-003"):
            if cid >= "RAP-CLAIM-0032":
                org, team, title, url = "P.K. Sharma", "", PK_TITLE, PK_URL
            else:
                org, team, title, url = "eSentire", "TRU", ESE_TITLE, ESE_URL
        elif cid >= "RAP-CLAIM-0028":
            org, team, title, url = "eSentire", "TRU", ESE_TITLE, ESE_URL
        else:
            org, team, title, url = o, t, RAP_TITLE, RAP_URL
        out.append(row(cid, "Rapuncel", "RAP", item[1], org, team, title, url, item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9] if len(item) > 9 else "", item[10] if len(item) > 10 else ""))
    return out


def settra() -> list[dict]:
    claims_spec = [
        ("SET-CLAIM-0001", "Cynet", "CyOps Research Labs", CYN_TITLE, CYN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "encryptor|anti-analysis", "", "Settra outer executable contains ~1.4 MB encrypted blob; without correct --pass the loader exits (may look inert to sandboxes).", ""),
        ("SET-CLAIM-0002", "Cynet", "CyOps", CYN_TITLE, CYN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "encryptor|password-gate", "", "Operator --pass derives key via ~200,000 SHA-256 iterations then AES-256-CTR decrypt; LP77 header validated; inner ransomware decompressed in memory.", "Password unlocks ransomware payload, not victim files."),
        ("SET-CLAIM-0003", "Cynet", "CyOps", CYN_TITLE, CYN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "encryptor|crypto", "", "Per-file symmetric keys wrapped with embedded 4096-bit RSA public key; private key never on victim; no C2 for keys during encryption.", "Offline encryption."),
        ("SET-CLAIM-0004", "Cynet", "CyOps", CYN_TITLE, CYN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "encryptor|no-exfil", "", "Reverse engineering found no file-exfiltration capability inside the encryptor (no WinHTTP/WinINet upload stack).", "Exfil is separate intrusion phase if it occurs."),
        ("SET-CLAIM-0005", "Cynet", "CyOps", CYN_TITLE, CYN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "encryptor|recovery-destruction", "", "Inner encryptor powers down Hyper-V VMs, disables WinRE/System Restore, shrinks VSS, clears logs/Prefetch/USN, uses Restart Manager.", ""),
        ("SET-CLAIM-0006", "Cynet", "CyOps", CYN_TITLE, CYN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "encryptor|anti-analysis", "", "Debugger detection and normal-looking exit codes can cause sandboxes to conclude nothing interesting happened.", ""),
        ("SET-CLAIM-0007", "Huntress", "", HUN_TITLE, HUN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "operator|IR|MeshAgent", "", "July incident: MeshAgent renamed mvtcs.exe to 45.13.122.7; ransomware from C:\\Perflogs; .locked; RESTORE_FILES.txt.", "Operator TTP not Settra.exe capability."),
        ("SET-CLAIM-0008", "Huntress", "", HUN_TITLE, HUN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "operator|IR|MeshAgent", "", "September incident: MeshAgent to 193.5.65.114; ransomware from Documents; .locked_wip; gdrv.sys BYOVD signals.", ""),
        ("SET-CLAIM-0009", "Huntress", "", HUN_TITLE, HUN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "operator|anti-forensics", "", "Embedded clear of Microsoft-Windows-Defender/Operational fails due to typo; correct is Microsoft-Windows-Windows-Defender/Operational.", "Defender artifact for defenders."),
        ("SET-CLAIM-0010", "Huntress", "", HUN_TITLE, HUN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "Moderate", False, "operator|WIN-LIVFRVQFMKO", "", "WIN-LIVFRVQFMKO associated with September Settra activity and prior Huntress incidents back to 2024-12-24; also linked to 193.5.65.114 since ~2025-11.", "Clustering signal; not attribution. Hostname also appears in unrelated historical campaigns (Sophos)."),
        ("SET-CLAIM-0011", "Huntress", "", HUN_TITLE, HUN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "High", False, "operator|naming", "", "Both incidents: ransomware named after victim domain + _win64.exe.", ""),
        ("SET-CLAIM-0012", "MOXFIVE", "", MOX_TITLE, MOX_URL, "2026-07-16", "PRIMARY", "PRIMARY_SOURCE", "High", False, "operator|intrusion-chain", "", "MOXFIVE IR observed VPN credential access → NetExec/Netscan → Procdump/Mimikatz → PAExec/NetExec → MeshAgent → edr_blind → STProcessMonitor_v114.sys BYOVD → Settra.", "Tools are operator TTPs."),
        ("SET-CLAIM-0013", "MOXFIVE", "", MOX_TITLE, MOX_URL, "2026-07-16", "PRIMARY", "INFERRED", "Low", False, "operator-model|SET-H2", "", "Batch leak-site postings and multi-day Tox response delays may indicate small operator set — interpretation not established fact.", "Keep as hypothesis SET-H2/H5."),
        ("SET-CLAIM-0014", "MOXFIVE", "", MOX_TITLE, MOX_URL, "2026-07-16", "PRIMARY", "PRIMARY_SOURCE", "Moderate", False, "extortion", "", "Double extortion via Tor leak site and Tox negotiations; financial motivation claimed by group.", "Leak-site claims != confirmed breaches."),
        ("SET-CLAIM-0015", "Huntress", "", HUN_TITLE, HUN_URL, "2026-09-17", "PRIMARY", "PRIMARY_SOURCE", "Moderate", False, "operator-model", "", "Huntress: nothing published stating Settra follows a RaaS model.", "Supports not asserting SET-H1."),
    ]
    # tuple: id, org, team, title, url, pub, stype, status, conf, verified, tags, _unused, claim, notes
    out = []
    for s in claims_spec:
        out.append(row(s[0], "Settra", "SET", s[12], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9], s[10], "", "", s[13]))
    return out


def rathat() -> list[dict]:
    specs = [
        ("RAT-CLAIM-0001", "Distributed via smishing, malvertising, phishing sites, third-party forums, malicious APK sideloading.", "delivery", ""),
        ("RAT-CLAIM-0002", "After Accessibility grant, automates Developer Options + Wireless Debugging; scrapes 6-digit pairing code and dynamic port; self-pairs via libadb-android.", "self-ADB|Accessibility", "No external computer required."),
        ("RAT-CLAIM-0003", "Three components: malicious APK; Go agent liblocal-service.so; FRP client libmedia_codec.so (frpc).", "architecture", ""),
        ("RAT-CLAIM-0004", "Go agent staged to /data/local/tmp; local HTTP on 127.0.0.1:7910; FRP reverse tunnel for remote ADB/shell access.", "persistence|C2", ""),
        ("RAT-CLAIM-0005", "APK uninstall != remediation: local-service outside package lifecycle can reinstall APK and re-enable Accessibility.", "persistence-taxonomy", "Privileged-agent persistence."),
        ("RAT-CLAIM-0006", "AI subsystem serializes Accessibility tree to XML and queries generative AI for target coordinates, on-screen text, and navigation (e.g. SCROLL_DOWN).", "AI-UI", "Investigate delegated vs deterministic logic; do not sensationalize."),
        ("RAT-CLAIM-0007", "Anti-analysis: ZIP tampering, ~61MB AndroidManifest with undocumented 0x9999 chunks, DEX poisoning, StringFog/StringCrypto, JDWP/ptrace/Frida/Xposed/root/emulator checks.", "anti-analysis", ""),
        ("RAT-CLAIM-0008", "Browser URL harvest resource IDs for Chrome, Brave, Opera, Opera Mini, Edge, DuckDuckGo, Samsung Internet, plus AOSP/ColorOS.", "browser-targets", ""),
        ("RAT-CLAIM-0009", "Hardware-level touch capture via getevent on /dev/input/* from shell UID; coordinates + known keypad geometry enable PIN reconstruction.", "hardware-input", "Distinct from Accessibility keylogging."),
        ("RAT-CLAIM-0010", "Credential channels include Accessibility text events, browser URL harvest, WebView overlays, SMS/notification OTP, MediaProjection, raw touch coordinates.", "credential-theft", "Multi-channel corroboration."),
        ("RAT-CLAIM-0011", "C2 uses HTTP register + WebSocket heartbeats with HMAC-SHA256; endpoints include /api/node/register and /api/data/credentials among others.", "C2", ""),
        ("RAT-CLAIM-0012", "zLabs links operators as appearing to operate in China; not a named APT attribution in this corpus.", "attribution", "Report as Zimperium assessment only."),
    ]
    out = []
    for s in specs:
        out.append(row(s[0], "RatHat", "RAT", s[1], "Zimperium", "zLabs", ZIM_TITLE, ZIM_URL, "2026-09-16", "PRIMARY", "PRIMARY_SOURCE", "High", False, s[2], "", "", s[3]))
    return out


def noderabbit() -> list[dict]:
    specs = [
        ("NRB-CLAIM-0001", "NodeRabbit is a cross-platform Node.js RAT (Windows/Linux/macOS) delivered via trojanized coding-challenge archives from fake recruiters on LinkedIn/job platforms.", "delivery|developer-targeting", ""),
        ("NRB-CLAIM-0002", "Front-Technical-Challenge.zip MD5 1EA83E4E4592B01E4ACAB63EB867BEE5 hosted on oracle-challenge.s3.us-east-1.amazonaws.com; README says server.js is bug-free and forbids AI assistants.", "social-engineering", ""),
        ("NRB-CLAIM-0003", "Trojanized local npm packages colorized_terminal and pretty-log v2.1.0 (bundled in node_modules, not npm registry) launch implant from node_modules/.cache/.320697f1/index.js.", "npm-abuse", ""),
        ("NRB-CLAIM-0004", "Three related variants found in Afghanistan, Egypt, Ethiopia with shared code lineage and progressive capability growth.", "evolution", ""),
        ("NRB-CLAIM-0005", "V1: 11 commands; AES-256-GCM C2; Azure endpoints plugplay/Rgbteller/Wslwebui; single-instance bind 127.0.0.1:48739.", "evolution|V1", ""),
        ("NRB-CLAIM-0006", "V2: sandbox/analyst checks; corporate proxy discovery (env, Internet Settings, PAC, HTTP CONNECT, Basic, curl --proxy-anyauth NTLM/Negotiate).", "evolution|V2|enterprise", "Enterprise developer environment hypothesis."),
        ("NRB-CLAIM-0007", "V3: 23 commands including agent:servers (replace C2 list, persist .sv.json); Outlook artifact discovery; persist:vscode; persist:project:inject Git hooks.", "evolution|V3", "Static IOC durability limited."),
        ("NRB-CLAIM-0008", "persist:vscode creates fake extension displayed as GitHub Copilot Helper; borrows publisher metadata without acquiring trusted signature/status; may interfere with Workspace Trust.", "VS-Code|detection", "Signature inconsistency detection opportunity."),
        ("NRB-CLAIM-0009", "Git persistence modifies .git/hooks/post-merge and post-checkout with # shepherd-persist marker; hooks are normally local and not committed — do not call supply-chain without evidence.", "Git-hooks", "Local persistence, not demonstrated propagation."),
        ("NRB-CLAIM-0010", "Kaspersky attributes activity to Mirage Kitten (aliases UNC1549/Smoke Sandstorm/Nimbus Manticore appear in industry tracking) targeting aviation/FinTech MEA.", "attribution", "Kaspersky assessment — not independently established by ETW."),
        ("NRB-CLAIM-0011", "Kaspersky detects as Trojan.JS.MirageKitten.*; first documented Node.js/JS malware for this cluster vs prior native DLL/Go tooling.", "attribution|tooling-shift", ""),
    ]
    out = []
    for s in specs:
        out.append(row(s[0], "NodeRabbit", "NRB", s[1], "Kaspersky", "GReAT", KAS_TITLE, KAS_URL, "2026-09-01", "PRIMARY", "PRIMARY_SOURCE", "High" if "attribution" not in s[2] or "independently" in s[3] else "Moderate", False, s[2], "", "", s[3]))
    # fix confidence for attribution
    for r in out:
        if "attribution" in r["evidence_tags"] and "NRB-CLAIM-0010" in r["claim_id"]:
            r["confidence"] = "Moderate"
            r["notes"] = (r["notes"] + " Report as Kaspersky's attribution.").strip()
    return out


def update_rap_hashes() -> None:
    path = ROOT / "investigations/rapuncel/iocs/hashes.csv"
    rows = list(csv.DictReader(path.open(encoding="utf-8")))
    for r in rows:
        r["source"] = "LastPass TIME / Delphos Labs primary report"
        r["confidence"] = "High"
        r["status"] = "HIGH_CONFIDENCE_MALICIOUS"
        r["notes"] = "Published SHA-256 in SOURCE-RAP-001 component table (2026-09-17). Independently_verified by ETW: false (metadata only)."
        r["first_seen"] = "2026-09-17"
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"updated {path}")


def update_rap_sources() -> None:
    path = ROOT / "investigations/rapuncel/evidence/source-index.csv"
    rows = [
        {"source_id": "SOURCE-RAP-001", "title": RAP_TITLE, "url": RAP_URL, "organization_or_author": "LastPass TIME / Delphos Labs", "publication_date": "2026-09-17", "retrieval_date": "2026-09-19", "source_tier": "PRIMARY", "case_ids": "rapuncel", "notes": "Authoritative baseline. Full page retrieved 2026-09-19."},
        {"source_id": "SOURCE-RAP-ESE-001", "title": ESE_TITLE, "url": ESE_URL, "organization_or_author": "eSentire TRU", "publication_date": "2026-08-19", "retrieval_date": "2026-09-19", "source_tier": "PRIMARY", "case_ids": "rapuncel", "notes": "Cruciferra/PUROSANGUE independent primary; track:cruciferra."},
        {"source_id": "SOURCE-RAP-PK-001", "title": PK_TITLE, "url": PK_URL, "organization_or_author": "P.K. Sharma", "publication_date": "2026-09-19", "retrieval_date": "2026-09-19", "source_tier": "INDEPENDENT_CORROBORATION", "case_ids": "rapuncel", "notes": "DNS/GitHub status only; RESOLVING!=malicious."},
        {"source_id": "SOURCE-RAP-TM-001", "title": "New BoryptGrab Stealer Targets Windows Users via Deceptive GitHub Pages", "url": TM_URL, "organization_or_author": "Trend Micro", "publication_date": "2026-03", "retrieval_date": "2026-09-19", "source_tier": "PRIMARY", "case_ids": "rapuncel", "notes": "Comparator lineage only — not Rapuncel IOCs."},
        {"source_id": "SOURCE-RAP-BC-001", "title": "Fake LastPass Authenticator GitHub repos push new Rapuncel infostealer", "url": "https://www.bleepingcomputer.com/news/security/fake-lastpass-authenticator-github-repos-push-new-rapuncel-infostealer/", "organization_or_author": "BleepingComputer", "publication_date": "2026-09-18", "retrieval_date": "2026-09-19", "source_tier": "SECONDARY", "case_ids": "rapuncel", "notes": "derives_from SOURCE-RAP-001"},
    ]
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"updated {path}")


def main() -> None:
    write_csv(ROOT / "investigations/rapuncel/claims/claims-ledger.csv", rapuncel())
    write_csv(ROOT / "investigations/settra/claims/claims-ledger.csv", settra())
    write_csv(ROOT / "investigations/rathat/claims/claims-ledger.csv", rathat())
    write_csv(ROOT / "investigations/noderabbit/claims/claims-ledger.csv", noderabbit())
    update_rap_hashes()
    update_rap_sources()


if __name__ == "__main__":
    main()
