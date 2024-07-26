Has anonymous login and the following can be extracted from an ls

```bash
ftp> ls -la
229 Entering Extended Passive Mode (|||16126|).
150 Here comes the directory listing.
drwxr-xr-x    3 0        0              17 Nov 23  2021 .
drwxr-xr-x    3 0        0              17 Nov 23  2021 ..
drwxr-xr-x    2 0        0               6 Jun 09  2021 pub
226 Directory send OK.
```

Inside pub there is nothing. All of the files are owned by 0 (i assume root)
### BRUTEFORCE

#### 1

User: simeon
Passwords: rockyou.txt (30 min no result), darkweb2017-top10000.txt (30 min no result)

#### TESTED
- Attempted login as root with no pass
- logins within the server