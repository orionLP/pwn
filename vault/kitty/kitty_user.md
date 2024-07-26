**user**: kitty
**passwords**: L0ng_Liv3_KittY

## COMMON VECTORS OF ATTACK

- SUDO: Kitty cannot use sudo 
- SUID/SGID:

```bash
kitty@kitty:/$ find / -perm /+s 2>/dev/null
/usr/sbin/unix_chkpwd
/usr/sbin/pam_extrausers_chkpwd
/usr/lib/x86_64-linux-gnu/utempter/utempter
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/mount
/usr/bin/sudo
/usr/bin/bsd-write
/usr/bin/expiry
/usr/bin/chage
/usr/bin/ssh-agent
/usr/bin/wall
/usr/bin/passwd
/usr/bin/su
/usr/bin/newgrp
/usr/bin/at
/usr/bin/umount
/usr/bin/fusermount
/usr/bin/crontab
/usr/bin/chfn
/usr/local/share/fonts
/usr/local/lib/python3.8
/usr/local/lib/python3.8/dist-packages
/snap/snapd/18357/usr/lib/snapd/snap-confine
/snap/core20/1822/usr/bin/chage
/snap/core20/1822/usr/bin/chfn
/snap/core20/1822/usr/bin/chsh
/snap/core20/1822/usr/bin/expiry
/snap/core20/1822/usr/bin/gpasswd
/snap/core20/1822/usr/bin/mount
/snap/core20/1822/usr/bin/newgrp
/snap/core20/1822/usr/bin/passwd
/snap/core20/1822/usr/bin/ssh-agent
/snap/core20/1822/usr/bin/su
/snap/core20/1822/usr/bin/sudo
/snap/core20/1822/usr/bin/umount
/snap/core20/1822/usr/bin/wall
/snap/core20/1822/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1822/usr/lib/openssh/ssh-keysign
/snap/core20/1822/usr/sbin/pam_extrausers_chkpwd
/snap/core20/1822/usr/sbin/unix_chkpwd
/snap/core20/1822/var/mail
/snap/core20/1328/usr/bin/chage
/snap/core20/1328/usr/bin/chfn
/snap/core20/1328/usr/bin/chsh
/snap/core20/1328/usr/bin/expiry
/snap/core20/1328/usr/bin/gpasswd
/snap/core20/1328/usr/bin/mount
/snap/core20/1328/usr/bin/newgrp
/snap/core20/1328/usr/bin/passwd
/snap/core20/1328/usr/bin/ssh-agent
/snap/core20/1328/usr/bin/su
/snap/core20/1328/usr/bin/sudo
/snap/core20/1328/usr/bin/umount
/snap/core20/1328/usr/bin/wall
/snap/core20/1328/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1328/usr/lib/openssh/ssh-keysign
/snap/core20/1328/usr/sbin/pam_extrausers_chkpwd
/snap/core20/1328/usr/sbin/unix_chkpwd
/snap/core20/1328/var/mail
/run/log/journal
/var/local
/var/log/journal
/var/log/journal/b77856cd1def4b02be58c669f6c57d4e
/var/mail
```

```bash
kitty@kitty:/usr/local/lib/python3.8/dist-packages$ find / -perm /+s -writable 2>/dev/null
kitty@kitty:/usr/local/lib/python3.8/dist-packages$ 
```
- CRONTAB: no external jobs running

  ```bash
  kitty@kitty:/usr/local/lib/python3.8/dist-packages$ crontab -l
  no crontab for kitty
    ```

- CAPABILITES: nothing interesting

  ```bash
  
  kitty@kitty:/$ getcap / -r 2>/dev/null
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/ping = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/snap/core20/1822/usr/bin/ping = cap_net_raw+ep
/snap/core20/1328/usr/bin/ping = cap_net_raw+ep

```

- RUNNING PROCESSES: 

  ```bash
	2024/07/20 10:19:10 CMD: UID=0     PID=3      | 
	2024/07/20 10:19:10 CMD: UID=0     PID=2      | 
	2024/07/20 10:19:10 CMD: UID=0     PID=1      | /sbin/init maybe-ubiquity 
	2024/07/20 10:19:29 CMD: UID=0     PID=2946   | 
	2024/07/20 10:20:01 CMD: UID=0     PID=2947   | /usr/sbin/CRON -f 
	2024/07/20 10:20:01 CMD: UID=0     PID=2948   | 
	2024/07/20 10:20:01 CMD: UID=0     PID=2949   | /bin/sh -c /usr/bin/bash /opt/log_checker.sh 
	2024/07/20 10:20:01 CMD: UID=0     PID=2950   | 

    ```

   The [[log_checker]] is interesting let us check it out.

## COMMON RECON

**MACHINE SPECIFIC**

- Checking the recent app we have just used to get here: 
	- define('DB_SERVER', 'localhost');
	 define('DB_USERNAME', 'kitty');
	 define('DB_PASSWORD', 'Sup3rAwesOm3Cat!');
     define('DB_NAME', 'mywebsite');

	 -> checking the DB with these credentials shows that there is little to none information in the tables of the website. There are other databases but i found nothing of interest in there
	 
	- Checking in the folder of the /var/www there is another site called development owned in it's majority by *root*, but some of the parts are owned by *www-data*. It is mostly similar to the normal site in /http but it is not that similar.

	- s

**Regarding the user kitty** 

```bash
kitty@kitty:/$ id
uid=1000(kitty) gid=1000(kitty) groups=1000(kitty)
```

```bash
kitty@kitty:/$ sudo -l
[sudo] password for kitty: 
Sorry, user kitty may not run sudo on kitty.
```

**GENERAL**

```bash
kitty@kitty:/$ cat /etc/passwd

root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
landscape:x:109:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:110:1::/var/cache/pollinate:/bin/false
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
sshd:x:112:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
kitty:x:1000:1000:kitty:/home/kitty:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
mysql:x:113:117:MySQL Server,,,:/nonexistent:/bin/false
fwupd-refresh:x:114:119:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
```

```bash
kitty@kitty:/usr/local/lib/python3.8/dist-packages$ cat /etc/group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog
tty:x:5:syslog
disk:x:6:
lp:x:7:
mail:x:8:
news:x:9:
uucp:x:10:
man:x:12:
proxy:x:13:
kmem:x:15:
dialout:x:20:
fax:x:21:
voice:x:22:
cdrom:x:24:
floppy:x:25:
tape:x:26:
sudo:x:27:
audio:x:29:
dip:x:30:
www-data:x:33:
backup:x:34:
operator:x:37:
list:x:38:
irc:x:39:
src:x:40:
gnats:x:41:
shadow:x:42:
utmp:x:43:
video:x:44:
sasl:x:45:
plugdev:x:46:
staff:x:50:
games:x:60:
users:x:100:
nogroup:x:65534:
systemd-journal:x:101:
systemd-network:x:102:
systemd-resolve:x:103:
systemd-timesync:x:104:
crontab:x:105:
messagebus:x:106:
input:x:107:
kvm:x:108:
render:x:109:
syslog:x:110:
tss:x:111:
uuidd:x:112:
tcpdump:x:113:
ssh:x:114:
landscape:x:115:
lxd:x:116:
systemd-coredump:x:999:
kitty:x:1000:
mysql:x:117:
ssl-cert:x:118:
fwupd-refresh:x:119:
```