SSH user: dev
SSH password: dev080217_devAPI!@

## /home/dev

There is an app folder with a git repository still active (hidden but still there), we also have other files, which might give us more information about the [[user profile]]
### /home/dev/apps

```bash
dev@editorial:~/apps$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    app_api/app.py
        deleted:    app_editorial/app.py
        deleted:    app_editorial/static/css/bootstrap-grid.css
        deleted:    app_editorial/static/css/bootstrap-grid.css.map
        deleted:    app_editorial/static/css/bootstrap-grid.min.css
        deleted:    app_editorial/static/css/bootstrap-grid.min.css.map
        deleted:    app_editorial/static/css/bootstrap-grid.rtl.css
        deleted:    app_editorial/static/css/bootstrap-grid.rtl.css.map
        deleted:    app_editorial/static/css/bootstrap-grid.rtl.min.css
        deleted:    app_editorial/static/css/bootstrap-grid.rtl.min.css.map
        deleted:    app_editorial/static/css/bootstrap-reboot.css
        deleted:    app_editorial/static/css/bootstrap-reboot.css.map
        deleted:    app_editorial/static/css/bootstrap-reboot.min.css
        deleted:    app_editorial/static/css/bootstrap-reboot.min.css.map
        deleted:    app_editorial/static/css/bootstrap-reboot.rtl.css
        deleted:    app_editorial/static/css/bootstrap-reboot.rtl.css.map
        deleted:    app_editorial/static/css/bootstrap-reboot.rtl.min.css
        deleted:    app_editorial/static/css/bootstrap-reboot.rtl.min.css.map
        deleted:    app_editorial/static/css/bootstrap-utilities.css
        deleted:    app_editorial/static/css/bootstrap-utilities.css.map
        deleted:    app_editorial/static/css/bootstrap-utilities.min.css
        deleted:    app_editorial/static/css/bootstrap-utilities.min.css.map
        deleted:    app_editorial/static/css/bootstrap-utilities.rtl.css
        deleted:    app_editorial/static/css/bootstrap-utilities.rtl.css.map
        deleted:    app_editorial/static/css/bootstrap-utilities.rtl.min.css
        deleted:    app_editorial/static/css/bootstrap-utilities.rtl.min.css.map
        deleted:    app_editorial/static/css/bootstrap.css
        deleted:    app_editorial/static/css/bootstrap.css.map
        deleted:    app_editorial/static/css/bootstrap.min.css
        deleted:    app_editorial/static/css/bootstrap.min.css.map
        deleted:    app_editorial/static/css/bootstrap.rtl.css
        deleted:    app_editorial/static/css/bootstrap.rtl.css.map
        deleted:    app_editorial/static/css/bootstrap.rtl.min.css
        deleted:    app_editorial/static/css/bootstrap.rtl.min.css.map
        deleted:    app_editorial/static/images/login-background.jpg
        deleted:    app_editorial/static/images/pexels-janko-ferlic-590493.jpg
        deleted:    app_editorial/static/images/pexels-min-an-694740.jpg
        deleted:    app_editorial/static/js/bootstrap.bundle.js
        deleted:    app_editorial/static/js/bootstrap.bundle.js.map
        deleted:    app_editorial/static/js/bootstrap.bundle.min.js
        deleted:    app_editorial/static/js/bootstrap.bundle.min.js.map
        deleted:    app_editorial/static/js/bootstrap.esm.js
        deleted:    app_editorial/static/js/bootstrap.esm.js.map
        deleted:    app_editorial/static/js/bootstrap.esm.min.js
        deleted:    app_editorial/static/js/bootstrap.esm.min.js.map
        deleted:    app_editorial/static/js/bootstrap.js
        deleted:    app_editorial/static/js/bootstrap.js.map
        deleted:    app_editorial/static/js/bootstrap.min.js
        deleted:    app_editorial/static/js/bootstrap.min.js.map
        deleted:    app_editorial/templates/about.html
        deleted:    app_editorial/templates/index.html
        deleted:    app_editorial/templates/upload.html

```

