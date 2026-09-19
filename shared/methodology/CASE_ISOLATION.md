# Case Isolation Rule

**Status:** Mandatory program rule  
**Applies to:** All investigations under `emerging-threat-watch`

---

## Rule

Each malware family is an **independent case**.

Active cases: **Rapuncel**, **Settra**, **RatHat**, **NodeRabbit**, **PollCat**, **SynkLoader**, **Showboat**.

Never transfer any of the following from one investigation to another **without direct evidence connecting them**:

- indicators of compromise (hashes, domains, IPs, URLs, certificates, paths, mutexes, etc.);
- attribution or actor naming;
- infrastructure relationships;
- TTPs framed as shared tradecraft of the same operator;
- capabilities asserted as common tooling;
- analytical conclusions (lineage, sibling variants, same campaign, same developers).

**Similar behavior alone does not establish shared operators or lineage.**

---

## PollCat ↔ NodeRabbit (special note)

PollCat and NodeRabbit were **co-disclosed** in the same Kaspersky Securelist article (2026-09-01) and share a dual-referenced primary HTML artifact (`PS-NRB-001` / `PS-POL-001`). That does **not** authorize merging cases.

| Allowed | Not allowed (default) |
|---------|------------------------|
| `COMMON TECHNIQUE` / landscape comparison (e.g. coding-challenge delivery class) | Treating co-disclosure as shared implant authorship |
| Explicit lineage assessment with evidence IDs in **both** ledgers | Copying IOCs from NodeRabbit into PollCat (or vice versa) because they “came from the same paper” |
| Dual-listing the same primary URL in both source indexes | Merging IC3 packages `ETW-NRB-IC3` and `ETW-POL-IC3` |
| Citing NightLedger as Mirage Kitten **ops context** | Using NightLedger as proof PollCat ≡ NodeRabbit code lineage |

**Default analytical posture:** non-authorship / non-shared-operator until direct connecting evidence exists. Critical open question: parallel implants, different generations, specialized payloads, or merely co-deployed by the same intrusion cluster?

Autonomous PollCat pivots **must not** auto-seed NodeRabbit collection (and vice versa) unless a defended link is recorded.

---

## Allowed Cross-Case Mentions

You **may**:

- note that two families use a *common technique class* (e.g., “both abuse SEO”) as a **landscape observation**, labeled `COMMON TECHNIQUE` / non-attributive;
- cite the same public methodology or public LOLBin as independently relevant to each case;
- list both families in the landscape report for comparison **without claiming relatedness**.

You **must not**:

- copy an IOC from Case A into Case B’s IOC tables because it “looks similar”;
- treat secondary articles that mention both families in one headline as proof they are linked;
- merge IC3 briefs.

---

## Establishing a Defended Link

A cross-case relationship requires **direct connecting evidence**, for example:

- shared unique implant hash or near-identical packed blob with demonstrated lineage;
- shared operator-controlled infrastructure with overlapping exclusive control indicators;
- primary-source documentation of code reuse with artifact-level comparison;
- independently observed shared build IDs, signing certificates unique to the operator, or identical unique misspellings in proprietary strings **plus** additional corroboration.

When a link is proposed:

1. Create evidence rows in **both** case ledgers referencing the same linking artifacts.  
2. Add a record to `intelligence/campaign-relationships.csv` with provenance and confidence.  
3. Keep separate threat reports and IC3 briefs; cross-reference rather than merge.  
4. Prefer probabilistic language (“moderate-confidence sibling assessment”) over certainty.

---

## IC3 Separation

If reportable information is established:

- file **separate** factual packages per campaign;
- combine only when evidence actually connects the campaigns and a human reviewer decides a joint filing is appropriate.

Packages: `ETW-RAP-IC3`, `ETW-SET-IC3`, `ETW-RAT-IC3`, `ETW-NRB-IC3`, `ETW-POL-IC3`, `ETW-SYN-IC3`, `ETW-SHO-IC3`.

---

## Review Gate

Before any cross-family statement in a report, ask:

1. What is the specific linking artifact?  
2. Which evidence IDs support it?  
3. Could this be coincidence, commodity tradecraft, or copied public code?  
4. Is the confidence stated?

If (1)–(2) fail → do not transfer the claim.
