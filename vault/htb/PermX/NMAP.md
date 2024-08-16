# SCANS

```bash
┌──(root㉿kali)-[~]
└─# nmap -sS -sV -sC -p - 10.10.11.23
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-13 14:30 EDT
Nmap scan report for 10.10.11.23
Host is up (0.10s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 e2:5c:5d:8c:47:3e:d8:72:f7:b4:80:03:49:86:6d:ef (ECDSA)
|_  256 1f:41:02:8e:6b:17:18:9c:a0:ac:54:23:e9:71:30:17 (ED25519)
80/tcp open  http    Apache httpd 2.4.52
|_http-title: Did not follow redirect to http://permx.htb
|_http-server-header: Apache/2.4.52 (Ubuntu)
Service Info: Host: 127.0.0.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 39.38 seconds              
```
# DISCOVERED SERVICES
- [[PORT 22]]: SSH server
- [[PORT 80]]: HTTP server