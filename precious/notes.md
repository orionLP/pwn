## Precious

First things first, let's ennumerate the services this server has public using nmap.

>> nmap -sV 10.10.11.189
 
Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-01 10:41 CET
Nmap scan report for 10.10.11.189
Host is up (0.081s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
80/tcp open  http    nginx 1.18.0
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.87 seconds

We can see that the server is hosting a website using nginx 1.18.0. Now we will modify the /etc/hosts file to include the ip of this server into the DNS. After looking at the webpage it only seems to have a 
web to pdf converter. Now we will use gobuster and burp suite to test the website.

```{sh}
gobuster -m dir  -u http://precious.htb -w /home/oriol/Universitat/hackaton/SecLists/Discovery/Web-Content/directory-list-1.0.txt
/\ (Status: 200)
```
