#!/bin/sh

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 이름"
    exit 1
fi

name=$1
echo "검색어: $name"

if grep -q "$name" DB.txt; then
    echo "검색 결과:" | tr '\n' ' '
    grep "$name" DB.txt
else
    echo "결과를 찾을 수 없습니다."
fi

exit 0
