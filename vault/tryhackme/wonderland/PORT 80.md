## FUZZES 

```bash
(base) oriol@oriol-Aspire-A515-56:~/Documents/GitHub/pwn$ ffuf -X GET -u http://10.10.147.61/FUZZ -w ./Tools/SecLists/Discovery/Web-Content/directory-list-2.3-big.txt

r                       [Status: 301, Size: 0, Words: 1, Lines: 1]
poem                    [Status: 301, Size: 0, Words: 1, Lines: 1]
```

```bash 
(base) oriol@oriol-Aspire-A515-56:~/Documents/GitHub/pwn$ ffuf -X GET -u http://10.10.147.61/FUZZ -w ./Tools/SecLists/Discovery/Web-Content/common.txt 

img                     [Status: 301, Size: 0, Words: 1, Lines: 1]
index.html              [Status: 301, Size: 0, Words: 1, Lines: 1]

```
## DISCOVERED 


```txt
/main.css # nothing interesting
/poem     # a big insecrutable poem
/r        # Says to keep going :^)
/img      # images of the website
```

on a whim i did the following 

```txt
/r/a # got an answer
/r/a/b/ # got an answer

http://10.10.147.61/r/a/b/b/i/t/ # followed the rabbit
```

The following is found hidden in the html 

alice:HowDothTheLittleCrocodileImproveHisShiningTail

So now we can access [[alice]]'s account