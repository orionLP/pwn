user: `xander`
password: `3nc0d3d_pa$$w0rd`

## SUDO 

```bash
xander@usage:/home/dash$ sudo -l 
Matching Defaults entries for xander on usage:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User xander may run the following commands on usage:
    (ALL : ALL) NOPASSWD: /usr/bin/usage_management
```

We are able to use a user created binary with the same privileges as root. Let us examine now [[usage_management]].
