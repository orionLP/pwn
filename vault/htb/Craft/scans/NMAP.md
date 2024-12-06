## SCANS

```bash
┌──(kali㉿kali)-[~/work/scans]
└─$ cat scan1.scan.nmap 
# Nmap 7.94SVN scan initiated Sun Dec  1 09:48:18 2024 as: nmap -sV -sC -p - -oA scan1.scan -vv 10.10.10.110
Nmap scan report for 10.10.10.110
Host is up, received reset ttl 255 (0.24s latency).
Scanned at 2024-12-01 09:48:31 EST for 1297s
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE  REASON         VERSION
22/tcp   open  ssh      syn-ack ttl 64 OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey: 
|   2048 bd:e7:6c:22:81:7a:db:3e:c0:f0:73:1d:f3:af:77:65 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCscULO5kzW5659eWy5BdBJWCHxBSvqKIn6TZwEdp4NG3cLJc6aVQxEUknoSoMa2RAy2CFv/IWKbFIEY33XM2PRhKTuSJd/aNrMKs0jX40q/0zpmRv4/HzLdWE33t9on739xRWgsnNI0JOaGAwa4ryubOeKo53ykP9fTgLeHvT37GthWJIzfXNA7UFXJen3T4+4xmbxA2Low8D8xAGjqVLoEgKGVy05oL+zGucd0C5LyclT0Gkxm3NCk3MLdFdPOuaVX5jlX32yKUA//Go9fN9OlGffcHkLfgTA7s+PLememC14H/r8ZLYJYByeBj2MqR6ndkQ3+OkmSjeOBPEamkqz
|   256 82:b5:f9:d1:95:3b:6d:80:0f:35:91:86:2d:b3:d7:66 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJAzk0wAfmy1zhnnnQOEoqLN0OK0zF9VwqqwIRkG58ARwaVlwSARRf3BS7Ywo2AfjZS9EWZycsXxy3/7MwEQS1U=
|   256 28:3b:26:18:ec:df:b3:36:85:9c:27:54:8d:8c:e1:33 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJsBTHLrhy1IfI4AeEWxjJBm9z6wm/F9mMPMUbpRt2+K
443/tcp  open  ssl/http syn-ack ttl 64 nginx 1.15.8
| tls-nextprotoneg: 
|_  http/1.1
|_ssl-date: TLS randomness does not represent time
| http-methods: 
|_  Supported Methods: GET HEAD OPTIONS
| tls-alpn: 
|_  http/1.1
| ssl-cert: Subject: commonName=craft.htb/organizationName=Craft/stateOrProvinceName=NY/countryName=US
| Issuer: commonName=Craft CA/organizationName=Craft/stateOrProvinceName=New York/countryName=US/emailAddress=admin@craft.htb/localityName=Buffalo/organizationalUnitName=Craft
| Public Key type: rsa
| Public Key bits: 2048
| Signature Algorithm: sha256WithRSAEncryption
| Not valid before: 2019-02-06T02:25:47
| Not valid after:  2020-06-20T02:25:47
| MD5:   0111:76e2:83c8:0f26:50e7:56e4:ce16:4766
| SHA-1: 2e11:62ef:4d2e:366f:196a:51f0:c5ca:b8ce:8592:3730
| -----BEGIN CERTIFICATE-----
| MIIEQDCCAigCCQC6e7PJjcRLnzANBgkqhkiG9w0BAQsFADCBhTELMAkGA1UEBhMC
| VVMxETAPBgNVBAgMCE5ldyBZb3JrMRAwDgYDVQQHDAdCdWZmYWxvMQ4wDAYDVQQK
| DAVDcmFmdDEOMAwGA1UECwwFQ3JhZnQxETAPBgNVBAMMCENyYWZ0IENBMR4wHAYJ
| KoZIhvcNAQkBFg9hZG1pbkBjcmFmdC5odGIwHhcNMTkwMjA2MDIyNTQ3WhcNMjAw
| NjIwMDIyNTQ3WjA+MQswCQYDVQQGEwJVUzELMAkGA1UECAwCTlkxDjAMBgNVBAoM
| BUNyYWZ0MRIwEAYDVQQDDAljcmFmdC5odGIwggEiMA0GCSqGSIb3DQEBAQUAA4IB
| DwAwggEKAoIBAQDV6vf1Ki4fZhJeMOQBAUFx98hM70l6Hpu+4MlB4++i/u2fKRvV
| woGYPpz3KGuNKv+BvjR0+yGFM2HflIgZcc5yE//MGnb9F1fcjJ66rT3qBHjIfwls
| 6MRygl9NRVSa09PvrXUbULBr95V624TTPewiEy1yZgMP+ByQzm9Td0jdTQ8HDugq
| kmOmUDX34kDtZc5u7iFBicTXYBpnYVZNEVsUoT6QVZiez07E5L9d0XZ9+iLeVvaB
| XmeimEdbaR2iKKDTmmWaduH/YLUAEP+gS0STM2lKiXL3euL13f9z6i0KjI8Tymby
| Sb6zeznqWCYuJRHfEZnYj+B26jcXU2ZE0GwrAgMBAAEwDQYJKoZIhvcNAQELBQAD
| ggIBACEEpKD0fivZFNx7Q8/q81SNE8TbAQKyfOP98SXU6LAMPOIfAf27tG8C8xGF
| NCmQcggUwpuz2PB+t8vN91oRHdehkpDsVa7ZOKPQm+RQYH7WlMyO65bz5M2zxkbq
| m7Eesaeakdj2XR4ah7TbCeSU7Mu2ePdOLgHme8qI60XjvTrNJ7sB7i5vc5cs7Q9j
| AgOQhQFJddhFsViOcuICei+m8WDg2w4/Kmbu1lSHCCAm4HPA+H8+dZcHN3v3EtqQ
| IRwoph/Jl5h9yxZXDDrFyGMburGjWtIwvrDJmC3m5eDigliUM1OZEWOmDEzBKfUG
| dpNln6Mku8EI2qrVITepg9Szb/7lbd8OJsWo1g4s9BPi2NA/ZGk3z3no6AvGPo6d
| 74uNAzGaIBaPH9v2pyUsKbeNm/TY2GikZuOUVdSt/dXCEQ5I5TVxLBJYB9RmzA2+
| u5qS2hN6KOBNBWvYsvLTsAyq5VTzi6seRUk887S5oMoVzD4AxchcrwmBOKPaeyTS
| sUpN2F4Ea7TRPyQWN1IjVnIjkpRzN5mUwnKyyKovKyQaYE9HPM59PC8uTri59mIv
| Rtz++eBxJu/2FFDhI7AiOctOhzKTa7AN0JmTO1pp4OFY5uDl4yFk3t+1lMKhggMa
| UOpGWGGlST3o/VI2ebJq4nDewBf/LY3ZtJbNIKcXNpQQzB7/
|_-----END CERTIFICATE-----
|_http-server-header: nginx/1.15.8
|_http-title: About
6022/tcp open  ssh      syn-ack ttl 64 (protocol 2.0)
| ssh-hostkey: 
|   2048 5b:cc:bf:f1:a1:8f:72:b0:c0:fb:df:a3:01:dc:a6:fb (RSA)
|_ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDU+fEcb0HbuFvUiMce89AuwclFwGQAJ/FSk+X/uPL+08lP9AzNCivAovV8Py3XEGfUhSDQeJ6Xw5aZCIZB7z/40IViSC1S1fe49lmv7TlDSFKEOZIDQIAuDP3giwyrdX0MnM5qrFtqs9lIH0D8MnGVCh3kcjG5Mh+Jb4/fcGkIpLSAyVc2Fm5PFFV0XIay5vv/SffCO1141JHFZj+Sal4t4MmlZiY1RTaAgGLsn1SshS2EYFv91rZqHmmNCk+GNVSU9txRQm3OrB+06QTsOWnYN71p6+hTe/TQjhaE53zM+/xZi7sPIq6l6evvNSMOOt9fgVQkvM2NuVutLiq6od2h
| fingerprint-strings: 
|   NULL: 
|_    SSH-2.0-Go
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port6022-TCP:V=7.94SVN%I=7%D=12/1%Time=674C7C23%P=x86_64-pc-linux-gnu%r
SF:(NULL,C,"SSH-2\.0-Go\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Dec  1 10:10:08 2024 -- 1 IP address (1 host up) scanned in 1310.03 seconds
```

## SERVICES

- [[PORT 22]]: ssh server
- [[PORT 443]]: https server
- [[PORT 6022]]: ssh server