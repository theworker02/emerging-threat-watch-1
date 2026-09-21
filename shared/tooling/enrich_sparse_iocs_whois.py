#!/usr/bin/env python3
"""Transcribe NEW network/hash IOCs from frozen primaries + RDAP/WHOIS ownership.

Passive only. Never invents IOCs. Skips values already present in package CSVs.
Case-isolates per family. Attribution stays metadata.
"""
from __future__ import annotations

import csv
import ipaddress
import json
import re
import subprocess
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PKG = ROOT / "reports/law-enforcement/packages"
INV = ROOT / "investigations"
OWN = ROOT / "intelligence/infra-ownership.csv"
EVID = ROOT / "evidence/primary-sources"

UA = "ETW-PassiveCollector/1.0 (defensive CTI; no C2 contact)"


def load_existing(path: Path) -> set[str]:
    if not path.exists():
        return set()
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return {(r.get("value") or "").strip().lower() for r in rows if r.get("value")}


def next_id(prefix: str, existing_rows: list[dict]) -> int:
    mx = 0
    for r in existing_rows:
        m = re.search(rf"{re.escape(prefix)}-IND-(\d+)", r.get("indicator_id") or "")
        if m:
            mx = max(mx, int(m.group(1)))
    return mx + 1


def read_rows(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_rows(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["indicator_id", "type", "value", "notes", "source"])
        w.writeheader()
        for r in rows:
            w.writerow(r)


def append_inds(pkg_dir: str, prefix: str, additions: list[tuple[str, str, str, str]]) -> int:
    """additions: (type, value, notes, source). Returns count added."""
    path = PKG / pkg_dir / "03_INDICATORS.csv"
    rows = read_rows(path)
    have = {(r.get("value") or "").strip().lower() for r in rows}
    n = next_id(prefix, rows)
    added = 0
    for typ, val, notes, source in additions:
        v = (val or "").strip()
        if not v or v.lower() in have:
            continue
        # skip obvious noise
        if typ == "domain" and not re.search(r"\.[a-z]{2,}$", v.lower()):
            continue
        if typ == "domain" and re.fullmatch(r"\d+\.\d+", v):
            continue
        rows.append(
            {
                "indicator_id": f"{prefix}-IND-{n:04d}",
                "type": typ,
                "value": v,
                "notes": notes,
                "source": source,
            }
        )
        have.add(v.lower())
        n += 1
        added += 1
    write_rows(path, rows)
    # mirror minimal inv combined
    fam = pkg_dir.split("-", 1)[1]
    inv_combined = INV / fam / "iocs" / "combined.csv"
    if inv_combined.parent.exists() or True:
        inv_combined.parent.mkdir(parents=True, exist_ok=True)
        write_rows(inv_combined, rows)
        # typed splits
        for t, fname in [("domain", "domains.csv"), ("ip", "domains.csv"), ("url", "urls.csv")]:
            pass
        hashes = [r for r in rows if r["type"] in ("md5", "sha1", "sha256")]
        domains = [r for r in rows if r["type"] in ("domain", "ip")]
        urls = [r for r in rows if r["type"] == "url"]
        write_rows(INV / fam / "iocs" / "hashes.csv", hashes)
        write_rows(INV / fam / "iocs" / "domains.csv", domains)
        write_rows(INV / fam / "iocs" / "urls.csv", urls)
    return added


def undefang(s: str) -> str:
    s = s.replace("[.]", ".").replace("(.)", ".")
    s = s.replace("hxxps://", "https://").replace("hxxp://", "http://")
    s = s.replace("[://]", "://")
    return s.strip().strip("`+").strip()


# --- curated NEW indicators (hand-verified from freezes / vendor IoC repos) ---

def curated() -> dict[str, list[tuple[str, str, str, str]]]:
    """pkg_dir -> list of (type, value, notes, source)"""
    PH = "Kaspersky Securelist (PhantomHeart RU freeze)"
    MK = "Kaspersky Securelist Mirage Kitten 2026-07-28"
    TAL = "Cisco Talos UAT-9244 IoC freeze (github-ioc/uat-9244.txt)"
    ABC = "Kaspersky Securelist ABCDoor"
    ESP = "ESET malware-ioc GitHub (promptspy)"
    ESG = "ESET malware-ioc GitHub (ghostchat)"
    ESH = "ESET malware-ioc GitHub (hybridpetya)"
    ESGOP = "ESET malware-ioc GitHub (gopherwhisper)"
    ESLN = "ESET malware-ioc GitHub (longnosedgoblin)"
    ESMW = "ESET malware-ioc GitHub (muddywater)"
    DOH = "Cisco Talos Dohdoor IoC freeze (github-ioc/dohdoor.txt)"
    FBI = "FBI FLASH HEAVYGRAM PDF 2026-09-15"
    GIB = "Group-IB HEAVYGRAM HTML freeze"
    U42 = "Unit 42 Screening Serpens freeze"
    PF = "Proofpoint TA585 MonsterV2 freeze"

    d: dict[str, list[tuple[str, str, str, str]]] = {}

    # PhantomHeart — 0 existing
    ph_ips = [
        "195.133.32.213",
        "31.56.227.61",
        "31.58.137.197",
        "31.56.48.178",
        "193.176.153.162",
        "188.127.254.233",
        "94.183.188.166",
        "80.66.81.13",
        "213.232.204.111",
        "31.56.227.100",
        "176.98.189.101",
        "178.255.127.65",
    ]
    ph_doms_c2 = [
        ("aegissecurity.online", "Head Mare / PhantomHeart related domain"),
        ("analytisec.space", "related domain"),
        ("brightshield.space", "related domain"),
        ("cryptara.online", "related domain"),
        ("cyberposi.space", "related domain"),
        ("cyvantis.online", "related domain"),
        ("defentry.online", "related domain"),
        ("fortisec.online", "related domain"),
        ("infoseon.online", "related domain"),
        ("msnetsec.space", "related domain"),
        ("netvion.online", "related domain"),
        ("nexaguard.space", "related domain"),
        ("safebloom.space", "related domain"),
        ("securafy.online", "related domain"),
        ("shieldora.online", "related domain"),
        ("unlikeu.org", "other relevant domain (article)"),
        ("hostinfo-service.info", "other relevant domain (article)"),
    ]
    # verify domain list from freeze opentip links only — pull clean list from HTML
    html = (EVID / "phantomheart/securelist-ru-phantomheart-2026.html").read_text(errors="ignore")
    otip_doms = sorted(
        {
            m.lower()
            for m in re.findall(r"opentip\.kaspersky\.com/([a-z0-9][a-z0-9.\-]{2,180}?)/", html, re.I)
            if "." in m
            and not re.match(r"^\d+\.\d+\.\d+\.\d+$", m)
            and not re.fullmatch(r"[a-f0-9]{32}", m, re.I)
        }
    )
    d["22-phantomheart"] = (
        [("ip", ip, "C2 / related IP (OpenTIP IoC list)", PH) for ip in ph_ips]
        + [("domain", dom, "related domain (OpenTIP IoC list)", PH) for dom in otip_doms]
        + [
            ("md5", m.lower(), "sample hash (OpenTIP)", PH)
            for m in re.findall(r"opentip\.kaspersky\.com/([a-f0-9]{32})/", html, re.I)
        ]
    )

    # Mirage Kitten — shared campaign net IOCs; tool-specific hashes
    mk_html = (EVID / "nightledger/securelist-mirage-kitten-nightledger-2026-07-28.html").read_text(
        errors="ignore"
    )
    mk_doms = sorted(
        {
            m.lower()
            for m in re.findall(r"opentip\.kaspersky\.com/([a-z0-9][a-z0-9.\-]{2,180}?)/", mk_html, re.I)
            if "." in m
            and not re.match(r"^\d+\.\d+\.\d+\.\d+$", m)
            and not re.fullmatch(r"[a-f0-9]{32}", m, re.I)
            and "kaspersky" not in m.lower()
        }
    )
    mk_net = [("ip", "172.86.98.113", "campaign IP (Domains and IPs section)", MK)] + [
        ("domain", x, "Mirage Kitten campaign shared infra (not tool-exclusive)", MK) for x in mk_doms
    ]
    d["57-nightledger"] = mk_net + [
        ("md5", "a239e655709a2518dd0b7bdbed163679", "NightLedger sspicli.dll", MK)
    ]
    d["58-arcbridge"] = mk_net + [
        ("md5", "5fa15ef96808ea82f0a6176f0bb4b386", "ArcBridge sample", MK),
        ("md5", "42f847597109da2a220391bb09d00676", "ArcBridge sample", MK),
        ("md5", "afb1c1583606599c7272cfb33cc6f498", "ArcBridge sample", MK),
    ]
    d["59-bridgehead"] = mk_net + [
        ("md5", "6038d42af0affd1fb263f470c0956f6b", "BridgeHead unbcl.dll", MK),
        ("md5", "ae628efa305387b633dce82f9364875b", "BridgeHead unbcl.dll", MK),
        ("md5", "f7d36cc5904a53252d2bb3d21615134f", "BridgeHead libwinpthread-1.dll", MK),
        ("md5", "c90f0efadbf322e5eb1c4103a38c30e6", "BridgeHead libwinpthread-1.dll", MK),
        ("md5", "d09b14a2fe01c7363ecc56f5d046162c", "BridgeHead IPHLPAPI.dll", MK),
    ]

    # UAT-9244 split
    tern_c2 = ["154.205.154.82", "207.148.121.95", "207.148.120.52", "212.11.64.105"]
    suspected = [
        "149.28.25.33",
        "154.205.154.194",
        "154.205.154.65",
        "154.205.154.70",
        "154.223.21.130",
        "154.223.21.194",
        "158.247.238.240",
        "216.238.112.222",
        "216.238.123.242",
        "216.238.94.37",
        "38.54.125.134",
        "38.60.199.34",
        "45.32.106.94",
        "45.77.34.194",
        "45.77.41.141",
        "47.76.100.159",
        "64.190.113.170",
        "64.95.10.253",
    ]
    d["51-terndoor"] = (
        [("ip", ip, "TernDoor C2 (Talos)", TAL) for ip in tern_c2]
        + [("ip", ip, "Suspected UAT-9244 IP (Talos; association-only)", TAL) for ip in suspected]
        + [
            (
                "sha256",
                "711d9427ee43bc2186b9124f31cba2db5f54ec9a0d56dc2948e1a4377bada289",
                "TernDoor Loader DLL",
                TAL,
            ),
            (
                "sha256",
                "3c098a687947938e36ab34b9f09a11ebd82d50089cbfe6e237d810faa729f8ff",
                "TernDoor Loader DLL",
                TAL,
            ),
            (
                "sha256",
                "f36913607356a32ea106103387105c635fa923f8ed98ad0194b66ec79e379a02",
                "TernDoor Loader DLL",
                TAL,
            ),
        ]
    )
    d["52-peertime"] = [
        ("ip", "185.196.10.247", "PeerTime remote location", TAL),
        ("ip", "185.196.10.38", "PeerTime C2", TAL),
        ("domain", "xtibh.com", "PeerTime remote location", TAL),
        ("domain", "xcit76.com", "PeerTime remote location", TAL),
        ("domain", "bloopencil.net", "PeerTime C2", TAL),
        (
            "sha256",
            "34d64b3cd9430e85edefcb883973a086dd5de9917e05fabec89b1f4ab9627e91",
            "PeerTime malware",
            TAL,
        ),
        (
            "sha256",
            "c9fc2af30f769d856b88b3051f19fdb663b3e0a0916279df9bbcba93c6a110c9",
            "PeerTime instrumentor",
            TAL,
        ),
    ]
    d["53-bruteentry"] = [
        ("ip", "212.11.64.105", "BruteEntry infrastructure (also PeerTime host)", TAL),
        ("ip", "185.196.10.247", "BruteEntry infrastructure", TAL),
        (
            "sha256",
            "1fcdd5a417db31e5e07d32cecfa69e53f0dce95b7130ad9c03b92249f001801d",
            "BruteEntry installation script",
            TAL,
        ),
        (
            "sha256",
            "66adeedfb739774fcc09aa7426c8fad29f8047ab4caee8040d07c0e84d011611",
            "BruteEntry agent",
            TAL,
        ),
        (
            "sha256",
            "66bdce93de3b02cf9cdadad18ca1504ac83e379a752d51f60deae6dcbafe4e31",
            "BruteEntry agent",
            TAL,
        ),
    ]

    # ABCDoor residual IPs/domains (skip existing 154.82.81.205, abc.haijing88.com, abc.fetish-friends.com)
    abc_html = (EVID / "abcdoor/securelist-abcdoor-en.html").read_text(errors="ignore")
    abc_ips = sorted(
        {
            m
            for m in re.findall(r"opentip\.kaspersky\.com/(\d{1,3}(?:\.\d{1,3}){3})/", abc_html)
        }
    )
    abc_doms = sorted(
        {
            m.lower()
            for m in re.findall(r"opentip\.kaspersky\.com/([a-z0-9][a-z0-9.\-]{2,180}?)/", abc_html, re.I)
            if "." in m
            and not re.match(r"^\d+\.\d+\.\d+\.\d+$", m)
            and not re.fullmatch(r"[a-f0-9]{32}", m, re.I)
        }
    )
    d["23-abcdoor"] = [("ip", ip, "ABCDoor related IP (OpenTIP)", ABC) for ip in abc_ips] + [
        ("domain", x, "ABCDoor related domain (OpenTIP)", ABC) for x in abc_doms
    ]

    # PromptSpy / GhostChat / HybridPetya from ESET GitHub
    d["28-promptspy"] = [
        ("domain", "mgardownload.com", "C2 / download domain", ESP),
        ("domain", "m-mgarg.com", "C2 domain", ESP),
        ("ip", "54.67.2.84", "C2 IP listed with domains", ESP),
        ("sha1", "F8F4C5BC498BCCE907DC975DD88BE8D594629909", "sample", ESP),
        ("sha1", "6BBC9AB132BA066F63676E05DA13D108598BC29B", "sample", ESP),
        ("sha1", "C14E9B062ED28115EDE096788F62B47A6ED841AC", "sample", ESP),
    ]
    d["29-ghostchat"] = [
        ("domain", "hitpak.org", "C2 domain", ESG),
        ("sha1", "B15B1F3F2227EBA4B69C85BDB638DF34B9D30B6A", "sample", ESG),
        ("sha1", "8B103D0AA37E5297143E21949471FD4F6B2ECBAA", "sample", ESG),
    ]
    d["30-hybridpetya"] = [
        ("sha1", "9B0EE05FFFDA0B16CF9DAAC587CB92BB06D3981B", "HybridPetya installer", ESH),
        ("sha1", "3393A8C258239D6802553FD1CCE397E18FA285A1", "HybridPetya installer", ESH),
        ("sha1", "BD35908D5A5E9F7E41A61B7AB598AB9A88DB723D", "UEFI bootkit", ESH),
        ("sha1", "9DF922D00171AA3C31B75446D700EE567F8D787B", "UEFI bootkit", ESH),
        ("path", "/EFI/Microsoft/Boot/counter", "host path", ESH),
        ("path", "/EFI/Microsoft/Boot/verify", "host path", ESH),
        ("path", "/EFI/Microsoft/Boot/config", "host path", ESH),
    ]

    # GopherWhisper / FriendDelivery / LaxGopher
    d["47-laxgopher"] = [
        ("ip", "43.231.113.50", "SSLORDoor C2; hosting Intelligent Tools (ESET)", ESGOP),
        ("sha1", "C72E7540D6F12D74D8E737B02F31568385F575D7", "CompactGopher temp001.exe", ESGOP),
        ("sha1", "57C2490E4DB194D3503EE85635FB1D6F26E8C534", "RatGopher Discord C2", ESGOP),
        ("sha1", "AD7E264EB08415871617E45F21D03F7D71E4C36F", "SSLORDoor delltool.exe", ESGOP),
        ("sha1", "926974FACFD0383C65458D6EF1F31FBB7C769E18", "BoxOfFriends", ESGOP),
    ]
    d["48-frienddelivery"] = [
        ("ip", "43.231.113.50", "GopherWhisper arsenal C2 (SSLORDoor); shared toolset context only", ESGOP),
        ("sha1", "FA9E65E58EB8FA41FDE0A0A870B7D24B298026D9", "JabGopher injector whisper.dll", ESGOP),
    ]

    # LongNosedGoblin
    ln_rows = [
        ("ip", "118.107.234.26", "NosyDownloader C2; www.sslvpnserver.com", ESLN),
        ("domain", "www.sslvpnserver.com", "NosyDownloader C2 domain", ESLN),
        ("ip", "103.159.132.30", "NosyDownloader C2; www.threadstub.com", ESLN),
        ("domain", "www.threadstub.com", "NosyDownloader C2 domain", ESLN),
        ("ip", "101.99.88.113", "NosyDownloader C2; www.blazenewso.com", ESLN),
        ("domain", "www.blazenewso.com", "NosyDownloader C2 domain", ESLN),
        ("ip", "101.99.88.188", "NosyDownloader C2; www.privacypolicy-my.com", ESLN),
        ("domain", "www.privacypolicy-my.com", "NosyDownloader C2 domain", ESLN),
        ("ip", "118.107.234.29", "ReverseSocks5 server", ESLN),
        ("ip", "38.54.17.131", "malware host (possibly Cobalt Strike) — association-only", ESLN),
    ]
    d["49-nosydoor"] = ln_rows + [
        ("sha1", "154A35DD4117DB760699C2092AFB307E94008506", "NosyDoor stage1 Registry.plo", ESLN),
        ("sha1", "1959E2198D6F81B2604DF7AC1F508AEB7A6FA07E", "NosyDoor stage2 SharedReg.dll", ESLN),
        ("sha1", "E0B44715BC4C327C04E63F881ECC087B7ACBD306", "NosyDoor stage3", ESLN),
    ]
    d["50-nosyhistorian"] = ln_rows + [
        ("sha1", "4E3F6E9D0F443F4C42974A0551EEE957B498DA3D", "NosyHistorian History.ini", ESLN),
        ("sha1", "CD745BD2636F607CC4FB9389535BF3579321CA72", "NosyHistorian History.ini", ESLN),
        ("sha1", "563677CFACD328EA2478836E58A8BD0DF11206A3", "NosyHistorian info.txt", ESLN),
    ]

    # MuddyWater Fooder / MuddyViper
    mw_net = [
        ("domain", "processplanet.org", "staging and C2", ESMW),
        ("domain", "magicallyday.com", "C2", ESMW),
        ("domain", "api.tikavodot.co.il", "C2", ESMW),
        ("ip", "3.95.7.142", "C2", ESMW),
        ("ip", "35.175.224.64", "C2", ESMW),
        ("ip", "51.16.209.105", "C2", ESMW),
        ("ip", "62.106.66.112", "staging", ESMW),
        ("ip", "157.20.182.45", "staging", ESMW),
        ("ip", "161.35.172.55", "staging", ESMW),
        ("ip", "167.99.224.13", "C2", ESMW),
        ("ip", "194.11.246.78", "C2", ESMW),
        ("ip", "194.11.246.101", "staging and C2", ESMW),
        ("ip", "206.71.149.51", "staging", ESMW),
        ("ip", "212.232.22.136", "C2", ESMW),
    ]
    d["60-fooder"] = mw_net + [
        ("sha1", "76632910CF67697BF5D7285FAE38BFCF438EC082", "Fooder launcher OsUpdater.exe", ESMW),
        ("sha1", "CD36F93DBC4C718930593D8F029EFDCAA52B619B", "Fooder + HackBrowserData", ESMW),
        ("sha1", "0657D0B0610618886DDD74C3D0A1D582CDD24863", "Fooder embedding MuddyViper", ESMW),
    ]
    d["61-muddyviper"] = mw_net + [
        ("sha1", "2939FD218E0145D730BD94AA1C76386A5259EACE", "Fooder loader w/ MuddyViper (msi.dll)", ESMW),
        ("sha1", "3BC6502A55A4D5D29132DA4D9943E154A810CC83", "Fooder loader w/ MuddyViper", ESMW),
        ("sha1", "7950296331802188EB99E232E2C383CB9FDD5D7D", "Fooder loader w/ MuddyViper", ESMW),
    ]

    # Dohdoor — DoH domains (normalize case)
    doh_txt = (EVID / "dohdoor/github-ioc/dohdoor.txt").read_text(errors="ignore")
    doh_adds: list[tuple[str, str, str, str]] = []
    for line in doh_txt.splitlines():
        line = undefang(line.strip())
        if not line:
            continue
        if re.fullmatch(r"[a-fA-F0-9]{64}", line):
            doh_adds.append(("sha256", line.lower(), "Dohdoor sample", DOH))
        elif line.startswith("http"):
            doh_adds.append(("url", line, "Dohdoor URL", DOH))
            # also domain
            m = re.search(r"https?://([^/]+)", line, re.I)
            if m:
                doh_adds.append(("domain", m.group(1).lower(), "Dohdoor DoH / staging domain", DOH))
        elif "[" in line or re.search(r"[a-zA-Z]", line):
            # domain-like with mixed case
            clean = undefang(line).lower()
            if "." in clean and " " not in clean and not clean.startswith("http"):
                doh_adds.append(("domain", clean, "Dohdoor DoH domain", DOH))
    d["46-dohdoor"] = doh_adds

    # HEAVYGRAM — email + staging + select hashes (not dumping entire 55-page hash dump)
    d["26-heavygram"] = [
        (
            "email",
            "ghazalehmehrjo@gmail.com",
            "Credential string embedded in Pictory_premium sample (FBI FLASH) — NOT confirmed operator identity",
            FBI,
        ),
        (
            "url",
            "https://sgp1.vultrobjects.com/downloads/pictory/Pictory_premium_ver9.0.4.exe",
            "Malware staging URL (Vultr Objects)",
            FBI,
        ),
        ("domain", "sgp1.vultrobjects.com", "Vultr Objects staging host", FBI),
        ("domain", "ams1.vultrobjects.com", "Vultr Objects host (Group-IB)", GIB),
        ("domain", "micbucket.ams1.vultrobjects.com", "Vultr Objects bucket host", GIB),
        ("domain", "ppt1.sgp1.vultrobjects.com", "Vultr Objects host", GIB),
        ("domain", "handala-hack.to", "related domain (Group-IB)", GIB),
        ("domain", "handala-redwanted.to", "related domain (Group-IB)", GIB),
        ("domain", "justicehomeland.org", "related domain (Group-IB)", GIB),
        ("domain", "karmabelow80.org", "related domain (Group-IB)", GIB),
        ("md5", "1E6B601F733BC40EAA58916986BFC5B9", "Pictory_premium_ver9.0.4.exe", FBI),
        ("sha256", "E8B633DCAD173EB41EF02686B46779A4A0E53DF7F6C63039A798F2DB5EB83AFC", "same sample", FBI),
        ("md5", "B9086413E7B6A0C6A11C25D14C22615F", "Telegram_Authenticator.exe", FBI),
        ("sha256", "9014FE4F16F01C0439B261ADE4CF980F460E0DAE46B1EC5F58FD9BC0AF26E531", "same sample", FBI),
    ]

    # MonsterV2 hashes from Proofpoint (network thin)
    mv = (EVID / "monsterv2/proofpoint-ta585-monsterv2.html").read_text(errors="ignore")
    mv_sha = sorted(set(re.findall(r"\b[a-fA-F0-9]{64}\b", mv)))
    d["21-monsterv2"] = [
        ("sha256", h.lower(), "MonsterV2 / TA585 related sample (Proofpoint)", PF) for h in mv_sha[:20]
    ]

    # Screening Serpens domains for miniupdate / minijunk / minibrowse
    sc = (EVID / "miniupdate/unit42-screening-serpens-2026.html").read_text(errors="ignore")
    # defanged domains in article
    sc_doms = sorted(
        {
            undefang(x).lower()
            for x in re.findall(
                r"\b[a-z0-9][a-z0-9\-]*(?:\[\.\.][a-z0-9][a-z0-9\-]*)+\b", sc, re.I
            )
        }
    )
    # also plain interesting domains from text near MiniUpdate etc — curated known from extract
    curated_sc = [
        "buisness-centeral-transportation.com",
        "business-startup.org",
        "premierhealthadvisory.com",
        "ramiltonsfinance.com",
    ]
    for fam, pkg, note in [
        ("24-miniupdate", "24-miniupdate", "Screening Serpens related domain (Unit 42); MiniUpdate context"),
        ("25-minijunk-v2", "25-minijunk-v2", "Screening Serpens related domain (Unit 42); MiniJunk context"),
        ("62-minibrowse", "62-minibrowse", "Screening Serpens related domain (Unit 42); MiniBrowse context"),
    ]:
        d[pkg] = [("domain", x, note, U42) for x in curated_sc]

    # GhostContainer hashes
    gc = (EVID / "ghostcontainer/securelist-ghostcontainer.html").read_text(errors="ignore")
    gc_md5 = sorted(
        {
            m.lower()
            for m in re.findall(r"opentip\.kaspersky\.com/([a-f0-9]{32})/", gc, re.I)
        }
    )
    d["45-ghostcontainer"] = [
        ("md5", m, "GhostContainer / Exchange backdoor sample (OpenTIP)", "Kaspersky Securelist GhostContainer")
        for m in gc_md5
    ]

    return d


# --- WHOIS / RDAP ---

def rdap_ip(ip: str) -> dict:
    out = {"query": ip, "kind": "ip", "asn": "", "asn_org": "", "network_name": "", "country": "", "rir": "", "raw_summary": ""}
    try:
        req = urllib.request.Request(f"https://rdap.org/ip/{ip}", headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.load(resp)
        out["network_name"] = data.get("name") or data.get("handle") or ""
        out["country"] = data.get("country") or ""
        out["rir"] = (data.get("port43") or "")[:40]
        for e in data.get("entities") or []:
            vcard = e.get("vcardArray") or []
            # skip
        # ASN from entities or cidr0_cidrs — try remarks / links
        # Many RDAP responses include network with remarks; also try ARIN originAS
        for n in data.get("cidr0_cidrs") or []:
            pass
        # parse entities for registrant org
        orgs = []
        for e in data.get("entities") or []:
            roles = e.get("roles") or []
            handle = e.get("handle") or ""
            if "registrant" in roles or "abuse" in roles or True:
                va = e.get("vcardArray")
                if isinstance(va, list) and len(va) > 1:
                    for item in va[1]:
                        if item and item[0] == "fn":
                            orgs.append(item[3])
                        if item and item[0] == "org":
                            orgs.append(item[3])
        if orgs:
            out["asn_org"] = "; ".join(dict.fromkeys(orgs))[:200]
        # try whois for ASN
        try:
            wh = subprocess.run(["whois", ip], capture_output=True, text=True, timeout=25)
            text = wh.stdout or ""
            for pat in [
                r"OriginAS:\s*(AS\d+)",
                r"origin:\s*(AS\d+)",
                r"originas:\s*(AS\d+)",
                r"aut-num:\s*(AS\d+)",
            ]:
                m = re.search(pat, text, re.I)
                if m:
                    out["asn"] = m.group(1).upper()
                    break
            for pat in [r"OrgName:\s*(.+)", r"org-name:\s*(.+)", r"descr:\s*(.+)"]:
                m = re.search(pat, text, re.I)
                if m and not out["asn_org"]:
                    out["asn_org"] = m.group(1).strip()[:200]
                    break
            if not out["country"]:
                m = re.search(r"Country:\s*([A-Z]{2})", text)
                if m:
                    out["country"] = m.group(1)
            out["raw_summary"] = " | ".join(
                line.strip()
                for line in text.splitlines()
                if re.match(r"^(OrgName|org-name|netname|descr|OriginAS|origin|Country|country):", line, re.I)
            )[:400]
        except Exception as e:
            out["raw_summary"] = f"whois_error:{e}"
    except Exception as e:
        out["raw_summary"] = f"rdap_error:{e}"
    return out


def rdap_domain(domain: str) -> dict:
    out = {
        "query": domain,
        "kind": "domain",
        "asn": "",
        "asn_org": "",
        "network_name": "",
        "country": "",
        "rir": "",
        "raw_summary": "",
        "registrant": "",
        "registrar": "",
        "created": "",
        "emails": "",
    }
    # skip cloud / CDN that won't yield useful WHOIS
    skip_suffix = (
        ".azurewebsites.net",
        ".cloudapp.azure.com",
        ".pages.dev",
        ".github.io",
        ".amazonaws.com",
        ".cloudfront.net",
        ".vultrobjects.com",
    )
    if domain.lower().endswith(skip_suffix):
        out["raw_summary"] = "cloud_managed_skip_detailed_whois"
        out["asn_org"] = "Cloud-managed hostname (Azure/CF/Vultr Objects) — registrant not actor-attributable via WHOIS alone"
        return out
    try:
        wh = subprocess.run(["whois", domain], capture_output=True, text=True, timeout=30)
        text = wh.stdout or ""
        def grab(pats):
            for p in pats:
                m = re.search(p, text, re.I | re.M)
                if m:
                    return m.group(1).strip()
            return ""

        out["registrar"] = grab([r"Registrar:\s*(.+)", r"Registrar Name:\s*(.+)"])
        out["registrant"] = grab(
            [
                r"Registrant Organization:\s*(.+)",
                r"Registrant Name:\s*(.+)",
                r"org:\s*(.+)",
                r"OrgName:\s*(.+)",
            ]
        )
        out["created"] = grab(
            [r"Creation Date:\s*(.+)", r"Created:\s*(.+)", r"created:\s*(.+)"]
        )
        emails = re.findall(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", text)
        # filter privacy
        emails = [e for e in emails if not re.search(r"abuse@|whoisprivacy|domainsbyproxy|contact\.gandi|godaddy\.com|markmonitor", e, re.I)]
        out["emails"] = "; ".join(dict.fromkeys(emails))[:200]
        out["country"] = grab([r"Registrant Country:\s*([A-Z]{2})", r"Country:\s*([A-Z]{2})"])
        out["asn_org"] = out["registrant"] or out["registrar"]
        out["raw_summary"] = " | ".join(
            line.strip()
            for line in text.splitlines()
            if re.match(
                r"^(Registrar|Registrant Organization|Registrant Name|Creation Date|Created|Name Server|nserver|org|country):",
                line,
                re.I,
            )
        )[:500]
        if "REDACTED" in text or "GDPR" in text or "redacted for privacy" in text.lower():
            out["raw_summary"] = ("PRIVACY_REDACTED; " + out["raw_summary"])[:500]
    except Exception as e:
        out["raw_summary"] = f"whois_error:{e}"
    return out


def collect_net_values() -> list[tuple[str, str, str]]:
    """Return (family, type, value) for all net IOCs in pkgs 16-66."""
    items = []
    for p in sorted(PKG.iterdir()):
        if not p.is_dir():
            continue
        try:
            n = int(p.name.split("-")[0])
        except Exception:
            continue
        if n < 16:
            continue
        fam = p.name.split("-", 1)[1]
        path = p / "03_INDICATORS.csv"
        for r in read_rows(path):
            t = (r.get("type") or "").lower()
            v = (r.get("value") or "").strip()
            if t in ("ip", "domain") and v:
                items.append((fam, t, v))
    return items


def main() -> None:
    print("=== Transcribing curated IOCs ===")
    totals = {}
    for pkg, adds in curated().items():
        prefix = {
            "22-phantomheart": "PHH",
            "21-monsterv2": "MNV",
            "23-abcdoor": "ABC",
            "24-miniupdate": "MUP",
            "25-minijunk-v2": "MJV",
            "26-heavygram": "HVG",
            "28-promptspy": "PSP",
            "29-ghostchat": "GCH",
            "30-hybridpetya": "HYP",
            "45-ghostcontainer": "GCT",
            "46-dohdoor": "DOH",
            "47-laxgopher": "LXG",
            "48-frienddelivery": "FDL",
            "49-nosydoor": "NSD",
            "50-nosyhistorian": "NSH",
            "51-terndoor": "TRN",
            "52-peertime": "PRT",
            "53-bruteentry": "BRE",
            "57-nightledger": "NLG",
            "58-arcbridge": "ARB",
            "59-bridgehead": "BRH",
            "60-fooder": "FDR",
            "61-muddyviper": "MVP",
            "62-minibrowse": "MBW",
        }[pkg]
        n = append_inds(pkg, prefix, adds)
        totals[pkg] = n
        print(f"  {pkg}: +{n}")

    print("=== WHOIS/RDAP enrichment ===")
    # unique net values prioritizing newly filled packages + existing with few
    seen = set()
    owners = []
    # also include existing net from 16-20, 31-42, 43, 52 for enrichment
    for fam, typ, val in collect_net_values():
        key = (typ, val.lower())
        if key in seen:
            continue
        seen.add(key)
    # limit enrichment volume: prioritize IPs and non-cloud domains; max ~120 lookups
    priority_fams = {
        "phantomheart",
        "nightledger",
        "arcbridge",
        "bridgehead",
        "terndoor",
        "peertime",
        "bruteentry",
        "laxgopher",
        "nosydoor",
        "nosyhistorian",
        "fooder",
        "muddyviper",
        "promptspy",
        "ghostchat",
        "dohdoor",
        "heavygram",
        "abcdoor",
        "countloader",
        "mayberobot",
        "norobot",
        "yesrobot",
        "tsunderebot",
        "foxveil",
        "moviereaper",
        "papermill",
        "kkrat",
        "c2looper",
        "smartrat",
    }
    items = [
        (fam, typ, val)
        for fam, typ, val in collect_net_values()
        if fam in priority_fams
    ]
    # unique
    uniq = []
    seen2 = set()
    for fam, typ, val in items:
        k = (typ, val.lower())
        if k in seen2:
            continue
        seen2.add(k)
        uniq.append((fam, typ, val))

    print(f"Unique net indicators to enrich: {len(uniq)}")
    for i, (fam, typ, val) in enumerate(uniq):
        if typ == "ip":
            try:
                ipaddress.ip_address(val)
            except Exception:
                continue
            info = rdap_ip(val)
        else:
            info = rdap_domain(val)
        owners.append(
            {
                "family": fam,
                "indicator_type": typ,
                "value": val,
                "asn": info.get("asn", ""),
                "org": info.get("asn_org") or info.get("registrant") or "",
                "registrar": info.get("registrar", ""),
                "registrant": info.get("registrant", ""),
                "country": info.get("country", ""),
                "created": info.get("created", ""),
                "contact_emails": info.get("emails", ""),
                "network_name": info.get("network_name", ""),
                "summary": info.get("raw_summary", ""),
                "caveat": "Passive WHOIS/RDAP only; privacy-redacted records do not establish operator identity. Cloud hostnames are infrastructure, not actor orgs.",
            }
        )
        if (i + 1) % 10 == 0:
            print(f"  ... {i+1}/{len(uniq)}")
        time.sleep(0.35)

    OWN.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "family",
        "indicator_type",
        "value",
        "asn",
        "org",
        "registrar",
        "registrant",
        "country",
        "created",
        "contact_emails",
        "network_name",
        "summary",
        "caveat",
    ]
    with OWN.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in owners:
            w.writerow(row)
    print(f"Wrote {OWN} ({len(owners)} rows)")
    print("Totals added:", totals)


if __name__ == "__main__":
    main()
