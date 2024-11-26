## MAIN

Starting from the top we are introduced to a an apache 2 ubuntu default page. From here we need to be able to see what capabilities does this server offer. 

## FUZZES 

By doing simple fuzzes to the website we can get the following results

```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -u http://help.htb/FUZZ    

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://help.htb/FUZZ
 :: Wordlist         : FUZZ: /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________
support                 [Status: 301, Size: 306, Words: 20, Lines: 10, Duration: 126ms]
javascript              [Status: 301, Size: 309, Words: 20, Lines: 10, Duration: 108ms]
```

So there is a [[support webpage]]