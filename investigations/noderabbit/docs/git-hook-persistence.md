# Git Hook Persistence — Local Beachhead (Not Automatic Supply Chain)

**Primary (Kaspersky V3):** `persist:projects:scan` finds repos; `persist:project:inject` appends marked launcher to `.git/hooks/post-merge` and `post-checkout` by default. Marker: `# shepherd-persist`.

## What this is

- **Local persistence** on a developer workstation after implant execution  
- Triggered when a later Git operation runs the hook and Node + payload still exist  

## What this is NOT (without extra evidence)

- Not proven **supply-chain propagation** to other clones/remotes  
- Git hooks are **normally not committed**; default repos do not share hooks via `git push`  
- Do not describe as “compromised upstream repository” unless evidence shows committed hooks, CI implant, or malicious remote content  

## Hunting

- Search workstations for `# shepherd-persist` in hook files  
- Alert on unexpected `node` spawned from git hook context  

**Cutoff:** 2026-09-19
