# Phase 1 Baseline Report — Settra

**Case ID:** settra  
**Report date (UTC):** 2026-09-19

## 1. Evidence Collected
9 ledger rows from Cynet primary RE and Huntress IR.

## 2. Sources Reviewed
Cynet blog + Settra hub page; Huntress MeshAgent variant post.

## 3. Indicators Catalogued
Incident-scoped MeshAgent IPs; ransom note filenames; `.locked` / `.locked_wip` extensions. Encryptor hashes not yet extracted into ledger (pending full IOC table from primary materials).

## 4. Claims Independently Corroborated
`.locked` extension and enterprise ransomware framing appear in both Cynet and Huntress (**CORROBORATED** at reporting level). ETW has not detonated samples.

## 5. Unresolved Claims
Universal initial-access method; complete public hash list; Tor infrastructure inventory; affiliate structure.

## 6. Contradictions
None material yet. Note: ransom note claims of theft vs encryptor lacking exfil is an **intentional operational split**, not a source contradiction (Cynet).

## 7. Promising Research Leads
Extract full Cynet IOC/ATT&CK appendix; compare Huntress vs Cynet encryptor descriptions; ransom-note corpus; Hyper-V / VSS behavioral detections (UNVALIDATED).

## 8. Safety Limitations
No ransomware execution; no Tor negotiation interaction; no payment or victim contact.

## 9. Recommended Phase 2
IOC harvesting from primary appendices; detection drafts for note filenames and extension patterns; ATT&CK mapping strictly from evidenced behaviors; separate IC3 brief if/when reportable victim-agnostic infrastructure is validated.