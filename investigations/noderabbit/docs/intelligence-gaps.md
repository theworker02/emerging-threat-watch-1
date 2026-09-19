# NodeRabbit Intelligence Gaps (updated 2026-09-19 deep pass)

| Gap | Priority | Current evidence | Required evidence | Status |
|-----|----------|------------------|-------------------|--------|
| Complete hash list from Kaspersky IOC section | P0 | MD5s transcribed; PolySwarm SHA-256 RELATED_SAMPLE only | MD5↔SHA-256 map for archives | OPEN |
| Passive Azure hostname status | P1 | Domains published; many CT=0 on Azure FQDNs | Passive DNS / HTTP metadata only | OPEN |
| PollCat boundary clarity in ETW corpus | P1 | Dual-list Securelist; POL-IND filled; RankChallenge retagged | Maintain isolation | PARTIAL |
| Independent confirmation of Mirage Kitten attribution | P2 | Kaspersky high confidence | External corroboration | OPEN |
| Additional coding-challenge lures beyond TaskFlow | P1 | Multiple ZIP MD5s; Wayback S3 sparse | Hunt public archives carefully/passively | OPEN |
| Non-Azure CT chronology | P0 | msmanagementgrp CT=49; health-* CT batch | Ongoing revisit | PARTIAL |
| GitHub shepherd-persist leakage | P2 | Logged-out result_count=0 | Optional authenticated search | CLOSED negative |
