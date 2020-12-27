import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip="192.168.1.20"
port=786
message=input("Enter Your Message : ")
message=message.encode()
print("Destination Ip : {0}\nDestination Port :{1}\nYour Message : {2}".format(ip,port,message))
s.sendto(message ,(ip,port))
print("Task Executed Successfully")