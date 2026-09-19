# PollCat primary source — dual reference

**Do not re-fetch** the Securelist HTML unless the archived bytes are missing or integrity fails.

| Field | Value |
|-------|-------|
| `SOURCE-POL-001` | Securelist Mirage Kitten / NodeRabbit / PollCat |
| Canonical bytes | `../noderabbit/securelist-noderabbit-2026-09-01.html` |
| Manifest | `PS-POL-001` (dual-lists same SHA-256 as `PS-NRB-001`) |
| Case rule | Dual-list in source indexes; **do not merge** pollcat and noderabbit cases |

Verified string presence: `PollCat` appears in the archived HTML.
