# PollCat — IC3 Filing Setup (`ETW-POL-IC3`)

**Status:** `FILED_IC3` · Submission ID `98a4444754324e539dbbffcb10c70637` · 2026-09-19 9:52:51 PM EST  
**Cutoff:** 2026-09-19  
**Record:** [`IC3_FILING_RECORD.md`](IC3_FILING_RECORD.md)

PollCat was filed as a separate IC3 complaint after NodeRabbit `ETW-NRB-IC3` (`dded86972e9347e0be27a6597b4cf08a`).

## 1. Regenerate local (gitignored) helpers

```bash
python3 -c "from shared.tooling.build_le_packages import FAMILIES, write_package
for fam in FAMILIES:
    if fam['id']=='05-pollcat':
        write_package(fam); break"
```

Creates / refreshes:

`reports/law-enforcement/private/filing-helpers/05-pollcat/`

| File | Use |
|------|-----|
| `00_COVER_SHEET.md` | Identity / integrity gate |
| `01_NARRATIVE_PASTE.txt` | Paste into IC3 complaint description |
| `06_EVIDENCE_RETAINED.md` | Local retention checklist |

Optional local add-on (not produced by the builder): `07_IC3_FORM_FIELDS.md` — form field map (recreate from the table below if missing).

## 2. Public package files (tracked)

| File | Purpose |
|------|---------|
| [`IC3_FULL_PACKAGE.md`](IC3_FULL_PACKAGE.md) | **Complete structured dossier** — narrative + all hashes/domains/URLs/paths/protocol + gaps |
| [`02_FBI_SUMMARY.md`](02_FBI_SUMMARY.md) | Investigator summary + prior IC3 cross-refs |
| [`03_INDICATORS.csv`](03_INDICATORS.csv) | 15 PRIMARY-SOURCE POL-IND rows (machine-readable) |
| [`04_SOURCES.md`](04_SOURCES.md) | Securelist primary URL |
| [`05_CAVEATS_AND_LIMITS.md`](05_CAVEATS_AND_LIMITS.md) | Non-claims / lineage limits |
| [`REVIEW_CHECKLIST.md`](REVIEW_CHECKLIST.md) | Pre-submit review |

Pointer brief: [`../../pollcat/POLLCAT_IC3_BRIEF.md`](../../pollcat/POLLCAT_IC3_BRIEF.md)

**Hash reality check:** corpus has **one MD5** (`795e053a990a1569ffdcb57f48f6d085`). **No SHA-256. No C2 IPs.** Do not invent them for the form.

## 3. IC3 form field map

| Area | Suggested content |
|------|-------------------|
| Crime-type language | Malware; Spear-phishing / social engineering (recruitment / coding-challenge lure) |
| Subject line | Defensive TI referral — PollCat (Kaspersky Securelist 2026-09-01) — `ETW-POL-IC3` |
| Description | Paste `01_NARRATIVE_PASTE.txt` (or the paste-ready block in the pointer brief) |
| Additional info | Primary: https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/ · Full CSV under `ETW-POL-IC3` available on request · Repo: https://github.com/theworker02/emerging-threat-watch-1 · Path: `reports/law-enforcement/packages/05-pollcat/` |
| Related IC3 IDs | Rapuncel `208b747c6f7445f0af2b69a9d63acc36`; Settra `631d8b4800d04bc19cdbfc6662e5c52c`; RatHat `f92c4c2f0dd3481f898fdd125e728adf`; NodeRabbit `dded86972e9347e0be27a6597b4cf08a` (**separate** — no shared-operator claim) |
| Loss / victimization | None claimed |

### Short indicator block (if the form has space)

```
MD5 (RankChallenge-react): 795e053a990a1569ffdcb57f48f6d085
Domains: sahi-finance.com; gamebarappinformation.azurewebsites.net; gamebarapp.azurewebsites.net; lifespotify.com
Persistence: NetSync_<user>; requireObject.js; com.harsh.requireobject.plist; ~/.node_packages
```

## 4. Hard rules

1. **PollCat only** — do not merge with NodeRabbit.  
2. **Never auto-submit.**  
3. No malware binaries on the IC3 web form.  
4. No invented dollar losses, victim names, hashes, or C2 hosts.  
5. Do not probe live OTP / C2 URLs to “confirm” indicators.

## 5. After filing

1. Save Submission ID + confirmation screenshot.  
2. Add `IC3_FILING_RECORD.md` (mirror `packages/04-noderabbit/IC3_FILING_RECORD.md`).  
3. Set `FILED_IC3` in `02_FBI_SUMMARY.md` and `MASTER_INDEX.csv`.  
4. Update `reports/law-enforcement/README.md` status line.
