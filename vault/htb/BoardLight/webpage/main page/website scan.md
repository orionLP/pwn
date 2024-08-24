Let us try to get hidden content

### RESULTING SITEMAP

- /index.php
- /about.php
- /do.php
- /contact.php: contains three forms. All of the forms for this page contain no names (so no input is passed to the website)
- /portafolio.php: gives a file not found message (not the default given by Apache)
- /images: folder for images, (this location is forbidden by default)
- /css: folder for css (location forbidden by default)
- /js: folder for javascript (location forbidden by default)

### FFUF

```bash
$ ffuf -u http://10.10.11.11/FUZZ -w /snap/seclists/current/Discovery/Web-Content/directory-list-2.3-big.txt 


        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.11/FUZZ
 :: Wordlist         : FUZZ: /snap/seclists/current/Discovery/Web-Content/directory-list-2.3-big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

images                  [Status: 301, Size: 311, Words: 20, Lines: 10]
#                       [Status: 200, Size: 15949, Words: 6243, Lines: 518]
                        [Status: 200, Size: 15949, Words: 6243, Lines: 518]
# or send a letter to Creative Commons, 171 Second Street, [Status: 200, Size: 15949, Words: 6243, Lines: 518]
#                       [Status: 200, Size: 15949, Words: 6243, Lines: 518]
# Suite 300, San Francisco, California, 94105, USA. [Status: 200, Size: 15949, Words: 6243, Lines: 518]
# This work is licensed under the Creative Commons [Status: 200, Size: 15949, Words: 6243, Lines: 518]
# directory-list-2.3-big.txt [Status: 200, Size: 15949, Words: 6243, Lines: 518]
# on at least 1 host    [Status: 200, Size: 15949, Words: 6243, Lines: 518]
#                       [Status: 200, Size: 15949, Words: 6243, Lines: 518]
# Attribution-Share Alike 3.0 License. To view a copy of this [Status: 200, Size: 15949, Words: 6243, Lines: 518]
#                       [Status: 200, Size: 15949, Words: 6243, Lines: 518]
# Priority-ordered case-sensitive list, where entries were found [Status: 200, Size: 15949, Words: 6243, Lines: 518]
# license, visit http://creativecommons.org/licenses/by-sa/3.0/ [Status: 200, Size: 15949, Words: 6243, Lines: 518]
# Copyright 2007 James Fisher [Status: 200, Size: 15949, Words: 6243, Lines: 518]
css                     [Status: 301, Size: 308, Words: 20, Lines: 10]
js                      [Status: 301, Size: 307, Words: 20, Lines: 10]
                        [Status: 200, Size: 15949, Words: 6243, Lines: 518]
server-status           [Status: 403, Size: 276, Words: 20, Lines: 10]
:: Progress: [1273832/1273832] :: Job [1/1] :: 579 req/sec :: Duration: [0:36:38] :: Errors: 0 ::



$ ffuf -u http://10.10.11.11/FUZZ -w /snap/seclists/current/Discovery/Web-Content/Common-PHP-Filenames.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.11/FUZZ
 :: Wordlist         : FUZZ: /snap/seclists/current/Discovery/Web-Content/Common-PHP-Filenames.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

index.php               [Status: 200, Size: 15949, Words: 6243, Lines: 518]
contact.php             [Status: 200, Size: 9426, Words: 3295, Lines: 295]
about.php               [Status: 200, Size: 9098, Words: 3084, Lines: 281]



$ ffuf -u http://10.10.11.11/FUZZ -w /snap/seclists/current/Discovery/Web-Content/CommonBackdoors-PHP.fuzz.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.11/FUZZ
 :: Wordlist         : FUZZ: /snap/seclists/current/Discovery/Web-Content/CommonBackdoors-PHP.fuzz.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

:: Progress: [422/422] :: Job [1/1] :: 211 req/sec :: Duration: [0:00:02] :: Errors: 0 ::



$ ffuf -u http://10.10.11.11/FUZZ -w /snap/seclists/current/Discovery/Web-Content/PHP.fuzz.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.11/FUZZ
 :: Wordlist         : FUZZ: /snap/seclists/current/Discovery/Web-Content/PHP.fuzz.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

:: Progress: [104/104] :: Job [1/1] :: 0 req/sec :: Duration: [0:00:00] :: Errors: 0 ::



$ ffuf -u http://10.10.11.11/images/FUZZ -w /snap/seclists/current/Discovery/Web-Content/directory-list-2.3-big.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.11/images/FUZZ
 :: Wordlist         : FUZZ: /snap/seclists/current/Discovery/Web-Content/directory-list-2.3-big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

# license, visit http://creativecommons.org/licenses/by-sa/3.0/ [Status: 403, Size: 276, Words: 20, Lines: 10]
#                       [Status: 403, Size: 276, Words: 20, Lines: 10]
#                       [Status: 403, Size: 276, Words: 20, Lines: 10]
# on at least 1 host    [Status: 403, Size: 276, Words: 20, Lines: 10]
#                       [Status: 403, Size: 276, Words: 20, Lines: 10]
#                       [Status: 403, Size: 276, Words: 20, Lines: 10]
# This work is licensed under the Creative Commons [Status: 403, Size: 276, Words: 20, Lines: 10]
# or send a letter to Creative Commons, 171 Second Street, [Status: 403, Size: 276, Words: 20, Lines: 10]
                        [Status: 403, Size: 276, Words: 20, Lines: 10]
# Suite 300, San Francisco, California, 94105, USA. [Status: 403, Size: 276, Words: 20, Lines: 10]
# Copyright 2007 James Fisher [Status: 403, Size: 276, Words: 20, Lines: 10]
# Attribution-Share Alike 3.0 License. To view a copy of this [Status: 403, Size: 276, Words: 20, Lines: 10]
# Priority-ordered case-sensitive list, where entries were found [Status: 403, Size: 276, Words: 20, Lines: 10]
# directory-list-2.3-big.txt [Status: 403, Size: 276, Words: 20, Lines: 10]
                        [Status: 403, Size: 276, Words: 20, Lines: 10]
:: Progress: [1273832/1273832] :: Job [1/1] :: 752 req/sec :: Duration: [0:28:12] :: Errors: 0 ::



$ ffuf -u http://10.10.11.11/FUZZ -w /snap/seclists/current/Discovery/Web-Content/common.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.11/FUZZ
 :: Wordlist         : FUZZ: /snap/seclists/current/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

.hta                    [Status: 403, Size: 276, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 276, Words: 20, Lines: 10]
css                     [Status: 301, Size: 308, Words: 20, Lines: 10]
images                  [Status: 301, Size: 311, Words: 20, Lines: 10]
index.php               [Status: 200, Size: 15949, Words: 6243, Lines: 518]
js                      [Status: 301, Size: 307, Words: 20, Lines: 10]
server-status           [Status: 403, Size: 276, Words: 20, Lines: 10]



$ ffuf -u http://10.10.11.11/FUZZ -w /snap/seclists/current/Discovery/Web-Content/dirsearch.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.11/FUZZ
 :: Wordlist         : FUZZ: /snap/seclists/current/Discovery/Web-Content/dirsearch.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

.                       [Status: 200, Size: 15949, Words: 6243, Lines: 518]
.htaccess.inc           [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess-local         [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess.old           [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess.bak           [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess-dev           [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess.sample        [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess-marco         [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccessBAK            [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess.orig          [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess.txt           [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess.save          [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccessOLD2           [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess.bak1          [Status: 403, Size: 276, Words: 20, Lines: 10]
.htm                    [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccessOLD            [Status: 403, Size: 276, Words: 20, Lines: 10]
.htaccess/              [Status: 403, Size: 276, Words: 20, Lines: 10]
.html                   [Status: 403, Size: 276, Words: 20, Lines: 10]
.htpasswd-old           [Status: 403, Size: 276, Words: 20, Lines: 10]
.htpasswd.inc           [Status: 403, Size: 276, Words: 20, Lines: 10]
.httr-oauth             [Status: 403, Size: 276, Words: 20, Lines: 10]
.htpasswd.bak           [Status: 403, Size: 276, Words: 20, Lines: 10]
.htpasswd/              [Status: 403, Size: 276, Words: 20, Lines: 10]
.php                    [Status: 403, Size: 276, Words: 20, Lines: 10]
                        [Status: 200, Size: 15949, Words: 6243, Lines: 518]
about.php               [Status: 200, Size: 9098, Words: 3084, Lines: 281]
contact.php             [Status: 200, Size: 9426, Words: 3295, Lines: 295]
css                     [Status: 301, Size: 308, Words: 20, Lines: 10]
css/                    [Status: 403, Size: 276, Words: 20, Lines: 10]
icons/                  [Status: 403, Size: 276, Words: 20, Lines: 10]
images                  [Status: 301, Size: 311, Words: 20, Lines: 10]
images/                 [Status: 403, Size: 276, Words: 20, Lines: 10]
index.php               [Status: 200, Size: 15949, Words: 6243, Lines: 518]
js/                     [Status: 403, Size: 276, Words: 20, Lines: 10]
js                      [Status: 301, Size: 307, Words: 20, Lines: 10]


$ ffuf -u http://10.10.11.11/FUZZ -w /snap/seclists/current/Discovery/Web-Content/big.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.11/FUZZ
 :: Wordlist         : FUZZ: /snap/seclists/current/Discovery/Web-Content/big.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

.htaccess               [Status: 403, Size: 276, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 276, Words: 20, Lines: 10]
css                     [Status: 301, Size: 308, Words: 20, Lines: 10]
images                  [Status: 301, Size: 311, Words: 20, Lines: 10]
js                      [Status: 301, Size: 307, Words: 20, Lines: 10]
server-status           [Status: 403, Size: 276, Words: 20, Lines: 10]

```
### NIKTO

```bash
$ nikto -host http://10.10.11.11/

- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          10.10.11.11
+ Target Hostname:    10.10.11.11
+ Target Port:        80
+ Start Time:         2024-08-22 11:45:48 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ The anti-clickjacking X-Frame-Options header is not present.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ DEBUG HTTP verb may show server debugging information. See http://msdn.microsoft.com/en-us/library/e8z01xdh%28VS.80%29.aspx for details.
+ 6544 items checked: 0 error(s) and 2 item(s) reported on remote host
+ End Time:           2024-08-22 11:55:08 (GMT2) (560 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

