#!/bin/bash

ls $PWD/../SecLists/Discovery/Web-Content | grep -E "^[cC]ommon|directory-list-2.3-medium.txt" | sort -u > output

echo "starting web discovery against https://administrator1.friendzone.red/"

for name in output
do 
    gobuster dir -w $PWD/../SecLists/Discovery/Web-Content/${name} -u https://administrator1.friendzone.red/ | grep -E "Status"
done

echo "starting web discovery against https://uploads.friendzone.red/"

for name in output
do 
    gobuster dir -w $PWD/../SecLists/Discovery/Web-Content/${name} -u https://administrator1.friendzone.red/ | grep -E "Status"
done