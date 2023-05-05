#!/bin/bash

for name in $(cat /home/oriol/Documents/GitHub/pwn/SecLists/Usernames/probable_usernames.txt)
do 
    cat /tmp/user_fuzz | grep -E "${name} "
done 