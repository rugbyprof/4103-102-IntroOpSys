#!/bin/bash

d=$(date +%d-%m-%Y)
echo $d'_'$1
cp $1 $d'_'$1 

