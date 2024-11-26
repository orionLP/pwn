```bash
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.11.38
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-11-07 12:44 EST
Nmap scan report for 10.10.11.38
Host is up (0.069s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
5000/tcp open  upnp

Nmap done: 1 IP address (1 host up) scanned in 15.17 seconds
```

## DISCOVERED 

- [[PORT 22]]: ssh server
- [[PORT 5000]]: upnp server (http server)