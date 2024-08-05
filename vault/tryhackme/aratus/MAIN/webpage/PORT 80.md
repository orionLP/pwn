### Primary info
- It's **Apache httpd 2.4.6** 
- Running on **CentOS** 
- Allowed methods are **GET**, **HEAD**, **POST**, **OPTIONS**, **TRACE**
- Of these **TRACE** is insecure 
- webmaster seems to be default user webmaster@example.com
### USES 
- bootstrap v3.1.1
- openssl
### TESTED
- version for known vulns : 
	- Not found in : exploit db, metasploit
- Default configurations: 
- TRACE:  
- This is something i did have to look up but simeon does have a part of the webpage for himself called [[simeon's page]]
### FUZZES 
```bash
$ ffuf -X GET -u http://10.10.149.74/FUZZ -w ../../Tools/SecLists/Discovery/Web-Content/directory-list-2.3-big.txt  

Nothing to report
```

```bash 
$ ffuf -X GET -u http://10.10.149.74/FUZZ -w ../../Tools/SecLists/Discovery/Web-Content/common.txt  

.hta                    [Status: 403, Size: 206, Words: 15, Lines: 9, Duration: 2756ms]
cgi-bin/                [Status: 403, Size: 210, Words: 15, Lines: 9, Duration: 47ms]
.htpasswd               [Status: 403, Size: 211, Words: 15, Lines: 9, Duration: 3765ms]
.htaccess               [Status: 403, Size: 211, Words: 15, Lines: 9, Duration: 4733ms]

```

Found noindex/css/bootstrap.min.css
Found images/

### INFO
- Saw nothing in the default communication with the server