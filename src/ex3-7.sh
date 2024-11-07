#!/bin/sh

if [ ! -d "$1" ]; then
    mkdir "$1"
fi

cd "$1" || exit

for i in $(seq 0 4); do
    mkdir -p "file$i"
    ln -s "../file$i.txt" "file$i/file$i.txt"
done

exit 0
