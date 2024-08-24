The used scripts where

```bash
$ nmap --script http-comments-displayer 10.10.11.11 

# output hidden since it was too long (nothing interesting)

$ nmap --script=http-devframework --script-args=httpspider.maxpagecount=20 10.10.11.11 -v -p 80

PORT   STATE SERVICE
80/tcp open  http
|_http-devframework: Couldn't determine the underlying framework or CMS. Try increasing 'httpspider.maxpagecount' value to spider more pages.

$ nmap --script=http-vhosts  10.10.11.11 -v -p 80

PORT   STATE SERVICE 
80/tcp open  http 
| http-vhosts: 
|_127 names had status ERROR 
```