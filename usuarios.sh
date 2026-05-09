#!/bin/bash

if id "devops_user" &>/dev/null; then
    echo "El usuario devops_user ya existe"
else
    sudo useradd devops_user
    echo "Usuario devops_user creado."
fi


sudo chown -R devops_user:devops_user ~/environment
echo "Permisos asignados temporalmente a devops_user."

sudo chown -R ec2-user:ec2-user ~/environment
echo "Permisos restaurados para ec2-user correctamente"
