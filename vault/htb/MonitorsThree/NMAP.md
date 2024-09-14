
```bash
# nmap -sS -sV -sC -p - -v 10.10.11.30
Starting Nmap 7.80 ( https://nmap.org ) at 2024-09-10 19:54 CEST
NSE: Loaded 151 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 19:54
Completed NSE at 19:54, 0.00s elapsed
Initiating NSE at 19:54
Completed NSE at 19:54, 0.00s elapsed
Initiating NSE at 19:54
Completed NSE at 19:54, 0.00s elapsed
Initiating Ping Scan at 19:54
Scanning 10.10.11.30 [4 ports]
Completed Ping Scan at 19:54, 0.05s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 19:54
Completed Parallel DNS resolution of 1 host. at 19:55, 13.00s elapsed
Initiating SYN Stealth Scan at 19:55
Scanning 10.10.11.30 [65535 ports]
Increasing send delay for 10.10.11.30 from 0 to 5 due to 11 out of 16 dropped probes since last increase.
Discovered open port 22/tcp on 10.10.11.30
Discovered open port 80/tcp on 10.10.11.30
```

### DISCOVERED PORTS 

[[PORT 22]]: ssh server
[[PORT 80]]: http server