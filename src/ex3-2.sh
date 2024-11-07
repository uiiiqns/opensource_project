#!/bin/sh

n1=$1
operator=$2
n2=$3

if [ "$operator" = "+" ]; then
	result=$((n1 + n2))
elif [ "$operator" = "-" ]; then
	result=$((n1 - n2))
else
	exit 1
fi

echo "$result"

exit 0
