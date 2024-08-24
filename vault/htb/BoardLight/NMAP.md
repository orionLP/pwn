### SCANS

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2024-08-22 11:22 CEST
Nmap scan report for 10.10.11.11
Host is up (0.12s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.76 seconds
```

### SERVICES DISCOVERED

- [[PORT 22]]: ssh service
- [[PORT 80]]: http service