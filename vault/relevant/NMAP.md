## SCANS

```bash
┌──(kali㉿kali)-[~]
└─$ sudo nmap 10.10.219.188 -sS -sV -sC -v     
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-23 05:36 EDT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 05:36
Completed NSE at 05:36, 0.00s elapsed
Initiating NSE at 05:36
Completed NSE at 05:36, 0.00s elapsed
Initiating NSE at 05:36
Completed NSE at 05:36, 0.00s elapsed
Initiating Ping Scan at 05:36
Scanning 10.10.219.188 [4 ports]
Completed Ping Scan at 05:36, 0.01s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 05:36
Completed Parallel DNS resolution of 1 host. at 05:36, 13.00s elapsed
Initiating SYN Stealth Scan at 05:36
Scanning 10.10.219.188 [1000 ports]
Discovered open port 80/tcp on 10.10.219.188
Discovered open port 139/tcp on 10.10.219.188
Discovered open port 3389/tcp on 10.10.219.188
Discovered open port 445/tcp on 10.10.219.188
Discovered open port 135/tcp on 10.10.219.188
Completed SYN Stealth Scan at 05:36, 5.09s elapsed (1000 total ports)
Initiating Service scan at 05:36
Scanning 5 services on 10.10.219.188
Completed Service scan at 05:37, 7.66s elapsed (5 services on 1 host)
NSE: Script scanning 10.10.219.188.
Initiating NSE at 05:37
Completed NSE at 05:37, 40.08s elapsed
Initiating NSE at 05:37
Completed NSE at 05:37, 0.44s elapsed
Initiating NSE at 05:37
Completed NSE at 05:37, 0.00s elapsed
Nmap scan report for 10.10.219.188
Host is up (0.017s latency).
Not shown: 995 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Windows Server 2016 Standard Evaluation 14393 microsoft-ds
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2024-07-23T09:38:03+00:00; +21s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: RELEVANT
|   NetBIOS_Domain_Name: RELEVANT
|   NetBIOS_Computer_Name: RELEVANT
|   DNS_Domain_Name: Relevant
|   DNS_Computer_Name: Relevant
|   Product_Version: 10.0.14393
|_  System_Time: 2024-07-23T09:37:23+00:00
| ssl-cert: Subject: commonName=Relevant
| Issuer: commonName=Relevant
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-07-22T09:32:11
| Not valid after:  2025-01-21T09:32:11
| MD5:   e546:3f1c:ea68:59f5:7e0d:835a:9a1d:0203
|_SHA-1: 9f72:fe06:0d0e:eabb:3882:324c:343e:5360:1e93:9c12
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2024-07-23T09:37:26
|_  start_date: 2024-07-23T09:32:30
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: Relevant
|   NetBIOS computer name: RELEVANT\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2024-07-23T02:37:25-07:00
|_clock-skew: mean: 1h24m21s, deviation: 3h07m51s, median: 20s

NSE: Script Post-scanning.
Initiating NSE at 05:37
Completed NSE at 05:37, 0.00s elapsed
Initiating NSE at 05:37
Completed NSE at 05:37, 0.00s elapsed
Initiating NSE at 05:37
Completed NSE at 05:37, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 66.53 seconds
           Raw packets sent: 2001 (88.012KB) | Rcvd: 8 (340B)
                                                                
```

Going way too fast 

```
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.185.23 -p - --max-retries 0  -v -Pn -sT -T4                    
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-24 12:29 EDT
Initiating Parallel DNS resolution of 1 host. at 12:29
Completed Parallel DNS resolution of 1 host. at 12:29, 13.00s elapsed
Initiating Connect Scan at 12:29
Scanning 10.10.185.23 [65535 ports]
Warning: 10.10.185.23 giving up on port because retransmission cap hit (0).
Connect Scan Timing: About 0.95% done
Connect Scan Timing: About 1.86% done; ETC: 13:23 (0:53:36 remaining)
Connect Scan Timing: About 7.06% done; ETC: 13:24 (0:50:52 remaining)
Connect Scan Timing: About 12.01% done; ETC: 13:23 (0:48:07 remaining)
Connect Scan Timing: About 71.04% done; ETC: 12:39 (0:02:53 remaining)
Completed Connect Scan at 12:36, 428.51s elapsed (65535 total ports)
Nmap scan report for 10.10.185.23
Host is up (0.077s latency).
All 65535 scanned ports on 10.10.185.23 are in ignored states.
Not shown: 37439 filtered tcp ports (no-response), 28096 closed tcp ports (conn-refused)

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 441.55 seconds
                                                                       
```

