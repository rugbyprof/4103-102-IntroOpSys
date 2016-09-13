#!/bin/bash

i=0
while read line; do
    myArray[i]="$line"
    i=$(( i = i + 1 ))
done < /usr/share/dict/words

echo $(( i ))
echo $(( RANDOM * RANDOM ))

for value in {1..25}
do
    r=$(( (RANDOM * RANDOM) % i ))
    echo ${myArray[$r]}
done
