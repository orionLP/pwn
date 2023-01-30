##Tips and remainders about the nmap tool:

#For selecting ports:

to select a range of ports: -p[number]-[number]

to select all ports: -p-

to select some specific ports: -p[number],[number]

to specify tcp or udp protocol: -p U:[ports] T:[ports]

#For selecting speed 

to specify a minimum package/second: --min-rate [number]    	> the higher the more speedy

to increase speed: -T[number] in the range [1,5]

# Firewall evasion

to introduce a bad checksum (if everything is okay it should all be dropped, if you get an ok response something is wrong)

#scripts 


# tips and tricks

(types of scans)

using -sT is slower than -sS and should be avoided

using -F only scans the 100 most common ports (useful when you have to check for firewalls)


