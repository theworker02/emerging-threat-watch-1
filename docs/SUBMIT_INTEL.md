# Submit Intelligence Tips

If you have **valuable, defensively useful information** about any Emerging Threat Watch family — **Rapuncel**, **Settra**, **RatHat**, **NodeRabbit**, **PollCat**, **SynkLoader**, or **Showboat** — please open a GitHub issue on this repository describing what you would like to add, or how we can incorporate your tip.

Tag the issue with the family name (for example: `rapuncel`, `settra`, `rathat`, `noderabbit`, `pollcat`, `synkloader`, `showboat`) when possible so maintainers can route it correctly.

## Law-enforcement reporting

Emerging Threat Watch materials are prepared for **defensive threat intelligence and lawful reporting**. When investigation packages are complete and human-reviewed, findings will be reported to the **FBI / IC3**.

Canonical draft packages (human review required before any filing) live under:

- [`reports/law-enforcement/`](../reports/law-enforcement/)

Do **not** assume that opening an issue itself files a complaint. Community tips help improve the research corpus; official filings are assembled and submitted by human reviewers using the packages in that path.

## What is useful

Prefer primary-source or well-documented observations that improve detection, victim defense, or accurate reporting:

- Indicators of compromise (domains, URLs, hashes, filenames, mutexes, certificates) with provenance and first-seen dates when known
- Independent sightings or victimology notes that do not expose private victim data
- Corrections to public claims, timelines, or attribution language already in this repository
- Links to reputable public research, vendor advisories, or court/LE releases
- Detection ideas (YARA/Sigma/query sketches) framed for defensive use

Cite sources. Prefer one clear claim per tip with enough context to verify.

## What not to submit (in issues or PRs)

- Malware **binaries**, packed samples, or archives attached to issues
- Instructions or assistance for interacting with **C2**, operators, or live infrastructure
- Stolen **credentials**, session tokens, or raw victim PII
- Requests to weaponize, deploy, or improve malware
- Unverified attribution presented as fact

If you have authorized sample access offline, describe hashes and provenance in text; do not upload executables here. See also `SECURITY.md` and `DISCLAIMER.md`.

## Case isolation

Each family is an **independent case**. Prefer **one family per tip or issue** when possible.

Do not transfer IOCs, attribution, infrastructure relationships, TTPs, or conclusions across families unless you provide **direct linkage evidence**. Similarity alone is not shared attribution. Cross-family comparative notes belong only in landscape materials and must be labeled as comparative observations.

## How to open a tip

1. Open a new issue on this repository.
2. State the family in the title (e.g. `[Settra] additional encryptor mutex sighting`).
3. Summarize the tip, list indicators or corrections, and include source URLs or evidence IDs if you have them.
4. Keep victim-identifying detail out of the public issue body when possible; offer to share redacted details with maintainers if needed.

For code, evidence ledgers, and methodology contributions, see [`CONTRIBUTING.md`](../CONTRIBUTING.md).
