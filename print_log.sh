#!/bin/bash

filename=$(basename "$1")

if [ ! -d "./logs" ]; then
    mkdir -p ./logs
fi

if [ ! -f "./logs/$filename.log" ]; then
    ./decompile.sh "$1" > /dev/null 2>&1
fi

cat ./logs/$filename.log
