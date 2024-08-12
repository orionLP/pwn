## Password reset

in http://usage.htb/forget-password giving a random email results in the server simply saying that it does not match any records. Giving the typical 

![[Screenshot from 2024-08-08 09-53-33.png]]

This part of the site is vulnerable to SQLI, so we can probably work out something from there. 

## Behaviour of the injection

- giving error inducing code results in a 500 error
- giving a false statement returns a "email not found in our records statement"
- giving a true statement returns a "we have mailed your password reset link to \<user\>"

By trial and error i found the following columns:

![[Screenshot from 2024-08-08 10-05-43.png]]

Since this does not trigger an error we can assume that the column password does exist in the table we are injecting to. Trying other things found the columns:

- **email**
- **password**

Since we get a binary answer depending on the truthfulness of the statement we can try blind binary sql injection to get usernames and passwords.

![[Screenshot from 2024-08-08 10-19-52.png]]

After running a script to get the passwrod we can 
see that the password is hashed.

```bash
python3 weapon1.py 

Password for admin@usage.htb is $2y$10$dVAYyH/Wj6ri3oFRIC0w9OHkubPpMsyVAeB/Ga/ews2GWpi0DawV. :) 
```

While also trying to [[crack]] it i also decided to ennumerate the [[database]].