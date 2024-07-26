### **SCANS**

```bash
$ sudo nmap -sS -p- -v 10.10.149.74

[sudo] password for oriol: 
Starting Nmap 7.80 ( https://nmap.org ) at 2024-05-07 16:31 CEST
Initiating Ping Scan at 16:31
Scanning 10.10.149.74 [4 ports]
Completed Ping Scan at 16:31, 0.10s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 16:31
Completed Parallel DNS resolution of 1 host. at 16:32, 13.00s elapsed
Initiating SYN Stealth Scan at 16:32
Scanning 10.10.149.74 [65535 ports]
Discovered open port 139/tcp on 10.10.149.74
Discovered open port 443/tcp on 10.10.149.74
Discovered open port 445/tcp on 10.10.149.74
Discovered open port 21/tcp on 10.10.149.74
Discovered open port 22/tcp on 10.10.149.74
Discovered open port 80/tcp on 10.10.149.74
SYN Stealth Scan Timing: About 15.97% done; ETC: 16:35 (0:02:43 remaining)
SYN Stealth Scan Timing: About 34.83% done; ETC: 16:34 (0:01:54 remaining)
SYN Stealth Scan Timing: About 55.23% done; ETC: 16:34 (0:01:14 remaining)
SYN Stealth Scan Timing: About 77.20% done; ETC: 16:34 (0:00:36 remaining)
Completed SYN Stealth Scan at 16:34, 154.76s elapsed (65535 total ports)
Nmap scan report for 10.10.149.74
Host is up (0.054s latency).
Not shown: 65529 filtered ports
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
139/tcp open  netbios-ssn
443/tcp open  https
445/tcp open  microsoft-ds

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 167.99 seconds
           Raw packets sent: 131004 (5.764MB) | Rcvd: 167 (11.812KB)

```

```bash 

$ sudo nmap -sS -p- -sV -sC -v 10.10.149.74
Starting Nmap 7.80 ( https://nmap.org ) at 2024-05-07 16:39 CEST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 16:39
Completed NSE at 16:39, 0.00s elapsed
Initiating NSE at 16:39
Completed NSE at 16:39, 0.00s elapsed
Initiating NSE at 16:39
Completed NSE at 16:39, 0.00s elapsed
Initiating Ping Scan at 16:39
Scanning 10.10.149.74 [4 ports]
Completed Ping Scan at 16:39, 0.07s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 16:39
Completed Parallel DNS resolution of 1 host. at 16:39, 13.00s elapsed
Initiating SYN Stealth Scan at 16:39
Scanning 10.10.149.74 [65535 ports]
Discovered open port 21/tcp on 10.10.149.74
Discovered open port 22/tcp on 10.10.149.74
Discovered open port 445/tcp on 10.10.149.74
Discovered open port 139/tcp on 10.10.149.74
Discovered open port 443/tcp on 10.10.149.74
Discovered open port 80/tcp on 10.10.149.74
Stats: 0:00:14 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 0.03% done
SYN Stealth Scan Timing: About 14.67% done; ETC: 16:42 (0:03:00 remaining)
SYN Stealth Scan Timing: About 34.77% done; ETC: 16:42 (0:01:54 remaining)
SYN Stealth Scan Timing: About 56.08% done; ETC: 16:42 (0:01:11 remaining)
SYN Stealth Scan Timing: About 79.72% done; ETC: 16:41 (0:00:31 remaining)
Completed SYN Stealth Scan at 16:41, 144.58s elapsed (65535 total ports)
Initiating Service scan at 16:41
Scanning 6 services on 10.10.149.74
Completed Service scan at 16:41, 12.35s elapsed (6 services on 1 host)
NSE: Script scanning 10.10.149.74.
Initiating NSE at 16:41
NSE: [ftp-bounce] PORT response: 500 Illegal PORT command.
Completed NSE at 16:42, 7.16s elapsed
Initiating NSE at 16:42
Completed NSE at 16:42, 0.46s elapsed
Initiating NSE at 16:42
Completed NSE at 16:42, 0.00s elapsed
Nmap scan report for 10.10.149.74
Host is up (0.050s latency).
Not shown: 65529 filtered ports
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.2
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxr-xr-x    2 0        0               6 Jun 09  2021 pub
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.11.73.42
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.2 - secure, fast, stable
|_End of status
22/tcp  open  ssh         OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 09:23:62:a2:18:62:83:69:04:40:62:32:97:ff:3c:cd (RSA)
|   256 33:66:35:36:b0:68:06:32:c1:8a:f6:01:bc:43:38:ce (ECDSA)
|_  256 14:98:e3:84:70:55:e6:60:0c:c2:09:77:f8:b7:a6:1c (ED25519)
80/tcp  open  http        Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips)
| http-methods: 
|   Supported Methods: GET HEAD POST OPTIONS TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips
|_http-title: Apache HTTP Server Test Page powered by CentOS
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
443/tcp open  ssl/http    Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips)
| http-methods: 
|   Supported Methods: GET HEAD POST OPTIONS TRACE
|_  Potentially risky methods: TRACE
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips
|_http-title: Apache HTTP Server Test Page powered by CentOS
| ssl-cert: Subject: commonName=aratus/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Issuer: commonName=aratus/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2021-11-23T12:28:26
| Not valid after:  2022-11-23T12:28:26
| MD5:   56cc c593 6bdc 9168 bc7d a4b7 7d3f 004e
|_SHA-1: 7678 b819 d2c6 5dc9 515e 09eb 1e18 d772 aec7 a686
|_ssl-date: TLS randomness does not represent time
445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
Service Info: Host: ARATUS; OS: Unix

Host script results:
|_clock-skew: mean: 6s, deviation: 0s, median: 5s
|_ms-sql-info: ERROR: Script execution failed (use -d to debug)
|_smb-os-discovery: ERROR: Script execution failed (use -d to debug)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-05-07T14:42:04
|_  start_date: N/A

NSE: Script Post-scanning.
Initiating NSE at 16:42
Completed NSE at 16:42, 0.00s elapsed
Initiating NSE at 16:42
Completed NSE at 16:42, 0.00s elapsed
Initiating NSE at 16:42
Completed NSE at 16:42, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 178.16 seconds
           Raw packets sent: 130988 (5.763MB) | Rcvd: 209 (21.227KB)

```
### DISCOVERED SERVICES

- http on [[PORT 80]]
- ssh on [[PORT 22]]
- ftp on [[PORT 21]]
- samba on [[PORT 139]]
- https on [[PORT 443]]
- samba [[PORT 445]]
