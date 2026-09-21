Tinker Tailor Soldier: Paper Werewolf’s latest toolkit | by BI.ZONE | May, 2026 | Medium

Open in app

Sign up

Get app

Sign up

# Tinker Tailor Soldier: Paper Werewolf’s latest toolkit

10 min read

May 13, 2026

--

Share

Press enter or click to view image in full size

## Overview

In March–April 2026, we uncovered a new campaign by Paper Werewolf targeting Russian industrial, financial, and transport organizations.

The analysis revealed several previously undescribed malware instances, including a custom-built stealer we dubbed PaperGrabber, loaders and downloaders written in C++, C#, Python, and JavaScript, and a novel shellcode-based implant for the Mythic post-exploitation framework.

## Key findings

- Paper Werewolf is actively experimenting with its attack chains, leveraging phishing PDFs, Inno Setup installers, and a variety of loaders and downloaders to deliver malicious payloads.
- The threat actor continues to develop custom Mythic implants, demonstrating a high level of expertise and technical maturity. This enables the group to maintain covert access to compromised environments and evade detection for longer periods.
- Adversaries have developed a dedicated PaperGrabber stealer to collect files from local and network drives and removable media, extract data from the Telegram messenger, and exfiltrate credentials stored in web browsers.

## EchoGather RAT phishing emails

In March–April 2026, Paper Werewolf conducted a phishing campaign targeting Russian industrial and financial organizations. The attackers distributed emails with PDF attachments containing a link to a ZIP file download. The archive conceals an Inno Setup installer executable that simulates the installation of legitimate software but, in fact, stealthily extracts and launches the EchoGather remote access trojan (RAT), along with a PDF decoy.

Press enter or click to view image in full size

Phishing email (The screenshots are AI-translated)

The PDF has an embedded URL pointing to a ZIP (`Adobe_Reader_RU.zi` p or`Adobe_Reader.zip`). When a user clicks Install Update, the archive is downloaded.

URL used:`hxxps://ntpluck[.]online/29mNqbkQB96clqjJMRsdVKa94ILLxbFclUe3wf4KSx0rRPtI9M/download/eeab4aec6ad3b271c303d927db55de273bbca008ebf00e06898336c6f3010296`

Press enter or click to view image in full size

Phishing PDF

The downloaded ZIP contains`Adobe_Acrobat_Reader_Plugin_ru.exe`, an installer created with Inno Setup. The installer encompasses the EchoGather executable and a PDF decoy.`Adobe_Acrobat_Reader_Plugin_ru.exe` simulates Adobe Acrobat plug-in installation. When launched, it extracts and opens`%APPDATA%\Adobe\adbp.exe` and`[installer_file_execution_directory]\Requirement.pdf`.

Press enter or click to view image in full size

Simulated Adobe Acrobat plug-in installation

Press enter or click to view image in full size

`Requirement.pdf` decoy

EchoGather allows adversaries to collect compromised system information, including local IP address, computer name, username, process ID (PID), and the path to the running file. It also loads files to/from the C2 server and executes incoming commands via the`cmd.exe` interpreter.

EchoGather remained largely unchanged (for additional detail, refer to our earlier research). However, in recent samples of this family, the threat actor removed explicit initialization of proxy values from the configuration. Instead, they introduced the magic parameter, whose value is djb2-calculated after the malware successfully passes all anti-virtualization checks. The magic value is subsequently verified during data retrieval and command execution initiated by the C2 server.

The EchoGather configuration data:

```
{"buildID": "3d0391a4-de3e-4322-ba67-5777c630b6a2","domain": "ntpsum[.]online","port": 443,"apiPath": "sum/M8suINj3ZFi22GMAUdCJH639vDrI2G4zdTWm2rpE5plxsr17Eg","userAgent": null,"httpMethod": "POST","useSSL": true,"sleepTime_ms": 314,"sleepTime_random": 15,"useAntiVM": true,"magic": 0x924A658}
```

