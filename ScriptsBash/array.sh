#!/bin/bash
# ==============================
# Script: array.sh
# ==============================
# Array 
SERVERLIST=("websrv01" "websrv02" "websrv03" "websrv04")
COUNT=0

# Loop
for INDEX in ${SERVERLIST[@]}; do
 echo "Servidor: ${SERVERLIST[COUNT]}"
 COUNT="`expr $COUNT + 1`"
done
