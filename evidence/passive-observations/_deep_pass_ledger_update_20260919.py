from pathlib import Path
import hashlib

root = Path(__file__).resolve().parents[2]


def sha(rel: str) -> str:
    p = root / rel
    return hashlib.sha256(p.read_bytes()).hexdigest()


def append_rows(path: Path, rows: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"appended {len(rows)} -> {path.relative_to(root)}")


rap_claims = [
    "RAP-CLAIM-0035,Rapuncel,RAP,urlscan public scan 01a01b78 (2026-08-19 Hybrid Analysis tag) shows massimolongqdoj.github.io/.github/DoNotSpy11 redirecting off-domain to albinofennel.com (Cloudflare 523 Origin unreachable at scan time).,ETW urlscan,Passive,urlscan search domain:albinofennel.com / result 01a01b78-6612-77eb-89ff-405327ef33ec,https://urlscan.io/result/01a01b78-6612-77eb-89ff-405327ef33ec/,2026-08-19,OBSERVED_PASSIVE,OBSERVED_PASSIVE,High,true,infrastructure|GitHub Pages|lure,RAP-PO-0021,,Additional fraudulent GH Pages host beyond LastPass-Authenticator / edgarcostartqd / dallikilic54. Do not auto-attribute operator identity.,2026-09-19T19:10:00Z,true",
    "RAP-CLAIM-0036,Rapuncel,RAP,urlscan public scan 019f9bc6 (2026-07-26) captured live albinofennel.com/o8ehlpnvdqan/passathook-cs2.github.io lure page (HTTP 200 Cloudflare) titled Passathook Cs2 · Github.,ETW urlscan,Passive,urlscan search domain:albinofennel.com / result 019f9bc6-946f-701b-bffc-eded8020c489,https://urlscan.io/result/019f9bc6-946f-701b-bffc-eded8020c489/,2026-07-26,OBSERVED_PASSIVE,CORROBORATED,High,true,lineage|BoryptGrab|infrastructure,RAP-PO-0021,RAP-CLAIM-0022,Independently corroborates LastPass passathook-cs2 brand path on payload host; not byte proof of BoryptGrab identity.,2026-09-19T19:10:00Z,true",
    "RAP-CLAIM-0037,Rapuncel,RAP,crt.sh CT: istatlmenus.com and macperformancetools.com share earliest not_before 2026-03-06; zaffersnouty.com first 2026-02-07; albinofennel.com first 2026-07-19; hanselarinmusky.com first 2026-08-06; icansamyope.com zero CT hits.,ETW crt.sh,Passive,HTTP GET crt.sh output=json for Rapuncel domains,https://crt.sh/?q=istatlmenus.com,2026-09-19,OBSERVED_PASSIVE,OBSERVED_PASSIVE,High,true,infrastructure|CT|chronology,RAP-PO-0007;RAP-PO-0009;RAP-PO-0011;RAP-PO-0001;RAP-PO-0003,,Chronology only — not actor ownership. Payload hosts appear later than traffic-director/terminal domains.,2026-09-19T19:10:00Z,true",
    "RAP-CLAIM-0038,Rapuncel,RAP,Cloudflare DoH 2026-09-19: albinofennel.com returns NXDOMAIN (Status=3); istatlmenus.com/macperformancetools.com/zaffersnouty.com/hanselarinmusky.com still resolve to Cloudflare A records.,ETW Cloudflare DoH,Passive,DNS-over-HTTPS A queries,https://cloudflare-dns.com/dns-query?name=albinofennel.com&type=A,2026-09-19,OBSERVED_PASSIVE,OBSERVED_PASSIVE,High,true,infrastructure|dns,RAP-PO-0022,,RESOLVING != serving malware. Aligns with PK Sharma NXDOMAIN for albinofennel; adds hanselarinmusky still resolving.,2026-09-19T19:10:00Z,true",
    "RAP-CLAIM-0039,Rapuncel,RAP,eSentire published Cruciferra IOC list includes DCRCVDrv.sys SHA-256 87e8d39db624f37d3e77aedf487a2dfd197f71a4730ea74f4e7a4341deaec2ff and Cruciferra DLL 0ae0a7f118b80e4655b8b86bb421c151a8f17930e76e714b2fa199409f3af9ce — distinct from Rapuncel Alinubx 611b3ba6… (shared tooling class ≠ same actor).,eSentire,TRU / GitHub IOCs,cruciferra-IoCs-08-12-2026.txt,https://raw.githubusercontent.com/eSentire/iocs/main/Cruciferra/cruciferra-IoCs-08-12-2026.txt,2026-08-12,PRIMARY,PRIMARY_SOURCE,High,false,track:cruciferra|driver|lineage,PS-RAP-002,RAP-CLAIM-0030,Do not merge DCRCVDrv into Rapuncel campaign IOC set without independent Rapuncel linkage.,2026-09-19T19:10:00Z,true",
    "RAP-CLAIM-0040,Rapuncel,RAP,eSentire Cruciferra sideloaded-apps CSV lists Microsoft vsdbg.exe among PUROSANGUE sideload targets (hash 3be2a5198dc46686ac514b8c70ecb28a8aff4dd56d4d0c60f66ebf5518ec85c9) — same legitimate host binary class used in Rapuncel delivery.,eSentire,TRU / GitHub IOCs,cruciferra_sideloaded_apps.csv,https://raw.githubusercontent.com/eSentire/iocs/main/Cruciferra/cruciferra_sideloaded_apps.csv,2026-08-19,PRIMARY,PRIMARY_SOURCE,Moderate,false,track:cruciferra|DLL-sideload|RAP-H-CRY,PS-RAP-003,RAP-CLAIM-0009,Supports crypter-supplied sideload catalog overlap; not proof same campaign operator.,2026-09-19T19:10:00Z,true",
    "RAP-CLAIM-0041,Rapuncel,RAP,LOLDrivers entry for CcProtect.sys documents SHA-256 5f0cfe8357bb52b45068ddbac053e32bc38e6cb5e086746f5402657b0a5cfb1c Creation Timestamp 2022-03-04 and WHCP-signed CnCrypt Protect Driver metadata matching Delphos Alinubx identity-swap baseline.,LOLDrivers,,CcProtect.sys driver entry 3e3067b0-3d74-46fe-9f57-1ae3a0293958,https://www.loldrivers.io/drivers/3e3067b0-3d74-46fe-9f57-1ae3a0293958/,2026-08-27,PRIMARY,PRIMARY_SOURCE,High,false,driver|CcProtect|Alinubx,PS-RAP-004,RAP-CLAIM-0016,Reference driver corpus for Alinubx comparison; shared vulnerable driver ≠ Rapuncel exclusive.,2026-09-19T19:10:00Z,true",
]

