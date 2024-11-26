In this case we find a simple login page with little else. Since the page seems custom made, injection might be an entry point to gather more information

### SQL INJECTION

```bash
┌──(kali㉿kali)-[~]
└─$ sqlmap -r request -p username,password

... # nothing found 
```