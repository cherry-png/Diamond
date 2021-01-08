#!/bin/bash

if [ "$#" == 2 ] && [ "$1" == "run" ]
then
    cd "$2"
    echo "Running..."
    echo ""
    echo ""
    python3 "file.py"
    echo "Cleaning up..."
    cd "__pycache__/"
    rm *
    cd -
    rmdir "__pycache__/"
    echo "Ended"
elif [ "$#" == 1 ] && [ "$1" == "diamondc" ]
then 
    echo "Running..."
    python3 diamondc.py
fi
