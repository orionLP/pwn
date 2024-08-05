The default ubuntu apache 2 page appears when we decide to check out the page.

## FUZZES

First thing ever thought of:

```bash
┌──(root㉿kali)-[~]
└─# ffuf -u http://10.10.215.152:80/FUZZ -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt 
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 79ms]

# Does not seem to do the trick :<
```
