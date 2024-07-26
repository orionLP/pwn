## SCANS

```
┌──(root㉿kali)-[~]
└─# nmap 10.10.215.152 -sV -sC -O 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-30 05:38 EDT
Nmap scan report for 10.10.215.152
Host is up (0.028s latency).
Not shown: 995 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
7/tcp  open  echo
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9e:30:c5:61:92:84:1b:24:64:86:c3:3b:b7:dc:99:34 (RSA)
|   256 78:c3:c3:83:81:73:cb:f1:50:41:f1:9a:d7:bf:3e:d1 (ECDSA)
|_  256 ec:ce:b8:f9:57:53:56:63:e9:61:90:12:15:e5:78:4a (ED25519)
23/tcp open  telnet  Linux telnetd
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=6/30%OT=7%CT=1%CU=38083%PV=Y%DS=2%DC=I%G=Y%TM=66812
OS:79F%P=x86_64-pc-linux-gnu)SEQ(SP=0%GCD=FA00%ISR=9A%TI=I%CI=RD%II=I%SS=S%
OS:TS=U)SEQ(SP=11%GCD=FA00%ISR=9C%TI=I%CI=RD%II=I%SS=S%TS=U)OPS(O1=M5B4%O2=
OS:M5B4%O3=M5B4%O4=M5B4%O5=M5B4%O6=M5B4)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF
OS:%W5=FFFF%W6=FFFF)ECN(R=Y%DF=N%T=41%W=FFFF%O=M5B4%CC=N%Q=)T1(R=Y%DF=N%T=4
OS:1%S=O%A=S+%F=AS%RD=0%Q=)T2(R=Y%DF=N%T=100%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3
OS:(R=Y%DF=N%T=100%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T4(R=Y%DF=N%T=100%W=0%S=A%A
OS:=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=N%T=100%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%
OS:DF=N%T=100%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=N%T=100%W=0%S=Z%A=S%F=AR
OS:%O=%RD=0%Q=)U1(R=Y%DF=N%T=34%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RU
OS:D=G)U1(R=Y%DF=N%T=36%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)U1(R
OS:=Y%DF=N%T=39%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)U1(R=Y%DF=N%
OS:T=3B%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)U1(R=Y%DF=N%T=40%IPL
OS:=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=S%T=25%CD=S)IE(R=
OS:Y%DFI=S%T=26%CD=S)IE(R=Y%DFI=S%T=29%CD=S)IE(R=Y%DFI=S%T=37%CD=S)IE(R=Y%D
OS:FI=S%T=3A%CD=S)

Network Distance: 2 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 39.51 seconds
```

```bash
┌──(root㉿kali)-[~]
└─# nmap 10.10.215.152 -sV -sC -sS -p - -v 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-30 05:39 EDT
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 05:39
Completed NSE at 05:39, 0.00s elapsed
Initiating NSE at 05:39
Completed NSE at 05:39, 0.00s elapsed
Initiating NSE at 05:39
Completed NSE at 05:39, 0.00s elapsed
Initiating Ping Scan at 05:39
Scanning 10.10.215.152 [4 ports]
Completed Ping Scan at 05:39, 0.01s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 05:39
Completed Parallel DNS resolution of 1 host. at 05:39, 13.00s elapsed
Initiating SYN Stealth Scan at 05:39
Scanning 10.10.215.152 [65535 ports]
Discovered open port 21/tcp on 10.10.215.152
Discovered open port 23/tcp on 10.10.215.152
Discovered open port 80/tcp on 10.10.215.152
Discovered open port 22/tcp on 10.10.215.152
SYN Stealth Scan Timing: About 29.87% done; ETC: 05:41 (0:01:13 remaining)
SYN Stealth Scan Timing: About 54.85% done; ETC: 05:41 (0:00:50 remaining)
Discovered open port 61337/tcp on 10.10.215.152
Discovered open port 7/tcp on 10.10.215.152
Completed SYN Stealth Scan at 05:41, 100.64s elapsed (65535 total ports)
Initiating Service scan at 05:41
Scanning 6 services on 10.10.215.152
Completed Service scan at 05:41, 6.25s elapsed (6 services on 1 host)
NSE: Script scanning 10.10.215.152.
Initiating NSE at 05:41
Completed NSE at 05:41, 7.76s elapsed
Initiating NSE at 05:41
Completed NSE at 05:41, 0.49s elapsed
Initiating NSE at 05:41
Completed NSE at 05:41, 0.00s elapsed
Nmap scan report for 10.10.215.152
Host is up (0.075s latency).
Not shown: 65529 closed tcp ports (reset)
PORT      STATE SERVICE VERSION
7/tcp     open  echo
21/tcp    open  ftp     vsftpd 3.0.3
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 9e:30:c5:61:92:84:1b:24:64:86:c3:3b:b7:dc:99:34 (RSA)
|   256 78:c3:c3:83:81:73:cb:f1:50:41:f1:9a:d7:bf:3e:d1 (ECDSA)
|_  256 ec:ce:b8:f9:57:53:56:63:e9:61:90:12:15:e5:78:4a (ED25519)
23/tcp    open  telnet  Linux telnetd
80/tcp    open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: POST OPTIONS HEAD GET
|_http-server-header: Apache/2.4.29 (Ubuntu)
61337/tcp open  http    Werkzeug httpd 2.0.1 (Python 3.6.9)
|_http-server-header: Werkzeug/2.0.1 Python/3.6.9
| http-title: Site doesn't have a title (text/html; charset=utf-8).
|_Requested resource was http://10.10.215.152:61337/login
| http-methods: 
|_  Supported Methods: HEAD OPTIONS GET
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 05:41
Completed NSE at 05:41, 0.00s elapsed
Initiating NSE at 05:41
Completed NSE at 05:41, 0.00s elapsed
Initiating NSE at 05:41
Completed NSE at 05:41, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 128.44 seconds
           Raw packets sent: 67336 (2.963MB) | Rcvd: 67333 (2.693MB)

```

## DISCOVERED SERVICES

- [[PORT 7]]: echo service (basically sends back whatever you have sent).
- [[PORT 21]]: ftp service
- [[PORT 22]]: SSH service
- [[PORT 23]]: telnet service
- [[PORT 80]]: http server
- [[PORT 61337]]: http server -> login page

## KNOWN VULNS
- port 21: no
- port 22: no
- port 23: no
- port 80: found some interesting things in exploit db, if no other options are available, it might be worth checking out.
- port 61337: metasploit seems to have an exploit for Werkzeug, but works for werkzeug 0.10 and older

At least so far this does not seem the way to go