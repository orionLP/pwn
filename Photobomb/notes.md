The scan shows that photobomb has 80 and 22 open 

```{sh}
nmap 10.129.93.24 -sC -sV -p22,80

Starting Nmap 7.80 ( https://nmap.org ) at 2023-02-02 15:01 CET
Nmap scan report for 10.129.93.24
Host is up (0.073s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://photobomb.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.91 seconds

```

The webpage has the following information:
<ol>
    <li>its a printing service</li>
    <li>credentials for printing are given to users in a welcome pack </li>
    <li>technichal support team is on  4 4283 77468377</li>
</ol>

when trying to access the link in the description we get a login alert. Looking at the js code that the webpage loads we can see that the credentials are in plain text in the js code 

```{sh}
curl http://photobomb.htb/photobomb.js
function init() {
  // Jameson: pre-populate creds for tech support as they keep forgetting them and emailing me
  if (document.cookie.match(/^(.*;)?\s*isPhotoBombTechSupport\s*=\s*[^;]+(.*)?$/)) {
    document.getElementsByClassName('creds')[0].setAttribute('href','http://pH0t0:b0Mb!@photobomb.htb/printer');
  }
}
window.onload = init;
```

>pH0t0:b0Mb!

in the next web page that loads, we have a form with the names: name (image to select), filetype (type of file to submit), dimensions (the dimensions of printing)

notes:
the sever blacklists (in photo) any form of / or .. 
it also blocks it in the dimensions
it does not in the filetype 
it seems to only have the jpg images and then convert them into png if asked

I am, for now, unable to find an arbitrary file read in the image selector.

playing around with it i broke it and it returned me an error web-page, with some information:

the server is running on ruby using sinatra
some images are in images are in resized_images

