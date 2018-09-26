# tcp_client.py
from socket import *
# create client socket 
sockfd=socket(AF_INET,SOCK_STREAM)


# connect:

    # sockfd.close()
while True: 
    server_addr=('127.0.0.1',9999)
    sockfd.connect(server_addr)
# message send and receive

    data=input("发送>>")
    sockfd.send(data.encode())
    data=sockfd.recv(1024)
    if data=="#":
        break    
    print("接收到：",data.decode())

# close socket

sockfd.close()