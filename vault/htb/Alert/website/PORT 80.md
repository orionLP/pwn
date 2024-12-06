## LANDING

The page seems to be a home brewed php site with minimal functionality. Specifically, the site allows to:

- View content uploaded by users (supposedly a markdown)
- Contact the site owners (ticket service)
- A donation service in order to donate to the web owners. 

The first step would be to map the application to know how it delivers functionality. For this let us first do some quick scans to verify we are not missing anything:

```bash
$ ffuf -w /snap/seclists/current/Discovery/Web-Content/CommonBackdoors-PHP.fuzz.txt -u http://alert.htb/FUZZ 

...

$ ffuf -w /snap/seclists/current/Discovery/Web-Content/common.txt -u http://alert.htb/FUZZ 

.hta                    [Status: 403, Size: 274, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 274, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 274, Words: 20, Lines: 10]
css                     [Status: 301, Size: 304, Words: 20, Lines: 10]
index.php               [Status: 302, Size: 659, Words: 123, Lines: 24]
messages                [Status: 301, Size: 309, Words: 20, Lines: 10]
server-status           [Status: 403, Size: 274, Words: 20, Lines: 10]
uploads                 [Status: 301, Size: 308, Words: 20, Lines: 10]

# let us also try another typical one (subdomains)

$ ffuf -w /snap/seclists/current/Discovery/DNS/subdomains-top1million-110000.txt -u http://10.129.244.229 -H "Host: FUZZ.alert.htb" -v > fuzzlog.log
```

It appears that there is a messages folder (maybie for the user given messages) and an uploads folder (maybie for the files uploaded by the user, even if it is temporary).

## WEB SITE STRUCTURE 

Any request to a domain of the server redirects us to index.php?page=alert. This is the first of the four main pages located at:

- http://alert.htb/index.php?page=alert : page to input document to see a markdown, The form that allows for user input is:

```html
<div class="form-container">
	<form action="visualizer.php" method="post" enctype="multipart/form-data">
		<input type="file" name="file" accept=".md" required>
		<input type="submit" value="View Markdown">
	</form>
</div>
```

Notice that the actual request is done at another endpoint [[visualizer.php]], and that we are restricted to sending (at least from the client side) a .md.
- http://alert.htb/index.php?page=donate : endpoint, which can be POST to with an amount of money given (nothing else so far)

- http://alert.htb/index.php?page=about : endpoint that returns static data about the company 

- http://alert.htb/index.php?page=contact : page to input a message to the admins. This is probably related to the [[messages]] endpoint.

```html 
<form action="contact.php" method="post">
	<input type="email" name="email" placeholder="Your email" required>
	<textarea name="message" placeholder="Your message" rows="4" required>   
	</textarea>
	<input type="submit" value="Send">
</form>
```

--- 

Which present the main functionality, although by themselves they do nothing other than presenting static data and forms

## ATTACK PLANNING

Given what we have seen, the most likely point of entry is the file upload functionality. It appears to work thusly:

The user gives a name of file and content -> the site stores that content in a file in /uploads with a hashed value -> when viewing the file, the site processes that file and 
displays it back to the user

It is also possible that we might use the sharing link to 

Let us see if we can break 1 or 2. [[attack]]
## GENERAL FUZZES

```bash
$ ffuf -w /snap/seclists/current/Discovery/Variables/secret-keywords.txt -u http://alert.htb//index.php?page=FUZZ

# nothing of interest

$ ffuf -w /snap/seclists/current/Discovery/Variables/awesome-environment-variable-names.txt -u http://alert.htb//index.php?page=FUZZ

$ ffuf -w /snap/seclists/current/Discovery/Web-Content/api/actions-lowercase.txt -u http://alert.htb//index.php?page=FUZZ -fs 689

alert                   [Status: 200, Size: 965, Words: 201, Lines: 29]
contact                 [Status: 200, Size: 999, Words: 191, Lines: 29]

$ ffuf -w /snap/seclists/current/Discovery/Web-Content/api/objects.txt -u http://alert.htb//index.php?page=FUZZ -fs 689

about                   [Status: 200, Size: 1045, Words: 187, Lines: 24]
alert                   [Status: 200, Size: 965, Words: 201, Lines: 29]
contact                 [Status: 200, Size: 999, Words: 191, Lines: 29]
donate                  [Status: 200, Size: 1115, Words: 292, Lines: 29]
messages                [Status: 200, Size: 660, Words: 123, Lines: 25]

```
