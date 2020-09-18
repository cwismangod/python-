'''
    ftp文件服务器
        1. 需求分析
            分为服务端和客户端，要求可以有多个客户端同时操作。
            客户端可以查看服务器文件库中有什么文件。
            客户端可以从文件库中下载文件到本地。
            客户端可以上传一个本地文件到文件库。
            使用print在客户端打印命令输入提示，引导操作

        2. 技术分析
            并发模型 : 多线程
            网络 : tcp
            文件传输 : 读发送 接收写入

        3. 模块划分
            封装结构 : 类封装

            查看文件
            下载文件
            上传文件

        4. 通信协议
                 请求类型       数据参量
            查看   LIST
            下载   STOR        文件名
            上传   RETR        文件名
            退出   EXIT
            允许   OK
            不允许 FAIL

        5. 按照模块设计功能逻辑
            框架结构的搭建
                服务端 : 多线程并发模型
                客户端 : 发起连接
                        print命令提示界面
                        根据输入分情况选择

            查看文件列表
                客户端 : 1. 发起请求
                        2. 等待服务端回复
                        3. 根据回复分情况处理
                            YES 接收文件列表
                            NO  结束
                服务端 : 1. 接收请求 分析请求类型
                        2. 判断能否满足请求
                        3. 根据情况操作
                            YES 发送文件列表
                            NO  结束
'''
from threading import Thread
from socket import *
import sys, os, time

HOST = '0.0.0.0'
PORT = 6666
ADDR = (HOST, PORT)

FTP = 'FTP/'


class FTPServer(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    def do_list(self):
        file_list = os.listdir(FTP)
        if not file_list:
            self.connfd.send(b'FAIL')
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)  # 防止粘包
            # 使用\n做消息边界,拼接文件列表
            data = '\n'.join(file_list)
            self.connfd.send(data.encode())

    # 处理上传
    def do_stor(self, filename):
        if os.path.exists(FTP+filename):
            self.connfd.send(b'FAIL')
            return
        else:
            self.connfd.send(b'OK')
            # 接收文件
            fw = open(FTP+filename,'wb')
            while True:
                data = self.connfd.recv(1024)
                if data == b'##':
                    break
                fw.write(data)
            fw.close()

    #处理下载
    def do_retr(self,filename):
        # 判断本地文件是否存在
        try:
            fr = open(FTP+filename, 'rb')
        except:
            self.connfd.send(b'FAIL')
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1)
            while True:
                data = fr.read(1024 * 10)
                if not data:
                    break
                self.connfd.send(data)
            # 表示文件已经发送结束
            time.sleep(0.1)
            self.connfd.send(b'##')
            fr.close()


    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            tmp = data.split(' ', 1)
            if not data or data == 'EXIT':
                break
            elif data == 'LIST':
                self.do_list()
            elif tmp[0] == 'STOR':
                self.do_stor(tmp[1])
            elif tmp[0] == 'RETR':
                self.do_retr(tmp[1])


        self.connfd.close()


def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)

    while True:
        try:
            connfd, addr = sock.accept()
            print('Connect from', addr)
        except KeyboardInterrupt:
            sys.exit('服务结束')

        t = FTPServer(connfd)
        t.start()


if __name__ == '__main__':
    main()
