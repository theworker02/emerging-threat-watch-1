# Phase 1 Baseline Report — NodeRabbit

**Case ID:** noderabbit  
**Report date (UTC):** 2026-09-19

## 1. Evidence Collected
9 ledger rows from Kaspersky Securelist primary.

## 2. Sources Reviewed
Kaspersky Securelist; The Hacker News; PolySwarm summary.

## 3. Indicators Catalogued
Challenge ZIP MD5; S3 URL; three Azure C2 hostnames; trojanized package names; implant path; local bind port.

## 4. Claims Independently Corroborated
Secondary outlets relay Kaspersky. ETW has not executed Node payloads or contacted Azure C2.

## 5. Unresolved Claims
Full remaining IOC table; current infra liveness; breadth of recruiter personas; PollCat overlap handling.

## 6. Contradictions
None material. Ensure secondary “Iranian hackers” headlines are tagged as journalism paraphrasing Kaspersky’s Mirage Kitten tracking—not ETW attribution.

## 7. Promising Research Leads
Passive Azure/S3 status; developer-persistence detections (VS Code/Git hooks) UNVALIDATED; package-name hunting in coding-test archives; AES-GCM C2 request shape hunting.

## 8. Safety Limitations
No running of coding-challenge archives; no C2 beacons; no LinkedIn engagement with suspected personas.

## 9. Recommended Phase 2
Finish IOC extraction from Securelist IOC section; STIX bundle; Sigma for EdgeUpdate-style persistence paths; separate PollCat evidence track; IC3 brief only with validated indicators.