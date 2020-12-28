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
