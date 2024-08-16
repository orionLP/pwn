### FUZZ

```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -u http://lms.permx.htb/FUZZ -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt  

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://lms.permx.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

#                       [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 131ms]
# Priority-ordered case-sensitive list, where entries were found [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 137ms]
# Attribution-Share Alike 3.0 License. To view a copy of this [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 142ms]
#                       [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 137ms]
# This work is licensed under the Creative Commons [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 147ms]
# Suite 300, San Francisco, California, 94105, USA. [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 148ms]
# or send a letter to Creative Commons, 171 Second Street, [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 149ms]
# on at least 1 host    [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 152ms]
# Copyright 2007 James Fisher [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 156ms]
#                       [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 172ms]
# license, visit http://creativecommons.org/licenses/by-sa/3.0/ [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 168ms]
                        [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 175ms]
# directory-list-2.3-big.txt [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 176ms]
main                    [Status: 301, Size: 313, Words: 20, Lines: 10, Duration: 57ms]
web                     [Status: 301, Size: 312, Words: 20, Lines: 10, Duration: 77ms]
#                       [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 851ms]
documentation           [Status: 301, Size: 322, Words: 20, Lines: 10, Duration: 66ms]
bin                     [Status: 301, Size: 312, Words: 20, Lines: 10, Duration: 40ms]
src                     [Status: 301, Size: 312, Words: 20, Lines: 10, Duration: 63ms]
app                     [Status: 301, Size: 312, Words: 20, Lines: 10, Duration: 77ms]
vendor                  [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 40ms]
LICENSE                 [Status: 200, Size: 35147, Words: 5836, Lines: 675, Duration: 36ms]
plugin                  [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 45ms]
certificates            [Status: 301, Size: 321, Words: 20, Lines: 10, Duration: 57ms]
                        [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 56ms]
custompages             [Status: 301, Size: 320, Words: 20, Lines: 10, Duration: 53ms]
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 48ms]

```

With this we already have interesting folders and files we might like

```bash
┌──(root㉿kali)-[~]
└─# ffuf -u http://lms.permx.htb/FUZZ -w file

# all redirects to the login page, where file contains common paths to chamilio code
```
### SCAN

Also tried out nikto, which found some interesting results:

```bash
┌──(kali㉿kali)-[~]
└─$ nikto -url lms.permx.htb
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.11.23
+ Target Hostname:    lms.permx.htb
+ Target Port:        80
+ Start Time:         2024-08-15 03:17:36 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache/2.4.52 (Ubuntu)
+ /: Retrieved x-powered-by header: Chamilo 1.
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /bin/: Directory indexing found.
+ /robots.txt: Entry '/whoisonline.php' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/whoisonlinesession.php' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /app/: Directory indexing found.
+ /robots.txt: Entry '/app/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/license.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/plugin/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/main/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/bin/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /vendor/: Directory indexing found.
+ /robots.txt: Entry '/vendor/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/documentation/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: contains 12 entries which should be manually viewed. See: https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt
+ Apache/2.4.52 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /web.config: ASP config file is accessible.
+ /web/: Directory indexing found.
+ /app/: This might be interesting.
+ /bin/: This might be interesting.
+ /src/: Directory indexing found.
+ /web/: This might be interesting.
+ /license.txt: License file found may identify site software.
+ /composer.json: PHP Composer configuration file reveals configuration information. See: https://getcomposer.org/
+ /composer.lock: PHP Composer configuration file reveals configuration information. See: https://getcomposer.org/
+ /README.md: Readme Found.
+ 8872 requests: 4 error(s) and 28 item(s) reported on remote host
+ End Time:           2024-08-15 03:59:39 (GMT-4) (596 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

One of the first things i did was try out the  robots.txt file:

```txt
#
# robots.txt
#
# This file is to prevent the crawling and indexing of certain parts
# of your site by web crawlers and spiders run by sites like Yahoo!
# and Google. By telling these "robots" where not to go on your site,
# you save bandwidth and server resources.
#
#
# For more information about the robots.txt standard, see:
# http://www.robotstxt.org/wc/robots.html
#
# For syntax checking, see:
# http://www.sxw.org.uk/computing/robots/check.html

User-Agent: *

# Directories

Disallow: /app/
Disallow: /bin/
Disallow: /documentation/
Disallow: /home/
Disallow: /main/
Disallow: /plugin/
Disallow: /tests/
Disallow: /vendor/

# Files
Disallow: /license.txt
Disallow: /README.txt
Disallow: /whoisonline.php
Disallow: /whoisonlinesession.php
```

Actually, inside of src we might have a lot of useful information related to how passwords are setted, or resetting passwords

**Cassification of directories/files**

- /**src**: views and code related to handling the webpage
- /web: fonts and other formatting information

- /web.config: file for url rewriting
- /whoisonline.php: list of online users (non are logged )
- /whoisonlinesession.php: sessions of those users (not allowed without admin)
- /composer.lock: for depedencies
- /composer.json: for dependencies

- /vendor: third party software
- /tests: not found 
- /plugin: nothing in there
- /main: in chamilio contains website functionality related information, but it is blocked by login
- /home: not found 
- /documentation: the documentation of the chamilio installation (with examples)
- /bin: contains a single doctrine console file (not working though)
- /**app**: application related information such as configuration files such as 
  `database_name: chamilo111`
  `database_user: root`
  `database_password: root`
  Other directories in the webpage did not seem so useful
### Input functionalities

It is also time to test the various inputs this website has to offer

**Site login**

Does not seem sql injectable 

```bash
┌──(kali㉿kali)-[~]
└─$ sqlmap -r change_email --risk 3 --level 5 -p "user"  --batch
```

Tried brute forcing with hydra with following lists:
- rockyou.txt -> noluck


**Password reset**

Does not seem sql injectable

```bash
┌──(kali㉿kali)-[~]
└─$ sqlmap -r  login --risk 3 --level 5 -p "login,password,submitAuth" --batch
```

### Public vulns 

Turns out this is one of the oldest versions of this software, which is more than vulnerable to remote code execution . [[RCE]] bois :) 

### GENERAL WEBSITE INFORMATION 

- Website uses Chamilo 1.11 
- Systems with chmilio work with a ftp/sftp server and a sql server
- The admin is Davis Miller with mail admin@permx.htb, and username admin