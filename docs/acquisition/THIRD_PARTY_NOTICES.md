# Third-Party Notices — Emerging Threat Watch

**Date:** 2026-09-21

This file summarizes third-party materials observed in-tree. It is **not** a complete SBOM.

## Package dependencies

No package manager lockfile for a product runtime. Content is docs/CSV/evidence.

Retain upstream license texts when redistributing binaries or bundled node_modules/site-packages.

## Non-package third-party materials

Large corpus of frozen vendor HTML/PDF under evidence/primary-sources — publishers retain copyright. IOC facts from public sources with provenance tags.

## Trademarks

Third-party marks referenced in docs remain owned by their respective owners. Project disclaimers (where present) should be preserved.

## Action items

- [ ] Regenerate machine-readable SBOM at closing
- [ ] Confirm Qt/PySide6 redistribution path if shipping GUI wheels — **REQUIRES_LEGAL_REVIEW**
- [ ] Confirm any vendored trees still carry upstream LICENSE/NOTICE
