#!/bin/bash

#--
#-- by Allex Lima
#-- TESTED ONLY IN ** DEBIAN-BASED ** SYSTEMS
#--
#-- This bash script will move the PyBestfit files directory to /opt/PyBestfit/
#-- and create a desktop entry in /usr/share/applications/ aiming an Desktop Shortcut
#-- OR
#-- It will remove the PyBestfit files from your computer
#--
#-- https://github.com/allexlima/PyBestfit.git
#--

FILE="/tmp/out.$$"
GREP="/bin/grep"

# Check root

if [ "$(id -u)" != "0" ]; then
   echo -e "\n\e[31m--* You must run this setup as root/sudo *-- \033[0m\n" 1>&2
   exit 1
fi

# Init

read -p "Do you want INSTALL or REMOVE PyBestfit? ([i]nstall | [r]emove) : " answer


if echo "$answer" | grep -iq "^i" ;then
    echo -e "\n\033[1;33mInstalling requirements... \033[0m\n"
    apt-get install python-qt4
    echo -e "\n\033[1;33mInstalling PyBestfit... \033[0m\n"
    echo "Creating files directory..."
    mkdir /opt/PyBestfit
    echo "Copying files..."
    cp -Rf . /opt/PyBestfit
    cd /opt/PyBestfit/
    rm interface.py
    mv setup_files/ui_to_opt.py interface.py
    echo "Creating desktop entry..."
    cp -f setup_files/PyBestfit.desktop /usr/share/applications/
    rm -rf setup_files
    echo -e "\n\e[1;34mInstallation done successfully!  \e[0m\n"
    echo -e "\nAccess the README file in https://github.com/allexlima/PyBestfit :)  \n"
elif echo "$answer" | grep -iq "^r" ;then
    cd ~
    echo -e "\n\033[1;33mRemoving PyBestfit... \033[0m\n"
    echo "Removing desktop entry..."
    rm /usr/share/applications/PyBestfit.desktop
    echo "Removing files..."
    rm -rf /opt/PyBestfit
    echo -e "\n\e[1;34mUninstall done successfully!  \e[0m"
    echo -e "\nThank you so much for use PyBestfit! \nhttps://github.com/allexlima/PyBestfit \n"
else
    echo "Error: Invalid parameter"
    exit
fi