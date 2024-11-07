#!/bin/sh

if [ ! -d "$1" ]; then
    mkdir "$1"
fi

cd "$1" || exit

for i in $(seq 0 4); do
    touch "$1$i.txt"
done

tar -cf "$1.tar" "$1"0.txt "$1"1.txt "$1"2.txt "$1"3.txt "$1"4.txt

ls "$1"0.txt "$1"1.txt "$1"2.txt "$1"3.txt "$1"4.txt "$1.tar"

mkdir "$1"
mv "$1.tar" "$1/"

cd "$1" || exit
tar -xvf "$1.tar"

exit 0

