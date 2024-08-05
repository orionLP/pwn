#### SCANS 

```bash
$ nmap -p139 --script smb-protocols 10.10.208.255

Starting Nmap 7.80 ( https://nmap.org ) at 2024-05-09 16:01 CEST
Nmap scan report for 10.10.208.255
Host is up (0.039s latency).

PORT    STATE SERVICE
139/tcp open  netbios-ssn

Host script results:
| smb-protocols: 
|   dialects: 
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2.02
|     2.10
|     3.00
|     3.02
|_    3.11



$ smbclient -m NT1 //10.10.208.255/temporary\ share
lp_load_ex: Max protocol NT1 is less than min protocol SMB2_02.
```

```bash 
$ python3 /opt/smbmap/smbmap.py -H 10.10.208.255

Disk                                                  	Permissions	Comment
----                                                  	-----------	-------
print$                                            	NO ACCESS	PrinterDrivers
temporary share                                   	READ ONLY	
IPC$                                              	NO ACCESS	IPC Service (Samba 4.10.16)
```
### SHARES LIST

```bash
$ smbclient -L 10.10.149.74

Password for [WORKGROUP\oriol]:
Anonymous login successful

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	temporary share Disk      
	IPC$            IPC       IPC Service (Samba 4.10.16)
	SMB1 disabled -- no workgroup available
	
```


### print$

```bash
$ smbclient //10.10.149.74/print$

Password for [WORKGROUP\oriol]:
Anonymous login successful
tree connect failed: NT_STATUS_ACCESS_DENIED
```

### temporary share

```bash
$ smbclient //10.10.149.74/temporary\ share
Password for [WORKGROUP\oriol]:
Anonymous login successful

smb: \> ls
  .                                   D        0  Mon Jan 10 14:06:44 2022
  ..                                  D        0  Tue Nov 23 17:24:05 2021
  .bash_logout                        H       18  Wed Apr  1 04:17:30 2020
  .bash_profile                       H      193  Wed Apr  1 04:17:30 2020
  .bashrc                             H      231  Wed Apr  1 04:17:30 2020
  .bash_history                       H        0  Tue May  7 16:26:40 2024
  chapter1                            D        0  Tue Nov 23 11:07:47 2021
  chapter2                            D        0  Tue Nov 23 11:08:11 2021
  chapter3                            D        0  Tue Nov 23 11:08:18 2021
  chapter4                            D        0  Tue Nov 23 11:08:25 2021
  chapter5                            D        0  Tue Nov 23 11:08:33 2021
  chapter6                            D        0  Tue Nov 23 11:12:24 2021
  chapter7                            D        0  Tue Nov 23 12:14:27 2021
  chapter8                            D        0  Tue Nov 23 11:12:45 2021
  chapter9                            D        0  Tue Nov 23 11:12:53 2021
  .ssh                               DH        0  Mon Jan 10 14:05:34 2022
  .viminfo                            H        0  Tue May  7 16:26:40 2024
  message-to-simeon.txt               N      251  Mon Jan 10 14:06:44 2022

		37726212 blocks of size 1024. 34889004 blocks available

```

doing a more exetensive one resultied in seeing all files and directories are read only 

In here we find:
- [[message-to-simeon.txt]]
- [[bashrc]]
- [[bash_profile]]
- [[bash_logout]]

Sadly ssh is not accessible :<

