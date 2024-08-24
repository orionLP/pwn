```bash
$ nmap --script=http-sitemap-generator --script-args=httpspider.maxdepth=1000 crm.board.htb -p 80
Starting Nmap 7.80 ( https://nmap.org ) at 2024-08-23 10:41 CEST
Nmap scan report for crm.board.htb (10.10.11.11)
Host is up (0.051s latency).
rDNS record for 10.10.11.11: board.htb

PORT   STATE SERVICE
80/tcp open  http
| http-sitemap-generator: 
|   Directory structure:
|     /
|       Other: 1; php: 1
|     /core/js/
|       js: 1; php: 1
|     /includes/jquery/js/
|       js: 2
|     /includes/jquery/plugins/jnotify/
|       css: 1; js: 1
|     /includes/jquery/plugins/multiselect/
|       js: 1
|     /includes/jquery/plugins/select2/dist/css/
|       css: 1
|     /includes/jquery/plugins/select2/dist/js/
|       js: 1
|     /includes/jstz/
|       js: 1
|     /support/
|       php: 1
|     /theme/
|       png: 1; svg: 1
|     /theme/common/fontawesome-5/css/
|       css: 2
|     /theme/eldy/
|       php: 2
|     /user/
|       php: 1
|   Longest directory structure:
|     Depth: 6
|     Dir: /includes/jquery/plugins/select2/dist/js/
|   Total files found (by extension):
|_    Other: 1; css: 4; js: 7; php: 6; png: 1; svg: 1

Nmap done: 1 IP address (1 host up) scanned in 8.45 seconds
```