Credentials for theodore are Rijyaswahebceibarjik

From here on let's try to be root

#### /opt

---

During the encounters i found that there were things in [[/opt]], and theodore has permissions to access.

#### SUDO

---

```bash

[theodore@aratus ansible]$ sudo -l
Matching Defaults entries for theodore on aratus:
    !visiblepw, always_set_home, match_group_by_gid, always_query_group_plugin, env_reset,
    env_keep="COLORS DISPLAY HOSTNAME HISTSIZE KDEDIR LS_COLORS", env_keep+="MAIL PS1 PS2 QTDIR
    USERNAME LANG LC_ADDRESS LC_CTYPE", env_keep+="LC_COLLATE LC_IDENTIFICATION LC_MEASUREMENT
    LC_MESSAGES", env_keep+="LC_MONETARY LC_NAME LC_NUMERIC LC_PAPER LC_TELEPHONE", env_keep+="LC_TIME
    LC_ALL LANGUAGE LINGUAS _XKB_CHARSET XAUTHORITY", secure_path=/sbin\:/bin\:/usr/sbin\:/usr/bin

User theodore may run the following commands on aratus:
    (automation) NOPASSWD: /opt/scripts/infra_as_code.sh
```


```
[theodore@aratus scripts]$ sudo -u automation /opt/scripts/infra_as_code.sh 
```
