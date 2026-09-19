# NodeRabbit Variant Evolution (V1 → V2 → V3)

**Primary:** Kaspersky GReAT Securelist 2026-09-01  
**Attribution:** Kaspersky’s Mirage Kitten assessment (not independently established by ETW)  
**Cutoff:** 2026-09-19

## Evolution table

| Dimension | V1 (Afghanistan sample) | V2 (Egypt) | V3 (Ethiopia) |
|-----------|-------------------------|------------|---------------|
| Launcher npm | `colorized_terminal` 2.1.0 local | `pretty-log` 2.1.0 local | `pretty-log` 2.1.0 local |
| Single-instance | TCP `127.0.0.1:48739` | Host-derived port `41984–46983` | (retains advanced instance model) |
| Anti-analysis | Minimal | Memory/CPU/uptime/user/tool checks; decoy HEAD to google/microsoft/cloudflare then exit | Inherited/extended |
| Proxy | Basic | HTTP(S) env, WinINET/PAC, WinHTTP; `curl.exe --proxy-anyauth` for NTLM/Negotiate | Enterprise-oriented stack retained |
| Persistence theme | Microsoft EdgeUpdate masquerade | Intel DSA masquerade | Build-specific tasks + **VS Code** + **Git hooks** + WSL bridge |
| C2 API | `/api/rabbit/checkin|task|result` | Similar rabbit API family | `/sdk/v2/ready|config|events` |
| Command count | 11 | Expanded vs V1 | **23** (11 + 12) |
| Notable cmds | sys/proc/fs/net/script | + proxy resilience | + `outlook:emails`, `persist:vscode*`, `persist:project*`, **`agent:servers`** |

## Hypothesis: enterprise developer environments

V2/V3 proxy/PAC/NTLM handling and developer persistence (VS Code, Git, WSL) support the hypothesis that implants are **engineered for corporate developer workstations** — OPEN but well-motivated by primary technical detail.

## Static vs behavioral IOC durability

`agent:servers` can replace the active C2 list and persist to `.sv.json`. Therefore:

- **Static domains/IPs:** short half-life  
- **Behavioral:** Node hidden paths, rabbit/sdk beacon shapes, VS Code fake extension, `# shepherd-persist` hooks — longer value

## Theme

Developer workstation as **espionage beachhead**: coding-challenge social engineering → local trust of `npm`/`node` → IDE/VCS persistence.
