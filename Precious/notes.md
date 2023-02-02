After a quick scan we find open the ports 22,80, and so we run a more through scan

```{sh}
sudo nmap -p22,80 -sC -sV 10.129.202.153

Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-02 14:42 CET
Nmap scan report for 10.129.202.153
Host is up (0.063s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
80/tcp open  http    nginx 1.18.0
|_http-server-header: nginx/1.18.0
|_http-title: Did not follow redirect to http://precious.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.28 seconds

```