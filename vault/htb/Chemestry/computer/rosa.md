Credentials:
- rosa 
- `unicorniosrosados`

Log in using ssh

## LINPEAS

Some of the information from linpeas included was the following:
```
# seems like a monitoring site
Service running at 127.0.0.1:8080 

# vulnerable to CVE (tested and it was a false positive)
Vulnerable to CVE-2021-3560

# vulnerable sudo version (tested and it was a false positive)
╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version
Sudo version 1.8.31

```

Since there was an app running by root, i wanted to test it out, so i forwarded that port to a local one.

```bash
2024/11/11 07:39:48 CMD: UID=0     PID=1082   | /usr/bin/python3.9 /opt/monitoring_site/app.py 
```

```bash
sh -L 8080:127.0.0.1:8080 rosa@10.10.11.38
```

And it turns out it is using aiohttp/3.9.1, which is vulnerable to path traversal (CVE-2021-3560)

If you fuzz the app you will find the following static folder (or if you use burp suite)

```bash
assets                  [Status: 403, Size: 14, Words: 2, Lines: 1]
```

In my case i used the code from: https://github.com/z3rObyte/CVE-2024-23334-PoC with path /assets/.

And after leaking /root/.ssh/id_rsa we are now [[root]]