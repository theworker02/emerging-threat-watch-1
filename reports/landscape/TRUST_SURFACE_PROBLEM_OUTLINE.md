# The Trust-Surface Problem — Landscape Outline (Not a Full Report)

**Status:** Outline only — PDF deferred  
**Cutoff:** 2026-09-19  
**Rule:** Compare four cases **without claiming relatedness**. Technique similarity ≠ common authorship.  
**Data:** `research/trust-surface-matrix.csv` / `intelligence/trust-surface-matrix.csv`

## Thesis (draft)

Modern intrusion chains increasingly **borrow trust** from components defenders already allow: signed binaries, attested drivers, OS accessibility/debug features, developer runtimes/IDEs, legitimate RMM, and cloud hosts. Detection that keys on “unsigned + unknown” systematically under-weights these stages.

## Proposed sections

1. **Definition of trust classes** — TRUSTED BINARY | SIGNED DRIVER | OS FEATURE | DEVELOPER TOOL | RMM | CLOUD SERVICE | SECURITY/DEBUGGING FEATURE | OPEN-SOURCE DUAL-USE | USER/BRAND TRUST  
2. **Rapuncel vignette** — Brand/GitHub trust → Microsoft vsdbg sideload → WHCP Alinubx/CcProtect → optional Cruciferra commodity layer (RAP-H-CRY)  
3. **Settra vignette** — Operator dual-use (MeshAgent, Mimikatz, BYOVD) **vs** password-gated encryptor (separate ATT&CK matrices)  
4. **RatHat vignette** — Accessibility + Wireless ADB developer feature (shell UID 2000); FRP dual-use; `/dev/input` via `getevent`; technique parallel to ToxicPanda/RedHook (**COMMON TECHNIQUE only**). Wording: Android + Linux-kernel interfaces — **not** “Linux malware.”  
5. **NodeRabbit vignette** — S3 + Node + Azure blend + VS Code publisher-name borrow + local Git hooks (not supply-chain by default); **Linux** `@reboot` cron under fake `microsoft-edge-update` / `intel-dsa` / `~/.local/share` + V3 WSL bridge (`wscript`→`wsl`)  
6. **Cross-case comparison table** — which trust class appears where (no operator merge)  
7. **Defender implications** — allowlists of applications not signatures; RMM allowlists; developer-mode enterprise policy; extension signing; driver blocklist lag  
8. **Intelligence gaps** — primary fetch failures; unverified hashes; operator-model ambiguity  
9. **What this report will never claim** — shared actors across RAP/SET/RAT/NRB without `campaign-relationships.csv` defended links  

## Non-goals

- Final PDF  
- IC3 combined filing  
- Adversary-simulation as primary evidence  
