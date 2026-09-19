# Security Policy

## Scope

This project is a defensive evidence repository. Security concerns include:

- Accidental inclusion of live malware binaries  
- Accidental inclusion of secrets, API keys, or credentials  
- Exposure of victim PII  
- Scripts that interact with suspected C2 or attacker infrastructure  

## Reporting

If you find live malware, secrets, or PII in this repository, open a private security advisory or contact the maintainers. Do not open a public issue containing the sensitive material.

## Handling Rules

1. Never commit executable malware samples.  
2. Prefer hash/metadata manifests under `samples/`.  
3. Shared tooling must remain passive (no C2 interaction).  
4. Defanged indicators in prose (`[.]`, `hxxps`). Machine-readable IOC files may contain literal values but must be clearly labeled.  
5. Case isolation applies to operational response: do not block or hunt one family's indicators solely because of another family's findings.