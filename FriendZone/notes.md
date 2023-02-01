## FriendZone

# Nmap

let's run the first default command:

```{sh}
sudo nmap -p- 10.129.222.224  > output
cat output | grep -E "/tcp" | cut -d "/" -f 1 | tr "\n" ","

21,22,53,80,139,443,445
```

We can see that a lot of services are up now let's do a "through" scan:

```{sh}
sudo nmap -p21,22,53,80,139,443,445 -sC -sV 10.129.222.224

Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-30 10:45 CET
Nmap scan report for 10.129.222.224
Host is up (0.26s latency).

PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 3.0.3
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 a9:68:24:bc:97:1f:1e:54:a5:80:45:e7:4c:d9:aa:a0 (RSA)
|   256 e5:44:01:46:ee:7a:bb:7c:e9:1a:cb:14:99:9e:2b:8e (ECDSA)
|_  256 00:4e:1a:4f:33:e8:a0:de:86:a6:e4:2a:5f:84:61:2b (ED25519)
53/tcp  open  domain      ISC BIND 9.11.3-1ubuntu1.2 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.11.3-1ubuntu1.2-Ubuntu
80/tcp  open  http        Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Friend Zone Escape software
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
443/tcp open  ssl/http    Apache httpd 2.4.29
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: 404 Not Found
| ssl-cert: Subject: commonName=friendzone.red/organizationName=CODERED/stateOrProvinceName=CODERED/countryName=JO
| Not valid before: 2018-10-05T21:02:30
|_Not valid after:  2018-11-04T21:02:30
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
Service Info: Hosts: FRIENDZONE, 127.0.1.1; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_ms-sql-info: ERROR: Script execution failed (use -d to debug)
|_nbstat: NetBIOS name: FRIENDZONE, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
|_smb-os-discovery: ERROR: Script execution failed (use -d to debug)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   2.02: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-01-30T09:45:55
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 41.94 seconds
```

There appears to be 2 domains for 10.129.222.224, the first one being the default and the second one being friendzone.red. The default one greets us with:

> email: info@friendzoneportal.red

Now let's run a quick scan to see if there are more webpages that the one we are greeted with.

```{sh}
#!/bin/bash

ls $PWD/../SecLists/Discovery/Web-Content | grep -E "^[cC]ommon|directory-list-2.3-medium.txt" | sort -u > output

for name in output
do 
    gobuster dir -w $PWD/../SecLists/Discovery/Web-Content/${name} -u http://10.129.222.224 | grep -E "Status"
done

/wordpress            (Status: 301) [Size: 320] [--> http://10.129.222.224/wordpress/]
```

There appears to be nothing there

After looking up how to do zone transfers with a dns server, we can do the following 

```{sh}
dig axfr friendzone.red @10.129.223.65

; <<>> DiG 9.18.1-1ubuntu1.3-Ubuntu <<>> axfr friendzone.red @10.129.223.65
;; global options: +cmd
friendzone.red.		604800	IN	SOA	localhost. root.localhost. 2 604800 86400 2419200 604800
friendzone.red.		604800	IN	AAAA	::1
friendzone.red.		604800	IN	NS	localhost.
friendzone.red.		604800	IN	A	127.0.0.1
administrator1.friendzone.red. 604800 IN A	127.0.0.1
hr.friendzone.red.	604800	IN	A	127.0.0.1
uploads.friendzone.red.	604800	IN	A	127.0.0.1
friendzone.red.		604800	IN	SOA	localhost. root.localhost. 2 604800 86400 2419200 604800
;; Query time: 136 msec
;; SERVER: 10.129.223.65#53(10.129.223.65) (TCP)
;; WHEN: Tue Jan 31 10:33:33 CET 2023
;; XFR size: 8 records (messages 1, bytes 289)

```


Now let's do a quick scan through the admin and uploads page

```{sh}
#!/bin/bash

ls $PWD/../SecLists/Discovery/Web-Content | grep -E "^[cC]ommon|directory-list-2.3-medium.txt" | sort -u > output

echo "starting web discovery against https://administrator1.friendzone.red/"

for name in output
do 
    gobuster dir -w $PWD/../SecLists/Discovery/Web-Content/${name} -u https://administrator1.friendzone.red/ -k | grep -E "Status"
done

echo "starting web discovery against https://uploads.friendzone.red/"

for name in output
do 
    gobuster dir -w $PWD/../SecLists/Discovery/Web-Content/${name} -u https://uploads.friendzone.red/ -k | grep -E "Status"
done

/images               (Status: 301) [Size: 349] [--> https://administrator1.friendzone.red/images/]


/files                (Status: 301) [Size: 334] [--> https://uploads.friendzone.red/files/]

gobuster dir -w ./directory-list-2.3-medium.txt -x php -u https://uploads.friendzone.red/ -k
/.php                 (Status: 403) [Size: 302]
/files                (Status: 301) [Size: 334] [--> https://uploads.friendzone.red/files/]
/upload.php           (Status: 200) [Size: 38]
/.php                 (Status: 403) [Size: 302]
/server-status        (Status: 403) [Size: 311]

gobuster dir -w ./directory-list-2.3-medium.txt -x php -u https://administrator1.friendzone.red/ -k
/.php                 (Status: 403) [Size: 309]
/images               (Status: 301) [Size: 349] [--> https://administrator1.friendzone.red/images/]
/login.php            (Status: 200) [Size: 7]
/dashboard.php        (Status: 200) [Size: 101]
/timestamp.php        (Status: 200) [Size: 36]
/server-status        (Status: 403) [Size: 318]

```

