#!/bin/bash
source colorizer.sh

if systemctl status firewalld 1>/dev/null
then 
    echo_color red "Your firewall is active, unable to do anything"
    exit 1
fi 

echo_color white "Welcome to a brute-force default tester for web applications"

echo_color white "Give an ip or domain to test"

read domain 

if echo "${domain}" | grep -Ev "^((([a-zA-Z]+\.)*[a-zA-Z]+)|([0-9]{1,3}\.){3}[0-9]{1,3})$"
then 
    echo_color red "you did not provide a valid domain"
    exit 2
fi

echo_color white "Testing for directives and php files, input the domain of the web-page to fuzz. temporary files will be inserted in /tmp/fuzz"

rm -rd /tmp/fuzz 2>/dev/null
mkdir /tmp/fuzz 

cat /home/oriol/Documents/GitHub/pwn/SecLists/Discovery/Web-Content/common.txt > /tmp/fuzz/file
cat /home/oriol/Documents/GitHub/pwn/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt >> /tmp/fuzz/file 

cat /tmp/fuzz/file | sort -u > /tmp/fuzz/file2

rm /tmp/fuzz/file 

ffuf -w /tmp/fuzz/file2 -u http://${domain}/FUZZ -r -e .php 1>/tmp/fuzz/results

cat /tmp/fuzz/results