## PaperGrabber stealer

In March 2026, during an analysis of Paper Werewolf network infrastructure, we discovered an associated`DocDownloader.exe` file that connects to`ntptop[.]online`. This executable is a previously undocumented VB.NET stealer that we dubbed PaperGrabber.

The malware enables file collection from local, network, and removable drives based on a predefined list of extensions. PaperGrabber also steals saved browser credentials and Telegram data. The retrieved information is exfiltrated to the C2 server over HTTPS. The stealer’s activity is logged and reported to a Telegram bot in a dedicated chat. The bot token and chat ID need to be indicated as executable launch parameters — otherwise, PaperGrabber terminates.

Supported arguments:

Press enter or click to view image in full size

The analyzed PaperGrabber sample uses the following default settings:

- enabledModes = None (activity mode)
- borrowFilesType = All (file collection mode)
- uploadExtensions =`".pdf,.doc,.docx,.txt,.rtf,.odt,.xls,.xlsx,.ppt,.pptx,.csv,.xps,.png,.gif,.jpg,.webp,.jpeg,.conf,.key,.ppk,.pub,.cer,.ovpn,.wg,.ods,.rdp,.vnc,.ssh,.sh,.kml,.kmz,.cdr,.vsd,.vsdx"`
- logExtensions =`".zip,.7z,.rar,.sql,.ps"`
- minFileSize = 0 bytes
- maxFileSize = 26,214,400 bytes

When launched, PaperGrabber retrieves the computer name and username, then sends them to the Telegram bot and chat specified in its arguments.

The stealer comprises the following classes: BorrowFilesMode, BorrowTelegramMode, BorrowBrowserDataMode, and WaitForRemovablesMode.

BorrowFilesMode collects files from local and network drives and removable media.

PaperGrabber can exclude certain directories from processing, namely: Windows, ProgramData, Recycler, Recovery, System Volume Information, Cache, Temp, Tmp, Logs, Log Files, AppData, Program Files, Program Files (x86), Microsoft, WindowsApps, Packages, .vs, Visual Studio, Licenses, SteamApps, Games, $Recycle.Bin, and FGAU.

During file collection, the malware references a list of target extensions either supplied as a launch argument or hardcoded in the sample by default.

Files whose names begin with`id_` or contain the`id_rsa`,`ssh`,`private`,`prv`,`key`,`rsa` substrings are of particular interest to the stealer. This behavior indicates a priority search for SSH keys and other cryptographic private keys.

Collection can also be restricted by file size. Minimum and maximum thresholds may be provided as launch parameters or fall back to hardcoded default values.

The PaperGrabber resources section contains an empty`KnownFiles.txt` used to exclude already processed or irrelevant files. Previously identified files are added to this list. The malware also employs MD5-based deduplication.

BorrowTelegramMode extracts Telegram sessions. It searches the system for a Telegram client in several directories:

- `%APPDATA%`
- Telegram Desktop UWP
- paths extracted from LNKs that may reference Telegram directories
- running processes (if the process description contains the string`"Telegram Desktop"`, it is considered a match)

After identifying the Telegram client path, the stealer copies the`tdata` directory that contains sensitive session data, including authorization keys, cache files, and other service-related information.

BorrowBrowserDataMode extracts saved credentials from browsers like Yandex Browser, Chrome, Opera, Edge, and Chromium. Data is retrieved from`Login Data` that stores encrypted usernames, passwords, and website URLs.

PaperGrabber uses the`ProtectedData.Unprotect()` method (DPAPI) for decryption. Once the master key is obtained, stored passwords are decrypted. If the procedure is incomplete or unsuccessful, the stealer retains whatever data is available. The results are exported to a file containing the URL, username, creation date, and decrypted password. The collected data is then loaded to a remote server.

A dedicated processing class is introduced for Yandex Browser, as its storage format and decryption mechanism differ from those of other Chromium-based browsers.

