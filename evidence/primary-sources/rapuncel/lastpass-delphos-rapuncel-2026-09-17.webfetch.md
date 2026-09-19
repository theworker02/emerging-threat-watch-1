Threat Intel | One Kit, Forty Companies: How a Malware-as-a-Service Platform Used GitHub as a Distribution Network for its Campaign

# Threat Intel | One Kit, Forty Companies: How a Malware-as-a-Service Platform Used GitHub as a Distribution Network for its Campaign

Threat Intelligence, Mitigation, and Escalation (TIME) team • Published September 17, 2026

LastPass Threat Intelligence, Mitigation, and Escalation (TIME) Team, in partnership with Delphos, identified and disrupted a multi-stage malware delivery campaign impersonating at least 40 companies on GitHub. The payload it delivered survived controls that were built to stop exactly this, with a Microsoft Windows Hardware Compatibility Publisher chain signature and a clean VirusTotal score. LastPass is internally tracking the infostealer as Rapuncel.

SCOPE: This report reflects the state of our investigation as of September 10, 2026. Threat actor infrastructure changes rapidly: domains are taken down, payload servers rotate, and new lure pages can be deployed on demand using the same kit. Details that were accurate at time of writing may have changed by the time you read this. We have documented what we observed and confirmed. Where findings are inferred rather than directly verified, we have said so. Where evidence is incomplete (particularly regarding the full scope of targeted brands, the driver's C2 configuration, and the operator structure behind the MaaS backend) we have noted those gaps openly rather than speculating beyond the data.

If you have encountered infrastructure, samples, or behaviors connected to this campaign that aren't covered here, we want to hear from you. Researchers who have investigated Rapuncel, Alinubx.sys, the albinofennel[.]com kit, or related activity are encouraged to reach out to the LastPass TIME team at security@lastpass.com. Coordinated disclosure helps the community move faster than any single team can alone.

## Executive Summary

On August 13, 2026, the LastPass TIME Team identified a fraudulent GitHub organization impersonating LastPass Authenticator which redirected visitors to attacker-controlled infrastructure which ultimately served the installer. LastPass shared the campaign with Delphos Labs for payload analysis. The joint analysis revealed a larger operation with its own infrastructure, crypter kit to evade detection, and multiple operators running lures in parallel targeting dozens of other companies.

The campaign delivered a Microsoft-attested kernel driver with zero VirusTotal detections that terminated 145 antivirus and EDR processes from kernel mode, enabling potential credential theft across browsers, cryptocurrency wallets, Discord, Steam, Telegram and Windows Credential Manager. Delphos Labs assesses with high confidence that the loader was produced by the Cruciferra PUROSANGUE crypter package or a close derivative, which was previously documented by Proofpoint in 2025.

The LastPass lure was a single recent frame in a campaign that has been running for months and shows every sign of continuing after its current infrastructure is burned. TIME and Delphos analysts assess there may be overlap with the BoryptGrab campaign that Trend Micro documented in March 2026; however, the exact nature of the relationship is unclear, and there is insufficient evidence to conclude these are the same campaign or the same operator.

This was opportunistic brand impersonation. No LastPass system, service, or customer vault was involved or compromised. The lure was distributed entirely outside LastPass channels. Official LastPass Authenticator is available through lastpass.com and the official app stores. GitHub is not a LastPass distribution channel. This was opportunistic use of a recognizable name.

This report incorporates the full joint technical findings prepared by the LastPass TIME Team and Delphos Labs. Payload analysis by Delphos Labs using static analysis, custom decryption, NativeAOT data reconstruction, and emulator-assisted inspection.

### Finding the victim

A user searching for "LastPass Authenticator download" or similar terms encounters a fraudulent GitHub organization page (github[.]com/LastPass-Authenticator) near the top of search results. The page is deliberately SEO-optimized and appeared to rank well. It looks like a legitimate LastPass product page, using LastPass branding, logos, and product descriptions, with a prominent "GET – LASTPASS AUTHENTICATOR" button.

There was also a second similar fake GitHub page (github[.]com/LastPass-S) which used nearly identical SEO-stuffed language about a "macOS LastPass" product. The TIME team assesses this was likely the same actor running multiple impersonation accounts. The website was taken down before we could investigate this site further.

 

### The fake download portal

Clicking the button takes the victim to a GitHub Pages site (lastpass-authenticator[.]github[.]io) that displays a convincing download interface. The page shows fabricated trust signals (i.e., "Authorized Access," "VirusTotal Approved," and "Secure Archive" badges) along with a spinning animation that says "Validating session / Generating secure token." None of these are real. They exist solely to create confidence while the page prepares the download.

 

### The hidden redirect chain

Behind the scenes, the page silently routes the victim through two additional observed GitHub Pages accounts (i.e., edgarcostartqd[.]github[.]io and dallikilic54[.]github[.]io) that act as hidden waypoints. These pages don't display anything visible to the user and exist to obscure the trail between the lure page and the actual malware server, making the infrastructure harder to trace and take down. Each one uses a custom 404.html file containing JavaScript that captures the URL path and silently forwards the victim to the next stage. This technique exploits standard GitHub Pages error-handling behavior to function as a covert redirector while appearing to be a broken or nonexistent page.

A separate Cloudflare-fronted server (istatlmenus[.]com) acts as the dynamic traffic director for the chain. Rather than hardcoding the payload server address into the lure pages directly, the chain fetches the destination from istatlmenus[.]com/mandua[.]wonted at runtime. This means the operator can redirect victims to a different payload server at any time simply by updating that single endpoint without touching any of the GitHub lure infrastructure. The endpoint was confirmed live and serving a JavaScript redirect on September 10, 2026, and its content had changed between August 27 and September 10, confirming active ongoing maintenance.

### The terminal destinations

macperformancetools[.]com and zaffersnouty[.]com are the terminal destinations of the redirect chain. Both are currently parked, consistent with the operator standing down visible malicious activity following researcher detection while keeping the infrastructure registered and ready to reactivate. macperformancetools[.]com is 302-redirecting to awwwards.com and zaffersnouty[.]com is 302-redirecting to threads.com.

Both domains are confirmed Cloudflare-fronted. Sandbox analysis of both independently produced an identical behavioral finding: deletion of the Windows registry key HKEY_CURRENT_USER\Software\Google\Chrome\PreferenceMACs\Default\extensions.settings, which controls Chrome's extension integrity verification. The consistent pattern across two separate domains suggests this is a deliberate capability of the campaign, not a sandbox artifact. Its purpose and whether it was activated against real victims remains unclear.

### The download

The victim is ultimately sent to the attacker's payload server (albinofennel[.]com or hanselarinmusky[.]com) with multiple user codes observed (unique tracking identifiers embedded in the download URL that indicate the infrastructure is managing multiple simultaneous lure campaigns or distribution channels) and a ZIP file downloads automatically.

During LastPass’ investigation, the TIME team identified albinofennel[.]com was serving at least 40 other branded impersonation lure pages, indicating LastPass was likely just one of the many targets using this same kit.

In the cases we observed, the zip file names and sizes differed slightly but contained identical malware components (i.e., LastPass-Authenticator-download-1.66.2.zip (148MB) and lastpass-authenticator-2.78.7.zip (127.9MB)). The large file size is intentional: most automated security scanning tools have size limits and will skip files this large, allowing the malware to arrive undetected.

Opening the ZIP

The archive contains what appears to be a LastPass installer alongside a collection of supporting files with plausible-sounding names. Two large files (TitanStorage.dll and ProManager.dll) are pure junk and are included only to inflate the archive size further. The actual malicious files are small and hidden among the legitimate-looking ones.

*The size-padding angle is familiar: Delphos previously documented a 55MB libpsl-5.dll stealer where most of the file was junk padding used to slip past scanners.

### Step 1: The fake installer runs

The victim runs what looks like a LastPass installer; however, it is actually Microsoft's own debugging tool (vsdbg.exe) renamed. When Windows loads this program, it automatically loads a companion file (vsdbg.dll) from the same folder. This is a standard Windows behavior the attacker deliberately exploits. The companion file is the attacker's code, not Microsoft's.

### Step 2: The malware takes full control

The malware attempts three different methods to obtain administrator-level access, exploiting built-in Windows features that allow programs to request elevated permissions. Once it succeeds, it runs as SYSTEM, which is the highest privilege level available on a Windows machine, above even a standard administrator account.

### Step 3: All security software is killed

The malware installs a kernel driver, which is software that runs at the deepest level of the operating system, below where antivirus and security tools operate. This driver is disguised as an NVIDIA graphics component (nvfsflt64.sys, registered under the name "NVIDIA File System Filter Driver"). It carries a list of 145 named antivirus and endpoint security products. It terminates every one of them that is running. Because the kill command comes from kernel level (below where security software operates) no antivirus can block or detect it. The driver was signed by Microsoft's own hardware compatibility program, giving it a level of trust that Windows does not question.

### Step 4: Stealth features load (partially)

The driver contains code to hide its own files from Windows and inject a helper component (ProtectR3.dll) into every running program on the machine. In this specific deployment, the attacker did not provide the configuration file that the driver needs to activate these features, so they did not run. The driver was used solely to kill security software.

### Step 5: Browser passwords are stolen

With security software gone, the stealer reads saved passwords from more than 25 web browsers. For Chrome, Edge, and other modern browsers that use Google’s 2024 “app-bound encryption” feature (a security improvement specifically designed to prevent this kind of theft) the malware uses a more sophisticated approach: it injects a small piece of code directly into the browser process. This code impersonates the browser itself and calls Chrome’s own password-decryption service from inside Chrome, bypassing the protection because the request appears to come from a legitimate source.

### Step 6: Everything of value is collected

Beyond passwords, the malware collects the following:

- cryptocurrency wallet files from more than 30 wallet applications, 
- Discord login tokens, 
- Steam session tokens (the malware will launch Steam silently if it is not already running, then scan its memory for credentials), 
- Telegram session data, 
- Windows credential store (which holds saved network passwords, Windows Hello data, and other credentials), 
- any document whose name contains words like "password," "seed," "wallet," or "recovery",
- a screenshot of every monitor connected to the machine, and 
- a detailed profile of the system. 

### Step 7: Everything is sent to the attacker

All collected data is compressed into a ZIP archive and uploaded to an attacker-controlled server at 2.26.126.50 over a raw internet connection formatted to look like ordinary web traffic. If the upload fails, the malware retries three times with two-second pauses between attempts. The Rapuncel Stealer uses a dedicated C2 at 2.26.126.50 for credential exfiltration. The delivery loader and Alinubx kernel driver do not communicate with external infrastructure in this deployment.

### Step 8: Web traffic hijacking (present but not active)

The kernel driver also contains code to intercept all web traffic passing through the machine and redirect it through a local proxy, which would allow the attacker to inject advertisements, modify search results, or replace software downloads with malicious ones. This feature requires a configuration file that the attacker did not provide in this deployment, so it did not activate. Its presence in the driver suggests the operation has broader capabilities that could be enabled in future deployments.

### Step 9: The machine stays compromised indefinitely

The malware installs itself as a Windows service that starts automatically every time the computer boots. It then loops continuously: checking for security products, killing any that have restarted, and re-running the stealer. The machine may remain fully under the attacker's control until the kernel driver is physically removed. This process requires booting the computer into Safe Mode or using an external recovery tool, because normal Windows tools cannot safely remove software operating at that level while the system is running. 

## What did the fake LastPass sample actually contain?

Component

Role

SHA256

vsdbg.dll

NativeAOT loader

ea8c31a86fa785ab514022c278a2f6e571c86aac9283745a96605c44d88382d6

Rapuncel stealer

Credential theft and exfiltration

aefbc6e04320e9a0e80f2323f8a897c4fdb222a37b0b87d76e850109decbfadd

Alinubx.sys

Kernel AV killer

611b3ba687b7f46319a19609605ddfe5225e6d85277d8e923eea3fdb6f7b5b61

Browser injection DLL

Chrome and Edge app-bound key decryption

75018b06c7105a1dca391805d17b402aed35ebd515b92d461236eafbd606cb40

ProtectR3.dll x64, unpacked

Usermode rootkit helper present inside driver

26db14b956e33f69b3397a36387d32e01eb63613acff91069dc76b6ed7de45a8

VirusTotal's last analysis for Alinubx.sys showed 3 malicious detections and 71 undetected engines, on September 10, 2026. 

## Is this connected to Cruciferra?

Delphos assesses with high confidence that the malicious DLL vsdbg.dll sample was produced by the Cruciferra PUROSANGUE package or a close derivative.

Proofpoint recently documented Cruciferra, a crypter service that uses DLL side-loading, .reloc payload storage, a custom Base16 alphabet (PQRSTUVWXYZ[\]^_), BYOVD-based EDR tampering, UAC bypass, persistence, and a large set of custom cryptographic routines. Proofpoint says Cruciferra often abuses GoFlyDrv.sys and lists additional helper drivers including Core64.sys, HwOs2Ec.sys, LnvMSRIO.sys, MemoryInformer.sys, NTIOLib_X64.sys, ProcessMonitorDriver.sys, and selfprot.sys.

The strongest overlap is the payload container: this sample also stores payloads in .reloc and uses the same custom Base16 style, with bytes in the 0x50 to 0x5F range corresponding to PQRSTUVWXYZ[\]^_. The other overlaps are contextual: DLL side-loading, UAC bypass, persistence, generated internal record names, and BYOVD-style EDR tampering. They all fit the Cruciferra pattern, but none is decisive alone.

A separate eSentire analysis strengthens the match. eSentire describes a Cruciferra package called PUROSANGUE that produces a NativeAOT side-loaded DLL with EDR/AV killing, COM Elevation Moniker UAC bypass, process hollowing into ServiceModelReg.exe, and 145 default AV/EDR process targets. Our loader contains the decrypted string C:\ExploitTests\purosangue.tx and matches every one of those features. Recorded Future lists the same PUROSANGUE tier in a broader Cruciferra pricing summary. The only operational difference is the driver: where eSentire observed DCRCVDrv.sys, this sample uses a renamed Microsoft-attested CnCrypt/CcProtect driver.

The main implementation change is the runtime. This sample uses .NET NativeAOT instead of Mono. That is a practical hardening step for a .NET crypter, which preserves much of the developer workflow while removing the easy IL-decompilation path that defenders expect from Mono and .NET samples. It uses a different driver, a renamed Microsoft-attested CnCrypt/CcProtect, that Proofpoint did not list among the observed helper drivers. It is not evidence against lineage.

## Possible overlap with BoryptGrab campaign

SOURCING: The following section is based on Trend Micro's published BoryptGrab report (March 5, 2026) and Delphos comparative analysis of the rapuncel payload against Trend Micro’s documented samples. No BoryptGrab IOCs from that report have been independently verified in this investigation's collected data. They are not included in this report's IOC tables.

Trend Micro documented the BoryptGrab campaign in March 2026, describing a data-stealing malware family distributed via SEO-optimized fake GitHub repositories and deceptive GitHub Pages download portals. The passathook-cs2 brand appears in both datasets: as albinofennel[.]com/c6g45wmf3qx9/passathook-cs2.github.io in the albinofennel.com VT Graph child URL export from this investigation, and as passathook-cs2-github-io-2.56.2.zip in the Trend Micro BoryptGrab IOC file. This is the primary observed link between the two campaigns.

Delphos compared the Rapuncel stealer payload directly against Trend Micro’s documented BoryptGrab samples. The two families are not byte-identical; however, the behavioral and artifact-level overlap is strong. Delphos assesses Rapuncel is a BoryptGrab-related variant or sibling build, not a confirmed match to any of Trend Micro’s published samples.

### Confirmed Overlaps (Independently Verifiable)

- Shared Lure Brand: passathook-cs2 confirmed in this investigation's albinofennel.com URL data and in Trend Micro's BoryptGrab IOC file. 
- Delivery Architecture: Both campaigns use SEO-optimized GitHub repositories pointing to .github.io Pages download portals. Both use an intermediate URL to dynamically supply the payload server address rather than hardcoding it. Observed independently in both campaigns. 
- Shared Collection Artifacts: Both payloads produce UserInformation.txt with a BUILD NAME field, installed_applications.txt, and a misspelled Filegraber directory. Both collect Telegram data, Discord tokens, Steam account data and tokens, screenshots, cryptocurrency wallet data, and browser credentials. 
- Chrome App-Bound Encryption Bypass: Both campaigns embed a browser helper DLL that injects into Chrome or Edge and calls the browser Elevation Service DecryptData method to bypass app-bound encryption. Delphos assesses this as a highly specific workflow, not generic stealer boilerplate. 
- Archive Size Inflation: Both distribute large ZIP archives with junk content to evade sandbox scanning size limits. 

### Key Differences

- Malware Family: The stealer payloads are not byte-identical and do not share hashes with any of Trend Micro's published IOCs. Rapuncel's build name differs from documented BoryptGrab builds (CryptoByte, Shrek, Sonic, Yaropolk). The behavioral and artifact-level overlap points to the same ecosystem, not the same binary. 
- Browser Helper DLL Implementation: Trend Micro's documented BoryptGrab samples embed a ChaCha20-encrypted PAYLOAD_DLL resource that decrypts to a 1.35 MB DLL exporting ReflectiveLoader. Rapuncel embeds a smaller 136 KB helper exporting Bootstrap. Same purpose, different packaging. 
- C2 infrastructure: Rapuncel's confirmed C2 is 2.26.126[.]50. Trend Micro's documented samples use different infrastructure. No shared C2 has been identified. Kernel Driver: This campaign deploys Alinubx.sys, a Microsoft-attested kernel driver with 0/72 VT detections terminating 145 AV/EDR processes. No kernel driver component is documented in Trend Micro's BoryptGrab reporting. 
- Secondary Payloads: BoryptGrab delivers a reverse SSH backdoor (TunnesshClient) and a Golang downloader (HeaconLoad), providing persistent remote access. This campaign delivers Alinubx.sys as the secondary payload, focused on defeating endpoint security rather than persistent access. Payload Server Architecture: albinofennel.com uses a window.__PM__ JavaScript kit generating dynamic lure pages from URL path parameters, supporting 40+ simultaneous brand impersonations. BoryptGrab's documented infrastructure does not include this level of automation.

### Assessment

The shared file names and similar behaviors used in both campaigns are the strongest observed connections between these two campaigns. The shared collection artifacts, the misspelled Filegraber directory, and the highly specific Chrome Elevation Service bypass workflow are not generic stealer boilerplate. They indicate a shared codebase, shared tooling, or a deliberate fork from within the BoryptGrab ecosystem.

The payload differences (distinct hashes, different build names, smaller and differently packaged browser helper DLL, separate C2 infrastructure) are consistent with how modern malware families evolve across builds. Builder automation, forks, and rewrite workflows can preserve the same theft model while changing packaging, helper modules, strings, and infrastructure. 

Rapuncel is a BoryptGrab-related variant or sibling build. It is not a confirmed match to any of Trend Micro's published samples, but the behavioral and artifact-level overlap is sufficient to place it within the BoryptGrab ecosystem with moderate confidence. Delphos found no definitive evidence that Rapuncel was AI-generated, though an AI-assisted rewrite from the same specification cannot be ruled out; a human rewrite is equally plausible.

## Why was the signed driver the important payload?

The stealer did the visible malicious work while the driver enabled it by disabling defenses where the user-mode components at the kernel level of the security software, where components are reduced to racing or observing the attacker's driver rather than remediating it.

Alinubx.sys exposes an IOCTL interface through \\.\Alinubx. The loader sends IOCTL 0x222024 with target process IDs. The driver resolves each target process with PsLookupProcessByProcessId, opens it with ObOpenObjectByPointer, and terminates it with ZwTerminateProcess. The loader's target set is fixed in code: sub_1800eae00 allocates 0x91 entries, which is 145, and fills them with decrypted EDR/AV process-name strings.

The driver calls ObOpenObjectByPointer with AccessMode=KernelMode, which bypasses the normal user-mode SeAccessCheck path at handle-open time. It asks the kernel to open the process as kernel code, then kills it. That is why it can defeat Protected Process Light (PPL); the protection many security products rely on to survive an administrator. It does not need to patch EPROCESS protection bits.

A user-mode stealer steals credentials. A trusted kernel driver clears the runway.

This is an abuse-by-design driver rather than a memory-corruption exploit. The process-kill interface appears to be product functionality exposed by a host-defense driver. The control is policy enforcement: block the driver, deny the signer or lineage, or prevent the drop. If the driver is trusted and not blocklisted, administrator rights are enough to install and use it.

## What made Alinubx different from CcProtect?

The version resources and VirusTotal pivots tie Alinubx.sys to the CnCrypt/CcProtect driver line from Henan Dafeng Software Co., Ltd. CnCrypt is a public Chinese disk encryption and host-defense product. Its protection driver, CcProtect.sys, is catalogued by LOLDrivers as a BYOVD process-killer provider, with public proof-of-concept code available in BlackSnufkin’s CcProtect-Killer, a widely mirrored GitHub repository.

That proof of concept opens \\.\CcProtect, sends IOCTL 0x222024, and passes a PID to kill an arbitrary process. A Chinese incident-response writeup also describes CnCrypt Protect being used after IIS compromise to create rules, install the CcProtect driver, redirect an IIS-loaded DLL to a malicious replacement, and hide a malicious service. Those are different uses of the same protection framework: process killing in one case, file and service hiding and redirection rules in another.

Our sample kept the CnCrypt product identity and version but changed the driver identity that most defenders would see first.

The functionality stayed recognizable, while the identity changed enough for detection to miss it.

Field

Known CcProtect.sys v1.32

Alinubx.sys from this sample

Product

CnCrypt

CnCrypt

Version

1.32

1.32

Description

CnCrypt Protect Driver

Alinubx Driver

Original filename

CcProtect.sys

Alinubx.sys

Submitter programName

Henan Dafeng Software Co., Ltd.

Henan Dafeng Software Co., Ltd.

VirusTotal detections (checked 2026-08-20)

7 malicious / 70 undetected / 1 failure (last analysis 2026-08-13T04:54:45Z)

0 malicious / 72 undetected (last analysis 2025-07-21T20:53:49Z)

Microsoft blocklist status

Not found in DriverPolicy_Enforced.xml downloaded 2026-08-20

Not found in the same file

## How does a Microsoft-signed driver end up killing 145 security processes?

The observed ZIP delivered two payloads through DLL side-loading. The first, a credential stealer the LastPass TIME team tracks as Rapuncel, targets 19 or more browsers, 34 or more cryptocurrency wallets, Discord, Steam, Telegram, and Windows Credential Manager, and decrypts Chrome and Edge app-bound encryption keys with a dedicated injection DLL. The second payload is the one that matters for defenders.

Alinubx.sys is a kernel driver. It exposes an IOCTL interface, accepts a list of process IDs, and terminates each one from kernel mode using ZwTerminateProcess after opening the process with KernelMode access. That KernelMode flag bypasses the user-mode access check that normally protects security software, defeating Protected Process Light without touching EPROCESS protection bits. It carries 145 hardcoded AV and EDR process names, dropped to disk as nvfsflt64.sys under the service name NvFsFilter, disguised as an NVIDIA File System Filter Driver.

The driver is signed through the Microsoft Windows Hardware Compatibility Publisher chain, with a signing timestamp of March 2023, years before this campaign. It scored 0 out of 72 on VirusTotal as of August 20, 2026, unchanged since July 2025. It was not present in the Microsoft vulnerable driver blocklist at publication.

The driver is a renamed, identity-swapped version of CcProtect.sys, a driver already listed on LOLDrivers with public proof-of-concept killer code. Same product string, same version, same submitter, same process-kill primitive. The operators changed the original filename from CcProtect.sys to Alinubx.sys, and that single change was enough to slip past detections keyed to the known name.

Microsoft attestation proves a driver passed through a trust pipeline. It does not prove the driver is safe.

## Why did signature-based detection miss all of this?

The signature was ineffective at halting this campaign because a signature merely asks whether a file matches something already discovered to be malicious. This driver was signed, timestamped, and clean on VirusTotal, and its dangerous twin was hiding behind a different filename. Every signal a signature-based control reads came back green. 

The Microsoft signature proves the driver passed through a trust pipeline. It does not prove the driver is safe.

Delphos checked 18 raw driver files from public BYOVD repositories, plus CcProtect.sys and Alinubx.sys, against the Microsoft DriverPolicy_Enforced.xml blocklist downloaded on August 20, 2026. There were 0 of 20 SHA256 matches because the blocklist is a list of known bad hashes. New malware can avoid matching by creating a new hash with techniques such as a filename swap or a recompilation.

Delphos Labs analyzed the compiled artifact directly through static analysis, custom decryption, NativeAOT data reconstruction, and emulator-assisted inspection. This allowed them to inspect the binary directly, rather than weaker techniques like antivirus signatures and YARA rules. Thus, the findings that identified this kit, the .reloc payload container, the 0x50 to 0x5F byte range, the build-environment string, and the 145-target count, came from reading the binary rather than relying on information of whether it had been previously detected.

A signature only works when malware has been previously identified. Delphos Labs’ technique of reading the binary does not have this handicap.

## What was active and what was only present in code?

The driver carries more than this deployment used: file and registry hiding, process and driver interception, DLL interception, network control, port redirection, WFP traffic handling, APC-based usermode DLL injection, and a rule configuration system based on \SystemRoot\Alinubx.ccf.

We found no evidence that the loader writes Alinubx.ccf, sends configuration IOCTL 0x222010, activates the network redirect, or performs ProtectR3.dll injection. The driver can also send a JSON rule and version heartbeat over an HTTP POST to a configured URL, but no URL is configured in this sample.

In this deployment, Alinubx acted as an AV killer and its broader functionality remained unconfigured. A future deployment with Alinubx.ccf present could activate the rest.

### Disclosure status

Delphos reported Alinubx.sys to Microsoft through the MSRC Researcher Portal on August 19, 2026. MSRC responded that the behavior does not meet its definition of a security vulnerability, since the driver is not a Microsoft-owned component, and directed the report to the Windows Defender Security Intelligence driver submission portal, which is the channel for blocklist consideration. That case was closed. Delphos resubmitted through the driver submission portal on August, 19, 2026. At publication, Alinubx.sys was not present in the Microsoft vulnerable driver blocklist.

## What should someone who ran the installer do?

Treat every credential stored in the browser on that machine as exposed, along with cryptocurrency wallet files, Discord and Steam and Telegram session tdata, and anything held in Windows Credential Manager. The stealer collected and exfiltrated these before the driver work began.

Change those credentials from a separate, known-clean device rather than the affected one, and review vault activity for anything unexpected.

## What does this mean for defenders?

Most robust techniques of binary inspection are needed to find novel malware. Hashes and payload server addresses can easily be rotated. For example, in this campaign, one payload server dropped off DNS during the analysis window while two others stayed live. As signatures and IP addresses are discovered, operators will redeploy to fresh infrastructure, recompile with a new signature, and swap the driver filename again, the same way CcProtect.sys became Alinubx.sys. Even durable indicators are behavioral: a file written to C:\Windows\System32\drivers\nvfsflt64.sys, a service created as NvFsFilter describing itself as an NVIDIA component while unsigned, vsdbg.exe spawning non-Microsoft child processes, and a PE file whose raw .reloc section is far larger than its declared relocation size with a high concentration of bytes in the 0x50 to 0x5F range. Any machine that executed this payload should consider kernel-level forensic investigation, because Alinubx.sys defeats the user-mode tooling that would normally perform the cleanup.

The larger lesson is about trusting fragile, lookup-based detection techniques. This campaign chained together four separate trust assumptions and broke each one: that a recognizable brand on GitHub means an official channel, that a Microsoft signature means a vetted driver, that a clean VirusTotal score means a safe file, and that a blocklist covers the drivers that matter.

Delphos analyzes compiled code to reveal intent, without source and without prior knowledge of the sample. That is the analytical posture this class of threat requires.

## What should defenders hunt for?

Hunt for lineage and behavior, not just the original name.

- Microsoft-attested drivers whose Authenticode programName contains the Henan Dafeng identity or whose version resources contain CnCrypt.
- Drivers with OriginalFilename or strings matching CcProtect.sys, Alinubx.sys, Alinubx, ProtectR3.dll, or \\.\Alinubx.
- Service creation for NvFsFilter or file writes to C:\Windows\System32\drivers\nvfsflt64.sys.
- Driver load followed by termination of security processes through kernel activity.
- Presence of \SystemRoot\Alinubx.ccf, which would indicate the broader rootkit configuration path rather than kill-only use.
- PE files where the raw .reloc section is much larger than the size declared in IMAGE_DIRECTORY_ENTRY_BASERELOC. In this loader, the excess region is mostly bytes in the 0x50 to 0x5F range, which encoded encrypted payload data before recovery.
- The Rapuncel stealer exfiltration pattern: ZIP upload to 2.26.126[.]50 using POST /upload HTTP/1.1 over raw TCP. Treat this IP as historical and shared-infrastructure context, not a standalone block rule without corroborating request framing.

### Confirmed Hashes

| Component | SHA256 |
| --- | --- |
| vsdbg.dll (.NET NativeAOT loader) | ea8c31a86fa785ab514022c278a2f6e571c86aac9283745a96605c44d88382d6 |
| Rapuncel stealer | aefbc6e04320e9a0e80f2323f8a897c4fdb222a37b0b87d76e850109decbfadd |
| Alinubx.sys (kernel driver) | 611b3ba687b7f46319a19609605ddfe5225e6d85277d8e923eea3fdb6f7b5b61 |
| Browser injection DLL | 75018b06c7105a1dca391805d17b402aed35ebd515b92d461236eafbd606cb40 |
| ProtectR3.dll x64 (unpacked) | 26db14b956e33f69b3397a36387d32e01eb63613acff91069dc76b6ed7de45a8 |
| CcProtect.sys v1.32 (reference — LOLDrivers) | 5f0cfe8357bb52b45068ddbac053e32bc38e6cb5e086746f5402657b0a5cfb1c |

### Domains

| Domain | Role |
| --- | --- |
| albinofennel.com | Primary MaaS payload server |
| hanselarinmusky.com | Secondary payload server |
| icansamyope.com | Tertiary payload server |
| istatlmenus.com | C2 redirect layer |
| macperformancetools.com | Terminal scareware |
| zaffersnouty.com | Terminal redirect |
| ryanpresbrey.cc | Favicon cluster — TBD |

### IP Addresses

| IP | Role |
| --- | --- |
| 2.26.126[.]50 | Rapuncel exfil endpoint — raw TCP POST /upload HTTP/1.1 |
| 104.21.27.38 | Cloudflare proxy — albinofennel.com |
| 172.67.168.224 | Cloudflare proxy — albinofennel.com |
| 172.67.212.253 | Cloudflare proxy — istatlmenus.com |
| 104.21.20.224 | Cloudflare proxy — macperformancetools.com |
| 104.21.18.89 | Cloudflare proxy — zaffersnouty.com |

### System & Registry Artifacts

| Artifact | Detail |
| --- | --- |
| C:\Windows\System32\drivers\nvfsflt64.sys | Dropped kernel driver path |
| NvFsFilter | Driver service name — disguised as NVIDIA component |
| \\.\Alinubx | Driver device name — IOCTL interface |
| \SystemRoot\Alinubx.ccf | Driver config path — not present in this deployment. Presence would indicate broader rootkit configuration. |
| Henan Dafeng Software Co., Ltd. | Authenticode OpusInfo programName — pivot field |
| browser_decryption.log / sends.log | Rapuncel forensic footprint in %TEMP% output folder — confirms compromise if present |
| Favicon dhash: 3761dd64e0d46913 | VTI pivot — use to identify related kit infrastructure |
| Body SHA-256: 1e6c1766ac78d7adfdae71d361cb132d972771897ae9065503b135cb812d7c35 | istatlmenus.com/mandua.wonted JavaScript redirect payload — confirmed 2026-09-10 |
| HKCU\Software\Google\Chrome\PreferenceMACs\Default\extensions.settings | Chrome extension integrity key — deleted in sandbox execution of BOTH macperformancetools.com and zaffersnouty.com. Consistent pattern across two terminal domains confirms deliberate behavior, not sandbox artifact. Warrants escalation to Google Chrome security team (security@chromium.org). |

### Observed in This Deployment — Confirmed by Delphos Labs

| Technique ID | Name |
| --- | --- |
| T1574.002 | Hijack Execution Flow: DLL Side-Loading |
| T1055.012 | Process Injection: Process Hollowing |
| T1562.001 | Impair Defenses: Disable or Modify Tools (145 AV/EDR processes via kernel driver) |
| T1555.003 | Credentials from Web Browsers |
| T1539 | Steal Web Session Cookie |
| T1113 | Screen Capture |
| T1005 | Data from Local System |
| T1041 | Exfiltration Over C2 Channel |
| T1548.002 | Abuse Elevation Control Mechanism: Bypass User Account Control |
| T1543.003 | Create or Modify System Process: Windows Service |
| T1036.005 | Masquerading: Match Legitimate Name or Location |
| T1553.002 | Subvert Trust Controls: Code Signing (Microsoft-attested driver) |

### Present in Driver Code — Not Confirmed Active in This Deployment

| Technique ID | Name |
| --- | --- |
| T1014 | Rootkit (file/registry hiding — requires Alinubx.ccf) |
| T1055.004 | Process Injection: APC-style DLL injection (ProtectR3.dll) |
| T1557 | Adversary-in-the-Middle (WFP network redirect — unconfigured) |