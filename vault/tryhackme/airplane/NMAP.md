## SCANS

```bash
# Nmap 7.80 scan initiated Tue Jun 25 16:51:21 2024 as: nmap -p - -sS -sC -sV -oN ./ctf/airplane/scan1.out 10.10.29.234
Nmap scan report for 10.10.29.234
Host is up (0.059s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
6048/tcp open  x11?
8000/tcp open  http-alt Werkzeug/3.0.2 Python/3.8.10
| fingerprint-strings: 
|   FourOhFourRequest: 
|     HTTP/1.1 404 NOT FOUND
|     Server: Werkzeug/3.0.2 Python/3.8.10
|     Date: Tue, 25 Jun 2024 14:53:51 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 207
|     Connection: close
|     <!doctype html>
|     <html lang=en>
|     <title>404 Not Found</title>
|     <h1>Not Found</h1>
|     <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
|   GetRequest: 
|     HTTP/1.1 302 FOUND
|     Server: Werkzeug/3.0.2 Python/3.8.10
|     Date: Tue, 25 Jun 2024 14:53:46 GMT
|     Content-Type: text/html; charset=utf-8
|     Content-Length: 269
|     Location: http://airplane.thm:8000/?page=index.html
|     Connection: close
|     <!doctype html>
|     <html lang=en>
|     <title>Redirecting...</title>
|     <h1>Redirecting...</h1>
|     <p>You should be redirected automatically to the target URL: <a href="http://airplane.thm:8000/?page=index.html">http://airplane.thm:8000/?page=index.html</a>. If not, click the link.
|   Socks5: 
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
|     "http://www.w3.org/TR/html4/strict.dtd">
|     <html>
|     <head>
|     <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
|     <title>Error response</title>
|     </head>
|     <body>
|     <h1>Error response</h1>
|     <p>Error code: 400</p>
|     <p>Message: Bad request syntax ('
|     ').</p>
|     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p>
|     </body>
|_    </html>
|_http-server-header: Werkzeug/3.0.2 Python/3.8.10
|_http-title: Did not follow redirect to http://airplane.thm:8000/?page=index.html
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8000-TCP:V=7.80%I=7%D=6/25%Time=667AD9F2%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,1F3,"HTTP/1\.1\x20302\x20FOUND\r\nServer:\x20Werkzeug/3\.0\.2\
SF:x20Python/3\.8\.10\r\nDate:\x20Tue,\x2025\x20Jun\x202024\x2014:53:46\x2
SF:0GMT\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-Length:
SF:\x20269\r\nLocation:\x20http://airplane\.thm:8000/\?page=index\.html\r\
SF:nConnection:\x20close\r\n\r\n<!doctype\x20html>\n<html\x20lang=en>\n<ti
SF:tle>Redirecting\.\.\.</title>\n<h1>Redirecting\.\.\.</h1>\n<p>You\x20sh
SF:ould\x20be\x20redirected\x20automatically\x20to\x20the\x20target\x20URL
SF::\x20<a\x20href=\"http://airplane\.thm:8000/\?page=index\.html\">http:/
SF:/airplane\.thm:8000/\?page=index\.html</a>\.\x20If\x20not,\x20click\x20
SF:the\x20link\.\n")%r(FourOhFourRequest,184,"HTTP/1\.1\x20404\x20NOT\x20F
SF:OUND\r\nServer:\x20Werkzeug/3\.0\.2\x20Python/3\.8\.10\r\nDate:\x20Tue,
SF:\x2025\x20Jun\x202024\x2014:53:51\x20GMT\r\nContent-Type:\x20text/html;
SF:\x20charset=utf-8\r\nContent-Length:\x20207\r\nConnection:\x20close\r\n
SF:\r\n<!doctype\x20html>\n<html\x20lang=en>\n<title>404\x20Not\x20Found</
SF:title>\n<h1>Not\x20Found</h1>\n<p>The\x20requested\x20URL\x20was\x20not
SF:\x20found\x20on\x20the\x20server\.\x20If\x20you\x20entered\x20the\x20UR
SF:L\x20manually\x20please\x20check\x20your\x20spelling\x20and\x20try\x20a
SF:gain\.</p>\n")%r(Socks5,213,"<!DOCTYPE\x20HTML\x20PUBLIC\x20\"-//W3C//D
SF:TD\x20HTML\x204\.01//EN\"\n\x20\x20\x20\x20\x20\x20\x20\x20\"http://www
SF:\.w3\.org/TR/html4/strict\.dtd\">\n<html>\n\x20\x20\x20\x20<head>\n\x20
SF:\x20\x20\x20\x20\x20\x20\x20<meta\x20http-equiv=\"Content-Type\"\x20con
SF:tent=\"text/html;charset=utf-8\">\n\x20\x20\x20\x20\x20\x20\x20\x20<tit
SF:le>Error\x20response</title>\n\x20\x20\x20\x20</head>\n\x20\x20\x20\x20
SF:<body>\n\x20\x20\x20\x20\x20\x20\x20\x20<h1>Error\x20response</h1>\n\x2
SF:0\x20\x20\x20\x20\x20\x20\x20<p>Error\x20code:\x20400</p>\n\x20\x20\x20
SF:\x20\x20\x20\x20\x20<p>Message:\x20Bad\x20request\x20syntax\x20\('\\x05
SF:\\x04\\x00\\x01\\x02\\x80\\x05\\x01\\x00\\x03'\)\.</p>\n\x20\x20\x20\x2
SF:0\x20\x20\x20\x20<p>Error\x20code\x20explanation:\x20HTTPStatus\.BAD_RE
SF:QUEST\x20-\x20Bad\x20request\x20syntax\x20or\x20unsupported\x20method\.
SF:</p>\n\x20\x20\x20\x20</body>\n</html>\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Jun 25 16:56:25 2024 -- 1 IP address (1 host up) scanned in 303.81 seconds

```

## FOUND SERVICES

- [[PORT 22]]: SSH
- [[PORT 6048]]: x11?  $genuenlyno idea and niether does nmap$
- [[PORT 8000]]: HTTP 