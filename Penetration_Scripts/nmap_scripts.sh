#!bin/bash
clear

read -p "Which script would you like to search? (a for all):" var
if [ $var -eq "a" ]
then
	ls -l /usr/share/nmap/scripts
else
	ls -l /usr/share/nmap/scripts | grep -i $var
fi

read -p "Would you like to run a script? (y/n):" ans
if [ $ans = 'y' ]
then
	read -p "Which script would you like to run? (copy and paste):" script
	read -p "Enter ip address of target system:" ip
	nmap --script=$script $ip
else
	break
fi

