# FBI / LE Summary — PhantomPyramid

**Status:** PRIMARY_FROZEN (not IC3-filed)

Python 3.8/PyInstaller backdoor used in Head Mare campaigns against Russian industrial organizations (~100 orgs / 800+ employees in March 2025 per Kaspersky). Delivered via password-protected polyglot ZIP/PE archives with double-extension LNK decoys. C2 includes HTTP polling to `109.107.182.11` (`/hello`, `/task`, `/result`). MeshAgent observed as a follow-on payload using `updourlan.ru`.

**Case isolation:** Do not merge with PhantomHeart despite Head Mare attribution overlap without direct linking evidence.
