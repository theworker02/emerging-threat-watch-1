# Settra Investigation

**Case ID:** `settra`  
**Independence:** Isolated from Rapuncel, RatHat, and NodeRabbit.

## Research Emphasis
- Password-gated / analysis-resistant outer loader (`--pass`)
- Inner encryptor: recovery destruction, Hyper-V shutdown, anti-forensics
- Ransom artifacts (`RESTORE_FILES.txt` / `.html`, Tor negotiation)
- Cryptography model (per-file keys, 4096-bit RSA wrap; offline decrypt secret)
- Separation of exfiltration phase vs encryption phase
- Enterprise precursors (RMM/MeshAgent, BYOVD) only when evidenced (Huntress)

## Status
Phase 1 baseline seeded from Cynet primary + Huntress secondary.