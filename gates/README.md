# Internal job gates

Operational queue for gated research jobs. Not part of the law-enforcement handoff surface.

See `shared/methodology/GATED_AUTONOMY.md` for policy.

| Directory | Meaning |
|-----------|---------|
| `queue/` | Pending approval |
| `approved/` | Approved |
| `denied/` | Rejected |
| `completed/` | Finished |
| `payloads/` | Job-specific JSON/YAML |
