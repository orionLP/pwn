## SCANS

The default nmap scan returns for the machine 

```bash
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.10.121
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-23 14:58 EST
Nmap scan report for 10.10.10.121
Host is up (0.31s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
3000/tcp open  ppp

Nmap done: 1 IP address (1 host up) scanned in 35.58 seconds
```

A little more insightful description

```bash
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.10.121 -sV -sC 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-23 15:42 EST
Nmap scan report for help.htb (10.10.10.121)
Host is up (0.19s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e5:bb:4d:9c:de:af:6b:bf:ba:8c:22:7a:d8:d7:43:28 (RSA)
|   256 d5:b0:10:50:74:86:a3:9f:c5:53:6f:3b:4a:24:61:19 (ECDSA)
|_  256 e2:1b:88:d3:76:21:d4:1e:38:15:4a:81:11:b7:99:07 (ED25519)
80/tcp   open  http    Apache httpd 2.4.18
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.18 (Ubuntu)
3000/tcp open  http    Node.js Express framework
|_http-title: Site doesn't have a title (application/json; charset=utf-8).
Service Info: Host: 127.0.1.1; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 37.20 seconds

```
## SERVICES

- [[PORT 22]]: ssh
- [[PORT 80]]: http server
- [[PORT 3000]]: http server in reality