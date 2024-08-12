```bash
┌──(root㉿kali)-[/usr/share/seclists/Fuzzing/Databases]
└─# nmap -p - -sT  -sV -sC 10.10.11.18  -v
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-07 08:50 EDT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 08:50
Completed NSE at 08:50, 0.00s elapsed
Initiating NSE at 08:50
Completed NSE at 08:50, 0.00s elapsed
Initiating NSE at 08:50
Completed NSE at 08:50, 0.00s elapsed
Initiating Ping Scan at 08:50
Scanning 10.10.11.18 [4 ports]
Completed Ping Scan at 08:50, 0.01s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 08:50
Completed Parallel DNS resolution of 1 host. at 08:50, 13.00s elapsed
Initiating Connect Scan at 08:50
Scanning 10.10.11.18 [65535 ports]
Discovered open port 22/tcp on 10.10.11.18
Discovered open port 80/tcp on 10.10.11.18
Increasing send delay for 10.10.11.18 from 0 to 5 due to max_successful_tryno increase to 4
Increasing send delay for 10.10.11.18 from 5 to 10 due to max_successful_tryno increase to 5
Increasing send delay for 10.10.11.18 from 10 to 20 due to 11 out of 12 dropped probes since last increase.
Increasing send delay for 10.10.11.18 from 20 to 40 due to max_successful_tryno increase to 6
Increasing send delay for 10.10.11.18 from 40 to 80 due to 11 out of 18 dropped probes since last increase.
Increasing send delay for 10.10.11.18 from 80 to 160 due to max_successful_tryno increase to 7
Increasing send delay for 10.10.11.18 from 160 to 320 due to 11 out of 26 dropped probes since last increase.
Connect Scan Timing: About 0.46% done
```

```bash
┌──(root㉿kali)-[/usr/share/seclists/Fuzzing/Databases]
└─# nmap -p - -sS -Pn  -sV -sC 10.10.11.18  -v
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-07 08:57 EDT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 08:57
Completed NSE at 08:57, 0.00s elapsed
Initiating NSE at 08:57
Completed NSE at 08:57, 0.00s elapsed
Initiating NSE at 08:57
Completed NSE at 08:57, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 08:57
Completed Parallel DNS resolution of 1 host. at 08:57, 13.00s elapsed
Initiating SYN Stealth Scan at 08:57
Scanning 10.10.11.18 [65535 ports]
Discovered open port 22/tcp on 10.10.11.18
Discovered open port 80/tcp on 10.10.11.18
Completed SYN Stealth Scan at 08:58, 24.66s elapsed (65535 total ports)
Initiating Service scan at 08:58
Scanning 2 services on 10.10.11.18
Completed Service scan at 08:58, 6.21s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.11.18.
Initiating NSE at 08:58
Completed NSE at 08:58, 2.78s elapsed
Initiating NSE at 08:58
Completed NSE at 08:58, 0.57s elapsed
Initiating NSE at 08:58
Completed NSE at 08:58, 0.00s elapsed
Nmap scan report for 10.10.11.18
Host is up (0.16s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 a0:f8:fd:d3:04:b8:07:a0:63:dd:37:df:d7:ee:ca:78 (ECDSA)
|_  256 bd:22:f5:28:77:27:fb:65:ba:f6:fd:2f:10:c7:82:8f (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Did not follow redirect to http://usage.htb/
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 08:58
Completed NSE at 08:58, 0.00s elapsed
Initiating NSE at 08:58
Completed NSE at 08:58, 0.00s elapsed
Initiating NSE at 08:58
Completed NSE at 08:58, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.52 seconds
           Raw packets sent: 65619 (2.887MB) | Rcvd: 65624 (2.625MB)
```

## DISCOVERED

- [[PORT 22]]: ssh service
- [[PORT 80]]: http service