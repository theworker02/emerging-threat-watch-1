# Rapuncel Infection Chain (Baseline)

```mermaid
flowchart LR
  A[Search engine query] --> B[SEO-ranked fake GitHub org/repo]
  B --> C[GitHub Pages / download lure]
  C --> D[Redirect / Cloudflare traffic director]
  D --> E[Padded ZIP archive]
  E --> F[Renamed vsdbg.exe + malicious vsdbg.dll]
  F --> G[Privilege escalation attempts]
  G --> H[Alinubx.sys as nvfsflt64.sys / NvFsFilter]
  H --> I[Security process termination]
  I --> J[Rapuncel collection + exfil]
  J --> K[Windows service persistence]
```

For each transition (Phase 1): evidence is **SECONDARY/PRIMARY-SOURCE cited**, not ETW-OBSERVED. Artifact liveness checks are Phase 2.