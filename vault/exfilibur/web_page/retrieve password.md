## NICE

When trying to get the reset for **admin** we get:

```txt
Error sending email in SendMailMessage: Failure sending mail. Unable to connect to the remote server A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond 209.85.203.109:587
```

-> at least and *admin* account exists.
-> also what is this ip? it turns out it is a mail server for smtp -> actually it seems to change the ip, but the port is the same (74.125.193.108:587)
And afterwards by trying other things: User not found

## FUZZES

```bash
                      
┌──(kali㉿kali)-[~]
└─$ ffuf -u http://10.10.91.177/blog/Account/login.aspx?ReturnURL=%2fblog%2fadmin%2f -X POST -d '{"ctl00$MainContent$LoginUser$UserName":"admin","ctl00$MainContent$LoginUser$Password":"FUZZ","ctl00$MainContent$LoginUser$LoginButton":"Log+in"}' -w /usr/share/seclists/Passwords/darkweb2017-top10000.txt -fr 'Login ' 

```