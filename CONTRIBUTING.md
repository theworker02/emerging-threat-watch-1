# Contributing

This repository is under a **proprietary commercial license** ([`LICENSE`](LICENSE)). Submitting a tip or pull request does **not** place your contribution under MIT or any open-source terms; accepted contributions are licensed to the copyright holder under the same proprietary terms unless a separate written agreement says otherwise.

To submit **intelligence tips** (indicators, sightings, corrections) about tracked families — including notes for FBI / IC3 reporting packages — see [`docs/SUBMIT_INTEL.md`](docs/SUBMIT_INTEL.md).

## Before You Contribute

1. Read `METHODOLOGY.md`, `DISCLAIMER.md`, and `LICENSE`.  
2. Respect **case isolation** between families.  
3. Prefer primary sources; cite evidence IDs.  
4. Do not invent novelty or attribution.

## Adding Evidence

- Append new rows; never silently overwrite historical observations.  
- Use immutable IDs: `RAP-EV-####`, `SET-EV-####`, `RAT-EV-####`, `NRB-EV-####`.  
- Fill provenance and confidence fields.  

## Pull Requests

- One family or shared tooling concern per PR when possible.  
- Conventional commits (`feat`, `fix`, `docs`, `chore`, `refactor`, `test`).  
- Update the relevant investigation changelog and `CHANGELOG.md`.
