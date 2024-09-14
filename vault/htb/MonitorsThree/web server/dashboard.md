In this case it turns out there is little in this part that seems interactive at first, as most information is hardcoded into the webpage. This part has a the following pages for administration:

- dashboard
- tasks
- invoices
- users
- customers
- changelog

### FUZZES

```bash
$ ffuf -u http://monitorsthree.htb/admin/FUZZ -w /snap/seclists/current/Discovery/Web-Content/directory-list-2.3-big.txt 
#                       [Status: 403, Size: 162, Words: 4, Lines: 8]
assets                  [Status: 301, Size: 178, Words: 6, Lines: 8]
                        [Status: 403, Size: 162, Words: 4, Lines: 8]
:: Progress: [1273832/1273832] :: Job [1/1] :: 528 req/sec :: Duration: [0:40:12] :: Errors: 0 ::

```