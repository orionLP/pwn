
```bash 
$ nmap -sS -p- -T5 -sV -sC -vv 10.10.61.71

Starting Nmap 7.60 ( https://nmap.org ) at 2024-04-24 14:21 BST
NSE: Loaded 146 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 14:21
Completed NSE at 14:21, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 14:21
Completed NSE at 14:21, 0.00s elapsed
Initiating ARP Ping Scan at 14:21
Scanning 10.10.61.71 [1 port]
Completed ARP Ping Scan at 14:21, 0.22s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 14:21
Completed Parallel DNS resolution of 1 host. at 14:21, 0.00s elapsed
Initiating SYN Stealth Scan at 14:21
Scanning ip-10-10-61-71.eu-west-1.compute.internal (10.10.61.71) [65535 ports]
Discovered open port 22/tcp on 10.10.61.71
Discovered open port 80/tcp on 10.10.61.71
Warning: 10.10.61.71 giving up on port because retransmission cap hit (2).
SYN Stealth Scan Timing: About 25.06% done; ETC: 14:23 (0:01:33 remaining)
SYN Stealth Scan Timing: About 48.46% done; ETC: 14:23 (0:01:05 remaining)
SYN Stealth Scan Timing: About 72.26% done; ETC: 14:23 (0:00:35 remaining)
Completed SYN Stealth Scan at 14:24, 172.88s elapsed (65535 total ports)
Initiating Service scan at 14:24
Scanning 2 services on ip-10-10-61-71.eu-west-1.compute.internal (10.10.61.71)
Completed Service scan at 14:24, 6.18s elapsed (2 services on 1 host)
NSE: Script scanning 10.10.61.71.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 14:24
Completed NSE at 14:24, 0.18s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 14:24
Completed NSE at 14:24, 0.00s elapsed
Nmap scan report for ip-10-10-61-71.eu-west-1.compute.internal (10.10.61.71)
Host is up, received arp-response (0.00047s latency).
Scanned at 2024-04-24 14:21:39 BST for 180s
Not shown: 65533 closed ports
Reason: 65533 resets
PORT   STATE SERVICE REASON         VERSION
22/tcp open  ssh     syn-ack ttl 64 OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCpgV7/18RfM9BJUBOcZI/eIARrxAgEeD062pw9L24Ulo5LbBeuFIv7hfRWE/kWUWdqHf082nfWKImTAHVMCeJudQbKtL1SBJYwdNo6QCQyHkHXslVb9CV1Ck3wgcje8zLbrml7OYpwBlumLVo2StfonQUKjfsKHhR+idd3/P5V3abActQLU8zB0a4m3TbsrZ9Hhs/QIjgsEdPsQEjCzvPHhTQCEywIpd/GGDXqfNPB0Yl/dQghTALyvf71EtmaX/fsPYTiCGDQAOYy3RvOitHQCf4XVvqEsgzLnUbqISGugF8ajO5iiY2GiZUUWVn4MVV1jVhfQ0kC3ybNrQvaVcXd
|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDCxodQaK+2npyk3RZ1Z6S88i6lZp2kVWS6/f955mcgkYRrV1IMAVQ+jRd5sOKvoK8rflUPajKc9vY5Yhk2mPj8=
|   256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (EdDSA)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJhXt+ZEjzJRbb2rVnXOzdp5kDKb11LfddnkcyURkYke
80/tcp open  http    syn-ack ttl 64 Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
MAC Address: 02:45:92:AB:58:E7 (Unknown)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 14:24
Completed NSE at 14:24, 0.00s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 14:24
Completed NSE at 14:24, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 180.33 seconds
           Raw packets sent: 138629 (6.100MB) | Rcvd: 138629 (5.545MB)
```

We have discovered
- [[Port 80]]: Apache
- [[Port 22]]: SSH
- There seems to be a port which we have given up to due to not getting back answers
- The host has MAC address **02:45:92:AB:58:E7**
- Uses Linux, no info on kernel for now. Ubuntu.