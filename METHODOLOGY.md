# Methodology

## Principles

1. **Evidence first. Conclusions second.**
2. Treat every assertion as requiring provenance.
3. Do not assume existing reporting is correct.
4. Never convert another researcher's observation into an independent observation.
5. Prefer passive collection. Do not execute unknown binaries on a normal workstation.
6. **Case isolation:** do not cross-pollinate findings between Rapuncel, Settra, RatHat, NodeRabbit, PollCat, SynkLoader, and Showboat without direct linkage evidence.

## Provenance Classifications

| Code | Meaning |
|------|---------|
| `OBSERVED` / `OBSERVED_PASSIVE` | Independently observed by this investigation (passive methods use `OBSERVED_PASSIVE`) |
| `PRIMARY-SOURCE` | Directly from the original analyzing organization/researcher |
| `CORROBORATED` | ≥2 sufficiently independent sources, or ETW passive evidence supports a vendor claim |
| `SECONDARY` | Reported but not the original source |
| `INFERRED` | Derived from evidence; not directly demonstrated |
| `UNVERIFIED` | Claim exists; insufficient evidence |
| `CONTRADICTED` | Reliable evidence conflicts |
| `ASSOCIATION_ONLY` | Weak co-occurrence (e.g. same hosting provider) — not ownership |
| `INFRASTRUCTURE_OVERLAP` | Shared technical artifact (e.g. same IP) — not actor identity |

**Autonomy policy:** Permitted passive collection runs without per-query approval. See [`shared/methodology/AUTONOMOUS_COLLECTION_POLICY.md`](shared/methodology/AUTONOMOUS_COLLECTION_POLICY.md). Prohibited: malware execution, C2 interaction, auth to attacker systems, exploitation. Underground / dark-web / commodity-RAT OSINT (forums, Telegram, private E2EE as CTI-only): [`shared/methodology/UNDERGROUND_AND_COMMODITY_RAT_OSINT.md`](shared/methodology/UNDERGROUND_AND_COMMODITY_RAT_OSINT.md) (alias [`APT_AND_DARKWEB_OSINT.md`](shared/methodology/APT_AND_DARKWEB_OSINT.md)). Unconventional staging (npm/GitHub/paste/open buckets/APK mirrors/bounded Shodan): [`shared/methodology/UNCONVENTIONAL_STAGING_OSINT.md`](shared/methodology/UNCONVENTIONAL_STAGING_OSINT.md). High-fidelity takedown / enforcement evidence (sandbox PCAP is human-lab / licensed-platform only): [`shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md`](shared/methodology/TAKEDOWN_AND_ENFORCEMENT_EVIDENCE.md).

Retrieving a vendor article preserves a `PRIMARY-SOURCE` artifact. It does **not** create `OBSERVED_PASSIVE` infrastructure.
## Confidence Levels

Every analytical conclusion receives **High**, **Moderate**, or **Low** confidence with an explicit rationale.

## Source Hierarchy

1. Independently collected passive evidence  
2. Original security-research publications  
3. Official vendor advisories  
4. Platform records (GitHub, npm, Play listings, etc.) where lawful  
5. Malware analysis platforms (lawful/authorized access only)  
6. VirusTotal / equivalent reputation data  
7. Passive DNS / certificate transparency / RDAP / WHOIS  
8. Web archives  
9. Established security journalism  
10. Secondary blogs / social posts  

Never use a secondary article as proof when the primary research is available. Repeated secondary coverage is **not** independent corroboration.

## Claim Ledgers & Research Cutoff

Every sourced technical assertion is recorded as a **claim** (`shared/schemas/claim.schema.json`) in `investigations/<family>/claims/claims-ledger.csv`.

Traceability path: **Report → Claim → Evidence → Original source.**

Claim IDs: `RAP-CLAIM-####` / `SET-CLAIM-####` / `RAT-CLAIM-####` / `NRB-CLAIM-####` / `POL-CLAIM-####` / `SYN-CLAIM-####` / `SHO-CLAIM-####`.

**v1 corpus freeze cutoff:** 2026-09-19. Every claim sets `cutoff_applies=true` and records both publication date and `retrieval_date_utc`.

Source classes on claims: `PRIMARY` | `INDEPENDENT_CORROBORATION` | `SECONDARY` | `UNVERIFIED`. Same-researcher reprints share one lineage via `derives_from`. DNS resolution ≠ malicious.

