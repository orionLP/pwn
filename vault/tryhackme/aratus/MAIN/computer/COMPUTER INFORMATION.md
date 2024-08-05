
### GENERIC INFORMATION

#### USERS

---

- simeon
- theodore
- automation

```bash
[simeon@aratus home]$ ls -la
total 4
drwxr-xr-x.  5 root       root         54 Nov 23  2021 .
dr-xr-xr-x. 17 root       root        224 Mar 25  2022 ..
drwx------.  4 automation automation  127 Dec  2  2021 automation
drwxr-xr-x. 12 simeon     simeon     4096 Jan 10  2022 simeon
drwx------.  5 theodore   theodore    158 Mar 25  2022 theodore
```

```bash
[simeon@aratus home]$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
theodore:x:1001:1001::/home/theodore:/bin/bash
automation:x:1002:1002::/home/automation:/bin/bash
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
simeon:x:1003:1003::/home/simeon:/bin/bash
tcpdump:x:72:72::/:/sbin/nologin
saslauth:x:998:76:Saslauthd user:/run/saslauthd:/sbin/nologin
apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin
```

```bash
[simeon@aratus home]$ cat /etc/group
root:x:0:
bin:x:1:
daemon:x:2:
sys:x:3:
adm:x:4:
tty:x:5:
disk:x:6:
lp:x:7:
mem:x:8:
kmem:x:9:
wheel:x:10:
cdrom:x:11:
mail:x:12:postfix
man:x:15:
dialout:x:18:
floppy:x:19:
games:x:20:
tape:x:33:
video:x:39:
ftp:x:50:
lock:x:54:
audio:x:63:
nobody:x:99:
users:x:100:
utmp:x:22:
utempter:x:35:
input:x:999:
systemd-journal:x:190:
systemd-network:x:192:
dbus:x:81:
polkitd:x:998:
ssh_keys:x:997:
sshd:x:74:
postdrop:x:90:
postfix:x:89:
theodore:x:1001:
automation:x:1002:
printadmin:x:996:
tss:x:59:
simeon:x:1003:
tcpdump:x:72:
saslauth:x:76:
apache:x:48:
```

```bash
[simeon@aratus home]$ ls -la /etc/shadow
----------. 1 root root 1029 Jan 10  2022 /etc/shadow
```

```bash
[simeon@aratus home]$ ls -la /etc/gshadow
----------. 1 root root 443 Nov 23  2021 /etc/gshadow
```

#### SIMEON

---

```
[simeon@aratus home]$ sudo -l

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

[sudo] password for simeon: 
Sorry, user simeon may not run sudo on aratus.
```

Specially the number 2 is rather suspicious

```bash
$ history 

# nothing of interest
```

```bash
[simeon@aratus home]$ id
uid=1003(simeon) gid=1003(simeon) groups=1003(simeon) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
```
It seems that selinux is installed, but it does not appear that i have any restrictions imposed on me

