#!/bin/bash
#Simple script to transfer files to your target via ssh


read -p "Enter name of file:" file
read -p "Enter name of user:" user
read -p "Enter ip address of user:" ip
read -p "Enter file location:" location

scp $file $user@$ip:$location
