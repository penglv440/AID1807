from socket import *
# create a socket
sockfd = socket.socket(AF_INET, SOCK_STREAM)
# bind address
sockfd.bind(('0.0.0.0', 9999))
# set linsten
sockfd.listen(10)
# wait receive connect
print("waiting for connect----------------------")
while True: 
    connfd, addr = sockfd.accept()
    print("connect from :", addr)
# print("connect socket---", connfd)
# receive and send message:------------ab'-------------

    data = connfd.recv(1024).decode() 
    print(data)
    # n = connfd.send(b' -------- wenjiang hello boy-----')
connfd.close()
sockfd.close()
