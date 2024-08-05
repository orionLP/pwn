## PATHS

```txt
/users : POST: sends data to create account
/users/sing_in : to log into an account
/users/sign_up : to create an account
/users/cancel
/users/edit
/assets/ : images ?
/assets/application
/assets/styles
/public
```

## SETUP

### /USERS/SING_UP
Weird thing: the variables in the user creation account are:
- user[avatar]
- user[email]
- user[password]
- user[password_confirmation]

inside the form there's a hidden input called **authenticity_token** with value **value="8hnLNIBMdYqYPqIk1-jQbnOH7aNFaWmn3W69ncFU--3aQf9b-LNIyNKMzFC3SHvWM-FxNEN7std5f6M8EkULGg"**
### /USERS/SING_IN

Always seems like there is this an auth token
- authenticity_token : kK9dznztXIdLW6MsSZoLY7eazLGYLPM_WDJJ_BZXSavMzGA0l-YSvtirkUy_6_oHjHpbBmZyaKNwdEiQbpuuww

### After creation of a user

mail: hello@gmail.com
pass: aaaaaa

A cookie for a session is given:

```txt
_emp_man_session=O1D2hx3Uho1HJ9hSR0fp8n2Nx6lyxW%2BpcYD%2FffZ1CpH2GO8pW6m9rh6WbDkt8yOnR51fTykWl4Me52vI5NdifJ58Ze%2BtzvxdhEVxZbDlpi2dw%2FY5IZcM%2FPWALF9dfEduenKapWkoGu4S4LRVcvV25cdmtrqSgNH1oAdM6xqZyvy51ycFZvx2sM%2B3uKNIno0zIrHsoR5mGTiBmNvKT6AYNNuE1plCRYR0mAvvdjtohLviJGRfiOwtcgEZFDqIGZ0rCb7JPIXBAvlgwpf%2B6knkqPNUNB4XwRfhvC1STZ7JZvDBPTt6YpC6VbJT7v5z63kC0nIjGpNVPgIFTXVkumKmdo9RDfs7LMLBxLfgvcNRxeMlHYvcVP14E8OuCYyh3%2ByfqPJzp1PnOb8DaXw5XqYRVH9NvIf29A6FTWnLp2YbcNErtgeRmlxJJ3ehgAgud6qPOlCGZRHUSzhFJCwevAe%2B%2BqKfBeEiIUKVdY8RG%2BIw%2BFYc9qDMxo04dQjOyy%2BmBBuN2rb%2BdKjVDjzH5%2FmMuHkSomDxwcV2xbuL3%2FkxfA%3D%3D--XIL9%2BET5S27Iq41R--%2BTTF7Kzp0k5DrrEYZ7%2B4Cw%3D%3D; path=/; HttpOnly; SameSite=Lax
```

death by glamour
### GENERAL

After sign in this file is given 

http://site.empman.thm/assets/application-6868713675c1621745555733b398a9765cdfe3820d4893477a7738b64d5f94b7.js




I felt i needed to be more granular here so here it goes:
- [[site]]
- [[sign_up]]
- [[sign_in]]
- [[new_password]]

EmpMan | DeezBytez's Little website for managing employees.


## RULED OUT

- First page containing personal information
- First page nothing out of the ordinary with the communication

- If account exists in sign up it will be sent back with an account already exists


## ANSWER 

After actually spending countless hours with this i decided to look up the answer and as it turns out the answer was to do subdomain enumeration:

```bash
$ ffuf -u http://10.10.77.227 -H "Host: FUZZ.empman.thm" -w ./Tools/SecLists/Discovery/DNS/subdomains-top1million-5000.txt 


        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.77.227
 :: Wordlist         : FUZZ: ./Tools/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
 :: Header           : Host: FUZZ.empman.thm
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

backup                  [Status: 200, Size: 255, Words: 56, Lines: 8]
site                    [Status: 200, Size: 4607, Words: 839, Lines: 97]
:: Progress: [4989/4989] :: Job [1/1] :: 831 req/sec :: Duration: [0:00:06] :: Errors: 0 ::
```

After this we gain access to [[backup]]