#!/bin/bash

read command
echo -n "$command" | xxd -p -c 1 | tr -d '\n' | sed 's/\(..\)/\\x\1/g' > /tmp/hexcommand

printf '$(/usr/bin/bash -c \"$(echo -e \x27'
echo "$(cat /tmp/hexcommand)')\")"