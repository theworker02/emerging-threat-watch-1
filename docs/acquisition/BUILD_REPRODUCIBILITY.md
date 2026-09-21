# Build Reproducibility — Emerging Threat Watch

**Date:** 2026-09-21

## Fresh machine path

```
git clone https://github.com/theworker02/emerging-threat-watch-1.git && cd emerging-threat-watch-1
ls investigations | head
head -40 METHODOLOGY.md
head -20 intelligence/combined_iocs.csv
# Confirm no malware binaries:
find . -name '*.exe' -o -name '*.dll' | head || echo 'none'
```

## Assumptions

- Stack: Documentation / CTI corpus (Markdown, CSV, frozen HTML/PDF evidence); no application runtime
- No machine-specific absolute paths should be required.
- Cloud credentials are optional unless exercising live provider features.

## Known reproducibility limits

Documented in KNOWN_LIMITATIONS.md and project-specific diligence.
