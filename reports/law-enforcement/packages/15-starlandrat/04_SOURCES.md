# StarlandRAT — Primary Sources

**Package:** `ETW-STR-IC3`

## Organizations

Cisco Talos (+ BleepingComputer / Security Affairs secondaries)

## Primary source URLs

- https://blog.talosintelligence.com/uat-11795-deploys-novel-starland-rat-and-bespoke-wldr-c2-implant-in-financially-motivated-campaign/
- https://raw.githubusercontent.com/Cisco-Talos/IOCs/main/2026/07/new-starland-rat-and-WLDR-implant-campaign.txt
- https://www.bleepingcomputer.com/news/security/russian-hackers-trojanize-webex-zoom-apps-to-push-starland-malware/ (SECONDARY)
- https://securityaffairs.com/195532/malware/new-russian-campaign-uses-fake-webex-and-zoom-installers-to-deploy-starland-rat.html (SECONDARY)

## Local archive

- `evidence/primary-sources/starlandrat/talos-uat-11795-starland-wldr.html` (PS-STR-001)
  - SHA-256: `0eff5ee5f2e32d8cc50ea58a9a4f6bf94b4919a9f997112d88f199e6a735eb84`
- `evidence/primary-sources/starlandrat/talos-starland-wldr-iocs.txt` (PS-STR-002)
  - SHA-256: `af756bf25110749ddcb27cea532c2fb4274e1f0945587b892cb559d38e34ac5a`
- `evidence/primary-sources/starlandrat/bleepingcomputer-starland-2026.html` (PS-STR-003 · SECONDARY)
  - SHA-256: `24a67af5ba17082f862ccc8fc4cb4ec359e9ab2119a3b9d3e558963df33a086b`
- `evidence/primary-sources/starlandrat/securityaffairs-starland-2026.html` (PS-STR-004 · SECONDARY)
  - SHA-256: `fa8d2aba29857c64cd49f5a445033c67e27d3fea805ec403697090d7e755b221`

## Provenance rule

These URLs are **PRIMARY-SOURCE** publications (except SECONDARY press). Retrieving or retaining them does **not** make infrastructure `OBSERVED` by the Emerging Threat Watch investigation. Sample SHA-256s come from the Talos IOC appendix (PS-STR-002), not the blog prose alone.