set_claims = [
    "SET-CLAIM-0016,Settra,SET,Kaspersky GERT (Dec 2024 Securelist): SSL certificate CN on port 7777 of a Hetzner-hosted scanner/attacker-adjacent host was WIN-LIVFRVQFMKO during FortiClient EMS CVE-2023-48788 exploitation IR; authors note Conti/LockBit frequent-use clustering OR default Windows/Hetzner template hostname — NOT Settra-exclusive.,Kaspersky,GERT,Attackers exploiting a FortiClient EMS vulnerability in the wild,https://securelist.com/patched-forticlient-ems-vulnerability-exploited-in-the-wild/115046/,2024-12-19,PRIMARY,PRIMARY_SOURCE,High,false,operator|WIN-LIVFRVQFMKO|UNKNOWN,PS-SET-005,SET-CLAIM-0010,Strengthens multi-campaign hostname reuse; do not attribute FortiClient EMS activity to Settra.,2026-09-19T19:10:00Z,true",
    "SET-CLAIM-0017,Settra,SET,urlscan public scans show 193.5.65.114 serving MeshCentral Login (tlsIssuer MeshCentralRoot-eca57f) on 2025-09-11 and earlier id-manulife.com pages resolving to the same IP with MeshCentral title on 2025-07-30 (and a 2025-05-05 certstream scan of id-manulife.com also on that IP).,ETW urlscan,Passive,urlscan search ip:193.5.65.114,https://urlscan.io/api/v1/search/?q=ip:193.5.65.114,2025-05-05,OBSERVED_PASSIVE,INFRASTRUCTURE_OVERLAP,High,true,operator|MeshAgent|MeshCentral|chronology,SET-PO-0003,SET-CLAIM-0008,Pre-dates Huntress ~2025-11 association window. UNKNOWN/not Settra-exclusive — domain id-manulife.com is ASSOCIATION_ONLY overlap.,2026-09-19T19:10:00Z,true",
    "SET-CLAIM-0018,Settra,SET,RDAP for 193.5.65.114: RIPE assignment NL-RAPIDSEEDBOX-20250306 (Rapid Seedbox / Seychelles admin contact) — hosting allocation metadata only; not malware-author identity.,ETW RDAP,Passive,HTTP GET rdap.org/ip/193.5.65.114,https://rdap.org/ip/193.5.65.114,2026-09-19,OBSERVED_PASSIVE,OBSERVED_PASSIVE,Moderate,true,infrastructure|rdap,SET-PO-0002,,Confirms seedbox/VPS hosting surface for MeshAgent IP; author_attribution=NOT_ESTABLISHED.,2026-09-19T19:10:00Z,true",
]

