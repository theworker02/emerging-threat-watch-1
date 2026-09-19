# Tracker passive observations

Defensive tag searches for ETW families against abuse.ch surfaces.

## 2026-09-19 run

- ThreatFox / MalwareBazaar **API**: HTTP 401 (Auth-Key required). No IOCs claimed.
- Public **browse** pages: hCaptcha interstitial ("Checking your browser"). Archived HTML is the challenge page, **not** a confirmed empty-tag / NEGATIVE SEARCH RESULT.
- Disposition ledger: `tracker_query_disposition_2026-09-19T190912Z.csv`
- Earlier API attempt summary: `tracker_query_summary_2026-09-19T190837Z.csv`
- Browse attempt summary: `tracker_browse_summary_2026-09-19T190912Z.csv`

To re-run successfully, configure an abuse.ch Auth-Key as an organization secret and query via API only (no captcha). Do not invent tags or IOCs.
