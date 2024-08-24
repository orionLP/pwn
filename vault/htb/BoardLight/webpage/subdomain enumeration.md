### FFUF

In this case i used ffuf to change the host header of the requests:

```bash
 ffuf -u http://10.10.11.11/ -H "Host: FUZZ.board.htb" -w /snap/seclists/current/Discovery/DNS/subdomains-top1million-110000.txt -fl 518

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.11.11/
 :: Wordlist         : FUZZ: /snap/seclists/current/Discovery/DNS/subdomains-top1million-110000.txt
 :: Header           : Host: FUZZ.board.htb
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
 :: Filter           : Response lines: 518
________________________________________________

crm                     [Status: 200, Size: 6360, Words: 397, Lines: 150]
```

Thus we can now see the [[login page]].