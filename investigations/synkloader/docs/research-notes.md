# SynkLoader — Research Notes

## Locked thesis

Modular mixed-language loader; Teams IT-helpdesk phishing; fake lock screen; tunneling; late-July compile window per Expel.

## Primary freeze

- `SOURCE-SYN-001` / `PS-SYN-001` → Expel blog HTML frozen locally.
- File: `evidence/primary-sources/synkloader/expel-synkloader-2026-08-20.html`
- SHA-256: `0e0864449f6fe6b17ce216e639c5b2c9066202b6f58cd19cdc21b00b1d6b9cd9` (1,389,994 bytes)
- Deep-pass notes: `docs/deep-pass-2026-09-19.md`

## Progress (2026-09-19 deep-pass)

- Claims expanded through `SYN-CLAIM-0011`
- Published IOCs `SYN-IND-0001`–`SYN-IND-0025`
- Passive CT/RDAP/urlscan rows under `SYN-PO-*`

## Gaps

- Dedicated pDNS still open
- Ransomware-follow-on hypothesis in secondary coverage is **not** established by ETW
- Teams sender identity partially redacted in primary

## Technique comparator — Matanbuchus (NOT lineage)

**Matanbuchus** (and related AstarionRAT MaaS packaging) is tracked as a **CANDIDATE technique comparator** for SynkLoader — Teams phishing delivery and ChaCha20 crypto tradecraft — **not** as ETW-attributed SynkLoader lineage or shared authorship.

- `authorship_link` SynkLoader ↔ Matanbuchus = **NOT_ESTABLISHED**
- Catalog: [`docs/CANDIDATE_FAMILIES.md`](../../../docs/CANDIDATE_FAMILIES.md) · [`docs/TECHNIQUE_COMPARATORS.md`](../../../docs/TECHNIQUE_COMPARATORS.md)
- Do not promote Matanbuchus IOCs into `SYN-*` ledgers without independent primary evidence and case-isolation review
