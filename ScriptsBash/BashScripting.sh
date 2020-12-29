# Bash Scripting

#!/bin/bash
# ==============================
# Script: hello-world.sh
# ==============================
TEXTO="Hello World"
echo $TEXTO



#!/bin/bash
# ==============================
# Script: backup.sh
# ==============================
tar -czf home.tar.gz /home/dmpm



#!/bin/bash
# ==============================
# Script: hist.sh
# ==============================
clear
echo "Informações do ambiente do usuário"
echo "================================================"
echo ""
echo "Olá: $USER"
echo ""
echo "Seu diretório home é: $HOME"
echo ""
echo "Seu cliente SSH é: $SSH_CLIENT"
echo ""
echo "Seu tipo de sessão terminal é: $TERM"
echo ""



#!/bin/bash
# ==============================
# Script: user.sh
# ==============================
# Input do Usuário
echo "Digite seu primeiro nome: "
read FIRSTNAME
echo "Digite seu sobrenome: "
read LASTNAME
echo ""
echo "Seu nome completo eh: $FIRSTNAME $LASTNAME"
echo ""
echo "Digite sua idade: "
read USERAGE
echo "Em 10 anos você estará com `expr $USERAGE + 10` anos."



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



#!/bin/bash
# ==============================
# Script: case.sh
# ==============================
# Case
clear
echo "MENU"
echo "========="
echo "1 Laranja"
echo "2 Melancia"
echo "3 Uva"
echo "4 Sair"
echo "Digite o número da sua escolha: "
read MENUCHOICE
case $MENUCHOICE in
 1)
  echo "Você escolheu a primeira opção";;
 2)
  echo "Você escolheu a segunda opção";;
 3)
  echo "Você escolheu a terceira opção";;
 4)
  echo "Você pediu para sair";;
esac



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
    echo "Ficando sem espaço em disco \"$partition ($usep%)\" on $(hostname) as on $(date)" |
     mail -s "Alerta: Quase sem espaço em disco em $usep%" email@exemplo.com
  fi
done



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



#!/bin/bash
# ==============================
# Script: copyfiles.sh
# ==============================
path_src=/home/dmpm/Downloads
path_dst=/tmp/Backup
date=$(date +"%m%d%y")
for file_src in $path_src/*; do
  file_dst="$path_dst/$(basename $file_src | \
    sed "s/^\(.*\)\.\(.*\)/\1$date.\2/")"
  echo cp "$file_src" "$file_dst"
done



#!/bin/bash
# ==============================
# Script: system.sh
# ==============================
# Script para mostrar estado atual do sistema
# -Hostname information:
echo -e "\e[31;43m***** HOSTNAME INFORMATION *****\e[0m"
hostnamectl
echo ""
# -File system disk space usage:
echo -e "\e[31;43m***** FILE SYSTEM DISK SPACE USAGE *****\e[0m"
df -h
echo ""
# -Free and used memory in the system:
echo -e "\e[31;43m ***** FREE AND USED MEMORY *****\e[0m"
free
echo ""
# -System uptime and load:
echo -e "\e[31;43m***** SYSTEM UPTIME AND LOAD *****\e[0m"
uptime
echo ""
# -Logged-in users:
echo -e "\e[31;43m***** CURRENTLY LOGGED-IN USERS *****\e[0m"
who
echo ""
# -Top 5 processes as far as memory usage is concerned
echo -e "\e[31;43m***** TOP 5 MEMORY-CONSUMING PROCESSES *****\e[0m"
ps -eo %mem,%cpu,comm --sort=-%mem | head -n 6
echo ""
echo -e "\e[1;32mDone.\e[0m"



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








