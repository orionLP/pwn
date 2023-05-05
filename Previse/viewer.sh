#!/bin/bash

list=$(tail results --lines=23 | grep -E "^.*\.php" | awk '{print $1}')

for val in ${list}
do 
    echo "fd${val}"
    echo "$val"
done