```bash
[simeon@aratus home]$ env
LC_PAPER=en_US.UTF-8
XDG_SESSION_ID=43
LC_ADDRESS=en_US.UTF-8
HOSTNAME=aratus
LC_MONETARY=en_US.UTF-8
SELINUX_ROLE_REQUESTED=
TERM=xterm-256color
SHELL=/bin/bash
HISTSIZE=1000
SSH_CLIENT=10.11.73.42 53716 22
SELINUX_USE_CURRENT_RANGE=
LC_NUMERIC=en_US.UTF-8
SSH_TTY=/dev/pts/0
USER=simeon
LS_COLORS=rs=0:di=38;5;27:ln=38;5;51:mh=44;38;5;15:pi=40;38;5;11:so=38;5;13:do=38;5;5:bd=48;5;232;38;5;11:cd=48;5;232;38;5;3:or=48;5;232;38;5;9:mi=05;48;5;232;38;5;15:su=48;5;196;38;5;15:sg=48;5;11;38;5;16:ca=48;5;196;38;5;226:tw=48;5;10;38;5;16:ow=48;5;10;38;5;21:st=48;5;21;38;5;15:ex=38;5;34:*.tar=38;5;9:*.tgz=38;5;9:*.arc=38;5;9:*.arj=38;5;9:*.taz=38;5;9:*.lha=38;5;9:*.lz4=38;5;9:*.lzh=38;5;9:*.lzma=38;5;9:*.tlz=38;5;9:*.txz=38;5;9:*.tzo=38;5;9:*.t7z=38;5;9:*.zip=38;5;9:*.z=38;5;9:*.Z=38;5;9:*.dz=38;5;9:*.gz=38;5;9:*.lrz=38;5;9:*.lz=38;5;9:*.lzo=38;5;9:*.xz=38;5;9:*.bz2=38;5;9:*.bz=38;5;9:*.tbz=38;5;9:*.tbz2=38;5;9:*.tz=38;5;9:*.deb=38;5;9:*.rpm=38;5;9:*.jar=38;5;9:*.war=38;5;9:*.ear=38;5;9:*.sar=38;5;9:*.rar=38;5;9:*.alz=38;5;9:*.ace=38;5;9:*.zoo=38;5;9:*.cpio=38;5;9:*.7z=38;5;9:*.rz=38;5;9:*.cab=38;5;9:*.jpg=38;5;13:*.jpeg=38;5;13:*.gif=38;5;13:*.bmp=38;5;13:*.pbm=38;5;13:*.pgm=38;5;13:*.ppm=38;5;13:*.tga=38;5;13:*.xbm=38;5;13:*.xpm=38;5;13:*.tif=38;5;13:*.tiff=38;5;13:*.png=38;5;13:*.svg=38;5;13:*.svgz=38;5;13:*.mng=38;5;13:*.pcx=38;5;13:*.mov=38;5;13:*.mpg=38;5;13:*.mpeg=38;5;13:*.m2v=38;5;13:*.mkv=38;5;13:*.webm=38;5;13:*.ogm=38;5;13:*.mp4=38;5;13:*.m4v=38;5;13:*.mp4v=38;5;13:*.vob=38;5;13:*.qt=38;5;13:*.nuv=38;5;13:*.wmv=38;5;13:*.asf=38;5;13:*.rm=38;5;13:*.rmvb=38;5;13:*.flc=38;5;13:*.avi=38;5;13:*.fli=38;5;13:*.flv=38;5;13:*.gl=38;5;13:*.dl=38;5;13:*.xcf=38;5;13:*.xwd=38;5;13:*.yuv=38;5;13:*.cgm=38;5;13:*.emf=38;5;13:*.axv=38;5;13:*.anx=38;5;13:*.ogv=38;5;13:*.ogx=38;5;13:*.aac=38;5;45:*.au=38;5;45:*.flac=38;5;45:*.mid=38;5;45:*.midi=38;5;45:*.mka=38;5;45:*.mp3=38;5;45:*.mpc=38;5;45:*.ogg=38;5;45:*.ra=38;5;45:*.wav=38;5;45:*.axa=38;5;45:*.oga=38;5;45:*.spx=38;5;45:*.xspf=38;5;45:
LC_TELEPHONE=en_US.UTF-8
MAIL=/var/spool/mail/simeon
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/simeon/.local/bin:/home/simeon/bin
LC_IDENTIFICATION=en_US.UTF-8
PWD=/home
LANG=en_GB.UTF-8
LC_MEASUREMENT=en_US.UTF-8
SELINUX_LEVEL_REQUESTED=
HISTCONTROL=ignoredups
SHLVL=1
HOME=/home/simeon
LOGNAME=simeon
SSH_CONNECTION=10.11.73.42 53716 10.10.161.63 22
LESSOPEN=||/usr/bin/lesspipe.sh %s
XDG_RUNTIME_DIR=/run/user/1003
LC_TIME=en_US.UTF-8
LC_NAME=en_US.UTF-8
_=/usr/bin/env
OLDPWD=/home/simeon
```

**Mail for simeon is empty**

