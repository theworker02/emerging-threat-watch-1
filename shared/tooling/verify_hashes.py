#!/usr/bin/env python3
"""Validate hash string formats. Does not download or execute samples."""
from __future__ import annotations
import argparse
import re
import sys

PATTERNS = {
    "md5": re.compile(r"^[a-fA-F0-9]{32}$"),
    "sha1": re.compile(r"^[a-fA-F0-9]{40}$"),
    "sha256": re.compile(r"^[a-fA-F0-9]{64}$"),
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("hash")
    ap.add_argument("--type", choices=sorted(PATTERNS), default="sha256")
    args = ap.parse_args()
    ok = bool(PATTERNS[args.type].match(args.hash.strip()))
    print("OK" if ok else "INVALID")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())