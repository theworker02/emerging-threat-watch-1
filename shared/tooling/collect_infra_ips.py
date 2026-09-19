#!/usr/bin/env python3
"""Passive DNS + IP RDAP collector for campaign infrastructure ledger.

Policy: AUTONOMOUS_COLLECTION_POLICY.md
- No malware execution, no C2 auth, no exploitation
- Skip / demote Cloudflare & Azure edge fan-out for DNS seeds
- OBSERVED_PASSIVE only; author_attribution never inferred
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EV = ROOT / "evidence"
PASSIVE = EV / "passive-observations"
MANIFEST = EV / "manifests" / "passive-observation-manifest.csv"
UA = "EmergingThreatWatch/1.0 (+passive-research; no-c2; autonomous-policy)"
COLLECTED = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TS = COLLECTED.replace(":", "")

CDN_HINTS = (
    "cloudflare",
    "azurewebsites",
    "blob.core.windows",
    "amazonaws.com",
    "akamai",
    "fastly",
    "github.io",
)

# Non-CDN-preferred domains for A/AAAA resolution
DNS_SEEDS: list[tuple[str, str]] = [
    # Rapuncel clustering lead (non-CF in prior resolve)
    ("Rapuncel", "ryanpresbrey.cc"),
    # NodeRabbit non-Azure vendor domains
    ("NodeRabbit", "visitfinancedentists.com"),
    ("NodeRabbit", "healthcomfsdpower.com"),
    ("NodeRabbit", "msmanagementgrp.com"),
    ("NodeRabbit", "msmanagementgrpmedia.com"),
    ("NodeRabbit", "healthfullyrecipes.com"),
    ("NodeRabbit", "lifespotify.com"),
    ("NodeRabbit", "sahi-finance.com"),
    ("NodeRabbit", "healthful-hub.com"),
    ("NodeRabbit", "neumedicahealthcare.com"),
    ("NodeRabbit", "optimumhealthcredit.com"),
    ("NodeRabbit", "refreshhealthandwellness.com"),
    ("NodeRabbit", "healthvitalitycare.com"),
    ("NodeRabbit", "aceofspadesmanagement.com"),
    ("NodeRabbit", "glmediaagency.com"),
    ("NodeRabbit", "digimediaskill.com"),
    ("NodeRabbit", "healthyweightplan.com"),
    ("NodeRabbit", "mens-health-online.com"),
    # SynkLoader Expel-published C2 domains (PRIMARY domains; resolve for OBSERVED_PASSIVE IPs)
    ("SynkLoader", "neversoftmain.net"),
    ("SynkLoader", "rootfarmapp.net"),
    ("SynkLoader", "tripinupdate.net"),
    ("SynkLoader", "aroclenetapp.net"),
    # RatHat community-IOC domains already CT'd (not Zimperium primary hosts)
    ("RatHat", "adidasabc.com"),
    ("RatHat", "admin.xiongmaocs.help"),
    ("RatHat", "kingbss.com"),
]

# Interesting IPs for IP-RDAP (vendor PRIMARY or high-value OBSERVED)
RDAP_IPS: list[tuple[str, str]] = [
    ("Rapuncel", "2.26.126.50"),
    ("Settra", "45.13.122.7"),
    ("Settra", "193.5.65.114"),
    ("Rapuncel", "207.207.210.50"),
    ("SynkLoader", "149.248.76.220"),
    ("SynkLoader", "162.33.177.8"),
    ("SynkLoader", "216.245.184.14"),
    ("SynkLoader", "64.94.85.67"),
]

MANIFEST_FIELDS = [
    "evidence_id",
    "family",
    "indicator",
    "observation_type",
    "value",
    "collected_utc",
    "collection_mechanism",
    "originating_service",
    "original_query",
    "raw_response_ref",
    "sha256",
    "provenance",
    "confidence",
    "relationship_type",
    "first_seen",
    "last_seen",
    "asn",
    "notes",
]

PREFIX = {
    "Rapuncel": "RAP",
    "Settra": "SET",
    "RatHat": "RAT",
    "NodeRabbit": "NRB",
    "PollCat": "POL",
    "SynkLoader": "SYN",
    "Showboat": "SHO",
}


def http_get(url: str, timeout: int = 45) -> tuple[int | None, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json,text/plain,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, (e.read() if e.fp else b"")
    except Exception as e:
        return None, str(e).encode("utf-8", errors="replace")


def next_po_id(family: str, existing: set[str]) -> str:
    p = PREFIX.get(family, "ETW")
    n = 1
    while True:
        eid = f"{p}-PO-{n:04d}"
        if eid not in existing:
            return eid
        n += 1


def append_manifest(rows: list[dict]) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    existing: list[dict] = []
    ids: set[str] = set()
    if MANIFEST.exists():
        with MANIFEST.open(newline="", encoding="utf-8") as f:
            existing = list(csv.DictReader(f))
            ids = {r["evidence_id"] for r in existing if r.get("evidence_id")}
    for r in rows:
        if not r.get("evidence_id"):
            r["evidence_id"] = next_po_id(r["family"], ids)
            ids.add(r["evidence_id"])
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=MANIFEST_FIELDS)
        w.writeheader()
        w.writerows(existing + rows)


def is_cdn_domain(domain: str) -> bool:
    d = domain.lower()
    return any(h in d for h in CDN_HINTS)


def classify_ip(ip: str) -> str:
    """Heuristic CDN/edge classification for notes — not attribution."""
    parts = ip.split(".")
    if len(parts) != 4:
        return "unknown"
    try:
        a, b = int(parts[0]), int(parts[1])
    except ValueError:
        return "unknown"
    # Cloudflare common ranges (partial)
    if a == 104 and b == 21:
        return "cdn_edge_cloudflare"
    if a == 172 and b == 67:
        return "cdn_edge_cloudflare"
    if a == 188 and b == 114:
        return "cdn_edge_cloudflare"
    # Azure / Microsoft-ish public cloud (loose)
    if a == 57 and b == 150:
        return "cdn_edge_azure"
    return "non_cdn_candidate"


def resolve_domain(family: str, domain: str) -> list[dict]:
    if is_cdn_domain(domain):
        return []
    fam = family
    out_dir = PASSIVE / "dns" / fam.lower()
    out_dir.mkdir(parents=True, exist_ok=True)

    result: dict = {"domain": domain, "collected_utc": COLLECTED, "a": [], "aaaa": [], "error": None}
    try:
        infos = socket.getaddrinfo(domain, None)
        seen = set()
        for info in infos:
            addr = info[4][0]
            if addr in seen:
                continue
            seen.add(addr)
            if ":" in addr:
                result["aaaa"].append(addr)
            else:
                result["a"].append(addr)
    except socket.gaierror as e:
        result["error"] = str(e)

    fname = f"dns_resolve_{re.sub(r'[^a-zA-Z0-9._-]+', '_', domain)}_{TS}.json"
    path = out_dir / fname
    body = json.dumps(result, indent=2).encode("utf-8")
    path.write_bytes(body)
    sha = hashlib.sha256(body).hexdigest()
    rel = str(path.relative_to(ROOT)).replace("\\", "/")

    ips = result["a"] + result["aaaa"]
    if result["error"] and not ips:
        value = f"nxdomain_or_error={result['error'][:120]}"
        conf = "Low"
    else:
        value = f"A={','.join(result['a']) or 'none'}; AAAA={','.join(result['aaaa']) or 'none'}"
        conf = "High" if ips else "Moderate"

    rows = [
        {
            "evidence_id": "",
            "family": fam,
            "indicator": domain,
            "observation_type": "dns",
            "value": value,
            "collected_utc": COLLECTED,
            "collection_mechanism": "socket.getaddrinfo A/AAAA",
            "originating_service": "system_resolver",
            "original_query": domain,
            "raw_response_ref": rel,
            "sha256": sha,
            "provenance": "OBSERVED_PASSIVE",
            "confidence": conf,
            "relationship_type": "OBSERVED_PASSIVE",
            "first_seen": "",
            "last_seen": "",
            "asn": "",
            "notes": (
                "Passive DNS A/AAAA only. Resolving != malicious / C2 active. "
                "CDN edges demoted; author identity NOT ESTABLISHED."
            ),
        }
    ]
    # One row per IP for ledger convenience
    for ip in ips:
        kind = classify_ip(ip)
        rel_type = "ASSOCIATION_ONLY" if kind.startswith("cdn_edge") else "INFRASTRUCTURE_OVERLAP"
        rows.append(
            {
                "evidence_id": "",
                "family": fam,
                "indicator": domain,
                "observation_type": "dns_a",
                "value": ip,
                "collected_utc": COLLECTED,
                "collection_mechanism": "socket.getaddrinfo A/AAAA",
                "originating_service": "system_resolver",
                "original_query": domain,
                "raw_response_ref": rel,
                "sha256": sha,
                "provenance": "OBSERVED_PASSIVE",
                "confidence": "Moderate" if kind.startswith("cdn_edge") else "High",
                "relationship_type": rel_type,
                "first_seen": "",
                "last_seen": "",
                "asn": "",
                "notes": f"A/AAAA mapping; class={kind}. Not actor-owned by default.",
            }
        )
    return rows


def rdap_ip(family: str, ip: str) -> list[dict]:
    fam = family
    out_dir = PASSIVE / "rdap" / fam.lower()
    out_dir.mkdir(parents=True, exist_ok=True)
    url = f"https://rdap.org/ip/{urllib.parse.quote(ip)}"
    status, body = http_get(url)
    fname = f"rdap_ip_{ip.replace(':', '_')}_{TS}.json"
    path = out_dir / fname
    path.write_bytes(body)
    sha = hashlib.sha256(body).hexdigest()
    rel = str(path.relative_to(ROOT)).replace("\\", "/")

    name = ""
    country = ""
    try:
        data = json.loads(body.decode("utf-8", errors="replace"))
        name = data.get("name") or ""
        country = data.get("country") or ""
    except json.JSONDecodeError:
        pass

    value = f"http_status={status}; name={name}; country={country}"
    conf = "Moderate" if status == 200 else "Low"
    return [
        {
            "evidence_id": "",
            "family": fam,
            "indicator": ip,
            "observation_type": "rdap_ip",
            "value": value,
            "collected_utc": COLLECTED,
            "collection_mechanism": "HTTP GET rdap.org/ip/{ip}",
            "originating_service": "rdap.org",
            "original_query": ip,
            "raw_response_ref": rel,
            "sha256": sha,
            "provenance": "OBSERVED_PASSIVE",
            "confidence": conf,
            "relationship_type": "OBSERVED_PASSIVE",
            "first_seen": "",
            "last_seen": "",
            "asn": "",
            "notes": (
                "Public IP RDAP allocation metadata only. "
                "RDAP contacts are typically ISP/hosting — NOT malware-author identity. "
                "author_attribution=NOT_ESTABLISHED."
            ),
        }
    ]


def fetch_showboat_iocs() -> list[dict]:
    """Preserve Black Lotus Labs Showboat_IOCs.txt if reachable."""
    url = "https://raw.githubusercontent.com/blacklotuslabs/IOCs/main/Showboat_IOCs.txt"
    status, body = http_get(url)
    out_dir = EV / "primary-sources" / "showboat"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"Showboat_IOCs_{TS}.txt"
    path.write_bytes(body)
    sha = hashlib.sha256(body).hexdigest()
    rel = str(path.relative_to(ROOT)).replace("\\", "/")
    ips = re.findall(r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b", body.decode("utf-8", errors="replace"))
    # Also write a small parse summary under passive dns notes folder for ledger
    summary = {"status": status, "sha256": sha, "ips_found": sorted(set(ips)), "path": rel}
    sum_path = PASSIVE / "dns" / "showboat"
    sum_path.mkdir(parents=True, exist_ok=True)
    sp = sum_path / f"showboat_iocs_parse_{TS}.json"
    sp.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    rows = [
        {
            "evidence_id": "",
            "family": "Showboat",
            "indicator": "Showboat_IOCs.txt",
            "observation_type": "vendor_ioc_list",
            "value": f"http_status={status}; ipv4_count={len(set(ips))}",
            "collected_utc": COLLECTED,
            "collection_mechanism": "HTTP GET raw.githubusercontent.com blacklotuslabs/IOCs",
            "originating_service": "github_raw",
            "original_query": url,
            "raw_response_ref": rel,
            "sha256": sha,
            "provenance": "PRIMARY-SOURCE" if status == 200 else "OBSERVED_PASSIVE",
            "confidence": "High" if status == 200 else "Low",
            "relationship_type": "PRIMARY-SOURCE" if status == 200 else "OBSERVED_PASSIVE",
            "first_seen": "",
            "last_seen": "",
            "asn": "",
            "notes": "Lumen Black Lotus Labs published IOC file. IPs are campaign infra candidates — author identity NOT ESTABLISHED.",
        }
    ]
    for ip in sorted(set(ips)):
        rows.append(
            {
                "evidence_id": "",
                "family": "Showboat",
                "indicator": ip,
                "observation_type": "ipv4",
                "value": ip,
                "collected_utc": COLLECTED,
                "collection_mechanism": "parsed from Showboat_IOCs.txt",
                "originating_service": "blacklotuslabs",
                "original_query": url,
                "raw_response_ref": rel,
                "sha256": sha,
                "provenance": "PRIMARY-SOURCE",
                "confidence": "High",
                "relationship_type": "PRIMARY-SOURCE",
                "first_seen": "",
                "last_seen": "",
                "asn": "",
                "notes": "Vendor-published Showboat IOC. Role unknown pending BLL article context. Not author home IP.",
            }
        )
    return rows


def main() -> None:
    all_rows: list[dict] = []
    print(f"collected_utc={COLLECTED}")

    for fam, dom in DNS_SEEDS:
        print(f"DNS {fam} {dom}")
        all_rows.extend(resolve_domain(fam, dom))
        time.sleep(0.3)

    for fam, ip in RDAP_IPS:
        # skip if RDAP already exists from earlier settra collect for these exact files? still refresh
        print(f"RDAP-IP {fam} {ip}")
        all_rows.extend(rdap_ip(fam, ip))
        time.sleep(0.8)

    print("Fetch Showboat_IOCs.txt")
    all_rows.extend(fetch_showboat_iocs())

    append_manifest(all_rows)
    print(f"wrote {len(all_rows)} passive rows -> {MANIFEST}")


if __name__ == "__main__":
    main()
