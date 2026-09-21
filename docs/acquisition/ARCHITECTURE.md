# Architecture — Emerging Threat Watch

See also repository root architecture docs where present (`ARCHITECTURE.md`, `docs/`, `README.md`).

## Stack

Documentation / CTI corpus (Markdown, CSV, frozen HTML/PDF evidence); no application runtime

## Deployment

Read-only documentation repository; no installable product. Gates are lab stubs only.

## Summary

Independent evidence-driven threat-intelligence investigations across malware family / candidate case folders with provenance vocabulary and LE packaging templates.

## Boundaries

- Third-party runtimes, cloud providers, and SDKs are **dependencies**, not owned assets.
- Project-specific diligence: [`ETW_DILIGENCE.md`](./ETW_DILIGENCE.md).

Buyer should walk architecture with the handoff plan ([HANDOFF_PLAN.md](./HANDOFF_PLAN.md)).