```bash
[simeon@aratus /]$ find / -type f -writable 2>/dev/null

# no files of interest to write to 
```

#### FILESYSTEM

---

Since there was  a reference in message-to-simeon

```bash
[simeon@aratus home]$ ls -la /opt/
total 0
drwxr-xr-x.  4 root       root      36 Nov 22  2021 .
dr-xr-xr-x. 17 root       root     224 Mar 25  2022 ..
drwxr-x---.  4 automation theodore  90 Nov 23  2021 ansible
drwxr-x---.  2 automation theodore  30 Nov 23  2021 scripts
```

```bash
[simeon@aratus home]$ ls -la /var/spool/mail
total 12
drwxrwxr-x. 2 root       mail   66 Mar 25  2022 .
drwxr-xr-x. 9 root       root  100 Nov 23  2021 ..
-rw-rw----. 1 automation mail    0 Nov 22  2021 automation
-rw-------. 1 root       mail 4391 Mar 25  2022 root
-rw-rw----. 1 simeon     mail    0 Nov 23  2021 simeon
-rw-rw----. 1 theodore   mail    1 Nov 23  2021 theodore
```
**Root & theodore have mail**

```bash
[simeon@aratus /]$ find / -type f -user theodore 2>/dev/null
/var/spool/mail/theodore
/home/simeon/message-to-simeon.txt
```

```bash
[simeon@aratus /]$ find / -type f -group theodore 2>/dev/null
```

```bash
[simeon@aratus /]$ find / -user theodore 2>/dev/null
/var/spool/mail/theodore
/home/theodore
/home/simeon/message-to-simeon.txt
```

```bash
[simeon@aratus /]$ find / -group theodore 2>/dev/null
/home/theodore
/opt/ansible
/opt/scripts
```

```bash
[simeon@aratus /]$ find / -user automation 2>/dev/null
/var/spool/mail/automation
/home/automation
/opt/ansible
/opt/scripts
```

```bash
[simeon@aratus /]$ find / -group  automation 2>/dev/null
/home/automation
```

```bash
[simeon@aratus /]$ find / -user simeon 2>/dev/null

# did not find much of use
```

```bash
[simeon@aratus /]$ find / -group simeon 2>/dev/null

# did not find much of use
```
#### SELINUX

```bash
[simeon@aratus ~]$ sestatus
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   permissive
Mode from config file:          permissive
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Max kernel policy version:      31
```

Seems no restrictions are placed upon us that i am aware of 
### POST SERVICE RECONASSANCE

---

### TESTED

#### **NOT DONE YET**
- kernel

#### **DONE**

##### SUID/SGUID

---

```bash
[simeon@aratus /]$ find / -perm /u=s -exec ls -la {} + 2>/dev/null
-rwsr-xr-x. 1 root root  73888 Aug  9  2019 /usr/bin/chage
-rws--x--x. 1 root root  23968 Feb  2  2021 /usr/bin/chfn
-rws--x--x. 1 root root  23880 Feb  2  2021 /usr/bin/chsh
-rwsr-xr-x. 1 root root  57576 Jan 13  2022 /usr/bin/crontab
-rwsr-xr-x. 1 root root  78408 Aug  9  2019 /usr/bin/gpasswd
-rwsr-xr-x. 1 root root  44264 Feb  2  2021 /usr/bin/mount
-rwsr-xr-x. 1 root root  41936 Aug  9  2019 /usr/bin/newgrp
-rwsr-xr-x. 1 root root  27856 Apr  1  2020 /usr/bin/passwd
-rwsr-xr-x. 1 root root  27672 Jan 25  2022 /usr/bin/pkexec
-rwsr-xr-x. 1 root root  32128 Feb  2  2021 /usr/bin/su
---s--x--x. 1 root root 151424 Oct 14  2021 /usr/bin/sudo
-rwsr-xr-x. 1 root root  31984 Feb  2  2021 /usr/bin/umount
-rwsr-x---. 1 root dbus  57936 Sep 30  2020 /usr/libexec/dbus-1/dbus-daemon-launch-helper
-rwsr-xr-x. 1 root root  15432 Jan 25  2022 /usr/lib/polkit-1/polkit-agent-helper-1
-rwsr-xr-x. 1 root root  11232 Apr  1  2020 /usr/sbin/pam_timestamp_check
-rwsr-xr-x. 1 root root  36272 Apr  1  2020 /usr/sbin/unix_chkpwd
-rwsr-xr-x. 1 root root  11296 Nov 16  2020 /usr/sbin/usernetctl
```

