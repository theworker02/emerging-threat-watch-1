# Emerging Threat Watch — Project-Specific Diligence

**Date:** 2026-09-21

## IOC provenance

- Vocabulary: PRIMARY-SOURCE, OBSERVED/OBSERVED_PASSIVE, CORROBORATED, SECONDARY, INFERRED, UNVERIFIED (see METHODOLOGY.md).
- Per-family CSV indices with provenance columns.

## Malware-report sources

- Frozen vendor HTML/PDF under `evidence/primary-sources/` — **third-party copyrights**.
- Passive observations under `evidence/passive-observations/`.

## Redistribution rights

- ETW proprietary LICENSE covers original packaging/analysis/compilation as claimed.
- Does **not** reclaim vendor copyrights.
- Bulk republication of vendor HTML/PDF — **REQUIRES_LEGAL_REVIEW**.

## Vendor-report copyrights

- Remain with publishers (Expel, Huntress, Kaspersky/Securelist, ESET, FBI FLASH, etc. as present in evidence).

## Screenshots / archive provenance

- Documented via manifests / `.meta.json` / hashes where present.
- Treat as third-party content unless proven otherwise.

## Detection-rule licenses

- Mostly placeholders (`condition: false`) authored as ETW stubs — not validated for production detection.
- No third-party YARA/Sigma attributions observed in placeholder files.

## Threat-intelligence source restrictions

- Follow vendor terms; underground OSINT methodology docs warn against fabricating license access.
- LE packages are templates — not auto-submit.

## Observed vs attributed findings

- Methodology requires claim ledgers and case isolation.
- PRIMARY transcription ≠ OBSERVED infrastructure.

## Hard exclusions from acquisition assets

- **Do NOT** package malware binaries, stolen credentials, live unauthorized access, or operational malicious infrastructure.
- Prior scan: no malware binaries found by extension/magic; keep it that way.
