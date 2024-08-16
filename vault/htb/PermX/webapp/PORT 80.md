# RECON

### VIRTUAL HOSTS

By using ffuf we can ennumerate virtual hosts 

```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -u http://permx.htb/ -H "Host: FUZZ.permx.htb" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -fc 302

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://permx.htb/
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.permx.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 302
________________________________________________

www                     [Status: 200, Size: 36182, Words: 12829, Lines: 587, Duration: 70ms]
lms                     [Status: 200, Size: 19347, Words: 4910, Lines: 353, Duration: 74ms]
```

This way we already have 2 subdomains we can target. **www** seems to be a copy of the baseline domain, while **[[lms]]** seems to direct us to a login page.
