
## RECON

--- 

22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)

- No known vulns in exploitdb for this version

We can log into the machine using the credentials:
- claire-r
- Password1

## POST ENTRY

---

**Tested for**
- kernel info: not that i could see
- filesystem misc
- get info on users 

## FILESYSTEM

---

```bash
ls -la /
total 72
drwxr-xr-x  19 root root  4096 Dec 20  2022 .
drwxr-xr-x  19 root root  4096 Dec 20  2022 ..
lrwxrwxrwx   1 root root     7 Aug 31  2022 bin -> usr/bin
drwxr-xr-x   4 root root  4096 Dec 20  2022 boot
drwxr-xr-x  18 root root  3940 May 19 12:14 dev
drwxr-xr-x 101 root root  4096 Sep 22  2023 etc
drwxr-xr-x   4 root root  4096 Dec 22  2022 home
lrwxrwxrwx   1 root root     7 Aug 31  2022 lib -> usr/lib
lrwxrwxrwx   1 root root     9 Aug 31  2022 lib32 -> usr/lib32
lrwxrwxrwx   1 root root     9 Aug 31  2022 lib64 -> usr/lib64
lrwxrwxrwx   1 root root    10 Aug 31  2022 libx32 -> usr/libx32
drwx------   2 root root 16384 Dec 20  2022 lost+found
drwxr-xr-x   2 root root  4096 Dec 22  2022 media
drwxr-xr-x   2 root root  4096 Aug 31  2022 mnt
drwxr-xr-x   2 root root  4096 Aug 31  2022 opt
dr-xr-xr-x 176 root root     0 May 19 12:12 proc
drwx------   5 root root  4096 Sep 22  2023 root
drwxr-xr-x  30 root root   940 May 19 13:55 run
lrwxrwxrwx   1 root root     8 Aug 31  2022 sbin -> usr/sbin
drwxr-xr-x   8 root root  4096 Dec 20  2022 snap
drwxr-xr-x   2 root root  4096 Aug 31  2022 srv
dr-xr-xr-x  13 root root     0 May 19 12:12 sys
drwxrwxrwt  12 root root  4096 May 19 13:47 tmp
drwxr-xr-x  14 root root  4096 Aug 31  2022 usr
drwxr-xr-x  13 root root  4096 Aug 31  2022 var
```
- etc Nothing of interest
- srv Nothing of interest
- mnt Nothing of interest

## USERS INFO

---
/etc/passwd

```bash
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
user:x:1000:1000:admin:/home/user:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
claire-r:x:1001:1001:Claire Redfield,,,:/home/claire-r:/bin/bash
```
/etc/group
```bash
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,user
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
cdrom:x:24:user
floppy:x:25:
tape:x:26:
sudo:x:27:user
audio:x:29:
dip:x:30:user
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
plugdev:x:46:user
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
lxd:x:116:user
systemd-coredump:x:999:
user:x:1000:
claire-r:x:1001:
```

**user seems to be pretty powerful here**


## USER

---

Seems to be promising

```bash
user
/home
Executable files from user and /home that have suid
Executable files from user and /home that have sgid
Readable files from user and /home
-rw-r--r-- 1 user user  220 Feb 25  2020 /home/user/.bash_logout
-rw-r--r-- 1 user user 3771 Feb 25  2020 /home/user/.bashrc
-rw-r--r-- 1 user user  807 Feb 25  2020 /home/user/.profile
-rw-r--r-- 1 user user    0 Dec 22  2022 /home/user/.sudo_as_admin_successful
Writable files from user and /home

```

nothing interesting in any of these

Nothing in:
- /etc
- /usr
- /var
- /tmp
- /bin
- /srv

Actually seems to have nothing under it's name in any other than the ones i have just given 

```bash
/home/user:
total 36
drwxr-xr-x 5 user user 4096 Dec 22  2022 .
drwxr-xr-x 4 root root 4096 Dec 22  2022 ..
-rw------- 1 user user    1 Sep 22  2023 .bash_history
-rw-r--r-- 1 user user  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 user user 3771 Feb 25  2020 .bashrc
drwx------ 2 user user 4096 Dec 20  2022 .cache
-rw-r--r-- 1 user user  807 Feb 25  2020 .profile
drwx------ 3 user user 4096 Dec 22  2022 snap
drwx------ 2 user user 4096 Dec 20  2022 .ssh
-rw-r--r-- 1 user user    0 Dec 22  2022 .sudo_as_admin_successful

```

Also did not find anything using pspy64, which kind of blows my whole strategy 
## CLAIRE-R

---

```bash
id
uid=1001(claire-r) gid=1001(claire-r) groups=1001(claire-r)
```

## DOCKER

---
**PSPY64 OUTPUT**

```bash
2024/05/19 14:33:12 CMD: UID=0    PID=1560   | registry serve /etc/docker/registry/config.yml  # root command

2024/05/19 14:33:12 CMD: UID=0    PID=1554   | node app.js # app of the root
 # a little interesting is that this is in the container and supposedly running by root?
 
2024/05/19 14:33:12 CMD: UID=0    PID=1501   | /snap/docker/2285/bin/containerd-shim-runc-v2 -namespace moby -id de0610f5184548d54c2812fd8ced309dee88479f66167dbaae5ec1c6111f125d -address /run/snap.docker/containerd/containerd.sock 
2024/05/19 14:33:12 CMD: UID=0    PID=15     | 
2024/05/19 14:33:12 CMD: UID=0    PID=1493   | /snap/docker/2285/bin/containerd-shim-runc-v2 -namespace moby -id 44000a18a947e4f508c76acd7d674bbb13ad0fa1e180c44d6490377db6ca94e9 -address /run/snap.docker/containerd/containerd.sock 
2024/05/19 14:33:12 CMD: UID=0    PID=1490   | /snap/docker/2285/bin/containerd-shim-runc-v2 -namespace moby -id ecfd3fea4eaa1f0d1fb612240012663bcc40e9d922e9bb779d1c6feae67e4e4a -address /run/snap.docker/containerd/containerd.sock 
2024/05/19 14:33:12 CMD: UID=0    PID=1461   | /snap/docker/2285/bin/docker-proxy -proto tcp -host-ip :: -host-port 3306 -container-ip 172.18.0.3 -container-port 3306 
2024/05/19 14:33:12 CMD: UID=0    PID=1456   | /snap/docker/2285/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 3306 -container-ip 172.18.0.3 -container-port 3306 
2024/05/19 14:33:12 CMD: UID=0    PID=1442   | /snap/docker/2285/bin/docker-proxy -proto tcp -host-ip :: -host-port 8080 -container-ip 172.18.0.2 -container-port 8080 
2024/05/19 14:33:12 CMD: UID=0    PID=1437   | /snap/docker/2285/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 8080 -container-ip 172.18.0.2 -container-port 8080 
2024/05/19 14:33:12 CMD: UID=0    PID=1417   | /snap/docker/2285/bin/docker-proxy -proto tcp -host-ip :: -host-port 5000 -container-ip 172.17.0.2 -container-port 5000 
2024/05/19 14:33:12 CMD: UID=0    PID=1412   | /snap/docker/2285/bin/docker-proxy -proto tcp -host-ip 0.0.0.0 -host-port 5000 -container-ip 172.17.0.2 -container-port 5000 

2024/05/19 14:33:12 CMD: UID=0    PID=1108   | containerd --config /run/snap.docker/containerd/containerd.toml --log-level error 


```