```
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.185.23 -p - -v -Pn -sT     
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-24 12:38 EDT
Initiating Parallel DNS resolution of 1 host. at 12:38
Completed Parallel DNS resolution of 1 host. at 12:38, 13.00s elapsed
Initiating Connect Scan at 12:38
Scanning 10.10.185.23 [65535 ports]
Discovered open port 10000/tcp on 10.10.185.23
Connect Scan Timing: About 30.13% done; ETC: 12:40 (0:01:12 remaining)
Connect Scan Timing: About 64.89% done; ETC: 12:40 (0:00:33 remaining)
Discovered open port 9999/tcp on 10.10.185.23
Completed Connect Scan at 12:40, 92.65s elapsed (65535 total ports)
Nmap scan report for 10.10.185.23
Host is up (0.055s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT      STATE SERVICE
9999/tcp  open  abyss
10000/tcp open  snet-sensor-mgmt

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 105.72 seconds
                                                                          

```

Tried to do something similar but with the machine provided by tryhackme (it's faster in general to do scans so i thought the following might work out, as it needs a more reliable network).

```
root@ip-10-10-165-55:~# sudo nmap -sS -A --defeat-rst-ratelimit 10.10.42.22 -v -p - -T4

Starting Nmap 7.60 ( https://nmap.org ) at 2024-07-25 10:27 BST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 10:27
Completed NSE at 10:27, 0.00s elapsed
Initiating NSE at 10:27
Completed NSE at 10:27, 0.00s elapsed
Initiating ARP Ping Scan at 10:27
Scanning 10.10.42.22 [1 port]
Completed ARP Ping Scan at 10:27, 0.22s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 10:27
Completed Parallel DNS resolution of 1 host. at 10:27, 0.00s elapsed
Initiating SYN Stealth Scan at 10:27
Scanning ip-10-10-42-22.eu-west-1.compute.internal (10.10.42.22) [65535 ports]
Discovered open port 3389/tcp on 10.10.42.22
Discovered open port 135/tcp on 10.10.42.22
Discovered open port 80/tcp on 10.10.42.22
Discovered open port 139/tcp on 10.10.42.22
Discovered open port 445/tcp on 10.10.42.22
SYN Stealth Scan Timing: About 4.17% done; ETC: 10:40 (0:11:53 remaining)
SYN Stealth Scan Timing: About 8.74% done; ETC: 10:39 (0:10:37 remaining)
SYN Stealth Scan Timing: About 13.30% done; ETC: 10:39 (0:09:53 remaining)
SYN Stealth Scan Timing: About 18.07% done; ETC: 10:38 (0:09:09 remaining)
SYN Stealth Scan Timing: About 23.18% done; ETC: 10:38 (0:08:30 remaining)
SYN Stealth Scan Timing: About 28.20% done; ETC: 10:38 (0:07:56 remaining)
SYN Stealth Scan Timing: About 33.60% done; ETC: 10:38 (0:07:21 remaining)
SYN Stealth Scan Timing: About 38.91% done; ETC: 10:38 (0:06:47 remaining)
SYN Stealth Scan Timing: About 44.34% done; ETC: 10:38 (0:06:10 remaining)
Discovered open port 49663/tcp on 10.10.42.22
Discovered open port 49669/tcp on 10.10.42.22
SYN Stealth Scan Timing: About 49.61% done; ETC: 10:38 (0:05:36 remaining)
SYN Stealth Scan Timing: About 55.07% done; ETC: 10:38 (0:04:59 remaining)
SYN Stealth Scan Timing: About 60.49% done; ETC: 10:38 (0:04:23 remaining)
SYN Stealth Scan Timing: About 65.79% done; ETC: 10:38 (0:03:48 remaining)
SYN Stealth Scan Timing: About 70.82% done; ETC: 10:38 (0:03:14 remaining)
SYN Stealth Scan Timing: About 76.00% done; ETC: 10:38 (0:02:40 remaining)
SYN Stealth Scan Timing: About 81.06% done; ETC: 10:38 (0:02:06 remaining)
Discovered open port 5985/tcp on 10.10.42.22
SYN Stealth Scan Timing: About 86.37% done; ETC: 10:38 (0:01:31 remaining)
SYN Stealth Scan Timing: About 91.35% done; ETC: 10:38 (0:00:58 remaining)
Discovered open port 49667/tcp on 10.10.42.22
Completed SYN Stealth Scan at 10:38, 663.13s elapsed (65535 total ports)
Initiating Service scan at 10:38
Scanning 9 services on ip-10-10-42-22.eu-west-1.compute.internal (10.10.42.22)
Completed Service scan at 10:39, 53.56s elapsed (9 services on 1 host)
Initiating OS detection (try #1) against ip-10-10-42-22.eu-west-1.compute.internal (10.10.42.22)
Retrying OS detection (try #2) against ip-10-10-42-22.eu-west-1.compute.internal (10.10.42.22)
NSE: Script scanning 10.10.42.22.
Initiating NSE at 10:39
Completed NSE at 10:40, 40.48s elapsed
Initiating NSE at 10:40
Completed NSE at 10:40, 0.01s elapsed
Nmap scan report for ip-10-10-42-22.eu-west-1.compute.internal (10.10.42.22)
Host is up (0.00063s latency).
Not shown: 65526 filtered ports
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT      STATE SERVICE       VERSION
80/tcp    open  http          Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds  Windows Server 2016 Standard Evaluation 14393 microsoft-ds
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=Relevant
| Issuer: commonName=Relevant
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-07-24T09:04:55
| Not valid after:  2025-01-23T09:04:55
| MD5:   e147 fbb2 4724 db5d 67a2 64a4 8bb6 f955
|_SHA-1: ceb7 50f0 b77b f866 80ce c67b c24d 5c71 cbd3 3ce8
|_ssl-date: 2024-07-25T09:39:40+00:00; 0s from scanner time.
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found
49663/tcp open  http          Microsoft IIS httpd 10.0
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
MAC Address: 02:39:D9:12:6F:EF (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): Microsoft Windows 10 (85%)
OS CPE: cpe:/o:microsoft:windows_10
Aggressive OS guesses: Microsoft Windows 10 build 14393 (85%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 0.025 days (since Thu Jul 25 10:03:39 2024)
Network Distance: 1 hop
TCP Sequence Prediction: Difficulty=262 (Good luck!)
IP ID Sequence Generation: Incremental
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| nbstat: NetBIOS name: RELEVANT, NetBIOS user: <unknown>, NetBIOS MAC: 02:39:d9:12:6f:ef (unknown)
| Names:
|   RELEVANT<00>         Flags: <unique><active>
|   WORKGROUP<00>        Flags: <group><active>
|_  RELEVANT<20>         Flags: <unique><active>
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: Relevant
|   NetBIOS computer name: RELEVANT\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2024-07-25T02:39:40-07:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-07-25 10:39:40
|_  start_date: 2024-07-25 10:05:10

TRACEROUTE
HOP RTT     ADDRESS
1   0.63 ms ip-10-10-42-22.eu-west-1.compute.internal (10.10.42.22)

NSE: Script Post-scanning.
Initiating NSE at 10:40
Completed NSE at 10:40, 0.00s elapsed
Initiating NSE at 10:40
Completed NSE at 10:40, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 763.16 seconds
           Raw packets sent: 197202 (8.682MB) | Rcvd: 570 (27.200KB)

```
## RECON

The computer is a Windows server 2016 standard version.  The services recognized have been 

- [[PORT 80]]: http server with IIS
- [[PORT 135]]: For RPC
- [[PORT 139]]: File sharing through NETBIOS
- [[PORT 445]]: File sharing through SMB
- [[PORT 3389]]: remote desktop protocol
- [[PORT 5985]]: another http server
- [[PORT 49663]]: another http server
- [[PORT 49667]]: 
- [[PORT 49669]]: 
