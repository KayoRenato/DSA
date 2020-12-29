#!/bin/bash
# ==============================
# Script: copyfiles.sh
# ==============================
path_src=~/Downloads
path_dst=/tmp/Backup
date=$(date +"%m%d%y")
for file_src in $path_src/*; do
  file_dst="$path_dst/$(basename $file_src | \
    sed "s/^\(.*\)\.\(.*\)/\1$date.\2/")"
  cp -r "$file_src" "$file_dst"
done