WaitForRemovablesMode monitors connected removable media and collects data from them. It detects newly connected devices and checks their type (`DriveType.Removable`). If a device is available and ready for use (IsReady), it is processed, and files may be extracted from it.

Before loading to the C2 server, the exfiltrated data is archived in the background without compression, with the ChunkedZipArchiver class. ChunkingStream is used to split the data stream into fixed 10 MB chunks.

## JS shellcode downloader

In March 2026, during an analysis of Paper Werewolf network infrastructure, we also uncovered related ZIP and RAR files comprising the following:

- `/node_modules/`: a standard directory in`Node.js` projects used to store installed dependencies (packages)
- `vain`: a`Node.js`-based JS code that checks for the presence of`%APPDATA%\yandex` which must contain`yandex.exe`,`vni.wsf`,`vain`; responsible for establishing persistence for`vni.wsf`
- `vain1`: a`Node.js`-based JS code that downloads the shellcode payload from the C2 server and executes it in the memory of the running process
- `vni.wsf`: a WSF containing JS code that launches the`vain1` JS downloader via`yandex.exe`(`node.exe`)
- `yandex.exe`: a legitimate`Node.js` interpreter (version 12.9.1)

In this attack chain,`vain` needs to be executed first. It adds`vni.wsf` to system startup via the following command:`reg add "HKCU\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Windows" /v LOAD /t REG_SZ /d "\"%APPDATA%vni.wsf\\"" /f`.

Notably, Paper Werewolf has already leveraged the`HKEY_CURRENT_USER\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\Windows\LOAD` registry parameter in its earlier attacks. Programs referenced in`LOAD` are executed in minimized mode.

`vain` source JS code

`vni.wsf` executes the following command to invoke`vain1` through the Node.js interpreter:`%APPDATA%\yandex\yandex.exe %APPDATA%\yandex\vain1`

`vni.wsf` source JS code

In turn,`vain1` acts as a downloader: it retrieves and executes the shellcode payload. The download process runs in an infinite loop, retrying every 43–57 seconds until successful. Once the payload is obtained, the malware allocates memory using HeapCreate and HeapAlloc WinAPI, writes shellcode into it, and triggers its execution via CreateThread.

To retrieve shellcode, the downloader generates a URL, inserts the computer name and username, then sends an HTTPS GET request. The payload itself was not available at the time of this research.

URL:`hxxps://zeccecard[.]com/116739/person_image/1167273647/48980/cis8petition/0201787911?asdzq=[hostname]&asdzf31=[username]`

User-Agent:`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.3`

## Custom-built Mythic implant with loaders

In March 2026, we discovered`111.rar` containing the following files:

- `py`: a Python loader that searches the current directory for`search.bin`, reads shellcode from the file, and executes that code in process memory via the CreateThread WinAPI function
- `ConsoleApplicationexe`: a C++ loader with a logic similar to`123.py`
- `search.bin`: a binary that contains obfuscated shellcode for a Mythic implant

Based on the structure and coding style,`123.py` may have been developed with the assistance of generative AI tools.

`123.py` loader source code

When shellcode is run, the malware creates the`5df098b7-efe6-4c1d-a7d1-dbc6519a66c2` mutex. Execution is then transferred to the function holding the implant’s main logic. There, strings are decrypted and required WinAPI functions are dynamically resolved. The resulting function pointers and strings are stored in a global malware structure used throughout subsequent operations.

Next, the malware performs an encryption key exchange with the C2 server. During this process, an RSA-4096 key pair is generated, a JSON object containing the public key is created, and data is loaded to the C2 server. Within initial communication, data is encrypted with a Base64-encoded AES key embedded in the stealer body.

С2 URL:`zeccecard[.]com/grain/duke`

JSON object:

```
{"action": "staging_rsa","pub_key": "[RSA_PUBKEY]","session_id": "<[A-Za-z]{20}>"}
```

The C2 server returns an AES session key used to encrypt communications.

After that, the following system information is sent to the C2 server:

