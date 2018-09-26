# tcp_client1.py
from socket import  *

soc=socket(AF_INET,SOCK_STREAM)


server_addr=('127.0.0.1',8888)
soc.connect(server_addr)



 

n1=input("please input a message:")

data=soc.recv(1024)
print("receive your message:",data)
n=soc.send(n1)
soc.close()