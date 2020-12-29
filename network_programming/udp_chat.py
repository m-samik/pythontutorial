# UDP Program for chat via nework from client to client
# importing the module used for UDP Program / Soket Programming

import socket
import os
import threading

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
os.system("figlet UDP Chat")
os.system("tput setaf 1")
print("\t\tVersion : 1.1 by Muhammad Sami")
os.system("tput setaf 7")
print("\n1. Chat with End User \n2. Group Chat \n3. Exit")
option=int(input("Enter Your Choice : "))

# Functions for Sender and Reciever

def sender():
    ip_send=input("Enter the IP of Ender User :")
    port_send=int(input("Enter the Port of End User : "))
    while True:
        message_send=input("\n\t\t\t\t\tMesssage : ")
        message_send=message_send.encode()
        mysocket.sendto(message_send,(ip_send,port_send))

def reciever():
    while True:
        y=mysocket.recvfrom(1024)
        addr= y[1][0]
        port= y[1][1]
        message=y[0].decode()
        # Recv from is used to get data via network and the max size here is 1024 bytes
        print("Message Recieved : {}\n".format(message))

x1=threading.Thread(target=sender)
x2=threading.Thread(target=reciever)
if option==1:
            x1.start()
            x2.start()
elif option==2:
    print("Group Chat")
    while True:
        y=mysocket.recvfrom(1024)
        addr= y[1][0]
        port= y[1][1]
        message=y[0].decode()
        # Recv from is used to get data via network and the max size here is 1024 bytes
        print("{0}: {1}\n".format(addr,message))
elif option==3:
    exit()
