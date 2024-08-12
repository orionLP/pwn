**DOMAIN**: admin.usage.htb

The default page is simply a login site for the admin to log in, giving random credentials results in a "incorrect login".

The login requires a username and a password

![[Screenshot from 2024-08-08 09-33-26.png]]

The website uses larvel-admin, an administrative interface to create website backends. The default credentials are admin:admin, tried those but the credentials do not match, so they have been probably changed

## POST FINDING CREDENTIALS

The credentials to enter are:

- user: admin
- password: whatever1

## ENNUMERATING SERVER VULNS 

- PHP 8.1.2 : none found 
- Laravel 10.8.0: 
	- Laravel is not in debug mode so CVE-2021-3129 does not apply 
	 Did not find anything in hacktricks
- nginx/1.18.0 : Does have some but i don't think i can exploit them
- The environment is the local one
- laravel-admin: filter bypass that can lead to uploading php files but this is 1.8.18 -> let's try anyway ? -> i can bypass the filter and get remote code execution so we are good to go boys. 

![[Screenshot from 2024-08-09 18-52-00.png]]

The CVE is CVE-2023-24249, and i found a proof of concept in https://flyd.uk/post/cve-2023-24249/. 

In my case let us just bring up pentest.

After a while we get a shell to user [[dash]] :)