rap_inds = [
    "RAP-IND-0031,Rapuncel,massimolongqdoj.github.io,url,2026-08-19,OBSERVED_PASSIVE,High,true,https://urlscan.io/result/01a01b78-6612-77eb-89ff-405327ef33ec/,2026-09-19T19:10:00Z,GitHub Pages lure path /.github/DoNotSpy11 redirected to albinofennel.com (urlscan). Manifest RAP-PO-0021. Not actor attribution.,CAMPAIGN_ASSOCIATED",
    "RAP-IND-0032,Rapuncel,github.com/massimolongqdoj,repository,2026-08-19,OBSERVED_PASSIVE,Moderate,true,https://urlscan.io/result/01a01b78-6612-77eb-89ff-405327ef33ec/,2026-09-19T19:10:00Z,Org/user inferred from Pages hostname only — verify before takedown. ASSOCIATION to Rapuncel via albinofennel redirect.,SUSPICIOUS",
    "RAP-IND-0033,Rapuncel,https://albinofennel.com/o8ehlpnvdqan/passathook-cs2.github.io,url,2026-07-26,OBSERVED_PASSIVE,High,true,https://urlscan.io/result/019f9bc6-946f-701b-bffc-eded8020c489/,2026-09-19T19:10:00Z,urlscan-observed branded lure path on payload host. Corroborates LastPass passathook-cs2 mention.,CAMPAIGN_ASSOCIATED",
    "RAP-IND-0034,Rapuncel,87e8d39db624f37d3e77aedf487a2dfd197f71a4730ea74f4e7a4341deaec2ff,sha256,unspecified,PRIMARY-SOURCE,High,false,https://raw.githubusercontent.com/eSentire/iocs/main/Cruciferra/cruciferra-IoCs-08-12-2026.txt,2026-09-19T19:10:00Z,DCRCVDrv.sys Cruciferra BYOVD — lineage comparison only; NOT a Rapuncel campaign hash unless independently linked.,CAMPAIGN_ASSOCIATED",
    "RAP-IND-0035,Rapuncel,0ae0a7f118b80e4655b8b86bb421c151a8f17930e76e714b2fa199409f3af9ce,sha256,unspecified,PRIMARY-SOURCE,High,false,https://raw.githubusercontent.com/eSentire/iocs/main/Cruciferra/cruciferra-IoCs-08-12-2026.txt,2026-09-19T19:10:00Z,Cruciferra mscoree.dll from eSentire IOC list — track:cruciferra only; not Rapuncel delivery artifact.,CAMPAIGN_ASSOCIATED",
    "RAP-IND-0036,Rapuncel,\\\\.\\DCRCVDRV_U,device,unspecified,PRIMARY-SOURCE,High,false,https://www.esentire.com/blog/malware-as-a-service-cocktail-errtraffic-and-cruciferra-killing-your-edr-since-2025,2026-09-19T19:10:00Z,Cruciferra DCRCVDrv device object — contrast with Rapuncel \\\\.\\Alinubx. Shared tooling ≠ same actor.,CAMPAIGN_ASSOCIATED",
]