This is what probably is in production and has been moved there. Let us get a copy of this [[repository]]

## Generic recon

```
dev@editorial:~$ cat /etc/passwd
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
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-network:x:101:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:102:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:104::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:104:105:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
pollinate:x:105:1::/var/cache/pollinate:/bin/false
sshd:x:106:65534::/run/sshd:/usr/sbin/nologin
syslog:x:107:113::/home/syslog:/usr/sbin/nologin
uuidd:x:108:114::/run/uuidd:/usr/sbin/nologin
tcpdump:x:109:115::/nonexistent:/usr/sbin/nologin
tss:x:110:116:TPM software stack,,,:/var/lib/tpm:/bin/false
landscape:x:111:117::/var/lib/landscape:/usr/sbin/nologin
usbmux:x:112:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
prod:x:1000:1000:Alirio Acosta:/home/prod:/bin/bash
lxd:x:999:100::/var/snap/lxd/common/lxd:/bin/false
dev:x:1001:1001::/home/dev:/bin/bash
fwupd-refresh:x:113:119:fwupd-refresh user,,,:/run/systemd:/usr/sbin/nologin
_laurel:x:998:998::/var/log/laurel:/bin/false
```

**Alirio Acosta** ?? for production

```bash
dev@editorial:/$ id
uid=1001(dev) gid=1001(dev) groups=1001(dev)
```

```bash
dev@editorial:/$ sudo -l
[sudo] password for dev: 
Sorry, try again.
[sudo] password for dev: 
Sorry, try again.
[sudo] password for dev: 
Sorry, user dev may not run sudo on editorial.
```

```bash
dev@editorial:/opt/internal_apps$ cat /etc/group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog
tty:x:5:
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
messagebus:x:104:
systemd-timesync:x:105:
input:x:106:
sgx:x:107:
kvm:x:108:
render:x:109:
lxd:x:110:
_ssh:x:111:
crontab:x:112:
syslog:x:113:
uuidd:x:114:
tcpdump:x:115:
tss:x:116:
landscape:x:117:
prod:x:1000:prod
dev:x:1001:
netdev:x:118:
fwupd-refresh:x:119:
_laurel:x:998:
```
## Files from apps 

```bash
dev@editorial:/opt/apps$ ls -la
total 12
drwxr-xr-x 3 www-data www-data 4096 Jun  5 14:36 .
drwxr-xr-x 4 root     root     4096 Jun  5 14:36 ..
drwxr-xr-x 6 www-data www-data 4096 Aug  1 09:50 app_editorial
```

```bash
dev@editorial:/opt/apps/app_editorial$ ls -la
total 32
drwxr-xr-x 6 www-data www-data 4096 Aug  1 09:50 .
drwxr-xr-x 3 www-data www-data 4096 Jun  5 14:36 ..
-rw-r--r-- 1 www-data www-data 3536 Jan 16  2024 app.py
srwxrwx--- 1 www-data www-data    0 Aug  1 09:50 editorial.sock
drwxrwxr-x 2 www-data www-data 4096 Jun  5 14:36 __pycache__
drwxr-xr-x 6 www-data www-data 4096 Jun  5 14:36 static
drwxr-xr-x 2 www-data www-data 4096 Jun  5 14:36 templates
drwxrwxr-x 5 www-data www-data 4096 Jun  5 14:36 venv
-rwxr-xr-x 1 www-data www-data   62 Feb  4  2023 wsgi.py
```

seems like app itself will not be much useful, although i wonder what is up with the socket

```bash
dev@editorial:/opt/internal_apps$ ls -la
total 20
drwxr-xr-x 5 www-data www-data 4096 Jun  5 14:36 .
drwxr-xr-x 4 root     root     4096 Jun  5 14:36 ..
drwxr-xr-x 3 root     root     4096 Jun  5 14:36 app_api
drwxr-x--- 7 root     prod     4096 Aug  1 12:03 clone_changes
drwxr-xr-x 2 www-data www-data 4096 Jun  5 14:36 environment_scripts
```

## Processes 

As for processes, there is the cleaner but that's for www-data, which i can't modify