Ecosystem modeling (crypters, delivery MaaS, operator tooling) is encouraged. Cross-family **trust-surface / COMMON TECHNIQUE** comparison is allowed without claiming shared authorship (`research/trust-surface-matrix.csv`). IOC/attribution transfer still requires direct connecting evidence (`CASE_ISOLATION.md`).

## Per-Family Research Emphases

### Rapuncel
- GitHub/SEO distribution ecosystem  
- Redirect and traffic-distribution infrastructure  
- DLL sideloading (`vsdbg.exe` / `vsdbg.dll`)  
- Alinubx.sys / BYOVD defensive implications  
- Browser credential interaction claims (precise wording)  
- **Lineage assessment vs BoryptGrab** (probabilistic; no forced authorship)

### Settra
- Password-gated / analysis-resistant outer loader  
- Inner encryptor behavior and recovery destruction  
- Ransom note / Tor negotiation artifacts  
- Separation of exfiltration vs encryption phases  
- Enterprise intrusion precursors (RMM, BYOVD) **only when evidenced**  
- Encryption cryptography model (per-file keys, RSA wrap)

### RatHat
- APK / DEX metadata and anti-analysis packaging  
- Permission and Accessibility-service abuse  
- Wireless Debugging / local ADB self-pairing  
- Go agent and FRP reverse-proxy components  
- Reported generative-AI UI automation architecture  
- Overlay / OTP / raw touch-input credential theft claims  
- Persistence after apparent uninstall

### NodeRabbit
- Fake recruiter / coding-challenge social engineering  
- Locally bundled trojanized npm packages  
- Cross-platform Node.js execution model  
- Persistence (Run keys, cron, LaunchAgents, VS Code, Git hooks)  
- Azure-hosted C2 and crypto (AES-256-GCM)  
- Relationship to PollCat / Mirage Kitten **only as reported + evidenced**  
- Developer-workflow blending

### PollCat
- Obfuscated JavaScript cross-platform RAT (Kaspersky primary)  
- Coding-challenge / recruiter delivery ecosystem (COMMON TECHNIQUE class with NodeRabbit — **not** automatic authorship)  
- `RankChallenge-react` lure and requireObjects.js startup path  
- Persistence paths as published (NetSync / cron / LaunchAgent)  
- **P1 lineage question:** parallel implant vs generation vs specialized payload vs co-deployment only — **non-authorship default**  
- Sparse public corpus → prioritize autonomous CT/pDNS/archive collection  
- NightLedger = Mirage Kitten ops context only (not PollCat≡NodeRabbit proof)

### SynkLoader
- Windows enterprise social-engineering intrusion  
- Microsoft Teams / IT-helpdesk phishing  
- Modular mixed-language / memory-resident loader  
- Fake lock-screen credential theft and tunneling  
- Late-July 2026 compile/distribution window **as Expel reports**

### Showboat
- Linux modular post-exploitation (telecom / ISP surface)  
- Shell, file transfer, SOCKS5 / proxy-style capabilities **as published**  
- Historical activity (≥ mid-2022) vs 2026 disclosure dating gap  
- Do not invent victim identities or IOCs

## Safety Boundary

Do **not**: deploy malware; infect systems; attempt unauthorized access; authenticate to attacker infrastructure; send C2 commands; create improved malware; execute unknown binaries on a researcher's normal workstation.

Prefer inert evidence metadata. Samples, if retained, remain outside public git and are handled only in isolated analysis environments.

## Reproducibility

Another researcher must be able to answer: origin of each indicator; observation time; reporting party; independent verification status; supporting evidence; confidence; and changelog between report versions.

## Landscape Report Rules

`EMERGING_THREAT_LANDSCAPE_REPORT` and `TRUST_SURFACE_PROBLEM_OUTLINE` may compare discovery dates, delivery mechanisms, platforms, objectives, evasion approaches, trust classes, confidence, coverage, and gaps. They must **not** imply shared operators, shared infrastructure, or shared campaigns without explicit linkage evidence recorded in `intelligence/campaign-relationships.csv`.

## Unix / Linux / Shell-Context Hunting

Literal `whoami` alone is an insufficient host-discovery search. Prefer semantic/API/C2 equivalents; preserve **NEGATIVE SEARCH RESULT** rows; classify RatHat as Android + ADB shell on Linux-kernel interfaces — **not** “Linux malware.” Full practice: `shared/methodology/UNIX_LINUX_HUNTING.md`. Ledgers: `intelligence/unix-search-ledger.csv`, `intelligence/linux-artifact-matrix.csv`.