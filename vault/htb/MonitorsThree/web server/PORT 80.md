### FIRST CONTACT

The things that stand out the most are a [[login]] and [[forgot password]] functionality. 

### SUBDOMAIN ENUMERATION

```bash
$ ffuf -u http://10.10.11.30 -H "Host: FUZZ.monitorsthree.htb" -w /snap/seclists/current/Discovery/DNS/subdomains-top1million-110000.txt 

...

cacti                   [Status: 302, Size: 0, Words: 1, Lines: 1]
```

Turns out there is a subdomain in this server used for network administration. Let us use [[cacti]].