```bash
2024/08/01 13:58:59 CMD: UID=0     PID=1      | /sbin/init 
2024/08/01 13:59:01 CMD: UID=0     PID=4584   | /usr/sbin/CRON -f -P 
2024/08/01 13:59:01 CMD: UID=0     PID=4585   | /usr/sbin/CRON -f -P 
2024/08/01 13:59:01 CMD: UID=33    PID=4586   | /bin/bash /opt/internal_apps/environment_scripts/clear.sh 
2024/08/01 13:59:01 CMD: UID=33    PID=4587   | find /opt/apps/app_editorial/static/uploads/. -exec rm -f {} ; 
2024/08/01 13:59:01 CMD: UID=33    PID=4588   | find /opt/apps/app_editorial/static/uploads/. -exec rm -f {} ; 
2024/08/01 13:59:28 CMD: UID=0     PID=4589   | (otd-news) 
2024/08/01 13:59:28 CMD: UID=0     PID=4590   | mktemp 
2024/08/01 13:59:28 CMD: UID=0     PID=4591   | mktemp 
2024/08/01 13:59:28 CMD: UID=0     PID=4592   | /bin/sh /etc/update-motd.d/50-motd-news --force 
2024/08/01 13:59:28 CMD: UID=0     PID=4593   | /bin/sh /etc/update-motd.d/50-motd-news --force 
2024/08/01 13:59:28 CMD: UID=0     PID=4595   | /bin/sh /etc/update-motd.d/50-motd-news --force 
2024/08/01 13:59:28 CMD: UID=0     PID=4594   | /bin/sh /etc/update-motd.d/50-motd-news --force 
2024/08/01 13:59:28 CMD: UID=0     PID=4596   | /bin/sh /etc/update-motd.d/50-motd-news --force 
2024/08/01 13:59:28 CMD: UID=0     PID=4598   | /bin/sh /etc/update-motd.d/50-motd-news --force 
2024/08/01 13:59:28 CMD: UID=0     PID=4599   | /bin/sh /etc/update-motd.d/50-motd-news --force 
2024/08/01 13:59:28 CMD: UID=0     PID=4600   | /bin/sh /etc/update-motd.d/50-motd-news --force 
2024/08/01 13:59:28 CMD: UID=0     PID=4601   | uname -m 
2024/08/01 13:59:28 CMD: UID=0     PID=4602   | /bin/sh /etc/update-motd.d/50-motd-news --force 
2024/08/01 13:59:28 CMD: UID=0     PID=4603   | /bin/sh /etc/update-motd.d/50-motd-news --force 
2024/08/01 13:59:29 CMD: UID=0     PID=4605   | sed -e s/.*: // -e s:\s\+:/:g 
2024/08/01 13:59:29 CMD: UID=0     PID=4604   | grep -m1 ^model name /proc/cpuinfo 
2024/08/01 13:59:29 CMD: UID=0     PID=4606   | /bin/sh /etc/update-motd.d/50-motd-news --force 
2024/08/01 13:59:34 CMD: UID=0     PID=4607   | 
2024/08/01 13:59:49 CMD: UID=0     PID=4608   | rm -f /tmp/tmp.lDj9vCpHV7 /tmp/tmp.kafOeKATts /tmp/tmp.sQCF9K93zW 
2024/08/01 13:59:49 CMD: UID=0     PID=4609   | 
2024/08/01 14:00:01 CMD: UID=0     PID=4610   | /usr/sbin/CRON -f -P 
2024/08/01 14:00:01 CMD: UID=0     PID=4611   | /usr/sbin/CRON -f -P 
2024/08/01 14:00:01 CMD: UID=33    PID=4612   | /bin/bash /opt/internal_apps/environment_scripts/clear.sh 
2024/08/01 14:00:01 CMD: UID=33    PID=4613   | find /opt/apps/app_editorial/static/uploads/. -exec rm -f {} ; 
2024/08/01 14:00:01 CMD: UID=33    PID=4614   | rm -f /opt/apps/app_editorial/static/uploads/. 
2024/08/01 14:01:01 CMD: UID=0     PID=4616   | /usr/sbin/CRON -f -P 
2024/08/01 14:01:01 CMD: UID=0     PID=4617   | /usr/sbin/CRON -f -P 
2024/08/01 14:01:01 CMD: UID=33    PID=4618   | /bin/bash /opt/internal_apps/environment_scripts/clear.sh 
2024/08/01 14:01:01 CMD: UID=33    PID=4619   | 
2024/08/01 14:01:01 CMD: UID=33    PID=4620   | find /opt/apps/app_editorial/static/uploads/. -exec rm -f {} ; 
```

