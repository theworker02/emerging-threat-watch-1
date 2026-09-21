# Research Plan — Emerging Threat Watch

**Cutoff:** 2026-09-19 · **Corpus retrieval:** 2026-09-19T18:07:48Z  
**Rule:** A new finding must change what is known, not merely add another URL repeating what is already known.

## Analytical theses (locked)

1. **Rapuncel** — three layers: GitHub/SEO distribution · Cruciferra/PUROSANGUE-like crypter/loader · Rapuncel stealer. Do not credit stealer authors with crypter capabilities (RAP-H-CRY).
2. **Settra** — ransomware binary ≠ human-operated intrusion. Separate ATT&CK matrices. WIN-LIVFRVQFMKO is a pivot, not backdating of Settra to 2024.
3. **RatHat** — Accessibility → Wireless ADB self-pair → shell UID; APK uninstall ≠ remediation.
4. **NodeRabbit** — enterprise developer specialization; mutable C2; VS Code signature mismatch; local Git hooks ≠ supply-chain without evidence.
5. **PollCat** — obfuscated JS RAT; co-disclosed with NodeRabbit; **non-authorship default**; open question = parallel / generation / specialized / co-deployed only.
6. **SynkLoader** — Teams IT-helpdesk enterprise intrusion; mixed-language modular loader; fake lock screen + tunneling.
7. **Showboat** — Linux telecom post-ex; historical activity may predate 2026 disclosure.

## Collection priorities

| Priority | Workstream | Required result |
|----------|------------|-----------------|
| P0 | Freeze primary evidence | HTML/screenshots/timestamps; claims+IOCs before pages change |
| P0 | CT / passive DNS | Cert IDs/SANs; A/AAAA history; first/last seen; ASN — seeds in `shared/queries/` |
| P0 | Hash enrichment | Settra SHA-256; RatHat APK SHA-256; NodeRabbit MD5→SHA-256 |
| P0 | Historical clustering | WIN-LIVFRVQFMKO + 193.5.65.114; Rapuncel domain chronology |
| P0 | PollCat / SynkLoader / Showboat primary freeze | Securelist dual-ref already held for PollCat; archive Expel + Lumen HTML |
| P1 | Lineage | Rapuncel↔BoryptGrab code-level; Cruciferra separation; NodeRabbit variants |
| P1 | **PollCat ↔ NodeRabbit comparison** | COMMON TECHNIQUE / lineage assessment only; non-authorship default; no IOC transfer |
| P1 | Platform forensics | RatHat ADB remnants; NodeRabbit Linux/WSL/VS Code/Git; Settra off-host |
| P1 | SynkLoader enterprise surface | Teams lure artifacts; PhishLocker detection hypotheses (UNVALIDATED) |
| P1 | Showboat dating gap | Document ≥2022 activity vs 2026 disclosure; Linux telecom hunting |
| P2 | Detection + IC3 | Only defensible findings; source-attributed IC3 narratives |

## Research hygiene

- Prefer PRIMARY freezes under `evidence/` before expanding narratives.
- Execute `shared/queries/certificate_transparency_seeds.csv` passively; promote UNVERIFIED→OBSERVED only after retrieval.
- Do **not** promote Cloudflare/Azure edge IPs as actor-owned.
- Keep case isolation except trust-surface / COMMON TECHNIQUE comparisons. PollCat pivots do **not** auto-seed NodeRabbit.

See `intelligence/priority-gaps.csv`, `docs/CANDIDATE_FAMILIES.md`, and per-family `gaps/priority-gaps.csv`.

## Sparse-corpus expansion (2026-09-21)

- Packages **16–30** and **43–66** added for young/obscure families; packages **31–42** retain prior deep-research freezes.
- Attribution stored as metadata only (`docs/attribution.md`, `attribution.csv`) — no nationality-based package trees.
- HEAVYGRAM and CHOSEN BRICK remain **separate** packages (contested alias).
- MiniUpdate / MiniJunk V2 / MiniBrowse **not merged** with existing MiniFast (11).
- NightLedger / ArcBridge / BridgeHead **not merged** with NodeRabbit/PollCat.
- Open: Cato Foxveil PRIMARY (WAF), Mandiant UNC1069 PRIMARY HTML, PhantomPyramid/ZeronetKit/PaperGrabber/PowerLoader/Atlas RAT PRIMARY URLs, IOC harvest for zero-IND PRIMARY_FROZEN packages, APT36 Poseidon Linux branch.
