#!/bin/bash
# ==============================
# Script: disk.sh
# ==============================
df -H | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{ print $5 " " $1 }' | while read output;
do
  echo $output
  usep=$(echo $output | awk '{ print $1}' | cut -d'%' -f1  )
  partition=$(echo $output | awk '{ print $2 }' )
  if [ $usep -ge 90 ]; then
    echo "Ficando sem espaço em disco \"$partition ($usep%)\" on $(hostname) as on $(date)" #|
    # mail -s "Alerta: Quase sem espaço em disco em $usep%" email@exemplo.com
  fi
done
