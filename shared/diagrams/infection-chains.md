# Infection / Delivery Chains (Mermaid)

Provenance: PRIMARY-SOURCE reconstructions. Not independently OBSERVED by ETW.

## Rapuncel

```mermaid
flowchart TD
  A[Search / SEO result] --> B[Fraudulent GitHub repository]
  B --> C[GitHub Pages lure]
  C --> D[GitHub Pages redirectors]
  D --> E[istatlmenus.com traffic director]
  E --> F[Payload infrastructure]
  F --> G[Oversized ZIP]
  G --> H[Legitimate vsdbg.exe]
  H --> I[Malicious vsdbg.dll]
  I --> J[Cruciferra / PUROSANGUE-like loader]
  J --> K[Rapuncel stealer]
  J --> L[Alinubx.sys defense impairment]
  K --> M[Credential / browser / wallet collection]
  M --> N[Reported exfil 2.26.126.50]
```

## Settra

```mermaid
flowchart TD
  A[Compromised credentials / VPN] --> B[Discovery]
  B --> C[Credential access]
  C --> D[Lateral movement]
  D --> E[MeshAgent]
  E --> F[Defense impairment / BYOVD]
  F --> G[Settra outer loader]
  G --> H["--pass KDF + AES-CTR"]
  H --> I[LP77 unpacking]
  I --> J[Process-hollowed inner encryptor]
  J --> K[Hyper-V shutdown]
  J --> L[Recovery destruction]
  J --> M[Anti-forensics]
  J --> N[Offline encryption]
```

Note: Left column stages are **operator** (MOXFIVE/Huntress); right/encryptor stages are **malware** (Cynet).

## RatHat

```mermaid
flowchart TD
  A[Smishing / malvertising / portal] --> B[Malicious APK / dropper]
  B --> C[Accessibility granted]
  C --> D[Developer Options]
  D --> E[Wireless Debugging]
  E --> F[Pairing code + port scraped]
  F --> G[Local ADB self-pair]
  G --> H[Android shell context]
  H --> I[liblocal-service.so]
  H --> J[libmedia_codec.so / FRP]
  I --> K[127.0.0.1:7910]
  J --> L[Reverse tunnel]
  I --> M[Persistence outside APK lifecycle]
  M --> N[APK reinstall / Accessibility restore]
  I --> O[Overlays + SMS + notification + input]
```

## NodeRabbit

```mermaid
flowchart TD
  A[Fake recruiter] --> B[Coding assessment ZIP]
  B --> C[Bundled malicious Node module]
  C --> D[Hidden Node.js implant]
  D --> E{Platform}
  E --> W[Windows]
  E --> L[Linux]
  E --> M[macOS]
  E --> S[WSL]
  D --> F[Azure / Cloudflare-backed C2]
  F --> G[Corporate proxy-aware transport]
  G --> H[agent:servers C2 replacement]
  D --> I[Fake VS Code extension]
  D --> J[Git hook persistence]
```