```
{"action": "checkin","uuid": "fdee29ec-896f-49d6-8b3f-0be230b1c95a","user": "[username]","os": "Windows","host": "[computer name]","domain": "[domain name or computer name if not domain-joined]","sleep_info": "123 seconds","architecture": "x64","ips": "[list of local IP addresses]","process_name": "[full path to executable]","integrity_level": "[0-4, process privilege level]","pid": "[current process ID]"}
```

If time-based execution restrictions are enabled, the implant checks whether the current day of the week and hour match the allowed schedule. If the restriction is disabled, the implant waits for commands from the C2 server. Once a command is executed, the malware enters a sleep cycle (`sleep`) with intervals defined in its configuration.

Mythic implant commands:

Press enter or click to view image in full size

## C++ shellcode downloader

In April 2026,`Форма заявки на обучение.exe`(training application form) was detected in a Paper Werewolf campaign. The executable functions as a downloader that retrieves the shellcode payload from the C2 server. The file is disguised as an application form for flight school training.

## Get BI.ZONE’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

At startup, the downloader runs anti-virtualization checks:

- Calls the GetVolumeInformationA WinAPI function for drive C:\ and compares volumeSerialNumber against predefined values.
- Analyzes the command-line arguments of running processes for the following substrings:`"/not /w /mm /mc /c /sw /k"`,`"Users\John"`,`"Users\Bruno"`,`"second stage"`.

The malware then extracts the`Форма заявки.docx` decoy (application form) from its resource section, saves it to the directory from which the downloader was launched, and opens the file to distract a victim.

Press enter or click to view image in full size

`Форма заявки.docx` decoy

Next, the downloader generates a URL used to download the shellcode payload which is then executed in the memory of the current process. A victim’s username and computer name are inserted into the URL parameters.

URL:`hxxps://arrotech[.]org/pathclass/33205/freehash/katy?user=[username]&hostNetBIOS=[computername]`

User-Agent:`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36`

The payload was not available at the time of this research.

## .NET assembly downloader

In another Paper Werewolf campaign observed in April 2026, we detected a WSF (Windows Script File) named`МЕТОДИЧЕСКИЕ РЕКОМЕНДАЦИИ_по формированию прогноза поступлений налоговых платежей.wsf`(methodological recommendations for forecasting tax revenue). This file contains an embedded VBScript (VBS) payload. When executed, the VBS opens a decoy PDF in the system’s default web browser via a hardcoded URL.

Decoy URL:`hxxps://woburneast[.]com/171751/20020722/1306wicadigi023.pdf`

Press enter or click to view image in full size

`1306wicadigi023.pdf` decoy

The VBS then creates the following files in`%LOCALAPPDATA%`: the`msb_cache.xml` MSBuild file with an embedded C# program and`msb_run.vbs` used to execute the task.

Command that runs the MSBuild task:

`%SYSTEMROOT%\Microsoft.NET\(Framework|Framework64)\v4.0.30319\MSBuild.exe /nologo "%LOCALAPPDATA%\msb_cache.xml" /t:___RunHelloWorld___`

The script also adds`msb_run.vbs` to startup by creating the UserInitMprLogonScript parameter in`[HKCU\Environment]`, with the startup command set as the value:`wscript.exe %LOCALAPPDATA%\msb_run.vbs`.

The C# program is launched by a loader running in an infinite loop. Every 30 seconds, it sends a GET request to a remote resource with a 15-second timeout to retrieve the payload. The request includes X-Machine-Name and X-User-Name headers.

Payload URL:`hxxps://woburneast[.]com/t2376/dom/fwcookiemanager/bs_afp/872794`

The server is expected to return a .NET assembly and X-Entry-Point and X-Entry-Method headers. The assembly is then loaded directly into memory via Assembly.Load, after which the required method is invoked. The .NET assembly file was not available at the time of this research.

## Indicators of compromise

## Checksums

Archives

