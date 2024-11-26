### SCANS

```bash
┌──(kali㉿kali)-[~]
└─$ nmap 10.10.11.33 -p - 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-09-22 10:34 EDT
Nmap scan report for 10.10.11.33
Host is up (0.080s latency).
Not shown: 65532 closed tcp ports (conn-refused)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
8080/tcp open  http-proxy

Nmap done: 1 IP address (1 host up) scanned in 32.92 seconds
```
### OPEN PORTS 
- [[PORT 22]]: ssh server
- [[PORT 80]]: http server
- [[PORT 8080]]: http server behind a proxy (probably load balancer)

### OTHERS 
- [[Fuzzes]]
