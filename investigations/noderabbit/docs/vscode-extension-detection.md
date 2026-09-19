# VS Code “GitHub Copilot Helper” — Detection Research Questions

**Primary behavior (Kaspersky):** `persist:vscode` creates a fake extension displayed as **GitHub Copilot Helper** (“AI coding assistant helper service”), activation `StartupFinished`. Publisher display name may be **borrowed from local extension metadata / trustedPublishers in state.vscdb** — **signature / trusted status is NOT copied**.

**Cutoff:** 2026-09-19

## Detection research questions (Phase 2)

1. Can we reliably alert on extensions whose **publisher string** does not match marketplace publisher ID / signature?  
2. Does Workspace Trust disablement correlate with malicious extension drops in enterprise telemetry?  
3. Are `extension.js` files that spawn **detached Node** processes rare enough to hunt?  
4. Can we baseline legitimate Copilot extension IDs and treat name-collisions as suspicious?  
5. What EDR/file events fire when VS Code loads an unpacked extension from an unexpected path?  
6. Interaction with Windows Run key fallback when extension directory missing (Windows V3 path)?

## Clarifications

- Display-name spoof ≠ code signing.  
- This is **developer-tool trust-surface** abuse, not proof of GitHub platform compromise.
