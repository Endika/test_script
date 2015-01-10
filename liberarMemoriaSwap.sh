#!/bin/bash
 
sudo ls &>/dev/null
if [ $? -ne 0 ]; then
        echo "El usuario no tiene permisos de administrador"
exit 1
fi
 
echo -e "\nAntes:"
free
swapoff -a ; swapon -a
echo -e "\nDespues:"
free
echo "Memoria Swap Liberada!"
