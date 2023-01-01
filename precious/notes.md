## Precious

First things first, let's ennumerate the services this server has public using nmap.

```{sh}
nmap -sV 10.10.11.189
 
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
```

We can see that the server is hosting a website using nginx 1.18.0. Now we will modify the /etc/hosts file to include the ip of this server into the DNS. After looking at the webpage it only seems to have a 
web to pdf converter. Now we will use gobuster and burp suite to test the website.

```{sh}
gobuster -m dir  -u http://precious.htb -w /home/oriol/Universitat/hackaton/SecLists/Discovery/Web-Content/directory-list-1.0.txt
/\ (Status: 200)
gobuster -m dir  -u http://precious.htb -w /home/oriol/Universitat/hackaton/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt  
gobuster -m dir  -u http://precious.htb -w /home/oriol/Universitat/hackaton/SecLists/Discovery/Web-Content/directory-list-1.0.txt -x php,html 
```


Many of the bruteforce analisys we are doing are yielding no results which may be due to the fact that 
they do not exist or are cleverly disguised.

A great thing about this server is that we can upload files from our computer, and specially, it does execute php inside the pages, now we need to give it a reverse shell and we will have access to it. 
Mental note for the future: always look for file uploads that can be executed lately, they are a great source of shells. A little problem occurs.

type of files that could be interesting .php, .sh,. Other possible exploits os command, or perhaphs 
modifying some of the values in the http packets.

It appears that php files are (which makes sense) executed before being sent to this server. I wonder
which file types it accepts:

Note: check the accepted file types 

> html: accepted 



Note: check if 
