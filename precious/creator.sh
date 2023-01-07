#!/bin/bash

# for i in txt html php js bin css sh 
# do
#     touch payload.${i}
# done

for i in $( seq 0 100000)
do 
echo "$i" >> payload.html
done