Not much of use

```bash
[simeon@aratus /]$ find / -perm /g=s -exec ls -la {} + 2>/dev/null
---x--s--x. 1 root nobody          382216 Nov 24  2021 /usr/bin/ssh-agent
-r-xr-sr-x. 1 root tty              15344 Jun 10  2014 /usr/bin/wall
-rwxr-sr-x. 1 root tty              19544 Feb  2  2021 /usr/bin/write
---x--s--x. 1 root ssh_keys        465760 Nov 24  2021 /usr/libexec/openssh/ssh-keysign
-rwx--s--x. 1 root utmp             11192 Jun 10  2014 /usr/libexec/utempter/utempter
-rwxr-sr-x. 1 root root             11224 Nov 16  2020 /usr/sbin/netreport
-rwxr-sr-x. 1 root postdrop        218560 Apr  1  2020 /usr/sbin/postdrop
-rwxr-sr-x. 1 root postdrop        264128 Apr  1  2020 /usr/sbin/postqueue

/run/log/journal:
total 0
drwxr-sr-x. 3 root systemd-journal 60 May 10 08:27 .
drwxr-xr-x. 3 root root            60 May 10 08:27 ..
drwxr-s---+ 2 root systemd-journal 60 May 10 08:27 12b8f3b650c474458eabe94bf9cca450

```

**Might be worth inspecting**

##### REVIEW LOGS

---

Since there was a reference in sudo -l of being a
```bash
[simeon@aratus /]$ find /var/log -perm /o=r -type f 2>/dev/null
/var/log/grubby_prune_debug
/var/log/lastlog
/var/log/wtmp
/var/log/tuned/tuned.log
/var/log/dmesg.old
/var/log/aws114_ssm_agent_installation.log
/var/log/dmesg
```

```bash
[simeon@aratus /]$ lastlog
Username         Port     From             Latest
root             pts/0    172.16.42.100    Fri Mar 25 21:29:50 +0100 2022
bin                                        **Never logged in**
daemon                                     **Never logged in**
adm                                        **Never logged in**
lp                                         **Never logged in**
sync                                       **Never logged in**
shutdown                                   **Never logged in**
halt                                       **Never logged in**
mail                                       **Never logged in**
operator                                   **Never logged in**
games                                      **Never logged in**
ftp                                        **Never logged in**
nobody                                     **Never logged in**
systemd-network                            **Never logged in**
dbus                                       **Never logged in**
polkitd                                    **Never logged in**
sshd                                       **Never logged in**
postfix                                    **Never logged in**
theodore         pts/0                     Fri Mar 25 21:57:42 +0100 2022
automation       pts/3    aratus           Wed Nov 24 19:37:07 +0100 2021
tss                                        **Never logged in**
simeon           pts/0    ip-10-11-73-42.e Fri May 10 08:47:03 +0200 2024
tcpdump                                    **Never logged in**
saslauth                                   **Never logged in**
apache                                     **Never logged in**

```

```bash
[simeon@aratus /]$ who
simeon   pts/0        2024-05-10 08:47 (ip-10-11-73-42.eu-west-1.compute.internal)
```

Nobody else is logged in the computer as of today

None of the logs that i can read seem to conatin things of interest.

##### CRONJOBS

By default in /etc/crontab and other files in /etc related to cron show nothing (only anacron runs hourly)

No access to /var/spool/cron

Seen things through pspy

After this i thought about doing [[PROCESS GATHERING]]