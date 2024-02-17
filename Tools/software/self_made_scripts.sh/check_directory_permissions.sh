#!/bin/bash

# functions

explore() {
    # the first parameter is a list of directories
    local depth=${1}

    # get all directories in the current directory
    local directories=($(ls -d */ 2>/dev/null))

    # check for size 0
    if [ ${#directories[@]} -eq 0 ]; then
        return
    fi
    
    # check if the user can access the directory
    for directory in ${directories[@]}; do
        if [ -r ${directory} ]; then
            whitespace=""
            # print the name of the directory with depth * 2 spaces 
            for ((i=0; i<$(( ${depth}  * 2 )); i++)); do
                whitespace="${whitespace} "
            done
            echo "${whitespace}:${directory}"

            cd ${directory}
            explore $user $groups $(( $depth + 1 ))
            cd ..
        fi
    done
}

# main

echo "Checking Directories you can access"

explore 0