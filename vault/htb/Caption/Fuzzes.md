### AGAINST PORT 80

```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -u http://10.10.11.33 -H "Host: FUZZ.caption.htb" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -fc 301

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.33
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.caption.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 301
________________________________________________

:: Progress: [114441/114441] :: Job [1/1] :: 706 req/sec :: Duration: [0:02:15] :: Errors: 0 ::

```

### AGAINST PORT 8080

```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -u http://10.10.11.33:8080 -H "Host: FUZZ.caption.htb" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -fw 1180

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.33:8080
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.caption.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response words: 1180
________________________________________________

:: Progress: [114441/114441] :: Job [1/1] :: 196 req/sec :: Duration: [0:09:31] :: Errors: 0 ::
                                                                                                      
```