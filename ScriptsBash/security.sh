#!/bin/bash
# ==============================
# Script: security.sh
# ==============================
# Automatizando tarefas
# -Update local file database:
echo -e "\e[4;32mUPDATING LOCAL FILE DATABASE\e[0m"
updatedb
if [ $? == 0 ]; then
echo "The local file database was updated correctly."
else
echo "The local file database was not updated correctly."
fi
echo ""
# -Find and / or delete files with 777 permissions.
echo -e "\e[4;32mLOOKING FOR FILES WITH 777 PERMISSIONS\e[0m"
find -type f -perm 0777 -exec rm -i {} +;
echo ""
# -Alert when file system usage surpasses a defined limit 
echo -e "\e[4;32mCHECKING FILE SYSTEM USAGE\e[0m"
THRESHOLD=30
while read line; do
# This variable stores the file system path as a string
FILESYSTEM=$(echo $line | awk '{print $1}')
# This variable stores the use percentage (XX%)
PERCENTAGE=$(echo $line | awk '{print $5}')
# Use percentage without the % sign.
USAGE=${PERCENTAGE%?}
if [ $USAGE -gt $THRESHOLD ]; then
echo "The remaining available space in $FILESYSTEM is critically low. Used: $PERCENTAGE"
fi
done < <(df -h --total | grep -vi filesystem)
