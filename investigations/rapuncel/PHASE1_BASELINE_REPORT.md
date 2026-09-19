# Phase 1 Baseline Report — Rapuncel

**Case ID:** rapuncel  
**Report date (UTC):** 2026-09-19  
**Status:** Draft — baseline acquisition

## 1. Evidence Collected
15 evidence ledger rows (`RAP-EV-0001`–`0015`): primary title citation, secondary journalism, seeded unverified hashes, reported IOCs (IP/domain/GitHub org), lineage claims.

## 2. Sources Reviewed
LastPass/Delphos (title via relay); BleepingComputer; CyberInsider; TechTimes; IBTimes SG; Trend Micro BoryptGrab (comparator only).

## 3. Indicators Catalogued
5 seeded SHA-256 (**UNVERIFIED**); `2.26.126.50`; `albinofennel.com`; `github.com/LastPass-Authenticator`; filenames/paths for sideload/driver chain.

## 4. Claims Independently Corroborated
**None as OBSERVED.** Multiple secondaries consistently relay the same primary narrative (SEO GitHub → sideload → Alinubx → stealer). Consistency ≠ independent corroboration.

## 5. Unresolved Claims
Exact hash provenance; full primary document retrieval; whether infrastructure still resolves/serves related content; precise ABE “bypass” mechanism wording; MaaS operator identity.

## 6. Contradictions
- Secondary articles sometimes say “variant of BoryptGrab” vs “insufficient to conclude same group” (CyberInsider). Track as **qualification variance**, not binary contradiction.
- Beeble first-person “I analyzed” tone appears secondary/opinionated; treat as low-weight.

## 7. Promising Research Leads
1. Locate and archive the original LastPass/Delphos joint report.  
2. Passive DNS/CT/RDAP for `albinofennel[.]com` and related redirectors.  
3. Web-archive fraudulent GitHub orgs.  
4. Build BoryptGrab comparison from Trend Micro primary IOCs vs Rapuncel primary IOCs once obtained.  
5. Trace seeded hashes via lawful VT/malware-repo metadata only.

## 8. Safety Limitations
No sample execution; no C2 interaction; no authentication to attacker infra; hashes remain metadata-only.

## 9. Recommended Phase 2
Passive infrastructure snapshot; primary document acquisition; hash source tracing; infection-chain observability checks; detection drafting labeled UNVALIDATED; lineage matrix update after primary IOC extraction.

**No speculative attribution.**