The scripts done have outputed

```bash
(base) user@user-computer:$ sudo nmap -sS -sC -sV -p- 10.10.196.202

Starting Nmap 7.80 ( https://nmap.org ) at 2024-04-27 20:27 CEST
Nmap scan report for 10.10.196.202
Host is up (0.061s latency).
Not shown: 65531 closed ports
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Athena - Gods of olympus
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: 4s
|_nbstat: NetBIOS name: ROUTERPANEL, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2024-04-27T18:29:46
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 130.02 seconds

```

We have discovered the following from the first scan:
- The target uses **Ubuntu**
- In [[PORT 80]] there is a website with **Apache/2.4.41**. : Some results have turned out in exploitdb
- In [[PORT 22]] ssh is open version **OpenSSH 8.2.p1** : No entry in exploit db
- In [[PORT 139]] Samba is open with **smbd 4.6.2** : Entry for RCE in exploit db CVE-2017-7494*
- In [[PORT 445]] Samba is open with **smbd 4.6.2** (seems exactly the same as the other port)

