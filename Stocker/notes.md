# STOCKER

The first thing to do is a quick scan to see what services this server has:

```{sh}
nmap -p- -sV -sC 10.129.80.89
Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-11 16:08 CET
Nmap scan report for stocker.htb (10.129.80.89)
Host is up (0.045s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-generator: Eleventy v2.0.0
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Stock - Coming Soon!
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 60.04 seconds
```

## Web page 

> Head IT: Angoose Garden
> Web page developer: Holger Koenemann
