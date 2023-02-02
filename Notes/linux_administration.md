## COMMANDS TO ADMINISTER A LINUX SERVER   

# Samba

smbclient is the default tool to access samba shares in a computer. 

Useful commands:
<ol>
    <li>to get the shares of a computer: smbclient -L //server_ip</li>
    <li>to connect to a share of a computer: smbclient //server_ip/share</li>
</ol>

smbmap is also another tool that can speed up recon.

# DNS

dig is a standard tool to communicate with dns servers

to get the sub-domains of a zone "zone" at ns "ip":  dig axfr "zone" @"ip"

# GUIDE FOR CUT COMMAND

cut is used to eliminate and split into different columns data from a file or the standard input

to specify which is the delimeter of your cut: -d '[string]'

to specify which columns you want to keep: -f '[range|list|number]' 

# TR COMMAND    

tr is a simple command to replace or delete some characters from a sequence 

usage:

tr '[set1]','[set2]' '[set1]','[set2]'

with set meaning any sequence of characters (you can use for example tr '\n1' ',2' or tr '\n','1' ',','2' to translate \n to a , and 1 to a 2)
