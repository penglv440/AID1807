# # tcp_server1.py
# from socket import *

# soc= socket(AF_INET, SOCK_STREAM)

# soc.bind(('0.0.0.0',8888))

# soc.listen(10)

# print("It is now waiting connect----")

# confd,attr=soc.accept()

# print("connect successfully,the address is :",attr)


# data=confd.recv(2048).decode()

# print("sever receive data:",data)
# # confd.send("my name is server")
# confd.close()

# soc.close()

from socket import *

s=socket()


# 设置端口立即释放
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

# 获取套接字选项值
# print(s.getsockopt(SQL_SOCKET,SO_REUSEADDR))
# print(s.family)
# print(s.type)
s.bind(('127.0.0.1',22222))
# print(s.getsockname())
s.listen(1024)
while True:
    c,addr=s.accept()
    print(s.fileno())
    print(c.getpeername())
    c.recv()