- `a4eacfe2fabb1eb5d888dfb5275506c12137cd54f603bc069d7e1767aa5f82f9`
- `4b8f437cd41c53a698c430a975fc7074e374712aca4c52fa49a8ab395b184f88`
- `4394ff157a86a44e5694ba40c93a982ac17c2f70c727b00efee63528f64b95de`
- `7b80c3055432a07680932778e2709e392b6b9dea21157badea76a14a4fc1f93a`
- `f3b5fa2d1cca8b4f232e08fb4bb64241f0caac93fc366deda7c23b6b6d7b4905`
- `f52d67e5b3e48208073dddd1c22728085a36744fdc91a0ca767cae6db9cdea74`

Phishing PDFs

- `f4a81dc69b87062e61bede3bf9f78b4d5f8df6afd856cacd6f1748370886d002`
- `64cda4837fc50bd651078d9a3925d6c8993a3b5426fba19cef16bd02c96e0520`

Inno Setup installer

- `551b705761a0d6015d596f0ce98d3552152e2c226ff57f89a3e315b6bb035956`
- `183a31a1615a18a6a9a86be41d342e4b5b10b0266ac6970ae46dc7e9d194307d`

EchoGather

- `77e1510002a5b04beadf7e5b7e8a96242849187a053906429e9c6a8d1facc0d1`
- `a208308930bf17df50e52cc0dcd14555e853c6da413836b60bf906f73ac94d9c`

PaperGrabber

`58f911d183b09ef9d587d1e59a5d17f9273581cee9891f4642e349b4f9f678b1`

JS loader

`4100708d2b461def58653a46344ec73aaabf2fafe4a2ebf27855b7b53dc30184`

JS downloaders

- `8b80626c8a42fe35c5d1fd2e1372fb57cfcf8b9eb969b1580350461389d227cc`
- `a6e0fc5de3e7ab1c6d0041f43a460bc3f3a02383c683223e684239ff65879140`

C++ loader

`5454f4811de9b1bf3b0e47cf8bad8e8e915b7379a0f3dffd5d36dcad26bdc03b`

C++ downloader

`938dac6227e47fed245ad25d289489d67e574882430652b5fb7b6368e262e873`

Python loader

`7d6d07b42f1b2a0728ae7b7ede14daf195d2b7baa1325065c4877e8db93e2c4f`

Binary file containing shellcode

`ad8c30add66c0043299fac827f1ffa174c786bcff846184cd2c135024c1d340b`

WSF files

- `71ad29aeabbbd78b7414541e48064a0bfb9d96b47d7a3a48f53729817fe54ab5`
- `6a997b7799f0ccb241219995ea275ffbf99d22a3777b442e7bb7ab907aef3641`

XML file

`def336fa0f8dfcc60f85a7a862e07730d0e99052515d1b5f7bbdd435de595aee`

VBScript files

`c5645cbd4295278a23c243e79a3f519b9a6ca8b59f7a4afa92c77e6ed737f080`

Decoys

- `e5edd8e5efb1ffc1804ac51f88f7401d91f9b0fd8cd3da1ba0a5fab401523446`
- `3a4d84886713695f3b3812a0a3733f9ce74b4614c881f9774995c01c61d09cf3`
- `8ae62e8a521a79e1ddfa4e360d5abce992bb671644ca7473c02dcfa120e575d1`
- `3c3ea0512687ff086c605cb6d331d0d588c39f362ee5bc580059b481410c1585`

## Network indicators

URLs

