# UDP Program for Input Data via nework from differnet clients
# importing the module used for UDP Program / Soket Programming

import socket
import os

# For Using UDP Protocol 
protocol=socket.SOCK_DGRAM
# For Network Address Family like IPv4==AF_INET  IPv6
netfam=socket.AF_INET
# Creating a Socket Object
mysocket=socket.socket(netfam,protocol)
# Using Host Ip and Port (Our Ip on which port will be enabled)
ip="192.168.1.20"
port=786

# Binding the ip and port to make a socker 
mysocket.bind((ip,port))
#Os System Commands 
os.system("clear")
os.system("tput setaf 3")
os.system("figlet UDP Program")
os.system("tput setaf 7")

x=input("Enter Your Name :")
print("Your Name is: {0}\nYour ip is: {1} \nUDP on running port: {2}  ".format(x,ip,port))
# Recv From is used to get data via network and the max size here is 1024 bytes
while True:
    y=mysocket.recvfrom(1024)
    addr= y[1][0]
    port= y[1][1]
    message=y[0].decode()
    print(addr + ":" + str(port) + "=" +message)
