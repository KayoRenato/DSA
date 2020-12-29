#!/bin/bash
# ==============================
# Script: readfile.sh
# ==============================
# Declare array
declare -a ARRAY
# Link filedescriptor 10 with stdin
exec 10<&0
exec < $1
let count=0

while read LINE; do

    ARRAY[$count]=$LINE
    ((count++))
done

echo Número de elementos: ${#ARRAY[@]}
echo ${ARRAY[@]}

exec 0<&10 10<&-
