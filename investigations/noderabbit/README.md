# NodeRabbit Investigation

**Case ID:** `noderabbit`  
**Independence:** Isolated from Rapuncel, Settra, RatHat, PollCat, SynkLoader, and Showboat.

## Research Emphasis
- Fake recruiter / coding-challenge social engineering
- Locally bundled trojanized npm packages (`colorized_terminal`, `pretty-log` @ 2.1.0)
- Cross-platform Node.js RAT execution
- Persistence: Run keys, cron, LaunchAgents, fake VS Code extension, Git hooks
- Azure App Service C2 + AES-256-GCM
- Mirage Kitten attribution **as reported by Kaspersky** (do not invent)
- PollCat is a **related disclosure but separate case** in the same Kaspersky paper — track carefully; **do not merge IOCs or assume shared authorship** without direct linking evidence. Comparison allowed only as `COMMON TECHNIQUE` / lineage assessment with **non-authorship default**.

## Status
Phase 1 baseline seeded from Kaspersky Securelist primary (2026-09-01). PollCat dual-lists the same HTML as `PS-POL-001` / `SOURCE-POL-001` — cases remain separate.
