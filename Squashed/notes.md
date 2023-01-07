## WELCOME TO SQUASHED 

This machine supposedly teaches NFS misconfigurations and user management. Hope you enjoy :).

# STEP 1: ENUMERATE
# ITERATION 1

```{sh}

nmap -sV 10.10.11.191 

Starting Nmap 7.80 ( https://nmap.org ) at 2023-01-07 22:06 CET
Nmap scan report for 10.10.11.191
Host is up (0.54s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu))
111/tcp  open  rpcbind 2-4 (RPC #100000)
2049/tcp open  nfs_acl 3 (RPC #100227)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.56 seconds

```

The server has a web server rpcbind (a service for running procedures (functions) on the network to then be transmitted back to the client) and a nfs_acl server (used to access files from that server 
the client has only to request an open of a file and a read from it, as if it where in its own). 

The webpage shows a furniture web app (i suppose to buy furniture). 

Question: Why does a furniture app need to retrieve files and do calculations on a server?

# ITERATION 2

The people at htb seem to try to scan all the ports (just in case), it seems as a good practice since i missed some services.

