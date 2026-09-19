# `# shepherd-persist` — Detection Material Catalog

**PRIMARY behavior:** Kaspersky GReAT Securelist 2026-09-01 — NodeRabbit V3 `persist:project:inject` appends a marked launcher to `.git/hooks/post-merge` and `post-checkout`. Marker string: `# shepherd-persist` (also referenced as `# shepherd-persist;`).

**Cutoff:** 2026-09-19  
**Scope:** Local Git hook persistence — **not** demonstrated repository supply-chain propagation in primary.

---

## Provenance split (mandatory)

| Material class | Provenance | Use |
|----------------|------------|-----|
| Marker existence + hook targets (`post-merge`, `post-checkout`) | **PRIMARY** (Kaspersky) | Claim / report / hunting seed |
| Community KQL, Sigma, GitHub Gists, blog “detections” for `shepherd-persist` | **SECONDARY** | Optional detection engineering input only — do **not** elevate to PRIMARY claims |
| ETW independent observation of marker on a victim disk | **OBSERVED** (none yet) | Would upgrade verification |

---

## PRIMARY facts (for claims)

- Marker is applied to **local** hooks (normally not committed).  
- Do **not** call this a supply-chain compromise without evidence of committed/pushed hooks or upstream repo compromise.  
- Cross-ref: `docs/git-hook-persistence.md`, `NRB-CLAIM-0009`.

---

## SECONDARY detection material (catalog only — not validated by ETW)

Record any community queries found during research here; do not copy unverified rule bodies into production packs without review.

| ID | Type | Location / reference | Status | Notes |
|----|------|----------------------|--------|-------|
| NRB-DET-SEC-0001 | Placeholder | Community KQL/GitHub searches for `shepherd-persist` | SECONDARY / UNVALIDATED | Populate when a specific public query is cited; verify against PRIMARY marker string |

---

## Hunting seed (PRIMARY-derived, unvalidated rule)

Search developer workstations for the literal substring `shepherd-persist` under `.git/hooks/`. Treat hits as **suspicious until explained**, not automatic NodeRabbit confirmation.