- `hxxps://ntpluck[.]online/29mNqbkQB96clqjJMRsdVKa94ILLxbFclUe3wf4KSx0rRPtI9M/download/eeab4aec6ad3b271c303d927db55de273bbca008ebf00e06898336c6f3010296`
- `hxxps://ntpsum[.]online/sum/M8suINj3ZFi22GMAUdCJH639vDrI2G4zdTWm2rpE5plxsr17Eg`
- `hxxps://ssltop[.]online/l402XY5rTBxLPOJDTnqlRCePwy2puTnieDSFVaHEKOyb0Eqh3y/download/32712a3f7ec72fac4535b47017135a72b4994ee69440eff95221fed673d41fdc`
- `hxxps://certcalc[.]online/certificate/calculate/G8OftO2lyUuRHa8wBuqR7wcOfAcirSnrp0PCsA3ST17RjjL7JQ`
- `hxxps://ntptop[.]online/VaukY9uSiPjpylxpDeTXQgmh0QLy2Q9I8kYY6OFyt0wFqz3yZF/upload`
- `hxxps://zeccecard[.]com/116739/person_image/1167273647/48980/cis8petition/0201787911?asdzq`
- `hxxps://zeccecard[.]com/grain/duke`
- `hxxps://arrotech[.]org/pathclass/33205/freehash/katy`
- `hxxps://woburneast[.]com/171751/20020722/1306wicadigi023.pdf`
- `hxxps://woburneast[.]com/t2376/dom/fwcookiemanager/bs_afp/872794`

Domains

- `ntpluck[.]online`
- `ntpsum[.]online`
- `ssltop[.]online`
- `certcalc[.]online`
- `ntptop[.]online`
- `zeccecard[.]com`
- `arrotech[.]org`
- `woburneast[.]com`

## MITRE ATT&CK

## How to protect your company from such threats

Building an effective cybersecurity strategy against Paper Werewolf attacks requires an understanding of tools and techniques used by the group. This task is further complicated by the continuous evolution of the threat actor’s toolkit comprising custom-built loaders and downloaders and dedicated implants that are harder to detect with conventional security solutions.

BI.ZONE Threat Intelligence helps organizations stay proactive and prevent such threats. The solution provides the latest information about threat actors, their tactics, techniques, and tools, as well as data from underground resources for faster detection and response.

## Written by BI.ZONE

BI.ZONE is an expert in digital risks management. We help organizations develop their businesses safely in cyberspace.

## No responses yet

## More from BI.ZONE

·

Apr 15, 2021

## Hunting Down MS Exchange Attacks. Part 1. ProxyLogon (CVE-2021–26855, 26858, 27065, 26857)

### By Anton Medvedev, Demyan Sokolin, Vadim Khrykov

A response icon3

·

Jun 9

## Fluffy Wolf tests new toolkit on Russian companies

### From March to May 2026, we uncovered a series of phishing attacks by Fluffy Wolf. The threat actor targeted Russian organizations across…

·

Apr 28, 2025

## Exploring CVE-2025–24364 and CVE-2025–24365 in Vaultwarden

### According to BI.ZONE TDR, 10% of Russian companies use Vaultwarden this year.

·

Aug 19, 2025

## Deep dive into CVE-2025–29824 in Windows

### Author: Andrey Chizhov, Senior Vulnerability Researcher

See all from BI.ZONE

## Recommended from Medium

·

3d ago

## You only have weeks left to vibe code

### Then it’s over. You better hurry up!

A response icon64

·

2d ago

## 117 People Waited 21 Years for One Feature. It Finally Arrived.

### Every expert who looked at it said it could not be built, and they closed the case. The one who reopened it had never written a line of…

A response icon6

·

Jun 23

## The apps I’ve kept for 5+ years

### Most apps do not survive very long in my stack.

A response icon1

In

by

·

2d ago

## 7 Native Mac Apps for Anyone Sick of Electron

### Stop letting Electron apps bloat your RAM and drain your battery.

A response icon3

In

Level Up Coding

by

·

2d ago

## Ornith 1.0: The 9B Coding Model That Writes Its Own Harness

### Ornith-1.0–9B scores 69.4 on SWE-bench Verified. The 9B Qwen 3.5 baseline sitting next to it in the same model card scores 53.2. Move up to…

A response icon2

·

3d ago

## Turn a city map into wall art in your browser — this Rust rendering engine is absolutely stunning

### Turn a city map into wall art — something that used to require a designer can now be done right in your browser.

See more recommendations

Text to speech