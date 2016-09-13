#!/bin/bash

d=$(date +%d-%m-%Y)
name="${1%%.*}"
ext="${1#*.}"
#echo $name
#echo $ext
#echo $name'_'$d'.'$ext
cp $1 $name'_'$d'.'$ext

