## SCANS

```bash
┌──(kali㉿kali)-[~]
└─$  nmap   10.129.244.229  -vv -Pn
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-26 14:19 EST
Initiating Parallel DNS resolution of 1 host. at 14:19
Completed Parallel DNS resolution of 1 host. at 14:20, 13.00s elapsed
Initiating Connect Scan at 14:20
Scanning 10.129.244.229 [1000 ports]
Discovered open port 22/tcp on 10.129.244.229
Discovered open port 80/tcp on 10.129.244.229
Completed Connect Scan at 14:20, 0.98s elapsed (1000 total ports)
Nmap scan report for 10.129.244.229
Host is up, received user-set (0.072s latency).
Scanned at 2024-11-26 14:20:04 EST for 1s
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE REASON
22/tcp open  ssh     syn-ack
80/tcp open  http    syn-ack

Read data files from: /usr/bin/../share/nmap
Nmap done: 1 IP address (1 host up) scanned in 14.00 seconds

```

```bash
┌──(kali㉿kali)-[~]
└─$  nmap -sV -sC -p -   10.129.244.229  -vv -Pn
Host discovery disabled (-Pn). All addresses will be marked 'up' and scan times may be slower.
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-26 14:20 EST
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:20
Completed NSE at 14:20, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:20
Completed NSE at 14:20, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:20
Completed NSE at 14:20, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 14:20
Completed Parallel DNS resolution of 1 host. at 14:20, 13.02s elapsed
Initiating Connect Scan at 14:20
Scanning 10.129.244.229 [65535 ports]
Discovered open port 80/tcp on 10.129.244.229
Discovered open port 22/tcp on 10.129.244.229
Increasing send delay for 10.129.244.229 from 0 to 5 due to max_successful_tryno increase to 4
Connect Scan Timing: About 51.37% done; ETC: 14:21 (0:00:30 remaining)
Connect Scan Timing: About 59.68% done; ETC: 14:22 (0:00:44 remaining)
Stats: 0:01:38 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 64.37% done; ETC: 14:22 (0:00:47 remaining)                                                                                                                                                             
Stats: 0:01:40 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan                                                                                                                                                        
Connect Scan Timing: About 65.08% done; ETC: 14:22 (0:00:47 remaining)                                                                                                                                                             
Stats: 0:01:42 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan                                                                                                                                                        
Connect Scan Timing: About 65.42% done; ETC: 14:22 (0:00:47 remaining)                                                                                                                                                             
Stats: 0:01:42 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan                                                                                                                                                        
Connect Scan Timing: About 65.57% done; ETC: 14:22 (0:00:47 remaining)                                                                                                                                                             
Connect Scan Timing: About 77.53% done; ETC: 14:23 (0:00:40 remaining)                                                                                                                                                             
Completed Connect Scan at 14:24, 239.44s elapsed (65535 total ports)
Initiating Service scan at 14:24
Scanning 2 services on 10.129.244.229
Completed Service scan at 14:24, 6.28s elapsed (2 services on 1 host)
NSE: Script scanning 10.129.244.229.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:24
Completed NSE at 14:24, 3.62s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:24
Completed NSE at 14:24, 0.81s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:24
Completed NSE at 14:24, 0.00s elapsed
Nmap scan report for 10.129.244.229
Host is up, received user-set (0.11s latency).
Scanned at 2024-11-26 14:20:37 EST for 250s
Not shown: 65514 closed tcp ports (conn-refused)
PORT      STATE    SERVICE     REASON      VERSION
22/tcp    open     ssh         syn-ack     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 7e:46:2c:46:6e:e6:d1:eb:2d:9d:34:25:e6:36:14:a7 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDSrBVJEKTgtUohrzoK9i67CgzqLAxnhEsPmW8hS5CFFGYikUduAcNkKsmmgQI09Q+6pa+7YHsnxcerBnW0taI//IYB5TI/LSE3yUxyk/ROkKLXPNiNGUhC6QiCj3ZTvThyHrFD9ZTxWfZKEQTcOiPs15+HRPCZepPouRtREGwmJcvDal1ix8p/2/C8X57ekouEEpIk1wzDTG5AM2/D08gXXe0TP+KYEaZEzAKM/mQUAqNTxfjc9x5rlfPYW+50kTDwtyKta57tBkkRCnnns0YRnPNtt0AH374ZkYLcqpzxwN8iTNXaeVT/dGfF4mA1uW89hSMarmiRgRh20Y1KIaInHjv9YcvSlbWz+2sz3ev725d4IExQTvDR4sfUAdysIX/q1iNpleyRgM4cvDMjxD6lEKpvQYSWVlRoJwbUUnJqnmZXboRwzRl+V3XCUaABJrA/1K1gvJfsPcU5LX303CV6LDwvLJIcgXlEbtjhkcxz7b7CS78BEW9hPifCUDGKfUs=
|   256 45:7b:20:95:ec:17:c5:b4:d8:86:50:81:e0:8c:e8:b8 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHYLF+puo27gFRX69GBeZJqCeHN3ps2BScsUhKoDV66yEPMOo/Sn588F/wqBnJxsPB3KSFH+kbYW2M6erFI3U5k=
|   256 cb:92:ad:6b:fc:c8:8e:5e:9f:8c:a2:69:1b:6d:d0:f7 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG/QUl3gapBOWCGEHplsOKe2NlWjlrb5vTTLjg6gMuGl
80/tcp    open     http        syn-ack     Apache httpd 2.4.41 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Did not follow redirect to http://alert.htb/
1478/tcp  filtered ms-sna-base no-response
1548/tcp  filtered axon-lm     no-response
2350/tcp  filtered psbserver   no-response
5817/tcp  filtered unknown     no-response
6488/tcp  filtered sun-sr-jmx  no-response
11290/tcp filtered unknown     no-response
12227/tcp filtered unknown     no-response
15812/tcp filtered unknown     no-response
17090/tcp filtered unknown     no-response
21991/tcp filtered unknown     no-response
24872/tcp filtered unknown     no-response
27103/tcp filtered unknown     no-response
28246/tcp filtered unknown     no-response
40092/tcp filtered unknown     no-response
49685/tcp filtered unknown     no-response
52597/tcp filtered unknown     no-response
56487/tcp filtered unknown     no-response
56743/tcp filtered unknown     no-response
57790/tcp filtered unknown     no-response
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 14:24
Completed NSE at 14:24, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 14:24
Completed NSE at 14:24, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 14:24
Completed NSE at 14:24, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 263.52 seconds
```

## SERVICES

- [[PORT 22]]: ssh server
- [[PORT 80]]: http server