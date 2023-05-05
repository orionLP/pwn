#!/bin/bash

function echo_color () {
    local color=$1

    case $color in
        "red")
            color=31
        ;;
        "blue")
            color=34
        ;;
        "white")
            color=37
        ;;
        *)
            echo "invalid color, valids: red, blue"
            return 1
        ;;
    esac

    echo -e "\e[${color}m${2}\e[0m\n"

}
