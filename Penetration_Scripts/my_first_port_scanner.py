#This is my first port scanner. I plan on making improvements with more advance features.

import socket

print ('Welcome to the Python3 port scanner!')
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input("Enter ip address for port scan :")
port = [20,21,22,23,80,135,139,445]

def pscan(port):
    try:
        sk.connect((ip,port))
        return True
    except:
        return False

for i in port:
    if pscan(i):
        print('PORT',i,'IS OPEN!')
    else:
        print('port',i,'PWND!')
