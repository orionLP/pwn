We can easily get the ssh private key of this individual in the .ssh folder, which will make our job easier

## Home directory

immediately after entering into the home directory of dash i found the [[monit]] configuration files, a product used for monitoring filesystems and processes

No other interesting things were found. 

## Checking files in computer

Since there is another user in this computer let us try to find out what might he have around 

```bash
dash@usage:~$ find / -user xander 2>/dev/null 
/tmp/linpeas.sh -> probably another user of htb
/tmp/tmux-1001 -> only xander can access
/home/xander -> only xander can access

```

## Locating previously used services 

```bash
dash@usage:/var/www/html$ ls -la 
total 16
drwxrwxrwx  4 root xander 4096 Aug  9 21:48 .
drwxr-xr-x  3 root root   4096 Apr  2 21:15 ..
drwxrwxr-x 13 dash dash   4096 Aug  9 21:39 project_admin
drwxrwxr-x 12 dash dash   4096 Apr  2 21:15 usage_blog

```

Let us try to investigate a little further these [[previous applications]]

## Checking on running processes

Using pspy64 i only found dash running processes on the server, but not xander so i doubt it is on this path