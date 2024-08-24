### PATH

The first thing to ever do is scan the website to find hidden content, therefore, let us do a [[website scan]]. After that i also decided to do a [[website code review]] to see if any important information was inside the website.

Another thing i noticed was that any .php file returns a different not found page than usual. There also seems to be a page called portafolio.php that is mentioned in a comment of index.php, however, searching for it returns 404. 

We still have no means of doing anything, so let us try to get more information though some [[main page nmap scripts]]. After this i decided:

- There is no useful information in the code
-  It seems i am not capable of identifying the framework this is using 

In the main page we can see a mention of the domain that the website is supposed to be called, board.htb. By trying [[subdomain enumeration]] i was able to find an admin login
### GENERIC INFORMATION

- The company is registered as Board.htb
- Information email is info@board.htb
- None of the forms in the default website actually send information to the server
- The site seems to be configured to not change behaviour depending on http method. It seems to allow OPTIONS,HEAD,GET,POST methods regardless