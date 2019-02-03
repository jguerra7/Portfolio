#This is my first port scanner. I plan on making improvements with more advance features.

import socket

print ('Welcome to the Python3 port scanner!')
tcp_connect = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
udp_connect = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port_input = int(input("Enter number of ports you with to scan :"))
port1 = range(1,port_input+1)
ip = input("Enter ip address you wish to scan :")

def tcp_port_scan(port):
    try:
        con = tcp_connect.connect((ip,port))
        return True
    except:
        return False

for i in port1:
    if tcp_port_scan(i):
        print("Port ",i," is OPEN!")
