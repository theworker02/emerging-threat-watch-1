#!/usr/bin/env python3
"""Security gate controller for Tier-1 autonomous jobs.

Tier 0 work does not use this tool.
Tier 2 (prohibited) actions must never be submitted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GATES = ROOT / "gates"
QUEUE = GATES / "queue"
APPROVED = GATES / "approved"
DENIED = GATES / "denied"
COMPLETED = GATES / "completed"
PAYLOADS = GATES / "payloads"

TIER1_TYPES = {
    "sandbox_detonate",
    "sample_download",
    "memory_dump",
    "infra_scan_expand",
    "abusech_submit",
    "panel_snapshot_fleet",
}

# Never allow these to be staged
TIER2_BLOCKLIST = re.compile(
    r"(panel.?login|c2.?command|exploit|brute.?force|ransomware.?negotiat|"
    r"buy.?malware|discord.?token|credential.?stuff)",
    re.I,
)


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def ensure_dirs() -> None:
    for d in (QUEUE, APPROVED, DENIED, COMPLETED, PAYLOADS):
        d.mkdir(parents=True, exist_ok=True)
    readme = GATES / "README.md"
    if not readme.exists():
        readme.write_text(
            "# Security gates (Tier 1)\n\n"
            "See `shared/methodology/GATED_AUTONOMY.md`.\n\n"
            "- `queue/` — pending your approval\n"
            "- `approved/` — approved, ready to run\n"
            "- `denied/` — rejected\n"
            "- `completed/` — finished runs\n"
            "- `payloads/` — job-specific JSON/YAML referenced by jobs\n",
            encoding="utf-8",
        )


def next_id() -> str:
    ensure_dirs()
    existing = list(QUEUE.glob("GATE-*.json")) + list(APPROVED.glob("GATE-*.json"))
    existing += list(DENIED.glob("GATE-*.json")) + list(COMPLETED.glob("GATE-*.json"))
    nums = []
    for p in existing:
        m = re.match(r"GATE-(\d+)", p.stem)
        if m:
            nums.append(int(m.group(1)))
    n = max(nums, default=0) + 1
    return f"GATE-{n:04d}"


def cmd_submit(args: argparse.Namespace) -> None:
    ensure_dirs()
    if args.type not in TIER1_TYPES:
        raise SystemExit(f"Unknown or non-Tier-1 type: {args.type}. Allowed: {sorted(TIER1_TYPES)}")
    blob = f"{args.type}|{args.family}|{args.summary}|{args.payload or ''}"
    if TIER2_BLOCKLIST.search(blob):
        raise SystemExit("Refused: job resembles Tier-2 prohibited activity.")
    gid = next_id()
    job = {
        "gate_id": gid,
        "tier": 1,
        "type": args.type,
        "family": args.family,
        "summary": args.summary,
        "payload_path": args.payload or "",
        "status": "pending",
        "submitted_utc": utc(),
        "submitted_by": args.by or "agent",
        "approved_utc": None,
        "approved_by": None,
        "denied_utc": None,
        "completed_utc": None,
        "run_notes": "",
        "content_sha256": hashlib.sha256(blob.encode("utf-8")).hexdigest(),
    }
    path = QUEUE / f"{gid}.json"
    path.write_text(json.dumps(job, indent=2) + "\n", encoding="utf-8")
    print(f"SUBMITTED {gid} -> {path}")
    print("Awaiting human approval: python shared/tooling/gate_ctl.py list")


def _load(gid: str) -> tuple[Path, dict]:
    for folder in (QUEUE, APPROVED, DENIED, COMPLETED):
        p = folder / f"{gid}.json"
        if p.exists():
            return p, json.loads(p.read_text(encoding="utf-8"))
    raise SystemExit(f"Gate not found: {gid}")


def cmd_list(_: argparse.Namespace) -> None:
    ensure_dirs()
    print(f"{'ID':12} {'STATUS':10} {'TYPE':22} {'FAMILY':12} SUMMARY")
    for folder, status in (
        (QUEUE, "pending"),
        (APPROVED, "approved"),
        (DENIED, "denied"),
        (COMPLETED, "completed"),
    ):
        for p in sorted(folder.glob("GATE-*.json")):
            job = json.loads(p.read_text(encoding="utf-8"))
            print(
                f"{job['gate_id']:12} {status:10} {job['type'][:22]:22} "
                f"{(job.get('family') or '')[:12]:12} {job.get('summary', '')[:60]}"
            )


def cmd_approve(args: argparse.Namespace) -> None:
    path, job = _load(args.gate_id)
    if path.parent != QUEUE:
        raise SystemExit(f"{args.gate_id} is not pending (in {path.parent.name})")
    job["status"] = "approved"
    job["approved_utc"] = utc()
    job["approved_by"] = args.by or "human"
    dest = APPROVED / path.name
    dest.write_text(json.dumps(job, indent=2) + "\n", encoding="utf-8")
    path.unlink()
    print(f"APPROVED {args.gate_id} by {job['approved_by']} at {job['approved_utc']}")
    print(f"Run with: python shared/tooling/gate_ctl.py run {args.gate_id}")


def cmd_deny(args: argparse.Namespace) -> None:
    path, job = _load(args.gate_id)
    if path.parent != QUEUE:
        raise SystemExit(f"{args.gate_id} is not pending")
    job["status"] = "denied"
    job["denied_utc"] = utc()
    job["run_notes"] = args.reason or ""
    dest = DENIED / path.name
    dest.write_text(json.dumps(job, indent=2) + "\n", encoding="utf-8")
    path.unlink()
    print(f"DENIED {args.gate_id}")


def cmd_run(args: argparse.Namespace) -> None:
    """Mark approved job completed and print run contract.

    Actual lab orchestration (CAPE/ANY.RUN) is environment-specific.
    This command refuses unless status=approved, then writes a run receipt.
    """
    path, job = _load(args.gate_id)
    if path.parent != APPROVED and not args.force_completed_replay:
        raise SystemExit(
            f"{args.gate_id} must be in gates/approved/ (currently {path.parent.name}). "
            "Approve first."
        )
    if job.get("type") not in TIER1_TYPES:
        raise SystemExit("Invalid type")
    # Dry-run contract for operators / future lab runners
    receipt = {
        "gate_id": job["gate_id"],
        "executed_utc": utc(),
        "type": job["type"],
        "family": job["family"],
        "payload_path": job.get("payload_path"),
        "approved_by": job.get("approved_by"),
        "approved_utc": job.get("approved_utc"),
        "operator_action": (
            "EXECUTE_IN_ISOLATED_LAB — connect this gate to your CAPE/ANY.RUN/Triage runner. "
            "ETW does not auto-detonate. After lab finishes, ingest PCAP/strings with "
            "extract_ips_from_text.py and rebuild CTI-Evidence-Repository."
        ),
    }
    job["status"] = "completed"
    job["completed_utc"] = receipt["executed_utc"]
    job["run_notes"] = json.dumps(receipt)
    dest = COMPLETED / path.name
    dest.write_text(json.dumps(job, indent=2) + "\n", encoding="utf-8")
    if path.parent == APPROVED:
        path.unlink()
    receipt_path = COMPLETED / f"{job['gate_id']}.receipt.json"
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    print(f"Receipt -> {receipt_path}")


def main() -> None:
    ensure_dirs()
    ap = argparse.ArgumentParser(description=__doc__)
    sp = ap.add_subparsers(dest="cmd", required=True)

    s = sp.add_parser("submit", help="Stage Tier-1 job (agent)")
    s.add_argument("--type", required=True, choices=sorted(TIER1_TYPES))
    s.add_argument("--family", required=True)
    s.add_argument("--summary", required=True)
    s.add_argument("--payload", default="")
    s.add_argument("--by", default="agent")
    s.set_defaults(func=cmd_submit)

    sp.add_parser("list", help="List gates").set_defaults(func=cmd_list)

    a = sp.add_parser("approve", help="Approve pending gate (YOU)")
    a.add_argument("gate_id")
    a.add_argument("--by", default="human")
    a.set_defaults(func=cmd_approve)

    d = sp.add_parser("deny", help="Deny pending gate (YOU)")
    d.add_argument("gate_id")
    d.add_argument("--reason", default="")
    d.set_defaults(func=cmd_deny)

    r = sp.add_parser("run", help="Execute approved gate contract")
    r.add_argument("gate_id")
    r.add_argument("--force-completed-replay", action="store_true")
    r.set_defaults(func=cmd_run)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