With a few commands 

```bash
dev@editorial:/proc$ for instance in $(ls); do if [[ $instance =~ ^[0-9]*$ ]] ; then cat ./${instance}/cmdline ; echo ; fi; done;
/sbin/init
/usr/bin/python3/usr/local/bin/gunicorn--workers3--bind127.0.0.1:5000-m007wsgi:app
/usr/bin/python3/usr/local/bin/gunicorn--workers4--bindunix:editorial.sock-m007wsgi:app
/usr/sbin/cron-f-P
sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups
/sbin/agetty-o-p -- \u--nocleartty1linux
nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
nginx: worker process
nginx: worker process
/usr/bin/python3/usr/local/bin/gunicorn--workers4--bindunix:editorial.sock-m007wsgi:app
/usr/bin/python3/usr/local/bin/gunicorn--workers3--bind127.0.0.1:5000-m007wsgi:app

/usr/bin/python3/usr/local/bin/gunicorn--workers3--bind127.0.0.1:5000-m007wsgi:app
/usr/bin/python3/usr/local/bin/gunicorn--workers4--bindunix:editorial.sock-m007wsgi:app
/usr/bin/python3/usr/local/bin/gunicorn--workers3--bind127.0.0.1:5000-m007wsgi:app
/usr/bin/python3/usr/local/bin/gunicorn--workers4--bindunix:editorial.sock-m007wsgi:app
/usr/bin/python3/usr/local/bin/gunicorn--workers4--bindunix:editorial.sock-m007wsgi:app


/lib/systemd/systemd-journald




/sbin/multipathd-d-s
/lib/systemd/systemd-udevd
/lib/systemd/systemd-networkd


/usr/libexec/fwupd/fwupd
/usr/libexec/upowerd


sshd: dev [priv]
/lib/systemd/systemd--user
(sd-pam)

sshd: dev@pts/0
-bash

cat: ./7277/cmdline: No such file or directory



/lib/systemd/systemd-resolved
/lib/systemd/systemd-timesyncd
/sbin/auditd
/usr/local/sbin/laurel--config/etc/laurel/config.toml
/usr/bin/VGAuthService
/usr/bin/vmtoolsd



/sbin/dhclient-1-4-v-i-pf/run/dhclient.eth0.pid-lf/var/lib/dhcp/dhclient.eth0.leases-I-df/var/lib/dhcp/dhclient6.eth0.leaseseth0

@dbus-daemon--system--address=systemd:--nofork--nopidfile--systemd-activation--syslog-only

/usr/sbin/irqbalance--foreground
/usr/bin/python3/usr/bin/networkd-dispatcher--run-startup-triggers
/usr/libexec/polkitd--no-debug
/usr/sbin/rsyslogd-n-iNONE
/lib/systemd/systemd-logind

/usr/libexec/udisks2/udisksd


/usr/sbin/ModemManager

```
## Files in general 

```bash
dev@editorial:/$ find / -writable 2>/dev/null
... nohthing interesting
dev@editorial:/$ find / -perm /+s 2>/dev/null
... nothing interesting
dev@editorial:/$ getcap / -r 2>/dev/null
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper cap_net_bind_service,cap_net_admin=ep
/usr/bin/mtr-packet cap_net_raw=ep
/usr/bin/ping cap_net_raw=ep
dev@editorial:/$ find / -user prod 2>/dev/null
/home/prod
/var/crash/_opt_wsgi.py.1000.crash
```

## Server nginx

Actually took a better look at what [[nginx]] was doing 



