## LISTING

```bash
┌──(kali㉿kali)-[~]
└─$ smbclient -L //10.10.231.111 -p 445 
Password for [WORKGROUP\kali]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        nt4wrksv        Disk      
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to 10.10.231.111 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)
Unable to connect with SMB1 -- no workgroup available
                                                               
```


## nt4wrksv

The **nt4wrksv** allows for connection without authentication

```bash
smb: \> ls
  .                                   D        0  Sat Jul 25 17:46:04 2020
  ..                                  D        0  Sat Jul 25 17:46:04 2020
  passwords.txt                       A       98  Sat Jul 25 11:15:33 2020
```

```bash
┌──(kali㉿kali)-[~]
└─$ cat passwords.txt 
[User Passwords - Encoded]
Qm9iIC0gIVBAJCRXMHJEITEyMw==
QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk      
```

```bash
┌──(kali㉿kali)-[~]
└─$ tail -n 2 passwords.txt | base64 -d -
Bob - !P@$$W0rD!123
base64: invalid input
```
Actually you can decode it 
```
┌──(kali㉿kali)-[~]
└─$ echo QmlsbCAtIEp1dzRubmFNNG40MjA2OTY5NjkhJCQk | base64 -d -
Bill - Juw4nnaM4n420696969!$$$      
```
## ADMIN$

Cannot connect with user Bob or Bill

## C$

Cannot connect though user Bob or Bill