#!/bin/bash

function colored_cow() {
    if which cowsay > /dev/null;
    then
        cowsay -t "$1" | lolcat
    else 
        colored_output $1
    fi
    return 0
}

function colored_output() {
    if which lolcat > /dev/null;
    then 
        echo "$1" | lolcat
    else
        echo "$1"
    fi
    return 0
}


MESSAGE="Welcome to this magic ennumerator";

colored_cow "$MESSAGE"

echo "Starting dump..."

echo "Printing system information"
uname -a 

echo "Printing filesystem misconfigurations"

read -p "do you want to inspect the filesystem y/n " answer
if [[ $answer == "y" ]];
then
    echo "Files executable by the user which might be tasty for an inputed user and folder"
    read name
    read path
    echo "Executable files from $name and $path that have suid"
    find $path -executable -perm /u=s -type f -user $name -exec ls -la {} + 2>/dev/null
    echo "Executable files from $name and $path that have sgid"
    find $path -executable -perm /g=s -type f -user $name -exec ls -la {} + 2>/dev/null
    echo "Readable files from $name and $path"
    find $path -readable -type f -user $name -exec ls -la {} + 2>/dev/null
    echo "Writable files from $name and $path"
    find $path -writable -type f -user $name -exec ls -la {} + 2>/dev/null
fi

read -p "do you want to get information on the users/groups y/n" answer
if [[ $answer == "y" ]];
then 
    echo "Information on the users in the system"
    cat /etc/passwd
    echo "Information on the groups in the system"
    cat /etc/group
fi