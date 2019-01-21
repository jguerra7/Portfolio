#!/bin/bash
#This script is designed to use agains a hashdump from a windows machine
clear

rm -rf /root/.john
read -p "Enter location of wordlist :" wordlist
read -p "Enter loaction of file containing password hash(s) :" list

john --format=NT $list --wordlist=$wordlist
