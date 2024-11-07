#!/bin/sh

n=$1


if [ -z "$n" ] ; then
	while true
	do 
		echo "hello world"
	done
else
	for i in $(seq 1 $n)
	do
		echo "hello world"
	done
fi

exit 0
