from socket import *

soc=socket(AF_INET,SOCK_STREAM)

soc.bind(('0.0.0.0',10000))

soc.listen(10)

print("It is now  connecting----")
socfd,addr=soc.accept()
print("connected---")
data=socfd.recv(1024).decode()
print("************data:",data)

# open file 
try:
        f= open('server.txt','rb')
        s=f.read(1024)
        socfd.send(s.encode())
        f.close()
        
except OSError:
    print("server打开文件失败")

socfd.close()
soc.close()

