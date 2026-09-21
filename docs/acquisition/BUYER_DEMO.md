# Buyer Demo — Emerging Threat Watch

**Target:** fresh machine → clone → install → run → verify (≈10–15 minutes where realistic).

## Exact commands

```bash
git clone https://github.com/theworker02/emerging-threat-watch-1.git && cd emerging-threat-watch-1
ls investigations | head
head -40 METHODOLOGY.md
head -20 intelligence/combined_iocs.csv
# Confirm no malware binaries:
find . -name '*.exe' -o -name '*.dll' | head || echo 'none'
```

## Expected results

- Commands exit 0 (or documented skip for optional live-cloud steps).
- No secrets required for the minimal path.
- See TEST_EVIDENCE.md for recorded exit codes from this program’s verification runs.

## Out of scope for minimal demo

- Live production cloud credentials
- Shipping malware / real vehicle bus hardware (OpenDashCAN)
- Paid API quotas
