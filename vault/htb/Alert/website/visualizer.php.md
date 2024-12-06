## BASIC STRUCTURE

The basic structure of a request to this endpoint is as such:

```http
POST /visualizer.php HTTP/1.1
Host: alert.htb
Content-Length: 189
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://alert.htb
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary6DFgpsw4tsTC1xwX
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://alert.htb/index.php?page=alert
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close

------WebKitFormBoundary6DFgpsw4tsTC1xwX
Content-Disposition: form-data; name="file"; filename="epic.md"
Content-Type: text/markdown

epic

------WebKitFormBoundary6DFgpsw4tsTC1xwX--
```

And a basic response would be:

```http
HTTP/1.1 200 OK
Date: Tue, 26 Nov 2024 19:48:17 GMT
Server: Apache/2.4.41 (Ubuntu)
Vary: Accept-Encoding
Content-Length: 796
Connection: close
Content-Type: text/html; charset=UTF-8

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alert - Markdown Viewer</title>
    <link rel="stylesheet" href="css/style.css">
    <style>
        .share-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: rgb(100, 100, 100);
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <p>&lt;?php echo "say hello to my little friend" ?&gt;</p><a class="share-button" href="http://alert.htb/visualizer.php?link_share=67462601009b77.99811164.md" target="_blank">Share Markdown</a></body>
</html>
```

One thing to notice is the link to share the file (using it just returns the same page). However if we now use the filename given by the app and use it in /uploads we now get that this file exists. So we have access to files within the uploads. If we actually do a mini google search we find that a possible hashing structure for the name we are given is:

`67474836d97689.98811228 - Possible algorithms: Base64(unhex(MD5($plaintext)))`

It is worth noticing that **the files are stored as they are and then they are processed by the visualiser** to create a markdown in html. It also worth noticing that there are filters that prevent the name of the file from being things different than .md.

## FUZZES

```bash
$ ffuf -w /snap/seclists/current/Discovery/Web-Content/directory-list-2.3-big.txt -u http://alert.htb/uploads/FUZZ
```

```bash
┌──(kali㉿kali)-[~]
└─$ nikto -url http://alert.htb/uploads
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.129.172.112
+ Target Hostname:    alert.htb
+ Target Port:        80
+ Start Time:         2024-11-27 13:19:41 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ /uploads/: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /uploads/: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.41 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS: Allowed HTTP Methods: GET, POST, OPTIONS, HEAD .
```