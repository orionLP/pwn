
## SCANS

---

```bash
$ sudo nmap -sS -sV -sC -p- 10.10.196.61

Starting Nmap 7.80 ( https://nmap.org ) at 2024-05-13 19:19 CEST
Nmap scan report for 10.10.196.61
Host is up (0.043s latency).
Not shown: 65531 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
3306/tcp open  mysql   MySQL 5.7.40
| mysql-info: 
|   Protocol: 10
|   Version: 5.7.40
|   Thread ID: 3
|   Capabilities flags: 65535
|   Some Capabilities: LongColumnFlag, Support41Auth, DontAllowDatabaseTableColumn, Speaks41ProtocolOld, ODBCClient, SupportsCompression, ConnectWithDatabase, InteractiveClient, IgnoreSigpipes, SwitchToSSLAfterHandshake, FoundRows, Speaks41ProtocolNew, IgnoreSpaceBeforeParenthesis, LongPassword, SupportsLoadDataLocal, SupportsTransactions, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults
|   Status: Autocommit
|   Salt: kX\x14y=`i\x16s\x02Kg3\x18G%z\x08!\x05
|_  Auth Plugin Name: mysql_native_password
5000/tcp open  http    Docker Registry (API: 2.0)
|_http-title: Site doesn't have a title.
8080/tcp open  http    Node.js (Express middleware)
|_http-title: Login
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 77.82 seconds
```
## NOTES

---

The services found are:
- SSH in [[PORT 22]]
- MYSQL in [[PORT 3306]]
- HTTP in [[PORT 5000]]
- HTTP in [[PORT 8080]]