The official writeup does the following thing: it gets the admin password for login in the samba share, allowing it to use the dashboard.php file, which uses a php file in one of the url parameters.
This can be leveraged as we have a way to upload files through samba, using the path ../../../../../../../../../etc/Development/shell we get a reverse shell.

After looking at the configuration file for the dns server we find another zone called friendzoneportal

```{sh}
$ cat db.friendzoneportal.red

;
; BIND data file for local loopback interface
;
$TTL    604800
@       IN      SOA     localhost. root.localhost. (
                              2         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      localhost.
@       IN      A       127.0.0.1
admin   IN      A       127.0.0.1
vpn     IN      A       127.0.0.1
files   IN      A       127.0.0.1
imports   IN      A       127.0.0.1

@       IN      AAAA    ::1
```

The configuration file for the samba includes the following definitions

```{sh}
[Files]
    comment = "FriendZone Samba Server Files /etc/Files"
    path = /etc/hole
    read only = yes
    browsable = yes

[general]
    comment = "FriendZone Samba Server Files"
    path = /etc/general
    read only = yes
    browsable = yes
    public = yes
    force user = nobody
    force group = nogroup

[Development]
    comment = "FriendZone Samba Server Files"
    path = /etc/Development
    read only = yes
    browsable = yes
    public = yes
    writable = yes
    create mask = 0777
    directory mask = 0777
    force user = nobody
    force group = nogroup
```

a configuration file from apache server 

```{sh}
$ cat 000-default.conf

<VirtualHost *:80>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	#ServerName www.example.com

	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html

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

<VirtualHost _default_:443>
    ServerAdmin admin@example.com
    #ServerName www.example.com
    #ServerAlias example.com

    DocumentRoot /var/www/html1

    SSLEngine on
    SSLCertificateFile /root/certs/friendzone.red.crt
    SSLCertificateKeyFile /root/certs/friendzone.red.key

</VirtualHost>

<VirtualHost _default_:443>
    ServerAdmin admin@example.com
    ServerName friendzone.red
    ServerAlias friendzone.red 

    DocumentRoot /var/www/friendzone

    SSLEngine on
    SSLCertificateFile /root/certs/friendzone.red.crt
    SSLCertificateKeyFile /root/certs/friendzone.red.key
</VirtualHost>

<VirtualHost _default_:443>
    ServerAdmin admin@example.com
    ServerName uploads.friendzone.red
    ServerAlias uploads.friendzone.red

    DocumentRoot /var/www/uploads

    SSLEngine on
    SSLCertificateFile /root/certs/friendzone.red.crt
    SSLCertificateKeyFile /root/certs/friendzone.red.key
</VirtualHost>

<VirtualHost _default_:443>
    ServerAdmin admin@example.com
    ServerName administrator1.friendzone.red
    ServerAlias administrator1.friendzone.red

    DocumentRoot /var/www/admin

    SSLEngine on
    SSLCertificateFile /root/certs/friendzone.red.crt
    SSLCertificateKeyFile /root/certs/friendzone.red.key
</VirtualHost>

<VirtualHost _default_:443>
    ServerAdmin admin@example.com
    ServerName friendzoneportal.red
    ServerAlias friendzoneportal.red

    DocumentRoot /var/www/friendzoneportal

    SSLEngine on
    SSLCertificateFile /root/certs/friendzone.red.crt
    SSLCertificateKeyFile /root/certs/friendzone.red.key
</VirtualHost>

<VirtualHost _default_:443>
    ServerAdmin admin@example.com

    ServerName admin.friendzoneportal.red
    ServerAlias admin.friendzoneportal.red

    DocumentRoot /var/www/friendzoneportaladmin

    SSLEngine on
    SSLCertificateFile /root/certs/friendzone.red.crt
    SSLCertificateKeyFile /root/certs/friendzone.red.key
</VirtualHost>


# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
```

after a  while i found this page in the apache server

```{sh}

$ cat mysql_data.conf
for development process this is the mysql creds for user friend

db_user=friend

db_pass=Agpyu12!0.213$

db_name=FZ

```

After that i had a permanent ssh connection using the user friend (which is quite better than the php shell).

The next part i did not do myself:

found the python script 

```{sh}
#!/usr/bin/python

import os

to_address = "admin1@friendzone.com"
from_address = "admin2@friendzone.com"

print "[+] Trying to send email to %s"%to_address

#command = ''' mailsend -to admin2@friendzone.com -from admin1@friendzone.com -ssl -port 465 -auth -smtp smtp.gmail.co-sub scheduled results email +cc +bc -v -user you -pass "PAPAP"'''

#os.system(command)

# I need to edit the script later
# Sam ~ python developer
```

the idea from here is that many of the commands running use os.py, which in this machine is writable and therefore, can be modified to do whatever we want it to do: this is known as module highjacking.
What the official writeup does is to add a job to the cron service that is running in the server to stablish a reverse shell as root. Insted i simply changed the friend user to be able to do sudo since i 
already had the password for that user.

