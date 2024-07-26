## FUZZES

```bash
ffuf -u http://10.10.91.177/FUZZ -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-big.txt -X GET -v

[Status: 200, Size: 22701, Words: 4407, Lines: 314, Duration: 46ms]
| URL | http://10.10.91.177/Blog
    * FUZZ: Blog
```

## /blog & /Blog

-> **Normal subdirectories**

- **/blog/archive**: Where posted articles are presented
- **/blog/post**: Place of the actual articles
- **/blog/contact**: Place to send mail to the devs
- **/blog/Account/login.aspx?ReturnURL=/blog/admin/**: Place to log into the accounts, made with blogengine.net -> i suppose then that **/blog/admin** is the administration site. -> also given when searching **/blog/admin**.
- **/blog/Account/password-retrieval.aspx** to retrieve lost passwords
- **/blog/search?q=s**: to search for articles

So far we see a way to [[login]], [[retrieve password]], [[search blogs]], and we can also [[send mail]]

-> **In general places with no access** 

- **/blog/Account**

-> **Sites that crash the server**

- **/blog/default**

I have noticed that the server seems to do a little of fuzzy matching for directories, as some baddly worded or slightly changed directory leads to the same place.

## KNOWN EXPLOITS

- blogengine.net: Seems there are both for path traversal and remote code execution. For versions below 3.3.6 this is done when editing a post and uploading a file (so still not able to do that)
- Nothing for:SyntaxHighlighter, jquery (things like uploadify, which for now i do not know), xregexp, bootstrap

## BLOGENGINE

Actually, in a little part of the html page we are given the following information:

```html
<a href="https://blogengine.io/" target="_blank" title="BlogEngine.NET 3.3.7.0">BlogEngine.NET</a>
```

So now we know that the server is using blogengine.net version 3.3.7