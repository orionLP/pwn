
## SCANS

```bash
┌──(root㉿kali)-[~]
└─# nmap -p 1-5000 -oN ./scan1.out -sV -sC -O -Pn 10.10.91.177 -sS -v 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-29 04:25 EDT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 04:25
Completed NSE at 04:25, 0.00s elapsed
Initiating NSE at 04:25
Completed NSE at 04:25, 0.00s elapsed
Initiating NSE at 04:25
Completed NSE at 04:25, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 04:25
Completed Parallel DNS resolution of 1 host. at 04:26, 13.00s elapsed
Initiating SYN Stealth Scan at 04:26
Scanning 10.10.91.177 [5000 ports]
Discovered open port 80/tcp on 10.10.91.177
Discovered open port 3389/tcp on 10.10.91.177
SYN Stealth Scan Timing: About 31.30% done; ETC: 04:27 (0:01:08 remaining)
Increasing send delay for 10.10.91.177 from 0 to 5 due to 11 out of 16 dropped probes since last increase.
Increasing send delay for 10.10.91.177 from 5 to 10 due to 11 out of 11 dropped probes since last increase.
SYN Stealth Scan Timing: About 33.85% done; ETC: 04:29 (0:01:59 remaining)
Increasing send delay for 10.10.91.177 from 10 to 20 due to 11 out of 11 dropped probes since last increase.
Increasing send delay for 10.10.91.177 from 20 to 40 due to 11 out of 11 dropped probes since last increase.
SYN Stealth Scan Timing: About 37.49% done; ETC: 04:30 (0:02:32 remaining)
SYN Stealth Scan Timing: About 57.52% done; ETC: 04:31 (0:02:16 remaining)
SYN Stealth Scan Timing: About 64.24% done; ETC: 04:31 (0:01:59 remaining)
SYN Stealth Scan Timing: About 70.99% done; ETC: 04:31 (0:01:40 remaining)
SYN Stealth Scan Timing: About 77.77% done; ETC: 04:31 (0:01:18 remaining)
SYN Stealth Scan Timing: About 84.73% done; ETC: 04:32 (0:00:55 remaining)
SYN Stealth Scan Timing: About 91.69% done; ETC: 04:32 (0:00:30 remaining)
Completed SYN Stealth Scan at 04:32, 369.61s elapsed (5000 total ports)
Initiating Service scan at 04:32
Scanning 2 services on 10.10.91.177
Completed Service scan at 04:32, 6.15s elapsed (2 services on 1 host)
Initiating OS detection (try #1) against 10.10.91.177
adjust_timeouts2: packet supposedly had rtt of -755334 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -755334 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -755357 microseconds.  Ignoring time.
adjust_timeouts2: packet supposedly had rtt of -755357 microseconds.  Ignoring time.
Retrying OS detection (try #2) against 10.10.91.177
NSE: Script scanning 10.10.91.177.
Initiating NSE at 04:32
Completed NSE at 04:32, 5.07s elapsed
Initiating NSE at 04:32
Completed NSE at 04:32, 0.31s elapsed
Initiating NSE at 04:32
Completed NSE at 04:32, 0.00s elapsed
Nmap scan report for 10.10.91.177
Host is up (0.041s latency).
Not shown: 4998 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: 403 - Forbidden: Access is denied.
| http-methods: 
|   Supported Methods: OPTIONS TRACE GET HEAD POST
|_  Potentially risky methods: TRACE
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2024-06-29T08:32:42+00:00; +10s from scanner time.
| ssl-cert: Subject: commonName=EXFILIBUR
| Issuer: commonName=EXFILIBUR
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2024-06-28T07:52:11
| Not valid after:  2024-12-28T07:52:11
| MD5:   bf5e:8173:1ddf:e917:f4a4:ac63:7768:53e8
|_SHA-1: 06fd:53b3:b1a5:eca2:8fd1:ab1f:ac20:43d9:6a9f:1d80
| rdp-ntlm-info: 
|   Target_Name: EXFILIBUR
|   NetBIOS_Domain_Name: EXFILIBUR
|   NetBIOS_Computer_Name: EXFILIBUR
|   DNS_Domain_Name: EXFILIBUR
|   DNS_Computer_Name: EXFILIBUR
|   Product_Version: 10.0.17763
|_  System_Time: 2024-06-29T08:32:37+00:00
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: bridge|general purpose
Running (JUST GUESSING): Oracle Virtualbox (97%), QEMU (95%)
OS CPE: cpe:/o:oracle:virtualbox cpe:/a:qemu:qemu
Aggressive OS guesses: Oracle Virtualbox (97%), QEMU user mode network gateway (95%)
No exact OS matches for host (test conditions non-ideal).
TCP Sequence Prediction: Difficulty=17 (Good luck!)
IP ID Sequence Generation: Busy server or unknown class
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 9s, deviation: 0s, median: 9s

NSE: Script Post-scanning.
Initiating NSE at 04:32
Completed NSE at 04:32, 0.00s elapsed
Initiating NSE at 04:32
Completed NSE at 04:32, 0.00s elapsed
Initiating NSE at 04:32
Completed NSE at 04:32, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 398.25 seconds
           Raw packets sent: 10335 (459.572KB) | Rcvd: 386789 (56.312MB)

```

Also tried the same scans up to port 15000, but did not bear any resutls
## INFORMATION EXTRACTED 

- [[PORT 80]]
- [[PORT 3389]]
