#!/bin/bash
clear

rm -rf /root/.john
read -p "Enter location of wordlist :" wordlist
read -p "Enter location of file containing password hash(s):" list

john --wordlist=$wordlist $list
