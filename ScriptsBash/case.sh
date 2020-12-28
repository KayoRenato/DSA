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
