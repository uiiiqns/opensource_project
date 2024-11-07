#!/bin/sh

if [ "$#" -lt 2 ]; then
    echo "Usage: $0 이름 전화번호"
    exit 1
fi

name=$1
phone=$2

if [ ! -f "DB.txt" ]; then
    echo "$name $phone" > DB.txt
else
    echo "$name $phone" >> DB.txt
fi

exit 0