set_inds = [
    "SET-IND-0015,Settra,id-manulife.com,domain,2025-05-05,OBSERVED_PASSIVE,Low,true,https://urlscan.io/api/v1/search/?q=ip:193.5.65.114,2026-09-19T19:10:00Z,Historical domain resolving to MeshAgent IP 193.5.65.114 (MeshCentral UI). INFRASTRUCTURE_OVERLAP / UNKNOWN — not Settra-exclusive.,SUSPICIOUS",
    "SET-IND-0016,Settra,MeshCentralRoot-eca57f,tls_issuer,2025-07-30,OBSERVED_PASSIVE,Moderate,true,https://urlscan.io/result/019939fe-261d-761d-b4c3-8d0eae2a8bf2/,2026-09-19T19:10:00Z,urlscan tlsIssuer for MeshCentral panel on 193.5.65.114. Detection artifact — not Settra malware hash.,CAMPAIGN_ASSOCIATED",
]

po_rows = [
    f"RAP-PO-0021,Rapuncel,albinofennel.com,urlscan,\"results=2; uuids=01a01b78…,019f9bc6…; massimolongqdoj+passathook\",2026-09-19T19:01:08Z,HTTP GET urlscan.io/api/v1/search,urlscan.io,domain:albinofennel.com,evidence/passive-observations/urlscan/rapuncel/urlscan_albinofennel_2026-09-19T190108Z.json,{sha('evidence/passive-observations/urlscan/rapuncel/urlscan_albinofennel_2026-09-19T190108Z.json')},OBSERVED_PASSIVE,High,OBSERVED_PASSIVE,2026-07-26,2026-08-19,,Public urlscan metadata only. Redirect/lure facts ≠ actor ownership.",
    f"RAP-PO-0022,Rapuncel,albinofennel.com,dns_doh,NXDOMAIN Status=3,2026-09-19T19:01:08Z,Cloudflare DoH application/dns-json,cloudflare-dns.com,albinofennel.com A,evidence/passive-observations/dns/rapuncel/doh_albinofennel_2026-09-19T190108Z.json,{sha('evidence/passive-observations/dns/rapuncel/doh_albinofennel_2026-09-19T190108Z.json')},OBSERVED_PASSIVE,High,OBSERVED_PASSIVE,,,,DoH NXDOMAIN observation. Not attribution.",
    f"RAP-PO-0023,Rapuncel,istatlmenus.com,dns_doh,\"A=172.67.212.253,104.21.85.249\",2026-09-19T19:01:08Z,Cloudflare DoH application/dns-json,cloudflare-dns.com,istatlmenus.com A,evidence/passive-observations/dns/rapuncel/doh_istatlmenus_2026-09-19T190108Z.json,{sha('evidence/passive-observations/dns/rapuncel/doh_istatlmenus_2026-09-19T190108Z.json')},OBSERVED_PASSIVE,High,ASSOCIATION_ONLY,,,,Cloudflare edges — ASSOCIATION_ONLY.",
    f"SET-PO-0003,Settra,193.5.65.114,urlscan,\"results=3; MeshCentral Login; id-manulife.com overlap\",2026-09-19T19:01:08Z,HTTP GET urlscan.io/api/v1/search,urlscan.io,ip:193.5.65.114,evidence/passive-observations/urlscan/settra/urlscan_193.5.65.114_2026-09-19T190108Z.json,{sha('evidence/passive-observations/urlscan/settra/urlscan_193.5.65.114_2026-09-19T190108Z.json')},OBSERVED_PASSIVE,High,INFRASTRUCTURE_OVERLAP,2025-05-05,2025-09-11,,MeshCentral panel + historical domain overlap. UNKNOWN/not Settra-exclusive. Not attribution.",
]

