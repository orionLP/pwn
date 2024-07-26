```bash
$ sudo nmap 10.10.238.137 -sS -sC -sV -p-

Starting Nmap 7.80 ( https://nmap.org ) at 2024-05-20 19:56 CEST
Nmap scan report for 10.10.238.137
Host is up (0.071s latency).
Not shown: 65533 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://site.empman.thm/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 104.87 seconds

```

We find:
- [[PORT 80]] with a web app
- [[PORT 22]] with ssh login