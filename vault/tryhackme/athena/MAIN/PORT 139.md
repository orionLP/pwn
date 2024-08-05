```bash
(base) user@usercomp:~/Documents/GitHub/pwn/ctf/athena$ smbclient -p 445 -L 10.10.196.202

Password for [WORKGROUP\user]:
Anonymous login successful

	Sharename       Type      Comment
	---------       ----      -------
	public          Disk      
	IPC$            IPC       IPC Service (Samba 4.15.13-Ubuntu)
SMB1 disabled -- no workgroup available
(base) user@usercomp:~/Documents/GitHub/pwn/ctf/athena$ smbclient //10.10.196.202/public
Password for [WORKGROUP\user]:
Anonymous login successful
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Mon Apr 17 02:54:43 2023
  ..                                  D        0  Mon Apr 17 02:54:05 2023
  msg_for_administrator.txt           N      253  Sun Apr 16 20:59:44 2023

		19947120 blocks of size 1024. 9547296 blocks available             
smb: \> get msg_for_administrator.txt 
getting file \msg_for_administrator.txt of size 253 as msg_for_administrator.txt (1.5 KiloBytes/sec) (average 1.5 KiloBytes/sec)

```

Also, after getting the file from the administrator the content is the following

```txt

Dear Administrator,

I would like to inform you that a new Ping system is being developed and I left the corresponding application in a specific path, which can be accessed through the following address: /myrouterpanel

Yours sincerely,

Athena
Intern

```

So now we can simply try http://IP/myrouterpanel in [[PORT 80]]