ps_set = root / "evidence/primary-sources/settra/kaspersky-forticlient-ems-win-liv_2026-09-19T185350Z.html"
ps_ioc = root / "evidence/primary-sources/rapuncel/esentire-cruciferra-iocs_2026-09-19T190108Z.txt"
ps_side = root / "evidence/primary-sources/rapuncel/esentire-cruciferra-sideload_2026-09-19T190108Z.csv"
ps_lol = root / "evidence/primary-sources/rapuncel/loldrivers-ccprotect_2026-09-19T190108Z.html"

ps_rows = [
    f"PS-SET-005,SOURCE-SET-KASPERSKY-EMS,https://securelist.com/patched-forticlient-ems-vulnerability-exploited-in-the-wild/115046/,2026-09-19T18:53:50Z,text/html; charset=UTF-8,kaspersky-forticlient-ems-win-liv_2026-09-19T185350Z.html,{sha('evidence/primary-sources/settra/kaspersky-forticlient-ems-win-liv_2026-09-19T185350Z.html')},HTTP GET curl ETW-PassiveCollector,2024-12-19,Kaspersky GERT / Securelist,settra,PRIMARY-SOURCE,CONTENT-VERIFIED,true,false,{ps_set.stat().st_size},200,WIN-LIVFRVQFMKO;7777;Hetzner,Hostname clustering PRIMARY for multi-campaign reuse — NOT Settra attribution.",
    f"PS-RAP-002,SOURCE-RAP-ESE-IOC,https://raw.githubusercontent.com/eSentire/iocs/main/Cruciferra/cruciferra-IoCs-08-12-2026.txt,2026-09-19T19:01:08Z,text/plain,esentire-cruciferra-iocs_2026-09-19T190108Z.txt,{sha('evidence/primary-sources/rapuncel/esentire-cruciferra-iocs_2026-09-19T190108Z.txt')},HTTP GET curl ETW-PassiveCollector,2026-08-12,eSentire,rapuncel,PRIMARY-SOURCE,CONTENT-VERIFIED,true,false,{ps_ioc.stat().st_size},200,DCRCVDrv;87e8d39d,Cruciferra lineage IOC file — case-isolated from Rapuncel campaign IOCs.",
    f"PS-RAP-003,SOURCE-RAP-ESE-SIDELOAD,https://raw.githubusercontent.com/eSentire/iocs/main/Cruciferra/cruciferra_sideloaded_apps.csv,2026-09-19T19:01:08Z,text/csv,esentire-cruciferra-sideload_2026-09-19T190108Z.csv,{sha('evidence/primary-sources/rapuncel/esentire-cruciferra-sideload_2026-09-19T190108Z.csv')},HTTP GET curl ETW-PassiveCollector,2026-08-19,eSentire,rapuncel,PRIMARY-SOURCE,CONTENT-VERIFIED,true,false,{ps_side.stat().st_size},200,vsdbg.exe,PUROSANGUE sideload catalog including vsdbg.exe.",
    f"PS-RAP-004,SOURCE-RAP-LOLDRIVERS-CCP,https://www.loldrivers.io/drivers/3e3067b0-3d74-46fe-9f57-1ae3a0293958/,2026-09-19T19:01:08Z,text/html,loldrivers-ccprotect_2026-09-19T190108Z.html,{sha('evidence/primary-sources/rapuncel/loldrivers-ccprotect_2026-09-19T190108Z.html')},HTTP GET curl ETW-PassiveCollector,2026-08-27,LOLDrivers,rapuncel,PRIMARY-SOURCE,CONTENT-VERIFIED,true,false,{ps_lol.stat().st_size},200,5f0cfe83;CcProtect,Reference CcProtect.sys hashes/metadata for Alinubx identity-swap analysis.",
]

append_rows(root / "investigations/rapuncel/claims/claims-ledger.csv", rap_claims)
append_rows(root / "investigations/settra/claims/claims-ledger.csv", set_claims)
append_rows(root / "investigations/rapuncel/evidence/published-indicators.csv", rap_inds)
append_rows(root / "investigations/settra/evidence/published-indicators.csv", set_inds)
append_rows(root / "evidence/manifests/passive-observation-manifest.csv", po_rows)
append_rows(root / "evidence/manifests/primary-source-manifest.csv", ps_rows)
print("ok")
