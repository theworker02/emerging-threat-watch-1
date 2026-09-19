#!/usr/bin/env python3
"""Ingest 2026-09-19 executive research pass as new evidence (local only)."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RET = "2026-09-19T18:07:48Z"  # corpus retrieval from user pass (UTC equiv of 14:07:48-04:00)
CUTOFF = "2026-09-19"
SRC_RAP = "https://blog.lastpass.com/posts/lastpass-delphos-report-rapuncel-infostealer"
SRC_HUN = "https://www.huntress.com/blog/new-settra-ransomware-variant"
SRC_CYN = "https://www.cynet.com/settra-ransomware-inside-a-new-enterprise-grade-extortion-threat/"
SRC_MOX = "https://www.moxfive.com/blog/settra-ransomware-ttps-victims-and-defense-guide"
SRC_ZIM = "https://zimperium.com/blog/rathat-ai-powered-mobile-threat-is-here-for-your-credentials-bank-accounts"
SRC_KAS = "https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/"

IND_HDR = [
    "evidence_id", "family", "indicator", "type", "first_seen", "provenance", "confidence",
    "independently_verified", "source_url", "retrieval_date_utc", "notes", "status_label",
]


def wcsv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {path} ({len(rows)})")


def ind(eid, family, indicator, typ, first, prov, conf, url, notes, status="CAMPAIGN_ASSOCIATED"):
    return {
        "evidence_id": eid, "family": family, "indicator": indicator, "type": typ,
        "first_seen": first, "provenance": prov, "confidence": conf,
        "independently_verified": "false", "source_url": url, "retrieval_date_utc": RET,
        "notes": notes, "status_label": status,
    }


def rap_inds():
    rows = [
        ("RAP-IND-0001", "ea8c31a86fa785ab514022c278a2f6e571c86aac9283745a96605c44d88382d6", "sha256", "vsdbg.dll NativeAOT loader", "HIGH_CONFIDENCE_MALICIOUS"),
        ("RAP-IND-0002", "aefbc6e04320e9a0e80f2323f8a897c4fdb222a37b0b87d76e850109decbfadd", "sha256", "Rapuncel stealer", "HIGH_CONFIDENCE_MALICIOUS"),
        ("RAP-IND-0003", "611b3ba687b7f46319a19609605ddfe5225e6d85277d8e923eea3fdb6f7b5b61", "sha256", "Alinubx.sys", "HIGH_CONFIDENCE_MALICIOUS"),
        ("RAP-IND-0004", "75018b06c7105a1dca391805d17b402aed35ebd515b92d461236eafbd606cb40", "sha256", "browser injection DLL", "HIGH_CONFIDENCE_MALICIOUS"),
        ("RAP-IND-0005", "26db14b956e33f69b3397a36387d32e01eb63613acff91069dc76b6ed7de45a8", "sha256", "ProtectR3.dll x64 unpacked", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0006", "5f0cfe8357bb52b45068ddbac053e32bc38e6cb5e086746f5402657b0a5cfb1c", "sha256", "CcProtect reference sample", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0007", "albinofennel.com", "domain", "primary payload server", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0008", "hanselarinmusky.com", "domain", "payload server", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0009", "icansamyope.com", "domain", "secondary payload server", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0010", "istatlmenus.com", "domain", "dynamic traffic director", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0011", "macperformancetools.com", "domain", "terminal domain", "HISTORICAL"),
        ("RAP-IND-0012", "zaffersnouty.com", "domain", "terminal domain", "HISTORICAL"),
        ("RAP-IND-0013", "ryanpresbrey.cc", "domain", "clustering lead", "SUSPICIOUS"),
        ("RAP-IND-0014", "2.26.126.50", "ipv4", "Rapuncel /upload exfil", "HIGH_CONFIDENCE_MALICIOUS"),
        ("RAP-IND-0015", "104.21.27.38", "ipv4", "Cloudflare-fronted mapping — low specificity", "HISTORICAL"),
        ("RAP-IND-0016", "172.67.168.224", "ipv4", "Cloudflare-fronted mapping — low specificity", "HISTORICAL"),
        ("RAP-IND-0017", "172.67.212.253", "ipv4", "Cloudflare-fronted — do not promote as actor-owned", "HISTORICAL"),
        ("RAP-IND-0018", "104.21.20.224", "ipv4", "Cloudflare-fronted — do not promote as actor-owned", "HISTORICAL"),
        ("RAP-IND-0019", "104.21.18.89", "ipv4", "Cloudflare-fronted — do not promote as actor-owned", "HISTORICAL"),
        ("RAP-IND-0020", "C:\\Windows\\System32\\drivers\\nvfsflt64.sys", "path", "Alinubx on-disk path", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0021", "NvFsFilter", "service", "NVIDIA-style service name", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0022", "\\\\.\\Alinubx", "device", "driver device object", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0023", "1e6c1766ac78d7adfdae71d361cb132d972771897ae9065503b135cb812d7c35", "sha256", "istatlmenus.com/mandua.wonted JS body hash (2026-09-10)", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0024", "github.com/LastPass-Authenticator", "repository", "fraudulent org", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0025", "github.com/LastPass-S", "repository", "related fraudulent org", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0026", "lastpass-authenticator.github.io", "url", "fake landing", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0027", "edgarcostartqd.github.io", "url", "redirector", "CAMPAIGN_ASSOCIATED"),
        ("RAP-IND-0028", "dallikilic54.github.io", "url", "redirector", "CAMPAIGN_ASSOCIATED"),
    ]
    out = []
    for eid, val, typ, note, status in rows:
        conf = "Moderate" if "clustering" in note or "Cloudflare" in note else "High"
        out.append(ind(eid, "Rapuncel", val, typ, "unspecified", "PRIMARY-SOURCE", conf, SRC_RAP,
                       note + " | NOT OBSERVED by ETW — primary-source only.", status))
    # Map user RAP-EV seed numbering crosswalk note in RAP-IND-0001
    out[0]["notes"] += " Seed corpus alias RAP-EV-0001 in executive pass; ETW uses RAP-IND-* to avoid collision with Phase1 publication RAP-EV-*."
    return out


def set_inds():
    rows = [
        ("SET-IND-0001", "45.13.122.7", "ipv4", "July 2026 MeshAgent C2 (mvtcs.exe)", SRC_HUN, "High", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0002", "193.5.65.114", "ipv4", "Sept MeshAgent C2; prior assoc Nov 2025 — NOT proof Settra existed 2024", SRC_HUN, "High", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0003", "WIN-LIVFRVQFMKO", "hostname", "Workstation ID; Huntress history to 2024-12-24; multi-campaign reuse possible", SRC_HUN, "High", "SUSPICIOUS"),
        ("SET-IND-0004", "RESTORE_FILES.txt", "filename", "ransom note", SRC_HUN, "High", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0005", "RESTORE_FILES.html", "filename", "ransom note (Cynet)", SRC_CYN, "High", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0006", "gdrv.sys", "filename", "BYOVD Sept incident", SRC_HUN, "High", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0007", "STProcessMonitor_v114.sys", "filename", "MOXFIVE BYOVD artifact — operator tooling", SRC_MOX, "High", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0008", "STProcessMonitor.sys", "filename", "related vulnerable-driver artifact", SRC_MOX, "Moderate", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0009", ".locked", "extension", "July encrypted extension", SRC_HUN, "High", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0010", ".locked_wip", "extension", "Sept / Cynet intermediate extension", SRC_HUN, "High", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0011", "C:\\Users\\Public\\NOTICE.png", "path", "wallpaper artifact (Cynet)", SRC_CYN, "Moderate", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0012", "win64.exe --pass <secret> --cmd --path <dir>", "behavioral", "CLI password gate pattern", SRC_CYN, "High", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0013", "*_win64.exe", "filename_pattern", "victim-domain_win64.exe naming", SRC_HUN, "High", "CAMPAIGN_ASSOCIATED"),
        ("SET-IND-0014", "Microsoft-Windows-Defender/Operational", "artifact", "typo in clear-list; correct is Microsoft-Windows-Windows-Defender/Operational", SRC_HUN, "High", "CAMPAIGN_ASSOCIATED"),
    ]
    return [ind(a, "Settra", b, c, "see notes", "PRIMARY-SOURCE", e, d, f + " | NOT OBSERVED by ETW.", g) for a, b, c, f, d, e, g in rows]


def rat_inds():
    rows = [
        ("RAT-IND-0001", "liblocal-service.so", "filename", "Go agent"),
        ("RAT-IND-0002", "/data/local/tmp", "path", "staging path"),
        ("RAT-IND-0003", "libmedia_codec.so", "filename", "disguised FRP client"),
        ("RAT-IND-0004", "127.0.0.1:7910", "local_service", "Go agent HTTP"),
        ("RAT-IND-0005", "/api/node/register", "uri_path", "C2 register"),
        ("RAT-IND-0006", "/api/data/credentials", "uri_path", "credential exfil"),
        ("RAT-IND-0007", "/api/adbk/upload", "uri_path", "ADB cert/key upload"),
        ("RAT-IND-0008", "/api/adbk/port", "uri_path", "ADB port reporting"),
        ("RAT-IND-0009", "/api/data/cipher", "uri_path", "PIN/pattern/password"),
        ("RAT-IND-0010", "/api/tun/config", "uri_path", "FRP config"),
        ("RAT-IND-0011", "0x9999", "manifest_chunk", "manifest bomb chunk type"),
        ("RAT-IND-0012", "27042/tcp", "port", "Frida anti-analysis probe"),
        ("RAT-IND-0013", "/api/v2/dev/tasks", "uri_path", "agent command queue"),
        ("RAT-IND-0014", "/api/v2/dev/localServiceHeartbeat", "uri_path", "agent heartbeat"),
        ("RAT-IND-0015", "/api/v2/dev/data/screen-monitor", "uri_path", "shell screen monitor"),
        ("RAT-IND-0016", "getevent", "command", "raw /dev/input capture"),
        ("RAT-IND-0017", "/dev/input", "path", "kernel input nodes"),
    ]
    return [ind(a, "RatHat", b, c, "unspecified", "PRIMARY-SOURCE", "High", SRC_ZIM,
                d + " | Architectural IOC — no SHA-256 in parsed article body. NOT OBSERVED by ETW.", "CAMPAIGN_ASSOCIATED")
            for a, b, c, d in rows]


def nrb_inds():
    md5s = [
        ("NRB-IND-0001", "1EA83E4E4592B01E4ACAB63EB867BEE5", "Front-Technical-Challenge.zip"),
        ("NRB-IND-0002", "CBAAF0900A13F28E380F49ADECEC932C", "FrontEnd-Task.zip"),
        ("NRB-IND-0003", "366515822D5AC1CC500711EF57A2E32E", "Task-FullStack.zip"),
        ("NRB-IND-0004", "CF449F1992C2819E62AC44A0B06AC2E7", "fullstack-1536.zip"),
        ("NRB-IND-0005", "E95A4366686E3F786EA3C056FAB5B0DA", "webapp76592.zip"),
        ("NRB-IND-0006", "DE5AF16A3757EF700B01DC34D67079AE", "webapp76531.zip"),
        ("NRB-IND-0007", "BE086789568441D0D7E4679AEE51F566", "challenges-17831.zip"),
        ("NRB-IND-0008", "E259C5EDF158AAC4CFE14F77DDD0B196", "challenges-17832.zip"),
        ("NRB-IND-0009", "291AC3ABE73C5158E59A437B75D5F0AA", "Project-1802.zip"),
        ("NRB-IND-0010", "0962F56D7EC69F4F2A0162DCBE22116B", "Case-34234.zip"),
        ("NRB-IND-0011", "795E053A990A1569FFDCB57F48F6D085", "RankChallenge-react-6uJSX3-main.zip"),
    ]
    out = [ind(a, "NodeRabbit", b.lower(), "md5", "unspecified", "PRIMARY-SOURCE", "High", SRC_KAS,
               f"Archive {c}. Preserve MD5; obtain SHA-256 via authorized metadata later. Alias NOD-EV in seed pass. NOT OBSERVED by ETW.",
               "CAMPAIGN_ASSOCIATED") for a, b, c in md5s]
    domains = [
        "plugplay.azurewebsites.net", "rgbteller.azurewebsites.net", "wslwebui.azurewebsites.net",
        "visitfinancedentists.com", "kyrasey-f8hfexa5cqamh7fk.westeurope-01.azurewebsites.net",
        "healthcomfsdpower.com", "naturalapplication.azurewebsites.net", "retaildemo.azurewebsites.net",
        "tubitak.azurewebsites.net", "crossdwm.azurewebsites.net", "wdisystem.azurewebsites.net",
        "wslmenus.azurewebsites.net", "dnshnsdev.azurewebsites.net", "hpjumpsrv.azurewebsites.net",
        "storview.azurewebsites.net", "msmanagementgrp.com", "msmanagementgrpmedia.com",
    ]
    for i, d in enumerate(domains, start=12):
        out.append(ind(f"NRB-IND-{i:04d}", d, "domain", "unspecified", "PRIMARY-SOURCE", "High", SRC_KAS,
                       "Azure/Cloudflare-backed C2 context. Shared cloud IP ≠ actor-owned. agent:servers makes lists perishable. NOT OBSERVED by ETW.",
                       "CAMPAIGN_ASSOCIATED"))
    return out


def ct_seeds():
    fields = ["family", "domain", "crt_sh_url", "crt_sh_wildcard_url", "virustotal_url", "urlscan_url", "rdap_url",
              "provenance", "status", "notes"]
    domains = {
        "Rapuncel": ["albinofennel.com", "hanselarinmusky.com", "icansamyope.com", "istatlmenus.com",
                     "macperformancetools.com", "zaffersnouty.com", "ryanpresbrey.cc"],
        "NodeRabbit": ["visitfinancedentists.com", "healthcomfsdpower.com", "msmanagementgrp.com",
                       "msmanagementgrpmedia.com", "plugplay.azurewebsites.net"],
    }
    rows = []
    for fam, ds in domains.items():
        for d in ds:
            rows.append({
                "family": fam, "domain": d,
                "crt_sh_url": f"https://crt.sh/?q={d}",
                "crt_sh_wildcard_url": f"https://crt.sh/?q=%25.{d}",
                "virustotal_url": f"https://www.virustotal.com/gui/domain/{d}",
                "urlscan_url": f"https://urlscan.io/search/#domain:{d}",
                "rdap_url": f"https://rdap.org/domain/{d}",
                "provenance": "COLLECTION_SEED", "status": "UNVERIFIED",
                "notes": "Do not fabricate cert IDs. DNS resolution ≠ malicious. CDN/Azure edges are low-specificity.",
            })
    return fields, rows


def lineage():
    fields = ["comparison", "signal", "assessment", "confidence", "provenance", "notes"]
    rows = [
        {"comparison": "Rapuncel↔BoryptGrab", "signal": "passathook-cs2; GitHub/SEO; UserInformation.txt; installed_applications.txt; Filegraber; browser elevation", "assessment": "Related variant/sibling plausible; same campaign/operator not established", "confidence": "Moderate", "provenance": "PRIMARY-SOURCE", "notes": "LastPass/Delphos"},
        {"comparison": "Rapuncel↔BoryptGrab", "signal": "different builds/C2/helper packaging; Alinubx vs TunnesshClient/HeaconLoad", "assessment": "Counterevidence to identical malware/campaign", "confidence": "High", "provenance": "PRIMARY-SOURCE", "notes": ""},
        {"comparison": "Rapuncel-loader↔Cruciferra/PUROSANGUE", "signal": "NativeAOT; .reloc; Base16; 145-process list; purosangue.tx", "assessment": "Strong shared-tooling; does not establish stealer authorship", "confidence": "High", "provenance": "PRIMARY-SOURCE", "notes": "RAP-H-CRY"},
        {"comparison": "Settra-malware↔Settra-operator", "signal": "encryptor no exfil; operator uses creds/RMM/lateral/BYOVD", "assessment": "Maintain separate ATT&CK models", "confidence": "High", "provenance": "PRIMARY-SOURCE", "notes": "Never say Settra uses Mimikatz"},
        {"comparison": "Settra-July↔Settra-September", "signal": "_win64.exe; recovery impairment; logs; note; MeshAgent", "assessment": "Strong operational similarity; affiliate/operator unresolved", "confidence": "High", "provenance": "PRIMARY-SOURCE", "notes": ""},
        {"comparison": "RatHat↔other-self-ADB", "signal": "Wireless ADB self-pair + shell", "assessment": "Technique parallel only unless code/infra evidence", "confidence": "Low", "provenance": "INFERRED", "notes": "Not lineage"},
        {"comparison": "NodeRabbit-V1↔V2↔V3", "signal": "proxy; persistence; C2; command set growth", "assessment": "Strong family evolution", "confidence": "High", "provenance": "PRIMARY-SOURCE", "notes": ""},
        {"comparison": "NodeRabbit↔Mirage-Kitten", "signal": "victimology; lure; cloud; historical overlap", "assessment": "Kaspersky attribution — not ETW-established", "confidence": "High", "provenance": "PRIMARY-SOURCE", "notes": "Attribution provenance"},
    ]
    return fields, rows


def gaps():
    fields = ["priority", "family", "gap", "why_crucial", "status"]
    rows = [
        {"priority": "P0", "family": "Rapuncel", "gap": "Byte/code compare Alinubx vs CcProtect", "why_crucial": "Defines identity-swapped precisely", "status": "OPEN"},
        {"priority": "P0", "family": "Rapuncel", "gap": "CT + historical DNS all domains", "why_crucial": "Chronology and co-host pivots", "status": "OPEN"},
        {"priority": "P0", "family": "Rapuncel", "gap": "Separate Cruciferra loader code from Rapuncel-specific code", "why_crucial": "Avoid attributing commodity capabilities", "status": "OPEN"},
        {"priority": "P0", "family": "Settra", "gap": "Verified SHA-256 outer and inner payloads", "why_crucial": "Usable sample-hash corpus missing", "status": "OPEN"},
        {"priority": "P0", "family": "Settra", "gap": "Historical pivot WIN-LIVFRVQFMKO + 193.5.65.114", "why_crucial": "Pre-Settra operator activity vs reusable infra", "status": "OPEN"},
        {"priority": "P0", "family": "Settra", "gap": "Pre-encryption exfiltration tooling/destination", "why_crucial": "Encryptor has no exfil stack", "status": "OPEN"},
        {"priority": "P0", "family": "RatHat", "gap": "APK hashes/package names from authorized sources", "why_crucial": "Reproducible sample identity", "status": "PARTIAL"},
        {"priority": "P0", "family": "RatHat", "gap": "Concrete C2/FRP hosts without active interaction", "why_crucial": "URI paths known; hosts sparse in article body", "status": "PARTIAL"},
        {"priority": "P0", "family": "NodeRabbit", "gap": "Resolve Kaspersky MD5 archives to SHA-256", "why_crucial": "Correlation robustness", "status": "OPEN"},
        {"priority": "P0", "family": "NodeRabbit", "gap": "CT/pDNS chronology for non-Azure domains", "why_crucial": "agent:servers mutability", "status": "OPEN"},
        {"priority": "P1", "family": "NodeRabbit", "gap": "Linux/WSL artifact timeline", "why_crucial": "Under-represented vs Windows reporting", "status": "IN_PROGRESS"},
        {"priority": "P1", "family": "NodeRabbit", "gap": "VS Code publisher/signature mismatch detection", "why_crucial": "Durable detection hypothesis", "status": "OPEN"},
    ]
    return fields, rows


def main():
    wcsv(ROOT / "investigations/rapuncel/evidence/published-indicators.csv", rap_inds(), IND_HDR)
    wcsv(ROOT / "investigations/settra/evidence/published-indicators.csv", set_inds(), IND_HDR)
    wcsv(ROOT / "investigations/rathat/evidence/published-indicators.csv", rat_inds(), IND_HDR)
    wcsv(ROOT / "investigations/noderabbit/evidence/published-indicators.csv", nrb_inds(), IND_HDR)

    f, r = ct_seeds()
    wcsv(ROOT / "shared/queries/infrastructure_collection_seeds.csv", r, f)
    wcsv(ROOT / "shared/queries/certificate_transparency_seeds.csv", r, f)

    f, r = lineage()
    (ROOT / "shared/lineage").mkdir(parents=True, exist_ok=True)
    wcsv(ROOT / "shared/lineage/lineage_comparison.csv", r, f)

    f, r = gaps()
    wcsv(ROOT / "intelligence/priority-gaps.csv", r, f)
    for fam in ("rapuncel", "settra", "rathat", "noderabbit"):
        fam_rows = [x for x in r if x["family"].lower() == fam]
        wcsv(ROOT / f"investigations/{fam}/gaps/priority-gaps.csv", fam_rows, f)

    # combined IOCs pointer
    combined = []
    for fam, path in [
        ("Rapuncel", ROOT / "investigations/rapuncel/evidence/published-indicators.csv"),
        ("Settra", ROOT / "investigations/settra/evidence/published-indicators.csv"),
        ("RatHat", ROOT / "investigations/rathat/evidence/published-indicators.csv"),
        ("NodeRabbit", ROOT / "investigations/noderabbit/evidence/published-indicators.csv"),
    ]:
        with path.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                combined.append({
                    "case_id": {"Rapuncel": "RAP", "Settra": "SET", "RatHat": "RAT", "NodeRabbit": "NRB"}[fam],
                    "evidence_id": row["evidence_id"],
                    "value": row["indicator"],
                    "type": row["type"],
                    "provenance": row["provenance"],
                    "confidence": row["confidence"],
                    "independently_verified": "false",
                    "cross_case_link_allowed": "false",
                    "status": row["status_label"],
                    "source_url": row["source_url"],
                    "notes": row["notes"],
                })
    wcsv(ROOT / "shared/combined_iocs.csv", combined,
         ["case_id", "evidence_id", "value", "type", "provenance", "confidence", "independently_verified",
          "cross_case_link_allowed", "status", "source_url", "notes"])
    wcsv(ROOT / "intelligence/master-ioc-index.csv", combined,
         ["case_id", "evidence_id", "value", "type", "provenance", "confidence", "independently_verified",
          "cross_case_link_allowed", "status", "source_url", "notes"])


if __name__ == "__main__":
    main()
