#!bin/bash

echo "Starting enumeration..."
echo "All info displayed will be saved at the current directory"
sleep 1

touch emumeration_localhost.txt
touch FLAGS.txt

echo "Hostname w/kernel version:"
uname -a
uname -a >> emumeration_localhost.txt
echo "Who's logged in:"
who
who >> emumeration_localhost.txt
echo "Your current user:"
echo $USER 
echo $USER >> emumeration_localhost.txt

echo "Your current ip address:"
ip addr | grep -A 3 eth1 | grep inet


read -p "Enter flag possible name (ex: _flag_[1-100]:" FLAG

echo "Scanning for possible flags"
ps -elf | egrep -i $FLAG >> FLAGS.txt
ps -elf | egrep -i $FLAG
iptables --list | egrep -i $FLAG >> FLAGS.txt
iptables --list | egrep -i $FLAG
crontab -l | egrep -i $FLAG >> FLAGS.txt
crontab -l | egrep -i $FLAG 
find / 2>&1 | egrep -i $FLAG
egrep -ir / -e $FLAG 2>&1

