#!/usr/bin/env python3
"""Bounded autonomous passive collector (CT / RDAP).

Policy: shared/methodology/AUTONOMOUS_COLLECTION_POLICY.md
- No malware execution, no C2 auth, no exploitation
- Writes OBSERVED_PASSIVE rows only for facts we retrieved
- Does NOT emit attribution
- Shared CDN edges are not used as fan-out seeds
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
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
SEEDS = ROOT / "shared" / "queries" / "certificate_transparency_seeds.csv"
COMBINED = ROOT / "shared" / "combined_iocs.csv"
UA = "EmergingThreatWatch/1.0 (+passive-research; no-c2; autonomous-policy)"
COLLECTED = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# depth ≤ 1 for this initial autonomous run (seeds only; no IP fan-out)
MAX_CT_QUERIES = 40
CDN_HINTS = ("cloudflare", "azurewebsites", "akamai", "fastly", "amazonaws")

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


def http_get(url: str, timeout: int = 45) -> tuple[int | None, bytes]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json,text/plain,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, (e.read() if e.fp else b"")
    except Exception as e:
        return None, str(e).encode("utf-8", errors="replace")


def load_domain_seeds() -> list[tuple[str, str]]:
    """Return list of (family, domain) from CT seeds + combined IOCs."""
    out: list[tuple[str, str]] = []
    seen = set()
    if SEEDS.exists():
        with SEEDS.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                # flexible column names
                fam = (row.get("family") or row.get("Family") or "").strip()
                dom = (row.get("domain") or row.get("query") or row.get(" Domains") or "").strip()
                if not dom and "crt.sh" in (row.get("url") or row.get("crt_sh_url") or ""):
                    q = urllib.parse.parse_qs(urllib.parse.urlparse(row.get("url") or row.get("crt_sh_url") or "").query)
                    dom = (q.get("q") or [""])[0]
                dom = dom.replace("[.]", ".").lstrip("%25.").lstrip("*.")
                if dom and dom not in seen and " " not in dom:
                    seen.add(dom)
                    out.append((fam or "unknown", dom))
    if COMBINED.exists():
        with COMBINED.open(newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if (row.get("type") or "").lower() != "domain":
                    continue
                ind = (row.get("indicator") or "").replace("[.]", ".")
                fam = row.get("family") or "unknown"
                if ind and ind not in seen and not any(h in ind.lower() for h in ("github.io",)):
                    # still allow github.io as CT seed but mark association-only later
                    seen.add(ind)
                    out.append((fam, ind))
    return out[:MAX_CT_QUERIES]


def next_po_id(family: str, existing: set[str]) -> str:
    prefix = {"Rapuncel": "RAP", "Settra": "SET", "RatHat": "RAT", "NodeRabbit": "NRB"}.get(family, "RAP")
    # normalize family title case from seeds
    for k, v in [("rapuncel", "RAP"), ("settra", "SET"), ("rathat", "RAT"), ("noderabbit", "NRB")]:
        if family.lower() == k:
            prefix = v
            break
    n = 1
    while True:
        eid = f"{prefix}-PO-{n:04d}"
        if eid not in existing:
            return eid
        n += 1


def normalize_family(fam: str) -> str:
    m = {
        "rapuncel": "Rapuncel",
        "settra": "Settra",
        "rathat": "RatHat",
        "noderabbit": "NodeRabbit",
        "Rapuncel": "Rapuncel",
        "Settra": "Settra",
        "RatHat": "RatHat",
        "NodeRabbit": "NodeRabbit",
    }
    return m.get(fam, m.get(fam.lower(), "Rapuncel"))


def append_manifest(rows: list[dict]) -> None:
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    existing: list[dict] = []
    ids: set[str] = set()
    if MANIFEST.exists():
        with MANIFEST.open(newline="", encoding="utf-8") as f:
            existing = list(csv.DictReader(f))
            ids = {r["evidence_id"] for r in existing if r.get("evidence_id")}
    # reassign ids if blank
    for r in rows:
        if not r.get("evidence_id"):
            r["evidence_id"] = next_po_id(r["family"], ids)
            ids.add(r["evidence_id"])
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=MANIFEST_FIELDS)
        w.writeheader()
        w.writerows(existing + rows)


def collect_ct(family: str, domain: str) -> list[dict]:
    rows = []
    fam = normalize_family(family)
    out_dir = PASSIVE / "certificate-transparency" / fam.lower()
    out_dir.mkdir(parents=True, exist_ok=True)
    query = domain
    url = f"https://crt.sh/?q={urllib.parse.quote(query)}&output=json"
    status, body = http_get(url)
    fname = f"ct_{re.sub(r'[^a-zA-Z0-9._-]+', '_', domain)}_{COLLECTED.replace(':', '')}.json"
    path = out_dir / fname
    path.write_bytes(body)
    sha = hashlib.sha256(body).hexdigest()
    rel = str(path.relative_to(ROOT)).replace("\\", "/")

    if status != 200 or not body.strip().startswith(b"["):
        rows.append(
            {
                "evidence_id": "",
                "family": fam,
                "indicator": domain,
                "observation_type": "ct",
                "value": f"fetch_status={status}",
                "collected_utc": COLLECTED,
                "collection_mechanism": "HTTP GET crt.sh output=json",
                "originating_service": "crt.sh",
                "original_query": query,
                "raw_response_ref": rel,
                "sha256": sha,
                "provenance": "OBSERVED_PASSIVE",
                "confidence": "Low",
                "relationship_type": "OBSERVED_PASSIVE",
                "first_seen": "",
                "last_seen": "",
                "asn": "",
                "notes": "CT query attempted; response not usable JSON. Not attribution. Not PRIMARY-SOURCE.",
            }
        )
        return rows

    try:
        certs = json.loads(body.decode("utf-8", errors="replace"))
    except json.JSONDecodeError:
        certs = []

    # summarize: one row per unique issuer CN + earliest/latest, plus count
    by_id = {}
    for c in certs if isinstance(certs, list) else []:
        cid = c.get("id") or c.get("min_cert_id")
        if cid is None:
            continue
        by_id[cid] = c

    note_base = (
        f"CT certificates observed for query={domain}; count={len(by_id)}. "
        "OBSERVED_PASSIVE fact only — does not establish actor ownership."
    )
    if not by_id:
        rows.append(
            {
                "evidence_id": "",
                "family": fam,
                "indicator": domain,
                "observation_type": "ct",
                "value": "cert_count=0",
                "collected_utc": COLLECTED,
                "collection_mechanism": "HTTP GET crt.sh output=json",
                "originating_service": "crt.sh",
                "original_query": query,
                "raw_response_ref": rel,
                "sha256": sha,
                "provenance": "OBSERVED_PASSIVE",
                "confidence": "Moderate",
                "relationship_type": "OBSERVED_PASSIVE",
                "first_seen": "",
                "last_seen": "",
                "asn": "",
                "notes": note_base,
            }
        )
        return rows

    # emit compact summary row + up to 5 sample cert IDs
    nb = sorted(by_id.values(), key=lambda x: x.get("not_before") or "")
    first = nb[0].get("not_before") if nb else ""
    last = nb[-1].get("not_before") if nb else ""
    sample_ids = ",".join(str(c.get("id")) for c in nb[:5])
    rows.append(
        {
            "evidence_id": "",
            "family": fam,
            "indicator": domain,
            "observation_type": "ct",
            "value": f"cert_count={len(by_id)}; sample_ids={sample_ids}",
            "collected_utc": COLLECTED,
            "collection_mechanism": "HTTP GET crt.sh output=json",
            "originating_service": "crt.sh",
            "original_query": query,
            "raw_response_ref": rel,
            "sha256": sha,
            "provenance": "OBSERVED_PASSIVE",
            "confidence": "High",
            "relationship_type": "OBSERVED_PASSIVE",
            "first_seen": first,
            "last_seen": last,
            "asn": "",
            "notes": note_base + " Compare to vendor PRIMARY-SOURCE separately for CORROBORATED.",
        }
    )
    return rows


def collect_rdap(family: str, domain: str) -> list[dict]:
    fam = normalize_family(family)
    out_dir = PASSIVE / "rdap" / fam.lower()
    out_dir.mkdir(parents=True, exist_ok=True)
    url = f"https://rdap.org/domain/{urllib.parse.quote(domain)}"
    status, body = http_get(url)
    fname = f"rdap_{re.sub(r'[^a-zA-Z0-9._-]+', '_', domain)}_{COLLECTED.replace(':', '')}.json"
    path = out_dir / fname
    path.write_bytes(body)
    sha = hashlib.sha256(body).hexdigest()
    rel = str(path.relative_to(ROOT)).replace("\\", "/")
    value = f"http_status={status}"
    conf = "Moderate" if status == 200 else "Low"
    return [
        {
            "evidence_id": "",
            "family": fam,
            "indicator": domain,
            "observation_type": "rdap",
            "value": value,
            "collected_utc": COLLECTED,
            "collection_mechanism": "HTTP GET rdap.org/domain/{domain}",
            "originating_service": "rdap.org",
            "original_query": domain,
            "raw_response_ref": rel,
            "sha256": sha,
            "provenance": "OBSERVED_PASSIVE",
            "confidence": conf,
            "relationship_type": "OBSERVED_PASSIVE",
            "first_seen": "",
            "last_seen": "",
            "asn": "",
            "notes": "RDAP retrieval only. Not attribution. Registrar/CDN facts != actor ownership.",
        }
    ]


def main() -> None:
    PASSIVE.mkdir(parents=True, exist_ok=True)
    seeds = load_domain_seeds()
    print(f"seeds={len(seeds)} collected_utc={COLLECTED}")
    all_rows: list[dict] = []
    for fam, domain in seeds:
        # skip pure IP seeds for CT
        if re.match(r"^\d+\.\d+\.\d+\.\d+$", domain):
            continue
        print(f"CT {fam} {domain}")
        all_rows.extend(collect_ct(fam, domain))
        time.sleep(1.2)  # be polite to crt.sh
        print(f"RDAP {fam} {domain}")
        all_rows.extend(collect_rdap(fam, domain))
        time.sleep(0.8)
    append_manifest(all_rows)
    print(f"wrote {len(all_rows)} passive rows -> {MANIFEST}")
    print("NOTE: OBSERVED_PASSIVE != attribution. CDN overlaps remain ASSOCIATION_ONLY / INFRASTRUCTURE_OVERLAP until analyzed.")


if __name__ == "__main__":
    main()
