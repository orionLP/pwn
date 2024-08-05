## Apache httpd 2.4.18 ((Ubuntu)) Info

Usable methods are:
- POST
- GET
- HEAD
- OPTIONS

The first page is the default one for **Apache 2 server**.

## Attempted 

- No public exploit in **exploit db** except for **Local privilege escalation**
- Attempted default directories **robots.txt** and **sitemap.xml** : nothing
- Something i did not notice and i should have is that the default page for Apache has the user jessie written on it (would have saved me more time than i am willing to admit)
-  # FFUF: directory discovery with:
			`Folder /`
			`wordlists:`
	- /SecLists/Discovery/Web-Content/directory-list-2.3-big.txt
			`The results are:`
	- [[sitemap]] : code 200
	- server-status : code 403
	