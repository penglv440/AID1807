# ftp_client1.py
from socket import *
import os,sys,time

#基本文件操作功能


class FtpClient(object):
    def __init__(self,sockfd):
        self.sockfd=sockfd
        self.FILE_PATH='/home/tarena/pythonNet/'
    def do_list(self):
        self.sockfd.send(b"L") #发送请求 
        # print("消息已经发送")
        #等待回复
        data=self.sockfd.recv(1024).decode()

        # print(data)
        if data=="OK":
            data=self.sockfd.recv(4096).decode()
            files=data.split("#")
            for file in files:
                print(file)
            print("文件展示完毕")
        else:
            #由服务器发送是失败的原因
            print(data)
    def do_get(self,filename):
        self.sockfd.send(('G '+ filename).encode())
        data=self.sockfd.recv(1024).decode()
        if data=="OK":
            fd=open(filename,'wb')
            while True:
                data=self.sockfd.recv(1024)
                if data==b'##':
                    break
                fd.write(data)
            fd.close()

            print("%s下载完毕\n"%filename)   

    #上传文件
    def do_put(self,filename):
        files=os.listdir(self.FILE_PATH)
        print(files)
        filename=input("which file you want to put:")
        # 如果要上传的文件存在
        if filename in files:
            self.sockfd.send(filename.encode())
            try:
                fd=open(filename,'rb')
                while True:
                    data=self.sockfd.read(1024)
                    if not data:
                        break
                    self.sockfd.send(data.encode())
                fd.close()
            except:
                print("error")
                return 
        else:
            print("您输入的文件名不存在")


        
       

            



    def do_quit(self):
        self.sockfd.send(b'Q')

    def do_put_file():
        pass


#网络链接 
def main():
    if len(sys.argv)<3:
        print("argv is error")
        return
    HOST=sys.argv[1]
    PORT=int(sys.argv[2])
    ADDR=(HOST,PORT)

    sockfd=socket()
    try:
        sockfd.connect(ADDR)
    except:
        print("链接服务器失败")
        return  
    ftp=FtpClient(sockfd) #功能类对象
    while True:
        print("＋＋＋＋＋命令选项＋＋＋＋＋＋+++")
        print("*************list************")
        print("*************get file********")
        print("*************put file********")
        print("*************quit*************")
        print("+++++++++++++++++++++++++++++")
        cmd=input("请输入命令>>")
        if cmd.strip()=='list':
            # print("ceshi")
            ftp.do_list()
        elif cmd[:3]=="get":
            filename=cmd.split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3]=="put": 
            filename=cmd.split(' ')[-1]
            ftp.do_put(filename)
            
        elif cmd.strip()=="quit":
            ftp.do_quit()
            sockfd.close()
            sys.exit("谢谢使用")
        else:
            pint("请输入正确的命令")
            continue 



if __name__=="__main__":
    main()