# PollCat — Research Notes

## Locked thesis

See family `README.md`. Co-disclosure with NodeRabbit is **not** shared authorship.

## Primary freeze

- `SOURCE-POL-001` → Securelist 2026-09-01 article (same HTML bytes as NodeRabbit `PS-NRB-001`).
- Dual-reference: `evidence/primary-sources/pollcat/` dual-lists `../noderabbit/securelist-noderabbit-2026-09-01.html`.
- Do **not** merge PollCat and NodeRabbit ledgers, IOCs, or IC3 packages.

## Deep pass 2026-09-19

- Full PollCat C2/persistence/command mining → `docs/deep-pass/2026-09-19-deep-passive.md`
- `POL-IND-0001`–`0015` transcribed; RankChallenge MD5 is PollCat (not NRB)
- Stronger documented structural overlap: PollCat ↔ MiniFast/Retrograde (not NodeRabbit)
- Lineage note: `shared/lineage/pollcat-noderabbit-lineage-note.md`

## Attribution correction (2026-09-19 staging follow-up)

Hunt matrices sometimes place `colorized_terminal` next to PollCat. **PRIMARY (Kaspersky) attributes `colorized_terminal` / `pretty-log@2.1.0` to NodeRabbit** (local `node_modules` bundle; public registry absent / no malicious 2.1.0). PollCat IOCs stay on `RankChallenge-react` / `requireObjects.js` / NetSync /gate paths — see NRB-IND-0042–0044 and `shared/methodology/UNCONVENTIONAL_STAGING_OSINT.md` case note. Do not reintroduce as POL-*.

## Open question (P1)

Parallel implant vs generation vs specialized payload vs co-deployment only — answer only with direct connecting evidence. Current evidence favors **co-deployment / shared actor toolkit** over shared implant lineage.

## Gaps

- Secondary corpus still thin
- MD5→SHA-256 for RankChallenge unresolved
- NightLedger (July 2026) = Mirage Kitten context only
